"""Tech.eu open funding API: preserve facts, currency, round identity and provenance."""

from __future__ import annotations

from datetime import timedelta
from urllib.parse import urljoin

from ..models import RawItem, now_iso, today
from ..funding import FundingRound
from .base import Http, register

BASE = "https://funding.tech.eu"


@register("techfunding")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    end = today()
    start = end - timedelta(days=max(1, int(cfg.get("lookback_days", 30))) - 1)
    params = {"sector": "AI", "from": start.isoformat(), "to": end.isoformat(), "limit": 100}
    limit = max(1, int(cfg.get("max_rounds", 100)))
    rows: dict[str, dict] = {}
    cursors: set[str] = set()
    for _ in range(max(1, int(cfg.get("max_pages", 3)))):
        data = http.get_json(f"{BASE}/api/v1/rounds", params=params)
        if not isinstance(data, dict) or not isinstance(data.get("data"), list):
            raise ValueError("Funding API response has no data array")
        for row in data["data"]:
            if isinstance(row, dict) and row.get("id") and row.get("company", {}).get("id"):
                rows[str(row["id"])] = row
        cursor = data.get("nextCursor")
        if not cursor or cursor in cursors or len(rows) >= limit:
            break
        cursors.add(cursor)
        params = {**params, "after": cursor}

    companies: dict[str, dict] = {}
    stamp = now_iso()
    items = []
    for row in list(rows.values())[:limit]:
        company_id = row["company"]["id"]
        if company_id not in companies:
            try:
                company = http.get_json(f"{BASE}/api/v1/companies/{company_id}")
                if not isinstance(company, dict) or company.get("id") != company_id:
                    raise ValueError("Funding company identity mismatch")
                companies[company_id] = company
            except Exception as exc:
                # Financing remains usable when an individual company profile is unavailable.
                print(f"    ! {row['company']['name']} profile: {exc}")
                companies[company_id] = row["company"]
        company = companies[company_id]
        payload = {"round": row, "company": company}
        # Fail within the source boundary if the upstream schema changes,
        # rather than crashing the later merge for every other source.
        FundingRound.from_payload(payload)
        items.append(RawItem(
            source="techfunding", external_id=row["id"], title=row["company"]["name"],
            url=urljoin(BASE, row["url"]), summary=str(company.get("description") or ""),
            published_at=f"{row['date']}T00:00:00Z", collected_at=stamp,
            metrics={}, extra={"kind": "funding", "publisher": "Tech.eu Funding Explorer"},
            payload=payload,
        ))
    return items
