"""中英文生态的日常市场核验。

发现源只能证明“某项目在哪个生态出现过”，无法证明另一边不存在同类供给。
本模块先对项目的行业与具体工作做独立公开检索，再把检索结果连同可点击证据
交给编辑模型判断。结论的边界始终是已覆盖的公开资料，不声称绝对不存在。
"""

from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date
from typing import Any
from urllib.parse import urlencode

from .brief import BriefError, _request
from .models import (
    DEMAND_EVIDENCE_STATUSES,
    SUPPLY_STATUSES,
    Evidence,
    MarketObservation,
    STATUS_QUEUED,
    STATUS_WATCHING,
    local_day,
    now_iso,
)
from .sources.base import Http
from .store import Store

SEARCH_URL = "https://www.bing.com/search"
MAX_HITS = 8
MARKET_BATCH_SIZE = 24
_QUERY_STOPWORDS = {
    "ai", "agent", "agents", "assistant", "assistants", "tool", "tools", "software", "platform",
    "development", "developer", "developers", "technical", "user", "users", "team", "teams",
    "helps", "help", "with", "that", "from", "into", "using", "public", "global",
}


@dataclass(frozen=True)
class MarketReport:
    day: date
    candidates: int
    observations: int
    skipped: bool = False


def _query(product: Any, ecosystem: str) -> str:
    industries = " ".join(product.industries[:2])
    jobs = " ".join(product.jobs[:2])
    if ecosystem == "zh":
        terms = " ".join(part for part in ("AI", industries, jobs) if part)
        return terms or f"AI {product.name}"
    # 英文摘要来自编辑层；若它尚未给出，则使用原始英文简介。查询不使用
    # 项目名称，以免只验证“同一个产品能否被搜到”而错过本地替代品。
    terms = (product.summary_en or product.summary).replace("\n", " ").strip()
    return f"AI {terms[:180]}" if terms else f"AI {product.name}"


def _rss_hits(xml: str) -> list[dict[str, str]]:
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        return []
    rows: list[dict[str, str]] = []
    for item in root.findall("./channel/item")[:MAX_HITS]:
        title = (item.findtext("title") or "").strip()
        url = (item.findtext("link") or "").strip()
        summary = (item.findtext("description") or "").strip()
        if title and url:
            rows.append({"title": title, "url": url, "summary": summary})
    return rows


def _search_url(query: str) -> str:
    return f"{SEARCH_URL}?{urlencode({'format': 'rss', 'q': query})}"


def _relevant_hit(hit: dict[str, str], query: str) -> bool:
    """搜索结果至少命中一个具体行业/工作词，通用 AI 首页不算市场证据。"""
    terms = {
        token.casefold()
        for token in re.findall(r"[\u3400-\u9fff]{2,}|[a-zA-Z0-9][a-zA-Z0-9-]{2,}", query)
        if token.casefold() not in _QUERY_STOPWORDS
    }
    if not terms:
        return False
    haystack = f"{hit.get('title', '')} {hit.get('summary', '')}".casefold()
    return any(term in haystack for term in terms)


def _scan_evidence(store: Store, product: Any, ecosystem: str, query: str, http: Http) -> list[Evidence]:
    """保存市场检索的查询入口和结果。即使结果为空也留查询证据。"""
    collected = now_iso()
    query_url = _search_url(query)
    prefix = f"market-{product.slug}-{ecosystem}-{local_day(collected)}"
    query_evidence = Evidence(
        id=f"ev-{hashlib.sha1((prefix + '-query').encode()).hexdigest()[:16]}",
        project_slug=product.slug,
        url=query_url,
        title="Public market coverage query",
        published_at="",
        collected_at=collected,
        source_kind="market_comparison",
        tier="independent",
        fact=f"Public-material coverage query for {ecosystem}: {query}",
    )
    evidence = [query_evidence]
    hits = [
        hit
        for hit in _rss_hits(http.get_text(SEARCH_URL, params={"format": "rss", "q": query}))
        if _relevant_hit(hit, query)
    ]
    for index, hit in enumerate(hits, 1):
        evidence.append(Evidence(
            id=f"ev-{hashlib.sha1((prefix + '-' + str(index) + hit['url']).encode()).hexdigest()[:16]}",
            project_slug=product.slug,
            url=hit["url"],
            title=hit["title"],
            published_at="",
            collected_at=collected,
            source_kind="market_comparison",
            tier="independent",
            fact=hit["summary"][:1000],
        ))
    for item in evidence:
        store.append_evidence(item)
    return evidence


def _market_candidates(store: Store, day: date) -> list[tuple[Any, str]]:
    """只核验当天经编辑保留、且另一生态还没有当日观察的项目。"""
    candidates: list[tuple[Any, str]] = []
    for product in store.iter_products():
        if product.status not in {STATUS_QUEUED, STATUS_WATCHING}:
            continue
        if local_day(product.last_seen) != day.isoformat():
            continue
        observed_today = {
            observation.ecosystem
            for observation in store.read_market_observations(product.slug)
            if local_day(observation.observed_at) == day.isoformat()
        }
        for ecosystem in ("zh", "en"):
            if ecosystem not in observed_today:
                candidates.append((product, ecosystem))
    return candidates


def _messages(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    payload = json.dumps(rows, ensure_ascii=False)
    system = """你是 xOcto 的跨市场研究编辑。只可依据输入的公开检索结果判断，不得联网、补造
竞争者、客户、价格或本地供给。每个待核验生态必须恰好输出一次 JSON 记录。

本地供给状态：
- emerging：证据直接指向该语言生态中面向同一行业和具体工作的独立产品、开源项目或实质服务；
- established：证据直接支持已有成熟供给；
- not_found_in_covered_sources：本次给出的覆盖结果没有可核验的本地供给。它只表示本次覆盖范围内未发现，绝不表示绝对不存在。

需求证据状态：unknown、early_signal、validated_signal。新闻、文章、目录或大模型主入口不等于本地供给。
evidence_ids 只能使用输入的 id；无结果时可只引用查询入口证据。不得写内部采集渠道名称。
输出仅为合法 JSON：
{"observations":[{"slug":"...","ecosystem":"zh|en","supply_status":"not_found_in_covered_sources|emerging|established","demand_status":"unknown|early_signal|validated_signal","evidence_ids":["ev-..."]}]}"""
    return [{"role": "system", "content": system}, {"role": "user", "content": f"<market_evidence>{payload}</market_evidence>"}]


def _validated_observations(
    result: dict[str, Any], expected: list[tuple[Any, str]], evidence_ids: dict[tuple[str, str], set[str]], day: date
) -> list[MarketObservation]:
    rows = result.get("observations")
    if not isinstance(rows, list) or len(rows) != len(expected):
        raise BriefError("跨市场判断没有逐一处理全部待核验生态")
    expected_keys = {(product.slug, ecosystem) for product, ecosystem in expected}
    out: list[MarketObservation] = []
    seen: set[tuple[str, str]] = set()
    for row in rows:
        if not isinstance(row, dict):
            raise BriefError("跨市场判断记录格式不正确")
        slug = str(row.get("slug") or "").strip()
        ecosystem = str(row.get("ecosystem") or "").strip()
        key = (slug, ecosystem)
        if key not in expected_keys or key in seen:
            raise BriefError("跨市场判断返回了未知或重复记录")
        seen.add(key)
        supply = str(row.get("supply_status") or "")
        demand = str(row.get("demand_status") or "")
        if supply not in SUPPLY_STATUSES or demand not in DEMAND_EVIDENCE_STATUSES:
            raise BriefError("跨市场判断的供给或需求状态不合法")
        ids = row.get("evidence_ids") or []
        if not isinstance(ids, list) or not all(isinstance(value, str) for value in ids):
            raise BriefError("跨市场判断的证据引用格式不合法")
        unknown = set(ids) - evidence_ids[key]
        if unknown:
            raise BriefError(f"跨市场判断引用了不存在的证据：{', '.join(sorted(unknown))}")
        if not ids:
            raise BriefError("跨市场判断必须保留至少一条可核验证据")
        market = "CN" if ecosystem == "zh" else "English-language market"
        scope = "中文生态相关行业与具体工作的公开资料覆盖" if ecosystem == "zh" else "英文生态相关行业与具体工作的公开资料覆盖"
        out.append(MarketObservation(
            project_slug=slug,
            market=market,
            ecosystem=ecosystem,
            observed_at=f"{day.isoformat()}T12:00:00Z",
            supply_status=supply,
            demand_status=demand,
            coverage=f"{scope}；检索日期 {day.isoformat()}。未发现仅限该覆盖范围。",
            evidence_ids=tuple(ids),
        ))
    if seen != expected_keys:
        raise BriefError("跨市场判断遗漏待核验生态")
    return out


def run(store: Store, *, day: date, http: Http | None = None) -> MarketReport:
    expected = _market_candidates(store, day)
    if not expected:
        return MarketReport(day, candidates=0, observations=0, skipped=True)
    http = http or Http()
    prompt_rows: list[dict[str, Any]] = []
    allowed: dict[tuple[str, str], set[str]] = {}
    for product, ecosystem in expected:
        query = _query(product, ecosystem)
        evidence = _scan_evidence(store, product, ecosystem, query, http)
        key = (product.slug, ecosystem)
        allowed[key] = {item.id for item in evidence}
        prompt_rows.append({
            "slug": product.slug,
            "ecosystem": ecosystem,
            "industry": list(product.industries),
            "jobs": list(product.jobs),
            "query_scope": query,
            "evidence": [item.to_dict() for item in evidence],
        })
    # 市场对照同样可能在候选丰富的日子超过 JSON 输出上限。检索证据仍一次
    # 完整保存，编辑判断则分批逐条返回，避免漏掉后半段项目。
    observations: list[MarketObservation] = []
    for start in range(0, len(expected), MARKET_BATCH_SIZE):
        batch_expected = expected[start:start + MARKET_BATCH_SIZE]
        batch_rows = prompt_rows[start:start + MARKET_BATCH_SIZE]
        batch_allowed = {
            (product.slug, ecosystem): allowed[(product.slug, ecosystem)]
            for product, ecosystem in batch_expected
        }
        result = _request(_messages(batch_rows))
        observations.extend(_validated_observations(result, batch_expected, batch_allowed, day))
    for observation in observations:
        store.append_market_observation(observation)
    return MarketReport(day, candidates=len({product.slug for product, _ in expected}), observations=len(observations))
