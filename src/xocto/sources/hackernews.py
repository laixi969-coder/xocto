"""Hacker News，走 Algolia 公共接口，无需密钥。

比 Product Hunt 更早、更真：开发者自荐（Show HN）往往在产品还没做营销时
就出现了，而且评论区会直接说出这东西哪里不行 —— 那是判断痛点真伪的好材料。

配置里可以写多组 query，同一条 story 命中多组只保留一次。
"""

from __future__ import annotations

import re

from ..dedupe import is_aggregator, url_host
from ..models import RawItem, now_iso
from .base import Http, register, to_iso, parse_iso
from datetime import datetime, timedelta, timezone
from urllib.parse import urlsplit

API = "https://hn.algolia.com/api/v1/search_by_date"
HITS_PER_PAGE = 100
DEFAULT_LOOKBACK_HOURS = 36

_SHOW_HN = re.compile(r"^\s*(?:show|launch)\s+hn\s*:\s*", re.I)

# HN 的 story 查询会捞回大量新闻报道（"扎克伯格抨击封闭 AI 对手"）。
# 那些不是产品，不该进产品池 —— 但对"大厂动作/趋势"那一节有用，
# 所以标记成 news 留在原始存档里，由下游决定怎么用。
_NEWS_HOSTS = frozenset(
    {
        "ft.com", "bbc.com", "bbc.co.uk", "economist.com", "nytimes.com", "wsj.com",
        "theverge.com", "techcrunch.com", "wired.com", "arstechnica.com", "reuters.com",
        "bloomberg.com", "cnbc.com", "theguardian.com", "washingtonpost.com",
        "businessinsider.com", "axios.com", "semafor.com", "theinformation.com",
        "404media.co", "restofworld.org", "abc.net.au", "npr.org", "cnn.com",
        "forbes.com", "fortune.com", "time.com", "theatlantic.com", "newyorker.com",
        "nature.com", "science.org", "spectrum.ieee.org", "technologyreview.com",
    }
)

# 企业博客/新闻稿的路径特征：/blog/、/news/、/2026/08/
_NEWS_PATH = re.compile(r"/(blog|news|press|newsroom|articles?)/|/\d{4}/\d{2}/", re.I)

# HN 标题里名字和描述的分隔符，实测有四种写法：
#   "Keen Code – an agentic coding agent"   破折号
#   "Needle2: 14MB agentic LLM for phones"  冒号
#   "Opencodex, a free open-source agent"   逗号
_SPLIT_DESC = re.compile(r"\s*(?:[–—]|(?<=\s)-(?=\s)|:|,)\s+")

# 以这些词开头的一定是句子不是产品名
_NOT_A_NAME = re.compile(
    r"^(a|an|the|i|we|my|our|how|why|what|when|is|it'?s|introducing"
    r"|building|built|make|making|use|using|watch|watching|open-source"
    r"|scroll|issue|design)\b",
    re.I,
)

# 产品名的形态约束：短、词少。放宽会把整句话当成名字。
MAX_NAME_LEN = 30
MAX_NAME_WORDS = 3


@register("hackernews")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    lookback = float(cfg.get("lookback_hours") or DEFAULT_LOOKBACK_HOURS)
    queries = cfg.get("queries") or []
    if not queries:
        print("    （没配 queries，跳过）")
        return []

    since = datetime.now(timezone.utc) - timedelta(hours=lookback)
    since_ts = int(since.timestamp())
    collected = now_iso()

    by_id: dict[str, RawItem] = {}

    for spec in queries:
        tags = spec.get("tags") or "story"
        query = spec.get("query") or ""
        min_points = int(spec.get("min_points") or 0)

        numeric = [f"created_at_i>{since_ts}"]
        if min_points > 0:
            numeric.append(f"points>={min_points}")

        payload = http.get_json(
            API,
            params={
                "tags": tags,
                "query": query,
                "numericFilters": ",".join(numeric),
                "hitsPerPage": HITS_PER_PAGE,
            },
        )

        hits = payload.get("hits") or []
        print(f"    [{tags}{' ' + query if query else ''}] {len(hits)} 条")

        for hit in hits:
            item = _parse_hit(hit, collected)
            # 同一条 story 命中多组 query 时只留一份
            if item is not None and item.external_id not in by_id:
                by_id[item.external_id] = item

    return list(by_id.values())


def _parse_hit(hit: dict, collected: str) -> RawItem | None:
    object_id = str(hit.get("objectID") or "").strip()
    raw_title = (hit.get("title") or "").strip()
    if not object_id or not raw_title:
        return None

    hn_url = f"https://news.ycombinator.com/item?id={object_id}"
    # 纯文本帖没有外链，退回讨论页
    url = (hit.get("url") or "").strip() or hn_url

    name, inline_desc = _derive_name(raw_title, url, hn_url)
    story_text = (hit.get("story_text") or "").strip()
    summary = inline_desc or _first_sentence(story_text)

    published = parse_iso(hit.get("created_at") or "")

    return RawItem(
        source="hackernews",
        external_id=object_id,
        title=name,
        url=url,
        summary=summary,
        published_at=to_iso(published) if published else "",
        collected_at=collected,
        metrics={
            "points": hit.get("points") or 0,
            "comments": hit.get("num_comments") or 0,
        },
        extra={
            "kind": "news" if _is_news(hit, url, hn_url) else "product",
            "builder": hit.get("author") or "",
            "author": hit.get("author") or "",
            "hn_url": hn_url,
            "tags": hit.get("_tags") or [],
            "original_title": raw_title,
        },
        payload=hit,
    )


def _derive_name(title: str, url: str, hn_url: str) -> tuple[str, str]:
    """从 HN 标题推断 (产品名, 描述)。

    Show HN 的标题有一大半根本不含产品名，而是一句话描述
    （"A tiny LLM running at 21,000 tok/s on a $250 FPGA"）。
    这种拿整句当名字，档案名会变成一长串，标题去重也就废了。
    所以拆不出名字时改用域名 —— 域名几乎总是产品名。
    """
    stripped = _SHOW_HN.sub("", title).strip()
    parts = _SPLIT_DESC.split(stripped, maxsplit=1)
    candidate = parts[0].strip()
    desc = parts[1].strip() if len(parts) == 2 else ""

    if _looks_like_name(candidate):
        return candidate, desc

    # 标题是句子不是名字，退到域名
    from_url = _name_from_url(url, hn_url)
    if from_url:
        return from_url, stripped

    # 域名也没有（纯讨论帖），只好截断整句
    return stripped[:MAX_NAME_LEN * 2], desc


def _is_news(hit: dict, url: str, hn_url: str) -> bool:
    """这条指向的是新闻报道还是产品。

    主判据是 HN 自己的 tag，不是域名黑名单 —— 黑名单永远填不完
    （openai.com、ai.meta.com 这些企业博客就漏掉了），而 tag 是准确的：
      Show HN / Launch HN = "我做了个东西"  → 产品
      其余 story          = "我看到篇文章"  → 新闻
    被判成新闻的不进产品池，但仍留在存档里供"趋势/大厂动作"那一节用。
    """
    tags = hit.get("_tags") or []
    if "show_hn" not in tags and "launch_hn" not in tags:
        return True

    # 到这里说明是 Show HN / Launch HN。极少数情况下有人拿它发文章，
    # 域名黑名单在这一层还有用。
    if not url or url == hn_url:
        return False

    host = url_host(url)
    if not host:
        return False
    if host in _NEWS_HOSTS or any(host.endswith("." + h) for h in _NEWS_HOSTS):
        return True

    try:
        return bool(_NEWS_PATH.search(urlsplit(url).path))
    except ValueError:
        return False


def _looks_like_name(text: str) -> bool:
    if not text or len(text) > MAX_NAME_LEN:
        return False
    if "%" in text or len(text.split()) > MAX_NAME_WORDS:
        return False
    return not _NOT_A_NAME.match(text)


def _name_from_url(url: str, hn_url: str) -> str:
    """从 URL 里取产品名。取不到返回空串。

    自有域名 acmewriter.com → acmewriter
    聚合站 github.com/user/cool-tool → cool-tool
    """
    if not url or url == hn_url:
        return ""

    host = url_host(url)
    if not host or host == "news.ycombinator.com":
        return ""

    if is_aggregator(host):
        # 聚合站下面取路径里的项目名。从后往前找第一个不是纯数字的段 ——
        # 末尾常是帖子 ID（x.com/user/status/2086754845218726027），
        # 那是 ID 不是名字。
        try:
            segments = [s for s in urlsplit(url).path.split("/") if s]
        except ValueError:
            return ""
        for segment in reversed(segments):
            if not segment.isdigit():
                return segment
        return ""

    # 去掉 TLD，保留主体（neolabs.fyi → neolabs）
    return host.split(".")[0]


def _first_sentence(text: str, limit: int = 220) -> str:
    if not text:
        return ""
    flat = " ".join(re.sub(r"<[^>]+>", " ", text).split())
    return flat[:limit] + ("…" if len(flat) > limit else "")
