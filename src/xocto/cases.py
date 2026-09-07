"""真实生意案例管线 —— 采集、存储、富化。

对应 CASE_PIPELINE_SPEC.md。与产品池管线（collect.py）平行、互不污染：
案例不进产品池，写入 data/casestudies/<slug>.md，由 site 渲染成详情页。

三步各自幂等，可单独跑：

    uv run xocto cases               # 采集 + 富化（每日 Actions 用）
    uv run xocto cases --collect-only
    uv run xocto cases --enrich-only

数据源见规格第 2 节（2026-09-06 实测）：
- Starter Story /stories/*：创始人书面采访，服务端渲染，sitemap 全量 3273 篇。
  证据等级 interviewed。/businesses/* 正文是前端 JSON 块，暂不采。
- TrustMRR：首页 JSON-LD 直接给出 Stripe 验证收入。证据等级 stripe_verified。

版权红线（规格 2.1）：只取事实与短引，档案必须回链原页，禁止整段转载。
"""

from __future__ import annotations

import gzip
import json
import re
import time
from dataclasses import dataclass, field, replace
from datetime import date
from typing import Any

import yaml

from .models import RawItem, now_iso, today
from .sources.base import Http, HttpError
from .store import Store

# ---------- 采集常量 ----------

SITEMAP_URL = "https://www.starterstory.com/sitemap"
TRUSTMRR_URL = "https://trustmrr.com/"

# 正文摘录从第 350 字符起：前面是全站导航（实测约 300 字符），
# 留 9000 字符给富化层 —— 覆盖访谈的开场、收入自述和打法问答。
_TEXT_START = 350
_TEXT_LIMIT = 9000

_LOC = re.compile(r"<loc>([^<]+)</loc>")
_STORY_URL = re.compile(r"^https?://(?:www\.)?starterstory\.com/stories/([A-Za-z0-9-]+)/?$")
_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)
_OG_DESC = re.compile(r'<meta[^>]+property="og:description" content="([^"]*)"')
_SCRIPT_STYLE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.S | re.I)
_TAG = re.compile(r"<[^>]+>")
_ENTITY = re.compile(r"&[a-z]+;|&#\d+;")


# ---------- 配置 ----------

_DEFAULTS = {
    "enabled": True,
    "first_run_max": 40,
    "max_pages_per_run": 20,
    "request_interval_seconds": 2.0,
    "enrich_limit_per_run": 15,
    "starterstory": {"enabled": True},
    "trustmrr": {"enabled": True, "max_startups": 20},
}


def load_settings(store: Store) -> dict:
    """读 config/cases.yaml。缺文件用默认值 —— 案例管线允许整体静默。"""
    path = store.config_dir / "cases.yaml"
    if not path.exists():
        return dict(_DEFAULTS)
    try:
        user = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        print(f"  ! config/cases.yaml 格式有问题，按默认配置跑：{exc}")
        return dict(_DEFAULTS)
    merged = {**_DEFAULTS, **{k: v for k, v in user.items() if v is not None}}
    for key in ("starterstory", "trustmrr"):
        sub = user.get(key)
        if isinstance(sub, dict):
            merged[key] = {**_DEFAULTS[key], **sub}
    return merged


# ---------- 案例档案（data/casestudies/<slug>.md） ----------

# 展示与富化涉及的双语字段。写入与读取必须成对，漏一个就会在某一语种
# 静默丢内容 —— 与 store.save_product 的同一约束。
_BILINGUAL_TEXT_FIELDS = (
    "summary", "money_model", "verdict_reason", "replaces",
    "first_customers", "transfer_note",
)
_BILINGUAL_LIST_FIELDS = ("playbooks", "evidence_gaps")

CASE_EVIDENCE_LEVELS = ("interviewed", "stripe_verified", "ai_estimated", "cited_public")
CASE_VERDICTS = ("real", "want", "fake")
CASE_STATUSES = ("pending", "published", "rejected")


@dataclass(frozen=True, slots=True)
class CaseStudy:
    """一条真实生意案例。字段缺失如实留空，禁止编造。"""

    slug: str
    name: str
    url: str                      # 一手来源页，必填
    source: str                   # starterstory / trustmrr
    evidence_level: str           # CASE_EVIDENCE_LEVELS 之一
    status: str = "pending"       # pending / published / rejected
    case_kind: str = ""           # story / trustmrr（源内形态，仅供内部分流）
    name_zh: str = ""
    monthly_revenue_usd: float | None = None
    revenue_note_zh: str = ""     # 收入口径说明（自报/估算/验证），双语各存一份
    revenue_note_en: str = ""
    startup_cost_usd: float | None = None
    time_to_revenue: str = ""
    # 渠道名统一存英文（SEO / LinkedIn / Creator communities）——渠道多是
    # 专有名词，双语两份只会制造同步负担；中文页直接显示英文渠道名可接受。
    channels: tuple[str, ...] = ()
    ai_relevance: str = ""        # high / medium / low
    verdict: str = ""             # real / want / fake
    first_seen: str = ""
    last_seen: str = ""
    # 双语正文：summary_zh/summary_en、playbooks_zh/playbooks_en …
    texts: dict[str, str] = field(default_factory=dict)
    notes: str = ""

    def text(self, field_name: str, locale_key: str) -> str:
        """取某语种的文案字段；该语种缺失时退回另一语种，双语全缺返回空。"""
        primary = self.texts.get(f"{field_name}_{locale_key}", "")
        if primary.strip():
            return primary
        fallback = "zh" if locale_key == "en" else "en"
        return self.texts.get(f"{field_name}_{fallback}", "")

    def text_list(self, field_name: str, locale_key: str) -> list[str]:
        primary = self.texts.get(f"{field_name}_{locale_key}", "")
        rows = [row.strip() for row in primary.split("\n") if row.strip()] if primary else []
        if rows:
            return rows
        fallback = "zh" if locale_key == "en" else "en"
        fallback_text = self.texts.get(f"{field_name}_{fallback}", "")
        return [row.strip() for row in fallback_text.split("\n") if row.strip()] if fallback_text else []


def _case_frontmatter(case: CaseStudy) -> dict[str, Any]:
    front: dict[str, Any] = {
        "slug": case.slug,
        "name": case.name,
        "url": case.url,
        "source": case.source,
        "evidence_level": case.evidence_level,
        "status": case.status,
        "case_kind": case.case_kind,
        "name_zh": case.name_zh,
        "monthly_revenue_usd": case.monthly_revenue_usd,
        "revenue_note_zh": case.revenue_note_zh,
        "revenue_note_en": case.revenue_note_en,
        "startup_cost_usd": case.startup_cost_usd,
        "time_to_revenue": case.time_to_revenue,
        "channels": list(case.channels),
        "ai_relevance": case.ai_relevance,
        "verdict": case.verdict,
        "first_seen": case.first_seen,
        "last_seen": case.last_seen,
    }
    front.update(case.texts)
    return front


def case_study_from_dict(slug: str, front: dict[str, Any], notes: str) -> CaseStudy:
    texts = {
        key: str(value) for key, value in front.items()
        if key not in {
            "slug", "name", "url", "source", "evidence_level", "status", "case_kind",
            "name_zh", "monthly_revenue_usd", "revenue_note_zh", "revenue_note_en",
            "startup_cost_usd",
            "time_to_revenue", "channels", "ai_relevance", "verdict",
            "first_seen", "last_seen",
        } and isinstance(value, str)
    }
    revenue = front.get("monthly_revenue_usd")
    cost = front.get("startup_cost_usd")
    return CaseStudy(
        slug=str(front.get("slug") or slug),
        name=str(front.get("name") or slug),
        url=str(front.get("url") or ""),
        source=str(front.get("source") or ""),
        evidence_level=str(front.get("evidence_level") or ""),
        status=str(front.get("status") or "pending"),
        case_kind=str(front.get("case_kind") or ""),
        name_zh=str(front.get("name_zh") or ""),
        monthly_revenue_usd=float(revenue) if isinstance(revenue, (int, float)) else None,
        revenue_note_zh=str(front.get("revenue_note_zh") or ""),
        revenue_note_en=str(front.get("revenue_note_en") or ""),
        startup_cost_usd=float(cost) if isinstance(cost, (int, float)) else None,
        time_to_revenue=str(front.get("time_to_revenue") or ""),
        channels=tuple(str(c) for c in (front.get("channels") or [])),
        ai_relevance=str(front.get("ai_relevance") or ""),
        verdict=str(front.get("verdict") or ""),
        first_seen=str(front.get("first_seen") or ""),
        last_seen=str(front.get("last_seen") or ""),
        texts=texts,
        notes=notes,
    )


# ---------- 采集 ----------

def _fetch_sitemap_story_urls(http: Http) -> list[tuple[str, str]]:
    """拉 sitemap，返回 (slug, url) 列表。sitemap.gz 约 270KB，全部是历史清单。"""
    raw = http.get_bytes(SITEMAP_URL)
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    urls = _LOC.findall(raw.decode("utf-8", errors="replace"))
    out: list[tuple[str, str]] = []
    for url in urls:
        match = _STORY_URL.match(url)
        if match:
            out.append((match.group(1), url))
    return out


def _clean_entities(text: str) -> str:
    import html as html_module

    return html_module.unescape(_ENTITY.sub(" ", text))


def _page_text(page_html: str) -> str:
    text = _SCRIPT_STYLE.sub(" ", page_html)
    text = _TAG.sub(" ", text)
    text = _clean_entities(text)
    return re.sub(r"\s+", " ", text).strip()


def _page_title(page_html: str) -> str:
    match = _TITLE.search(page_html)
    if not match:
        return ""
    title = _clean_entities(re.sub(r"\s+", " ", match.group(1))).strip()
    # 统一去掉站名尾巴：" - Starter Story" / "· Starter Story"
    return re.split(r"\s+[-|·]\s+Starter Story\s*$", title)[0].strip()


def _page_description(page_html: str) -> str:
    match = _OG_DESC.search(page_html)
    if not match:
        return ""
    return _clean_entities(match.group(1)).strip()[:400]


def _story_item(slug: str, url: str, page_html: str, collected_at: str) -> RawItem:
    text = _page_text(page_html)
    # 正文摘录从第 350 字符起跳过全站导航；页面短得不像真实案例时
    # （测试桩或异常页）保留全文，宁可多带导航也不空手而归。
    body = text[_TEXT_START:] if len(text) > _TEXT_START + _TEXT_LIMIT // 2 else text
    return RawItem(
        source="casestudies",
        external_id=f"starterstory:{slug}",
        title=_page_title(page_html) or slug.replace("-", " "),
        url=url,
        summary=_page_description(page_html),
        published_at="",
        collected_at=collected_at,
        metrics={},
        extra={
            "kind": "casestudy",
            "case_kind": "story",
            "case_slug": slug,
            "case_site": "starterstory",
            "evidence_level": "interviewed",
        },
        payload={"text": body[:_TEXT_LIMIT]},
    )


def _walk_startup_orgs(node: Any, out: list[dict[str, Any]]) -> None:
    """深度优先收集带 /startup/ 链接和 additionalProperty 的实体。

    TrustMRR 的数据在 Next.js 的 application/json script 块里（实测不在
    ld+json 里），实体可能平铺也可能嵌在 item 字段下，遍历全树最稳。
    """
    if isinstance(node, dict):
        url = str(node.get("url") or "")
        if "/startup/" in url and isinstance(node.get("additionalProperty"), list):
            out.append(node)
        else:
            item = node.get("item")
            if "/startup/" in url and isinstance(item, dict):
                out.append(item)
        for value in node.values():
            _walk_startup_orgs(value, out)
    elif isinstance(node, list):
        for value in node:
            _walk_startup_orgs(value, out)


def _trustmrr_items(home_html: str, max_startups: int, collected_at: str) -> list[RawItem]:
    """从首页嵌入的 JSON 提取 Stripe 验证的创业收入记录。

    additionalProperty 里带 "Verified GMV, last 30 days" 等已验证数字
    （值为美元浮点）。非 JSON 的 script 块（RSC flight）解析失败就跳过，
    列表数据在能解析的那一块里。
    """
    orgs: list[dict[str, Any]] = []
    for block in re.findall(r"<script[^>]*>(.*?)</script>", home_html, re.S | re.I):
        text = block.strip()
        if not text.startswith(("{", "[")):
            continue
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            continue
        _walk_startup_orgs(data, orgs)

    items: list[RawItem] = []
    seen_slugs: set[str] = set()
    for entity in orgs:
        url = str(entity.get("url") or "")
        slug = url.rstrip("/").rsplit("/", 1)[-1]
        if not slug or slug in seen_slugs:
            continue
        seen_slugs.add(slug)
        properties: dict[str, Any] = {}
        for prop in entity.get("additionalProperty") or []:
            if isinstance(prop, dict) and prop.get("name"):
                properties[str(prop["name"])] = prop.get("value")
        monthly = None
        for key, value in properties.items():
            if "last 30 days" in key.lower() and isinstance(value, (int, float)):
                monthly = float(value)
                break
        items.append(RawItem(
            source="trustmrr",
            external_id=f"trustmrr:{slug}",
            title=str(entity.get("name") or slug),
            url=url,
            summary=str(entity.get("description") or "")[:400],
            published_at="",
            collected_at=collected_at,
            metrics=(
                {"monthly_revenue_usd": round(monthly)}
                if monthly is not None else {}
            ),
            extra={
                "kind": "casestudy",
                "case_kind": "trustmrr",
                "case_slug": slug,
                "case_site": "trustmrr",
                "evidence_level": "stripe_verified",
            },
            payload={"properties": properties},
        ))
        if len(items) >= max_startups:
            break
    return items


def collect_cases(
    store: Store, *, day: date | None = None, dry_run: bool = False,
    http: Http | None = None, settings: dict | None = None,
) -> dict[str, Any]:
    """采集新案例页，写入当天 raw，返回报告 dict。manifest 保证增量。"""
    store.ensure_dirs()
    settings = settings or load_settings(store)
    day = day or today()
    collected_at = now_iso()
    manifest = store.read_case_manifest()
    known = set(manifest)
    report: dict[str, Any] = {
        "day": day.isoformat(), "dry_run": dry_run, "new_items": 0,
        "starterstory": 0, "trustmrr": 0, "manifest_known": len(known),
    }
    if not settings.get("enabled", True):
        report["skipped"] = "config/cases.yaml 里 enabled: false"
        return report

    from .collect import build_http, load_config

    http = http or build_http(load_config(store))
    pending_items: list[RawItem] = []
    first_run = len(known) == 0

    starter_cfg = settings.get("starterstory") or {}
    if starter_cfg.get("enabled", True):
        try:
            stories = _fetch_sitemap_story_urls(http)
        except HttpError as exc:
            print(f"  ! Starter Story sitemap 拉取失败：{exc}")
            stories = []
        fresh = [(slug, url) for slug, url in stories if url not in known]
        report["starterstory_new"] = len(fresh)
        budget = settings["first_run_max"] if first_run else settings["max_pages_per_run"]
        interval = float(settings.get("request_interval_seconds") or 2.0)
        fetched = 0
        for slug, url in fresh[:budget]:
            if fetched:
                time.sleep(interval)
            try:
                page = http.get_text(url)
            except HttpError as exc:
                print(f"  ! {slug} 抓取失败：{exc}")
                continue
            pending_items.append(_story_item(slug, url, page, collected_at))
            known.add(url)
            fetched += 1
        report["starterstory"] = fetched

    trust_cfg = settings.get("trustmrr") or {}
    if trust_cfg.get("enabled", True):
        try:
            home = http.get_text(TRUSTMRR_URL)
            rows = _trustmrr_items(home, int(trust_cfg.get("max_startups") or 20), collected_at)
        except HttpError as exc:
            print(f"  ! TrustMRR 拉取失败：{exc}")
            rows = []
        rows = [row for row in rows if row.url not in known]
        for row in rows:
            known.add(row.url)
        report["trustmrr"] = len(rows)
        pending_items.extend(rows)

    report["new_items"] = len(pending_items)
    if not dry_run and pending_items:
        store.append_raw(pending_items, day)
    if not dry_run:
        for url in known:
            manifest.setdefault(url, {"seen_at": collected_at})
        store.save_case_manifest(manifest)
    return report


# ---------- 富化 ----------

_ENRICH_PROMPT_FILE = "cases.md"


def _pending_items(store: Store) -> list[RawItem]:
    """还没富化过的案例原始记录：没有档案，或档案仍是 pending。"""
    done: dict[str, str] = {}
    for case in store.iter_case_studies():
        done[case.slug] = case.status
    out: list[RawItem] = []
    for day in store.raw_days():
        for item in store.read_raw(day):
            if item.extra.get("kind") != "casestudy":
                continue
            slug = str(item.extra.get("case_slug") or "")
            if not slug or done.get(slug) == "published" or done.get(slug) == "rejected":
                continue
            out.append(item)
    # 同一案例可能跨天重复采集（manifest 之前的老数据），按 slug 留最新
    latest: dict[str, RawItem] = {}
    for item in out:
        slug = str(item.extra.get("case_slug"))
        kept = latest.get(slug)
        if kept is None or item.collected_at > kept.collected_at:
            latest[slug] = item
    return sorted(latest.values(), key=lambda item: item.collected_at)


def _prefill_revenue(item: RawItem) -> tuple[float | None, str, str]:
    """来源侧已知的收入数字不经模型 —— 数字必须来自原始记录，模型只写文案。"""
    value = item.metrics.get("monthly_revenue_usd")
    if isinstance(value, (int, float)):
        return float(value), "Stripe 支付验证（TrustMRR）", "Stripe-verified (TrustMRR)"
    level = str(item.extra.get("evidence_level") or "")
    if level == "interviewed":
        return (
            None,
            "创始人自报，未经审计（以来源页为准）",
            "Founder self-reported, unaudited (see source page)",
        )
    if level == "ai_estimated":
        return None, "平台自动研究估算，未经审计", "Platform auto-estimate, unaudited"
    return None, "", ""


def _validate(result: dict[str, Any]) -> str:
    """校验模型输出，返回失败原因；通过返回空串。"""
    if not isinstance(result, dict):
        return "结果不是 JSON object"
    if result.get("publish") is True:
        verdict = str(result.get("verdict") or "")
        if verdict not in CASE_VERDICTS:
            return f"verdict 必须是 {CASE_VERDICTS} 之一，得到 {verdict!r}"
        if not str(result.get("summary_zh") or "").strip():
            return "publish=true 时 summary_zh 不能为空"
        if not str(result.get("verdict_reason_zh") or "").strip():
            return "publish=true 时 verdict_reason_zh 不能为空"
        relevance = str(result.get("ai_relevance") or "")
        if relevance not in {"high", "medium", "low"}:
            return f"ai_relevance 必须是 high/medium/low，得到 {relevance!r}"
    return ""


def _enrich_messages(item: RawItem) -> list[dict[str, str]]:
    from .store import project_root

    prompt_path = project_root() / "config" / _ENRICH_PROMPT_FILE
    template = (
        prompt_path.read_text(encoding="utf-8")
        if prompt_path.exists()
        else "请按 JSON 输出对下面创业案例的判断。"
    )
    revenue, note_zh, note_en = _prefill_revenue(item)
    payload = {
        "title": item.title,
        "url": item.url,
        "source_page_summary": item.summary,
        "revenue_known_usd_monthly": revenue,
        "revenue_basis_note_zh": note_zh,
        "revenue_basis_note_en": note_en,
        "page_text": item.payload.get("text", "")[:_TEXT_LIMIT],
    }
    user = (
        f"{template}\n\n---\n\n以下是案例原始内容（JSON）。"
        f"revenue_known_usd_monthly 不为 null 时必须原样采用，不许改动数字：\n\n"
        f"```json\n{json.dumps(payload, ensure_ascii=False)}\n```"
    )
    return [
        {
            "role": "system",
            "content": (
                "你是 x-octo 的编辑。这个站研究 AI 应用的商业模式，读者是创业者与操盘手。"
                "只依据给到的材料写判断，拿不准就写进 evidence_gaps；禁止编造数字与事实。"
                "禁止营销话术。输出只能是 JSON object。"
            ),
        },
        {"role": "user", "content": user},
    ]


def _result_to_case(item: RawItem, result: dict[str, Any], revenue: float | None, note_zh: str, note_en: str) -> CaseStudy:
    slug = str(item.extra.get("case_slug") or "")
    texts: dict[str, str] = {}
    for name in _BILINGUAL_TEXT_FIELDS:
        for suffix in ("zh", "en"):
            key = f"{name}_{suffix}"
            value = result.get(key)
            if isinstance(value, str) and value.strip():
                texts[key] = value.strip()
    for name in _BILINGUAL_LIST_FIELDS:
        for suffix in ("zh", "en"):
            key = f"{name}_{suffix}"
            rows = result.get(key)
            if isinstance(rows, list):
                lines = [str(row).strip() for row in rows if str(row).strip()]
                if lines:
                    texts[key] = "\n".join(lines)
    cost = result.get("startup_cost_usd")
    channels = result.get("channels")
    return CaseStudy(
        slug=slug,
        name=item.title,
        url=item.url,
        source=str(item.extra.get("case_site") or item.source),
        evidence_level=str(item.extra.get("evidence_level") or ""),
        status="published" if result.get("publish") is True else "rejected",
        case_kind=str(item.extra.get("case_kind") or ""),
        name_zh=str(result.get("name_zh") or "").strip(),
        monthly_revenue_usd=revenue,
        revenue_note_zh=note_zh,
        revenue_note_en=note_en,
        startup_cost_usd=float(cost) if isinstance(cost, (int, float)) and cost >= 0 else None,
        time_to_revenue=str(result.get("time_to_revenue") or "").strip(),
        channels=tuple(str(c).strip() for c in channels if str(c).strip()) if isinstance(channels, list) else (),
        ai_relevance=str(result.get("ai_relevance") or "").strip(),
        verdict=str(result.get("verdict") or "").strip(),
        first_seen=now_iso(),
        last_seen=now_iso(),
        texts=texts,
    )


def enrich_cases(
    store: Store, *, limit: int | None = None, dry_run: bool = False,
) -> dict[str, Any]:
    """把待富化的案例原始记录交给模型，写 data/casestudies/<slug>.md。"""
    settings = load_settings(store)
    limit = limit or int(settings.get("enrich_limit_per_run") or 15)
    items = _pending_items(store)[:limit]
    report: dict[str, Any] = {
        "pending": len(items), "published": 0, "rejected": 0, "failed": 0, "dry_run": dry_run,
    }
    if not items:
        return report
    if dry_run:
        report["slugs"] = [str(item.extra.get("case_slug")) for item in items]
        return report

    from .brief import BriefError, _request

    for item in items:
        slug = str(item.extra.get("case_slug"))
        revenue, note_zh, note_en = _prefill_revenue(item)
        try:
            result = _request(_enrich_messages(item))
        except BriefError as exc:
            print(f"  ! {slug} 富化失败（下一轮重试）：{exc}")
            report["failed"] += 1
            continue
        if result is None:
            report["failed"] += 1
            continue
        reason = _validate(result)
        if reason:
            print(f"  ! {slug} 模型输出不合格（下一轮重试）：{reason}")
            report["failed"] += 1
            continue
        if result.get("publish") is not True:
            # 淘汰也要落盘：只淘汰一次，不要每天对着同一条素材重新花钱
            report["rejected"] += 1
        else:
            report["published"] += 1
        store.save_case_study(_result_to_case(item, result, revenue, note_zh, note_en))
    return report


def run(
    store: Store, *, day: date | None = None, dry_run: bool = False,
    collect_only: bool = False, enrich_only: bool = False, limit: int | None = None,
) -> dict[str, Any]:
    """案例管线入口：采集（可跳过）→ 富化（可跳过）。"""
    report: dict[str, Any] = {}
    if not enrich_only:
        report["collect"] = collect_cases(store, day=day, dry_run=dry_run)
    if not collect_only:
        report["enrich"] = enrich_cases(store, limit=limit, dry_run=dry_run)
    return report
