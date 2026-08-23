from __future__ import annotations

import tempfile
from dataclasses import replace
import unittest
from pathlib import Path

from xocto.i18n import BOARD_EN
from xocto.i18n import EN
from xocto.i18n import ZH
from xocto.models import (
    DEMAND_EARLY_SIGNAL,
    REQ_GATE_CONSENSUS,
    REQ_GATE_INSUFFICIENT,
    REQ_GATE_MODEL,
    REQ_GATE_SUPPORTED,
    REQ_GATE_TRUTH,
    REQ_GATE_VALUE,
    REQ_NEEDS_VALIDATION,
    SUPPLY_EMERGING,
    SUPPLY_NOT_FOUND,
    EVENT_FIRST_DISCOVERED,
    EVENT_MATERIAL_UPDATE,
    DiscoveryEvent,
    Evidence,
    MarketObservation,
    Product,
    ReqGateReview,
    ReqReview,
    Sighting,
)
from xocto.site import (
    _business_form,
    build_context,
    _daily_rotation,
    _is_publishable,
    _metric_badges,
    _remove_stale_pages,
    _research_view,
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
        self.assertIn("first_discoveries", template)
        self.assertIn("important_updates", template)
        self.assertIn("{% for p in items %}", template)
        self.assertIn("t.home.what", template)
        self.assertIn("t.home.req_initial", template)
        self.assertNotIn("reader-routes", template)
        self.assertIn("event_day", template)
        self.assertIn("t.home.daily_flow", template)
        self.assertIn("market_summary", template)
        self.assertIn("t.home.past_reports", template)
        self.assertLess(template.index("first_discoveries"), template.index("important_updates"))
        self.assertLess(template.index("important_updates"), template.index("market_summary"))
        self.assertLess(template.index("market_summary"), template.index("t.home.past_reports"))
        self.assertNotIn("fresh_picks", template)
        self.assertNotIn("today_takeaway", template)
        self.assertNotIn("more_opportunities", template)
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

    def test_english_view_never_falls_back_to_untranslated_raw_fields(self) -> None:
        untranslated = replace(
            product(),
            summary="为货运团队处理异常订单。",
            summary_en="",
            builder="中文团队",
            industries=("物流",),
            jobs=("异常处理",),
            regions=("中国",),
        )

        view = product_view(untranslated, EN)

        self.assertEqual(view["summary"], "")
        self.assertFalse(view["has_summary"])
        self.assertEqual(view["builder"], "")
        self.assertEqual(view["industries"], [])
        self.assertEqual(view["jobs"], [])
        self.assertEqual(view["regions"], [])

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

    def test_settled_general_assistant_stays_out_of_the_opportunity_library(self) -> None:
        settled = replace(
            product(),
            category="通用助手",
            sightings=(
                Sighting("ranking", "https://example.com", "2026-08-13T00:00:00Z", {"value": 40_000_000}),
            ),
        )
        self.assertFalse(_is_publishable(settled))

    def test_large_vertical_product_is_still_publishable(self) -> None:
        vertical = replace(
            product(),
            category="AI + 商业",
            summary="Automates shipment exception handling for freight forwarders.",
            summary_zh="给货代处理货运异常的系统",
            sightings=(
                Sighting("ranking", "https://example.com", "2026-08-13T00:00:00Z", {"value": 40_000_000}),
            ),
        )
        self.assertTrue(_is_publishable(vertical))

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

    def test_home_event_cards_surface_initial_req_and_dates(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "index.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("t.home.what", template)
        self.assertIn("t.home.direction", template)
        self.assertIn("t.home.req_initial", template)
        self.assertIn("t.home.discovered_at", template)
        self.assertIn('id="today-cases"', template)
        self.assertIn('id="important-updates"', template)
        self.assertIn('id="past-calls"', template)
        self.assertIn("p.summary", template)
        self.assertIn("p.inspiration", template)
        self.assertIn("p.req_signal", template)
        self.assertIn("p.req_next", template)
        self.assertIn("p.event_day", template)

    def test_home_uses_only_the_latest_event_day_and_separates_first_discoveries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            from xocto.store import Store

            store = Store(Path(tmp))
            historical = product()
            fresh = replace(product(), slug="fresh", name="Fresh", industries=("货运物流",))
            store.save_product(historical)
            store.save_product(fresh)
            store.append_event(DiscoveryEvent(
                id="first-example",
                project_slug="example",
                event_type=EVENT_FIRST_DISCOVERED,
                occurred_at="2026-08-13T10:00:00Z",
                discovered_at="2026-08-13T11:00:00Z",
            ))
            store.append_event(DiscoveryEvent(
                id="update-example",
                project_slug="example",
                event_type=EVENT_MATERIAL_UPDATE,
                occurred_at="2026-08-14T10:00:00Z",
                discovered_at="2026-08-14T11:00:00Z",
                summary="A new public adoption signal.",
            ))
            store.append_event(DiscoveryEvent(
                id="first-fresh",
                project_slug="fresh",
                event_type=EVENT_FIRST_DISCOVERED,
                occurred_at="2026-08-14T12:00:00Z",
                discovered_at="2026-08-14T13:00:00Z",
            ))

            ctx = build_context(store, ZH)

            self.assertEqual(ctx["event_day"], "2026-08-14")
            self.assertEqual([item["slug"] for item in ctx["first_discoveries"]], ["fresh"])
            self.assertEqual([item["slug"] for item in ctx["important_updates"]], ["example"])
            self.assertEqual(ctx["market_summary"][0]["title"], "今日首次发现涉及的行业")

    def test_home_hides_collector_status_as_event_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            from xocto.store import Store

            store = Store(Path(tmp))
            store.save_product(product())
            store.append_event(DiscoveryEvent(
                id="generic-update",
                project_slug="example",
                event_type=EVENT_MATERIAL_UPDATE,
                occurred_at="2026-08-14T10:00:00Z",
                discovered_at="2026-08-14T11:00:00Z",
                summary="发现新的公开信号",
            ))

            ctx = build_context(store, ZH)

            self.assertEqual(ctx["important_updates"][0]["event_summary"], "")

    def test_opportunity_library_offers_parallel_dimensions_and_shareable_date_filters(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "products.html").read_text(
            encoding="utf-8"
        )
        for dim in ("projectType", "industry", "job", "region", "openSource", "crossMarket", "req"):
            self.assertIn(f'data-dim="{dim}"', template)
        self.assertIn('id="date-from"', template)
        self.assertIn('id="date-to"', template)
        self.assertIn("data-discovered", template)
        self.assertIn("dateFrom", template)
        self.assertIn("dateTo", template)

    def test_detail_research_view_keeps_market_coverage_and_marks_cross_market_only_from_snapshots(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            from xocto.store import Store

            store = Store(Path(tmp))
            evidence = Evidence(
                id="ev-product",
                project_slug="freight-ai",
                url="https://example.com",
                title="Freight AI",
                published_at="2026-08-14T09:00:00Z",
                collected_at="2026-08-14T10:00:00Z",
                source_kind="product",
                tier="first_party",
                fact="Shipment-exception workflow is publicly described.",
            )
            store.append_evidence(evidence)
            for market, ecosystem, supply, coverage in (
                ("US", "en", SUPPLY_EMERGING, "English public coverage checked on 2026-08-14."),
                ("CN", "zh", SUPPLY_NOT_FOUND, "已覆盖中文生态公开项目发布与开发者讨论。"),
            ):
                store.append_market_observation(MarketObservation(
                    project_slug="freight-ai",
                    market=market,
                    ecosystem=ecosystem,
                    observed_at="2026-08-14T10:00:00Z",
                    supply_status=supply,
                    demand_status=DEMAND_EARLY_SIGNAL,
                    coverage=coverage,
                    evidence_ids=("ev-product",),
                ))
            store.append_req_review(ReqReview(
                id="req-1",
                project_slug="freight-ai",
                level="initial",
                reviewed_at="2026-08-14T10:00:00Z",
                verdict=REQ_NEEDS_VALIDATION,
                signal_level="待验证",
                gates=(
                    ReqGateReview(REQ_GATE_VALUE, REQ_GATE_SUPPORTED, "货运异常处理场景具体，现有工作流可识别。", ("ev-product",)),
                    ReqGateReview(REQ_GATE_CONSENSUS, REQ_GATE_INSUFFICIENT, "重复采用信号尚未公开。"),
                    ReqGateReview(REQ_GATE_MODEL, REQ_GATE_INSUFFICIENT, "付费主体与定价尚待核验。"),
                    ReqGateReview(REQ_GATE_TRUTH, REQ_GATE_INSUFFICIENT, "异常交付的责任边界待验证。"),
                ),
                next_validation="确认货代是否为异常处理持续付费。",
            ))

            research = _research_view(store, "freight-ai", ZH)

            self.assertTrue(research["cross_market"])
            self.assertEqual(len(research["markets"]), 2)
            self.assertTrue(any("已覆盖中文生态" in row["coverage"] for row in research["markets"]))
            self.assertEqual(research["req"]["gates"][0]["name"], "价值")
            self.assertEqual(research["evidence"][0]["title"], "Freight AI")

            english = _research_view(store, "freight-ai", EN)
            self.assertEqual(english["req"]["signal"], "Needs validation")
            self.assertEqual(english["req"]["gates"][0]["reason"], EN.t["product"]["req_reason_pending"])
            self.assertEqual(english["req"]["next_validation"], EN.t["product"]["req_next_pending"])
            self.assertTrue(any(
                row["coverage"] == EN.t["product"]["market_coverage_pending"]
                for row in english["markets"]
            ))

    def test_product_template_surfaces_req_market_and_evidence_sections(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "product.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("t.product.req_title", template)
        self.assertIn("product.req.gates", template)
        self.assertIn("t.product.markets_title", template)
        self.assertIn("product.cross_market", template)
        self.assertIn("t.product.evidence_title", template)
        self.assertIn("product.evidence", template)

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

    def test_static_site_has_no_conflicting_font_preloads(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "base.html").read_text(
            encoding="utf-8"
        )
        self.assertNotIn('as="font"', template)

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
