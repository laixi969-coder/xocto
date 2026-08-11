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
    STATUS_ANALYZED,
    STATUS_PENDING_FILTER,
    STATUS_QUEUED,
    STATUS_WATCHING,
    Product,
)
from .store import Store

SOURCE_LABELS = {
    "producthunt": "Product Hunt",
    "hackernews": "Hacker News",
    "github": "GitHub",
    "aicpb": "AICPB 榜单",
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
    """一份深度分析。"""

    slug: str
    name: str
    verdict: str
    analyzed_at: str
    body_html: str
    excerpt: str

    @property
    def verdict_rank(self) -> int:
        return VERDICT_ORDER.get(self.verdict, 9)


@dataclass(frozen=True)
class Report:
    """一份每日观察。"""

    day: str
    body_html: str


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
        out.append(Report(day=path.stem, body_html=_markdown(text)))
    return out


def _metric_badges(product: Product) -> list[str]:
    """把各源口径不同的指标压成人能读的短标签。"""
    badges: list[str] = []
    for sighting in product.sightings:
        m = sighting.metrics
        if m.get("points") is not None:
            badges.append(f"HN {m['points']} 分")
        if m.get("stars") is not None:
            badges.append(f"{m['stars']:,} ★")
        if m.get("raw_value"):
            unit = "月活" if m.get("metric") == "mau" else "访问"
            badges.append(f"{unit} {m['raw_value']}")
        if m.get("mom_percent") is not None:
            sign = "+" if m["mom_percent"] >= 0 else ""
            badges.append(f"环比 {sign}{m['mom_percent']:.0f}%")
    return badges


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
    products = list(store.iter_products())
    analyses = load_analyses(store)
    reports = load_reports(store)
    analysed_slugs = {a.slug for a in analyses}

    for product in products:
        product_view(product)  # 提前校验，坏数据早暴露

    early = [p for p in products if "aicpb" not in p.sources]
    ranked = [p for p in products if "aicpb" in p.sources]

    # 增长异常的放前面，那才是信号
    movers = sorted(
        (p for p in ranked if _growth_rate(p) is not None),
        key=lambda p: -(_growth_rate(p) or 0),
    )[:12]

    latest_day = max((p.last_seen[:10] for p in products), default="")
    fresh = [p for p in early if p.first_seen[:10] == latest_day]

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "latest_day": latest_day,
        "stats": {
            "total": len(products),
            "early": len(early),
            "ranked": len(ranked),
            "analysed": len(analyses),
            "sources": len({s for p in products for s in p.sources}),
        },
        "analyses": analyses,
        "reports": reports,
        "movers": [product_view(p) for p in movers],
        "fresh": [product_view(p) for p in sorted(early, key=_weight, reverse=True)[:12]],
        "products": [
            product_view(p)
            for p in sorted(products, key=_weight, reverse=True)
        ],
        "analysed_slugs": analysed_slugs,
    }


def product_view(product: Product) -> dict[str, Any]:
    """把 Product 摊平成模板好用的字典。"""
    return {
        "slug": product.slug,
        "name": product.name,
        "builder": product.builder,
        "summary": product.summary,
        "url": product.url,
        "status": product.status,
        "status_label": STATUS_LABELS.get(product.status, product.status),
        "sources": [SOURCE_LABELS.get(s, s) for s in product.sources],
        "source_keys": list(product.sources),
        "badges": _metric_badges(product),
        "scale": _scale_badge(product),
        "first_seen": product.first_seen[:10],
        "last_seen": product.last_seen[:10],
        "growth": _growth_rate(product),
        "sightings": [
            {
                "source": SOURCE_LABELS.get(s.source, s.source),
                "url": s.url,
                "seen_at": s.seen_at[:10],
                "metrics": s.metrics,
            }
            for s in product.sightings
        ],
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

    # root 是页面到站点根的相对路径。顶层页面为空，子目录页面要回退一级 ——
    # 这样整站可以直接双击打开，不需要起服务器。
    (out_dir / "index.html").write_text(
        env.get_template("index.html").render(**ctx, page="home", root=""), encoding="utf-8"
    )
    pages += 1

    (out_dir / "products.html").write_text(
        env.get_template("products.html").render(**ctx, page="products", root=""),
        encoding="utf-8",
    )
    pages += 1

    detail = env.get_template("product.html")
    by_slug = {a.slug: a for a in ctx["analyses"]}
    for view in ctx["products"]:
        html = detail.render(
            **ctx, page="products", root="../", product=view, analysis=by_slug.get(view["slug"])
        )
        (out_dir / "p" / f"{view['slug']}.html").write_text(html, encoding="utf-8")
        pages += 1

    report_tpl = env.get_template("report.html")
    for report in ctx["reports"]:
        html = report_tpl.render(**ctx, page="reports", root="../", report=report)
        (out_dir / "r" / f"{report.day}.html").write_text(html, encoding="utf-8")
        pages += 1

    css_src = templates_dir / "style.css"
    if css_src.exists():
        shutil.copy2(css_src, out_dir / "style.css")

    print(f"  生成 {pages} 个页面 → {out_dir}")
    return out_dir
