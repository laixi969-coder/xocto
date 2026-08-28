"""跨媒体新闻搜索发现。

固定 RSS 适合已知媒体，但发现未知产品还需要横跨媒体的查询。这里使用公开
新闻搜索 RSS；Adapter 只忠实保存标题、摘要、链接和出处，不判断它最终是
产品、公司 AI 改造还是纯市场变化。
"""

from __future__ import annotations

import hashlib
import html
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

from ..models import RawItem, now_iso
from .base import Http, HttpError, register, to_iso

SEARCH_URL = "https://news.google.com/rss/search"
_TAG = re.compile(r"<[^>]+>")


def _published(value: str) -> datetime | None:
    try:
        return parsedate_to_datetime(value).astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def _clean(value: str) -> str:
    return " ".join(html.unescape(_TAG.sub(" ", value or "")).split())


@register("newssearch")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    lookback = float(cfg.get("lookback_hours") or 72)
    since = datetime.now(timezone.utc) - timedelta(hours=lookback)
    per_query = int(cfg.get("max_results_per_query") or 30)
    collected = now_iso()
    rows: list[RawItem] = []
    seen: set[str] = set()

    for spec in cfg.get("queries") or []:
        if not isinstance(spec, dict):
            continue
        name = str(spec.get("name") or "未命名查询").strip()
        query = str(spec.get("query") or "").strip()
        if not query:
            continue
        params = {
            "q": query,
            "hl": str(spec.get("hl") or "en-US"),
            "gl": str(spec.get("gl") or "US"),
            "ceid": str(spec.get("ceid") or "US:en"),
        }
        try:
            root = ET.fromstring(http.get_text(SEARCH_URL, params=params))
        except (ET.ParseError, OSError, HttpError) as exc:
            print(f"    ! 新闻搜索「{name}」失败：{exc}")
            continue
        accepted = 0
        for item in root.findall("./channel/item"):
            raw_title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            source_el = item.find("source")
            publisher = (source_el.text or "").strip() if source_el is not None else ""
            # Google News RSS 会把媒体名追加为 “标题 - Publisher”。媒体载体
            # 不属于实体标题；剥掉后可与该媒体的原生 RSS 做跨源标题去重。
            suffix = f" - {publisher}" if publisher else ""
            title = raw_title[:-len(suffix)].strip() if suffix and raw_title.endswith(suffix) else raw_title
            if not title or not link or link in seen:
                continue
            published = _published((item.findtext("pubDate") or "").strip())
            if published is not None and published < since:
                continue
            external_id = hashlib.sha1(link.encode("utf-8")).hexdigest()[:20]
            rows.append(RawItem(
                source="newssearch",
                external_id=external_id,
                title=title,
                url=link,
                summary=_clean(item.findtext("description") or ""),
                published_at=to_iso(published) if published else "",
                collected_at=collected,
                metrics={},
                extra={
                    "kind": "news",
                    "official": False,
                    "publisher": publisher,
                    "query_lane": name,
                    # 查询语言是发现覆盖，不等于产品已在该市场形成供给。
                    "content_ecosystem": str(spec.get("ecosystem") or ""),
                    "search_market": str(spec.get("market") or ""),
                },
                payload={"query": query, "publisher": publisher},
            ))
            seen.add(link)
            accepted += 1
            if accepted >= per_query:
                break
        print(f"    [{name}] {accepted} 条")
    return rows
