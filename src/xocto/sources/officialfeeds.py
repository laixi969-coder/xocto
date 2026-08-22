"""RSS / Atom 更新：公司一手发布，以及独立作者与公开平台的观察。

全部按新闻处理，不进产品池。公司源标 official=true，独立作者与平台标 false。
站点上不出现这些源的名字。"""

from __future__ import annotations

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
ATOM = "{http://www.w3.org/2005/Atom}"


@register("officialfeeds")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    feeds = cfg.get("feeds") or []
    lookback = float(cfg.get("lookback_hours") or DEFAULT_LOOKBACK_HOURS)
    since = datetime.now(timezone.utc) - timedelta(hours=lookback)
    collected = now_iso()
    items: list[RawItem] = []
    seen: set[str] = set()

    for spec in feeds:
        if not isinstance(spec, dict):
            continue
        name = str(spec.get("name") or "").strip()
        url = str(spec.get("url") or "").strip()
        official = True if "official" not in spec else bool(spec.get("official"))
        if not name or not url:
            continue
        try:
            root = ET.fromstring(http.get_text(url))
        except (ET.ParseError, OSError, HttpError) as exc:
            print(f"    ! 源「{name}」解析失败：{exc}")
            continue
        count = 0
        for row in _entries(root):
            item = _parse_entry(row, name, collected, official=official)
            if item is None or item.external_id in seen:
                continue
            published = parse_iso(item.published_at)
            if published is None or published < since:
                continue
            seen.add(item.external_id)
            items.append(item)
            count += 1
        print(f"    [{name}] {count} 条")
    return items


def _entries(root: ET.Element) -> list[ET.Element]:
    return root.findall(".//item") or root.findall(f".//{ATOM}entry")


def _parse_entry(
    entry: ET.Element, publisher: str, collected: str, *, official: bool = True
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
        source="officialfeeds",
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
