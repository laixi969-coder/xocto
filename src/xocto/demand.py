"""Project a user-centred Demand Read from reviews, products, and evidence.

The review pipeline stores claims and citations.  This module owns the public
interpretation seam: a demand claim and a business opportunity are related, but
they are not the same assertion.  Missing commercial evidence must therefore not
erase the job, pain, existing alternative, or reason people try the product.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

from xocto.models import is_product_attributed_metric


@dataclass(frozen=True, slots=True)
class DemandRead:
    job: str
    pain: str
    current_alternative: str
    usage_reason: str
    demand_maturity: str
    business_maturity: str
    judgment_basis: str
    recommended_action: str


def _clean(value: Any) -> str:
    return " ".join(str(value or "").split())


def _metric_reason(product: Any, *, english: bool) -> str:
    """Explain attention/adoption without pretending that traffic proves retention."""
    for sighting in reversed(product.sightings or ()):
        metrics = sighting.metrics or {}
        if not is_product_attributed_metric(metrics):
            continue
        raw = metrics.get("raw_value")
        value = metrics.get("value")
        amount = raw if raw not in (None, "") else value
        metric = _clean(metrics.get("metric"))
        growth = metrics.get("mom_percent")
        if amount not in (None, "", 0, 0.0):
            if english:
                label = "monthly visits" if metric == "visits" else (metric or "public activity")
                growth_text = f" and {growth:g}% month-over-month growth" if isinstance(growth, (int, float)) else ""
                return (
                    f"A public record shows {amount} {label}{growth_text}. That explains the attention, "
                    "but product-level retention and payment are not yet verified."
                )
            label = "月访问" if metric == "visits" else (metric or "公开使用指标")
            growth_text = f"、环比 {growth:g}%" if isinstance(growth, (int, float)) else ""
            return f"公开记录显示{label} {amount}{growth_text}；这解释了它为何受到关注，但产品级留存与付费仍未核验。"
        stars = metrics.get("stars")
        forks = metrics.get("forks")
        if isinstance(stars, (int, float)) and stars > 0:
            if english:
                fork_text = f" and {int(forks):,} forks" if isinstance(forks, (int, float)) and forks > 0 else ""
                return f"Its public repository has {int(stars):,} stars{fork_text}, showing developer attention; repeat use and payment are not yet verified."
            fork_text = f"、{int(forks):,} 次复刻" if isinstance(forks, (int, float)) and forks > 0 else ""
            return f"公开代码仓库有 {int(stars):,} 个收藏{fork_text}，说明开发者正在关注或试用；持续使用与付费仍未核验。"
    return ""


def _business_maturity(product: Any, review: Any | None, evidence: Iterable[Any]) -> str:
    evidence = tuple(evidence)
    cited_ids = {
        evidence_id
        for gate in (review.gates if review else ())
        for evidence_id in gate.evidence_ids
    }
    cited_kinds = {str(item.source_kind) for item in evidence if item.id in cited_ids}
    if cited_kinds & {"retention", "repeat_purchase"}:
        return "retained"
    if cited_kinds & {"payment", "procurement", "revenue"}:
        return "paid"
    if cited_kinds & {"adoption", "open_source", "customer_case"} or _metric_reason(product, english=False):
        return "adoption"
    if any(item.source_kind == "pricing" and item.tier == "first_party" for item in evidence):
        return "pricing"
    return "unverified"


def demand_read(product: Any, review: Any | None, evidence: Iterable[Any], *, english: bool = False) -> DemandRead:
    """Return a complete Demand Read, including honest fallbacks for legacy data."""
    evidence = tuple(evidence)
    suffix = "_en" if english else ""

    jobs = product.jobs_en if english else product.jobs
    summary = _clean((product.summary_en or product.summary) if english else (product.summary_zh or product.summary))
    job = _clean(getattr(review, f"job{suffix}", "")) if review else ""
    if not job:
        job = "、".join(jobs) if jobs and not english else (", ".join(jobs) if jobs else summary)
    if not job:
        job = "The concrete user job is not yet described in public materials." if english else "公开材料尚未说清用户要完成的具体任务。"

    pain = _clean(getattr(review, f"pain{suffix}", "")) if review else ""
    if not pain:
        pain = (
            "The product targets friction in this job, but public user evidence does not yet show the cost, frequency, or consequence of leaving it unsolved."
            if english else
            "它试图减少完成这项任务时的摩擦；公开用户材料尚未说明不解决的具体代价、发生频率或后果。"
        )

    alternative = _clean(getattr(review, f"current_alternative{suffix}", "")) if review else ""
    if not alternative:
        alternative = (
            "Public materials do not yet show how users complete this job today or what they replace."
            if english else
            "公开材料尚未说明用户目前如何完成这项工作、它实际替代了什么。"
        )

    usage_reason = _clean(getattr(review, f"usage_reason{suffix}", "")) if review else ""
    if not usage_reason:
        usage_reason = _metric_reason(product, english=english)
    if not usage_reason:
        usage_reason = (
            f"It promises a simpler way to complete this job: {job} The exact adoption motive and repeat use are not yet verified."
            if english else
            f"它承诺用更直接的方式完成这项任务：{job}；具体采用动机与持续使用情况尚未核验。"
        )

    value_gate = next((gate for gate in (review.gates if review else ()) if gate.gate == "value"), None)
    if value_gate is not None and value_gate.status == "supported":
        demand_maturity = "evidenced"
    elif value_gate is not None and value_gate.status == "challenged":
        demand_maturity = "challenged"
    elif summary or jobs:
        demand_maturity = "job_only"
    else:
        demand_maturity = "unclear"

    business_maturity = _business_maturity(product, review, evidence)
    if business_maturity in {"paid", "retained"}:
        judgment_basis = "commercial"
    elif business_maturity == "adoption":
        judgment_basis = "behavioral"
    elif summary or jobs or review:
        judgment_basis = "reasoned"
    else:
        judgment_basis = "facts_only"

    if demand_maturity == "evidenced" and business_maturity in {"paid", "retained"}:
        recommended_action = "investigate"
    elif demand_maturity == "evidenced":
        recommended_action = "try"
    elif business_maturity == "adoption":
        recommended_action = "dissect"
    elif demand_maturity == "job_only":
        recommended_action = "watch"
    else:
        recommended_action = "clue"

    return DemandRead(
        job=job,
        pain=pain,
        current_alternative=alternative,
        usage_reason=usage_reason,
        demand_maturity=demand_maturity,
        business_maturity=business_maturity,
        judgment_basis=judgment_basis,
        recommended_action=recommended_action,
    )
