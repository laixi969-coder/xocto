from __future__ import annotations

from copy import deepcopy
from datetime import date, datetime, timezone
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from xocto.funding import funding_context
from xocto.funding_news import pending_candidates, save_candidates, save_extraction, validate_extraction
from xocto.i18n import EN
from xocto.sources.usfunding import fetch
from xocto.store import Store


TEXT = "San Francisco-based Acme is an AI workflow company. Acme raised $7 million in seed funding from Example Capital. It also secured $3 million in debt financing."


def candidate():
    return {"id": "source-id", "title": "Acme financing", "url": "https://publisher.example/acme",
            "published_at": "2026-10-08T12:00:00Z", "publisher": "Crunchbase News", "fingerprint": "abc",
            "payload": {"text": TEXT, "links": ["https://acme.example"]}}


def row():
    return {"name": "Acme", "country": "United States", "is_ai": True, "completed": True,
            "stage": "Seed", "amount_native": 7000000, "currency": "USD", "website": "https://acme.example",
            "investors": ["Example Capital"], "description_en": "An AI workflow company.",
            "funding_quote": "raised $7 million in seed funding", "geography_quote": "San Francisco-based Acme",
            "ai_quote": "an AI workflow company"}


class USFundingTests(unittest.TestCase):
    def test_native_currency_and_report_date_are_preserved(self):
        payload = validate_extraction({"rounds": [row()]}, candidate())[0]
        self.assertEqual(payload["round"]["amountNative"], 7000000)
        self.assertIsNone(payload["round"]["amountEur"])
        self.assertEqual(payload["date_basis"], "reported")
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory)); save_extraction(store, candidate(), {"rounds": [row()]})
            context = funding_context(store, EN)
            self.assertEqual(context["us_count"], 1)
            self.assertEqual(context["undisclosed_count"], 0)
            self.assertEqual(context["rounds"][0]["amount"], "$7.00M")
            self.assertEqual(context["rounds"][0]["publisher"], "Crunchbase News")

    def test_invented_amount_country_investor_and_website_are_rejected(self):
        for change in ({"amount_native": 70000000}, {"country": "Canada"},
                       {"name": "Invented Company"},
                       {"investors": ["Invented Capital"]}, {"website": "https://guessed.example"},
                       {"completed": False}, {"amount_native": "7000000"}, {"geography_quote": "Unknown city"}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_extraction({"rounds": [{**row(), **change}]}, candidate())

    def test_debt_is_a_separate_round_not_added_to_equity(self):
        debt = {**row(), "stage": "Debt", "amount_native": 3000000, "investors": [],
                "funding_quote": "secured $3 million in debt financing"}
        rounds = validate_extraction({"rounds": [row(), debt]}, candidate())
        self.assertNotEqual(rounds[0]["round"]["id"], rounds[1]["round"]["id"])
        self.assertEqual([r["round"]["amountNative"] for r in rounds], [7000000, 3000000])

    def test_invented_stage_and_dates_are_rejected(self):
        for change in ({"stage": "Series B"}, {"date": "2026-10-07", "date_basis": "reported"},
                       {"date": "2026-10-07", "date_basis": "announced", "date_quote": "October 7"}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_extraction({"rounds": [{**row(), **change}]}, candidate())

    def test_second_article_does_not_double_count_the_same_reported_round(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory))
            first = candidate(); save_extraction(store, first, {"rounds": [row()]})
            second = deepcopy(first)
            second.update(id="other-source", url="https://other.example/acme", publisher="TechCrunch", published_at="2026-10-09T12:00:00Z")
            save_extraction(store, second, {"rounds": [row()]})
            paths = list((store.data_dir / "funding" / "rounds").glob("*.json"))
            self.assertEqual(len(paths), 1)
            import json
            saved = json.loads(paths[0].read_text())
            self.assertEqual(saved["round"]["date"], "2026-10-08")
            self.assertEqual(saved["additional_sources"][0]["source_url"], second["url"])

    def test_valuation_and_proposed_funding_do_not_become_round_amounts(self):
        for text in ("Acme targets $7 million in funding", "Acme total funding is $7 million", "Acme valuation is $7 million"):
            data = candidate(); data["payload"]["text"] += " " + text
            with self.assertRaises(ValueError):
                validate_extraction({"rounds": [{**row(), "funding_quote": text}]}, data)

    def test_rss_content_is_available_and_extraction_state_is_incremental(self):
        class Http:
            def get_text(self, url):
                return '''<rss xmlns:content="http://purl.org/rss/1.0/modules/content/"><channel><item><title>Acme raised funding</title><link>https://publisher.example/acme</link><pubDate>Thu, 08 Oct 2026 12:00:00 GMT</pubDate><description>Short description</description><content:encoded><![CDATA[<p>''' + TEXT + '''</p><a href="https://acme.example">Company</a>]]></content:encoded></item></channel></rss>'''
        with patch("xocto.sources.usfunding.today", return_value=date(2026, 10, 8)):
            items = fetch({"feeds": [{"name": "Crunchbase News", "url": "https://publisher.example/feed"}]}, Http())
        self.assertIn("seed funding", items[0].payload["text"])
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory));save_candidates(store, items)
            first = pending_candidates(store, date(2026, 10, 8))[0]
            save_extraction(store, first, {"rounds": [row()]})
            save_candidates(store, items)
            self.assertEqual(pending_candidates(store, date(2026, 10, 8)), [])


if __name__ == "__main__": unittest.main()
