from __future__ import annotations

import tempfile
from dataclasses import replace
import unittest
from pathlib import Path

from xocto.i18n import BOARD_EN
from xocto.i18n import ZH
from xocto.models import Product, Sighting
from xocto.site import _daily_rotation, _is_publishable, _metric_badges, _remove_stale_pages, _schema, product_view


def product(*, status: str = "watching", summary_zh: str = "中文说明", inspiration: str = "灵感") -> Product:
    return Product(
        slug="example",
        name="Example",
        url="https://example.com",
        canonical_url="https://example.com",
        summary="Source summary",
        first_seen="2026-08-13T00:00:00Z",
        last_seen="2026-08-13T00:00:00Z",
        status=status,
        sightings=(),
        summary_zh=summary_zh,
        inspiration=inspiration,
    )


class PublishabilityTests(unittest.TestCase):
    def test_home_prioritizes_latest_observation_and_caps_long_lists(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "index.html").read_text(
            encoding="utf-8"
        )

        self.assertLess(template.index("t.home.latest_report"), template.index("t.home.today_takeaway_title"))
        self.assertLess(template.index("t.home.today_takeaway_title"), template.index("t.home.fresh_picks"))
        self.assertLess(template.index("t.home.fresh_picks"), template.index("t.home.movers"))
        self.assertLess(template.index("t.home.movers"), template.index("t.home.notables"))
        self.assertLess(template.index("t.home.notables"), template.index("t.home.long_term_picks"))
        self.assertLess(template.index("t.home.long_term_picks"), template.index("t.home.cats"))
        self.assertLess(template.index("t.home.cats"), template.index("t.home.past_reports"))
        self.assertIn("{% for p in items[:3] %}", template)
        self.assertIn("{% for p in movers[:8] %}", template)
        self.assertIn("{% for p in notables[:8] %}", template)
        self.assertNotIn("t.home.col_boards", template)

        products_template = (Path(__file__).parents[1] / "templates" / "products.html").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("p.boards", products_template)

    def test_daily_rotation_moves_the_window_forward(self) -> None:
        items = ["one", "two", "three", "four"]
        first_day = _daily_rotation(items, "2026-08-18", limit=3)
        second_day = _daily_rotation(items, "2026-08-19", limit=3)

        self.assertEqual(len(first_day), 3)
        self.assertNotEqual(first_day, second_day)
        self.assertEqual(_daily_rotation(items, "not-a-date", limit=10), items)

    def test_product_page_uses_latest_metric_and_decodes_names(self) -> None:
        product_with_updates = replace(
            product(),
            name="Safe&amp;Fast",
            sightings=(
                Sighting("github", "https://example.com", "2026-08-11T00:00:00Z", {"stars": 100}),
                Sighting("github", "https://example.com", "2026-08-13T00:00:00Z", {"stars": 120}),
            ),
        )

        self.assertEqual(_metric_badges(product_with_updates, ZH), ["开源关注 120"])
        self.assertEqual(product_view(product_with_updates, ZH)["name"], "Safe&Fast")

    def test_live_board_names_have_english_labels(self) -> None:
        self.assertEqual(BOARD_EN["角色扮演榜"], "Roleplay")
        self.assertEqual(BOARD_EN["全球降速榜"], "Global fastest-declining")

    def test_public_verdict_labels_keep_their_stable_keys(self) -> None:
        self.assertEqual(ZH.verdict_key("重点研究"), "strong")
        self.assertEqual(ZH.verdict_key("持续观察"), "notable")

    def test_product_schema_is_machine_readable_and_uses_known_dates(self) -> None:
        view = product_view(product(), ZH)
        schema = _schema(
            locale=ZH,
            canonical="https://xocto.vercel.app/p/example.html",
            description=view["summary"],
            page="products",
            title=view["name"],
            product=view,
        )
        software = next(item for item in schema["@graph"] if item["@type"] == "SoftwareApplication")
        self.assertEqual(software["name"], "Example")
        self.assertEqual(software["dateModified"], "2026-08-13")

    def test_rejected_product_is_never_published(self) -> None:
        self.assertFalse(_is_publishable(product(status="rejected")))

    def test_incomplete_card_waits_off_site(self) -> None:
        self.assertFalse(_is_publishable(product(summary_zh="")))
        self.assertFalse(_is_publishable(product(inspiration="")))

    def test_reader_ready_product_is_published(self) -> None:
        self.assertTrue(_is_publishable(product()))

    def test_stale_generated_page_is_removed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in ("p/keep.html", "p/rejected.html", "en/p/rejected.html"):
                path = root / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(rel, encoding="utf-8")

            removed = _remove_stale_pages(root, {"p/keep.html"})

            self.assertEqual(removed, 2)
            self.assertTrue((root / "p/keep.html").exists())
            self.assertFalse((root / "p/rejected.html").exists())
            self.assertFalse((root / "en/p/rejected.html").exists())


if __name__ == "__main__":
    unittest.main()
