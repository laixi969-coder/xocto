from __future__ import annotations

from datetime import datetime, timezone
from email.utils import format_datetime
import unittest

from xocto.sources.newssearch import SEARCH_URL, fetch


class FakeHttp:
    def get_text(self, url: str, *, params: dict | None = None) -> str:
        assert url == SEARCH_URL
        title = "AI company reports recurring revenue - Example News" if params and params["hl"] == "en-US" else "智能体业务披露复购收入 - Example News"
        link = "https://news.google.com/rss/articles/" + ("en" if params and params["hl"] == "en-US" else "zh")
        return f"""<rss><channel><item><title>{title}</title><link>{link}</link><pubDate>{format_datetime(datetime.now(timezone.utc))}</pubDate><description>&lt;p&gt;Documented commercial signal.&lt;/p&gt;</description><source>Example News</source></item></channel></rss>"""


class NewsSearchTests(unittest.TestCase):
    def test_search_lanes_preserve_cross_language_news_as_discovery_signals(self) -> None:
        rows = fetch({
            "queries": [
                {"name": "US commercial", "query": "AI revenue", "hl": "en-US", "ecosystem": "en", "market": "US"},
                {"name": "CN commercial", "query": "AI 营收", "hl": "zh-CN", "ecosystem": "zh", "market": "CN"},
            ]
        }, FakeHttp())

        self.assertEqual(len(rows), 2)
        self.assertTrue(all(row.extra["kind"] == "news" for row in rows))
        self.assertEqual({row.extra["content_ecosystem"] for row in rows}, {"zh", "en"})
        self.assertTrue(all(not row.title.endswith("Example News") for row in rows))
        self.assertTrue(all("Documented commercial signal" in row.summary for row in rows))


if __name__ == "__main__":
    unittest.main()
