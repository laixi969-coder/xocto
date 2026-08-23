"""V2EX 的中文早期项目发现。

V2EX 是创始人、设计师和开发者发布项目的公开社区。这里不把整站讨论都当产品：
只读取明确配置的节点；泛开发节点还要求同时出现 AI 线索、发布动作和外部产品链接。
帖子是发现与早期讨论证据，产品 URL 则用于跨渠道去重。
"""

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from urllib.parse import urlsplit

from ..dedupe import is_aggregator, url_host
from ..models import RawItem, now_iso
from .base import Http, register, to_iso

API = "https://www.v2ex.com/api/topics/show.json"
_URL = re.compile(r"https?://[^\s<>\]\[)\\\"']+", re.I)
_AI = re.compile(r"\b(?:ai|llm|aigc|gpt|mcp|agent)\b|人工智能|大模型|智能体|生成式", re.I)
_LAUNCH = re.compile(r"发布|上线|推出|开源|内测|公测|做了.{0,12}(?:工具|产品|应用)|\b(?:launch|released?|built|open[ -]?source)\b", re.I)


def _epoch_iso(value: object) -> str:
    try:
        return to_iso(datetime.fromtimestamp(float(value), timezone.utc))
    except (TypeError, ValueError, OSError):
        return ""


def _external_url(text: str, topic_url: str) -> str:
    for match in _URL.findall(text or ""):
        url = match.rstrip(".,，。!！?？:：")
        host = url_host(url)
        if host and host != url_host(topic_url) and not is_aggregator(url):
            return url
    return ""


def _name_from_url(url: str, fallback: str) -> str:
    host = url_host(url).removeprefix("www.")
    if not host:
        return fallback[:80]
    head = host.split(".")[0].replace("-", " ").replace("_", " ").strip()
    return head.title() or fallback[:80]


def _parse_topic(topic: dict, *, node: str, strict: bool, collected: str) -> RawItem | None:
    topic_id = str(topic.get("id") or "").strip()
    title = str(topic.get("title") or "").strip()
    topic_url = str(topic.get("url") or "").strip()
    content = str(topic.get("content") or "").strip()
    if not topic_id or not title or not topic_url:
        return None
    text = f"{title}\n{content}"
    product_url = _external_url(text, topic_url)
    # 泛开发节点只留下“AI + 发布动作 + 可去重产品地址”；指定 AI SaaS 节点
    # 允许更早、更少信息的项目，但仍需有独立产品链接。
    if not product_url or (strict and (not _AI.search(text) or not _LAUNCH.search(text))):
        return None
    published = _epoch_iso(topic.get("created"))
    return RawItem(
        source="v2ex",
        external_id=topic_id,
        title=_name_from_url(product_url, title),
        url=product_url,
        summary=content or title,
        published_at=published,
        collected_at=collected,
        metrics={"comments": int(topic.get("replies") or 0)},
        extra={
            "kind": "product",
            "ecosystem": "zh",
            "market": "CN",
            "evidence_url": topic_url,
            "evidence_title": title,
            "evidence_tier": "independent",
            "node": node,
            "builder": str((topic.get("member") or {}).get("username") or ""),
        },
        payload=topic,
    )


@register("v2ex")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    """读取中文项目发布节点；V2EX 旧版公开接口无需登录。"""
    lookback = float(cfg.get("lookback_hours") or 72)
    since = datetime.now(timezone.utc) - timedelta(hours=lookback)
    collected = now_iso()
    nodes = cfg.get("nodes") or []
    rows: list[RawItem] = []
    seen: set[str] = set()
    for spec in nodes:
        node = str(spec.get("name") if isinstance(spec, dict) else spec).strip()
        if not node:
            continue
        strict = bool(spec.get("strict", node != "aisaas")) if isinstance(spec, dict) else node != "aisaas"
        payload = http.get_json(API, params={"node_name": node})
        topics = payload if isinstance(payload, list) else []
        accepted = 0
        for topic in topics:
            if not isinstance(topic, dict):
                continue
            published = _epoch_iso(topic.get("created"))
            if published:
                try:
                    if datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc) < since:
                        continue
                except ValueError:
                    pass
            item = _parse_topic(topic, node=node, strict=strict, collected=collected)
            if item is not None and item.external_id not in seen:
                rows.append(item)
                seen.add(item.external_id)
                accepted += 1
        print(f"    [V2EX {node}] {accepted}/{len(topics)} 条")
    return rows
