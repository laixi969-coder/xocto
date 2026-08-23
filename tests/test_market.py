from __future__ import annotations

from datetime import date
import unittest

from xocto.market import _query, _rss_hits, _validated_observations
from xocto.models import Product, Sighting


def product() -> Product:
    return Product(
        slug="freight-ai", name="Freight AI", url="https://example.com", canonical_url="https://example.com",
        summary="Helps freight teams resolve shipment exceptions.", first_seen="2026-08-23T10:00:00Z",
        last_seen="2026-08-23T10:00:00Z", status="watching", sightings=(Sighting("v2ex", "https://example.com", "2026-08-23T10:00:00Z", {}),),
        summary_en="Helps freight teams resolve shipment exceptions.", industries=("物流",), jobs=("货运异常处理",),
    )


class MarketReviewTests(unittest.TestCase):
    def test_queries_use_work_dimensions_in_chinese_and_editorial_summary_in_english(self) -> None:
        item = product()
        self.assertIn("物流", _query(item, "zh"))
        self.assertIn("货运异常处理", _query(item, "zh"))
        self.assertIn("shipment exceptions", _query(item, "en"))

    def test_rss_search_results_become_evidence_candidates(self) -> None:
        rows = _rss_hits("""<rss><channel><item><title>Local freight AI</title><link>https://example.cn</link><description>Product</description></item></channel></rss>""")
        self.assertEqual(rows, [{"title": "Local freight AI", "url": "https://example.cn", "summary": "Product"}])

    def test_market_editor_cannot_reference_unknown_evidence_or_skip_ecosystem(self) -> None:
        item = product()
        expected = [(item, "zh"), (item, "en")]
        result = {"observations": [
            {"slug": "freight-ai", "ecosystem": "zh", "supply_status": "not_found_in_covered_sources", "demand_status": "unknown", "evidence_ids": ["ev-zh"]},
            {"slug": "freight-ai", "ecosystem": "en", "supply_status": "emerging", "demand_status": "early_signal", "evidence_ids": ["ev-en"]},
        ]}
        observations = _validated_observations(result, expected, {("freight-ai", "zh"): {"ev-zh"}, ("freight-ai", "en"): {"ev-en"}}, date(2026, 8, 23))
        self.assertEqual(observations[0].market, "CN")
        self.assertIn("未发现仅限", observations[0].coverage)
        with self.assertRaises(Exception):
            _validated_observations({"observations": result["observations"][:1]}, expected, {("freight-ai", "zh"): {"ev-zh"}, ("freight-ai", "en"): {"ev-en"}}, date(2026, 8, 23))
