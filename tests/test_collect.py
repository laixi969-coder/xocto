from __future__ import annotations

from dataclasses import replace
from datetime import date
from pathlib import Path
import tempfile
import unittest

from xocto.collect import merge_into_pool
from xocto.models import EVENT_FIRST_DISCOVERED, EVENT_MATERIAL_UPDATE, Product, RawItem, Sighting
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


class OpportunityEventTests(unittest.TestCase):
    def test_new_product_creates_one_first_discovery_event_and_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = RawItem(
                source="github",
                external_id="repo-1",
                title="Vertical AI",
                url="https://example.com/vertical-ai",
                summary="Helps freight teams resolve shipment exceptions.",
                published_at="2026-08-14T09:00:00Z",
                collected_at="2026-08-14T10:00:00Z",
                metrics={"stars": 42},
                extra={},
            )

            merge_into_pool(store, [item], dry_run=False)

            events = store.read_events(date(2026, 8, 14))
            self.assertEqual(len(events), 1)
            self.assertEqual(events[0].event_type, EVENT_FIRST_DISCOVERED)
            self.assertEqual(events[0].project_slug, "vertical-ai")
            evidence = store.read_evidence("vertical-ai")
            self.assertEqual(len(evidence), 1)
            self.assertEqual(evidence[0].source_kind, "open_source")

    def test_repeat_does_not_repeat_first_discovery_but_material_change_creates_update(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            original = RawItem(
                source="github",
                external_id="repo-1",
                title="Vertical AI",
                url="https://example.com/vertical-ai",
                summary="Helps freight teams resolve shipment exceptions.",
                published_at="2026-08-14T09:00:00Z",
                collected_at="2026-08-14T10:00:00Z",
                metrics={"stars": 42},
                extra={},
            )
            merge_into_pool(store, [original], dry_run=False)
            merge_into_pool(store, [original], dry_run=False)

            changed = RawItem(
                source="github",
                external_id="repo-1",
                title="Vertical AI",
                url="https://example.com/vertical-ai",
                summary="Helps freight teams resolve shipment exceptions.",
                published_at="2026-08-14T09:00:00Z",
                collected_at="2026-08-14T12:00:00Z",
                metrics={"stars": 80},
                extra={},
            )
            merge_into_pool(store, [changed], dry_run=False)

            events = store.read_events(date(2026, 8, 14))
            self.assertEqual([event.event_type for event in events], [EVENT_FIRST_DISCOVERED, EVENT_MATERIAL_UPDATE])
            self.assertEqual(len(store.read_evidence("vertical-ai")), 2)

    def test_local_ecosystem_discovery_creates_a_market_observation_without_claiming_other_market_absence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = RawItem(
                source="v2ex",
                external_id="topic-1",
                title="Freight AI",
                url="https://freight-ai.cn",
                summary="AI shipment exception product.",
                published_at="2026-08-14T09:00:00Z",
                collected_at="2026-08-14T10:00:00Z",
                metrics={"comments": 3},
                extra={
                    "ecosystem": "zh",
                    "market": "CN",
                    "evidence_url": "https://www.v2ex.com/t/1",
                    "evidence_tier": "independent",
                },
            )

            merge_into_pool(store, [item], dry_run=False)

            observations = store.read_market_observations("freight-ai")
            self.assertEqual(len(observations), 1)
            self.assertEqual(observations[0].ecosystem, "zh")
            self.assertEqual(observations[0].supply_status, "emerging")
            self.assertNotEqual(observations[0].supply_status, "not_found_in_covered_sources")


if __name__ == "__main__":
    unittest.main()
