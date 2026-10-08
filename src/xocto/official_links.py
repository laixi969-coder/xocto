"""Keep discovery/evidence URLs out of fields labelled as a product's website.

Product.url is also a discovery identity, so it must retain the original URL for
deduplication. Only the public website projection is filtered here; news and
data platforms can still be cited as evidence under their proper labels.
"""

from urllib.parse import urlsplit

from .dedupe import canonical_url, url_host
from .models import Product


# These pages describe, rank, distribute, or discuss somebody else's product.
# Product-owned subdomains on hosting services (e.g. pages.dev) are not blocked.
THIRD_PARTY_HOSTS = frozenset({
    "aicpb.com", "aicpb.cn", "similarweb.com", "semrush.com", "sensortower.com",
    "data.ai", "appfigures.com", "crunchbase.com", "pitchbook.com", "tracxn.com",
    "trustmrr.com", "starterstory.com", "toolify.ai", "theresanaiforthat.com",
    "futurepedia.io", "aitools.fyi", "producthunt.com", "ycombinator.com",
    "v2ex.com", "x.com", "twitter.com", "reddit.com", "youtube.com", "youtu.be",
    "linkedin.com", "zhihu.com", "medium.com", "substack.com",
    "github.com", "gitlab.com", "huggingface.co", "modelscope.cn",
    "npmjs.com", "pypi.org", "zenodo.org", "arxiv.org",
    "apps.apple.com", "testflight.apple.com", "play.google.com",
    "chromewebstore.google.com", "chrome.google.com",
    "news.google.com", "bing.com", "techcrunch.com", "tech.eu", "qbitai.com",
    "geekpark.net", "sifted.eu", "venturebeat.com", "theverge.com",
    "arstechnica.com", "technologyreview.com", "36kr.com", "ithome.com",
    "reuters.com", "bloomberg.com", "ft.com", "bbc.com", "bbc.co.uk",
    "nytimes.com", "wsj.com", "wired.com", "cnbc.com", "forbes.com",
    "businessinsider.com", "theguardian.com", "washingtonpost.com",
})

_NEWS_SOURCES = frozenset({"newssearch", "marketfeeds", "officialfeeds", "searchfeeds"})


def official_site_url(product: Product) -> str:
    """Return a website candidate only when it is not a known source page.

    An unseen publisher is still excluded using the stored news provenance. A
    company's announcement or customer story is evidence too, not proof that its
    domain belongs to the product being discussed. Never guess a replacement URL.
    """
    url = product.url.strip()
    try:
        parts = urlsplit(url)
        if parts.scheme not in {"http", "https"} or not parts.hostname or parts.username:
            return ""
    except ValueError:
        return ""
    host = url_host(url).rstrip(".")
    if any(host == domain or host.endswith("." + domain) for domain in THIRD_PARTY_HOSTS):
        return ""
    key = canonical_url(url)
    if any(
        canonical_url(sighting.url) == key
        and (sighting.kind == "news" or sighting.source in _NEWS_SOURCES)
        for sighting in product.sightings
    ):
        return ""
    return url
