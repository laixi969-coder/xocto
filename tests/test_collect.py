from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import tempfile
import unittest

from xocto.collect import merge_into_pool
from xocto.models import Product, RawItem, Sighting
from xocto.store import Store


class PriorityReviewMergeTests(unittest.TestCase):
    def test_current_github_result_can_clear_an_old_topic_only_priority_mark(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            existing = Product(
                slug="plugin",
                name="Plugin",
                url="https://github.com/example/plugin",
                canonical_url="https://github.com/example/plugin",
                summary="",
                first_seen="2026-08-14T00:00:00Z",
                last_seen="2026-08-14T00:00:00Z",
                status="pending_filter",
                sightings=(Sighting("github", "https://github.com/example/plugin", "2026-08-14T00:00:00Z", {}),),
                priority_review=True,
            )
            store.save_product(existing)
            item = RawItem(
                source="github",
                external_id="1",
                title="Plugin",
                url="https://github.com/example/plugin",
                summary="",
                published_at="",
                collected_at="2026-08-14T01:00:00Z",
                metrics={},
                extra={"priority_review": False},
            )

            merge_into_pool(store, [item], dry_run=False)

            saved = next(store.iter_products())
            self.assertFalse(saved.priority_review)


if __name__ == "__main__":
    unittest.main()
