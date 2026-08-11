"""Product Hunt AI 分类 feed。

feed 是 Atom 格式，每次约 50 条。注意两个坑：
1. feed 按 updated 排序，里面混着几周前发布、最近才有新评论的老产品。
   所以按 published 过滤，不按 feed 顺序。
2. feed 不给票数，也不给产品官网（只给 PH 的跳转链接）。
   热度和官网留到深挖阶段补 —— 采集阶段不做多余的网络请求。
"""

from __future__ import annotations

import html
import re
import xml.etree.ElementTree as ET

from ..models import RawItem, now_iso
from .base import Http, HttpError, hours_since, register, to_iso, parse_iso

ATOM = "{http://www.w3.org/2005/Atom}"

DEFAULT_FEED = "https://www.producthunt.com/feed?category=ai"
DEFAULT_LOOKBACK_HOURS = 48

# PH 的 content 里第一个 <p> 是 tagline，后面跟着 Discussion / Link 两个链接
_FIRST_P = re.compile(r"<p>(.*?)</p>", re.S | re.I)
_TAG = re.compile(r"<[^>]+>")
_POST_ID = re.compile(r"Post/(\d+)")


@register("producthunt")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    feed_url = cfg.get("feed_url") or DEFAULT_FEED
    lookback = float(cfg.get("lookback_hours") or DEFAULT_LOOKBACK_HOURS)

    xml_text = http.get_text(feed_url)
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        raise HttpError(f"Product Hunt feed 不是合法 XML: {exc}") from exc

    collected = now_iso()
    items: list[RawItem] = []
    skipped_old = 0

    for entry in root.findall(f"{ATOM}entry"):
        parsed = _parse_entry(entry, collected)
        if parsed is None:
            continue

        age = hours_since(parsed.published_at)
        if age is not None and age > lookback:
            skipped_old += 1
            continue

        items.append(parsed)

    if skipped_old:
        print(f"    （跳过 {skipped_old} 条超出 {lookback:.0f} 小时窗口的旧条目）")
    return items


def _parse_entry(entry: ET.Element, collected: str) -> RawItem | None:
    """解析单个 entry。缺关键字段就返回 None，不让半条数据污染下游。"""
    title = _text(entry.find(f"{ATOM}title"))
    if not title:
        return None

    raw_id = _text(entry.find(f"{ATOM}id"))
    match = _POST_ID.search(raw_id)
    external_id = match.group(1) if match else raw_id
    if not external_id:
        return None

    url = ""
    for link in entry.findall(f"{ATOM}link"):
        if link.get("rel") == "alternate":
            url = link.get("href") or ""
            break
    if not url:
        return None

    published = parse_iso(_text(entry.find(f"{ATOM}published")))
    updated = parse_iso(_text(entry.find(f"{ATOM}updated")))

    author = ""
    author_el = entry.find(f"{ATOM}author")
    if author_el is not None:
        author = _text(author_el.find(f"{ATOM}name"))

    return RawItem(
        source="producthunt",
        external_id=external_id,
        title=title,
        url=url,
        summary=_tagline(_text(entry.find(f"{ATOM}content"))),
        published_at=to_iso(published) if published else "",
        collected_at=collected,
        # feed 不提供票数。留空 dict 而不是编造字段。
        metrics={},
        extra={
            # 各源统一用 builder 这个键放"人"，下游不用管来自哪个源。
            # 注意 PH 的提交者未必是创始人，深挖阶段要核实。
            "builder": author,
            "submitter": author,
            "updated_at": to_iso(updated) if updated else "",
            # 这个链接会 302 到产品真实官网，深挖阶段用
            "outbound_url": f"https://www.producthunt.com/r/p/{external_id}",
        },
        payload={"atom_entry": ET.tostring(entry, encoding="unicode")},
    )


def _text(el: ET.Element | None) -> str:
    return (el.text or "").strip() if el is not None else ""


def _tagline(content: str) -> str:
    """从 content 的 HTML 里抠出第一段作为简介。"""
    if not content:
        return ""
    unescaped = html.unescape(content)
    match = _FIRST_P.search(unescaped)
    text = match.group(1) if match else unescaped
    return " ".join(_TAG.sub("", text).split())
