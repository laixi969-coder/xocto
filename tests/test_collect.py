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
    def test_two_reports_on_the_same_media_host_do_not_become_one_product(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            items = [
                RawItem(
                    source="marketfeeds",
                    external_id=f"report-{number}",
                    title=title,
                    url=f"https://www.qbitai.com/{number}",
                    summary=summary,
                    published_at="2026-08-14T09:00:00Z",
                    collected_at="2026-08-14T10:00:00Z",
                    metrics={},
                    extra={"kind": "news", "official": False},
                )
                for number, title, summary in (
                    (1, "云知声披露智能体收入增长", "企业智能体业务出现收入和客户复购信号。"),
                    (2, "医疗影像公司发布新产品", "另一家公司推出面向医院的影像工作流。"),
                )
            ]

            result = merge_into_pool(store, items, dry_run=False)

            self.assertEqual(result, (2, 0, 0, 2))
            self.assertEqual(len(list(store.iter_products())), 2)

    def test_chinese_entity_mention_attaches_a_report_and_reopens_editorial_review(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            existing = Product(
                slug="云知声",
                name="云知声",
                url="https://www.unisound.com",
                canonical_url="https://unisound.com",
                summary="企业智能体业务",
                first_seen="2026-08-13T00:00:00Z",
                last_seen="2026-08-13T00:00:00Z",
                status="watching",
                sightings=(Sighting("official", "https://www.unisound.com", "2026-08-13T00:00:00Z", {}),),
            )
            store.save_product(existing)
            report = RawItem(
                source="marketfeeds",
                external_id="qbit-report",
                title="港股 AGI 公司云知声披露智能体收入增长",
                url="https://www.qbitai.com/2026/08/123.html",
                summary="云知声披露智能体业务收入和复购信号。",
                published_at="2026-08-14T09:00:00Z",
                collected_at="2026-08-14T10:00:00Z",
                metrics={},
                extra={"kind": "news", "official": False},
            )

            result = merge_into_pool(store, [report], dry_run=False)

            self.assertEqual(result, (0, 1, 0, 1))
            saved = next(store.iter_products())
            self.assertEqual(saved.status, "pending_filter")
            self.assertEqual(len(saved.sightings), 2)
            self.assertEqual(store.read_events(date(2026, 8, 14))[0].event_type, EVENT_MATERIAL_UPDATE)

    def test_news_is_a_discovery_signal_instead_of_being_discarded_from_the_pool(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = RawItem(
                source="marketfeeds",
                external_id="report-1",
                title="Agent business reaches material revenue",
                url="https://example.com/report",
                summary="The company disclosed revenue, repeat purchases, and customer adoption.",
                published_at="2026-08-14T09:00:00Z",
                collected_at="2026-08-14T10:00:00Z",
                metrics={},
                extra={"kind": "news", "official": False},
            )

            new, updated, unchanged, news = merge_into_pool(store, [item], dry_run=False)

            self.assertEqual((new, updated, unchanged, news), (1, 0, 0, 1))
            saved = next(store.iter_products())
            self.assertEqual(saved.status, "pending_filter")
            self.assertEqual(store.read_evidence(saved.slug)[0].source_kind, "market_signal")
            self.assertEqual(len(store.read_events(date(2026, 8, 14))), 1)

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
