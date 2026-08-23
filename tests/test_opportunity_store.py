from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from xocto.models import (
    DEMAND_EARLY_SIGNAL,
    REQ_GATE_CONSENSUS,
    REQ_GATE_INSUFFICIENT,
    REQ_GATE_MODEL,
    REQ_GATE_SUPPORTED,
    REQ_GATE_TRUTH,
    REQ_GATE_VALUE,
    REQ_NEEDS_VALIDATION,
    SUPPLY_NOT_FOUND,
    Evidence,
    MarketObservation,
    ReqGateReview,
    ReqReview,
)
from xocto.store import Store


class OpportunityStoreTests(unittest.TestCase):
    def test_market_observation_and_req_review_are_persisted_per_project(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            evidence = Evidence(
                id="ev-1",
                project_slug="freight-ai",
                url="https://example.com/pricing",
                title="Pricing",
                published_at="2026-08-14T09:00:00Z",
                collected_at="2026-08-14T10:00:00Z",
                source_kind="pricing",
                tier="first_party",
            )
            self.assertTrue(store.append_evidence(evidence))
            self.assertFalse(store.append_evidence(evidence))

            observation = MarketObservation(
                project_slug="freight-ai",
                market="CN",
                ecosystem="zh",
                observed_at="2026-08-14T10:00:00Z",
                supply_status=SUPPLY_NOT_FOUND,
                demand_status=DEMAND_EARLY_SIGNAL,
                coverage="Chinese public product and developer ecosystems checked on 2026-08-14.",
                evidence_ids=("ev-1",),
            )
            self.assertTrue(store.append_market_observation(observation))
            self.assertEqual(store.read_market_observations("freight-ai"), [observation])

            review = ReqReview(
                id="req-1",
                project_slug="freight-ai",
                level="initial",
                reviewed_at="2026-08-14T10:00:00Z",
                verdict=REQ_NEEDS_VALIDATION,
                signal_level="待验证",
                gates=(
                    ReqGateReview(REQ_GATE_VALUE, REQ_GATE_SUPPORTED, "货运异常处理场景明确。", ("ev-1",)),
                    ReqGateReview(REQ_GATE_CONSENSUS, REQ_GATE_INSUFFICIENT, "尚无重复采用证据。"),
                    ReqGateReview(REQ_GATE_MODEL, REQ_GATE_INSUFFICIENT, "尚未披露付费路径。"),
                    ReqGateReview(REQ_GATE_TRUTH, REQ_GATE_INSUFFICIENT, "交付边界待验证。"),
                ),
                next_validation="确认货代是否为异常处理支付。",
                market="US",
            )
            self.assertTrue(store.append_req_review(review))
            self.assertFalse(store.append_req_review(review))
            self.assertEqual(store.read_req_reviews("freight-ai"), [review])


if __name__ == "__main__":
    unittest.main()
