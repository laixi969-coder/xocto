"""RSS / Atom 更新：公司一手发布，以及独立作者与公开平台的观察。

全部按报道载体处理并进入统一发现候选池。公司源标 official=true，独立作者与
平台标 false；后续解释层再判断其对象是实体、市场背景还是无效信号。站点上
不出现这些源的名字。"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import hashlib
import html
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

from ..models import RawItem, now_iso
from .base import Http, HttpError, parse_iso, register, to_iso

_TAG = re.compile(r"<[^>]+>")
DEFAULT_LOOKBACK_HOURS = 72
DEFAULT_MAX_PARALLEL_FEEDS = 6
ATOM = "{http://www.w3.org/2005/Atom}"


def _fetch(cfg: dict, http: Http, *, source: str, default_official: bool) -> list[RawItem]:
    feeds = cfg.get("feeds") or []
    lookback = float(cfg.get("lookback_hours") or DEFAULT_LOOKBACK_HOURS)
    since = datetime.now(timezone.utc) - timedelta(hours=lookback)
    collected = now_iso()
    items: list[RawItem] = []
    seen: set[str] = set()

    specs = [spec for spec in feeds if isinstance(spec, dict)]
    max_workers = max(
        1, min(int(cfg.get("max_parallel_feeds") or DEFAULT_MAX_PARALLEL_FEEDS), len(specs) or 1)
    )
    # 源彼此独立：并行让一两个慢源不会占满每日发布窗口。map 按配置顺序返回，
    # 所以原始存档和日报仍然可复现，不会因网络快慢改变顺序。
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(
            lambda spec: _fetch_feed(spec, http, source, default_official, since, collected), specs
        )
        for name, rows, error in results:
            if error:
                print(f"    ! 源「{name}」解析失败：{error}")
                continue
            count = 0
            for item in rows:
                if item.external_id in seen:
                    continue
                seen.add(item.external_id)
                items.append(item)
                count += 1
            print(f"    [{name}] {count} 条")
    return items


def _fetch_feed(
    spec: dict, http: Http, source: str, default_official: bool, since: datetime, collected: str
) -> tuple[str, list[RawItem], str]:
    name = str(spec.get("name") or "").strip()
    url = str(spec.get("url") or "").strip()
    official = default_official if "official" not in spec else bool(spec.get("official"))
    if not name or not url:
        return name or "未命名", [], "缺少 name 或 url"
    try:
        root = ET.fromstring(http.get_text(url))
    except (ET.ParseError, OSError, HttpError) as exc:
        return name, [], str(exc)

    rows: list[RawItem] = []
    for row in _entries(root):
        item = _parse_entry(row, name, collected, source=source, official=official)
        if item is None:
            continue
        published = parse_iso(item.published_at)
        if published is not None and published >= since:
            rows.append(item)
    return name, rows, ""


@register("officialfeeds")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    """公司、基础设施与模型方的一手更新。"""
    return _fetch(cfg, http, source="officialfeeds", default_official=True)


@register("marketfeeds")
def fetch_market(cfg: dict, http: Http) -> list[RawItem]:
    """独立研究、开发者观察与行业媒体；与公司公告分开计数和健康检查。"""
    return _fetch(cfg, http, source="marketfeeds", default_official=False)


def _entries(root: ET.Element) -> list[ET.Element]:
    return root.findall(".//item") or root.findall(f".//{ATOM}entry")


def _parse_entry(
    entry: ET.Element, publisher: str, collected: str, *, source: str, official: bool = True
) -> RawItem | None:
    atom = entry.tag == f"{ATOM}entry"
    title = _text(entry.find(f"{ATOM}title" if atom else "title"))
    link = ""
    if atom:
        for candidate in entry.findall(f"{ATOM}link"):
            if candidate.get("rel", "alternate") == "alternate":
                link = candidate.get("href") or ""
                break
        if not link:
            first = entry.find(f"{ATOM}link")
            link = (first.get("href") if first is not None else "") or ""
    else:
        link_el = entry.find("link")
        link = _text(link_el) or (link_el.get("href") if link_el is not None else "")
    if not title or not link:
        return None
    published = _date(_text(entry.find(f"{ATOM}published" if atom else "pubDate")) or _text(entry.find(f"{ATOM}updated" if atom else "date")))
    summary = _clean(_text(entry.find(f"{ATOM}summary" if atom else "description")) or _text(entry.find(f"{ATOM}content")))
    external_id = hashlib.sha1(link.encode("utf-8")).hexdigest()[:20]
    return RawItem(
        source=source,
        external_id=external_id,
        title=title,
        url=link,
        summary=summary,
        published_at=to_iso(published) if published else "",
        collected_at=collected,
        metrics={},
        extra={"kind": "news", "publisher": publisher, "official": official},
        payload={"publisher": publisher, "link": link},
    )


def _text(element: ET.Element | None) -> str:
    return "" if element is None or element.text is None else element.text.strip()


def _clean(value: str) -> str:
    return html.unescape(_TAG.sub(" ", value)).strip()


def _date(value: str) -> datetime | None:
    parsed = parse_iso(value)
    if parsed is not None:
        return parsed
    try:
        return parsedate_to_datetime(value).astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None
