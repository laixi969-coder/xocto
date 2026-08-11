"""Product Hunt 官方 GraphQL API。

为什么要它：PH 除了 RSS 之外整站 403（Cloudflare），RSS 又只给产品名和一句
tagline —— 没有票数、没有真实官网、没有分类。三十多个产品因此只能停在
"一句话判断"，看不到定价也看不到官网。

官方 API 一次解决这三样：
    website     产品真实官网（RSS 只给 PH 自己的页面链接）
    votesCount  票数，能看出真实关注度
    topics      官方分类，比关键词猜赛道准

需要一个免费 token（producthunt.com/v2/oauth/applications 申请，五分钟）。
token 只从环境变量读，不进配置文件也不进仓库。
没有 token 时自动退回 RSS 模式，功能照常，只是信息少一些。
"""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone

from ..models import RawItem, now_iso
from .base import Http, HttpError, to_iso, parse_iso

API = "https://api.producthunt.com/v2/api/graphql"
TOKEN_ENV = "PRODUCTHUNT_TOKEN"
PAGE_SIZE = 50

# 只取需要的字段。PH 对查询复杂度有配额，多要一个字段就多烧一点额度。
_QUERY = """
query($after: DateTime!, $first: Int!, $cursor: String) {
  posts(order: NEWEST, postedAfter: $after, first: $first, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    edges {
      node {
        id
        name
        tagline
        description
        url
        website
        votesCount
        commentsCount
        createdAt
        topics(first: 5) { edges { node { name } } }
        makers { name username }
      }
    }
  }
}
"""


def has_token() -> bool:
    return bool(os.environ.get(TOKEN_ENV, "").strip())


def fetch_via_api(cfg: dict, http: Http) -> list[RawItem]:
    """走官方 API 抓最近的新品。没有 token 会抛异常，调用方负责回退。"""
    token = os.environ.get(TOKEN_ENV, "").strip()
    if not token:
        raise HttpError(f"没有设置 {TOKEN_ENV} 环境变量")

    lookback = float(cfg.get("lookback_hours") or 48)
    after = (datetime.now(timezone.utc) - timedelta(hours=lookback)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    collected = now_iso()

    items: list[RawItem] = []
    cursor: str | None = None
    pages = 0
    max_pages = int(cfg.get("max_pages") or 4)

    while pages < max_pages:
        payload = _post(
            http,
            token,
            {"after": after, "first": PAGE_SIZE, "cursor": cursor},
        )
        posts = (payload.get("data") or {}).get("posts") or {}
        edges = posts.get("edges") or []

        for edge in edges:
            item = _parse_node(edge.get("node") or {}, collected)
            if item is not None:
                items.append(item)

        page_info = posts.get("pageInfo") or {}
        pages += 1
        if not page_info.get("hasNextPage"):
            break
        cursor = page_info.get("endCursor")
        if not cursor:
            break

    print(f"    [官方接口] {len(items)} 条，{pages} 页")
    return items


def _post(http: Http, token: str, variables: dict) -> dict:
    """GraphQL 请求。Http 只封装了 GET，这里直接用 httpx 发 POST。"""
    import httpx

    try:
        resp = httpx.post(
            API,
            json={"query": _QUERY, "variables": variables},
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
                "User-Agent": http.user_agent,
            },
            timeout=http.timeout,
        )
    except httpx.HTTPError as exc:
        raise HttpError(f"官方接口请求失败：{exc}") from exc

    if resp.status_code == 401:
        raise HttpError(f"{TOKEN_ENV} 无效或已过期")
    if resp.status_code == 429:
        raise HttpError("官方接口配额用尽，等一会儿再试")
    if resp.status_code >= 400:
        raise HttpError(f"官方接口返回 {resp.status_code}")

    try:
        data = resp.json()
    except ValueError as exc:
        raise HttpError(f"官方接口返回的不是合法 JSON：{exc}") from exc

    if data.get("errors"):
        first = data["errors"][0].get("message", "未知错误")
        raise HttpError(f"查询被拒：{first}")
    return data


def _parse_node(node: dict, collected: str) -> RawItem | None:
    post_id = str(node.get("id") or "").strip()
    name = (node.get("name") or "").strip()
    if not post_id or not name:
        return None

    # website 才是产品官网，url 是 PH 自己的页面。优先用前者 ——
    # 指向聚合站的链接既暴露来源，对读者也没价值。
    website = (node.get("website") or "").strip()
    ph_url = (node.get("url") or "").strip()

    topics = [
        (e.get("node") or {}).get("name", "")
        for e in ((node.get("topics") or {}).get("edges") or [])
    ]
    makers = [m.get("name") or m.get("username") or "" for m in (node.get("makers") or [])]
    created = parse_iso(node.get("createdAt") or "")

    return RawItem(
        source="producthunt",
        external_id=post_id,
        title=name,
        url=website or ph_url,
        summary=(node.get("tagline") or "").strip(),
        published_at=to_iso(created) if created else "",
        collected_at=collected,
        metrics={
            "points": node.get("votesCount") or 0,
            "comments": node.get("commentsCount") or 0,
        },
        extra={
            "builder": makers[0] if makers else "",
            "makers": [m for m in makers if m],
            "topics": [t for t in topics if t],
            "description": (node.get("description") or "").strip(),
            "listing_url": ph_url,
            "via": "api",
        },
        payload=node,
    )
