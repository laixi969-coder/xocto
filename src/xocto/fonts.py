"""自托管字体：构建时把字体拷进站点，并按实际用到的标题字符子集化中文字体。

为什么自托管：Google Fonts 的 CJK 字体拆成 100+ 个子集，加载慢且在部分
网络环境下整体失败，标题字体会无声地掉回系统字体。拉丁字体文件很小直接
全量拷贝；思源黑体 Bold 源文件 26MB，必须按字符集子集化——站点是静态
的，标题字符集在构建时就能确定。

fonttools 不在环境里时降级为只拷贝拉丁字体，中文标题用系统字体，
构建不中断。
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

LATIN_FONTS = (
    "inter-400-latin.woff2",
    "inter-500-latin.woff2",
    "inter-600-latin.woff2",
    "fraunces-400-latin.woff2",
    "fraunces-700-latin.woff2",
)
CJK_SOURCE = "NotoSansCJKsc-Bold.otf"
CJK_OUT = "noto-sans-sc-700-subset.woff2"

_HEADING_RE = re.compile(r"<h[12][^>]*>(.*?)</h[12]>", re.IGNORECASE | re.DOTALL)
_TAG_RE = re.compile(r"<[^>]+>")

# 标题里可能出现的混排字符：ASCII 可打印字符 + 常用中文标点
_BASE_CHARS = "".join(chr(c) for c in range(0x20, 0x7F)) + (
    "「」·，。：；？！—…“”‘’《》（）、【】￥％℃→←↑↓±×÷①②③④⑤"
)


def collect_heading_chars(html_pages: list[str]) -> set[str]:
    """从渲染好的页面里抓 h1/h2 的纯文本字符（标题字体只用在 h1/h2 上）。"""
    chars = set(_BASE_CHARS)
    for html in html_pages:
        for m in _HEADING_RE.finditer(html):
            chars.update(_TAG_RE.sub("", m.group(1)))
    return chars


def build_fonts(templates_dir: Path, out_dir: Path, html_pages: list[str]) -> str:
    """把字体产物写进 out_dir/fonts/，返回给人看的一行状态。"""
    src_dir = templates_dir / "fonts"
    dst_dir = out_dir / "fonts"
    if not src_dir.exists():
        return "无字体目录，跳过"
    dst_dir.mkdir(parents=True, exist_ok=True)

    # 清掉过时产物（比如换字体后留下的旧子集），避免整站带着没用的文件
    keep = set(LATIN_FONTS) | {CJK_OUT}
    for old in dst_dir.glob("*.woff2"):
        if old.name not in keep:
            old.unlink()

    copied = 0
    for name in LATIN_FONTS:
        src = src_dir / name
        if src.exists():
            shutil.copy2(src, dst_dir / name)
            copied += 1

    cjk_src = src_dir / CJK_SOURCE
    if not cjk_src.exists():
        return f"拷贝 {copied} 个拉丁字体；缺 {CJK_SOURCE}，中文标题用系统字体"

    try:
        from fontTools import subset
    except ImportError:
        return f"拷贝 {copied} 个拉丁字体；缺 fonttools，中文标题用系统字体"

    chars = collect_heading_chars(html_pages)
    subset.main(
        [
            str(cjk_src),
            f"--text={''.join(sorted(chars))}",
            "--flavor=woff2",
            "--output-file=" + str(dst_dir / CJK_OUT),
            "--layout-features=*",
            "--no-hinting",
            "--desubroutinize",
        ]
    )
    size_kb = (dst_dir / CJK_OUT).stat().st_size // 1024
    return f"拷贝 {copied} 个拉丁字体 + 思源黑体 Bold 子集 {size_kb}KB（{len(chars)} 字符）"
