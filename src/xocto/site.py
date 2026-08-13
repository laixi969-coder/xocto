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

import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import mistune
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import (
    CATEGORIES,
    STATUS_ANALYZED,
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

# 线上地址。这是部署事实不是品味，所以放代码里而不是 config/。
# 用途：canonical、sitemap、og:url —— 三处都必须是绝对地址。
BASE_URL = "https://xocto.vercel.app"

# 搜索结果里的摘要长度。中文超过这个数会被截断，不如自己控制在哪断。
DESC_LIMIT = 150

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
    # 评级的稳定键（strong / notable / unproven）。CSS 类名和排序都认它 ——
    # 认显示文字的话，英文站的徽章会因为写的是 "Strong pick" 而全部掉色。
    verdict_key: str
    verdict_rank: int
    analyzed_at: str
    body_html: str
    excerpt: str
    replaces: str = ""
    takeaway: str = ""


# 段首是引言、表格或列表符号 —— 那不是正文段落
_NOT_PROSE = re.compile(r"^(?:[>|]|[-*+]\s)")


def _section(body: str, *titles: str, limit: int = 200) -> str:
    """抽出某个二级标题下的第一段正文。找不到返回空串。

    按空行切段，不按换行切行 —— Markdown 里一段话可以折成好几行，
    原来逐行取会把"它试图把二十年积累的判断力／打包成软件卖给不懂营销的人"
    截成后半句，首页上那张卡就是一个没头没尾的残句。
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
            text = " ".join(para.split())
            if text and not _NOT_PROSE.match(text):
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
                verdict=verdict,
                verdict_key=locale.verdict_key(verdict),
                verdict_rank=locale.verdict_rank(verdict),
                analyzed_at=str(front.get("analyzed_at") or ""),
                body_html=_markdown(body),
                excerpt=excerpt,
                replaces=_section(body, *locale.heading_replaces),
                takeaway=_section(body, *locale.heading_takeaway),
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
    """把各源口径不同的指标压成人话，不带平台名。"""
    badges: list[str] = []
    for sighting in product.sightings:
        m = sighting.metrics
        if m.get("points") is not None:
            badges.append(f"{locale.metrics['points']} {m['points']}")
        if m.get("stars") is not None:
            badges.append(f"{locale.metrics['stars']} {m['stars']:,}")
        if m.get("raw_value"):
            unit = locale.metrics["mau" if m.get("metric") == "mau" else "visits"]
            badges.append(f"{unit} {m['raw_value']}")
        if m.get("mom_percent") is not None:
            sign = "+" if m["mom_percent"] >= 0 else ""
            badges.append(f"{locale.metrics['mom']} {sign}{m['mom_percent']:.0f}%")
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


def build_context(store: Store, locale: Locale) -> dict[str, Any]:
    """组装某个语种的整站数据。

    版块顺序按信息价值密度排：判断 > 数据 > 罗列。
    有判断的东西全站只有几个，但那是别处拿不到的；
    罗列谁都能做，所以往后放。
    """
    products = list(store.iter_products())
    analyses = load_analyses(store, locale)
    reports = load_reports(store, locale)
    by_slug = {a.slug: a for a in analyses}

    views = [product_view(p, locale) for p in products]
    view_by_slug = {v["slug"]: v for v in views}

    early = [v for v in views if v["stage_key"] == STAGE_EARLY]
    proven = [v for v in views if v["stage_key"] == STAGE_PROVEN]

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
        "latest_day": max((v["last_seen"] for v in views), default=""),
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
        "picks": picks,
        "notables": notables,
        "movers": movers,
        "categories": categories,
        "products": sorted(views, key=lambda v: -v["weight"]),
    }


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


def write_seo(out_dir: Path, pages: list[tuple[str, str]]) -> None:
    """robots.txt 和 sitemap.xml。

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
        "name": product.name,
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
        "seen_count": len(product.sightings),
        "notes": product.notes,
    }


def _page_paths(ctx: dict[str, Any]) -> set[str]:
    """某语种实际会输出哪些页面（不带语种前缀）。

    语言切换按钮要靠它决定跳去哪：产品页两个语种都有，但每日观察不一定 ——
    中文有 2026-08-11 而英文还没写的时候，直接跳过去就是一条死链。
    """
    paths = {"index.html", "products.html"}
    paths.update(f"p/{v['slug']}.html" for v in ctx["products"])
    paths.update(f"r/{r.day}.html" for r in ctx["reports"])
    return paths


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
        html = env.get_template(template).render(
            **ctx,
            page=page,
            root=root,
            locale=locale,
            t=locale.t,
            canonical=_canonical(locale.path(rel)),
            description=description,
            alt_locale=alt,
            alt_href=f"{root}{alt.prefix}{alt_rel}",
            alt_canonical=_canonical(alt.path(alt_rel)) if alt_exact else "",
            **extra,
        )
        (base / rel).write_text(html, encoding="utf-8")
        rendered.append(html)

    stats = ctx["stats"]
    write("index.html", "index.html", "home", locale.site_desc)
    sitemap.append((locale.path("index.html"), ctx["latest_day"]))

    write(
        "products.html", "products.html", "products",
        locale.t["products"]["desc"].format(total=stats["total"]),
    )
    sitemap.append((locale.path("products.html"), ctx["latest_day"]))

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
        )
        sitemap.append((locale.path(rel), view["last_seen"]))

    for report in ctx["reports"]:
        rel = f"r/{report.day}.html"
        # 当天那句钩子就是最好的搜索摘要
        write(rel, "report.html", "reports", _describe(report.hook, locale.site_desc),
              report=report)
        sitemap.append((locale.path(rel), report.day))

    return 2 + len(ctx["products"]) + len(ctx["reports"])


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

    write_seo(out_dir, sitemap)
    print(f"  robots.txt + sitemap.xml（{len(sitemap)} 个 URL）")

    from .fonts import build_fonts

    print(f"  字体：{build_fonts(templates_dir, out_dir, rendered)}")
    print(f"  生成 {pages} 个页面 → {out_dir}")
    return out_dir
