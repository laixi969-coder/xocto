"""静态站生成：把 data/ 里的文件变成能直接打开的网站。

不做后台服务 —— 数据本来就是文件，每天采集完重新生成一次就行。
没有服务器要维护，没有月费，双击 index.html 也能看。

    data/pool/*.md      → 产品档案
    data/analysis/*.md  → 深度分析
    data/reports/*.md   → 每日观察
            ↓
    site/index.html          首页
    site/products.html       全部产品（可筛选）
    site/p/<slug>.html       产品详情
    site/r/<date>.html       每日观察

出两个语种：中文在 site/，英文在 site/en/（内容读 data/analysis/en/、
data/reports/en/ 和 frontmatter 里的 *_en 字段）。模板只有一套，渲染两次，
语言相关的东西全在 i18n.py。
"""

from __future__ import annotations

import html
import re
import shutil
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import mistune
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import (
    CATEGORIES,
    EVENT_FIRST_DISCOVERED,
    EVENT_MATERIAL_UPDATE,
    EVENT_MARKET_CHANGE,
    EVENT_REQ_CHANGE,
    STATUS_ANALYZED,
    STATUS_MARKET_CONTEXT,
    STATUS_REJECTED,
    STATUS_WATCHING,
    Product,
    local_day,
)
from .dedupe import is_aggregator, url_host
from .i18n import LOCALES, Locale, other
from .report import ReportDoc, parse_report, split_stat
from .store import Store

# 网站上不出现任何数据源名称。用户不关心东西从哪抓来的，
# 那是实现细节 —— 泄漏到界面上既没用，也把采集策略白送出去了。
# 只暴露对用户有意义的两件事：成熟度（阶段）和方向（赛道）。
# 两个阶段的显示文字见 i18n.py，这里只留稳定的键。
STAGE_EARLY = "early"
STAGE_PROVEN = "proven"

# 生意形态。给创业者、投资者、大众同一把尺子：这还是不是一门生意。
FORM_NOT_BUSINESS = "not_business"
FORM_CHARGING = "charging"
FORM_SCALED = "scaled"
FORM_SETTLED = "settled"
FORM_KEYS = (FORM_NOT_BUSINESS, FORM_CHARGING, FORM_SCALED, FORM_SETTLED)
# 月访问或月活到这个量级，普通用户已经会碰到，新进入者很难正面抢默认位置。
SETTLED_USAGE = 10_000_000
_PAID_HINTS = (
    "订阅", "买断", "按量", "按次", "按席", "按月", "计费", "付费",
    "美元", "元/", "$", "€", "£",
    "subscription", "one-time", "per seat", "priced", "billing", "paid tier",
)
_NOT_PAID_HINTS = ("收费未披露", "pricing not disclosed", "无商业模式", "没有商业模式", "no business model")

# 线上地址。这是部署事实不是品味，所以放代码里而不是 config/。
# 用途：canonical、sitemap、og:url —— 三处都必须是绝对地址。
BASE_URL = "https://xocto.vercel.app"
OG_IMAGE = f"{BASE_URL}/logo/logo-on-light.png"

# 搜索结果里的摘要长度。中文超过这个数会被截断，不如自己控制在哪断。
DESC_LIMIT = 150

_markdown = mistune.create_markdown(plugins=["table", "strikethrough"])


@dataclass(frozen=True)
class Analysis:
    """一份深度分析。

    replaces、money、takeaway 单独抽出来 —— 创业者先要看见这三件：
    它替代了什么、怎么赚钱、能拿走什么。埋在正文里等于没有。
    """

    slug: str
    name: str
    verdict: str
    # 评级的稳定键（strong / notable / unproven）。CSS 类名和排序都认它 ——
    # 认显示文字的话，英文站的徽章会因为写的是 "Strong pick" 而全部掉色。
    verdict_key: str
    verdict_rank: int
    analyzed_at: str
    body_html: str
    excerpt: str
    replaces: str = ""
    money: str = ""
    takeaway: str = ""
    call: str = ""
    watch_next: str = ""
    takeaway_topics: dict = None


# 段首是引言、表格或列表符号 —— 那不是正文段落
_NOT_PROSE = re.compile(r"^(?:[>|]|[-*+]\s)")


def _section(body: str, *titles: str, limit: int = 200, allow_list: bool = False) -> str:
    """抽出某个二级标题下的第一段正文。找不到返回空串。

    按空行切段，不按换行切行 —— Markdown 里一段话可以折成好几行，
    原来逐行取会把"它试图把二十年积累的判断力／打包成软件卖给不懂营销的人"
    截成后半句，首页上那张卡就是一个没头没尾的残句。

    商业模式常被写成列表。默认跳过列表是为了「替代了什么」这种段落；
    抽收费结构时 allow_list=True，否则会跳过定价、落到后面的判断段。
    """
    for title in titles:
        match = re.search(
            rf"^##\s*{re.escape(title)}[^\n]*\n+(.+?)(?=\n#{{1,2}}\s|\Z)",
            body,
            re.S | re.M,
        )
        if not match:
            continue
        for para in re.split(r"\n\s*\n", match.group(1)):
            if allow_list:
                lines = [
                    re.sub(r"^\s*[-*+]\s+", "", line).strip()
                    for line in para.splitlines()
                ]
                text = "; ".join(line for line in lines if line)
            else:
                text = " ".join(para.split())
                if _NOT_PROSE.match(text):
                    continue
            if text:
                return _strip_md(text, limit)
    return ""


# 「可借鉴的做法」章节里的三个主题标记。中英文都用同一个正则匹配：
# 中文是 **产品逻辑**：/ **话术**：/ **定价结构**：
# 英文是 **Product logic**: / **Narrative**: / **Pricing structure**:
_TOPIC_LABELS = {
    "产品逻辑": "product", "Product logic": "product",
    "话术": "narrative", "Narrative": "narrative",
    "定价结构": "pricing", "Pricing structure": "pricing",
}


def _takeaway_topics(body: str, *titles: str) -> dict[str, str]:
    """抽出 '可借鉴的做法' 章节里三个主题（product/narrative/pricing）的正文。

    每段以 **产品逻辑**：或 **话术**：或 **定价结构**：开头。返回 dict，缺失的 key 值为空串。
    """
    topics: dict[str, str] = {"product": "", "narrative": "", "pricing": ""}
    section_text = ""
    for title in titles:
        match = re.search(
            rf"^##\s*{re.escape(title)}[^\n]*\n+(.+?)(?=\n#{{1,2}}\s|\Z)",
            body, re.S | re.M,
        )
        if match:
            section_text = match.group(1)
            break
    if not section_text:
        return topics
    # 按 **label**：切分
    pattern = re.compile(
        r"\*\*(" + "|".join(re.escape(k) for k in _TOPIC_LABELS) + r")\*\*[：:]\s*",
        re.M,
    )
    splits = pattern.split(section_text)
    # splits 形如 [pre, label, content, label, content, ...]
    for i in range(1, len(splits) - 1, 2):
        label = splits[i]
        key = _TOPIC_LABELS.get(label)
        if not key:
            continue
        # content 到下一个 **label** 或段落结束
        content = splits[i + 1]
        # 截到下一个段落开头（**粗体** 或空行）
        content = re.split(r"\n\s*\n", content, maxsplit=1)[0]
        text = " ".join(content.split()).strip()
        if text:
            topics[key] = text
    return topics


@dataclass(frozen=True)
class Report:
    """一份每日观察。

    hook 是给首页用的钩子 —— 列表里只写"当日趋势判断"没人会点，
    得把当天最反直觉的那句结论摆出来。

    doc 是切好版块的正文结构（见 report.py）。报告页不再渲染整篇 Markdown ——
    那样出来的是一坨没有主次的长文。
    """

    day: str
    doc: ReportDoc
    # 报头上的人话日期。格式随语种走（见 i18n.Locale.date_label），
    # 所以在加载时就定下来，不做成属性
    label: str
    hook: str = ""
    highlights: tuple[str, ...] = ()
    stats: tuple[tuple[str, str], ...] = ()


def _split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """拆出 YAML frontmatter 和正文。没有 frontmatter 就整篇当正文。"""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        front = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        front = {}
    return (front if isinstance(front, dict) else {}), parts[2]


def _strip_md(text: str, limit: int = 120) -> str:
    """把一段 Markdown 压成纯文本摘要。

    只拆语法记号，不碰正文字符。原来是把 [#>*_`()|-] 一律换成空格 ——
    中文里看不出问题，英文会把 self-hosted 打成 self hosted、
    把 (YC S26) 拆成裸词，摘要和 meta description 全被波及。
    """
    flat = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)  # 链接只留文字
    flat = re.sub(r"_([^_\n]+)_", r"\1", flat)  # 下划线强调
    flat = re.sub(r"[*`#]", "", flat)  # 加粗、行内代码、标题记号
    flat = re.sub(r"^\s*[-+]\s+", "", flat, flags=re.M)  # 列表符号
    flat = flat.replace("|", " ")  # 表格分隔
    flat = " ".join(flat.split())
    return flat[:limit] + ("…" if len(flat) > limit else "")


def _content_dir(base: Path, locale: Locale) -> Path:
    """某语种的内容目录。中文用根目录，英文用它下面的 en/。

    英文缺文件就是缺，不回退到中文 —— 英文页面里混一段中文，
    比那块干脆不出现更糟。
    """
    return base / locale.content_subdir if locale.content_subdir else base


def load_analyses(store: Store, locale: Locale) -> list[Analysis]:
    out: list[Analysis] = []
    for path in sorted(_content_dir(store.analysis_dir, locale).glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"  ! 读不了 {path.name} — {exc}")
            continue

        front, body = _split_frontmatter(text)
        slug = front.get("slug") or path.stem
        # 分析正文开头的 H1 和页面标题重复，剥掉
        body = re.sub(r"\A\s*#\s+[^\n]*\n", "", body)
        # 摘要取"一句话定位"下面那段，取不到就用正文开头
        excerpt = _section(body, *locale.heading_excerpt, limit=120)
        if not excerpt:
            excerpt = _strip_md(body)

        verdict = front.get("verdict") or ""
        out.append(
            Analysis(
                slug=slug,
                name=front.get("name") or slug,
                verdict=locale.verdict_label(verdict),
                verdict_key=locale.verdict_key(verdict),
                verdict_rank=locale.verdict_rank(verdict),
                analyzed_at=str(front.get("analyzed_at") or ""),
                body_html=_markdown(body),
                excerpt=excerpt,
                replaces=_section(body, *locale.heading_replaces),
                money=_section(body, *locale.heading_money, allow_list=True, limit=240),
                takeaway=_section(body, *locale.heading_takeaway),
                call=_section(body, *locale.heading_call, limit=300),
                watch_next=_section(body, *locale.heading_watch_next, limit=300, allow_list=True),
                takeaway_topics=_takeaway_topics(body, *locale.heading_takeaway),
            )
        )
    return sorted(out, key=lambda a: (a.verdict_rank, a.name))


def load_reports(store: Store, locale: Locale) -> list[Report]:
    out: list[Report] = []
    for path in sorted(_content_dir(store.reports_dir, locale).glob("*.md"), reverse=True):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue

        front, body = _split_frontmatter(text)
        highlights = tuple(str(h) for h in (front.get("highlights") or []))
        day = str(front.get("day") or path.stem)
        out.append(
            Report(
                day=day,
                doc=parse_report(body, locale),
                label=locale.date_label(day),
                hook=str(front.get("hook") or ""),
                highlights=highlights,
                # 每条 highlight 开头那个数字单独抽出来 —— 数字放大才是数字
                stats=tuple(split_stat(h) for h in highlights),
            )
        )
    return out


def _metric_badges(product: Product, locale: Locale) -> list[str]:
    """各类指标只显示最新一条，避免每日更新被读者误看成多份数据。"""
    latest: dict[str, tuple[str, str]] = {}

    def record(key: str, seen_at: str, label: str) -> None:
        if key not in latest or seen_at >= latest[key][0]:
            latest[key] = (seen_at, label)

    for sighting in product.sightings:
        m = sighting.metrics
        if m.get("points") is not None:
            record("points", sighting.seen_at, f"{locale.metrics['points']} {m['points']}")
        if m.get("stars") is not None:
            record("stars", sighting.seen_at, f"{locale.metrics['stars']} {m['stars']:,}")
        if m.get("raw_value"):
            unit = locale.metrics["mau" if m.get("metric") == "mau" else "visits"]
            record("scale", sighting.seen_at, f"{unit} {m['raw_value']}")
        if m.get("mom_percent") is not None:
            sign = "+" if m["mom_percent"] >= 0 else ""
            record("growth", sighting.seen_at, f"{locale.metrics['mom']} {sign}{m['mom_percent']:.0f}%")
    return [latest[key][1] for key in ("points", "stars", "scale", "growth") if key in latest]


def _external_url(product: Product) -> str:
    """对外展示的链接。

    只在它是产品自己的域名时才给 —— 指向聚合站页面的链接既暴露了采集来源，
    对用户也没价值（那不是产品官网）。
    """
    if not product.url or is_aggregator(url_host(product.url)):
        return ""
    return product.url


def _stage(product: Product) -> str:
    """成熟度。有真实流量数据的算已验证，其余都是刚冒头。返回稳定键。"""
    for sighting in product.sightings:
        if sighting.metrics.get("raw_value"):
            return STAGE_PROVEN
    return STAGE_EARLY


def _boards(product: Product, locale: Locale) -> list[str]:
    """产品上过的细分榜，去重保序。这是它的品类地位证明。"""
    seen: list[str] = []
    for sighting in product.sightings:
        for board in sighting.metrics.get("boards") or []:
            label = locale.board(board)
            if label not in seen:
                seen.append(label)
    return seen


def _scale_badge(product: Product, locale: Locale) -> str:
    """规模标签（访问量 / 月活）。只有榜单源才有。"""
    for sighting in product.sightings:
        m = sighting.metrics
        if m.get("raw_value"):
            unit = locale.metrics["mau" if m.get("metric") == "mau" else "visits"]
            return f"{unit} {m['raw_value']}"
    return ""


def _growth_rate(product: Product) -> float | None:
    for sighting in product.sightings:
        pct = sighting.metrics.get("mom_percent")
        if pct is not None:
            return pct
    return None


def _weight(product: Product) -> int:
    """产品的排序权重：能拿到的最大热度信号。"""
    best = 0
    for sighting in product.sightings:
        m = sighting.metrics
        best = max(best, m.get("points") or 0, m.get("stars") or 0)
    return best


def _usage_value(product: Product) -> float:
    """公开使用规模的数字。没有就返回 0，不编。"""
    for sighting in product.sightings:
        value = sighting.metrics.get("value")
        if isinstance(value, (int, float)) and value > 0:
            return float(value)
    return 0.0


_GENERIC_ASSISTANT_HINTS = (
    "对话", "问答", "聊天", "智能助手", "ai 助手", "ai助手", "大模型", "ai搜索",
    "chat", "assistant", "general ai", "ai search",
)


def _is_settled_general_assistant(product: Product) -> bool:
    """识别已是默认入口的通用助手，避免历史数据继续污染机会库。

    新数据应在编辑阶段得到 market_context 状态；这条规则是给已写入档案的
    历史产品的安全网。它要求同时具备「千万级公开使用量」和通用入口特征，
    因此不会把已有规模的垂直产品一并藏掉。
    """
    if _usage_value(product) < SETTLED_USAGE:
        return False
    text = " ".join((product.name, product.summary, product.summary_zh)).casefold()
    return product.category == "通用助手" or any(hint in text for hint in _GENERIC_ASSISTANT_HINTS)


def _has_paid_signal(money: str) -> bool:
    """只认商业模式正文里的收费证据，不把「未披露」读成已经在收费。"""
    text = (money or "").strip()
    if not text:
        return False
    lower = text.casefold()
    if any(hint in text or hint in lower for hint in _NOT_PAID_HINTS):
        if not any(hint in text or hint.casefold() in lower for hint in ("订阅", "买断", "按量", "按次", "$", "€", "subscription", "one-time")):
            return False
    return any(hint in text or hint.casefold() in lower for hint in _PAID_HINTS)


def _business_form(stage_key: str, category_key: str, usage_value: float, money: str) -> str:
    """生意形态只由证据来：有规模、有收费、或还没有。"""
    if stage_key == STAGE_PROVEN:
        if category_key == "通用助手" or usage_value >= SETTLED_USAGE:
            return FORM_SETTLED
        return FORM_SCALED
    if _has_paid_signal(money):
        return FORM_CHARGING
    return FORM_NOT_BUSINESS


def _audience_copy(locale: Locale, form_key: str, category_key: str) -> tuple[str, str]:
    """对投资者、对普通人各一句。按形态和赛道取，不编产品私有数字。"""
    investor = locale.t["product"]["for_investor"].get(form_key, "")
    public_map = locale.t["product"]["for_public"]
    public = public_map.get(category_key) or public_map.get("基础层", "")
    return investor, public


def _pick_sort_key(item: dict[str, Any], *, emerging: bool) -> tuple[Any, ...]:
    form = item["form_key"]
    analysis = item.get("analysis")
    if emerging:
        form_rank = {FORM_CHARGING: 0, FORM_SCALED: 1, FORM_SETTLED: 2, FORM_NOT_BUSINESS: 3}[form]
    else:
        form_rank = {FORM_SETTLED: 0, FORM_SCALED: 1, FORM_CHARGING: 2, FORM_NOT_BUSINESS: 3}[form]
    verdict = analysis.verdict_rank if analysis else 9
    niche = 1 if item["category_key"] in {"AI + 开发", "基础层"} and form == FORM_NOT_BUSINESS else 0
    return (niche, form_rank, verdict, -item["weight"])


def _opportunity_rank(item: dict[str, Any]) -> int:
    """机会库的默认次序：先看还在形成的切口，再看热度。

    热度只是证据，不能再把成熟默认入口排在用户第一次看到的位置。
    这个分数不展示给用户，也不冒充成功概率；它只负责保护阅读顺序。
    """
    rank = 10_000 if item["stage_key"] == STAGE_EARLY else 0
    rank += {FORM_CHARGING: 600, FORM_NOT_BUSINESS: 300, FORM_SCALED: 120, FORM_SETTLED: 0}[item["form_key"]]
    rank += {STATUS_ANALYZED: 200, STATUS_WATCHING: 100}.get(item["status"], 0)
    return rank + min(item["weight"], 99)


def _report_blob(report: Report | None) -> str:
    """把当天判断压成一段可检索文本，用来对齐首页证据案例。"""
    if report is None:
        return ""
    parts: list[str] = [report.hook, *report.highlights]
    doc = report.doc
    if doc is not None:
        parts.append(doc.intro)
        for section in doc.sections:
            parts.append(section.title)
            for pick in section.picks:
                parts.append(pick.name)
    return " ".join(part for part in parts if part)


def _evidence_picks(analysed_picks: list[dict[str, Any]], report: Report | None) -> list[dict[str, Any]]:
    """首页证据：先用当天判断里点到的产品，不够再用能讲成生意的案例补齐。"""
    blob = _report_blob(report).casefold()
    mentioned: list[dict[str, Any]] = []
    if blob:
        for item in analysed_picks:
            name = (item.get("name") or "").strip()
            if len(name) >= 4 and name.casefold() in blob:
                mentioned.append(item)
    ranked = sorted(analysed_picks, key=lambda item: _pick_sort_key(item, emerging=True))
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in mentioned + ranked:
        slug = item["slug"]
        if slug in seen:
            continue
        seen.add(slug)
        out.append(item)
        if len(out) == 3:
            break
    return out


def _daily_rotation(items: list[Any], day: str, *, limit: int) -> list[Any]:
    """按数据日期平移一个窗口，让首页每日内容稳定且确实轮换。"""
    if not items or limit <= 0:
        return []
    try:
        offset = int(day.replace("-", "")) % len(items)
    except ValueError:
        offset = 0
    return [items[(offset + index) % len(items)] for index in range(min(limit, len(items)))]


def _event_view(event: Any, view: dict[str, Any], store: Store, locale: Locale) -> dict[str, Any]:
    """把结构化事件与项目、`/req` 判断组合成首页机会流的一条记录。"""
    reviews = store.read_req_reviews(event.project_slug)
    review = max(reviews, key=lambda item: item.reviewed_at, default=None)
    event_labels = {
        EVENT_FIRST_DISCOVERED: locale.t["home"]["event_first"],
        EVENT_MATERIAL_UPDATE: locale.t["home"]["event_update"],
        EVENT_MARKET_CHANGE: locale.t["home"]["event_market"],
        EVENT_REQ_CHANGE: locale.t["home"]["event_req"],
    }
    signal_labels = {
        "release": locale.t["home"]["signal_release"],
        "update": locale.t["home"]["signal_update"],
        "open_source": locale.t["home"]["signal_open_source"],
        "adoption": locale.t["home"]["signal_adoption"],
    }
    return {
        **view,
        "event_type": event.event_type,
        "event_label": event_labels[event.event_type],
        "event_day": local_day(event.discovered_at),
        "occurred_day": local_day(event.occurred_at),
        "signals": [signal_labels.get(signal, signal) for signal in event.signals],
        "event_summary": event.summary,
        "req_signal": review.signal_level if review else locale.t["home"]["req_pending"],
        "req_next": review.next_validation if review else locale.t["home"]["req_pending_note"],
        "has_req": review is not None,
    }


def _facet(values: list[str]) -> list[dict[str, Any]]:
    """为机会库生成可增长的标签筛选项，按覆盖项目数排序。"""
    counts: dict[str, int] = {}
    for value in values:
        if value:
            counts[value] = counts.get(value, 0) + 1
    return [
        {"name": name, "count": count}
        for name, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    ]


def _research_view(store: Store, slug: str, locale: Locale) -> dict[str, Any]:
    """将证据、`/req` 版本及市场快照整理为详情页所需的公开信息。

    缺少市场记录时不把空白翻译成“未发现”。“未发现”只来自带覆盖范围和
    观察时间的 MarketObservation；这是跨国机会判断最重要的边界。
    """
    evidence = sorted(store.read_evidence(slug), key=lambda item: item.collected_at, reverse=True)
    evidence_by_id = {item.id: item for item in evidence}
    evidence_kind = {
        "product": locale.t["product"]["evidence_product"],
        "pricing": locale.t["product"]["evidence_pricing"],
        "open_source": locale.t["product"]["evidence_open_source"],
        "adoption": locale.t["product"]["evidence_adoption"],
        "market_comparison": locale.t["product"]["evidence_market"],
    }
    evidence_rows = [
        {
            "id": item.id,
            "url": item.url,
            "title": item.title or item.url,
            "kind": evidence_kind.get(item.source_kind, item.source_kind),
            "fact": item.fact,
            "published_at": local_day(item.published_at) if item.published_at else "",
        }
        for item in evidence
        if item.url
    ]

    gate_labels = {
        "value": locale.t["product"]["req_value"],
        "consensus": locale.t["product"]["req_consensus"],
        "model": locale.t["product"]["req_model"],
        "truth": locale.t["product"]["req_truth"],
    }
    gate_statuses = {
        "supported": locale.t["product"]["req_supported"],
        "insufficient": locale.t["product"]["req_insufficient"],
        "challenged": locale.t["product"]["req_challenged"],
    }
    reviews = store.read_req_reviews(slug)
    review = max(reviews, key=lambda item: item.reviewed_at, default=None)
    req = None
    if review:
        req = {
            "level": locale.t["product"]["req_initial"] if review.level == "initial" else locale.t["product"]["req_full"],
            "signal": review.signal_level,
            "verdict": review.verdict,
            "next_validation": review.next_validation,
            "reviewed_at": local_day(review.reviewed_at),
            "gates": [
                {
                    "name": gate_labels[gate.gate],
                    "status": gate_statuses[gate.status],
                    "reason": gate.reason,
                    "evidence": [evidence_by_id[eid] for eid in gate.evidence_ids if eid in evidence_by_id],
                }
                for gate in review.gates
            ],
        }

    supply_labels = {
        "not_found_in_covered_sources": locale.t["product"]["supply_not_found"],
        "emerging": locale.t["product"]["supply_emerging"],
        "established": locale.t["product"]["supply_established"],
    }
    demand_labels = {
        "unknown": locale.t["product"]["demand_unknown"],
        "early_signal": locale.t["product"]["demand_early"],
        "validated_signal": locale.t["product"]["demand_validated"],
    }
    observations = store.read_market_observations(slug)
    # 同一市场每天可复查；详情只展示每个市场最新一次结论。
    latest_by_market: dict[str, Any] = {}
    for observation in observations:
        previous = latest_by_market.get(observation.market)
        if previous is None or observation.observed_at > previous.observed_at:
            latest_by_market[observation.market] = observation
    market_rows = []
    for observation in sorted(latest_by_market.values(), key=lambda item: (item.ecosystem, item.market)):
        market_rows.append({
            "market": observation.market,
            "ecosystem": locale.t["product"]["ecosystem_zh"] if observation.ecosystem == "zh" else locale.t["product"]["ecosystem_en"],
            "supply": supply_labels[observation.supply_status],
            "demand": demand_labels[observation.demand_status],
            "coverage": observation.coverage,
            "observed_at": local_day(observation.observed_at),
            "evidence": [evidence_by_id[eid] for eid in observation.evidence_ids if eid in evidence_by_id],
        })

    # 只在相反生态均存在明确市场快照时标记跨国机会；可访问性从不作为本地供给。
    latest_by_ecosystem: dict[str, Any] = {}
    for observation in observations:
        previous = latest_by_ecosystem.get(observation.ecosystem)
        if previous is None or observation.observed_at > previous.observed_at:
            latest_by_ecosystem[observation.ecosystem] = observation
    zh = latest_by_ecosystem.get("zh")
    en = latest_by_ecosystem.get("en")
    cross_market = bool(
        zh and en and (
            (zh.supply_status == "not_found_in_covered_sources" and en.supply_status in {"emerging", "established"})
            or (en.supply_status == "not_found_in_covered_sources" and zh.supply_status in {"emerging", "established"})
        )
    )
    return {
        "req": req,
        "evidence": evidence_rows,
        "markets": market_rows,
        "cross_market": cross_market,
        "cross_market_label": locale.t["product"]["cross_market"],
        "markets_pending": not market_rows,
    }


def build_context(store: Store, locale: Locale) -> dict[str, Any]:
    """组装某个语种的整站数据。

    首页只放今天的判断和最多三个证据。目录、增长、往期全部是二级档案。
    """
    # 产品池是内部工作队列，不等于公开站点。淘汰项必须消失；还没有中文说明
    # 和灵感的半成品卡片对读者也没有价值，等判断层补齐后再自动上站。
    products = [p for p in store.iter_products() if _is_publishable(p)]
    analyses = load_analyses(store, locale)
    reports = load_reports(store, locale)
    report_months: list[dict[str, Any]] = []
    for report in reports:
        key = report.day[:7]
        if not report_months or report_months[-1]["key"] != key:
            report_months.append({"key": key, "label": locale.month_label(report.day), "reports": []})
        report_months[-1]["reports"].append(report)

    views = [product_view(p, locale) for p in products]
    view_by_slug = {v["slug"]: v for v in views}
    analyses = [a for a in analyses if a.slug in view_by_slug]
    by_slug = {a.slug: a for a in analyses}

    form_counts = {key: 0 for key in FORM_KEYS}
    for view in views:
        money = by_slug[view["slug"]].money if view["slug"] in by_slug else ""
        form_key = _business_form(view["stage_key"], view["category_key"], view["usage_value"], money)
        investor, public = _audience_copy(locale, form_key, view["category_key"])
        view["form_key"] = form_key
        view["form"] = locale.form(form_key)
        view["for_investor"] = investor
        view["for_public"] = public
        analysis = by_slug.get(view["slug"])
        # 目录页不该只是一排产品名：在决定点上先把「钱从哪来」露出来。
        # 缺分析时诚实留空，不用泛化文案把未知伪装成洞见。
        view["money_brief"] = _strip_md(analysis.money, 110) if analysis and analysis.money else ""
        view["opportunity_rank"] = _opportunity_rank(view)
        view.update(_research_view(store, view["slug"], locale))

    # 发现日期是事件时间而非热度或公开发布时间。旧档案没有事件时才退回
    # 到历史记录日期，避免因缺失迁移数据让机会库完全不可筛。
    discovery_days: dict[str, str] = {}
    for event_day_item in store.event_days():
        for event in store.read_events(event_day_item):
            if event.event_type == EVENT_FIRST_DISCOVERED:
                previous = discovery_days.get(event.project_slug)
                day_text = local_day(event.discovered_at)
                if not previous or day_text < previous:
                    discovery_days[event.project_slug] = day_text
    for view in views:
        view["discovered_at"] = discovery_days.get(view["slug"], view["first_seen"])
        form_counts[form_key] = form_counts.get(form_key, 0) + 1

    early = [v for v in views if v["stage_key"] == STAGE_EARLY]
    proven = [v for v in views if v["stage_key"] == STAGE_PROVEN]
    latest_day = max((v["last_seen"] for v in views), default="")

    analysed_picks = [
        {
            **view_by_slug[a.slug],
            "analysis": a,
            "money_brief": _strip_md(a.money, 90) if a.money else "",
        }
        for a in analyses
        if a.slug in view_by_slug
    ]
    # 首页只回答今天：证据案例优先用当日判断点到的产品。
    fresh_picks = _evidence_picks(analysed_picks, reports[0] if reports else None)
    used = {item["slug"] for item in fresh_picks}
    more_opportunities = sorted(
        (
            item for item in analysed_picks
            if item["slug"] not in used and item["stage_key"] == STAGE_EARLY
        ),
        key=lambda item: _pick_sort_key(item, emerging=True),
    )

    # 2. 值得留意：进了观察名单但还没展开分析的
    notables = sorted(
        (v for v in views if v["status"] == STATUS_WATCHING and v["summary"]),
        key=lambda v: -v["weight"],
    )

    # 覆盖率：没说明、没灵感的产品对读者是废卡片，得看得见还差多少
    missing_zh = [v for v in views if not v["has_summary"]]
    missing_insp = [v for v in views if not v["inspiration"]]

    # 3. 增长信号：环比异常的，那才是信号，不是排名
    movers = sorted(
        (v for v in proven if v["growth"] is not None),
        key=lambda v: -(v["growth"] or 0),
    )[:10]

    # 4. 赛道分布：给一个进入方式，不在首页罗列产品。
    # 按规范键计数，按 CATEGORIES 的顺序输出显示名 —— 顺序是编排过的，
    # 不能让某个语种的字母序把它打乱。
    counts: dict[str, int] = {}
    for view in views:
        counts[view["category_key"]] = counts.get(view["category_key"], 0) + 1
    categories = [
        {"name": locale.category(key), "count": counts[key]}
        for key in CATEGORIES
        if counts.get(key)
    ]
    project_types = _facet([view["project_type"] for view in views])
    industries = _facet([tag for view in views for tag in view["industries"]])
    jobs = _facet([tag for view in views for tag in view["jobs"]])
    regions = _facet([tag for view in views for tag in view["regions"]])
    req_signals = _facet([view["req"]["signal"] for view in views if view["req"]])
    opportunity_filters = {
        "project_types": project_types,
        "industries": industries,
        "jobs": jobs,
        "regions": regions,
        "req_signals": req_signals,
        "open_source": sum(1 for view in views if view["open_source"]),
        "cross_market": sum(1 for view in views if view["cross_market"]),
    }

    # 5. 可借鉴索引：从所有产品的 analysis.takeaway_topics 抽出来，
    # 按三个主题（产品逻辑 / 话术 / 定价结构）分桶。每条引用来源产品 + 链接。
    # 这张索引页是给创业者用的导航图——不是产品列表，是"方法列表"。
    takeaways_by_topic: dict[str, list[dict]] = {"product": [], "narrative": [], "pricing": []}
    for a in analyses:
        if a.slug not in view_by_slug:
            continue
        v = view_by_slug[a.slug]
        for key, text in (a.takeaway_topics or {}).items():
            if not text or key not in takeaways_by_topic:
                continue
            # 「无。」或 "无。" 这种诚实承认不可借鉴的，不进索引
            if re.fullmatch(r"[无N][oOoO]?\s*[。.]?", text):
                continue
            takeaways_by_topic[key].append({
                "slug": a.slug,
                "name": v["name"],
                "category": v["category"],
                "verdict": a.verdict,
                "verdict_key": a.verdict_key,
                "text": text,
            })

    # 6. 创业者能拿走的：首页不再从成熟大产品抽一条「打法」。
    # 定价结构优先，没有再退回产品逻辑；两者都只取还在形成的早期机会。
    emerging_takeaways = [
        item
        for item in (takeaways_by_topic["pricing"] or takeaways_by_topic["product"])
        if view_by_slug[item["slug"]]["stage_key"] == STAGE_EARLY
    ]
    takeaway_pool = emerging_takeaways
    today_takeaway = next(iter(_daily_rotation(takeaway_pool, latest_day, limit=1)), None)

    # 首页只消费事件，不再从旧日报或历史分析中轮换案例。当天的首次发现是主体；
    # 旧项目只能以“重要更新”出现，且卡片只陈述新事实和受影响判断。
    event_days = store.event_days()
    event_day = event_days[-1].isoformat() if event_days else ""
    event_rows = store.read_events(event_days[-1]) if event_days else []
    first_discoveries: list[dict[str, Any]] = []
    important_updates: list[dict[str, Any]] = []
    for event in sorted(event_rows, key=lambda item: item.discovered_at, reverse=True):
        view = view_by_slug.get(event.project_slug)
        if view is None:
            continue
        item = _event_view(event, view, store, locale)
        if event.event_type == EVENT_FIRST_DISCOVERED:
            first_discoveries.append(item)
        else:
            important_updates.append(item)

    # 当日市场摘要只从当天的事件流归纳，不用旧项目的规模或排行榜替代新变化。
    # “首次发现涉及”是观察范围，不暗示这是该行业全球第一次使用 AI。
    market_summary: list[dict[str, Any]] = []
    industry_counts: dict[str, int] = {}
    for item in first_discoveries:
        for industry in item["industries"]:
            industry_counts[industry] = industry_counts.get(industry, 0) + 1
    if industry_counts:
        industries_text = "、".join(
            name for name, _ in sorted(industry_counts.items(), key=lambda pair: (-pair[1], pair[0]))[:5]
        )
        market_summary.append({
            "kind": "industry",
            "title": locale.t["home"]["market_industry"],
            "text": locale.t["home"]["market_industry_text"].format(industries=industries_text),
        })
    cross_items = [item for item in first_discoveries + important_updates if item["cross_market"]]
    if cross_items:
        names = "、".join(item["name"] for item in cross_items[:5])
        market_summary.append({
            "kind": "cross_market",
            "title": locale.t["home"]["market_cross"],
            "text": locale.t["home"]["market_cross_text"].format(products=names),
        })


    # 读完一份分析之后没有下一步，旅程就断在那里了。
    # 给每个产品算好"同方向的邻居"和"上一个/下一个"，详情页才不是死路。
    ranked = sorted(views, key=lambda v: -v["weight"])
    for i, view in enumerate(ranked):
        view["prev"] = ranked[i - 1] if i > 0 else None
        view["next"] = ranked[i + 1] if i < len(ranked) - 1 else None
        same = [
            o
            for o in ranked
            if o["category_key"] == view["category_key"] and o["slug"] != view["slug"]
        ]
        # 同方向里优先推有判断的，其次是热度高的
        same.sort(key=lambda o: (o["status"] != STATUS_ANALYZED, -o["weight"]))
        view["siblings"] = same[:4]
        view["category_total"] = counts.get(view["category_key"], 0)

    return {
        # 页脚要回答的是"数据什么时候更新的"，不是"HTML 什么时候渲染的"。
        # 原来填 datetime.now()，于是不采集只重建也会让"更新于"往前走 —— 那是假消息。
        # 顺带修掉一个更烦的后果：时间戳进了 163 个页面，每次构建全部文件都变，
        # git diff 里看不出当天真正改了什么，也违反 CLAUDE.md 的幂等要求。
        "latest_day": latest_day,
        "stats": {
            "total": len(views),
            "early": len(early),
            "proven": len(proven),
            "analysed": len(analyses),
            "watching": len(notables),
            "missing_summary": len(missing_zh),
            "missing_inspiration": len(missing_insp),
        },
        "analyses": analyses,
        "analysis_by_slug": by_slug,
        "reports": reports,
        "report_months": report_months,
        # 保留下面两个上下文值，直到产品详情与方法库迁移完成；首页模板不再使用。
        "fresh_picks": fresh_picks,
        "more_opportunities": more_opportunities[:5],
        "event_day": event_day,
        "first_discoveries": first_discoveries,
        "important_updates": important_updates,
        "market_summary": market_summary,
        "notables": notables,
        "movers": movers,
        "categories": categories,
        "opportunity_filters": opportunity_filters,
        "form_keys": FORM_KEYS,
        "form_counts": form_counts,
        "products": sorted(views, key=lambda v: (-v["opportunity_rank"], -v["weight"], v["name"])),
        "takeaways_by_topic": takeaways_by_topic,
        "today_takeaway": today_takeaway,
    }


def _is_publishable(product: Product) -> bool:
    """公开站的最低门槛；内部状态和半成品仍完整保留在 data/pool。"""
    return (
        product.status not in {STATUS_REJECTED, STATUS_MARKET_CONTEXT}
        and not _is_settled_general_assistant(product)
        and bool(product.summary_zh.strip())
        and bool(product.inspiration.strip())
    )


def _canonical(path: str) -> str:
    """页面的唯一地址。

    实测线上只有带 .html 的路径能访问（/products 是 404），
    所以 canonical 必须带扩展名，否则指向一个不存在的 URL。
    首页例外：/ 和 /index.html 内容相同，统一收敛到 /。
    """
    if path in ("", "index.html"):
        return BASE_URL + "/"
    return f"{BASE_URL}/{path}"


def _describe(text: str, fallback: str) -> str:
    """给搜索结果用的摘要。空的就退回站点默认那句。"""
    flat = _strip_md(text or "", DESC_LIMIT)
    return flat or fallback


def write_seo(out_dir: Path, pages: list[tuple[str, str]], contexts: dict[str, dict[str, Any]]) -> None:
    """robots.txt、sitemap.xml 与 llms.txt。

    pages 是 (相对路径, lastmod) 列表。sitemap 只写 loc 和 lastmod ——
    priority/changefreq 主流搜索引擎早就不看了，写了是自我安慰。
    """
    (out_dir / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n" f"Sitemap: {BASE_URL}/sitemap.xml\n",
        encoding="utf-8",
    )

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, lastmod in pages:
        lines.append("  <url>")
        lines.append(f"    <loc>{_canonical(path)}</loc>")
        if lastmod:
            lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")
    (out_dir / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    zh = contexts["zh"]
    en = contexts["en"]
    latest_zh = zh["reports"][0] if zh["reports"] else None
    latest_en = en["reports"][0] if en["reports"] else None
    llms = [
        "# x-octo",
        "",
        "> A daily, bilingual radar for new and proven AI products.",
        "",
        "x-octo explains what an AI product helps people do, tracks public usage and community signals when available, and publishes editorial observations that distinguish evidence from hypotheses.",
        "",
        "## Key pages",
        "",
        f"- [Chinese home]({BASE_URL}/)",
        f"- [English home]({BASE_URL}/en/)",
        f"- [Product directory]({BASE_URL}/products.html)",
        f"- [Daily-observation archive]({BASE_URL}/reports.html)",
        f"- [Methodology]({BASE_URL}/methodology.html)",
    ]
    if latest_zh:
        llms.append(f"- [Latest Chinese daily observation]({BASE_URL}/r/{latest_zh.day}.html)")
    if latest_en:
        llms.append(f"- [Latest English daily observation]({BASE_URL}/en/r/{latest_en.day}.html)")
    llms.extend([
        "",
        "## Citation guidance",
        "",
        "Cite the canonical URL of the relevant product or daily observation. Product descriptions use public material; analysis and growth angles are editorial views. Usage figures and growth rates are dated snapshots, not claims of causation.",
        "",
        "## Freshness",
        "",
        f"Latest data update: {zh['latest_day']}",
        f"Sitemap: {BASE_URL}/sitemap.xml",
    ])
    (out_dir / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8")


def _breadcrumb(locale: Locale, canonical: str, title: str) -> dict[str, Any]:
    """所有详情页使用相同、可验证的三级面包屑。"""
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": locale.t["nav"]["home"], "item": _canonical(locale.path("index.html"))},
            {"@type": "ListItem", "position": 2, "name": locale.t["nav"]["products"], "item": _canonical(locale.path("products.html"))},
            {"@type": "ListItem", "position": 3, "name": title, "item": canonical},
        ],
    }


def _schema(
    *, locale: Locale, canonical: str, description: str, page: str, title: str,
    product: dict[str, Any] | None = None, report: Report | None = None,
) -> dict[str, Any]:
    """生成只包含页面上可核实信息的 Schema.org JSON-LD。"""
    organization = {
        "@type": "Organization",
        "@id": f"{BASE_URL}/#organization",
        "name": "x-octo",
        "url": BASE_URL,
        "description": locale.site_desc,
    }
    webpage: dict[str, Any] = {
        "@type": "WebPage",
        "@id": f"{canonical}#webpage",
        "url": canonical,
        "name": title,
        "description": description,
        "inLanguage": locale.lang,
        "isPartOf": {"@id": f"{BASE_URL}/#website"},
    }
    graph: list[dict[str, Any]] = [webpage]
    if page == "home":
        graph.extend([
            organization,
            {
                "@type": "WebSite",
                "@id": f"{BASE_URL}/#website",
                "url": BASE_URL,
                "name": "x-octo",
                "description": locale.site_desc,
                "inLanguage": locale.lang,
                "publisher": {"@id": f"{BASE_URL}/#organization"},
            },
        ])
    elif product:
        graph.extend([
            {
                "@type": "SoftwareApplication",
                "@id": f"{canonical}#software",
                "name": product["name"],
                "description": product["summary"],
                "url": canonical,
                "applicationCategory": product["category"],
                "datePublished": product["first_seen"],
                "dateModified": product["last_seen"],
                "inLanguage": locale.lang,
                "mainEntityOfPage": {"@id": f"{canonical}#webpage"},
                **({"sameAs": product["url"]} if product["url"] else {}),
            },
            _breadcrumb(locale, canonical, product["name"]),
        ])
    elif report:
        graph.extend([
            {
                "@type": "Article",
                "@id": f"{canonical}#article",
                "headline": report.hook or report.label,
                "description": description,
                "url": canonical,
                "datePublished": report.day,
                "dateModified": report.day,
                "inLanguage": locale.lang,
                "author": {"@id": f"{BASE_URL}/#organization"},
                "publisher": {"@id": f"{BASE_URL}/#organization"},
                "mainEntityOfPage": {"@id": f"{canonical}#webpage"},
            },
            _breadcrumb(locale, canonical, report.label),
        ])
    elif page == "products":
        webpage["@type"] = "CollectionPage"
    elif page == "methodology":
        webpage["@type"] = "AboutPage"
        graph.append(organization)
    elif page == "takeaways":
        webpage["@type"] = "CollectionPage"
    elif page == "privacy":
        webpage["@type"] = "AboutPage"
    return {"@context": "https://schema.org", "@graph": graph}


def product_view(product: Product, locale: Locale) -> dict[str, Any]:
    """把 Product 摊平成模板好用的字典。

    注意这里刻意不导出任何来源信息 —— 模板拿不到，就不可能不小心渲染出去。
    """
    stage = _stage(product)
    if locale.key == "zh":
        # 中文站一律优先中文。源给的多半是英文营销话术，
        # 摆在列表里读者一行扫过去等于没看见。
        summary = product.summary_zh or product.summary
        inspiration = product.inspiration
        written = bool(product.summary_zh)
    else:
        # 英文站：源自带的英文原句能用就用，说不清的才写 summary_en 覆盖。
        # 灵感没有兜底 —— 没写就整块不显示，不拿中文顶上。
        summary = product.summary_en or product.summary
        inspiration = product.inspiration_en
        written = bool(product.summary_en or product.summary)
    return {
        "slug": product.slug,
        "name": html.unescape(product.name),
        "builder": product.builder,
        "summary": summary,
        "summary_raw": product.summary,
        "has_summary": written,
        "inspiration": inspiration,
        "url": _external_url(product),
        "status": product.status,
        "status_label": locale.status(product.status),
        # category 是给人看的（随语种翻译），category_key 是数据里的规范值，
        # 计数和归组一律用键 —— 用显示文字归组，换个语种就分不到一起
        "category": locale.category(product.category),
        "category_key": product.category,
        "project_type": locale.project_type(product.project_type),
        "project_type_key": product.project_type,
        "industries": list(product.industries_en if locale.key == "en" and product.industries_en else product.industries),
        "jobs": list(product.jobs_en if locale.key == "en" and product.jobs_en else product.jobs),
        "regions": list(product.regions_en if locale.key == "en" and product.regions_en else product.regions),
        "open_source": product.open_source,
        "stage": locale.stage(stage),
        "stage_key": stage,
        "badges": _metric_badges(product, locale),
        "scale": _scale_badge(product, locale),
        "boards": _boards(product, locale),
        # 存的是 UTC，页面上显示北京日期 —— 页脚"数据截至"也取自这里，
        # 直接截前 10 位会让早上 7 点更新的站写着昨天的日期。
        "first_seen": local_day(product.first_seen),
        "last_seen": local_day(product.last_seen),
        "growth": _growth_rate(product),
        "weight": _weight(product),
        "usage_value": _usage_value(product),
        "seen_count": len(product.sightings),
        "notes": product.notes,
    }


def _page_paths(ctx: dict[str, Any]) -> set[str]:
    """某语种实际会输出哪些页面（不带语种前缀）。

    语言切换按钮要靠它决定跳去哪：产品页两个语种都有，但每日观察不一定 ——
    中文有 2026-08-11 而英文还没写的时候，直接跳过去就是一条死链。
    """
    paths = {"index.html", "products.html", "methodology.html", "privacy.html", "takeaways.html", "reports.html"}
    paths.update(f"p/{v['slug']}.html" for v in ctx["products"])
    paths.update(f"r/{r.day}.html" for r in ctx["reports"])
    return paths


def _remove_stale_pages(out_dir: Path, expected: set[str]) -> int:
    """删掉上一轮生成、这一轮已不应存在的详情页和观察页。

    只处理四个明确的生成目录和普通 HTML 文件，不遍历符号链接。这样状态从
    watching 变成 rejected 后，旧 URL 不会因为文件残留而继续在线。
    """
    removed = 0
    for rel_dir in ("p", "r", "en/p", "en/r"):
        directory = out_dir / rel_dir
        if not directory.exists() or directory.is_symlink():
            continue
        for path in directory.glob("*.html"):
            if path.is_symlink() or not path.is_file():
                continue
            rel = path.relative_to(out_dir).as_posix()
            if rel not in expected:
                path.unlink()
                removed += 1
    return removed


def _build_locale(
    env: Environment,
    out_dir: Path,
    locale: Locale,
    ctx: dict[str, Any],
    alt_paths: set[str],
    rendered: list[str],
    sitemap: list[tuple[str, str]],
) -> int:
    """渲染一个语种的全部页面，返回页面数。"""
    alt = other(locale)
    base = out_dir / locale.prefix if locale.prefix else out_dir
    base.mkdir(parents=True, exist_ok=True)
    (base / "p").mkdir(exist_ok=True)
    (base / "r").mkdir(exist_ok=True)

    def write(rel: str, template: str, page: str, description: str, **extra: Any) -> None:
        # root 是页面到站点根的相对路径。顶层页面为空，子目录页面要回退一级 ——
        # 这样整站可以直接双击打开，不需要起服务器。
        # 英文站整体多一层（site/en/），所以前缀里的斜杠也要算进去。
        root = "../" * (locale.prefix.count("/") + rel.count("/"))
        # 另一语种的同一个页面。那边没有这一页就退回它的首页，
        # 绝不生成指向不存在文件的链接。
        # 退回首页时不发 hreflang —— hreflang 声明的是"同一内容的另一语言版本"，
        # 指到首页是假话，会让搜索引擎把两页当互译。
        alt_exact = rel in alt_paths
        alt_rel = rel if alt_exact else "index.html"
        schema_title = extra.pop("schema_title", locale.site_name)
        canonical = _canonical(locale.path(rel))
        html = env.get_template(template).render(
            **ctx,
            page=page,
            root=root,
            locale=locale,
            t=locale.t,
            canonical=canonical,
            description=description,
            og_image=OG_IMAGE,
            schema=_schema(
                locale=locale, canonical=canonical, description=description,
                page=page, title=schema_title, product=extra.get("product"), report=extra.get("report"),
            ),
            alt_locale=alt,
            alt_href=f"{root}{alt.prefix}{alt_rel}",
            alt_canonical=_canonical(alt.path(alt_rel)) if alt_exact else "",
            **extra,
        )
        (base / rel).write_text(html, encoding="utf-8")
        rendered.append(html)

    stats = ctx["stats"]
    write("index.html", "index.html", "home", locale.site_desc, schema_title=f"x-octo · {locale.site_tagline}")
    sitemap.append((locale.path("index.html"), ctx["latest_day"]))

    write(
        "products.html", "products.html", "products",
        locale.t["products"]["desc"].format(total=stats["total"]),
        schema_title=locale.t["products"]["title"],
    )
    sitemap.append((locale.path("products.html"), ctx["latest_day"]))

    write(
        "methodology.html", "methodology.html", "methodology",
        locale.t["methodology"]["lede"], schema_title=locale.t["methodology"]["title"],
    )
    sitemap.append((locale.path("methodology.html"), ctx["latest_day"]))

    write(
        "takeaways.html", "takeaways.html", "takeaways",
        locale.t["takeaways"]["desc"].format(total=len(ctx["takeaways_by_topic"]["product"]) + len(ctx["takeaways_by_topic"]["narrative"]) + len(ctx["takeaways_by_topic"]["pricing"])),
        schema_title=locale.t["takeaways"]["title"],
    )
    sitemap.append((locale.path("takeaways.html"), ctx["latest_day"]))

    write(
        "privacy.html", "privacy.html", "privacy",
        locale.t["privacy"]["lede"], schema_title=locale.t["privacy"]["title"],
    )
    sitemap.append((locale.path("privacy.html"), ctx["latest_day"]))

    write(
        "reports.html", "reports.html", "reports",
        locale.t["report"]["archive_lede"], schema_title=locale.t["report"]["archive_title"],
    )
    sitemap.append((locale.path("reports.html"), ctx["latest_day"]))

    by_slug = ctx["analysis_by_slug"]
    for view in ctx["products"]:
        rel = f"p/{view['slug']}.html"
        write(
            rel, "product.html", "products",
            # 用产品自己的一句话介绍当摘要 —— 上百个页面共用一句
            # 通用描述，对搜索引擎等于没有描述
            _describe(view["summary"], locale.site_desc),
            product=view,
            analysis=by_slug.get(view["slug"]),
            schema_title=view["name"],
        )
        sitemap.append((locale.path(rel), view["last_seen"]))

    for report in ctx["reports"]:
        rel = f"r/{report.day}.html"
        # 当天那句钩子就是最好的搜索摘要
        write(rel, "report.html", "reports", _describe(report.hook, locale.site_desc),
              report=report, schema_title=f"{report.day} {locale.t['report']['kicker']}")
        sitemap.append((locale.path(rel), report.day))

    return 4 + len(ctx["products"]) + len(ctx["reports"])


def build(store: Store, out_dir: Path | None = None) -> Path:
    """生成整站（中文 + 英文），返回输出目录。"""
    out_dir = out_dir or store.root / "site"
    templates_dir = store.root / "templates"
    if not templates_dir.exists():
        raise FileNotFoundError(f"找不到模板目录 {templates_dir}")

    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    out_dir.mkdir(parents=True, exist_ok=True)

    # 两个语种的数据先各自组好，再开始渲染 —— 语言切换要知道对面有没有这一页
    contexts = {loc.key: build_context(store, loc) for loc in LOCALES}
    paths = {key: _page_paths(ctx) for key, ctx in contexts.items()}

    pages = 0
    rendered: list[str] = []  # 留给字体子集化抓标题字符（两个语种一起，
    #                            30 个产品名本身是中文，英文页面上也要有字）
    sitemap: list[tuple[str, str]] = []   # (相对路径, lastmod)

    for locale in LOCALES:
        pages += _build_locale(
            env, out_dir, locale, contexts[locale.key],
            paths[other(locale).key], rendered, sitemap,
        )

    expected = {
        locale.path(rel)
        for locale in LOCALES
        for rel in paths[locale.key]
    }
    stale = _remove_stale_pages(out_dir, expected)
    if stale:
        print(f"  清掉 {stale} 个不再发布的旧页面")

    css_src = templates_dir / "style.css"
    if css_src.exists():
        shutil.copy2(css_src, out_dir / "style.css")

    # 品牌标识：两个版本（浅色底 / 暗色底），由 CSS 的 --logo token 挑
    logo_src = templates_dir / "logo"
    if logo_src.is_dir():
        logo_out = out_dir / "logo"
        logo_out.mkdir(exist_ok=True)
        for f in sorted(logo_src.glob("*.png")):
            shutil.copy2(f, logo_out / f.name)

    write_seo(out_dir, sitemap, contexts)
    print(f"  robots.txt + sitemap.xml + llms.txt（{len(sitemap)} 个 URL）")

    from .fonts import build_fonts

    print(f"  字体：{build_fonts(templates_dir, out_dir, rendered)}")
    print(f"  生成 {pages} 个页面 → {out_dir}")
    return out_dir
