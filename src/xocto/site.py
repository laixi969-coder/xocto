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
import hashlib
import re
import shutil
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

import mistune
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup, escape as html_escape

from .demand import demand_read
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
    is_product_attributed_metric,
    local_day,
    public_req_labels,
    req_conclusion,
    scrub_pending_phrase,
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

# 英文站不展示未经翻译的中日韩原始文本。采集层必须保留原文，不能为了
# 展示而改写证据；因此在渲染边界拦住它，并使用明确的英文待补充文案。
# 产品名称例外：check_design.py 会按产品档案中的专名白名单处理。
_CJK_TEXT = re.compile(r"[　-〿㐀-䶿一-鿿＀-￯가-힯]")
_ENGLISH_PROSE = re.compile(r"\b[A-Za-z][A-Za-z'’-]*\b(?:[\s,;:—]+[A-Za-z][A-Za-z'’-]*\b){4,}")
_GENERIC_REQ_REASON_HINTS = ("描述模糊", "价值主张不明确", "具体痛点与使用场景")
_PUBLIC_SOURCE_NAMES = (
    "Product Hunt", "Hacker News", "AICPB", "officialfeeds", "marketfeeds",
    "newssearch", "searchfeeds", "QbitAI", "量子位", "GeekPark", "TechCrunch",
    "VentureBeat", "Crunchbase News", "Sifted", "Tech.eu", "Ars Technica",
)


def _english_text(value: str, fallback: str = "") -> str:
    """只让已是英文的自由文本进入英文站。"""
    text = (value or "").strip()
    return text if text and not _CJK_TEXT.search(text) else fallback


def _chinese_text(value: str, fallback: str = "") -> str:
    """保留中文与必要专名，移除旧数据中用分隔符拼入的英文说明段。"""
    text = (value or "").strip()
    if not text or not _CJK_TEXT.search(text):
        return fallback
    text = _ENGLISH_PROSE.sub("", text)
    text = re.sub(r"^\s*[|｜、，:：—-]+\s*", "", text)
    text = re.sub(r"\s*[|｜、，:：]+$", "", text)
    return " ".join(text.split()) or fallback


def _sentence_excerpt(value: str, limit: int = 100) -> str:
    text = " ".join((value or "").split())
    if len(text) <= limit:
        return text.rstrip("。；; ")
    sentence_end = next(
        (match.end() for match in re.finditer(r"[。！？!?\.]", text) if match.end() >= 18),
        None,
    )
    return (text[:sentence_end] if sentence_end and sentence_end <= limit else text[:limit]).rstrip("。；，、;:： ")


def _neutralize_public_source_names(value: str, locale: Locale) -> str:
    """Remove collection-channel names at the final public rendering boundary."""
    text = value or ""
    replacement = "public reporting" if locale.key == "en" else "公开资料"
    for name in sorted(_PUBLIC_SOURCE_NAMES, key=len, reverse=True):
        # Feed headlines commonly append the publisher as a bare suffix. Removing
        # that suffix reads better than replacing it with another noun phrase.
        suffix = re.compile(rf"\s*(?:[-—|·:]\s*)?{re.escape(name)}\s*$", re.IGNORECASE)
        if suffix.search(text):
            text = suffix.sub("", text)
        text = re.sub(re.escape(name), replacement, text, flags=re.IGNORECASE)
    return " ".join(text.split())


def _public_product_name(value: str, locale: Locale) -> str:
    name = _neutralize_public_source_names(html.unescape(value), locale)
    return name or ("Market development" if locale.key == "en" else "市场动态")


_TAG_ALIASES_ZH = {
    "industry": {
        "软件": "软件开发", "软件研发": "软件开发", "软件开发者": "软件开发",
        "软件与信息技术服务": "软件开发", "电子商务": "电商",
        "市场营销": "营销", "数字营销": "营销", "影视": "影视制作",
        "视频制作": "影视制作", "视频创作": "影视制作", "学术研究": "科研",
        "办公": "办公效率", "个人效率": "办公效率", "办公自动化": "办公效率",
        "通用办公": "办公效率", "远程办公": "办公效率", "游戏开发": "游戏",
        "数字内容创作": "内容创作",
    },
    "job": {
        "开发者": "软件开发者", "开发人员": "软件开发者", "软件工程师": "软件开发者",
        "程序员": "软件开发者", "AI工程师": "AI 工程师", "研究员": "研究人员",
        "开发运维工程师": "DevOps 工程师", "运维工程师": "DevOps 工程师",
        "普通用户": "个人用户", "视频制作人": "视频创作者",
    },
    "region": {},
}

_TAG_ALIASES_EN = {
    "industry": {
        "software development": "Software Development", "software": "Software Development",
        "software developers": "Software Development", "software & it services": "Software Development",
        "film": "Film & Video Production", "film production": "Film & Video Production",
        "video production": "Film & Video Production", "video creation": "Film & Video Production",
        "digital marketing": "Marketing", "academic research": "Research",
        "office": "Workplace Productivity", "personal productivity": "Workplace Productivity",
        "remote work": "Workplace Productivity", "games": "Gaming", "game development": "Gaming",
        "digital content creation": "Content Creation",
    },
    "job": {
        "developer": "Software Developer", "developers": "Software Developer",
        "software engineer": "Software Developer", "software engineers": "Software Developer",
        "software developer": "Software Developer", "programmer": "Software Developer",
        "ai engineers": "AI Engineer", "researchers": "Researcher",
        "content creators": "Content Creator", "video editors": "Video Editor",
        "security engineers": "Security Engineer", "penetration testers": "Penetration Tester",
        "students": "Student", "animators": "Animator", "job seekers": "Job Seeker",
        "project managers": "Project Manager", "designers": "Designer",
        "frontend developers": "Frontend Developer", "qa engineers": "QA Engineer",
        "live stream operators": "Live Stream Operator", "video creators": "Video Creator",
        "video creator": "Video Creator",
    },
    "region": {"us": "United States", "usa": "United States", "united states": "United States"},
}


def _raw_localized_tags(locale: Locale, english: tuple[str, ...], chinese: tuple[str, ...]) -> list[str]:
    """Return only tags that really exist in this edition; never cross-language fallback."""
    if locale.key != "en":
        return [tag.strip() for tag in chinese if tag.strip()]
    return [tag.strip() for tag in english if _english_text(tag)]


def _localized_tags(
    locale: Locale,
    english: tuple[str, ...],
    chinese: tuple[str, ...],
    dimension: str = "",
) -> list[str]:
    """Normalize obvious public-label duplicates without changing archived source tags."""
    raw = _raw_localized_tags(locale, english, chinese)
    aliases = (_TAG_ALIASES_EN if locale.key == "en" else _TAG_ALIASES_ZH).get(dimension, {})
    normalized = [aliases.get(tag.casefold() if locale.key == "en" else tag, tag) for tag in raw]
    return list(dict.fromkeys(normalized))


_REQ_SIGNAL_EN = {
    "需求信号明确": "Clear demand signal",
    "初步成立": "Initial support",
    "需求存疑": "Demand in question",
    "需求有依据": "Demand is evidenced",
    "解决问题，但需求刚性不足": "Useful problem, weak urgency",
    "问题已识别，需求强度未明": "Problem identified, demand strength unclear",
}


def _scrub_pending_phrase(text: str) -> str:
    return scrub_pending_phrase(text)


def _req_signal_label(signal: str, locale: Locale) -> str:
    if signal == "待验证":
        signal = "需求存疑"
    if locale.key != "en":
        return signal
    return _REQ_SIGNAL_EN.get(signal, _english_text(signal, locale.t["home"]["req_pending"]))


def _public_req(review: Any, locale: Locale) -> tuple[str, str]:
    """对外需求判定与证据档；旧档案里的「待验证」在这里被重算掉。"""
    verdict_label, signal = public_req_labels(review.verdict, review.signal_level, review.gates)
    return _req_signal_label(verdict_label, locale), _req_signal_label(signal, locale)


def _latest_req_review(reviews: list[Any]) -> Any | None:
    """选出应公开的一版判断：完整判断永远不被较新的基础初判降级。"""
    if not reviews:
        return None
    return max(
        reviews,
        key=lambda item: (
            1 if item.level == "full" else 0,
            item.day,
            item.reviewed_at,
        ),
    )


def _req_decision_reason(review: Any, locale: Locale, product_summary: str = "") -> str:
    """首页展示当前停在哪道闸门；英文站只输出英文边界说明。"""
    challenged = next((gate for gate in review.gates if gate.status == "challenged"), None)
    blocking = challenged or next((gate for gate in review.gates if gate.status == "insufficient"), None)
    decisive = blocking or (review.gates[-1] if review.gates else None)
    if decisive is None:
        return review.next_validation if locale.key != "en" else locale.t["home"]["req_pending_note"]
    if locale.key != "en":
        value_gate = review.gates[0] if review.gates else None
        if product_summary and (value_gate is None or value_gate.status != "supported"):
            summary = _sentence_excerpt(product_summary)
            return (
                f"产品主张帮助用户完成：“{summary}”。"
                "具体痛点强度与不采用代价尚未由用户证据核验。"
            )
        if product_summary and any(fragment in decisive.reason for fragment in _GENERIC_REQ_REASON_HINTS):
            summary = _sentence_excerpt(product_summary)
            return f"产品主张帮助用户完成：“{summary}”。具体痛点强度与不采用代价尚未由用户证据核验。"
        return _scrub_pending_phrase(decisive.reason)
    gate = locale.t["product"][f"req_{decisive.gate}"]
    return locale.t["home"][f"boundary_{decisive.status}"].format(gate=gate)


def _gate_reason_for_display(gate: Any, product: Any | None, locale: Locale) -> str:
    """价值关即使买方不清，也要先写出需求和痛点。"""
    raw = gate.reason if locale.key != "en" else _english_text(
        gate.reason, locale.t["product"]["req_reason_pending"]
    )
    summary = ""
    if product is not None:
        summary = product.summary_zh if locale.key != "en" else (product.summary_en or product.summary)
        summary = _sentence_excerpt(" ".join((summary or "").split()))
    if (
        gate.gate == "value"
        and gate.status != "supported"
        and summary
        and "它解决的用户需求和痛点" not in (raw or "")
        and "user need and pain" not in (raw or "").casefold()
    ):
        if locale.key != "en":
            return f"产品主张帮助用户完成：“{summary}”。具体痛点强度与不采用代价尚未由用户证据核验。"
        return f"The product claims to help users complete: “{summary}”. User evidence has not yet verified pain intensity or the cost of doing without it."
    return _scrub_pending_phrase(raw)


def _opportunity_action(review: Any | None, locale: Locale) -> str:
    """把内部闸门转换为创业者可执行的注意力决策。"""
    if review is None:
        key = "clue"
    else:
        verdict, signal = req_conclusion(review.gates) if review.gates else (review.verdict, review.signal_level)
        if verdict == "pseudo_demand" or any(gate.status == "challenged" for gate in review.gates):
            key = "avoid"
        elif verdict == "true_demand":
            key = "investigate" if signal == "需求信号明确" else "watch"
        else:
            key = "clue"
    return locale.t["home"][f"action_{key}"]


def _is_market_query_evidence(item: Any) -> bool:
    return item.title == "Public market coverage query" or (
        url_host(item.url).endswith("bing.com") and "format=rss" in item.url
    )


def _localized_evidence_copy(item: Any, product: Any | None, locale: Locale) -> tuple[str, str]:
    """证据事实保持原始存档，页面只投影当前语种，不展示双语拼接。"""
    raw_title = (item.title or "").strip()
    raw_fact = (item.fact or "").strip()
    product_name = product.name if product is not None else ""
    host = url_host(item.url).removeprefix("www.")
    is_product_title = bool(product_name and raw_title.casefold() == product_name.casefold())
    if locale.key == "en":
        title = _english_text(raw_title) if is_product_title else (_english_text(raw_title) or host)
        fact = _english_text(raw_fact)
        if not fact and product is not None and item.source_kind in {"product", "open_source"}:
            fact = _english_text(product.summary_en) or _english_text(product.summary)
        return (
            _neutralize_public_source_names(title or locale.t["product"]["evidence_link"], locale),
            scrub_pending_phrase(_neutralize_public_source_names(fact, locale)),
        )
    # 中文页不能直接倾倒英文采集摘要：标题与事实都经 _chinese_text 投影，
    # 整段英文的原始标题退到域名，混排标题保留中文部分和必要专名。
    title = _chinese_text(raw_title)
    if not title and is_product_title:
        title = product_name
    if not title:
        title = host or locale.t["product"]["evidence_link"]
    if product is not None and item.source_kind in {"product", "open_source"}:
        fact = _chinese_text(product.summary_zh)
    else:
        fact = _chinese_text(raw_fact)
    return (
        _neutralize_public_source_names(title, locale),
        scrub_pending_phrase(_neutralize_public_source_names(fact, locale)),
    )

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
    # 正文里的 Markdown 表格会包含 "| --- |"；只有独占一行的 --- 才是
    # frontmatter 边界，不能用普通字符串 split。
    parts = re.split(r"^---\s*$", text, maxsplit=2, flags=re.MULTILINE)
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
                body_html=_desk_wrap_analysis_html(scrub_pending_phrase(_finish_inline_emphasis(_markdown(body)))),
                excerpt=scrub_pending_phrase(excerpt),
                replaces=scrub_pending_phrase(_section(body, *locale.heading_replaces)),
                money=scrub_pending_phrase(_section(body, *locale.heading_money, allow_list=True, limit=240)),
                takeaway=scrub_pending_phrase(_section(body, *locale.heading_takeaway)),
                call=scrub_pending_phrase(_section(body, *locale.heading_call, limit=300)),
                watch_next=scrub_pending_phrase(_section(body, *locale.heading_watch_next, limit=300, allow_list=True)),
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
        highlights = tuple(_scrub_pending_phrase(str(h)) for h in (front.get("highlights") or []))
        day = str(front.get("day") or path.stem)
        out.append(
            Report(
                day=day,
                doc=parse_report(body, locale),
                label=locale.date_label(day),
                hook=_scrub_pending_phrase(str(front.get("hook") or "")),
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
        if not is_product_attributed_metric(m):
            continue
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


_INTERNAL_METHOD_RE = re.compile(r"`?/req`?")


def _public_page_url(url: str) -> str:
    """读者能看到的外链。聚合站链接既暴露来源，也不是产品自己的页面。"""
    if not url or is_aggregator(url_host(url)):
        return ""
    return url


def _public_event_summary(text: str) -> str:
    """事件摘要可以保留判断变化，但不能把内部方法名带上首页。"""
    cleaned = _INTERNAL_METHOD_RE.sub("", text or "")
    return re.sub(r"\s+", " ", cleaned).strip().lstrip("；;").strip()


def _external_url(product: Product) -> str:
    """对外展示的链接。

    只在它是产品自己的域名时才给 —— 指向聚合站页面的链接既暴露了采集来源，
    对用户也没价值（那不是产品官网）。
    """
    return _public_page_url(product.url)


def _stage(product: Product) -> str:
    """成熟度。有真实流量数据的算已验证，其余都是刚冒头。返回稳定键。"""
    for sighting in product.sightings:
        if is_product_attributed_metric(sighting.metrics) and sighting.metrics.get("raw_value"):
            return STAGE_PROVEN
    return STAGE_EARLY


def _boards(product: Product, locale: Locale) -> list[str]:
    """产品上过的细分榜，去重保序。这是它的品类地位证明。"""
    seen: list[str] = []
    for sighting in product.sightings:
        if not is_product_attributed_metric(sighting.metrics):
            continue
        for board in sighting.metrics.get("boards") or []:
            label = locale.board(board)
            if label not in seen:
                seen.append(label)
    return seen


def _scale_badge(product: Product, locale: Locale) -> str:
    """规模标签（访问量 / 月活）。只有榜单源才有。"""
    for sighting in product.sightings:
        m = sighting.metrics
        if not is_product_attributed_metric(m):
            continue
        if m.get("raw_value"):
            unit = locale.metrics["mau" if m.get("metric") == "mau" else "visits"]
            return f"{unit} {m['raw_value']}"
    return ""


def _growth_rate(product: Product) -> float | None:
    for sighting in product.sightings:
        if not is_product_attributed_metric(sighting.metrics):
            continue
        pct = sighting.metrics.get("mom_percent")
        if pct is not None:
            return pct
    return None


def _weight(product: Product) -> int:
    """产品的排序权重：能拿到的最大热度信号。"""
    best = 0
    for sighting in product.sightings:
        m = sighting.metrics
        if not is_product_attributed_metric(m):
            continue
        best = max(best, m.get("points") or 0, m.get("stars") or 0)
    return best


def _usage_value(product: Product) -> float:
    """公开使用规模的数字。没有就返回 0，不编。"""
    for sighting in product.sightings:
        if not is_product_attributed_metric(sighting.metrics):
            continue
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


def _daily_event_selection(items: list[dict[str, Any]], *, limit: int = 6) -> list[dict[str, Any]]:
    """Pick a varied, finite front page from one day's publishable events.

    A daily edition should not become a raw dump.  Prefer items with an actual
    editorial read, then give different categories a chance before filling the
    remaining slots.  Every selected item still comes from the same content day.
    """
    ranked = sorted(
        items,
        key=lambda item: (
            item.get("status") != STATUS_ANALYZED,
            item.get("status") == STATUS_WATCHING,
            -int(item.get("opportunity_rank") or 0),
            -int(item.get("weight") or 0),
            item.get("name") or "",
        ),
    )
    selected: list[dict[str, Any]] = []
    used_categories: set[str] = set()
    for item in ranked:
        category = str(item.get("category_key") or "")
        if category and category in used_categories:
            continue
        selected.append(item)
        used_categories.add(category)
        if len(selected) == limit:
            return selected
    for item in ranked:
        if item not in selected:
            selected.append(item)
        if len(selected) == limit:
            break
    return selected


def _proven_business_selection(
    items: list[dict[str, Any]], *, limit: int = 3
) -> list[dict[str, Any]]:
    """Choose useful benchmarks, not the loudest growth leaderboard.

    Scaled businesses retain more entry value than settled default products.  Within
    that boundary, public usage scale is the strongest deterministic signal.  Give
    distinct categories a chance before filling any remaining slots.
    """
    ranked = sorted(
        items,
        key=lambda item: (
            item.get("form_key") != FORM_SCALED,
            -float(item.get("usage_value") or 0),
            item.get("name") or "",
        ),
    )
    selected: list[dict[str, Any]] = []
    categories: set[str] = set()
    for item in ranked:
        category = str(item.get("category_key") or "")
        if category and category in categories:
            continue
        selected.append(item)
        categories.add(category)
        if len(selected) == limit:
            return selected
    for item in ranked:
        if item not in selected:
            selected.append(item)
        if len(selected) == limit:
            break
    return selected


def _business_card_view(view: dict[str, Any], store: Store, locale: Locale) -> dict[str, Any]:
    """把已验证产品收成与机会流相同的卡片结构。"""
    reviews = store.read_req_reviews(view["slug"])
    review = _latest_req_review(reviews)
    decision_reason = (
        _req_decision_reason(review, locale, view["summary"]) if review else locale.t["home"]["req_pending_note"]
    )
    verdict_label = _public_req(review, locale)[0] if review else locale.t["home"]["req_pending"]
    return {
        **view,
        "event_type": "proven_business",
        "event_label": locale.t["home"]["event_proven"],
        "event_day": view["last_seen"],
        "occurred_day": view["first_seen"],
        "event_summary": "",
        "req_signal": verdict_label,
        "req_reason": decision_reason,
        "opportunity_action": _opportunity_action(review, locale),
        "opportunity_text": view["inspiration"] or view["summary"],
        "opportunity_boundary": locale.t["home"]["evidence_boundary"].format(reason=decision_reason),
        "has_req": review is not None,
    }


def _event_view(event: Any, view: dict[str, Any], store: Store, locale: Locale) -> dict[str, Any]:
    """把结构化事件与项目、`/req` 判断组合成首页机会流的一条记录。"""
    reviews = store.read_req_reviews(event.project_slug)
    review = _latest_req_review(reviews)
    event_labels = {
        EVENT_FIRST_DISCOVERED: locale.t["home"]["event_first"],
        EVENT_MATERIAL_UPDATE: locale.t["home"]["event_update"],
        EVENT_MARKET_CHANGE: locale.t["home"]["event_market"],
        EVENT_REQ_CHANGE: locale.t["home"]["event_req"],
    }
    raw_summary = _public_event_summary(
        (event.summary_en if locale.key == "en" else event.summary) or ""
    )
    # 旧档案中曾以采集器状态充当事件摘要；它没有解释产品发生了什么，
    # 不应占用首页的阅读空间。保留有事实内容的人工/模型摘要。
    if raw_summary in {"首次发现项目", "发现新的公开信号"}:
        raw_summary = ""
    event_summary = raw_summary if locale.key != "en" else _english_text(raw_summary)
    event_summary = _scrub_pending_phrase(event_summary)
    decision_reason = _req_decision_reason(review, locale, view["summary"]) if review else locale.t["home"]["req_pending_note"]
    return {
        **view,
        "event_type": event.event_type,
        "event_label": event_labels[event.event_type],
        "event_day": local_day(event.discovered_at),
        "occurred_day": local_day(event.occurred_at),
        "event_summary": event_summary,
        "req_signal": (_public_req(review, locale)[0] if review else locale.t["home"]["req_pending"]),
        "req_reason": decision_reason,
        "opportunity_action": _opportunity_action(review, locale),
        "opportunity_text": view["inspiration"] or view["summary"],
        "opportunity_boundary": locale.t["home"]["evidence_boundary"].format(reason=decision_reason),
        "req_next": (
            review.next_validation if locale.key != "en" else _english_text(
                review.next_validation, locale.t["home"]["req_pending_note"]
            )
        ) if review else locale.t["home"]["req_pending_note"],
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
    product = store.load_product(slug)
    evidence = sorted(store.read_evidence(slug), key=lambda item: item.collected_at, reverse=True)
    evidence_by_id = {item.id: item for item in evidence}
    evidence_kind = {
        "product": locale.t["product"]["evidence_product"],
        "pricing": locale.t["product"]["evidence_pricing"],
        "open_source": locale.t["product"]["evidence_open_source"],
        "adoption": locale.t["product"]["evidence_adoption"],
        "market_comparison": locale.t["product"]["evidence_market"],
        "pain": locale.t["product"]["evidence_pain"],
        "workaround": locale.t["product"]["evidence_workaround"],
        "customer_case": locale.t["product"]["evidence_customer_case"],
        "payment": locale.t["product"]["evidence_payment"],
        "procurement": locale.t["product"]["evidence_payment"],
        "revenue": locale.t["product"]["evidence_payment"],
        "retention": locale.t["product"]["evidence_retention"],
        "repeat_purchase": locale.t["product"]["evidence_retention"],
        "delivery": locale.t["product"]["evidence_delivery"],
    }
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
    review = _latest_req_review(reviews)
    observations = store.read_market_observations(slug)
    latest_by_market: dict[str, Any] = {}
    for observation in observations:
        previous = latest_by_market.get(observation.market)
        if previous is None or observation.observed_at > previous.observed_at:
            latest_by_market[observation.market] = observation
    cited_ids = {
        evidence_id
        for gate in (review.gates if review else ())
        for evidence_id in gate.evidence_ids
    }
    cited_ids.update(
        evidence_id
        for observation in latest_by_market.values()
        for evidence_id in observation.evidence_ids
    )
    evidence_rows = []
    seen_evidence_urls: set[str] = set()
    for item in evidence:
        public_url = _public_page_url(item.url)
        if not public_url or _is_market_query_evidence(item):
            continue
        if item.source_kind == "market_comparison" and item.id not in cited_ids:
            continue
        kind = evidence_kind.get(item.source_kind, item.source_kind)
        title, fact = _localized_evidence_copy(item, product, locale)
        if public_url in seen_evidence_urls:
            continue
        seen_evidence_urls.add(public_url)
        evidence_rows.append({
            "id": item.id,
            "url": public_url,
            "title": title,
            "kind": kind,
            "fact": fact,
            "published_at": local_day(item.published_at) if item.published_at else "",
        })
    public_evidence_by_id = {item["id"]: item for item in evidence_rows}
    public_read = demand_read(product, review, evidence, english=locale.key == "en")
    demand_maturity_labels = {
        "unclear": locale.t["product"]["demand_maturity_unclear"],
        "job_only": locale.t["product"]["demand_maturity_job"],
        "evidenced": locale.t["product"]["demand_maturity_evidenced"],
        "challenged": locale.t["product"]["demand_maturity_challenged"],
    }
    business_maturity_labels = {
        "unverified": locale.t["product"]["business_maturity_unverified"],
        "pricing": locale.t["product"]["business_maturity_pricing"],
        "adoption": locale.t["product"]["business_maturity_adoption"],
        "paid": locale.t["product"]["business_maturity_paid"],
        "retained": locale.t["product"]["business_maturity_retained"],
    }
    judgment_basis_labels = {
        key: locale.t["product"][f"basis_{key}"]
        for key in ("facts_only", "reasoned", "behavioral", "commercial")
    }
    action_labels = {
        key: locale.t["product"][f"action_{key}"]
        for key in ("investigate", "try", "dissect", "watch", "clue")
    }
    req = None
    if review:
        verdict_label, evidence_signal = _public_req(review, locale)
        supported_gate = next((gate for gate in review.gates if gate.status == "supported"), None)
        if locale.key == "en":
            known_fact = _english_text(product.summary_en) or public_read.job
        elif supported_gate is not None:
            known_fact = _gate_reason_for_display(supported_gate, product, locale)
        else:
            known_fact = product.summary_zh or public_read.job
        localized_next = _scrub_pending_phrase(
            review.next_validation if locale.key != "en" else _english_text(
                review.next_validation, locale.t["product"]["req_next_pending"]
            )
        )
        req = {
            "level": locale.t["product"]["req_initial"] if review.level == "initial" else locale.t["product"]["req_full"],
            "signal": verdict_label,
            "evidence_signal": evidence_signal,
            "verdict": review.verdict,
            "verdict_label": verdict_label,
            "next_validation": localized_next,
            "reviewed_at": review.day,
            "job": public_read.job,
            "pain": public_read.pain,
            "current_alternative": public_read.current_alternative,
            "usage_reason": public_read.usage_reason,
            "demand_maturity": demand_maturity_labels[public_read.demand_maturity],
            "business_maturity": business_maturity_labels[public_read.business_maturity],
            "judgment_basis": judgment_basis_labels[public_read.judgment_basis],
            "recommended_action": action_labels[public_read.recommended_action],
            "known_fact": known_fact,
            "inference": public_read.usage_reason,
            "unknown": localized_next,
            "gates": [
                {
                    "name": gate_labels[gate.gate],
                    "status": gate_statuses[gate.status],
                    "reason": _gate_reason_for_display(gate, product, locale),
                    # Only expose evidence that survived the public URL,
                    # aggregator, language, and deduplication boundary above.
                    "evidence": [
                        public_evidence_by_id[eid]
                        for eid in gate.evidence_ids
                        if eid in public_evidence_by_id
                    ],
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
    # 同一市场每天可复查；详情只展示每个市场最新一次结论。
    market_rows = []
    for observation in sorted(latest_by_market.values(), key=lambda item: (item.ecosystem, item.market)):
        market_rows.append({
            "market": observation.market,
            "ecosystem": locale.t["product"]["ecosystem_zh"] if observation.ecosystem == "zh" else locale.t["product"]["ecosystem_en"],
            "supply": supply_labels[observation.supply_status],
            "demand": demand_labels[observation.demand_status],
            "coverage": observation.coverage if locale.key != "en" else _english_text(
                observation.coverage, locale.t["product"]["market_coverage_pending"]
            ),
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
        "research_links": [
            {
                "label": locale.t["product"][key],
                "url": f"https://www.google.com/search?q={quote_plus(query)}",
            }
            for key, query in (
                ("research_official", f'"{product.name}" official documentation'),
                ("research_pricing", f'"{product.name}" pricing plans'),
                ("research_reviews", f'"{product.name}" customer reviews complaints'),
                ("research_cases", f'"{product.name}" customer case study results'),
                ("research_alternatives", f'"{product.name}" alternatives comparison'),
            )
        ],
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
    all_products = list(store.iter_products())
    products = [p for p in all_products if _is_publishable(p)]
    market_context_products = {
        p.slug: p for p in all_products
        if p.status == STATUS_MARKET_CONTEXT
        and bool((p.summary_en if locale.key == "en" else p.summary_zh).strip())
    }
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
        # Count the form assigned to this view.  `form_key` from the previous
        # loop only describes its final item and used to put every product in
        # one bucket on the opportunity-map filter.
        view_form = view["form_key"]
        form_counts[view_form] = form_counts.get(view_form, 0) + 1

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
    ranked_proven = _proven_business_selection(proven, limit=3)
    proven_businesses = [_business_card_view(item, store, locale) for item in ranked_proven]

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

    # 首页使用“最近一个已经形成公开内容的日期”，而不是最新原始采集日期。
    # 采集通常早于编辑：若最新批次还全是半成品，直接拿它当今日会得到一个
    # 空的“首次发现”区，再由固定历史产品补位，看起来就像日期变了内容没变。
    generic_summaries = {
        "",
        "首次发现项目",
        "发现新的公开信号",
        "新增证据改变了 `/req` 判断。",
        "新增证据改变了 判断",
    }
    event_days = store.event_days()
    publishable_event_days: list[str] = []
    for candidate_day in event_days:
        if any(
            event.homepage
            and (
                (
                    event.project_slug in view_by_slug
                    and (
                        event.event_type == EVENT_FIRST_DISCOVERED
                        or (
                            event.summary.strip() not in generic_summaries
                            and _public_event_summary(event.summary) not in generic_summaries
                        )
                    )
                )
                or (
                    event.project_slug in market_context_products
                    and event.event_type == EVENT_FIRST_DISCOVERED
                )
            )
            for event in store.read_events(candidate_day)
        ):
            publishable_event_days.append(candidate_day.isoformat())
    completed_days = set(publishable_event_days) | {report.day for report in reports}
    event_day = max(completed_days, default="")
    event_rows = (
        store.read_events(date.fromisoformat(event_day))
        if event_day and event_day in publishable_event_days
        else []
    )
    daily_report = next((report for report in reports if report.day == event_day), None)
    past_reports = [report for report in reports if report.day != event_day]

    # 首页只消费这一版的事件。首次发现是主体；旧项目只能以“重要更新”出现，
    # 且卡片只陈述新事实和受影响判断。
    first_discoveries: list[dict[str, Any]] = []
    important_updates: list[dict[str, Any]] = []
    ordered_events = sorted(event_rows, key=lambda item: item.discovered_at, reverse=True)
    first_slugs: set[str] = set()
    for event in ordered_events:
        if event.event_type != EVENT_FIRST_DISCOVERED or not event.homepage or event.project_slug in first_slugs:
            continue
        view = view_by_slug.get(event.project_slug)
        if view is None:
            continue
        first_slugs.add(event.project_slug)
        first_discoveries.append(_event_view(event, view, store, locale))
    # The front page promises three evidence cases, not a second directory.
    # Everything else remains discoverable in the opportunity map the next day.
    first_discoveries = _daily_event_selection(first_discoveries, limit=3)

    # “重要更新”必须同时满足：明确允许上首页、有可陈述的新事实、同一项目
    # 当天只出现一次。首次发现优先，不能又在更新区重复出现。
    update_slugs: set[str] = set()
    for event in ordered_events:
        if (
            event.event_type == EVENT_FIRST_DISCOVERED
            or not event.homepage
            or event.project_slug in first_slugs
            or event.project_slug in update_slugs
            or event.summary.strip() in generic_summaries
            or _public_event_summary(event.summary) in generic_summaries
        ):
            continue
        view = view_by_slug.get(event.project_slug)
        if view is None:
            continue
        update_slugs.add(event.project_slug)
        important_updates.append(_event_view(event, view, store, locale))
    important_updates = important_updates[:4]

    # 当日市场摘要只从当天的事件流归纳，不用旧项目的规模或排行榜替代新变化。
    # “首次发现涉及”是观察范围，不暗示这是该行业全球第一次使用 AI。
    market_summary: list[dict[str, Any]] = []
    context_slugs: set[str] = set()
    for event in ordered_events:
        product = market_context_products.get(event.project_slug)
        if product is None or product.slug in context_slugs or not event.homepage:
            continue
        context_slugs.add(product.slug)
        context_summary = product.summary_en if locale.key == "en" else product.summary_zh
        market_summary.append({
            "kind": "context",
            "title": _public_product_name(product.name, locale),
            "text": _neutralize_public_source_names(context_summary, locale),
            "url": product.url,
        })
    industry_counts: dict[str, int] = {}
    for item in first_discoveries:
        for industry in item["industries"]:
            industry_counts[industry] = industry_counts.get(industry, 0) + 1
    if industry_counts:
        separator = "、" if locale.key != "en" else ", "
        industries_text = separator.join(
            name for name, _ in sorted(industry_counts.items(), key=lambda pair: (-pair[1], pair[0]))[:5]
        )
        market_summary.append({
            "kind": "industry",
            "title": locale.t["home"]["market_industry"],
            "text": locale.t["home"]["market_industry_text"].format(industries=industries_text),
        })
    cross_items = [item for item in first_discoveries + important_updates if item["cross_market"]]
    if cross_items:
        separator = "、" if locale.key != "en" else ", "
        names = separator.join(item["name"] for item in cross_items[:5])
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
        "daily_report": daily_report,
        "past_reports": past_reports,
        "first_discoveries": first_discoveries,
        "proven_businesses": proven_businesses,
        "important_updates": important_updates,
        "market_summary": market_summary,
        "notables": notables,
        "movers": movers,
        "categories": categories,
        "opportunity_filters": opportunity_filters,
        "form_keys": FORM_KEYS,
        "form_counts": form_counts,
        # 机会库目录页只要能判断"要不要点进去"；完整说明在详情页。
        # 全量摘要把单页 HTML 顶过解析预算，列表页用截断副本。
        "directory_products": sorted(
            ({**v, "summary": v["summary"][:160]} if v["summary"] else v for v in views),
            key=lambda v: (-v["opportunity_rank"], -v["weight"], v["name"]),
        ),
        "products": sorted(views, key=lambda v: (-v["opportunity_rank"], -v["weight"], v["name"])),
        "takeaways_by_topic": takeaways_by_topic,
        "today_takeaway": today_takeaway,
    }


def _is_publishable(product: Product) -> bool:
    """公开站的最低门槛；内部状态和半成品仍完整保留在 data/pool。"""
    return (
        product.status not in {STATUS_REJECTED, STATUS_MARKET_CONTEXT}
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
        # 中文站一律优先经编辑的中文产品说明。源给的多半是英文营销话术，
        # 读者需要看到具体工作流与交付，而不是一句抽象定位。
        summary = _scrub_pending_phrase(product.summary_zh or product.summary)
        inspiration = _scrub_pending_phrase(product.inspiration)
        written = bool(product.summary_zh)
    else:
        # 英文站：源自带的英文原句能用就用，说不清的才写 summary_en 覆盖。
        # 灵感与标签没有中文兜底；原始字段尚未翻译时不能让它阻断发布。
        summary = _scrub_pending_phrase(_english_text(product.summary_en) or _english_text(product.summary))
        inspiration = _scrub_pending_phrase(_english_text(product.inspiration_en))
        written = bool(summary)
    raw_industries = _raw_localized_tags(locale, product.industries_en, product.industries)
    raw_jobs = _raw_localized_tags(locale, product.jobs_en, product.jobs)
    raw_regions = _raw_localized_tags(locale, product.regions_en, product.regions)
    industries = _localized_tags(locale, product.industries_en, product.industries, "industry")
    jobs = _localized_tags(locale, product.jobs_en, product.jobs, "job")
    regions = _localized_tags(locale, product.regions_en, product.regions, "region")
    public_name = _public_product_name(product.name, locale)
    summary = _neutralize_public_source_names(summary, locale)
    inspiration = _neutralize_public_source_names(inspiration, locale)
    return {
        "slug": product.slug,
        "name": public_name,
        "builder": product.builder if locale.key != "en" else _english_text(product.builder),
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
        "industries": industries,
        "jobs": jobs,
        "regions": regions,
        # Search keeps the original editorial vocabulary as synonyms, while
        # filters and visible tags use the normalized public label.
        "search_terms": list(dict.fromkeys(raw_industries + raw_jobs + raw_regions + industries + jobs + regions)),
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
        "notes": product.notes if locale.key != "en" else _english_text(product.notes),
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
    asset_version: str,
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
            asset_version=asset_version,
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





def _desk_wrap_analysis_html(html_text: str) -> str:
    """Wrap analysis markdown HTML into Linear-desk cards (one card per h2).

    Analysis bodies are flat h2/p/ul/table trees. Grouping each h2 with its
    following siblings keeps content unchanged while letting CSS paint the
    intelligence-desk panels used elsewhere on the product page.
    """
    if not html_text or not html_text.strip():
        return html_text
    text = html_text.strip()
    if "<h2" not in text.lower():
        return (
            '<div class="desk-prose">'
            f'<article class="desk-prose-block desk-prose-solo">{text}</article>'
            "</div>"
        )
    parts = re.split(r"(?=<h2\b)", text, flags=re.IGNORECASE)
    chunks: list[str] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if re.match(r"<h2\b", part, flags=re.IGNORECASE):
            chunks.append(f'<article class="desk-prose-block">{part}</article>')
        else:
            chunks.append(f'<div class="desk-prose-lead">{part}</div>')
    return '<div class="desk-prose">' + "".join(chunks) + "</div>"


def _finish_inline_emphasis(html_text: str) -> str:
    """Convert leftover ``**emphasis**`` that mistune did not promote.

    Common with CJK adjacency (``三是**"词"**``): mistune leaves the markers,
    having already escaped quotes inside the text node. Safe to promote because
    the interior is already HTML-escaped.
    """
    if not html_text or "**" not in html_text:
        return html_text
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html_text)


def md_inline(value: object) -> Markup:
    """Render lightweight inline Markdown for reader-facing short fields.

    Escapes HTML first, then turns ``**emphasis**`` into ``<strong>``.
    Analysis bodies already go through mistune; takeaways / inspiration /
    judgment blurbs are plain strings that still carry author Markdown.
    """
    if value is None:
        return Markup("")
    text = str(value)
    if not text:
        return Markup("")
    escaped = str(html_escape(text))
    # Non-greedy pairs only; leave unpaired asterisks alone so we do not invent tags.
    converted = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    return Markup(converted)


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
    env.filters["md_inline"] = md_inline

    out_dir.mkdir(parents=True, exist_ok=True)
    css_src = templates_dir / "style.css"
    tokens_src = store.root / "tokens.css"
    asset_bytes = b""
    for asset in (css_src, tokens_src):
        if asset.exists():
            asset_bytes += asset.read_bytes()
    asset_version = hashlib.sha256(asset_bytes).hexdigest()[:12] if asset_bytes else "0"

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
            paths[other(locale).key], rendered, sitemap, asset_version,
        )

    expected = {
        locale.path(rel)
        for locale in LOCALES
        for rel in paths[locale.key]
    }
    stale = _remove_stale_pages(out_dir, expected)
    if stale:
        print(f"  清掉 {stale} 个不再发布的旧页面")

    if css_src.exists():
        shutil.copy2(css_src, out_dir / "style.css")
    if tokens_src.exists():
        shutil.copy2(tokens_src, out_dir / "tokens.css")

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
