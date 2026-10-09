"""Funding facts and bilingual editorial views, independent of product maturity."""

from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass
from datetime import date
from urllib.parse import urljoin, urlsplit
from uuid import UUID
import yaml

from .i18n import Locale
from .models import RawItem, slugify, today
from .store import Store, _atomic_write

BASE = "https://funding.tech.eu"
SECTIONS = ("product", "customer", "workflow", "business_model", "traction", "moat", "funding_read", "risks", "takeaway", "watch_next")


def safe_url(value: str) -> str:
    parts = urlsplit(str(value or ""))
    return value if parts.scheme in {"http", "https"} and parts.hostname and not parts.username else ""


def company_url(value: str) -> str:
    from .official_links import THIRD_PARTY_HOSTS
    url = safe_url(value)
    host = (urlsplit(url).hostname or "").removeprefix("www.").rstrip(".")
    if not host or any(host == name or host.endswith("." + name) for name in THIRD_PARTY_HOSTS | {"cbinsights.com"}):
        return ""
    return url


def amount(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value) if math.isfinite(value) and value >= 0 else None


@dataclass(frozen=True)
class FundingRound:
    id: str
    company_id: str
    name: str
    day: str
    country: str
    stage: str
    raw_stage: str
    eur: float | None
    native: float | None
    currency: str
    investors: tuple[str, ...]
    confidence: str
    website: str
    description: str
    payload: dict

    @property
    def slug(self) -> str:
        return f"{slugify(self.name)}-{self.company_id[:8].lower()}"

    @property
    def url(self) -> str:
        return safe_url(self.payload.get("source_url") or "") or f"{BASE}/deals/{self.id}"

    @property
    def publisher(self) -> str:
        return str(self.payload.get("publisher") or "Tech.eu Funding Explorer")

    @property
    def fingerprint(self) -> str:
        facts = {"round": self.payload["round"], "company": {
            key: self.payload["company"].get(key) for key in ("name", "description", "website")
        }}
        return hashlib.sha256(json.dumps(facts, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

    @classmethod
    def from_payload(cls, payload: dict) -> FundingRound:
        row, company = payload["round"], payload["company"]
        UUID(row["id"])
        UUID(row["company"]["id"])
        day = date.fromisoformat(row["date"][:10]).isoformat()
        return cls(
            id=row["id"], company_id=row["company"]["id"], name=row["company"]["name"],
            day=day, country=str(row["company"].get("country") or ""),
            stage=str(row.get("stage") or "Other"), raw_stage=str(row.get("rawRoundType") or ""),
            eur=amount(row.get("amountEur")), native=amount(row.get("amountNative")),
            currency=str(row.get("currency") or ""), investors=tuple(row.get("investors") or ()),
            confidence=str(row.get("confidence") or "none"), website=company_url(company.get("website") or ""),
            description=str(company.get("description") or ""), payload=payload,
        )


def save_rounds(store: Store, items: list[RawItem], *, dry_run: bool = False) -> None:
    for item in items:
        if item.extra.get("kind") != "funding":
            continue
        record = FundingRound.from_payload(item.payload)
        if not dry_run:
            path = store.data_dir / "funding" / "rounds" / f"{record.id}.json"
            content = json.dumps(item.payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                _atomic_write(path, content)


def read_rounds(store: Store, *, as_of: date | None = None) -> list[FundingRound]:
    end = (as_of or today()).isoformat()
    rounds = []
    for path in sorted((store.data_dir / "funding" / "rounds").glob("*.json")):
        record = FundingRound.from_payload(json.loads(path.read_text(encoding="utf-8")))
        if record.day <= end:
            rounds.append(record)
    return sorted(rounds, key=lambda r: (r.day, r.id), reverse=True)


def analysis_path(store: Store, record: FundingRound):
    return store.data_dir / "funding" / "analysis" / f"{record.company_id}.json"


def read_analysis(store: Store, record: FundingRound) -> dict:
    path = analysis_path(store, record)
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def validate_analysis(result: dict, record: FundingRound) -> dict:
    """Validate identity, both editions and citations before any write."""
    if not isinstance(result, dict) or result.get("company_id") != record.company_id:
        raise ValueError("Funding analysis company identity mismatch")
    allowed = {record.url, record.website}
    if record.publisher == "Tech.eu Funding Explorer":
        allowed.add(f"{BASE}/companies/{record.company_id}")
    allowed.update(safe_url(item.get("url") or "") for item in result.get("evidence", []) if isinstance(item, dict) and item.get("status", "retrieved") == "retrieved")
    first_party = {item.get("url") for item in result.get("evidence", []) if isinstance(item, dict)
                   and item.get("kind") == "company_claim" and item.get("status", "retrieved") == "retrieved"
                   and len(item.get("text", "").strip()) >= 180}
    if result.get("research_version", 0) >= 2 and not first_party:
        raise ValueError("Funding product research needs retrieved first-party evidence")
    for key in ("zh", "en"):
        edition = result.get(key)
        if not isinstance(edition, dict):
            raise ValueError(f"Missing funding analysis edition: {key}")
        for field in ("summary", "judgment", "replaces", "segment", *SECTIONS):
            text = edition.get(field)
            if not isinstance(text, str) or not text.strip():
                raise ValueError(f"Missing funding analysis field: {key}.{field}")
            if key == "en" and re.search(r"[一-鿿]", text.replace(record.name, "")):
                raise ValueError(f"Untranslated funding analysis field: {field}")
        citations = edition.get("citations")
        if not isinstance(citations, list) or not citations:
            raise ValueError("Funding analysis requires citations")
        for citation in citations:
            if not isinstance(citation, dict) or not citation.get("label") or not safe_url(citation.get("url", "")) or citation["url"] not in allowed:
                raise ValueError("Funding analysis has an unsupported citation")
        if result.get("research_version", 0) >= 2 and not any(c.get("url") in first_party for c in citations):
            raise ValueError("Product analysis must cite first-party product evidence")
    return result


def save_analysis(store: Store, record: FundingRound, result: dict) -> None:
    validate_analysis(result, record)
    _atomic_write(analysis_path(store, record), json.dumps(result, ensure_ascii=False, indent=2) + "\n")


def money_label(value: float | None, currency: str, locale: Locale) -> str:
    if value is None:
        return locale.t["funding"]["undisclosed"]
    prefix = {"EUR": "€", "USD": "$", "GBP": "£"}.get(currency, f"{currency} ")
    if value >= 1_000_000_000:
        return f"{prefix}{value / 1_000_000_000:,.2f}B"
    if value >= 1_000_000:
        return f"{prefix}{value / 1_000_000:,.2f}M"
    return f"{prefix}{value:,.0f}"


def funding_context(store: Store, locale: Locale) -> dict:
    rounds = read_rounds(store)
    official_config = store.config_dir / "funding-research.yaml"
    reviewed_sites = (yaml.safe_load(official_config.read_text()) or {}).get("companies", {}) if official_config.exists() else {}
    views, companies = [], {}
    t = locale.t["funding"]
    for record in rounds:
        analysis = read_analysis(store, record)
        edition = analysis.get(locale.key) or {}
        profile_path = store.data_dir / "funding" / "profiles" / f"{record.company_id}.json"
        profile = json.loads(profile_path.read_text(encoding="utf-8")) if profile_path.exists() else {}
        summary = edition.get("summary") or profile.get(locale.key) or (record.description if locale.key == "en" else "")
        from .funding_research import read_state
        research_state = read_state(store, record)
        evidence_pages = [{"url": e["url"], "role": t["evidence_roles"].get(e.get("role"), t["evidence_roles"]["overview"])}
                          for e in research_state.get("evidence", []) if e.get("kind") == "company_claim" and e.get("status") == "retrieved"]
        view = {
            "slug": record.slug, "name": record.name, "day": record.day,
            "country": t["countries"].get(record.country, record.country),
            "country_key": record.country, "stage": t["stages"].get(record.stage, record.stage),
            "stage_key": record.stage, "amount": money_label(record.eur if record.eur is not None else record.native, "EUR" if record.eur is not None else record.currency, locale),
            "amount_value": record.eur if record.eur is not None else record.native,
            "amount_currency": "EUR" if record.eur is not None else record.currency,
            "market": "US" if record.country == "United States" else "Europe",
            "native": money_label(record.native, record.currency, locale) if record.eur is not None and record.currency and record.currency != "EUR" else "",
            "investors": record.investors, "url": record.url,
            "website": company_url((reviewed_sites.get(record.company_id) or {}).get("website") or record.website),
            "confidence": t["confidence_labels"].get(record.confidence, t["confidence_labels"]["none"]),
            "summary": summary,
            "publisher": record.publisher,
            "evidence_pages": evidence_pages,
            "research_gaps": [t["evidence_roles"].get(gap, gap) for gap in research_state.get("gaps", [])],
            "research_attempt": research_state.get("last_attempt", ""),
            "research_blocked": research_state.get("status") == "blocked",
            "date_basis": t["reported_date"] if record.payload.get("date_basis") == "reported" else t["announced_date"],
            "edition": edition, "analyzed": bool(edition), "analysis_day": analysis.get("checked_on") or analysis.get("analyzed_at", "")[:10],
            "stale": bool(edition and (analysis.get("fingerprint") != record.fingerprint or
                          (analysis.get("research_version", 0) >= 2 and research_state.get("fingerprint") and
                           analysis.get("research_fingerprint") != research_state["fingerprint"]))),
            "type": t["debt"] if record.stage == "Debt" else t["grant"] if record.stage == "Grant" else t["unspecified"] if record.stage == "Other" else t["equity"],
        }
        views.append(view)
        if record.company_id not in companies:
            companies[record.company_id] = view
    latest = list(companies.values())
    for view in latest:
        view["history"] = [{key: record[key] for key in ("amount", "native", "day", "stage", "type", "publisher", "url", "date_basis")}
                           for record in views if record["slug"] == view["slug"]]
    return {
        "rounds": views, "companies": latest, "picks": [v for v in latest if v["analyzed"]][:3],
        "latest_day": rounds[0].day if rounds else "", "from_day": rounds[-1].day if rounds else "",
        "count": len(rounds), "analyzed_count": sum(v["analyzed"] for v in latest),
        "undisclosed_count": sum(r.eur is None and r.native is None for r in rounds),
        "us_count": sum(r.country == "United States" for r in rounds),
        "currencies": sorted({v["amount_currency"] for v in views if v["amount_currency"]}),
        "publishers": sorted({r.publisher for r in rounds}),
        "sources": [{"name": name, "url": next(r.url for r in rounds if r.publisher == name)}
                    for name in sorted({r.publisher for r in rounds})],
        "stages": sorted({v["stage_key"]: v["stage"] for v in views}.items()),
        "countries": sorted({v["country_key"]: v["country"] for v in views}.items()),
    }
