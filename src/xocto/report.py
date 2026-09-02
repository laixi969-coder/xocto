"""每日观察的结构化解析 —— 把扁平的 Markdown 切成有层级的版块。

报告是手写的 Markdown，一条直线：## / ### / 段落 / 表格 / 列表。
整篇丢给渲染器会得到一坨没有主次的长文 ——
"今天最值得看的 3 个"（全篇最值钱）和"这份观察的边界"（免责声明）
长得一模一样，读者进来不知道有什么、有多长、该先看哪里。

所以这里把直线切成结构：
每个 ## 一个版块（带编号、锚点、条目数、类型），
"最值得看"里的 ### 再拆成带排名和推荐度徽章的产品卡。

纯确定性切分，不做任何判断 —— 判断在写报告的时候就做完了。
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import mistune

from .i18n import Locale
from .models import scrub_pending_phrase

_render_markdown = mistune.create_markdown(plugins=["table", "strikethrough"])


def _markdown(text: str) -> str:
    if not text:
        return ""
    html = _render_markdown(text)
    # mistune can leave CJK-adjacent **emphasis** as literal markers
    if "**" in html:
        html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    return scrub_pending_phrase(html)

# 报告里指向 data/ 的相对链接在网站上打不开，得指回站内产品页
_DATA_LINK = re.compile(r"\((?:\.{1,2}/)*(?:data/)?(?:analysis|pool)/([^)\s/]+?)\.md\)")

# 版块末尾的"→ [完整分析](...)"：单独抽出来做按钮，不留在正文里
_CTA_LINE = re.compile(r"^\s*(?:→|->)\s*\[([^\]]+)\]\(([^)]+)\)\s*$", re.M)

# 版块之间的 --- 由版式提供留白，不需要再画一条线
_RULE_LINE = re.compile(r"^-{3,}\s*$", re.M)

# 整段只有一句加粗（可能带冒号）—— 作者的意思是小标题，不是段落
_LABEL_ONLY = re.compile(r"^\*\*([^*]+?)\*\*\s*[:：]?$")

# 模型偶尔会把“1. A：… 2. B：…”塞进同一个段落。内容没丢，但卡片解析器
# 只认 ###，会把三条判断排成一堵墙。这里仅接住完整的连续编号段，避免猜测正文。
_INLINE_PICK = re.compile(
    r"(?:^|\s)(?P<rank>\d+)\s*[.、]\s*(?P<name>[^：:\n]+?)\s*[：:]\s*"
    r"(?P<lead>.*?)(?=(?:\s+\d+\s*[.、]\s*[^：:\n]+?\s*[：:])|\Z)",
    re.S,
)


@dataclass(frozen=True)
class Pick:
    """一个上榜产品。排名、推荐度、指标各自成件，不再是一行纯文本标题。"""

    rank: str
    name: str
    verdict: str
    verdict_key: str
    metas: tuple[str, ...]
    lead: str
    body_html: str
    link: str
    link_label: str

    @property
    def is_empty(self) -> bool:
        """没有可读内容的占位小节不占用一张卡。"""
        marker = self.lead.strip().casefold().rstrip("。.!！")
        return not self.body_html and marker in {"无", "none", "n/a", "暂无"}

    @property
    def is_list(self) -> bool:
        """清单型补充信息用更轻的附录版式。"""
        return self.body_html.lstrip().startswith(("<ul>", "<ol>"))


@dataclass(frozen=True)
class Section:
    """一个版块。

    kind 决定版式：picks 出卡片、table 放宽到全宽、quiet 降权收进注记块。
    count_label 让读者在目录里就知道每块有多少东西。
    """

    index: str
    title: str
    subtitle: str
    anchor: str
    kind: str
    count_label: str
    lead_html: str
    body_html: str
    picks: tuple[Pick, ...]


@dataclass(frozen=True)
class ReportDoc:
    intro: str
    read_minutes: int
    sections: tuple[Section, ...]


def _plain(md: str) -> str:
    """把 Markdown 压成纯文本，用于摘要和字数统计。"""
    flat = re.sub(r"[#>*_`\[\]()|]", " ", md)
    flat = re.sub(r"^\s*[-–—]\s*", "", flat, flags=re.M)
    return " ".join(flat.split())


def _fix_links(md: str) -> str:
    """data/ 里的相对路径换成站内产品页。报告页在 site/r/，同样退一级。"""
    return _DATA_LINK.sub(lambda m: f"(../p/{m.group(1)}.html)", md)


def _promote_labels(md: str) -> str:
    """把"整段只有一句加粗"提成小标题。

    "**替代关系清晰、值得下次留意：**" 后面跟一串 bullet —— 作者写的是分组标签，
    渲染成加粗段落就和正文一个层级，一长串清单还是一堵墙。
    整段完全匹配才动，"**结论**——后面还有话"这种不碰。
    """
    paras = re.split(r"\n\s*\n", md)
    out = []
    for para in paras:
        match = _LABEL_ONLY.match(para.strip())
        # 提成标题之后那个冒号就多余了
        out.append(f"#### {match.group(1).strip().rstrip('：:')}" if match else para)
    return "\n\n".join(out)


def _split_title(title: str) -> tuple[str, str]:
    """标题拆成主标 + 副标。

    "今天的趋势：SaaS 正在被为 agent 重做一遍" → 主标短、副标长，
    层级立刻出来了；全塞在一行里就只是一句长句子。
    """
    for sep in ("：", ":"):
        if sep in title:
            head, _, tail = title.partition(sep)
            if head.strip() and tail.strip():
                return head.strip(), tail.strip()
    match = re.match(r"^(.+?)（(.+)）$", title)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return title.strip(), ""


def _count_label(md: str, kind: str, picks: int, locale: Locale) -> str:
    """版块里有多少东西。目录靠它给出篇幅预期。"""
    if kind == "picks":
        return locale.count_label("picks", picks) if picks else ""
    if kind == "table":
        rows = [ln.strip() for ln in md.splitlines() if ln.strip().startswith("|")]
        seps = [ln for ln in rows if set(ln) <= set("|-: ")]
        # 每条分隔线对应一个表头行，两者都不是数据
        data = len(rows) - len(seps) * 2
        return locale.count_label("table", data) if data > 0 else ""
    if kind == "list":
        items = re.findall(r"^\s*(?:[-*]|\d+\.)\s+\S", md, re.M)
        return locale.count_label("list", len(items)) if items else ""
    return ""


def _kind(md: str, title: str, locale: Locale) -> str:
    if _RULE_LINE.sub("", md).lstrip().startswith("|") or "\n|" in md:
        kind = "table"
    elif re.search(r"^\s*(?:[-*]|\d+\.)\s+\S", md, re.M):
        kind = "list"
    else:
        kind = "prose"
    if any(hint in title for hint in locale.quiet_hints):
        return "quiet"
    return kind


def _read_minutes(text: str, locale: Locale) -> int:
    """估阅读时长。中文按字数，英文按词数 —— 英文用字数会把 5 分钟报成 20 分钟。"""
    size = len(text.split()) if locale.read_unit == "words" else len(text)
    return max(1, round(size / locale.read_speed))


def _parse_pick_head(
    head: str, fallback_rank: int, locale: Locale
) -> tuple[str, str, tuple[str, ...], str]:
    """拆开 "1. 名字 · 开源关注 655 · **强烈推荐**"。

    整行当标题渲染出来的效果是：所有信息同一号字、同一个颜色，
    等于没有分级。拆成排名 / 名字 / 指标 / 推荐度四件之后才能分别给权重。
    """
    text = head.replace("**", "").strip()
    parts = [p.strip() for p in text.split("·") if p.strip()]
    if not parts:
        return f"{fallback_rank:02d}", text, (), ""

    name = parts[0]
    rank = f"{fallback_rank:02d}"
    match = re.match(r"^(\d+)\s*[.、]\s*(.+)$", name)
    if match:
        rank = f"{int(match.group(1)):02d}"
        name = match.group(2).strip()

    verdict = ""
    rest = parts[1:]
    if rest and locale.verdict_key(rest[-1]):
        verdict = rest[-1]
        rest = rest[:-1]
    return rank, name, tuple(rest), verdict


def _parse_inline_picks(text: str) -> tuple[tuple[str, str, str], ...]:
    """识别一个完整的行内编号产品段；不完整时保持原样交给普通 Markdown。"""
    text = text.strip()
    matches = list(_INLINE_PICK.finditer(text))
    if len(matches) < 2:
        return ()

    cursor = 0
    rows: list[tuple[str, str, str]] = []
    for match in matches:
        if text[cursor:match.start()].strip():
            return ()
        cursor = match.end()
        rows.append(
            (
                match.group("rank"),
                match.group("name").replace("**", "").strip(),
                _plain(match.group("lead")),
            )
        )
    return tuple(rows) if not text[cursor:].strip() else ()


def _parse_picks(body: str, locale: Locale) -> tuple[str, tuple[Pick, ...]]:
    """把 ### 拆成产品卡，返回（版块引言, 卡片）。"""
    chunks = re.split(r"^###\s+", body, flags=re.M)
    lead = _RULE_LINE.sub("", chunks[0]).strip()
    picks: list[Pick] = []

    for i, chunk in enumerate(chunks[1:], start=1):
        head, _, rest = chunk.partition("\n")
        inline_picks = _parse_inline_picks(rest)
        if inline_picks:
            # “今天最值得看的 3 个”只是分组标题；真正的卡片由其中三条产品构成。
            for rank, name, inline_lead in inline_picks:
                picks.append(
                    Pick(
                        rank=f"{int(rank):02d}",
                        name=name,
                        verdict="",
                        verdict_key="",
                        metas=(),
                        lead=scrub_pending_phrase(inline_lead),
                        body_html="",
                        link="",
                        link_label=locale.cta_default,
                    )
                )
            continue
        rank, name, metas, verdict = _parse_pick_head(head, len(picks) + 1, locale)

        rest = _RULE_LINE.sub("", rest)
        link = link_label = ""
        cta = _CTA_LINE.search(rest)
        if cta:
            link_label, link = cta.group(1).strip(), cta.group(2).strip()
            rest = _CTA_LINE.sub("", rest)

        # 第一段是一句话定位，单独放大 —— 读者扫一眼只看这句
        paras = [p.strip() for p in re.split(r"\n\s*\n", rest.strip()) if p.strip()]
        first = paras[0] if paras else ""
        lead_text = _plain(first) if first and not first.startswith(("|", "-", "*", ">")) else ""
        body_md = "\n\n".join(paras[1:] if lead_text else paras)

        verdict_key = locale.verdict_key(verdict)
        picks.append(
            Pick(
                rank=rank,
                name=name,
                verdict=locale.verdict_label(verdict),
                verdict_key=verdict_key,
                metas=metas,
                lead=scrub_pending_phrase(lead_text),
                body_html=_markdown(body_md) if body_md else "",
                link=link,
                link_label=link_label or locale.cta_default,
            )
        )
    return (_markdown(lead) if lead else ""), tuple(picks)


def parse_report(md: str, locale: Locale) -> ReportDoc:
    """扁平 Markdown → 有层级的版块结构。"""
    md = _fix_links(md)
    md = re.sub(r"\A\s*#\s+[^\n]*\n", "", md)

    chunks = re.split(r"^##\s+", md, flags=re.M)

    intro = ""
    for para in re.split(r"\n\s*\n", _RULE_LINE.sub("", chunks[0])):
        text = _plain(para)
        if text:
            intro = scrub_pending_phrase(text)
            break

    sections: list[Section] = []
    for i, chunk in enumerate(chunks[1:], start=1):
        head, _, rest = chunk.partition("\n")
        title, subtitle = _split_title(head)
        has_picks = bool(re.search(r"^###\s+", rest, re.M))
        kind = "picks" if has_picks else _kind(rest, head, locale)

        lead_html = ""
        picks: tuple[Pick, ...] = ()
        body_html = ""
        if has_picks:
            lead_html, picks = _parse_picks(rest, locale)
        else:
            body_html = _markdown(_promote_labels(_RULE_LINE.sub("", rest).strip()))

        # 标题里已经写了数量（"今天最值得看的 3 个"）就别再右对齐标一次
        visible_picks = sum(not pick.is_empty for pick in picks)
        count = _count_label(rest, kind, visible_picks, locale)
        if count and count.replace(" ", "") in head.replace(" ", ""):
            count = ""

        sections.append(
            Section(
                index=f"{i:02d}",
                title=title,
                subtitle=subtitle,
                anchor=f"s{i:02d}",
                kind=kind,
                count_label=count,
                lead_html=lead_html,
                body_html=body_html,
                picks=picks,
            )
        )

    return ReportDoc(
        intro=intro,
        read_minutes=_read_minutes(_plain(md), locale),
        sections=tuple(sections),
    )


def split_stat(text: str) -> tuple[str, str]:
    """"3 个值得看" → ("3", "个值得看")，让开头那个数字能单独放大。"""
    match = re.match(r"^([+\-]?\d[\d,.]*%?)\s*(.*)$", text.strip())
    if match and match.group(2):
        return match.group(1), match.group(2).strip()
    return "", text.strip()
