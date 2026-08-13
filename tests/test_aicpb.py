from __future__ import annotations

import unittest
from unittest.mock import patch

from xocto.models import RawItem
from xocto.sources.aicpb import (
    DETAIL_BATCH_PAUSE,
    DETAIL_BATCH_SIZE,
    DETAIL_DELAY,
    _enrich,
)


class FakeHttp:
    def get_text(self, url: str) -> str:
        return '<meta name="description" content="A &amp; B">'


def item(index: int) -> RawItem:
    return RawItem(
        source="aicpb",
        external_id=str(index),
        title=f"Product {index}",
        url=f"https://example.com/{index}",
        summary="",
        published_at="",
        collected_at="2026-08-13T00:00:00Z",
        metrics={},
        extra={},
        payload={"path": f"/product/{index}"},
    )


class EnrichmentTests(unittest.TestCase):
    @patch("xocto.sources.aicpb.time.sleep")
    def test_details_are_split_across_rate_limit_windows(self, sleep) -> None:
        enriched = _enrich([item(i) for i in range(DETAIL_BATCH_SIZE * 2 + 1)], FakeHttp())

        pauses = [call.args[0] for call in sleep.call_args_list]
        self.assertEqual(pauses.count(DETAIL_BATCH_PAUSE), 2)
        self.assertEqual(pauses.count(DETAIL_DELAY), len(enriched) - 3)
        self.assertTrue(all(x.summary == "A & B" for x in enriched))


if __name__ == "__main__":
    unittest.main()
