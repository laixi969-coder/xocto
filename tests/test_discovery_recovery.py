from __future__ import annotations

from dataclasses import replace
from datetime import date
from pathlib import Path
import tempfile
import unittest

from xocto.brief import candidates_for_day
from xocto.collect import merge_into_pool
from xocto.dedupe import ProductIndex
from xocto.entity_watch import annotate
from xocto.models import Product, RawItem, Sighting
from xocto.store import Store


def product(slug, name, url, **kwargs):
    return Product(slug=slug, name=name, url=url, canonical_url=url, summary="",
                   first_seen="2026-09-08T12:00:00Z", last_seen="2026-09-10T12:00:00Z",
                   status="pending_filter", sightings=(), **kwargs)


def item(title, url, summary="", **extra):
    return RawItem("newssearch", "id", title, url, summary, "2026-10-08T12:00:00Z", "2026-10-08T13:00:00Z", {}, {"kind": "news", **extra})


META = {"name": "Meta Muse", "url": "https://muse.ai/", "patterns": [r"\bMeta(?:'s)?\b.{0,60}\bMuse\b"],
        "exclude": [r"\bMuse[ -]+Spark\b"], "issuer_hosts": ["about.fb.com"], "aliases": ["Muse"]}


class DiscoveryRecoveryTests(unittest.TestCase):
    def test_first_tracking_date_is_not_the_old_article_publication_date(self):
        raw=item('New app','https://new.example/')
        raw=replace(raw,published_at='2026-09-08T19:10:38Z',collected_at='2026-09-10T05:13:24Z')
        created=Product.from_raw(raw,'https://new.example')
        self.assertEqual(created.first_seen,raw.collected_at)
        with tempfile.TemporaryDirectory() as directory:
            store=Store(Path(directory));store.ensure_dirs()
            merge_into_pool(store,[raw],dry_run=False)
            event=store.read_events(date(2026,9,10))[0]
            self.assertEqual(event.occurred_at,raw.collected_at)

    def test_same_name_distinct_product_sites_are_not_merged(self):
        index = ProductIndex([product("bookmark", "Muse", "https://bookmark.example")])
        self.assertIsNone(index.match(replace(item("Muse", "https://muse.ai/"), extra={"kind": "product"})))

    def test_aggregator_name_is_not_enough_to_identify_a_news_subject(self):
        index = ProductIndex([product("bookmark", "Muse", "https://www.producthunt.com/products/muse-19")])
        self.assertIsNone(index.match(item("Muse", "https://media.example/story")))

    def test_incidental_summary_mentions_and_substrings_do_not_attach(self):
        index = ProductIndex([product("muse", "Muse", "https://muse.ai/")])
        self.assertIsNone(index.match(item("Pocket FM doubles revenue", "https://media.example/one", "Competitor Meta Muse is mentioned.")))
        self.assertIsNone(index.match(item("Amusement software launches", "https://media.example/two")))

    def test_reviewed_identity_routes_a_report_to_the_right_muse(self):
        bookmark = product("bookmark", "Muse", "https://www.producthunt.com/products/muse-19")
        meta = product("meta", "Meta Muse", "https://muse.ai/")
        tagged = annotate(item("Meta's Muse arrives on Mac", "https://media.example/story"), [META])
        self.assertEqual(ProductIndex([bookmark, meta]).match(tagged).slug, "meta")
        self.assertTrue(tagged.extra["priority_review"])
        model=annotate(item("Meta Muse Spark model", "https://media.example/model"), [META])
        self.assertNotIn("verified_entity_url", model.extra)
        self.assertIsNone(ProductIndex([meta]).match(model))
        self.assertNotIn("verified_entity_url", annotate(item("Pocket FM launches", "https://media.example/pocket", "Meta Muse is its competitor"), [META]).extra)
        self.assertIn("verified_entity_url", annotate(item("Introducing Muse", "https://about.fb.com/news/launch"), [META]).extra)

    def test_all_overdue_priorities_survive_a_bounded_ordinary_backlog(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory))
            for n in range(40): store.save_product(product(f"old-{n:02}", f"Old {n}", f"https://old{n}.example"))
            store.save_product(product("priority", "Important", "https://priority.example", priority_review=True))
            current = replace(product("today", "Today", "https://today.example"), last_seen="2026-10-08T13:00:00Z")
            store.save_product(current)
            rows = candidates_for_day(store, date(2026, 10, 8))
            self.assertEqual(len(rows), 34)
            self.assertEqual(rows[0].slug, "priority")
            self.assertIn("today", {p.slug for p in rows})

    def test_comparison_preserves_multiple_subjects_through_weak_matching(self):
        instinct_spec={"name":"Instinct", "url":"https://instinct.com/", "patterns":[r"\bInstinct\b"]}
        tagged=annotate(item("Rival AI agents Instinct and Meta's Muse add calls", "https://media.example/comparison"), [META, instinct_spec])
        self.assertNotIn("verified_entity_url", tagged.extra)
        # Apostrophe spelling prevents the ordinary Meta Muse name from
        # matching; that must not turn the comparison into an Instinct report.
        index=ProductIndex([product("meta", "Meta Muse", "https://muse.ai/"), product("instinct", "Instinct", "https://instinct.com/")])
        self.assertIsNone(index.match(tagged))

    def test_third_party_plugins_do_not_become_the_watched_product(self):
        plugin = replace(item("Meta Muse helper", "https://github.com/example/muse-helper"),
                         source="github", extra={"kind": "product"})
        self.assertNotIn("verified_entity_url", annotate(plugin, [META]).extra)

    def test_tracked_identity_upgrades_an_aggregator_profile_and_keeps_its_slug(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory)); store.ensure_dirs()
            store.save_product(product("muse-by-meta", "Muse by Meta", "https://www.producthunt.com/products/muse-22"))
            page = replace(item("Meta Muse", "https://muse.ai/", "First-party capabilities"),
                           source="trackedproducts", external_id="muse-by-meta:digest",
                           metrics={"content_hash": "digest"},
                           extra={"kind": "product", "verified_entity_slug": "muse-by-meta",
                                  "verified_entity_url": "https://muse.ai/", "priority_review": True})
            merge_into_pool(store, [page], dry_run=False)
            rows = list(store.iter_products())
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0].slug, "muse-by-meta")
            self.assertEqual(rows[0].url, "https://muse.ai/")

    def test_retired_article_urls_route_future_updates_to_the_canonical_product(self):
        canonical=product("instinct","Instinct","https://instinct.com/")
        article=replace(product("old-story","Instinct","https://media.example/story"),status="rejected")
        index=ProductIndex([article,canonical],aliases={"old-story":"instinct"})
        self.assertEqual(index.match(item("Updated financing story","https://media.example/story")).slug,"instinct")
        self.assertEqual(index.match(item("Instinct expands its service","https://other.example/story")).slug,"instinct")

    def test_non_github_priority_and_official_page_change_reopen_review(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory)); store.ensure_dirs()
            existing = replace(product("meta", "Meta Muse", "https://muse.ai/"), status="analyzed")
            store.save_product(existing)
            page = replace(item("Meta Muse", "https://muse.ai/", "New first-party capability"),
                           source="trackedproducts", metrics={"content_hash": "new"},
                           extra={"kind": "product", "priority_review": True})
            merge_into_pool(store, [page], dry_run=False)
            saved = next(store.iter_products())
            self.assertTrue(saved.priority_review)
            self.assertEqual(saved.status, "pending_filter")


if __name__ == "__main__": unittest.main()
