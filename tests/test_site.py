from __future__ import annotations

import tempfile
from dataclasses import replace
import unittest
from pathlib import Path

from xocto.i18n import BOARD_EN
from xocto.i18n import EN
from xocto.i18n import ZH
from xocto.models import Product, Sighting
from xocto.site import (
    _business_form,
    _daily_rotation,
    _is_publishable,
    _metric_badges,
    _remove_stale_pages,
    _schema,
    _section,
    product_view,
)


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
    def test_home_is_todays_front_page(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "index.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("r.hook", template)
        self.assertIn("fresh_picks", template)
        self.assertIn("{% for p in items[:3] %}", template)
        self.assertIn("t.home.what", template)
        self.assertIn("t.home.money", template)
        self.assertIn("t.home.meaning", template)
        self.assertNotIn("reader-routes", template)
        self.assertLess(template.index("r.hook"), template.index("t.home.fresh_picks"))
        self.assertIn("t.home.today_takeaway_title", template)
        self.assertIn("t.home.long_term_picks", template)
        self.assertIn("t.home.past_reports", template)
        self.assertLess(template.index("t.home.fresh_picks"), template.index("t.home.today_takeaway_title"))
        self.assertLess(template.index("t.home.today_takeaway_title"), template.index("t.home.long_term_picks"))
        self.assertLess(template.index("t.home.long_term_picks"), template.index("t.home.past_reports"))
        self.assertNotIn("t.home.movers", template)
        self.assertNotIn("t.home.notables", template)
        self.assertNotIn("t.home.cats", template)
        self.assertNotIn("p.analysis.replaces", template)
        self.assertNotIn("stats.total", template)

        products_template = (Path(__file__).parents[1] / "templates" / "products.html").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("p.boards", products_template)
        self.assertIn('href="#grid"', products_template)
        self.assertIn("t.products.results_jump", products_template)
        self.assertIn("grid.scrollIntoView", products_template)
        self.assertIn("event.preventDefault()", products_template)

        nav = (Path(__file__).parents[1] / "templates" / "base.html").read_text(encoding="utf-8")
        nav_start = nav.index('<nav class="nav">')
        nav_end = nav.index("</nav>")
        main_nav = nav[nav_start:nav_end]
        self.assertIn("t.nav.home", main_nav)
        self.assertIn("t.nav.products", main_nav)
        self.assertIn("t.nav.takeaways", main_nav)
        self.assertNotIn("t.nav.reports", main_nav)

    def test_methodology_promises_daily_global_collection_without_naming_sources(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "methodology.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("t.methodology.cadence_title", template)
        self.assertIn("t.methodology.cadence_body", template)
        self.assertIn("t.methodology.reader_title", template)
        self.assertIn("t.methodology.decision_title", template)
        self.assertLess(
            template.index("t.methodology.reader_title"),
            template.index("t.methodology.decision_title"),
        )
        self.assertIn("每天自动更新", ZH.t["home"]["lede_body"])
        self.assertIn("every day", EN.t["home"]["lede_body"].lower())
        forbidden = (
            "Product Hunt",
            "Hacker News",
            "AICPB",
            "GitHub",
            "Hugging Face",
            "Reddit",
        )
        for locale in (ZH, EN):
            blob = " ".join(
                [
                    locale.t["home"]["lede_body"],
                    locale.t["methodology"]["cadence_title"],
                    locale.t["methodology"]["cadence_body"],
                ]
            )
            for name in forbidden:
                self.assertNotIn(name, blob)

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

    def test_money_section_is_extracted_from_analysis(self) -> None:
        body = (
            "## 它在替代什么旧行为\n\n"
            "以前靠人事一个个发资料、核证件。\n\n"
            "## 商业模式\n\n"
            "按席位订阅，价格未披露。掏钱的是公司 HR，不是入职的人。\n\n"
            "## 硬数字\n\n"
            "未披露\n"
        )
        self.assertIn("按席位订阅", _section(body, "商业模式", allow_list=True))
        self.assertIn("人事", _section(body, "它在替代什么旧行为"))

    def test_money_section_keeps_price_list_not_judgment(self) -> None:
        body = (
            "## 商业模式\n\n"
            "- 面向用户：免费，无广告\n"
            "- 面向开发者：API 按量计费\n\n"
            "_判断：网页端本身不产生直接收入。_\n"
        )
        text = _section(body, "商业模式", allow_list=True)
        self.assertIn("免费", text)
        self.assertIn("按量计费", text)
        self.assertIn("; ", text)
        self.assertNotIn("；", text)
        self.assertNotIn("不产生直接收入", text)

    def test_product_page_shows_undisclosed_money_when_missing(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "product.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("t.product.money_unknown", template)
        self.assertIn("t.product.for_investor_k", template)
        self.assertIn("product.for_investor", template)
        self.assertIn("t.product.for_public_k", template)
        self.assertIn("product.for_public", template)

    def test_business_form_follows_evidence(self) -> None:
        self.assertEqual(_business_form("proven", "通用助手", 100_000_000, ""), "settled")
        self.assertEqual(_business_form("proven", "AI + 创作", 50_000_000, ""), "settled")
        self.assertEqual(_business_form("proven", "AI + 效率", 80_000, ""), "scaled")
        self.assertEqual(_business_form("early", "AI + 效率", 0, "一次性买断 129 美元"), "charging")
        self.assertEqual(_business_form("early", "基础层", 0, ""), "not_business")
        self.assertEqual(_business_form("early", "AI + 开发", 0, "收费未披露。公开信息里看不到定价。"), "not_business")

    def test_product_page_puts_money_and_direction_on_top(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "product.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("t.product.money", template)
        self.assertIn("t.product.money_unknown", template)
        self.assertIn("t.product.inspiration", template)
        self.assertIn("analysis.money", template)

    def test_home_picks_surface_direction_not_just_features(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "index.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("t.home.what", template)
        self.assertIn("t.home.money", template)
        self.assertIn("t.home.meaning", template)
        self.assertIn("t.home.daily_contract", template)
        self.assertIn('id="today-cases"', template)
        self.assertIn('id="today-move"', template)
        self.assertIn('id="past-calls"', template)
        self.assertIn("p.summary", template)
        self.assertIn("p.money_brief", template)
        self.assertIn("p.inspiration", template)

    def test_product_page_answers_is_it_a_business_first(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "product.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("t.product.decision_title", template)
        self.assertIn("t.product.call", template)
        self.assertIn("t.product.watch_next", template)
        self.assertLess(template.index("t.product.call"), template.index("t.product.money"))
        self.assertLess(template.index("t.product.money"), template.index("t.product.inspiration"))
        self.assertLess(template.index("t.product.inspiration"), template.index("t.product.watch_next"))
        self.assertLess(template.index("t.product.watch_next"), template.index("t.product.replaces"))
        self.assertLess(template.index("t.product.replaces"), template.index("t.product.for_investor_k"))
        self.assertLess(template.index("t.product.for_investor_k"), template.index("t.product.for_public_k"))

    def test_daily_report_can_be_shared_without_an_account(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "report.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("data-share", template)
        self.assertIn("navigator.share", template)
        self.assertIn("navigator.clipboard.writeText", template)
        self.assertIn("document.execCommand('copy')", template)
        self.assertIn("window.prompt(manualCopy, url)", template)

    def test_analytics_choice_does_not_cover_reading_content(self) -> None:
        css = (Path(__file__).parents[1] / "templates" / "style.css").read_text(
            encoding="utf-8"
        )
        consent_rule = css.split(".analytics-consent", 1)[1].split("}", 1)[0]
        self.assertNotIn("position: fixed", consent_rule)

    def test_local_static_site_does_not_preload_same_origin_fonts_as_cross_origin(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "base.html").read_text(
            encoding="utf-8"
        )
        self.assertNotIn('type="font/woff2" crossorigin', template)

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
