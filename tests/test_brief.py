from __future__ import annotations

from dataclasses import replace
from datetime import date
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from xocto.brief import (
    BriefError,
    PublicSourceLeakError,
    _candidate_data,
    _decode_json_object,
    _event_summaries,
    _interpretation_prompt,
    _interpretations,
    _model_providers,
    _neutralize_model_public_copy,
    _neutralize_public_source_names,
    _normalize_model_public_text_types,
    _prompt,
    _public_source_leaks,
    _report_prompt,
    _report_markdown,
    _recover_missing_public_text,
    _require_no_public_source_leaks,
    _require_priority_coverage,
    _req_reviews,
    _estimate_payload_bytes,
    _fit_messages,
    _split_batches,
    _updates,
    _validation_repair_messages,
    candidates_for_day,
    news_for_day,
    report_context,
    run,
)
from xocto.models import Evidence, Product, RawItem, STATUS_MARKET_CONTEXT, STATUS_PENDING_FILTER, STATUS_WATCHING, Sighting
from xocto.store import Store


DAY = date(2026, 8, 14)


def product(slug: str = "example", *, last_seen: str = "2026-08-13T23:10:00Z") -> Product:
    return Product(
        slug=slug,
        name="Example",
        url="https://example.com",
        canonical_url="https://example.com",
        summary="A concrete AI product.",
        first_seen=last_seen,
        last_seen=last_seen,
        status=STATUS_PENDING_FILTER,
        sightings=(Sighting("github", "https://example.com", last_seen, {"stars": 20}),),
    )


class BriefTests(unittest.TestCase):
    def test_product_prompt_requires_a_workflow_level_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            store.config_dir.mkdir(parents=True, exist_ok=True)
            (store.config_dir / "filter.md").write_text("筛选规则", encoding="utf-8")
            (store.config_dir / "template.md").write_text("编辑模板", encoding="utf-8")
            (store.config_dir / "req.md").write_text("REQ 公开证据模式", encoding="utf-8")

            prompt = _prompt(store, DAY, [product()], [])

            self.assertIn("60–130 个中文字符", prompt[0]["content"])
            self.assertIn("具体工作节点", prompt[0]["content"])
            self.assertIn("用户最终拿到什么", prompt[0]["content"])
            self.assertIn("REQ 公开证据模式", prompt[0]["content"])
            self.assertIn("筛选规则", prompt[1]["content"])
            self.assertNotIn("编辑模板", str(prompt))
            self.assertNotIn("previous_report_zh", str(prompt))

    def test_news_interpretation_separates_entities_from_public_market_context(self) -> None:
        entity = replace(
            product("entity"),
            name="A revenue headline",
            sightings=(Sighting("marketfeeds", "https://news.example/entity", "2026-08-13T23:10:00Z", {}, kind="news"),),
        )
        context = replace(
            product("context"),
            sightings=(Sighting("newssearch", "https://news.example/context", "2026-08-13T23:10:00Z", {}, kind="news"),),
        )
        result = {
            "products": [
                {
                    "slug": "entity",
                    "name": "Stable AI Company",
                    "decision": "entity",
                    "event_summary_zh": "公司披露企业智能体业务收入与客户复购增长。",
                    "event_summary_en": "The company disclosed revenue growth and repeat purchases for its enterprise agent business.",
                },
                {
                    "slug": "context",
                    "name": "Enterprise agent pricing",
                    "decision": "market_context",
                    "summary_zh": "企业智能体采购正在从试点转向持续服务与结果付费。",
                    "summary_en": "Enterprise agent procurement is moving from pilots to recurring services and outcome-based spending.",
                    "event_summary_zh": "多家供应商开始披露持续服务与结果收费安排。",
                    "event_summary_en": "Multiple vendors began disclosing recurring service and outcome-based pricing arrangements.",
                },
            ]
        }

        updates, entities, events = _interpretations(result, [entity, context])

        self.assertEqual([item.name for item in entities], ["Stable AI Company"])
        self.assertEqual(updates["context"].status, STATUS_MARKET_CONTEXT)
        self.assertEqual(set(events), {"entity", "context"})

    def test_news_interpretation_prompt_is_lightweight_and_entity_first(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            prompt = _interpretation_prompt(store, [product()])
        self.assertIn("载体不等于对象", prompt[0]["content"])
        self.assertIn("entity|market_context|rejected", prompt[0]["content"])
        self.assertNotIn("req_initial", prompt[0]["content"])

    def test_oversized_batch_is_split_in_the_caller(self) -> None:
        # 预检拒绝请求体超限的批次时，责任在调用方：对半拆到每一批都装得下，
        # 且覆盖关系不丢。这里每个候选约 31KB，两条就超过 32KB 上限。
        def build(items: list) -> list[dict[str, str]]:
            payload = "x" * (31_000 * len(items))
            return [
                {"role": "system", "content": "s"},
                {"role": "user", "content": payload},
            ]

        items = [product(f"p{i}") for i in range(4)]
        batches = _split_batches(items, build)
        self.assertEqual([len(batch) for batch in batches], [1, 1, 1, 1])
        self.assertEqual(
            [item.slug for batch in batches for item in batch],
            [f"p{i}" for i in range(4)],
        )

        single = [product("only")]
        self.assertEqual(_split_batches(single, build), [single])

    def test_compact_candidate_data_truncates_text_but_keeps_evidence_ids(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.save_product(item)
            store.append_evidence(Evidence(
                id="ev-1", project_slug="example",
                url="https://news.example/story",
                title="T" * 400,
                published_at="2026-08-13T00:00:00Z",
                collected_at="2026-08-13T00:00:00Z",
                source_kind="market_signal",
                tier="independent",
                fact="F" * 2000,
            ))

            full = _candidate_data(store, item)
            compact = _candidate_data(store, item, compact=True)

        self.assertEqual(compact["evidence"][0]["id"], "ev-1")
        self.assertLessEqual(len(compact["evidence"][0]["fact"]), 700)
        self.assertEqual(len(full["evidence"][0]["fact"]), 2000)
        self.assertLessEqual(len(compact["source_summary"]), 700)

    def test_evidence_limit_keeps_only_the_most_recent_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.save_product(item)
            for index in range(4):
                store.append_evidence(Evidence(
                    id=f"ev-{index}", project_slug="example",
                    url=f"https://news.example/{index}",
                    title=f"story {index}",
                    published_at="2026-08-13T00:00:00Z",
                    collected_at="2026-08-13T00:00:00Z",
                    source_kind="market_signal",
                    tier="independent",
                    fact=f"fact {index}",
                ))

            limited = _candidate_data(store, item, evidence_limit=2)

        self.assertEqual(
            [row["id"] for row in limited["evidence"]], ["ev-2", "ev-3"]
        )

    def test_fit_messages_escalates_until_the_request_fits(self) -> None:
        calls: list[tuple[bool, int | None]] = []

        def build(items: list, compact: bool, limit: int | None) -> list[dict[str, str]]:
            calls.append((compact, limit))
            size = 35_000 if not compact or limit is None else 1_000 * limit
            return [
                {"role": "system", "content": "s"},
                {"role": "user", "content": "x" * size},
            ]

        messages = _fit_messages([product()], build)

        self.assertLessEqual(_estimate_payload_bytes(messages), 32000)
        self.assertEqual(calls[-1], (True, 12))
        self.assertEqual(calls[0], (False, None))

    def test_news_event_summary_falls_back_to_validated_product_copy(self) -> None:
        news = replace(
            product("cover"),
            sightings=(
                Sighting(
                    "marketfeeds",
                    "https://news.example/cover",
                    "2026-08-13T23:10:00Z",
                    {},
                    kind="news",
                ),
            ),
        )
        result = {
            "products": [{
                "slug": "cover",
                "decision": "watching",
                "summary_zh": "企业正在改变内容审核与发布流程。",
                "summary_en": "Enterprises are changing content review and publishing workflows.",
            }]
        }

        summaries = _event_summaries(result, [news])

        self.assertEqual(summaries["cover"], (
            "企业正在改变内容审核与发布流程。",
            "Enterprises are changing content review and publishing workflows.",
        ))

    def test_gemini_can_be_the_primary_model_with_deepseek_fallback(self) -> None:
        with patch.dict(
            "os.environ",
            {
                "GEMINI_API_KEY": "gemini-key",
                "DEEPSEEK_API_KEY": "deepseek-key",
                "MODEL_PROVIDER": "gemini",
            },
            clear=True,
        ):
            providers = _model_providers()
        self.assertEqual([item[0] for item in providers], ["gemini", "deepseek"])
        self.assertEqual(providers[0][1], "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions")

    def test_groq_defaults_to_a_production_free_model(self) -> None:
        with patch.dict("os.environ", {"GROQ_API_KEY": "groq-key", "MODEL_PROVIDER": "groq"}, clear=True):
            providers = _model_providers()
        self.assertEqual(providers, [("groq", "https://api.groq.com/openai/v1/chat/completions", "groq-key", "openai/gpt-oss-20b")])

    def test_groq_prefers_gemini_before_deepseek_as_its_fallback(self) -> None:
        with patch.dict(
            "os.environ",
            {"GROQ_API_KEY": "groq-key", "GEMINI_API_KEY": "gemini-key", "DEEPSEEK_API_KEY": "deepseek-key", "MODEL_PROVIDER": "groq"},
            clear=True,
        ):
            providers = _model_providers()
        self.assertEqual([item[0] for item in providers], ["groq", "gemini", "deepseek"])

    def test_json_decoder_accepts_a_fenced_object_but_rejects_truncation(self) -> None:
        self.assertEqual(_decode_json_object("```json\n{\"products\": []}\n```"), {"products": []})
        with self.assertRaises(BriefError):
            _decode_json_object('{"products": [')

    def test_validation_repair_keeps_the_original_result_and_names_the_failure(self) -> None:
        messages = [{"role": "system", "content": "rules"}]
        repaired = _validation_repair_messages(messages, {"products": []}, BriefError("field is too short"))
        self.assertEqual(repaired[-2]["role"], "assistant")
        self.assertIn("field is too short", repaired[-1]["content"])

    def test_daily_report_prompt_keeps_priority_products_in_scope(self) -> None:
        priority = replace(product("priority"), name="Priority project", priority_review=True)
        prompt = _report_prompt(DAY, [priority], [])
        self.assertIn("Priority project", prompt[0]["content"])
        self.assertIn("selected_products", prompt[1]["content"])
        self.assertIn("正向方向判断", prompt[0]["content"])
        self.assertNotIn("今天没有值得展开的内容时", prompt[0]["content"])

    def test_editorial_market_context_is_a_first_class_report_input(self) -> None:
        context = replace(
            product("agent-economics"),
            name="Agent economics",
            status=STATUS_MARKET_CONTEXT,
            summary_zh="企业智能体采购正在从试点转向按结果持续付费。",
            summary_en="Enterprise agent procurement is shifting from pilots to recurring outcome-based spending.",
        )
        rows = report_context(
            [context],
            [
                {"title": "duplicate raw report", "url": context.url},
                {"title": "legacy raw report", "url": "https://news.example/legacy"},
            ],
        )
        self.assertEqual([row.get("kind") for row in rows], ["market_context", None])
        prompt = _report_prompt(DAY, [context], rows)
        self.assertIn("正式市场背景", prompt[0]["content"])
        self.assertIn("企业智能体采购", prompt[1]["content"])

    def test_existing_daily_report_is_revised_when_a_later_candidate_arrives(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            store.config_dir.mkdir(parents=True, exist_ok=True)
            (store.config_dir / "filter.md").write_text("筛选规则", encoding="utf-8")
            (store.config_dir / "template.md").write_text("编辑模板", encoding="utf-8")
            (store.config_dir / "req.md").write_text("REQ 公开证据模式", encoding="utf-8")
            store.save_product(product())
            store.save_report("旧版观察", DAY)
            store.save_report("Previous edition", DAY, locale="en")
            product_result = {
                "products": [{
                    "slug": "example",
                    "name": "Example",
                    "decision": "market_context",
                    "summary_zh": "这项新变化改变了企业采用智能工具的采购与交付方式。",
                    "summary_en": "This new shift changes how enterprises procure and deploy intelligent tools.",
                }]
            }
            report_result = {
                "report": {
                    "hook_zh": "企业采购信号正在从试用走向持续交付",
                    "highlights_zh": ["一项新增市场变化已进入当日观察"],
                    "body_zh": "## 当日变化\n\n新增事实已合并进晚间版本。",
                    "hook_en": "Enterprise buying signals are moving from trials to recurring delivery",
                    "highlights_en": ["A new market shift entered today's view"],
                    "body_en": "## Daily shift\n\nThe new fact is included in the evening revision.",
                }
            }
            with patch("xocto.brief._request", side_effect=[product_result, report_result]) as request:
                result = run(store, day=DAY)

            self.assertFalse(result.skipped)
            self.assertEqual(request.call_count, 2)
            self.assertIn("旧版观察", request.call_args_list[1].args[0][1]["content"])
            self.assertIn("晚间版本", store.report_path(DAY).read_text(encoding="utf-8"))

    def test_report_markdown_rejects_empty_day_copy(self) -> None:
        result = {
            "report": {
                "hook_zh": "今天没有值得展开的产品",
                "highlights_zh": ["采集完成"],
                "body_zh": "## 今日观察\n\n今天没有值得展开的产品。",
                "hook_en": "No product worth expanding today",
                "highlights_en": ["Collection finished"],
                "body_en": "## Today's note\n\nNo editorial pick today.",
            }
        }
        with self.assertRaises(BriefError):
            _report_markdown(result, DAY, english=False)
        with self.assertRaises(BriefError):
            _report_markdown(result, DAY, english=True)

    def test_empty_candidate_day_is_a_filter_failure_not_a_publishable_edition(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            with self.assertRaises(BriefError) as ctx:
                run(store, day=DAY)
            self.assertIn("过滤或采集故障", str(ctx.exception))
            self.assertFalse(store.report_path(DAY).exists())

    def test_only_today_pending_products_are_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.save_product(product("today"))
            store.save_product(product("old", last_seen="2026-08-12T01:00:00Z"))
            store.save_product(replace(product("rejected"), status="rejected"))

            self.assertEqual([item.slug for item in candidates_for_day(store, DAY)], ["today"])

    def test_official_news_is_available_to_the_report_but_not_the_product_pool(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.append_raw(
                [
                    RawItem(
                        source="officialfeeds",
                        external_id="announcement",
                        title="A documented product update",
                        url="https://example.com/announcement",
                        summary="A first-party announcement.",
                        published_at="2026-08-14T12:00:00Z",
                        collected_at="2026-08-14T13:00:00Z",
                        metrics={},
                        extra={"kind": "news", "official": True},
                        payload={},
                    )
                ],
                DAY,
            )
            self.assertEqual(candidates_for_day(store, DAY), [])
            self.assertEqual(news_for_day(store, DAY)[0]["title"], "A documented product update")
            self.assertTrue(news_for_day(store, DAY)[0]["first_party"])

    def test_independent_and_discussion_news_reach_the_daily_brief(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.append_raw(
                [
                    RawItem(
                        source="officialfeeds",
                        external_id="blogger",
                        title="An independent observation",
                        url="https://example.com/notes/observation",
                        summary="A writer explains who is paying.",
                        published_at="2026-08-14T11:00:00Z",
                        collected_at="2026-08-14T13:00:00Z",
                        metrics={},
                        extra={"kind": "news", "official": False},
                    ),
                    RawItem(
                        source="hackernews",
                        external_id="discussion",
                        title="A widely discussed AI launch",
                        url="https://example.com/launch",
                        summary="Public discussion of a new product.",
                        published_at="2026-08-14T10:00:00Z",
                        collected_at="2026-08-14T13:00:00Z",
                        metrics={},
                        extra={"kind": "news"},
                    ),
                    RawItem(
                        source="producthunt",
                        external_id="app",
                        title="A new app",
                        url="https://example.com/app",
                        summary="",
                        published_at="2026-08-14T09:00:00Z",
                        collected_at="2026-08-14T13:00:00Z",
                        metrics={},
                        extra={"kind": "product"},
                    ),
                ],
                DAY,
            )
            titles = [row["title"] for row in news_for_day(store, DAY)]
            self.assertEqual(
                titles,
                ["An independent observation", "A widely discussed AI launch"],
            )
            self.assertFalse(news_for_day(store, DAY)[0]["first_party"])
            self.assertFalse(news_for_day(store, DAY)[1]["first_party"])

    def test_first_party_news_does_not_crowd_out_independent_signals(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            items = [
                RawItem(
                    source="officialfeeds",
                    external_id=f"lab-{index}",
                    title=f"Lab update {index:02d}",
                    url=f"https://example.com/lab/{index}",
                    summary="A first-party changelog.",
                    published_at=f"2026-08-14T{index:02d}:00:00Z",
                    collected_at="2026-08-14T13:00:00Z",
                    metrics={},
                    extra={"kind": "news", "official": True},
                )
                for index in range(14)
            ]
            items.append(
                RawItem(
                    source="officialfeeds",
                    external_id="writer",
                    title="Independent window",
                    url="https://example.com/window",
                    summary="An independent read of the window.",
                    published_at="2026-08-14T00:30:00Z",
                    collected_at="2026-08-14T13:00:00Z",
                    metrics={},
                    extra={"kind": "news", "official": False},
                )
            )
            store.append_raw(items, DAY)
            rows = news_for_day(store, DAY)
            self.assertLessEqual(len(rows), 18)
            self.assertTrue(any(row["title"] == "Independent window" for row in rows))
            self.assertTrue(all(row["first_party"] for row in rows if row["title"].startswith("Lab update")))

    def test_updates_require_every_candidate_once(self) -> None:
        source = product()
        payload = {
            "products": [
                {
                    "slug": "example",
                    "decision": "watching",
                    "category": "AI + 开发",
                    "project_type": "new_application",
                    "industries": ["软件研发"],
                    "industries_en": ["Software development"],
                    "jobs": ["需求梳理"],
                    "jobs_en": ["Requirements triage"],
                    "regions": ["英文生态"],
                    "regions_en": ["English ecosystem"],
                    "open_source": False,
                    "summary_zh": "把需求整理成可执行的开发任务",
                    "inspiration": "把模糊需求先变成可审阅的中间产物，能降低协作返工",
                    "summary_en": "Turns rough requirements into executable engineering tasks.",
                    "inspiration_en": "A reviewable intermediate artifact reduces rework in collaboration.",
                }
            ]
        }
        updated = _updates(payload, [source])["example"]
        self.assertEqual(updated.status, "watching")
        self.assertEqual(updated.category, "AI + 开发")
        self.assertEqual(updated.industries, ("软件研发",))
        self.assertTrue(updated.inspiration_en)

    def test_market_context_keeps_a_public_bilingual_record_and_stable_entity_name(self) -> None:
        source = product()
        updated = _updates(
            {"products": [{
                "slug": "example",
                "name": "Example AI",
                "decision": "market_context",
                "summary_zh": "这项变化改变了企业采用 AI 的成本与交付方式。",
                "summary_en": "This change alters the cost and delivery model of enterprise AI adoption.",
            }]},
            [source],
        )["example"]
        self.assertEqual(updated.status, STATUS_MARKET_CONTEXT)
        self.assertEqual(updated.name, "Example AI")
        self.assertIn("企业采用", updated.summary_zh)
        self.assertIn("enterprise AI", updated.summary_en)

    def test_market_context_without_public_copy_is_rejected(self) -> None:
        with self.assertRaises(BriefError):
            _updates(
                {"products": [{"slug": "example", "decision": "market_context"}]},
                [product()],
            )

    def test_req_initial_review_requires_all_gates_and_uses_known_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            source = product()
            store.append_evidence(
                Evidence(
                    id="ev-1",
                    project_slug="example",
                    url="https://example.com",
                    title="Product page",
                    published_at=source.last_seen,
                    collected_at=source.last_seen,
                    source_kind="product",
                    tier="first_party",
                )
            )
            result = {
                "products": [
                    {
                        "slug": "example",
                        "decision": "watching",
                        "req_initial": {
                            "verdict": "needs_validation",
                            "signal_level": "待验证",
                            "gates": [
                                {"gate": "value", "status": "supported", "reason": "公开材料称能处理运单异常", "evidence_ids": ["ev-1"]},
                                {"gate": "consensus", "status": "insufficient", "reason": "公开材料尚未证明货代会持续采用或替换现有人工流程。", "evidence_ids": []},
                                {"gate": "model", "status": "insufficient", "reason": "尚未披露具体付费者、价格或能够支持单位经济的收费证据。", "evidence_ids": []},
                                {"gate": "truth", "status": "insufficient", "reason": "异常判断准确率、责任边界和人工复核机制仍缺少可核验信息。", "evidence_ids": []},
                            ],
                            "next_validation": "确认至少一家货代是否愿意为减少异常处理时间付费。",
                        },
                    }
                ]
            }

            review = _req_reviews(result, [source], store, day=DAY)["example"]
            self.assertEqual(review.verdict, "true_demand")
            self.assertEqual(review.signal_level, "初步成立")
            self.assertEqual(review.gates[0].evidence_ids, ("ev-1",))
            self.assertEqual(review.id, "req-initial-example-2026-08-14")

    def test_req_initial_review_keeps_a_nonempty_reason_outside_the_target_length(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            source = product()
            long_reason = "公开材料仅说明了产品能力，尚无用户持续使用或付费的证据。" * 30
            result = {
                "products": [{
                    "slug": "example", "decision": "watching",
                    "req_initial": {
                        "verdict": "needs_validation", "signal_level": "待验证",
                        "gates": [
                            {"gate": gate, "status": "insufficient", "reason": long_reason, "evidence_ids": []}
                            for gate in ("value", "consensus", "model", "truth")
                        ],
                        "next_validation": "核验是否有目标用户持续使用该产品。",
                    },
                }],
            }

            review = _req_reviews(result, [source], store, day=DAY)["example"]

            self.assertEqual(len(review.gates[0].reason), 320)

    def test_req_initial_review_rejects_hallucinated_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            source = product()
            result = {
                "products": [
                    {
                        "slug": "example",
                        "decision": "watching",
                        "req_initial": {
                            "verdict": "needs_validation",
                            "signal_level": "待验证",
                            "gates": [
                                {"gate": "value", "status": "supported", "reason": "货代每天都需要处理会影响交付和客户关系的运输异常。", "evidence_ids": ["made-up"]},
                                {"gate": "consensus", "status": "insufficient", "reason": "公开材料尚未证明货代会持续采用或替换现有人工流程。", "evidence_ids": []},
                                {"gate": "model", "status": "insufficient", "reason": "尚未披露具体付费者、价格或能够支持单位经济的收费证据。", "evidence_ids": []},
                                {"gate": "truth", "status": "insufficient", "reason": "异常判断准确率、责任边界和人工复核机制仍缺少可核验信息。", "evidence_ids": []},
                            ],
                            "next_validation": "确认至少一家货代是否愿意为减少异常处理时间付费。",
                        },
                    }
                ]
            }
            with self.assertRaises(BriefError):
                _req_reviews(result, [source], store, day=DAY)

    def test_priority_candidate_cannot_be_silently_rejected(self) -> None:
        source = replace(product(), priority_review=True)
        with self.assertRaises(BriefError):
            _updates(
                {"products": [{"slug": "example", "decision": "rejected"}]},
                [source],
            )

    def test_priority_candidate_cannot_be_demoted_to_market_context(self) -> None:
        source = replace(product(), priority_review=True)
        with self.assertRaises(BriefError):
            _updates(
                {"products": [{"slug": "example", "decision": "market_context"}]},
                [source],
            )

    def test_product_update_rejects_untranslated_cjk_in_english_copy(self) -> None:
        row = {
            "slug": "example",
            "decision": "queued",
            "category": "AI + 开发",
            "project_type": "product",
            "summary_zh": "把需求整理成可执行的开发任务",
            "inspiration": "先形成可审阅的中间产物，再进入交付。",
            "summary_en": "Turns requirements、into build-ready development tasks.",
            "inspiration_en": "Create a reviewable intermediate artifact before delivery.",
            "industries": ["软件研发"], "industries_en": ["Software development"],
            "jobs": ["需求梳理"], "jobs_en": ["Requirements analysis"],
            "regions": ["英文生态"], "regions_en": ["English-speaking markets"],
            "open_source": True,
        }
        with self.assertRaises(BriefError):
            _updates({"products": [row]}, [product()])

    def test_priority_candidate_must_appear_in_both_reports(self) -> None:
        source = replace(product("deepseek-harness"), name="DeepSeek Harness", priority_review=True)
        with self.assertRaises(BriefError):
            _require_priority_coverage([source], "## 今日观察\n\nDeepSeek Harness", "## Today")

    def test_report_frontmatter_is_created_by_code(self) -> None:
        result = {
            "report": {
                "hook_zh": "今天的工具都在把模糊需求变成可审阅的步骤",
                "highlights_zh": ["1 个值得继续看"],
                "body_zh": "## 今天值得看的 1 个\n\n### Example\n\n一句判断。",
                "hook_en": "Today's tools turn fuzzy requests into reviewable steps",
                "highlights_en": ["1 worth watching"],
                "body_en": "## One product worth watching\n\n### Example\n\nA concise call.",
            }
        }
        markdown = _report_markdown(result, DAY, english=False)
        self.assertTrue(markdown.startswith("---\nday: '2026-08-14'"))
        self.assertIn("# AI 应用雷达 · 2026-08-14", markdown)

    def test_report_rejects_body_without_section(self) -> None:
        result = {
            "report": {
                "hook_zh": "一条钩子",
                "highlights_zh": ["一条要点"],
                "body_zh": "没有二级标题",
            }
        }
        with self.assertRaises(BriefError):
            _report_markdown(result, DAY, english=False)

    def test_report_rejects_untranslated_cjk_in_english_copy(self) -> None:
        result = {
            "report": {
                "hook_en": "A new workflow、with a leaked punctuation mark",
                "highlights_en": ["One observation"],
                "body_en": "## One product worth watching\n\nA concise call.",
            }
        }
        with self.assertRaises(BriefError):
            _report_markdown(result, DAY, english=True)

    def test_public_copy_rejects_internal_source_names(self) -> None:
        updated = replace(
            product(),
            summary_zh="在 AICPB 的增速榜上表现突出",
            inspiration="用增长信号补强产品判断",
            summary_en="A product with an unusual growth signal.",
            inspiration_en="Growth signals can strengthen product judgment.",
        )
        with self.assertRaises(PublicSourceLeakError):
            _require_no_public_source_leaks(
                {updated.slug: updated},
                "## 今日观察\n\n没有泄漏。",
                "## Today's notes\n\nNo leak.",
            )

    def test_public_copy_allows_neutral_evidence_language(self) -> None:
        updated = replace(
            product(),
            summary_zh="在 AI 产品增长榜上出现异常增速",
            inspiration="用增长信号补强产品判断",
            summary_en="A product with an unusual growth signal.",
            inspiration_en="Growth signals can strengthen product judgment.",
        )
        _require_no_public_source_leaks(
            {updated.slug: updated},
            "## 今日观察\n\n增长数据值得继续观察。",
            "## Today's notes\n\nThe growth signal is worth watching.",
        )

    def test_source_name_fallback_preserves_daily_copy_without_leaking_channel(self) -> None:
        zh = _neutralize_public_source_names("项目在 GitHub 发布，随后被 TechCrunch 报道。", english=False)
        en = _neutralize_public_source_names("Released on GitHub and covered by TechCrunch.", english=True)

        self.assertEqual(zh, "项目在 公开代码仓库 发布，随后被 公开资料 报道。")
        self.assertEqual(en, "Released on public code repository and covered by public reporting.")
        self.assertEqual(_public_source_leaks([zh, en]), ())

    def test_structured_source_fallback_cleans_only_public_copy(self) -> None:
        result = {
            "products": [{
                "slug": "example",
                "name": "Example",
                "url": "https://github.com/example/repo",
                "summary_zh": "项目在 GitHub 发布",
                "summary_en": "The model is hosted on Hugging Face.",
                "req_initial": {
                    "next_validation": "核验 GitHub 之外的采用证据",
                    "gates": [{"reason": "目前只有 GitHub 数据"}],
                    "demand_read": {"job_en": "Teams discover it through TechCrunch."},
                },
            }]
        }

        cleaned = _neutralize_model_public_copy(result)

        self.assertIn("GitHub", result["products"][0]["summary_zh"])
        self.assertEqual(cleaned["products"][0]["url"], "https://github.com/example/repo")
        self.assertNotIn("GitHub", cleaned["products"][0]["summary_zh"])
        self.assertNotIn("Hugging Face", cleaned["products"][0]["summary_en"])
        self.assertNotIn(
            "TechCrunch",
            cleaned["products"][0]["req_initial"]["demand_read"]["job_en"],
        )

    def test_structured_text_fallback_unwraps_common_json_shape_drift(self) -> None:
        result = {
            "products": [{
                "slug": "apps",
                "summary_zh": {
                    "content": [{"type": "text", "text": "面向团队的应用交付方式发生变化。"}]
                },
                "summary_en": ["Application delivery", "is changing for teams."],
                "req_initial": {
                    "next_validation": {"value": "核验目标团队是否持续采用。"},
                    "gates": [{"reason": ["公开材料尚未证明", "持续付费。"]}],
                },
            }],
            "report": {
                "hook_zh": {"summary": "本期出现新的交付信号"},
                "highlights_en": [{"text": "One new delivery signal"}],
            },
        }

        cleaned = _normalize_model_public_text_types(result)

        row = cleaned["products"][0]
        self.assertEqual(row["summary_zh"], "面向团队的应用交付方式发生变化。")
        self.assertEqual(row["summary_en"], "Application delivery is changing for teams.")
        self.assertEqual(row["req_initial"]["next_validation"], "核验目标团队是否持续采用。")
        self.assertEqual(row["req_initial"]["gates"][0]["reason"], "公开材料尚未证明 持续付费。")
        self.assertEqual(cleaned["report"]["hook_zh"], "本期出现新的交付信号")
        self.assertEqual(cleaned["report"]["highlights_en"], ["One new delivery signal"])

    def test_terminal_public_copy_fallback_preserves_uncertainty(self) -> None:
        candidate = replace(
            product("qwen38-flash-next"),
            sightings=(
                Sighting("producthunt", "https://example.com", "2026-08-13T23:10:00Z", {}),
                Sighting("marketfeeds", "https://news.example/qwen", "2026-08-13T23:10:00Z", {}, kind="news"),
            ),
        )
        result = {
            "products": [{
                "slug": candidate.slug,
                "decision": "watching",
                "summary_zh": None,
                "summary_en": "A compact open-weight model preview.",
                "inspiration": [],
                "inspiration_en": "Validate production use before investing.",
            }]
        }

        recovered = _recover_missing_public_text(result, [candidate])["products"][0]

        self.assertIn("尚不足以确认", recovered["summary_zh"])
        self.assertEqual(recovered["summary_en"], "A compact open-weight model preview.")
        self.assertIn("真实工作流", recovered["inspiration"])
        self.assertIn("进一步核验", recovered["event_summary_zh"])
        self.assertIn("requires validation", recovered["event_summary_en"])

    def test_failed_run_resumes_from_the_first_unfinished_batch(self) -> None:
        def market_context(slug: str) -> dict:
            return {
                "products": [{
                    "slug": slug,
                    "name": slug.title(),
                    "decision": "market_context",
                    "summary_zh": f"{slug} 改变了企业采购与交付方式。",
                    "summary_en": f"{slug.title()} changes enterprise buying and delivery patterns.",
                }]
            }

        report = {
            "report": {
                "hook_zh": "企业采购正在转向可持续交付",
                "highlights_zh": ["两个市场变化已完成判断"],
                "body_zh": "## 本期判断\n\n采购与交付方式正在变化。",
                "hook_en": "Enterprise buying is shifting toward durable delivery",
                "highlights_en": ["Two market shifts completed assessment"],
                "body_en": "## Edition call\n\nBuying and delivery patterns are changing.",
            }
        }
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            store.config_dir.mkdir(parents=True, exist_ok=True)
            (store.config_dir / "filter.md").write_text("筛选规则", encoding="utf-8")
            (store.config_dir / "template.md").write_text("编辑模板", encoding="utf-8")
            (store.config_dir / "req.md").write_text("REQ 公开证据模式", encoding="utf-8")
            store.save_product(product("alpha"))
            store.save_product(product("beta"))

            with patch("xocto.brief.BRIEF_BATCH_SIZE", 1), patch(
                "xocto.brief._request",
                side_effect=[market_context("alpha"), BriefError("second batch failed")],
            ):
                with self.assertRaises(BriefError):
                    run(store, day=DAY)

            progress = store.read_brief_progress(DAY)
            self.assertEqual(set(progress["full"]), {"alpha"})
            self.assertEqual(store.load_product("alpha").status, STATUS_PENDING_FILTER)

            with patch("xocto.brief.BRIEF_BATCH_SIZE", 1), patch(
                "xocto.brief._request",
                side_effect=[market_context("beta"), report],
            ) as request:
                result = run(store, day=DAY)

            self.assertEqual(request.call_count, 2)
            self.assertEqual(result.updated, 2)
            self.assertEqual(store.load_product("alpha").status, STATUS_MARKET_CONTEXT)
            self.assertEqual(store.load_product("beta").status, STATUS_MARKET_CONTEXT)
            self.assertFalse(store.brief_progress_path(DAY).exists())


    def test_failed_batch_is_isolated_unless_it_holds_a_priority_candidate(self) -> None:
        def broken(slug: str) -> dict:
            # watching 但缺 category、标签和 req_initial：确定性兜底补不齐，
            # 校验屡修不过，正好命中隔离路径。
            return {"products": [{"slug": slug, "name": slug.title(), "decision": "watching"}]}

        valid_beta = {
            "products": [{
                "slug": "beta",
                "name": "Beta",
                "decision": "market_context",
                "summary_zh": "贝塔改变了企业采购与交付方式。",
                "summary_en": "Beta changes enterprise buying and delivery patterns.",
            }]
        }
        report = {
            "report": {
                "hook_zh": "企业采购正在转向可持续交付",
                "highlights_zh": ["一个市场变化已完成判断"],
                "body_zh": "## 本期判断\n\nAlpha 与采购交付方式正在变化。",
                "hook_en": "Enterprise buying is shifting toward durable delivery",
                "highlights_en": ["One market shift completed assessment"],
                "body_en": "## Edition call\n\nAlpha and buying patterns are changing.",
            }
        }

        def fake_request(messages: list[dict[str, str]]) -> dict:
            if "<candidates_json>" not in messages[1]["content"]:
                return report
            if "alpha" in messages[1]["content"]:
                return broken("alpha")
            return valid_beta

        def prepare(tmp: str) -> Store:
            store = Store(Path(tmp))
            store.ensure_dirs()
            store.config_dir.mkdir(parents=True, exist_ok=True)
            (store.config_dir / "filter.md").write_text("筛选规则", encoding="utf-8")
            (store.config_dir / "template.md").write_text("编辑模板", encoding="utf-8")
            (store.config_dir / "req.md").write_text("REQ 公开证据模式", encoding="utf-8")
            store.save_product(product("alpha"))
            store.save_product(product("beta"))
            return store

        # 普通候选的坏批次只隔离该批：beta 照常完成，日报照常发布。
        with tempfile.TemporaryDirectory() as tmp:
            store = prepare(tmp)
            with patch("xocto.brief.BRIEF_BATCH_SIZE", 1), patch(
                "xocto.brief._request", side_effect=fake_request
            ):
                result = run(store, day=DAY)

            self.assertEqual(result.updated, 1)
            self.assertEqual(store.load_product("alpha").status, STATUS_PENDING_FILTER)
            self.assertEqual(store.load_product("beta").status, STATUS_MARKET_CONTEXT)
            self.assertTrue(store.report_path(DAY).exists())

        # 重大项目屡被降级时由兜底接管：留在机会流里（watching + 基础初判），
        # 日报必须点名它，而不是让全天判断失败。
        with tempfile.TemporaryDirectory() as tmp:
            store = prepare(tmp)
            store.save_product(replace(store.load_product("alpha"), priority_review=True))
            with patch("xocto.brief.BRIEF_BATCH_SIZE", 1), patch(
                "xocto.brief._request", side_effect=fake_request
            ):
                run(store, day=DAY)

            rescued = store.load_product("alpha")
            self.assertEqual(rescued.status, STATUS_WATCHING)
            self.assertTrue(rescued.category)
            reviews = store.read_req_reviews("alpha")
            self.assertTrue(reviews)
            self.assertTrue(store.report_path(DAY).exists())


if __name__ == "__main__":
    unittest.main()
