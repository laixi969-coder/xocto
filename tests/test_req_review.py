from __future__ import annotations

from dataclasses import replace
from datetime import date
from pathlib import Path
import tempfile
import unittest

from xocto.models import DiscoveryEvent, Evidence, Product, ReqGateReview, ReqReview, Sighting
from xocto.req_review import _is_substantive_full_review, _messages, _reviews, candidates, seed_initial_reviews
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
    reason = "货运异常处理的对象、旧流程与交付结果已有公开说明，但仍需核验不同规模货代是否愿意把该环节持续交给产品处理。"
    return {"reviews": [{"slug": "freight-ai", "verdict": "needs_validation", "signal_level": "待验证", "gates": [
        {"gate": gate, "status": "supported" if gate == "value" else "insufficient", "reason": reason, "evidence_ids": ["ev-1"]}
        for gate in ("value", "consensus", "model", "truth")
    ], "next_validation": "确认至少两家货代是否愿意为降低异常处理时长持续付费。"}]}


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
            self.assertEqual(seeded.signal_level, "待验证")
            self.assertIn("价值闸门", seeded.gates[0].reason)
            self.assertIn("公开补证", seeded.next_validation)
            self.assertNotIn("访谈", seeded.next_validation)
            revised = ReqReview(
                id=seeded.id, project_slug=item.slug, level="initial", reviewed_at=item.last_seen,
                verdict="needs_validation", signal_level="初步成立",
                gates=seeded.gates, next_validation="验证付费意愿。",
            )
            self.assertTrue(store.upsert_req_review(revised))
            self.assertEqual(store.read_req_reviews(item.slug), [revised])

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
            with self.assertRaises(Exception):
                _reviews(bad, [item], store, DAY)

    def test_full_review_rejects_generic_short_gate_reasons(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            shallow = result()
            shallow["reviews"][0]["gates"][0]["reason"] = "信息不足。"
            with self.assertRaises(Exception):
                _reviews(shallow, [item], store, DAY)

    def test_full_review_allows_concise_unentered_gates_after_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            item = product()
            store.append_evidence(Evidence("ev-1", item.slug, "https://example.com", "Product", item.last_seen, item.last_seen, "product", "first_party"))
            blocked = result()
            gates = blocked["reviews"][0]["gates"]
            gates[2]["reason"] = "共识闸门未通过，商业模型暂不进入。"
            gates[3]["reason"] = "共识闸门未通过，真需求暂不进入。"
            self.assertEqual(_reviews(blocked, [item], store, DAY)[0].level, "full")

            gates[2]["status"] = "supported"
            with self.assertRaises(Exception):
                _reviews(blocked, [item], store, DAY)

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
