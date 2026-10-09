from __future__ import annotations

import json
import tempfile
import unittest
from copy import deepcopy
from datetime import date
from pathlib import Path
from unittest.mock import patch

from xocto.collect import merge_into_pool
from xocto.funding import (
    FundingRound, SECTIONS, analysis_path, funding_context, read_rounds,
    save_analysis, save_rounds, validate_analysis,
)
from xocto.i18n import EN, ZH
from xocto.sources.techfunding import fetch
from xocto.store import Store

COMPANY = "00000000-0000-4000-8000-000000000001"
ROUND = "00000000-0000-4000-8000-000000000002"
ROUND2 = "00000000-0000-4000-8000-000000000003"


def row(id=ROUND, **changes):
    return {
        "id": id, "url": f"/deals/{id}", "date": "2026-10-08", "stage": "Other",
        "rawRoundType": "funding round", "amountEur": None, "amountNative": None,
        "currency": "", "investors": ["Example Capital"], "confidence": "none",
        "company": {"id": COMPANY, "name": "Example", "country": "UK"}, **changes,
    }


class FakeHttp:
    def __init__(self, pages):
        self.pages = iter(pages)
        self.calls = []

    def get_json(self, url, *, params=None):
        self.calls.append((url, deepcopy(params)))
        if "/companies/" in url:
            return {"id": COMPANY, "name": "Example", "website": "https://example.org", "description": "An AI workflow."}
        return next(self.pages)


def items(*rows):
    http = FakeHttp([{"data": list(rows), "nextCursor": None}])
    with patch("xocto.sources.techfunding.today", return_value=date(2026, 10, 8)):
        return fetch({"lookback_days": 30}, http)


def analysis(record):
    edition = {field: "A grounded commercial inference." for field in ("summary", "judgment", "replaces", "segment", *SECTIONS)}
    edition["citations"] = [{"label": "Funding record", "url": record.url}]
    edition["citations"].append({"label": "Product site", "url": record.website})
    return {"company_id": COMPANY, "round_id": record.id, "fingerprint": record.fingerprint,
            "analyzed_at": "2026-10-08T12:00:00Z", "en": edition, "zh": deepcopy(edition)}


class FundingTests(unittest.TestCase):
    def test_reviewed_official_identity_survives_a_feed_with_no_website(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory)); store.config_dir.mkdir(parents=True)
            fetched=items(row()); fetched[0].payload['company']['website']=''
            save_rounds(store,fetched)
            (store.config_dir/'funding-research.yaml').write_text('companies:\n  '+COMPANY+':\n    website: https://example.org\n')
            self.assertEqual(funding_context(store,EN)['companies'][0]['website'],'https://example.org')
    def test_pagination_deduplicates_rounds_and_reuses_company_profile(self):
        http = FakeHttp([
            {"data": [row()], "nextCursor": "cursor-1"},
            {"data": [row(), row(ROUND2, stage="Debt", amountEur=100)], "nextCursor": None},
        ])
        with patch("xocto.sources.techfunding.today", return_value=date(2026, 10, 8)):
            fetched = fetch({"lookback_days": 30}, http)
        self.assertEqual(len(fetched), 2)
        self.assertEqual(http.calls[0][1]["from"], "2026-09-09")
        self.assertEqual(http.calls[1][1]["after"], "cursor-1")
        self.assertEqual(sum("/companies/" in url for url, _ in http.calls), 1)
        self.assertIsNone(fetched[0].payload["round"]["amountEur"])
        self.assertEqual(fetched[1].payload["round"]["stage"], "Debt")

    def test_rounds_are_idempotent_and_never_change_product_maturity(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory)); store.ensure_dirs()
            fetched = items(row(), row(ROUND2, stage="Debt", amountEur=100))
            merge_into_pool(store, fetched, dry_run=True)
            self.assertEqual(read_rounds(store), [])
            merge_into_pool(store, fetched, dry_run=False)
            merge_into_pool(store, fetched, dry_run=False)
            self.assertEqual(list(store.iter_products()), [])
            records = read_rounds(store, as_of=date(2026, 10, 8))
            self.assertEqual(len(records), 2)
            self.assertEqual(len({r.company_id for r in records}), 1)
            context = funding_context(store, EN)
            self.assertEqual(context["undisclosed_count"], 1)
            self.assertEqual(context["rounds"][1]["amount"], "Undisclosed")
            self.assertEqual(context["rounds"][0]["type"], "Debt financing")

    def test_future_records_are_not_published(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory))
            save_rounds(store, items(row(date="2026-10-09")))
            self.assertEqual(read_rounds(store, as_of=date(2026, 10, 8)), [])

    def test_partial_translation_and_invented_citations_never_overwrite_analysis(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory))
            record = FundingRound.from_payload(items(row())[0].payload)
            good = analysis(record); save_analysis(store, record, good)
            before = analysis_path(store, record).read_bytes()
            bad = deepcopy(good); bad["en"]["workflow"] = "未翻译"
            with self.assertRaises(ValueError): save_analysis(store, record, bad)
            self.assertEqual(analysis_path(store, record).read_bytes(), before)
            bad = deepcopy(good); bad["en"]["citations"][0]["url"] = "https://invented.org"
            with self.assertRaises(ValueError): validate_analysis(bad, record)

    def test_new_round_and_corrections_mark_existing_analysis_stale_in_both_editions(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory))
            fetched = items(row()); save_rounds(store, fetched)
            record = FundingRound.from_payload(fetched[0].payload)
            save_analysis(store, record, analysis(record))
            save_rounds(store, items(row(amountEur=200)))
            for locale in (ZH, EN):
                context = funding_context(store, locale)
                self.assertTrue(context["companies"][0]["stale"])
                self.assertEqual(context["analyzed_count"], 1)
            save_rounds(store, items(row(ROUND2, date="2026-10-09")))
            self.assertEqual(len(read_rounds(store, as_of=date(2026, 10, 9))), 2)

    def test_model_refresh_is_incremental_and_failed_translation_preserves_previous_analysis(self):
        from xocto.brief import BriefError, run_funding
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory))
            fetched = items(row()); save_rounds(store, fetched)
            record = FundingRound.from_payload(fetched[0].payload)
            evidence = [{"url": record.url, "kind": "funding", "text": "Recorded facts."},
                        {"url": record.website, "kind": "company_claim", "text": "Concrete product workflow and deliverables. " * 8}]
            with patch("xocto.collect.load_config", return_value={}), \
                 patch("xocto.brief._read_config", return_value="Ground claims in supplied evidence."), \
                 patch("xocto.funding_research.research", return_value=evidence), \
                 patch("xocto.brief._request", return_value=analysis(record)) as request:
                self.assertEqual(run_funding(store, day=date(2026, 10, 8)), 1)
                self.assertEqual(run_funding(store, day=date(2026, 10, 8)), 0)
                self.assertEqual(request.call_count, 1)
                before = analysis_path(store, record).read_bytes()
                request.return_value = {"company_id": COMPANY, "zh": {}}
                with self.assertRaises(BriefError):
                    run_funding(store, day=date(2026, 10, 8), force=True)
                self.assertEqual(analysis_path(store, record).read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
