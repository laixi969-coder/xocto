"""Fetch explicitly tracked official product pages as independent discovery evidence."""

from __future__ import annotations

import hashlib

from ..page_text import PageText
from ..models import RawItem, now_iso
from .base import Http, register


@register("trackedproducts")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    stamp = now_iso()
    items, failures = [], []
    for spec in cfg.get("products") or []:
        try:
            page = PageText(); page.feed(http.get_text(spec["url"]))
            text = " ".join(page.parts)
            if len(text) < 60:
                raise ValueError("Official page has insufficient readable product information")
            digest = hashlib.sha256(text.encode()).hexdigest()[:16]
            items.append(RawItem(
                source="trackedproducts", external_id=f"{spec['slug']}:{digest}",
                title=spec["name"], url=spec["url"], summary=text[:3500],
                published_at="", collected_at=stamp,
                metrics={"content_hash": digest},
                extra={"kind": "product", "official": True, "priority_review": True,
                       "verified_entity_slug": spec["slug"],
                       "verified_entity_url": spec["url"], "verified_entity_name": spec["name"]},
                payload={"website": spec["url"], "content_hash": digest},
            ))
        except Exception as exc:
            failures.append(spec.get("name", "Unknown"))
            print(f"    ! {spec.get('name')}: {type(exc).__name__}: {exc}")
    if failures and not items:
        raise ValueError("All tracked official pages failed: " + ", ".join(failures))
    return items
