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
    _decode_json_object,
    _model_providers,
    _prompt,
    _report_prompt,
    _report_markdown,
    _require_no_public_source_leaks,
    _require_priority_coverage,
    _req_reviews,
    _updates,
    _validation_repair_messages,
    candidates_for_day,
    news_for_day,
)
from xocto.models import Evidence, Product, RawItem, STATUS_MARKET_CONTEXT, STATUS_PENDING_FILTER, Sighting
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

    def test_settled_general_assistant_is_kept_as_market_context_not_an_opportunity(self) -> None:
        source = product()
        updated = _updates(
            {"products": [{"slug": "example", "decision": "market_context"}]},
            [source],
        )["example"]
        self.assertEqual(updated.status, STATUS_MARKET_CONTEXT)
        self.assertFalse(updated.summary_zh)

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
            self.assertEqual(review.verdict, "needs_validation")
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


if __name__ == "__main__":
    unittest.main()
