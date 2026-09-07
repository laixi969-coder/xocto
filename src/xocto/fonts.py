"""自托管字体：构建时把字体拷进站点，并按实际用到的字符子集化中文字体。

为什么自托管：Google Fonts 的 CJK 字体拆成 100+ 个子集，加载慢且在部分
网络环境下整体失败，中文字体会无声地掉回系统字体。拉丁字体文件很小直接
全量拷贝；思源黑体单字重源文件 16–26MB，必须按字符集子集化——站点是静态
的，全站字符集在构建时就能确定。

中文子集必须覆盖全站文本而不只是标题：@font-face 一旦声明，正文也会匹配
到这个家族；子集里没有的字会掉回系统字体，一段话粗细混排（2026-09-07 修）。
因此 400/700 两个字重都按全站文本字符子集化，font-family 里中文统一走思源。

fonttools 不在环境里时降级为只拷贝拉丁字体，中文用系统字体，构建不中断。
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

LATIN_FONTS = (
    "inter-400-latin.woff2",
    "inter-500-latin.woff2",
    "inter-600-latin.woff2",
)
# (源文件, 输出文件, font-weight)。新增字重时 CSS 里的 @font-face 要成对加。
CJK_SOURCES = (
    ("NotoSansCJKsc-Regular.otf", "noto-sans-sc-400-subset.woff2", 400),
    ("NotoSansCJKsc-Bold.otf", "noto-sans-sc-700-subset.woff2", 700),
)

_SCRIPT_STYLE_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.IGNORECASE | re.DOTALL)
_TAG_RE = re.compile(r"<[^>]+>")

# 正文里可能出现的混排字符：ASCII 可打印字符 + 常用中文标点与符号
_BASE_CHARS = "".join(chr(c) for c in range(0x20, 0x7F)) + (
    "「」·，。：；？！—…“”‘’《》（）、【】￥％℃→←↑↓±×÷①②③④⑤"
)


def collect_text_chars(html_pages: list[str]) -> set[str]:
    """从渲染好的页面里抓全部可见文本字符（中文子集要覆盖正文，不只是标题）。"""
    chars = set(_BASE_CHARS)
    for html in html_pages:
        body = _SCRIPT_STYLE_RE.sub("", html)
        chars.update(_TAG_RE.sub("", body))
    return chars


def build_fonts(templates_dir: Path, out_dir: Path, html_pages: list[str]) -> str:
    """把字体产物写进 out_dir/fonts/，返回给人看的一行状态。"""
    src_dir = templates_dir / "fonts"
    dst_dir = out_dir / "fonts"
    if not src_dir.exists():
        return "无字体目录，跳过"
    dst_dir.mkdir(parents=True, exist_ok=True)

    # 清掉过时产物（比如换字体后留下的旧子集），避免整站带着没用的文件
    keep = set(LATIN_FONTS) | {out for _, out, _ in CJK_SOURCES}
    for old in dst_dir.glob("*.woff2"):
        if old.name not in keep:
            old.unlink()

    copied = 0
    for name in LATIN_FONTS:
        src = src_dir / name
        if src.exists():
            shutil.copy2(src, dst_dir / name)
            copied += 1

    try:
        from fontTools import subset
    except ImportError:
        return f"拷贝 {copied} 个拉丁字体；缺 fonttools，中文用系统字体"

    chars = collect_text_chars(html_pages)
    text = "".join(sorted(chars))
    parts: list[str] = []
    for source, out_name, _weight in CJK_SOURCES:
        cjk_src = src_dir / source
        if not cjk_src.exists():
            parts.append(f"缺 {source}（该字重用系统字体）")
            continue
        subset.main(
            [
                str(cjk_src),
                f"--text={text}",
                "--flavor=woff2",
                "--output-file=" + str(dst_dir / out_name),
                "--layout-features=*",
                "--no-hinting",
                "--desubroutinize",
            ]
        )
        size_kb = (dst_dir / out_name).stat().st_size // 1024
        parts.append(f"{out_name} {size_kb}KB")
    return f"拷贝 {copied} 个拉丁字体 + 思源黑体子集（{len(chars)} 字符）：{'，'.join(parts)}"
