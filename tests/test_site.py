from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from xocto.i18n import BOARD_EN
from xocto.models import Product
from xocto.site import _is_publishable, _remove_stale_pages


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

        self.assertLess(template.index("t.home.latest_report"), template.index("t.home.picks"))
        self.assertLess(template.index("t.home.picks"), template.index("t.home.movers"))
        self.assertLess(template.index("t.home.movers"), template.index("t.home.notables"))
        self.assertLess(template.index("t.home.notables"), template.index("t.home.cats"))
        self.assertLess(template.index("t.home.cats"), template.index("t.home.past_reports"))
        self.assertIn("{% for p in picks[:3] %}", template)
        self.assertIn("{% for p in movers[:5] %}", template)
        self.assertIn("{% for p in notables[:8] %}", template)

    def test_live_board_names_have_english_labels(self) -> None:
        self.assertEqual(BOARD_EN["角色扮演榜"], "Roleplay")
        self.assertEqual(BOARD_EN["全球降速榜"], "Global fastest-declining")

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
