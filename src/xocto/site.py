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
"""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import mistune
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import (
    CATEGORIES,
    STATUS_ANALYZED,
    STATUS_PENDING_FILTER,
    STATUS_QUEUED,
    STATUS_WATCHING,
    Product,
)
from .dedupe import is_aggregator, url_host
from .report import ReportDoc, parse_report, split_stat
from .store import Store

# 网站上不出现任何数据源名称。用户不关心东西从哪抓来的，
# 那是实现细节 —— 泄漏到界面上既没用，也把采集策略白送出去了。
# 只暴露对用户有意义的两件事：成熟度（阶段）和方向（赛道）。
STAGE_EARLY = "刚冒头"
STAGE_PROVEN = "已验证"

# 各源指标口径不同，统一成人话，且不透露来自哪个平台
METRIC_LABELS = {
    "points": "社区热度",
    "stars": "开源关注",
    "comments": "讨论量",
}

STATUS_LABELS = {
    STATUS_ANALYZED: "已分析",
    STATUS_WATCHING: "观察中",
    STATUS_QUEUED: "待分析",
    STATUS_PENDING_FILTER: "新收录",
    "rejected": "已淘汰",
}

VERDICT_ORDER = {"强烈推荐": 0, "值得关注": 1, "有待观察": 2}

_markdown = mistune.create_markdown(plugins=["table", "strikethrough"])


@dataclass(frozen=True)
class Analysis:
    """一份深度分析。

    replaces 和 takeaway 单独抽出来 —— 那是整份分析里最值钱的两段：
    "它替代了什么旧行为"是判断真伪的依据，"可迁移点"是读者真正要拿走的东西。
    埋在正文里等于没有。
    """

    slug: str
    name: str
    verdict: str
    analyzed_at: str
    body_html: str
    excerpt: str
    replaces: str = ""
    takeaway: str = ""

    @property
    def verdict_rank(self) -> int:
        return VERDICT_ORDER.get(self.verdict, 9)


def _section(body: str, *titles: str, limit: int = 200) -> str:
    """抽出某个二级标题下的第一段正文。找不到返回空串。"""
    for title in titles:
        match = re.search(
            rf"^##\s*{re.escape(title)}[^\n]*\n+(.+?)(?=\n#{{1,2}}\s|\Z)",
            body,
            re.S | re.M,
        )
        if not match:
            continue
        for line in match.group(1).split("\n"):
            text = line.strip()
            # 跳过引言块和空行，取第一段实际内容
            if text and not text.startswith((">", "|", "-", "*")):
                return _strip_md(text, limit)
    return ""


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
    hook: str = ""
    highlights: tuple[str, ...] = ()
    stats: tuple[tuple[str, str], ...] = ()

    @property
    def label(self) -> str:
        """报头上的人话日期：2026 年 8 月 11 日 · 星期二。"""
        try:
            d = date.fromisoformat(self.day)
        except ValueError:
            return self.day
        return f"{d.year} 年 {d.month} 月 {d.day} 日 · 星期{'一二三四五六日'[d.weekday()]}"


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
    """把一段 Markdown 压成纯文本摘要。"""
    flat = re.sub(r"[#>*_`\[\]()|-]", " ", text)
    flat = " ".join(flat.split())
    return flat[:limit] + ("…" if len(flat) > limit else "")


def load_analyses(store: Store) -> list[Analysis]:
    out: list[Analysis] = []
    for path in sorted(store.analysis_dir.glob("*.md")):
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
        excerpt = ""
        match = re.search(r"##\s*一句话定位\s*\n+(.+?)\n", body)
        if match:
            excerpt = _strip_md(match.group(1))
        if not excerpt:
            excerpt = _strip_md(body)

        out.append(
            Analysis(
                slug=slug,
                name=front.get("name") or slug,
                verdict=front.get("verdict") or "",
                analyzed_at=str(front.get("analyzed_at") or ""),
                body_html=_markdown(body),
                excerpt=excerpt,
                replaces=_section(body, "它在替代什么旧行为", "它在替代什么"),
                takeaway=_section(body, "对你的可迁移点", "对我的可迁移点"),
            )
        )
    return sorted(out, key=lambda a: (a.verdict_rank, a.name))


def load_reports(store: Store) -> list[Report]:
    out: list[Report] = []
    for path in sorted(store.reports_dir.glob("*.md"), reverse=True):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue

        front, body = _split_frontmatter(text)
        highlights = tuple(str(h) for h in (front.get("highlights") or []))
        out.append(
            Report(
                day=str(front.get("day") or path.stem),
                doc=parse_report(body),
                hook=str(front.get("hook") or ""),
                highlights=highlights,
                # 每条 highlight 开头那个数字单独抽出来 —— 数字放大才是数字
                stats=tuple(split_stat(h) for h in highlights),
            )
        )
    return out


def _metric_badges(product: Product) -> list[str]:
    """把各源口径不同的指标压成人话，不带平台名。"""
    badges: list[str] = []
    for sighting in product.sightings:
        m = sighting.metrics
        if m.get("points") is not None:
            badges.append(f"社区热度 {m['points']}")
        if m.get("stars") is not None:
            badges.append(f"开源关注 {m['stars']:,}")
        if m.get("raw_value"):
            unit = "月活" if m.get("metric") == "mau" else "月访问"
            badges.append(f"{unit} {m['raw_value']}")
        if m.get("mom_percent") is not None:
            sign = "+" if m["mom_percent"] >= 0 else ""
            badges.append(f"环比 {sign}{m['mom_percent']:.0f}%")
    return badges


def _external_url(product: Product) -> str:
    """对外展示的链接。

    只在它是产品自己的域名时才给 —— 指向聚合站页面的链接既暴露了采集来源，
    对用户也没价值（那不是产品官网）。
    """
    if not product.url or is_aggregator(url_host(product.url)):
        return ""
    return product.url


def _stage(product: Product) -> str:
    """成熟度。有真实流量数据的算已验证，其余都是刚冒头。"""
    for sighting in product.sightings:
        if sighting.metrics.get("raw_value"):
            return STAGE_PROVEN
    return STAGE_EARLY


def _boards(product: Product) -> list[str]:
    """产品上过的细分榜，去重保序。这是它的品类地位证明。"""
    seen: list[str] = []
    for sighting in product.sightings:
        for board in sighting.metrics.get("boards") or []:
            if board not in seen:
                seen.append(board)
    return seen


def _scale_badge(product: Product) -> str:
    """规模标签（访问量 / 月活）。只有榜单源才有。"""
    for sighting in product.sightings:
        m = sighting.metrics
        if m.get("raw_value"):
            unit = "月活" if m.get("metric") == "mau" else "访问"
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


def build_context(store: Store) -> dict[str, Any]:
    """组装整站数据。

    版块顺序按信息价值密度排：判断 > 数据 > 罗列。
    有判断的东西全站只有几个，但那是别处拿不到的；
    罗列谁都能做，所以往后放。
    """
    products = list(store.iter_products())
    analyses = load_analyses(store)
    reports = load_reports(store)
    by_slug = {a.slug: a for a in analyses}

    views = [product_view(p) for p in products]
    view_by_slug = {v["slug"]: v for v in views}

    early = [v for v in views if v["stage"] == STAGE_EARLY]
    proven = [v for v in views if v["stage"] == STAGE_PROVEN]

    # 1. 今日判断：有深度分析的，按推荐度排
    picks = [
        {**view_by_slug.get(a.slug, {"slug": a.slug, "name": a.name}), "analysis": a}
        for a in analyses
        if a.slug in view_by_slug
    ]

    # 2. 值得留意：进了观察名单但还没展开分析的
    notables = sorted(
        (v for v in views if v["status"] == STATUS_WATCHING and v["summary"]),
        key=lambda v: -v["weight"],
    )

    # 覆盖率：没中文说明、没灵感的产品对读者是废卡片，得看得见还差多少
    missing_zh = [v for v in views if not v["is_zh"]]
    missing_insp = [v for v in views if not v["inspiration"]]

    # 3. 增长信号：环比异常的，那才是信号，不是排名
    movers = sorted(
        (v for v in proven if v["growth"] is not None),
        key=lambda v: -(v["growth"] or 0),
    )[:10]

    # 4. 赛道分布：给一个进入方式，不在首页罗列产品
    counts: dict[str, int] = {}
    for view in views:
        key = view["category"] or "未归类"
        counts[key] = counts.get(key, 0) + 1
    categories = [
        {"name": name, "count": counts[name]}
        for name in CATEGORIES
        if counts.get(name)
    ]

    # 读完一份分析之后没有下一步，旅程就断在那里了。
    # 给每个产品算好"同方向的邻居"和"上一个/下一个"，详情页才不是死路。
    ranked = sorted(views, key=lambda v: -v["weight"])
    for i, view in enumerate(ranked):
        view["prev"] = ranked[i - 1] if i > 0 else None
        view["next"] = ranked[i + 1] if i < len(ranked) - 1 else None
        same = [
            o
            for o in ranked
            if o["category"] == view["category"] and o["slug"] != view["slug"]
        ]
        # 同方向里优先推有判断的，其次是热度高的
        same.sort(key=lambda o: (o["status"] != STATUS_ANALYZED, -o["weight"]))
        view["siblings"] = same[:4]
        view["category_total"] = counts.get(view["category"], 0)

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "latest_day": max((v["last_seen"] for v in views), default=""),
        "stats": {
            "total": len(views),
            "early": len(early),
            "proven": len(proven),
            "analysed": len(analyses),
            "watching": len(notables),
            "missing_zh": len(missing_zh),
            "missing_inspiration": len(missing_insp),
        },
        "analyses": analyses,
        "analysis_by_slug": by_slug,
        "reports": reports,
        "picks": picks,
        "notables": notables,
        "movers": movers,
        "categories": categories,
        "products": sorted(views, key=lambda v: -v["weight"]),
    }


def product_view(product: Product) -> dict[str, Any]:
    """把 Product 摊平成模板好用的字典。

    注意这里刻意不导出任何来源信息 —— 模板拿不到，就不可能不小心渲染出去。
    """
    stage = _stage(product)
    return {
        "slug": product.slug,
        "name": product.name,
        "builder": product.builder,
        # 展示一律优先中文。源给的多半是英文营销话术，
        # 摆在列表里读者一行扫过去等于没看见。
        "summary": product.summary_zh or product.summary,
        "summary_raw": product.summary,
        "is_zh": bool(product.summary_zh),
        "inspiration": product.inspiration,
        "url": _external_url(product),
        "status": product.status,
        "status_label": STATUS_LABELS.get(product.status, product.status),
        "category": product.category,
        "stage": stage,
        "stage_key": "proven" if stage == STAGE_PROVEN else "early",
        "badges": _metric_badges(product),
        "scale": _scale_badge(product),
        "boards": _boards(product),
        "first_seen": product.first_seen[:10],
        "last_seen": product.last_seen[:10],
        "growth": _growth_rate(product),
        "weight": _weight(product),
        "seen_count": len(product.sightings),
        "notes": product.notes,
    }


def build(store: Store, out_dir: Path | None = None) -> Path:
    """生成整站，返回输出目录。"""
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

    ctx = build_context(store)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "p").mkdir(exist_ok=True)
    (out_dir / "r").mkdir(exist_ok=True)

    pages = 0
    rendered: list[str] = []  # 留给字体子集化抓标题字符

    # root 是页面到站点根的相对路径。顶层页面为空，子目录页面要回退一级 ——
    # 这样整站可以直接双击打开，不需要起服务器。
    html = env.get_template("index.html").render(**ctx, page="home", root="")
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    rendered.append(html)
    pages += 1

    html = env.get_template("products.html").render(**ctx, page="products", root="")
    (out_dir / "products.html").write_text(html, encoding="utf-8")
    rendered.append(html)
    pages += 1

    detail = env.get_template("product.html")
    by_slug = ctx["analysis_by_slug"]
    for view in ctx["products"]:
        html = detail.render(
            **ctx, page="products", root="../", product=view, analysis=by_slug.get(view["slug"])
        )
        (out_dir / "p" / f"{view['slug']}.html").write_text(html, encoding="utf-8")
        rendered.append(html)
        pages += 1

    report_tpl = env.get_template("report.html")
    for report in ctx["reports"]:
        html = report_tpl.render(**ctx, page="reports", root="../", report=report)
        (out_dir / "r" / f"{report.day}.html").write_text(html, encoding="utf-8")
        rendered.append(html)
        pages += 1

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

    from .fonts import build_fonts

    print(f"  字体：{build_fonts(templates_dir, out_dir, rendered)}")
    print(f"  生成 {pages} 个页面 → {out_dir}")
    return out_dir
