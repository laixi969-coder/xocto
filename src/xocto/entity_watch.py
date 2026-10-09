"""Explicit, reviewed product identities; no popularity inference or fuzzy name merging."""

from __future__ import annotations

import re
from dataclasses import replace
from urllib.parse import urlsplit

from .dedupe import canonical_url
from .models import RawItem


def annotate(item: RawItem, specs: list[dict]) -> RawItem:
    # Only the title establishes subject identity. Summary mentions of rivals
    # must not attach an unrelated company report to a watched product.
    text = item.title
    matched = []
    excluded_urls = set(item.extra.get("excluded_entity_urls") or [])
    for spec in specs:
        website = str(spec.get("url") or "")
        direct = website and canonical_url(item.url) == canonical_url(website)
        patterns = spec.get("patterns") or []
        excluded = any(re.search(pattern, text, re.I) for pattern in spec.get("exclude") or [])
        if excluded and not direct:
            excluded_urls.add(website)
        issuer = urlsplit(item.url).hostname in (spec.get("issuer_hosts") or [])
        owned_mention = issuer and any(re.search(r"(?<!\w)" + re.escape(alias) + r"(?!\w)", text, re.I) for alias in spec.get("aliases") or [])
        if not direct and not owned_mention and item.extra.get("kind") != "news":
            continue
        if direct or (not excluded and (owned_mention or any(re.search(pattern, text, re.I) for pattern in patterns))):
            matched.append(spec)
    if len(matched) > 1:
        # A comparison headline belongs to multiple subjects. Preserve the
        # ambiguity so the weak-name fallback cannot choose just one of them.
        excluded_urls.update(spec["url"] for spec in matched)
    if len(matched) != 1:
        return replace(item, extra={**item.extra, "excluded_entity_urls": sorted(excluded_urls)}) if excluded_urls else item
    spec = matched[0]
    return replace(item, extra={**item.extra,
        "verified_entity_url": spec["url"], "verified_entity_name": spec["name"],
        "priority_review": bool(spec.get("priority_review", True)),
    })
