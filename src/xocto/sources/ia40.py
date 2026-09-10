"""Madrona Intelligent Applications 40（IA40）年度榜单。

54 家机构的 72 位投资人从 450+ 家公司里提名投票，再叠加 PitchBook 数据
评分，选出当年最值得关注的私有 AI 公司。上榜本身就是强商业证据 ——
入选公司普遍已公开收入或 ARR。名单每年发布一次，页面是静态的：每天
重抓只为幂等地续上 sighting，并在 Madrona 更新页面时自动跟进入榜和
出局的变化。换届后改 config/sources.yaml 里的 URL 即可，external_id
带年份，历史条目不会被新榜单覆盖。

页面只给公司名和所属阶段，不给官网。域名表是入库时逐一验证过的手工
数据（探活 + 首页标题比对，见 tests/test_ia40.py）；新榜单出现表外
公司时宁可跳过并在日志里告警，也不编一个 URL —— 域名表补一行，下一
轮采集自动接上。
"""

from __future__ import annotations

import html as _html
import re

from ..models import RawItem, now_iso
from .base import Http, register

# 公司名 → 官网。验证记录见 tests/test_ia40.py（探活 + 标题比对）。
OFFICIAL_SITES: dict[str, str] = {
    # Early
    "Yutori": "https://yutori.com/",
    "Paper": "https://paper.design/",
    "AI Underwriting Company": "https://aiuc.com/",
    "Pierre": "https://pierre.computer/",
    "Clarify": "https://clarify.ai/",
    "JetStream Security": "https://jetstream.security/",
    "Fable Security": "https://fablesecurity.com/",
    "Resend": "https://resend.com/",
    "Roadrunner": "https://roadrunner.ai/",
    "Fireflies.ai": "https://fireflies.ai/",
    "Zed Industries": "https://zed.dev/",
    # Mid
    "Wispr Flow": "https://wisprflow.ai/",
    "Granola": "https://www.granola.ai/",
    "Serval": "https://www.serval.com/",
    "Profound": "https://www.tryprofound.com/",
    "Gamma": "https://gamma.app/",
    "Linear": "https://linear.app/",
    "CodeRabbit": "https://www.coderabbit.ai/",
    "Gradial": "https://gradial.com/",
    "Listen Labs": "https://listenlabs.ai/",
    "Town": "https://town.com/",
    "HeyGen": "https://www.heygen.com/",
    # Late
    "ElevenLabs": "https://elevenlabs.io/",
    "Anduril": "https://www.anduril.com/",
    "Ramp": "https://ramp.com/",
    "Sierra": "https://sierra.ai/",
    "OpenEvidence": "https://www.openevidence.com/",
    "Cognition": "https://cognition.com/",
    "Applied Intuition": "https://www.appliedintuition.com/",
    "Legora": "https://legora.com/",
    "Clay": "https://www.clay.com/",
    "Lovable": "https://lovable.dev/",
    "Simile": "https://www.simile.com/",
    # Enabler
    "Anthropic": "https://www.anthropic.com/",
    "Turbopuffer": "https://turbopuffer.com/",
    "Databricks": "https://www.databricks.com/",
    "OpenAI": "https://openai.com/",
    "Baseten": "https://www.baseten.co/",
    "OpenRouter": "https://openrouter.ai/",
    "ClickHouse": "https://clickhouse.com/",
    "Cartesia": "https://www.cartesia.ai/",
    "Together AI": "https://www.together.ai/",
    "Fal": "https://fal.ai/",
    "Vercel": "https://vercel.com/",
    "Fireworks AI": "https://fireworks.ai/",
    # Emerging Enabler
    "Gimlet Labs": "https://gimletlabs.ai/",
    "Browserbase": "https://www.browserbase.com/",
    "Mastra": "https://mastra.ai/",
}

# 榜单正文提到公司时用的简称。摘取提及句时连同全名一起匹配。
_ALIASES: dict[str, tuple[str, ...]] = {
    "AI Underwriting Company": ("AI Underwriting",),
    "JetStream Security": ("JetStream",),
    "Fable Security": ("Fable",),
    "Zed Industries": ("Zed",),
    "Fireflies.ai": ("Fireflies",),
    "Wispr Flow": ("Wispr",),
    "Listen Labs": ("Listen",),
    "Together AI": ("Together",),
    "Fireworks AI": ("Fireworks",),
    "Gimlet Labs": ("Gimlet",),
}

_LIST_MARKER = re.compile(r"The\s+(\d{4})\s+IA40</h5>", re.I)
_PUBLISHED = re.compile(r'article:published_time" content="([^"]+)"')
_STAGE_BLOCK = re.compile(r"<h4>([^<]+)</h4>\s*<(ol|ul)>(.*?)</\2>", re.S)
_ITEM = re.compile(r"<li>\s*([^<]+?)\s*</li>")
_TAG = re.compile(r"<[^>]+>")
_SENTENCE = re.compile(r"(?<=[.!?])\s+")


def _narrative_sentences(raw: str, marker_start: int) -> list[str]:
    """榜单之前的正文，拆成句子供各公司摘取与自己相关的提及。"""
    body = _TAG.sub(" ", raw[:marker_start])
    body = _html.unescape(re.sub(r"\s+", " ", body))
    return [s.strip() for s in _SENTENCE.split(body) if len(s.strip()) > 40]


def _mentions(name: str, sentences: list[str], *, limit: int = 3) -> str:
    keys = [name, *_ALIASES.get(name, ())]
    hits: list[str] = []
    for sentence in sentences:
        if any(re.search(rf"\b{re.escape(key)}\b", sentence) for key in keys):
            hits.append(sentence)
        if len(hits) >= limit:
            break
    return " ".join(hits)


@register("ia40")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    url = str(cfg.get("url") or "").strip()
    if not url:
        return []
    raw = http.get_text(url)

    marker = _LIST_MARKER.search(raw)
    if marker is None:
        raise RuntimeError(f"{url} 里找不到「The YYYY IA40」榜单标题，页面可能改版了")
    year = marker.group(1)
    published = ""
    meta = _PUBLISHED.search(raw)
    if meta:
        published = meta.group(1)
    collected = now_iso()

    sentences = _narrative_sentences(raw, marker.start())
    section = raw[marker.end():]

    items: list[RawItem] = []
    for stage_match in _STAGE_BLOCK.finditer(section):
        stage = _html.unescape(stage_match.group(1)).strip()
        for name_match in _ITEM.finditer(stage_match.group(3)):
            name = _html.unescape(name_match.group(1)).strip()
            site = OFFICIAL_SITES.get(name)
            if site is None:
                print(f"    ! IA40 {year} 入榜公司「{name}」不在域名表里，已跳过：补 sources/ia40.py 后下一轮自动入库")
                continue
            summary = f"Named to Madrona's {year} Intelligent Applications 40 ({stage} stage)."
            mentions = _mentions(name, sentences)
            if mentions:
                summary = f"{summary} {mentions}"[:700]
            items.append(
                RawItem(
                    source="ia40",
                    external_id=f"{year}:{name.casefold()}",
                    title=name,
                    url=site,
                    summary=summary,
                    published_at=published or collected,
                    collected_at=collected,
                    metrics={"stage": stage, "edition": year},
                    extra={},
                    payload={"stage": stage, "edition": year, "list_url": url},
                )
            )
    return items
