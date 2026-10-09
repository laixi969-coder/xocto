"""Public US funding news candidates; entity, geography and AI relevance remain editorial."""

from __future__ import annotations

import hashlib
import re
import xml.etree.ElementTree as ET
from datetime import timedelta

from ..models import RawItem, now_iso, today
from ..page_text import PageText
from .base import Http, register, to_iso
from .officialfeeds import _date


@register("usfunding")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    since = today() - timedelta(days=max(1, int(cfg.get("lookback_days", 30))))
    items, seen, failures = [], set(), []
    stamp = now_iso()
    for spec in cfg.get("feeds") or []:
        try:
            root = ET.fromstring(http.get_text(spec["url"]))
        except Exception as exc:
            failures.append(spec["name"])
            print(f"    ! {spec['name']}: {type(exc).__name__}: {exc}")
            continue
        count = 0
        for entry in root.findall("./channel/item"):
            title, url = entry.findtext("title") or "", entry.findtext("link") or ""
            published = _date(entry.findtext("pubDate") or "")
            parsed = published
            if not title or not url or url in seen or not parsed or parsed.date() < since:
                continue
            body = entry.findtext("{http://purl.org/rss/1.0/modules/content/}encoded") or entry.findtext("description") or ""
            page = PageText(); page.feed(body)
            text = " ".join(page.parts)[:16000]
            categories = [row.text or "" for row in entry.findall("category")]
            # Lexical retrieval only; deals, fund raises, rumours and non-US
            # companies are all retained for the model to distinguish.
            if not re.search(r"funding|raised?|raises|financing|series [a-z]|seed|lands|nabs|invest", title + " " + text, re.I):
                continue
            ident = hashlib.sha1(url.encode()).hexdigest()[:20]
            items.append(RawItem(
                source="usfunding", external_id=ident, title=title, url=url,
                summary=" ".join(text.split()[:160]), published_at=to_iso(published), collected_at=stamp,
                metrics={}, extra={"kind": "funding_news", "publisher": spec["name"]},
                payload={"text": text, "categories": categories,
                         "links": list(dict.fromkeys(re.findall(r'href=["\'](https?://[^"\']+)', body))),
                         "feed": spec["url"]},
            ))
            seen.add(url); count += 1
        print(f"    [{spec['name']}] {count} financing candidates")
    if failures and not items:
        raise ValueError("All US funding feeds failed: " + ", ".join(failures))
    return items
