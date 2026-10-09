"""Deterministic validation and persistence for model-extracted funding facts."""

from __future__ import annotations

import hashlib
import json
import re
from decimal import Decimal
from datetime import date
from uuid import NAMESPACE_URL, uuid5

from .funding import FundingRound, amount, safe_url
from .models import RawItem, slugify
from .store import Store, _atomic_write

STAGES = {"Pre-Seed", "Seed", "Series A", "Series B", "Series C", "Series D+", "Growth/Late", "Debt", "Grant", "Other", "Angel"}


def quoted_amount(quote: str, currency: str, native: float) -> bool:
    markers = {"USD": r"(?:US\$|USD|\$)", "EUR": r"(?:EUR|€)", "GBP": r"(?:GBP|£)", "CAD": r"(?:CAD|C\$)"}
    pattern = markers.get(currency, r"(?!)") + r"\s*([\d,]+(?:\.\d+)?)\s*(billion|million|thousand|bn|[bmk])?\b"
    factors = {"billion": 10**9, "bn": 10**9, "b": 10**9, "million": 10**6, "m": 10**6, "thousand": 1000, "k": 1000}
    return any(Decimal(number.replace(",", "")) * factors.get(unit.lower(), 1) == Decimal(str(native))
               for number, unit in re.findall(pattern, quote, re.I))


def save_candidates(store: Store, items: list[RawItem], *, dry_run: bool = False):
    for item in items:
        if item.extra.get("kind") != "funding_news" or dry_run:
            continue
        path = store.data_dir / "funding" / "news" / f"{item.external_id}.json"
        # Exclude collection time so the same unchanged article does not reset
        # extraction state on every daily pull.
        data = {"id": item.external_id, "title": item.title, "url": item.url,
                "published_at": item.published_at, "publisher": item.extra["publisher"],
                "payload": item.payload}
        content = json.dumps(data, ensure_ascii=False, sort_keys=True)
        data["fingerprint"] = hashlib.sha256(content.encode()).hexdigest()
        _atomic_write(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def pending_candidates(store: Store, day: date):
    records = []
    for path in (store.data_dir / "funding" / "news").glob("*.json"):
        data = json.loads(path.read_text())
        if data["published_at"][:10] > day.isoformat():
            continue
        state = store.data_dir / "funding" / "extraction" / path.name
        previous = json.loads(state.read_text()) if state.exists() else {}
        if previous.get("fingerprint") != data["fingerprint"]:
            records.append(data)
    return sorted(records, key=lambda r: (r["published_at"], r["id"]), reverse=True)


def validate_extraction(result: dict, candidate: dict) -> list[dict]:
    if not isinstance(result, dict) or not isinstance(result.get("rounds"), list):
        raise ValueError("Funding extraction requires a rounds array")
    records = []
    text = candidate["title"] + "\n" + candidate["payload"]["text"]
    for row in result["rounds"]:
        if not isinstance(row, dict) or row.get("country") != "United States" or row.get("completed") is not True or row.get("is_ai") is not True:
            raise ValueError("Only confirmed US AI company rounds can be published")
        name = row.get("name")
        if not isinstance(name, str) or not name.strip() or len(name) > 120:
            raise ValueError("Funding entity has no stable name")
        if name.casefold() not in text.casefold():
            raise ValueError("Funding company name is not present in the source")
        proof = row.get("funding_quote")
        if not isinstance(proof, str) or not proof or proof not in text:
            raise ValueError("Funding quote must occur verbatim in the source")
        if re.search(r"total funding|valuation|seeking|looking to raise|in talks|targets", proof, re.I):
            raise ValueError("A valuation, cumulative total or proposed round is not a completed round amount")
        for key in ("geography_quote", "ai_quote"):
            quote = row.get(key)
            if not isinstance(quote, str) or not quote or quote not in text:
                raise ValueError(f"Missing source-grounded {key}")
        day = row.get("date") or candidate["published_at"][:10]
        date.fromisoformat(day)
        basis = row.get("date_basis", "reported")
        if basis not in {"announced", "reported"}:
            raise ValueError("Funding date basis is invalid")
        if day > candidate["published_at"][:10]:
            raise ValueError("Funding date cannot be in the article's future")
        if basis == "reported" and day != candidate["published_at"][:10]:
            raise ValueError("A reported date must equal the article publication date")
        if basis == "announced":
            date_quote = row.get("date_quote")
            if not isinstance(date_quote, str) or not date_quote or date_quote not in text:
                raise ValueError("An announcement date requires a source quote")
            parsed_day = date.fromisoformat(day)
            tokens = (day, parsed_day.strftime("%B ") + str(parsed_day.day),
                      parsed_day.strftime("%b ") + str(parsed_day.day),
                      parsed_day.strftime("%b. ") + str(parsed_day.day))
            if not any(token.casefold() in date_quote.casefold() for token in tokens):
                raise ValueError("The announcement date does not match its quote")
        stage = row.get("stage", "Other")
        if stage not in STAGES:
            raise ValueError("Unknown funding stage")
        if stage.startswith("Series ") and not re.search(re.escape(stage) if stage != "Series D+" else r"series [d-z]\b", proof, re.I):
            raise ValueError("The funding stage is not supported by its quote")
        stage_terms = {"Seed": r"\bseed\b", "Pre-Seed": r"\bpre[ -]?seed\b", "Debt": r"\bdebt\b", "Grant": r"\bgrant\b", "Angel": r"\bangel\b", "Growth/Late": r"\b(?:growth|late)\b"}
        if stage in stage_terms and not re.search(stage_terms[stage], proof, re.I):
            raise ValueError("The funding type is not supported by its quote")
        native = amount(row.get("amount_native"))
        if row.get("amount_native") is not None and native is None:
            raise ValueError("Funding amount must be a finite non-negative number or null")
        currency = row.get("currency", "")
        if native is not None and currency not in {"USD", "EUR", "GBP", "CAD"}:
            raise ValueError("Funding amount has no explicit currency")
        if native is not None and not quoted_amount(proof, currency, native):
            raise ValueError("Extracted amount does not match the cited funding quote")
        investors = row.get("investors") or []
        if not isinstance(investors, list) or any(not isinstance(name, str) or not name.strip() for name in investors):
            raise ValueError("Investors must be a list of names")
        for investor in investors:
            if investor not in text:
                raise ValueError("Investor name is not present in the source")
        website = safe_url(row.get("website") or "")
        if website and website.rstrip("/") not in {str(url).rstrip("/") for url in candidate["payload"].get("links", [])}:
            raise ValueError("A company website must occur in the source links")
        company_id = str(uuid5(NAMESPACE_URL, "xocto:company:US:" + slugify(name)))
        round_id = str(uuid5(NAMESPACE_URL, f"xocto:round:{company_id}:{day}:{stage}:{currency}:{native}"))
        payload = {
            "publisher": candidate["publisher"], "source_url": candidate["url"],
            "date_basis": basis, "source_quote": proof,
            "geography_quote": row["geography_quote"], "ai_quote": row["ai_quote"],
            "round": {"id": round_id, "url": candidate["url"], "date": day, "stage": stage,
                      "rawRoundType": stage, "amountEur": native if currency == "EUR" else None,
                      "amountNative": native, "currency": currency,
                      "investors": investors, "confidence": "medium",
                      "company": {"id": company_id, "name": name, "country": "United States"}},
            "company": {"id": company_id, "name": name, "description": str(row.get("description_en") or ""),
                        "website": website},
        }
        FundingRound.from_payload(payload)
        records.append(payload)
    return records


def save_extraction(store: Store, candidate: dict, result: dict):
    records = validate_extraction(result, candidate)
    saved_ids = []
    for record in records:
        # Multiple public articles can describe one completed round. When at
        # least one date is a report date, identical financing facts within one
        # week are one event; retain the original date label and both citations.
        for path in sorted((store.data_dir / "funding" / "rounds").glob("*.json")):
            previous = json.loads(path.read_text())
            old, new = previous["round"], record["round"]
            if old["id"] == new["id"]:
                continue
            same = (old["company"]["id"] == new["company"]["id"]
                    and all(old.get(key) == new.get(key) for key in ("stage", "amountNative", "currency"))
                    and new.get("amountNative") is not None
                    and "reported" in (previous.get("date_basis"), record.get("date_basis"))
                    and abs((date.fromisoformat(old["date"][:10]) - date.fromisoformat(new["date"][:10])).days) <= 7)
            if same:
                citation = {key: record[key] for key in ("publisher", "source_url", "source_quote", "date_basis")}
                citation["date"] = new["date"]
                additional = previous.setdefault("additional_sources", [])
                if record["source_url"] != previous.get("source_url") and citation not in additional:
                    additional.append(citation)
                record = previous
                break
        _atomic_write(store.data_dir / "funding" / "rounds" / f"{record['round']['id']}.json",
                      json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        saved_ids.append(record["round"]["id"])
    _atomic_write(store.data_dir / "funding" / "extraction" / f"{candidate['id']}.json",
                  json.dumps({"fingerprint": candidate["fingerprint"], "round_ids": saved_ids,
                              "reason": result.get("reason", "")}, ensure_ascii=False, indent=2) + "\n")
    return len(records)
