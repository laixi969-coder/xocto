"""去重：认出"这三条记录其实是同一个产品"。

判同的三条依据，按可靠性从高到低：
  1. 规范化 URL 完全相同
  2. 官网域名相同（聚合站域名除外 —— github.com 下面有几千万个项目）
  3. 标题归一化后相同（只在标题够长时才用，短名字容易撞车）

宁可漏判（同一产品建了两份档案）也不要误判（两个产品合成一份）。
漏判后面还能人工合并，误判会永久丢失信息。
"""

from __future__ import annotations

import re
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

from .models import Product, RawItem

# 这些域名下有海量不同产品，域名相同不代表是同一个东西
AGGREGATOR_HOSTS = frozenset(
    {
        "github.com",
        "gitlab.com",
        "producthunt.com",
        "aicpb.com",
        "news.ycombinator.com",
        "ycombinator.com",
        "huggingface.co",
        "x.com",
        "twitter.com",
        "medium.com",
        "substack.com",
        "notion.so",
        "notion.site",
        "gumroad.com",
        "reddit.com",
        "youtube.com",
        "linkedin.com",
        "apps.apple.com",
        "play.google.com",
        "chromewebstore.google.com",
        "chrome.google.com",
        "vercel.app",
        "netlify.app",
        "streamlit.app",
        "replit.app",
        "pages.dev",
        "webflow.io",
        "framer.website",
    }
)

# 跟踪参数，不参与判同
_TRACKING_PREFIXES = ("utm_", "ref_", "mtm_", "pk_")
_TRACKING_KEYS = frozenset({"ref", "source", "via", "fbclid", "gclid", "igshid", "app_id"})

# 标题归一化时要剥掉的常见后缀噪音
_TITLE_NOISE = re.compile(
    r"\b(app|ai|io|com|inc|labs?|studio|hq|official|beta|alpha)\b", re.I
)
_NON_WORD = re.compile(r"[^\w一-鿿]+")

MIN_TITLE_KEY_LEN = 4


def canonical_url(url: str) -> str:
    """URL 规范化，用于判同。

    统一 scheme 和大小写，去掉 www.、尾部斜杠、跟踪参数。
    保留有意义的 query（有些产品页靠 query 区分）。
    """
    if not url:
        return ""
    text = url.strip()
    if not re.match(r"^https?://", text, re.I):
        text = "https://" + text

    try:
        parts = urlsplit(text)
    except ValueError:
        return text.lower()

    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]

    path = re.sub(r"/{2,}", "/", parts.path or "").rstrip("/")

    kept = [
        (k, v)
        for k, v in parse_qsl(parts.query, keep_blank_values=False)
        if not k.lower().startswith(_TRACKING_PREFIXES) and k.lower() not in _TRACKING_KEYS
    ]
    query = urlencode(sorted(kept))

    return urlunsplit(("https", host, path, query, ""))


def url_host(url: str) -> str:
    """取主机名，已去掉 www.。取不出来返回空串。"""
    canon = canonical_url(url)
    if not canon:
        return ""
    try:
        return (urlsplit(canon).hostname or "").lower()
    except ValueError:
        return ""


def is_aggregator(host: str) -> bool:
    """这个域名是不是聚合站。子域也算（比如 foo.vercel.app）。"""
    if not host:
        return True
    if host in AGGREGATOR_HOSTS:
        return True
    return any(host.endswith("." + agg) for agg in AGGREGATOR_HOSTS)


def title_key(title: str) -> str:
    """标题归一化。太短或全是噪音词就返回空串（表示不可用于判同）。"""
    if not title:
        return ""
    lowered = title.strip().lower()
    # 去掉括号里的补充说明
    lowered = re.sub(r"[\(\[（【].*?[\)\]）】]", " ", lowered)
    cleaned = _TITLE_NOISE.sub(" ", lowered)
    key = _NON_WORD.sub("", cleaned)
    return key if len(key) >= MIN_TITLE_KEY_LEN else ""


class ProductIndex:
    """产品池的判同索引。

    构造一次，之后每条新记录 O(1) 查匹配。
    """

    def __init__(self, products: list[Product] | None = None) -> None:
        self._by_slug: dict[str, Product] = {}
        self._by_url: dict[str, str] = {}  # canonical_url -> slug
        self._by_host: dict[str, str] = {}  # host -> slug
        self._by_title: dict[str, str] = {}  # title_key -> slug
        for product in products or []:
            self.add(product)

    def add(self, product: Product) -> None:
        """把产品加进索引。已存在的 slug 会被替换（更新场景）。"""
        self._by_slug[product.slug] = product

        for url in {product.canonical_url, canonical_url(product.url)}:
            if url:
                self._by_url.setdefault(url, product.slug)

        host = url_host(product.canonical_url or product.url)
        if host and not is_aggregator(host):
            self._by_host.setdefault(host, product.slug)

        key = title_key(product.name)
        if key:
            self._by_title.setdefault(key, product.slug)

    def get(self, slug: str) -> Product | None:
        return self._by_slug.get(slug)

    def all(self) -> list[Product]:
        return list(self._by_slug.values())

    def match(self, item: RawItem) -> Product | None:
        """给一条原始记录找池子里已有的产品。找不到返回 None。"""
        canon = canonical_url(item.url)

        if canon and canon in self._by_url:
            return self._by_slug.get(self._by_url[canon])

        host = url_host(item.url)
        if host and not is_aggregator(host) and host in self._by_host:
            return self._by_slug.get(self._by_host[host])

        key = title_key(item.title)
        if key and key in self._by_title:
            return self._by_slug.get(self._by_title[key])

        return None

    def next_free_slug(self, slug: str) -> str:
        """slug 撞车时加数字后缀。

        撞车说明标题归一化后相同但判定为不同产品 —— 这是有意为之的保守策略，
        两份档案总比错误合并强。
        """
        if slug not in self._by_slug:
            return slug
        for n in range(2, 100):
            candidate = f"{slug}-{n}"
            if candidate not in self._by_slug:
                return candidate
        raise RuntimeError(f"slug「{slug}」冲突超过 100 次，检查是不是采集出了问题")
