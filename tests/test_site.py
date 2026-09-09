from __future__ import annotations

import json
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
    _blank_takeaway,
    _business_form,
    build_context,
    _daily_event_selection,
    _daily_rotation,
    _is_publishable,
    _latest_req_review,
    _localized_evidence_copy,
    _metric_badges,
    _neutralize_public_source_names,
    _opportunity_action,
    _proven_business_selection,
    _public_method_text,
    _public_page_url,
    load_analyses,
    _takeaway_topics,
    _remove_stale_pages,
    _req_decision_reason,
    _research_view,
    _schema,
    _section,
    product_view,
)
from xocto.store import Store


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
    def test_public_evidence_copy_removes_collection_channel_names(self) -> None:
        headline = "Visa patches production code before review VentureBeat"
        self.assertEqual(
            _neutralize_public_source_names(headline, EN),
            "Visa patches production code before review",
        )
        self.assertEqual(
            _neutralize_public_source_names("VentureBeat 报道了新产品", ZH),
            "公开资料 报道了新产品",
        )

    def test_html_is_never_served_stale_after_a_deployment(self) -> None:
        config = json.loads((Path(__file__).parents[1] / "vercel.json").read_text(encoding="utf-8"))
        rules = {rule["source"]: rule["headers"] for rule in config["headers"]}
        for source in ("/", "/(.*).html"):
            cache = next(header["value"] for header in rules[source] if header["key"] == "Cache-Control")
            self.assertEqual(cache, "no-store, max-age=0")

    def test_pages_declare_the_existing_brand_mark_as_favicon(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "base.html").read_text(encoding="utf-8")
        self.assertIn('rel="icon" type="image/png" href="{{ root }}logo/mark-on-light.png"', template)

    def test_reader_facing_copy_does_not_use_pending_validation(self) -> None:
        for locale in (ZH, EN):
            blob = " ".join(
                value
                for section in locale.t.values()
                if isinstance(section, dict)
                for value in section.values()
                if isinstance(value, str)
            )
            self.assertNotIn("待验证", blob)
            self.assertNotIn("Needs validation", blob)

    def test_reader_facing_copy_does_not_expose_internal_req_name(self) -> None:
        for locale in (ZH, EN):
            for section in ("home", "products", "product"):
                for value in locale.t[section].values():
                    if isinstance(value, str):
                        self.assertNotIn("/req", value.lower())

    def test_home_strips_internal_req_name_from_event_summaries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            from xocto.store import Store

            store = Store(Path(tmp))
            store.save_product(product())
            store.append_event(DiscoveryEvent(
                id="req-change",
                project_slug="example",
                event_type=EVENT_MATERIAL_UPDATE,
                occurred_at="2026-08-25T10:00:00Z",
                discovered_at="2026-08-25T11:00:00Z",
                summary="`/req` 信号由“初步成立”调整为“待验证”；当前停在价值闸门：公开材料仅描述产品功能。",
            ))

            ctx = build_context(store, ZH)

            self.assertEqual(len(ctx["important_updates"]), 1)
            summary = ctx["important_updates"][0]["event_summary"]
            self.assertNotIn("/req", summary)
            self.assertNotIn("待验证", summary)
            self.assertIn("信号由“初步成立”调整为“需求不成立”", summary)

    def test_section_notes_use_the_full_available_line(self) -> None:
        css = (Path(__file__).parents[1] / "templates" / "style.css").read_text(
            encoding="utf-8"
        )
        self.assertIn(".sec-head .note { grid-column: 1 / -1;", css)

    def test_decision_content_does_not_use_desktop_side_columns(self) -> None:
        css = (Path(__file__).parents[1] / "templates" / "style.css").read_text(
            encoding="utf-8"
        )
        self.assertIn(".decision-grid { display: grid; grid-template-columns: 1fr;", css)
        self.assertIn(".decision-overview { grid-template-columns: 1fr;", css)
        self.assertIn(".role-grid { display: grid; grid-template-columns: 1fr;", css)

    def test_emphasised_fields_are_not_flush_with_the_content_edge(self) -> None:
        css = (Path(__file__).parents[1] / "templates" / "style.css").read_text(
            encoding="utf-8"
        )
        self.assertIn(".field-take { margin-left: 16px;", css)

    def test_home_is_todays_front_page(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "index.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("r.hook", template)
        self.assertIn("first_discoveries", template)
        self.assertIn("important_updates", template)
        self.assertIn("{% for p in items %}", template)
        self.assertIn("t.home.what", template)
        self.assertIn("t.home.why_today", template)
        self.assertIn("daily_report", template)
        self.assertNotIn("reader-routes", template)
        self.assertIn("event_day", template)
        self.assertIn("t.home.daily_flow", template)
        self.assertIn("market_summary", template)
        self.assertIn("t.home.past_reports", template)
        self.assertIn("proven_businesses", template)
        self.assertLess(template.index("daily_report"), template.index("first_discoveries"))
        self.assertLess(template.index("first_discoveries"), template.index("important_updates"))
        self.assertLess(template.index("important_updates"), template.index("market_summary"))
        self.assertLess(template.index("market_summary"), template.index("proven_businesses"))
        # 往期判断放在页面最下方收尾：先看本期内容，最后回看校验。
        self.assertLess(template.index("proven_businesses"), template.index("case_spotlights"))
        self.assertLess(template.index("case_spotlights"), template.index("t.home.past_reports"))
        self.assertNotIn("fresh_picks", template)
        self.assertNotIn("today_takeaway", template)
        self.assertNotIn("more_opportunities", template)
        self.assertNotIn("t.home.movers", template)
        self.assertNotIn("t.home.notables", template)
        self.assertNotIn("t.home.cats", template)
        self.assertNotIn("p.analysis.replaces", template)
        self.assertNotIn("stats.total", template)

    def test_home_uses_latest_publishable_day_instead_of_empty_raw_batch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            ready = product()
            hidden = replace(
                product(), slug="hidden", name="Hidden", summary_zh="", inspiration="",
                first_seen="2026-08-26T10:00:00Z", last_seen="2026-08-26T10:00:00Z",
            )
            store.save_product(ready)
            store.save_product(hidden)
            store.append_event(DiscoveryEvent(
                id="ready", project_slug=ready.slug, event_type=EVENT_FIRST_DISCOVERED,
                occurred_at="2026-08-25T10:00:00Z", discovered_at="2026-08-25T11:00:00Z",
            ))
            store.append_event(DiscoveryEvent(
                id="hidden", project_slug=hidden.slug, event_type=EVENT_FIRST_DISCOVERED,
                occurred_at="2026-08-26T10:00:00Z", discovered_at="2026-08-26T11:00:00Z",
            ))

            ctx = build_context(store, ZH)

            self.assertEqual(ctx["event_day"], "2026-08-25")
            self.assertEqual([item["slug"] for item in ctx["first_discoveries"]], [ready.slug])

    def test_home_ignores_newer_updates_without_an_editorial_fact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            ready = product()
            store.save_product(ready)
            store.append_event(DiscoveryEvent(
                id="ready", project_slug=ready.slug, event_type=EVENT_FIRST_DISCOVERED,
                occurred_at="2026-08-25T10:00:00Z", discovered_at="2026-08-25T11:00:00Z",
            ))
            store.append_event(DiscoveryEvent(
                id="empty-update", project_slug=ready.slug, event_type=EVENT_MATERIAL_UPDATE,
                occurred_at="2026-08-26T10:00:00Z", discovered_at="2026-08-26T11:00:00Z",
                summary="",
            ))

            ctx = build_context(store, ZH)

            self.assertEqual(ctx["event_day"], "2026-08-25")
            self.assertEqual([item["slug"] for item in ctx["first_discoveries"]], [ready.slug])

    def test_daily_event_selection_prefers_category_variety(self) -> None:
        items = [
            {"name": "A", "category_key": "AI + 开发", "status": "queued", "opportunity_rank": 9, "weight": 0},
            {"name": "B", "category_key": "AI + 开发", "status": "queued", "opportunity_rank": 8, "weight": 0},
            {"name": "C", "category_key": "AI + 商业", "status": "queued", "opportunity_rank": 7, "weight": 0},
        ]

        selected = _daily_event_selection(items, limit=2)

        self.assertEqual({item["category_key"] for item in selected}, {"AI + 开发", "AI + 商业"})

    def test_proven_businesses_prefer_scaled_and_category_variety(self) -> None:
        items = [
            {"name": "Settled", "category_key": "通用助手", "form_key": "settled", "usage_value": 100_000_000},
            {"name": "Work A", "category_key": "AI + 效率", "form_key": "scaled", "usage_value": 8_000_000},
            {"name": "Work B", "category_key": "AI + 效率", "form_key": "scaled", "usage_value": 7_000_000},
            {"name": "Creative", "category_key": "AI + 创作", "form_key": "scaled", "usage_value": 5_000_000},
        ]

        selected = _proven_business_selection(items, limit=2)

        self.assertEqual([item["name"] for item in selected], ["Work A", "Creative"])

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

    def test_product_page_hides_metric_that_is_not_product_attributed(self) -> None:
        feature = replace(
            product(),
            sightings=(Sighting(
                "ranking", "https://example.com", "2026-08-13T00:00:00Z",
                {
                    "raw_value": "2.79M",
                    "value": 2_790_000.0,
                    "mom_percent": 49.37,
                    "product_attribution": False,
                },
            ),),
        )

        self.assertEqual(_metric_badges(feature, ZH), [])

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

    def test_public_tags_merge_obvious_aliases_but_keep_search_synonyms(self) -> None:
        fragmented = replace(
            product(),
            industries=("软件", "软件开发", "电子商务"),
            industries_en=("Software development", "Software Development", "E-commerce"),
            jobs=("开发者", "程序员", "AI工程师"),
            jobs_en=("Developers", "Programmer", "AI Engineers"),
            regions=("美国",),
            regions_en=("USA",),
        )

        chinese = product_view(fragmented, ZH)
        english = product_view(fragmented, EN)

        self.assertEqual(chinese["industries"], ["软件开发", "电商"])
        self.assertEqual(chinese["jobs"], ["软件开发者", "AI 工程师"])
        self.assertIn("程序员", chinese["search_terms"])
        self.assertEqual(english["industries"], ["Software Development", "E-commerce"])
        self.assertEqual(english["jobs"], ["Software Developer", "AI Engineer"])
        self.assertEqual(english["regions"], ["United States"])
        self.assertIn("USA", english["search_terms"])

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

    def test_settled_general_assistant_is_published_as_a_proven_business(self) -> None:
        settled = replace(
            product(),
            category="通用助手",
            sightings=(
                Sighting("ranking", "https://example.com", "2026-08-13T00:00:00Z", {"value": 40_000_000, "raw_value": 40_000_000}),
            ),
        )
        self.assertTrue(_is_publishable(settled))

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
        self.assertNotIn("t.product.money_unknown", template)
        self.assertIn("analysis and (analysis.money or analysis.watch_next)", template)
        self.assertIn("t.product.for_investor_k", template)
        self.assertIn("analysis.money", template)

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
        self.assertIn("t.product.story_call", template)
        self.assertIn("t.product.story_tension", template)
        self.assertIn("product.inspiration", template)
        self.assertIn("analysis.money", template)

    def test_home_event_cards_surface_initial_req_and_dates(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "index.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("t.home.what", template)
        self.assertIn("t.home.why_today", template)
        self.assertIn("t.home.keep_asking", template)
        self.assertIn('id="today-cases"', template)
        self.assertIn('id="important-updates"', template)
        self.assertIn('id="past-calls"', template)
        self.assertIn("field-what", template)
        self.assertIn("p.summary", template)
        self.assertIn("p.opportunity_text", template)
        self.assertIn("p.req_next", template)
        self.assertIn("p.req_signal", template)
        self.assertIn("p.opportunity_action", template)
        self.assertNotIn("p.req_reason", template)
        self.assertIn("p.event_day", template)

    def test_opportunity_action_converts_req_gates_into_attention_decision(self) -> None:
        gates = tuple(
            ReqGateReview(gate, REQ_GATE_SUPPORTED if gate == REQ_GATE_VALUE else REQ_GATE_INSUFFICIENT, "具体理由")
            for gate in (REQ_GATE_VALUE, REQ_GATE_CONSENSUS, REQ_GATE_MODEL, REQ_GATE_TRUTH)
        )
        review = ReqReview(
            id="req", project_slug="example", level="initial", reviewed_at="2026-08-24T00:00:00Z",
            verdict=REQ_NEEDS_VALIDATION, signal_level="初步成立", gates=gates,
        )
        self.assertEqual(_opportunity_action(review, ZH), "继续跟踪")
        self.assertEqual(_opportunity_action(review, EN), "Keep watching")
        true_demand = replace(review, verdict="true_demand", signal_level="初步成立")
        self.assertEqual(_opportunity_action(true_demand, ZH), "继续跟踪")
        clue = replace(review, gates=tuple(replace(gate, status=REQ_GATE_INSUFFICIENT) for gate in gates))
        self.assertEqual(_opportunity_action(clue, ZH), "仅作方向线索")

        generic = replace(review, gates=(
            replace(gates[0], status=REQ_GATE_INSUFFICIENT, reason="描述模糊，未明确具体应用场景和用户价值。"),
            *gates[1:],
        ))
        reason = _req_decision_reason(generic, ZH, "货代输入异常运单，系统输出待处置清单。")
        self.assertIn("痛点强度", reason)
        self.assertIn("货代输入异常运单", reason)
        self.assertNotIn("描述模糊", reason)

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
            self.assertIn("proven_businesses", ctx)
            self.assertEqual(ctx["market_summary"][0]["title"], "本期首次发现涉及的行业")

            english = build_context(store, EN)
            self.assertNotIn("、", " ".join(item["text"] for item in english["market_summary"]))

    def test_home_publishes_editorial_market_context_instead_of_hiding_it(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            from xocto.store import Store

            store = Store(Path(tmp))
            context = replace(
                product(),
                slug="agent-economics",
                name="Agent economics",
                status="market_context",
                summary_zh="企业智能体收入与复购上升，说明采购正在从试验转向持续服务。",
                summary_en="Rising agent revenue and repeat purchases show procurement moving from trials to recurring service.",
                inspiration="",
                inspiration_en="",
            )
            store.save_product(context)
            store.append_event(DiscoveryEvent(
                id="first-agent-economics",
                project_slug=context.slug,
                event_type=EVENT_FIRST_DISCOVERED,
                occurred_at="2026-08-14T12:00:00Z",
                discovered_at="2026-08-14T13:00:00Z",
            ))

            chinese = build_context(store, ZH)
            english = build_context(store, EN)

            self.assertTrue(any(item["title"] == "Agent economics" for item in chinese["market_summary"]))
            self.assertTrue(any("repeat purchases" in item["text"] for item in english["market_summary"]))

    def test_market_context_attributes_actual_publisher_from_raw_record(self) -> None:
        from datetime import date
        from xocto.models import RawItem
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            url = "https://news.google.com/rss/articles/example"
            stamp = "2026-08-14T12:00:00Z"
            item = replace(product(), slug="pricing", status="market_context",
                           url=url, summary_zh="平台推理价格下调三成，降低应用调用成本。",
                           summary_en="Inference prices fell 30%, lowering application costs.",
                           sightings=(Sighting("newssearch", url, stamp, {}, kind="news"),))
            store.save_product(item)
            store.append_event(DiscoveryEvent(id="pricing", project_slug=item.slug,
                               event_type=EVENT_FIRST_DISCOVERED, occurred_at=stamp, discovered_at=stamp))
            self.assertFalse(any(row.get("kind") == "context" for row in build_context(store, ZH)["market_summary"]))
            store.append_raw([RawItem(source="newssearch", external_id="pricing", title="Price cut",
                             url=url, summary="Prices fell", published_at=stamp, collected_at=stamp,
                             metrics={}, extra={"publisher": "Example Journal"})], date(2026, 8, 14))
            for locale in (ZH, EN):
                row = next(row for row in build_context(store, locale)["market_summary"] if row.get("kind") == "context")
                self.assertEqual(row["source_name"], "Example Journal")
                self.assertEqual(row["url"], url)

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

            self.assertEqual(ctx["important_updates"], [])

    def test_home_deduplicates_updates_and_honors_homepage_flag(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            from xocto.store import Store

            store = Store(Path(tmp))
            store.save_product(product())
            for event_id, discovered_at, summary, homepage in (
                ("old", "2026-08-14T10:00:00Z", "采用数据首次跨过公开阈值。", True),
                ("new", "2026-08-14T11:00:00Z", "付费方案从免费测试改为按席收费。", True),
                ("hidden", "2026-08-14T12:00:00Z", "不应公开的内部观察。", False),
            ):
                store.append_event(DiscoveryEvent(
                    id=event_id,
                    project_slug="example",
                    event_type=EVENT_MATERIAL_UPDATE,
                    occurred_at=discovered_at,
                    discovered_at=discovered_at,
                    summary=summary,
                    homepage=homepage,
                ))

            ctx = build_context(store, ZH)

            self.assertEqual(len(ctx["important_updates"]), 1)
            self.assertEqual(ctx["important_updates"][0]["event_summary"], "付费方案从免费测试改为按席收费。")

    def test_home_collapses_same_company_split_across_slugs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.save_product(replace(product(), slug="navana-ai", name="Navana.ai"))
            store.save_product(replace(product(), slug="navana-ai-voice", name="Navana.ai"))
            store.append_event(DiscoveryEvent(
                id="upd-navana-1",
                project_slug="navana-ai",
                event_type=EVENT_MATERIAL_UPDATE,
                occurred_at="2026-09-08T10:00:00Z",
                discovered_at="2026-09-08T11:00:00Z",
                summary="Navana.ai 发布新的语音识别接口。",
            ))
            store.append_event(DiscoveryEvent(
                id="upd-navana-2",
                project_slug="navana-ai-voice",
                event_type=EVENT_MATERIAL_UPDATE,
                occurred_at="2026-09-08T10:30:00Z",
                discovered_at="2026-09-08T11:30:00Z",
                summary="Navana.ai 再次出现在公开报道中。",
            ))

            ctx = build_context(store, ZH)

            names = [item["name"] for item in ctx["important_updates"]]
            self.assertEqual(names.count("Navana.ai"), 1)
            self.assertEqual(len(ctx["important_updates"]), 1)

    def test_home_does_not_repeat_first_discovery_as_update_under_alias_slug(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.save_product(replace(product(), slug="zhihu-works", name="知乎AI Works"))
            store.save_product(replace(product(), slug="zhihu-works-update", name="知乎AI Works"))
            store.append_event(DiscoveryEvent(
                id="first-zhihu",
                project_slug="zhihu-works",
                event_type=EVENT_FIRST_DISCOVERED,
                occurred_at="2026-09-08T10:00:00Z",
                discovered_at="2026-09-08T11:00:00Z",
            ))
            store.append_event(DiscoveryEvent(
                id="upd-zhihu",
                project_slug="zhihu-works-update",
                event_type=EVENT_MATERIAL_UPDATE,
                occurred_at="2026-09-08T10:30:00Z",
                discovered_at="2026-09-08T11:30:00Z",
                summary="知乎AI Works 支持应用一键部署。",
            ))

            ctx = build_context(store, ZH)

            self.assertEqual([item["name"] for item in ctx["first_discoveries"]], ["知乎AI Works"])
            self.assertEqual(ctx["important_updates"], [])

    def test_home_market_summary_collapses_same_entity_and_identical_text(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            crusoe_zh = "Crusoe 是一家 AI 基础设施公司，此次新闻仅报道其融资估值。"
            crusoe_en = "Crusoe is an AI infrastructure company; this report only covers valuation."
            stub_zh = "该 AI 产品提供了新的能力，但现有公开材料尚不足以确认其具体工作流价值。"
            stub_en = "Public materials are not yet enough to confirm a concrete workflow."
            store.save_product(replace(
                product(), slug="crusoe-1", name="Crusoe", status="market_context",
                summary_zh=crusoe_zh, summary_en=crusoe_en, inspiration="",
                url="https://news.example.com/crusoe-1",
            ))
            store.save_product(replace(
                product(), slug="crusoe-2", name="Crusoe", status="market_context",
                summary_zh=crusoe_zh, summary_en=crusoe_en, inspiration="",
                url="https://news.example.com/crusoe-2",
            ))
            store.save_product(replace(
                product(), slug="soundhound", name="SoundHound AI", status="market_context",
                summary_zh=stub_zh, summary_en=stub_en, inspiration="",
                url="https://news.example.com/soundhound",
            ))
            store.save_product(replace(
                product(), slug="uber-ai", name="Uber", status="market_context",
                summary_zh=stub_zh, summary_en=stub_en, inspiration="",
                url="https://news.example.com/uber",
            ))
            store.save_product(replace(
                product(), slug="isar", name="Isar Aerospace", status="market_context",
                summary_zh="德国火箭二次飞行进入轨道并部署载荷。",
                summary_en="A second test flight reached orbit and deployed a payload.",
                inspiration="", url="https://isar.example.com",
            ))
            for slug, stamp in (
                ("crusoe-1", "2026-09-08T10:00:00Z"),
                ("crusoe-2", "2026-09-08T10:10:00Z"),
                ("soundhound", "2026-09-08T10:20:00Z"),
                ("uber-ai", "2026-09-08T10:30:00Z"),
                ("isar", "2026-09-08T10:40:00Z"),
            ):
                store.append_event(DiscoveryEvent(
                    id=f"first-{slug}",
                    project_slug=slug,
                    event_type=EVENT_FIRST_DISCOVERED,
                    occurred_at=stamp,
                    discovered_at=stamp,
                ))

            ctx = build_context(store, ZH)
            titles = [item["title"] for item in ctx["market_summary"] if item.get("kind") == "context"]
            texts = [item["text"] for item in ctx["market_summary"] if item.get("kind") == "context"]

            self.assertEqual(titles.count("Crusoe"), 1)
            self.assertEqual(texts.count(crusoe_zh), 1)
            self.assertEqual(texts.count(stub_zh), 0)
            self.assertNotIn("Uber", titles)
            self.assertNotIn("SoundHound AI", titles)
            for item in ctx["market_summary"]:
                if item.get("kind") == "context":
                    self.assertTrue(item["source_name"])
            self.assertEqual(titles.count("Isar Aerospace"), 1)

    def test_same_day_full_req_review_wins_over_later_initial_timestamp(self) -> None:
        initial = ReqReview(
            id="initial", project_slug="example", level="initial",
            reviewed_at="2026-08-14T23:00:00Z", verdict=REQ_NEEDS_VALIDATION,
            signal_level="待验证", gates=tuple(
                ReqGateReview(gate, REQ_GATE_INSUFFICIENT, "基础初判")
                for gate in (REQ_GATE_VALUE, REQ_GATE_CONSENSUS, REQ_GATE_MODEL, REQ_GATE_TRUTH)
            ),
        )
        full = replace(initial, id="full", level="full", reviewed_at="2026-08-14T18:00:00Z")
        self.assertIs(_latest_req_review([initial, full]), full)

    def test_full_req_review_is_not_downgraded_by_a_newer_day_initial_review(self) -> None:
        initial = ReqReview(
            id="req-initial-example-2026-08-15", project_slug="example", level="initial",
            reviewed_at="2026-08-15T10:00:00Z", verdict=REQ_NEEDS_VALIDATION,
            signal_level="需求存疑", gates=tuple(
                ReqGateReview(gate, REQ_GATE_INSUFFICIENT, "基础初判")
                for gate in (REQ_GATE_VALUE, REQ_GATE_CONSENSUS, REQ_GATE_MODEL, REQ_GATE_TRUTH)
            ),
        )
        full = replace(initial, id="req-full-example-2026-08-14", level="full", reviewed_at="2026-08-14T18:00:00Z")
        self.assertIs(_latest_req_review([initial, full]), full)

    def test_opportunity_library_offers_parallel_dimensions_and_shareable_date_filters(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "products.html").read_text(
            encoding="utf-8"
        )
        for dim in ("projectType", "openSource", "crossMarket", "req"):
            self.assertIn(f'data-dim="{dim}"', template)
        for dim in ("industry", "job", "region"):
            self.assertIn(f"('{dim}', opportunity_filters.", template)
        self.assertIn('id="date-from"', template)
        self.assertIn('id="date-to"', template)
        self.assertIn("data-discovered", template)
        self.assertIn("dateFrom", template)
        self.assertIn("dateTo", template)
        self.assertIn('id="product-search"', template)
        self.assertIn('class="advanced-controls"', template)
        self.assertIn('class="facet-select"', template)
        self.assertIn("active.search", template)
        self.assertIn("var PAGE_SIZE = 40", template)
        self.assertIn('id="load-more"', template)
        self.assertIn("visibleLimit += PAGE_SIZE", template)
        self.assertNotIn("data-search=", template)
        self.assertIn("card._searchText", template)
        self.assertNotIn('class="card-insp"', template)
        self.assertNotIn("p.inspiration", template)

    def test_public_product_view_neutralizes_collection_channel_names(self) -> None:
        source_named = replace(
            product(),
            name="Crunchbase News",
            summary_zh="TechCrunch 报道了一项市场变化。",
            summary_en="TechCrunch reported a market development.",
        )

        chinese = product_view(source_named, ZH)
        english = product_view(source_named, EN)

        self.assertEqual(chinese["name"], "市场动态")
        self.assertEqual(english["name"], "Market development")
        self.assertNotIn("TechCrunch", chinese["summary"])
        self.assertNotIn("TechCrunch", english["summary"])

    def test_opportunity_library_counts_each_business_form_bucket(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            early = product()
            settled = replace(
                product(), slug="settled", name="Settled", category="通用助手",
                sightings=(Sighting(
                    "ranking", "https://example.com/settled", "2026-08-13T00:00:00Z",
                    {"value": 40_000_000, "raw_value": 40_000_000},
                ),),
            )
            store.save_product(early)
            store.save_product(settled)

            ctx = build_context(store, ZH)

            self.assertEqual(ctx["form_counts"]["not_business"], 1)
            self.assertEqual(ctx["form_counts"]["settled"], 1)
            self.assertEqual(sum(ctx["form_counts"].values()), 2)

    def test_detail_research_view_keeps_market_coverage_and_marks_cross_market_only_from_snapshots(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            from xocto.store import Store

            store = Store(Path(tmp))
            store.save_product(replace(
                product(), slug="freight-ai", name="Freight AI",
                summary="Helps freight teams resolve shipment exceptions.",
                summary_zh="货代团队用它处理运输异常并输出待处置清单。",
            ))
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
            store.append_evidence(replace(evidence, id="ev-product-duplicate"))
            store.append_evidence(Evidence(
                id="ev-query", project_slug="freight-ai",
                url="https://www.bing.com/search?format=rss&q=freight",
                title="Public market coverage query", published_at="", collected_at="2026-08-14T10:00:00Z",
                source_kind="market_comparison", tier="independent", fact="Public query",
            ))
            store.append_evidence(Evidence(
                id="ev-generic", project_slug="freight-ai", url="https://chatgpt.com",
                title="ChatGPT: Chat, Work, Create & Code with AI", published_at="", collected_at="2026-08-14T10:00:00Z",
                source_kind="market_comparison", tier="independent", fact="Answer questions, write, and code.",
            ))
            store.append_evidence(Evidence(
                id="ev-aggregator", project_slug="freight-ai",
                url="https://www.producthunt.com/products/freight-ai",
                title="Freight AI", published_at="2026-08-14T09:00:00Z",
                collected_at="2026-08-14T10:00:00Z", source_kind="product",
                tier="independent", fact="Launch page.",
            ))
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
            self.assertEqual(research["req"]["gates"][0]["evidence"][0]["url"], "https://example.com")
            self.assertEqual(research["evidence"][0]["title"], "Freight AI")
            self.assertEqual(len(research["evidence"]), 1)
            self.assertNotIn("producthunt", research["evidence"][0]["url"])
            self.assertIn("货代团队", research["evidence"][0]["fact"])
            self.assertNotIn("Shipment-exception", research["evidence"][0]["fact"])

            english = _research_view(store, "freight-ai", EN)
            self.assertEqual(english["req"]["signal"], "Demand is evidenced")
            self.assertEqual(english["req"]["verdict_label"], "Demand is evidenced")
            self.assertEqual(english["req"]["evidence_signal"], "Initial support")
            self.assertEqual(english["req"]["gates"][0]["reason"], EN.t["product"]["req_reason_pending"])
            self.assertEqual(english["req"]["next_validation"], EN.t["product"]["req_next_pending"])
            self.assertNotRegex(english["evidence"][0]["fact"], r"[一-鿿]")
            self.assertTrue(any(
                row["coverage"] == EN.t["product"]["market_coverage_pending"]
                for row in english["markets"]
            ))
            self.assertTrue(research["req"]["job"])
            self.assertTrue(research["req"]["pain"])
            self.assertTrue(research["req"]["usage_reason"])
            self.assertEqual(len(research["research_links"]), 5)

    def test_product_template_surfaces_req_market_and_evidence_sections(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "product.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("t.product.story_title", template)
        self.assertIn("t.product.story_kicker", template)
        self.assertIn("product.req.usage_reason", template)
        self.assertIn("product.req.known_fact", template)
        self.assertIn("product.req.inference", template)
        self.assertIn("product.req.unknown", template)
        self.assertIn("product.req.gates", template)
        self.assertIn("gate.evidence", template)
        # 模板改版后证据边界改为 product-evidence 折叠块，默认展开。
        self.assertIn('<details class="product-evidence" open>', template)
        self.assertNotIn("product.req.business_maturity", template)
        self.assertIn("t.product.markets_title", template)
        self.assertIn("product.cross_market", template)
        self.assertIn("t.product.evidence_title", template)
        self.assertIn("product.evidence", template)
        self.assertIn("product.research_links", template)

    def test_product_page_answers_is_it_a_business_first(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "product.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("t.product.story_scene", template)
        self.assertIn("t.product.story_call", template)
        self.assertIn("t.product.story_adoption", template)
        self.assertIn("t.product.story_tension", template)
        self.assertLess(template.index("t.product.story_scene"), template.index("t.product.story_call"))
        self.assertLess(template.index("t.product.story_call"), template.index("t.product.story_adoption"))
        self.assertLess(template.index("t.product.story_adoption"), template.index("t.product.story_tension"))
        self.assertLess(template.index("t.product.story_tension"), template.index("t.product.story_for_user"))
        self.assertLess(template.index("t.product.story_for_user"), template.index("t.product.story_evidence"))

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

    def test_static_site_versions_its_stylesheet(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "base.html").read_text(
            encoding="utf-8"
        )
        self.assertIn('style.css?v={{ asset_version }}', template)

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


class PlaybookIndexTests(unittest.TestCase):
    def test_blank_takeaway_drops_no_method_notes(self) -> None:
        self.assertTrue(_blank_takeaway("无。"))
        self.assertTrue(_blank_takeaway("无。技术文档，没有可偷的句式。"))
        self.assertTrue(_blank_takeaway("无。官网是工程文档，没有可偷的句式。"))
        self.assertTrue(_blank_takeaway("None. README is an engineering doc."))
        self.assertTrue(_blank_takeaway("无。未披露。"))
        self.assertTrue(_blank_takeaway("无，未披露。"))
        self.assertFalse(_blank_takeaway('无。但"非营利 + 捐赠"是可参考的成立方式。'))
        self.assertFalse(_blank_takeaway(
            'none. But "nonprofit + donations" is a viable structure.'
        ))
        self.assertFalse(_blank_takeaway(
            "无特别可偷的句式，它的发布文案靠具体细节（「截图取点击前那一帧」）"
        ))
        self.assertFalse(_blank_takeaway(
            "无。标题太技术化，反而值得引以为戒——工具要有可传播的一句话。"
        ))

    def test_public_method_text_leads_with_the_move(self) -> None:
        self.assertEqual(_public_method_text("无。技术文档，没有可偷的句式。"), "")
        self.assertEqual(
            _public_method_text('可偷一句："Agents grade their own homework."'),
            '"Agents grade their own homework."',
        )
        self.assertEqual(
            _public_method_text(
                "无特别可偷的句式，它的发布文案靠具体细节（「截图取点击前那一帧」）"
            ),
            "它的发布文案靠具体细节（「截图取点击前那一帧」）",
        )
        self.assertEqual(
            _public_method_text('无。但"非营利 + 捐赠"是可参考的成立方式。'),
            '"非营利 + 捐赠"是可参考的成立方式。',
        )
        self.assertEqual(
            _public_method_text(
                'none. But "nonprofit + donations" is a viable structure.'
            ),
            '"nonprofit + donations" is a viable structure.',
        )

    def test_english_positioning_language_maps_to_how_to_say_it(self) -> None:
        topics = _takeaway_topics(
            """## What you can take from it

**Product logic**: put verification outside the agent.

**Positioning language**: one line worth stealing — "Agents grade their own homework."

**Pricing structure**: founding user price first.
""",
            "What you can take from it",
        )
        self.assertEqual(
            _public_method_text(topics["narrative"]),
            '"Agents grade their own homework."',
        )
        self.assertFalse(_blank_takeaway(
            "none. Its HN title was too technical — which is itself the lesson: a tool needs one shareable sentence."
        ))
        zh_topics = _takeaway_topics(
            """## 可借鉴的做法

**定位语**："你说话，它操作"。

**定价**：无定价本身就是卖点。
""",
            "可借鉴的做法",
        )
        self.assertEqual(_public_method_text(zh_topics["narrative"]), '"你说话，它操作"。')
        self.assertIn("无定价本身就是卖点", _public_method_text(zh_topics["pricing"]))
        en_short = _takeaway_topics(
            """## What you can take from it

**Positioning**: "in your own voice."
""",
            "What you can take from it",
        )
        self.assertEqual(_public_method_text(en_short["narrative"]), '"in your own voice."')

    def test_playbook_copy_answers_what_functions_and_reference(self) -> None:
        zh = ZH.t["takeaways"]
        en = EN.t["takeaways"]
        self.assertEqual(zh["what"], "这是什么")
        self.assertEqual(zh["functions"], "功能")
        self.assertEqual(zh["reference"], "可参考")
        blob = " ".join(str(value) for value in zh.values())
        self.assertNotIn("文案结构", blob)
        self.assertNotIn("可偷", blob)
        self.assertNotIn("可抄", blob)
        en_blob = " ".join(str(value) for value in en.values()).lower()
        self.assertNotIn("steal", en_blob)
        self.assertNotIn("copyable", en_blob)
        self.assertNotIn("stealable", en_blob)
        self.assertEqual(en["what"], "What it is")
        self.assertEqual(en["functions"], "What it does")
        self.assertEqual(en["reference"], "Worth taking")

    def test_playbook_case_shows_what_functions_and_reference(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            store.save_product(product())
            (store.analysis_dir / "example.md").write_text(
                """---
slug: example
name: Example
verdict: 有待观察
analyzed_at: 2026-08-14
---

## 一句话定位

独立于 agent 的目击证人。

## 它到底能做哪几件事

- commit 前做像素对比
- 没动过的页面验证为一致

## 可借鉴的做法

**产品逻辑**：把验收放到被检查方够不着的地方。

**话术**："Agents grade their own homework."

**定价结构**：创始人价先收，版本发布才扣。
""",
                encoding="utf-8",
            )
            ctx = build_context(store, ZH)
            self.assertEqual(len(ctx["playbook_cases"]), 1)
            case = ctx["playbook_cases"][0]
            self.assertEqual(case["name"], "Example")
            self.assertIn("目击证人", case["what"])
            self.assertEqual(
                case["functions"],
                "commit 前做像素对比；没动过的页面验证为一致",
            )
            self.assertEqual(
                case["refs"],
                ["把验收放到被检查方够不着的地方。", "创始人价先收，版本发布才扣。"],
            )
            self.assertFalse(any("homework" in item for item in case["refs"]))
            self.assertNotIn("verdict", case)
            self.assertNotIn("verdict_key", case)
            analysis = load_analyses(store, ZH)[0]
            self.assertIn("验收", analysis.takeaway)
            self.assertIn("创始人价", analysis.takeaway)
            self.assertNotIn("homework", analysis.takeaway)
            self.assertNotIn("话术", analysis.body_html)
            self.assertNotIn("homework", analysis.body_html)
            self.assertEqual(case["url"], "https://example.com")
            self.assertEqual(case["url_host"], "example.com")

    def test_public_page_url_keeps_product_hosts_hides_collection_hosts(self) -> None:
        self.assertEqual(_public_page_url("https://sightdiff.com/"), "https://sightdiff.com/")
        self.assertEqual(
            _public_page_url("https://foo.vercel.app/"),
            "https://foo.vercel.app/",
        )
        self.assertEqual(_public_page_url("https://www.producthunt.com/posts/x"), "")
        self.assertEqual(_public_page_url("https://news.ycombinator.com/item?id=1"), "")

    def test_playbook_skips_cases_with_nothing_to_reference(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            store.save_product(product())
            (store.analysis_dir / "example.md").write_text(
                """---
slug: example
name: Example
verdict: 有待观察
analyzed_at: 2026-08-14
---

## 一句话定位

一个时钟页面。

## 可借鉴的做法

**产品逻辑**：无。

**话术**：无。技术文档，没有可偷的句式。

**定价结构**：无。未披露。
""",
                encoding="utf-8",
            )
            ctx = build_context(store, ZH)
            self.assertEqual(ctx["playbook_cases"], [])

    def test_takeaways_template_reads_as_case_cards(self) -> None:
        template = (Path(__file__).parents[1] / "templates" / "takeaways.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("playbook_cases", template)
        self.assertIn("t.takeaways.what", template)
        self.assertIn("t.takeaways.functions", template)
        self.assertIn("t.takeaways.reference", template)
        self.assertIn("t.takeaways.site", template)
        self.assertIn("item.url", template)
        self.assertLess(template.index("t.takeaways.what"), template.index("t.takeaways.functions"))
        self.assertLess(template.index("t.takeaways.functions"), template.index("t.takeaways.reference"))
        self.assertNotIn("item.verdict", template)
        self.assertNotIn("topic_product", template)


class EvidenceLocalizationTests(unittest.TestCase):
    @staticmethod
    def _item(title: str, fact: str) -> Evidence:
        return Evidence(
            id="ev-1", project_slug="compute",
            url="https://finance.biggo.com/news/x",
            title=title,
            published_at="2026-09-05T00:00:00Z",
            collected_at="2026-09-06T00:00:00Z",
            source_kind="market_signal",
            tier="independent",
            fact=fact,
        )

    def test_chinese_evidence_never_dumps_full_english_headlines(self) -> None:
        # 全角分隔符「｜」也匹配 CJK，但不能因此把整段英文标题倒进中文证据链。
        title, fact = _localized_evidence_copy(
            self._item(
                "Everyone Gets A Software Company — Benjamin Guo, Zo Computer｜AI Engineer",
                "Everyone Gets A Software Company — Benjamin Guo, Zo Computer｜AI Engineer finance.biggo.com",
            ),
            None,
            ZH,
        )
        self.assertNotIn("Everyone Gets A Software Company", title)
        self.assertNotIn("Everyone Gets A Software Company", fact)

    def test_mixed_chinese_title_keeps_its_chinese_part(self) -> None:
        title, _ = _localized_evidence_copy(
            self._item(
                "AI Engineer 专访：Everyone Gets A Software Company — Benjamin Guo",
                "",
            ),
            None,
            ZH,
        )
        self.assertIn("AI Engineer 专访", title)
        self.assertNotIn("Everyone Gets A Software Company", title)

    def test_product_name_title_still_wins_over_host_fallback(self) -> None:
        item = self._item("Example", "")
        example = product()
        title, _ = _localized_evidence_copy(item, example, ZH)
        self.assertEqual(title, "Example")


if __name__ == "__main__":
    unittest.main()
