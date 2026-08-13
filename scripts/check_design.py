#!/usr/bin/env python3
"""设计约束的复算脚本 —— DESIGN.md 里那些数字的唯一真相。

存在的理由：2026-08-11 换配色时，DESIGN.md 写着 ink-faint "通过 WCAG AA"，
实测只有 3.72:1。文档里的承诺没人复算，回归就这么溜进去了。
凡是写成数字的约束，都得有一条命令能验。

复算七件事：

  1. token 对比度  —— 所有承担文字的颜色在 paper / surface 上 ≥4.5:1
  2. 来源泄漏      —— 站点里不许出现任何采集源名称（含 sitemap/robots）
  3. 中文漏进英文站 —— site/en/ 里除了产品名不许有中文
  4. 私人指涉泄漏  —— 站点里不许出现只有作者本人看得懂的自有项目名和身世指代
  5. 站内死链      —— 相对链接都要指向真实存在的文件
  6. sitemap 自洽  —— 每个 URL 都存在，页面数对得上，robots 指向它
  7. 发布门槛      —— rejected 和缺中文说明/灵感的半成品没有残留页面

只读，不改任何东西。有问题返回退出码 1，能挂在 CI 上。
"""

from __future__ import annotations

import html as html_lib
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "templates" / "style.css"
SITE = ROOT / "site"
POOL = ROOT / "data" / "pool"

# 正文对比度门槛（WCAG 2.1 SC 1.4.3 AA）。大字（≥24px 或 ≥18.66px 粗体）是 3:1，
# 但这些 token 大多用在小字上，一律按 4.5 要求，省得逐处判断字号。
MIN_RATIO = 4.5

# 网站上不许出现的采集源名称（见 CLAUDE.md）
FORBIDDEN = ("Product Hunt", "Hacker News", "AICPB", "producthunt", "hackernews", "aicpb")

# 只有作者本人看得懂的指代。
# 这一条防的是 2026-08-13 发现的事故：分析模板第五部分原本写着"这一栏是给蔡蔡写的"，
# 而 i18n 又把这一栏抽成首页的「能拿走什么」—— 于是十份分析里的
# "你的 songo""直接撞你的 octo""你二十年积累的判断力"全部登上了首页最显眼的位置。
# 读者不知道 songo 是什么，也不认识作者。
# data/ 里没有私人角落：写进去什么，站上就出什么。
PRIVATE_REFS = ("songo", "octo", "蔡蔡", "你二十年", "你的短剧业务")


def _luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    channels = [int(h[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(fg: str, bg: str) -> float:
    a, b = _luminance(fg), _luminance(bg)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def _resolve(tokens: dict[str, str], name: str, depth: int = 0) -> str | None:
    """把 --x: var(--y) 一路解到具体的 hex。解不出（比如 rgba）返回 None。"""
    value = tokens.get(name)
    if value is None or depth > 6:
        return None
    value = value.strip()
    if value.startswith("#"):
        return value
    match = re.fullmatch(r"var\(\s*(--[\w-]+)\s*\)", value)
    if match:
        return _resolve(tokens, match.group(1), depth + 1)
    return None


def _tokens_in(block: str) -> dict[str, str]:
    return dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", block))


def check_contrast() -> list[str]:
    """浅色和暗色各自的 token 表，逐个对 paper / surface 复算。"""
    css = CSS.read_text(encoding="utf-8")
    fails: list[str] = []

    root = re.search(r":root\s*\{(.*?)\n\}", css, re.S)
    dark = re.search(r':root\[data-theme="dark"\]\s*\{(.*?)\n\}', css, re.S)
    if not root or not dark:
        return [":root 或 [data-theme=dark] 块解析不出来，检查 style.css 结构"]

    light_tokens = _tokens_in(root.group(1))
    dark_tokens = {**light_tokens, **_tokens_in(dark.group(1))}

    # 承担文字的 token。accent / line 之类不是文字色，不在这里管。
    text_tokens = ("ink", "ink-soft", "ink-faint", "signal", "good", "watch")

    for theme, tokens in (("浅色", light_tokens), ("暗色", dark_tokens)):
        for surface_name in ("paper", "surface"):
            bg = _resolve(tokens, f"--{surface_name}")
            if not bg:
                continue
            for token in text_tokens:
                fg = _resolve(tokens, f"--{token}")
                if not fg:
                    continue
                ratio = contrast(fg, bg)
                if ratio < MIN_RATIO:
                    fails.append(
                        f"{theme} --{token} ({fg}) 在 --{surface_name} ({bg}) 上 "
                        f"{ratio:.2f}:1，低于 {MIN_RATIO}"
                    )
    return fails


def check_leaks() -> list[str]:
    if not SITE.is_dir():
        return ["site/ 不存在，先跑 uv run xocto build"]
    hits = []
    # 不只扫 HTML：sitemap.xml 和 robots.txt 也是对外可见的文件
    for pattern in ("*.html", "*.xml", "*.txt"):
        for path in SITE.rglob(pattern):
            text = path.read_text(encoding="utf-8", errors="ignore")
            for name in FORBIDDEN:
                if name in text:
                    hits.append(f"{path.relative_to(SITE)} 里出现了采集源名称 “{name}”")
    return hits


# 中日韩文字。英文站里出现这些就是没翻译，除非它是产品自己的名字。
CJK = re.compile(r"[　-〿㐀-䶿一-鿿＀-￯가-힯]+")

# 语言切换按钮上写的就是「中文」，那是故意的
_LANG_BTN = re.compile(r'<a class="lang-btn".*?</a>', re.S)
_SCRIPT = re.compile(r"<script.*?</script>", re.S)
_TAG = re.compile(r"<[^>]+>")


# frontmatter 里 name 的取值，可能跨行（有的产品名自带换行）
_NAME_BLOCK = re.compile(r"^name:(.*?)(?=^\w+:)", re.S | re.M)


def _allowed_cjk() -> set[str]:
    """产品名里合法的中文片段。

    豆包、纳米AI、腾讯元宝这些是专有名词，在英文页面上也该是中文 ——
    翻译产品名等于伪造它。

    比的是"中文片段"而不是整个名字：名字在 YAML 里可能被引号包着、
    可能带 &amp; 这种实体、可能跨行，整串比对怎么都对不齐；
    而引号和实体都是 ASCII，永远不会落进中文片段里。
    """
    runs: set[str] = set()
    for path in sorted(POOL.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        match = _NAME_BLOCK.search(text)
        if match:
            runs.update(CJK.findall(" ".join(match.group(1).split())))
    return runs


def check_en_chinese() -> list[str]:
    """英文站里的漏译。

    这条检查存在的理由和另外两条一样：新采到的产品没写 inspiration_en、
    新写的分析忘了出英文版、新出现的细分榜没登记译名，页面会安静地
    混进一段中文，没有任何人会报错。得有一条命令抓得住。
    """
    en_dir = SITE / "en"
    if not en_dir.is_dir():
        return ["site/en/ 不存在，先跑 uv run xocto build"]

    allowed = _allowed_cjk()
    problems: list[str] = []
    for path in sorted(en_dir.rglob("*.html")):
        raw = path.read_text(encoding="utf-8", errors="ignore")
        raw = _LANG_BTN.sub(" ", raw)
        raw = _SCRIPT.sub(" ", raw)
        text = html_lib.unescape(_TAG.sub(" ", raw))
        hits = {run for run in CJK.findall(text) if run.strip() and run not in allowed}
        if hits:
            sample = " / ".join(sorted(hits)[:3])
            problems.append(f"en/{path.relative_to(en_dir)} 里有没译的中文：{sample}")
    return problems[:20]


def check_private_refs() -> list[str]:
    """站点里不许出现只有作者本人看得懂的指代。

    只扫渲染出来的 HTML —— 判断依据是"读者看不看得到"，不是"文件里有没有"。
    """
    problems: list[str] = []
    for path in sorted(SITE.rglob("*.html")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        visible = html_lib.unescape(re.sub(r"<[^>]+>", " ", text))
        for ref in PRIVATE_REFS:
            if re.search(rf"(?<![a-zA-Z0-9-]){re.escape(ref)}(?![a-zA-Z0-9-])", visible, re.I):
                rel = path.relative_to(ROOT)
                problems.append(f"{rel} 出现「{ref}」—— 读者不知道这是什么")
    return problems


def check_links() -> list[str]:
    if not SITE.is_dir():
        return []
    bad = set()
    pages = list(SITE.rglob("*.html"))
    for page in pages:
        html = page.read_text(encoding="utf-8", errors="ignore")
        for href in re.findall(r'(?:href|src)="([^"]+)"', html):
            if href.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = urllib.parse.unquote(href.split("#")[0].split("?")[0])
            if not target:
                continue
            if not (page.parent / target).resolve().exists():
                bad.add(f"{page.relative_to(SITE)} → {href}")
    return sorted(bad)[:20]


def check_sitemap() -> list[str]:
    """sitemap 里的每个 URL 都要真的存在，且页面数要对得上。

    sitemap 指向 404 会被搜索引擎降权，而这种错不会有任何人报错 ——
    必须靠复算发现。
    """
    sitemap = SITE / "sitemap.xml"
    robots = SITE / "robots.txt"
    problems: list[str] = []

    if not sitemap.exists():
        return ["缺 site/sitemap.xml —— 想被收录就得有"]
    if not robots.exists():
        return ["缺 site/robots.txt"]

    xml = sitemap.read_text(encoding="utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", xml)
    if not locs:
        return ["sitemap.xml 里没有任何 <loc>"]

    for loc in locs:
        rel = loc.split("//", 1)[-1].split("/", 1)[-1] or "index.html"
        target = SITE / (rel if rel != "" else "index.html")
        if not target.exists():
            problems.append(f"sitemap 指向不存在的页面：{loc}")

    # 搜索平台的所有权验证文件必须留在根目录，但它不是读者页面，
    # 也不应该被放入 sitemap。当作页面计数会把这条检查变成误报。
    pages = len([
        path for path in SITE.rglob("*.html")
        if not path.read_text(encoding="utf-8", errors="ignore").startswith("google-site-verification:")
    ])
    if len(locs) != pages:
        problems.append(f"sitemap 有 {len(locs)} 个 URL，站点有 {pages} 个页面，对不上")

    if "Sitemap:" not in robots.read_text(encoding="utf-8"):
        problems.append("robots.txt 里没有指向 sitemap")

    return problems


def check_publishability() -> list[str]:
    """内部工作队列不能直接等同于公开站点。"""
    problems: list[str] = []
    for path in sorted(POOL.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        front = text.split("---", 2)[1] if text.startswith("---") else ""
        slug_match = re.search(r"^slug:\s*(.+?)\s*$", front, re.M)
        if not slug_match:
            continue
        slug = slug_match.group(1).strip("'\"")
        rejected = bool(re.search(r"^status:\s*rejected\s*$", front, re.M))
        missing_summary = bool(re.search(r"^summary_zh:\s*''\s*$", front, re.M))
        missing_inspiration = bool(re.search(r"^inspiration:\s*''\s*$", front, re.M))
        if not (rejected or missing_summary or missing_inspiration):
            continue
        for published in (SITE / "p" / f"{slug}.html", SITE / "en" / "p" / f"{slug}.html"):
            if published.exists():
                reason = "已淘汰" if rejected else "内容未补齐"
                problems.append(f"{published.relative_to(SITE)} 仍在发布（{reason}）")
    return problems


def main() -> int:
    groups = (
        ("token 对比度", check_contrast()),
        ("来源泄漏", check_leaks()),
        ("中文漏进英文站", check_en_chinese()),
        ("私人指涉泄漏", check_private_refs()),
        ("站内死链", check_links()),
        ("sitemap 自洽", check_sitemap()),
        ("发布门槛", check_publishability()),
    )
    failed = False
    for name, problems in groups:
        if problems:
            failed = True
            print(f"✗ {name}（{len(problems)} 项）")
            for p in problems:
                print(f"    {p}")
        else:
            print(f"✓ {name}")

    if failed:
        print("\n有不达标项。改代码，或者改 DESIGN.md 里对应的承诺 —— 别两边都不动。")
        return 1
    print("\n全部通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
