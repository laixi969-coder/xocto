from __future__ import annotations

from dataclasses import replace
from datetime import date
from pathlib import Path
import tempfile
import unittest

from xocto.models import (
    DiscoveryEvent,
    Evidence,
    Product,
    REQ_NEEDS_VALIDATION,
    REQ_PSEUDO_DEMAND,
    REQ_SIGNAL_DOUBT,
    REQ_SIGNAL_INITIAL,
    REQ_TRUE_DEMAND,
    ReqGateReview,
    ReqReview,
    Sighting,
    public_req_labels,
    req_conclusion,
)
from xocto.req_review import (
    _decision_change_summary,
    _decision_signature,
    _is_proven,
    _is_substantive_full_review,
    _messages,
    _reviews,
    candidates,
    seed_initial_reviews,
)
from xocto.store import Store


DAY = date(2026, 8, 23)


def product() -> Product:
    return Product(
        slug="freight-ai", name="Freight AI", url="https://example.com", canonical_url="https://example.com",
        summary="Helps freight teams resolve shipment exceptions.", first_seen="2026-08-23T10:00:00Z",
        last_seen="2026-08-23T10:00:00Z", status="watching", sightings=(Sighting("github", "https://example.com", "2026-08-23T10:00:00Z", {}),),
        priority_review=True,
    )


def result() -> dict:
    reasons = {
        "value": "货运异常处理的对象、旧流程与交付结果已有公开说明，目标问题可以被清晰定位。",
        "consensus": "现有材料尚未给出持续部署、复购或独立用户评价，采用共识仍待公开证据确认。",
        "model": "共识闸门未通过，付费主体、定价和单位经济暂不进入判断。",
        "truth": "共识闸门未通过，可复现结果和人工边界暂不进入判断。",
    }
    return {"reviews": [{"slug": "freight-ai", "verdict": "needs_validation", "signal_level": "待验证", "gates": [
        {"gate": gate, "status": "supported" if gate == "value" else "insufficient", "reason": reasons[gate], "evidence_ids": ["ev-1"]}
        for gate in ("value", "consensus", "model", "truth")
    ], "next_validation": "追踪官网客户案例与公开部署文档，确认货代是否持续采用并为降低异常处理时长付费。"}]}


class FullReqReviewTests(unittest.TestCase):
    def test_full_review_prompt_uses_req_public_evidence_protocol(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.config_dir.mkdir(parents=True, exist_ok=True)
            (store.config_dir / "req.md").write_text("# REQ 公开证据模式\n\n不得要求读者访谈。", encoding="utf-8")
            prompt = _messages([product()], store)
            self.assertIn("REQ 公开证据模式", prompt[0]["content"])
            self.assertIn("不得要求读者访谈", prompt[0]["content"])

    def test_seeded_initial_review_exists_without_a_model_call_and_is_replaced_by_the_editor(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.save_product(item)
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            store.append_event(DiscoveryEvent(
                id="first-freight", project_slug=item.slug, event_type="first_discovered",
                occurred_at=item.last_seen, discovered_at=item.last_seen, evidence_ids=("ev-1",),
            ))

            report = seed_initial_reviews(store, day=DAY)
            seeded = store.read_req_reviews(item.slug)[0]

            self.assertEqual((report.candidates, report.reviews), (1, 1))
            self.assertEqual(seeded.verdict, REQ_NEEDS_VALIDATION)
            self.assertEqual(seeded.signal_level, REQ_SIGNAL_DOUBT)
            self.assertIn("产品说明不能代替用户证据", seeded.gates[0].reason)
            self.assertEqual(seeded.gates[0].status, "insufficient")
            self.assertEqual(seeded.gates[2].status, "insufficient")
            self.assertTrue(seeded.job)
            self.assertTrue(seeded.pain)
            self.assertTrue(seeded.current_alternative)
            self.assertTrue(seeded.usage_reason)
            self.assertIn("公开补证", seeded.next_validation)
            self.assertNotIn("访谈", seeded.next_validation)
            revised = ReqReview(
                id=seeded.id, project_slug=item.slug, level="initial", reviewed_at=item.last_seen,
                verdict="needs_validation", signal_level="初步成立",
                gates=seeded.gates, next_validation="验证付费意愿。",
            )
            self.assertTrue(store.upsert_req_review(revised))
            self.assertEqual(store.read_req_reviews(item.slug), [revised])

    def test_seeded_review_without_a_job_description_stays_unfounded(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = replace(product(), summary="", summary_zh="")
            store.save_product(item)
            store.append_event(DiscoveryEvent(
                id="first-freight", project_slug=item.slug, event_type="first_discovered",
                occurred_at=item.last_seen, discovered_at=item.last_seen,
            ))
            seed_initial_reviews(store, day=DAY)
            seeded = store.read_req_reviews(item.slug)[0]
            self.assertEqual(seeded.verdict, REQ_NEEDS_VALIDATION)
            self.assertIn("具体用户任务", seeded.gates[0].reason)

    def test_priority_project_with_initial_review_enters_full_req_queue(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.save_product(item)
            store.append_req_review(ReqReview(
                id="initial", project_slug=item.slug, level="initial", reviewed_at=item.last_seen,
                verdict="needs_validation", signal_level="待验证",
                gates=tuple(ReqGateReview(gate, "insufficient", "公开信息仍不足以确认该闸门。") for gate in ("value", "consensus", "model", "truth")),
            ))
            self.assertEqual(candidates(store, DAY), [item])

    def test_full_review_requires_known_evidence_and_all_gates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            reviews = _reviews(result(), [item], store, DAY)
            self.assertEqual(reviews[0].level, "full")
            self.assertEqual(reviews[0].id, "req-full-freight-ai-2026-08-23")
            bad = result()
            bad["reviews"][0]["gates"][0]["evidence_ids"] = ["invented"]
            normalized = _reviews(bad, [item], store, DAY)[0]
            self.assertEqual(normalized.gates[0].status, "insufficient")
            self.assertEqual(normalized.gates[0].evidence_ids, ())

    def test_full_review_conservatively_downgrades_generic_short_gate_reasons(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            shallow = result()
            shallow["reviews"][0]["gates"][0]["reason"] = "信息不足。"
            review = _reviews(shallow, [item], store, DAY)[0]
            self.assertEqual(review.gates[0].status, "insufficient")
            self.assertIn("shipment exceptions", review.gates[0].reason)
            self.assertEqual(review.gates[1].reason, "价值闸门未通过，共识闸门未进入。")

    def test_full_review_replaces_long_but_generic_value_reason(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            generic = result()
            generic["reviews"][0]["gates"][0]["reason"] = "描述模糊，未明确具体应用场景和用户价值。"
            review = _reviews(generic, [item], store, DAY)[0]
            self.assertEqual(review.gates[0].status, "insufficient")
            self.assertNotIn("描述模糊", review.gates[0].reason)
            self.assertIn("shipment exceptions", review.gates[0].reason)

    def test_fallback_reason_stops_at_a_complete_sentence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = replace(product(), summary_zh=(
                "GamePhanes 是一个面向 Godot 游戏引擎的开源游戏编码代理环境与基准。"
                "游戏开发者可让代理编写、运行和测试游戏代码，并依据多项指标评估表现。"
            ))
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            generic = result()
            generic["reviews"][0]["gates"][0]["reason"] = "价值主张不明确，具体痛点与使用场景尚未得到证明。"
            reason = _reviews(generic, [item], store, DAY)[0].gates[0].reason
            self.assertIn("环境与基准。", reason)
            self.assertNotIn("并依”，", reason)

    def test_later_gates_are_blocked_only_when_value_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            blocked = result()
            blocked["reviews"][0]["gates"][0]["status"] = "insufficient"
            blocked["reviews"][0]["gates"][0]["reason"] = "公开材料尚未说明货运异常由谁处理、不处理会失去什么。"
            blocked["reviews"][0]["gates"][1]["status"] = "supported"
            review = _reviews(blocked, [item], store, DAY)[0]
            self.assertEqual(review.gates[1].status, "insufficient")
            self.assertEqual(review.verdict, REQ_NEEDS_VALIDATION)

    def test_value_pass_keeps_later_gate_judgments(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            payload = result()
            payload["reviews"][0]["gates"][2] = {
                "gate": "model",
                "status": "supported",
                "reason": "货代按异常处理次数付费的路径已在公开材料中写明，钱来自货代企业。",
                "evidence_ids": ["ev-1"],
            }
            review = _reviews(payload, [item], store, DAY)[0]
            self.assertEqual(review.gates[2].status, "supported")
            self.assertEqual(review.verdict, REQ_TRUE_DEMAND)
            self.assertEqual(review.signal_level, "需求信号明确")

    def test_value_supported_without_pricing_is_true_demand(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            review = _reviews(result(), [item], store, DAY)[0]
            self.assertEqual(review.verdict, REQ_TRUE_DEMAND)
            self.assertEqual(review.signal_level, REQ_SIGNAL_INITIAL)

    def test_challenged_value_is_pseudo_demand(self) -> None:
        gates = (
            ReqGateReview("value", "challenged", "看着挺好但没有也行，货代不处理异常也能过完今天。", ("ev-1",)),
            ReqGateReview("consensus", "insufficient", "价值闸门未通过，共识闸门未进入。"),
            ReqGateReview("model", "insufficient", "价值闸门未通过，模式闸门未进入。"),
            ReqGateReview("truth", "insufficient", "价值闸门未通过，求真闸门未进入。"),
        )
        self.assertEqual(req_conclusion(gates), (REQ_PSEUDO_DEMAND, REQ_SIGNAL_DOUBT))
        self.assertEqual(public_req_labels("needs_validation", "待验证", gates), ("解决问题，但需求刚性不足", REQ_SIGNAL_DOUBT))

    def test_public_labels_never_say_pending_validation(self) -> None:
        gates = tuple(ReqGateReview(gate, "insufficient", "公开材料尚未说明买方和工作。") for gate in ("value", "consensus", "model", "truth"))
        verdict_label, signal = public_req_labels("needs_validation", "待验证", gates)
        self.assertEqual(verdict_label, "问题已识别，需求强度未明")
        self.assertNotEqual(signal, "待验证")
        self.assertNotIn("待验证", verdict_label)

    def test_normalized_numeric_value_counts_as_proven_even_when_raw_value_is_text(self) -> None:
        item = replace(product(), sightings=(Sighting(
            "ranking", "https://example.com", "2026-08-23T10:00:00Z",
            {"raw_value": "2.79M", "value": 2_790_000.0, "metric": "visits"},
        ),))
        self.assertTrue(_is_proven(item))

    def test_unattributed_parent_site_metric_does_not_make_feature_proven(self) -> None:
        item = replace(product(), sightings=(Sighting(
            "ranking", "https://example.com", "2026-08-23T10:00:00Z",
            {
                "raw_value": "2.79M",
                "value": 2_790_000.0,
                "metric": "visits",
                "product_attribution": False,
            },
        ),))
        self.assertFalse(_is_proven(item))

    def test_full_review_downgrades_unsupported_claim_without_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            unsupported = result()
            unsupported["reviews"][0]["gates"][0]["evidence_ids"] = []
            review = _reviews(unsupported, [item], store, DAY)[0]
            self.assertEqual(review.gates[0].status, "insufficient")
            self.assertEqual(review.verdict, "needs_validation")

    def test_full_review_replaces_duplicated_active_reason(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            duplicated = result()
            duplicated["reviews"][0]["gates"][1]["reason"] = duplicated["reviews"][0]["gates"][0]["reason"]
            review = _reviews(duplicated, [item], store, DAY)[0]
            self.assertNotEqual(review.gates[0].reason, review.gates[1].reason)
            self.assertIn("持续部署", review.gates[1].reason)

    def test_full_review_replaces_reader_delegation_with_public_evidence_step(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            delegated = result()
            delegated["reviews"][0]["next_validation"] = "访谈一位货代，询问是否愿意为此付费。"
            review = _reviews(delegated, [item], store, DAY)[0]
            self.assertNotIn("访谈", review.next_validation)
            self.assertIn("公开部署文档", review.next_validation)

    def test_internal_downstream_normalization_is_not_a_decision_change(self) -> None:
        reason = "现有公开材料能够支持当前闸门判断，并可回溯至项目证据。"
        previous = ReqReview(
            id="old", project_slug="freight-ai", level="full", reviewed_at="2026-08-23T01:00:00Z",
            verdict="needs_validation", signal_level="初步成立",
            gates=(
                ReqGateReview("value", "supported", reason, ("ev-1",)),
                ReqGateReview("consensus", "insufficient", reason),
                ReqGateReview("model", "insufficient", reason),
                ReqGateReview("truth", "supported", reason, ("ev-1",)),
            ),
        )
        normalized = replace(previous, id="new", gates=(
            previous.gates[0], previous.gates[1], previous.gates[2],
            ReqGateReview("truth", "insufficient", "共识闸门未通过，求真闸门未进入。"),
        ))
        self.assertEqual(_decision_signature(previous), _decision_signature(normalized))

        advanced = replace(normalized, gates=tuple(
            replace(gate, status="supported", evidence_ids=("ev-1",)) if gate.gate == "consensus" else gate
            for gate in normalized.gates
        ))
        self.assertNotEqual(_decision_signature(normalized), _decision_signature(advanced))
        summary = _decision_change_summary(normalized, advanced)
        self.assertIn("连续通过阶段由 1 道调整为 2 道", summary)
        self.assertIn("当前停在模式闸门", summary)
        self.assertNotIn("/req", summary)

    def test_low_quality_same_day_full_review_is_queued_for_repair(self) -> None:
        shallow_gates = tuple(
            ReqGateReview(gate, "insufficient", "公开信息不足。")
            for gate in ("value", "consensus", "model", "truth")
        )
        shallow = ReqReview(
            id="req-full-freight-ai-2026-08-23", project_slug="freight-ai", level="full",
            reviewed_at="2026-08-23T10:00:00Z", verdict="needs_validation", signal_level="待验证",
            gates=shallow_gates, next_validation="查看公开资料。",
        )
        self.assertFalse(_is_substantive_full_review(shallow))
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.save_product(item)
            store.append_req_review(replace(shallow, id="initial", level="initial"))
            store.append_req_review(shallow)
            self.assertEqual(candidates(store, DAY), [item])
