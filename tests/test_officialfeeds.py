from __future__ import annotations

from datetime import datetime, timezone
from email.utils import format_datetime
import unittest

from xocto.sources.officialfeeds import fetch, fetch_market


NOW_RSS = format_datetime(datetime.now(timezone.utc))
NOW_ATOM = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class FakeHttp:
    def get_text(self, url: str) -> str:
        if url == "https://example.com/rss.xml":
            return f"""<rss><channel><item><title>New model</title><link>https://example.com/model</link><pubDate>{NOW_RSS}</pubDate><description>&lt;p&gt;A first-party update.&lt;/p&gt;</description></item></channel></rss>"""
        return f"""<feed xmlns=\"http://www.w3.org/2005/Atom\"><entry><title>SDK update</title><link href=\"https://example.com/sdk\"/><updated>{NOW_ATOM}</updated><summary>Documented capability.</summary></entry></feed>"""


class OfficialFeedTests(unittest.TestCase):
    def test_rss_and_atom_entries_are_first_party_news(self) -> None:
        rows = fetch(
            {
                "lookback_hours": 72,
                "feeds": [
                    {"name": "Example", "url": "https://example.com/rss.xml"},
                    {"name": "Example Labs", "url": "https://example.com/atom.xml"},
                ],
            },
            FakeHttp(),
        )
        self.assertEqual([item.title for item in rows], ["New model", "SDK update"])
        self.assertTrue(all(item.extra["kind"] == "news" for item in rows))
        self.assertTrue(all(item.extra["official"] for item in rows))
        self.assertEqual(rows[0].summary, "A first-party update.")

    def test_independent_writer_feed_is_news_but_not_first_party(self) -> None:
        rows = fetch(
            {
                "lookback_hours": 72,
                "feeds": [
                    {
                        "name": "Independent",
                        "url": "https://example.com/rss.xml",
                        "official": False,
                    }
                ],
            },
            FakeHttp(),
        )
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].extra["kind"], "news")
        self.assertFalse(rows[0].extra["official"])

    def test_market_feeds_default_to_independent_and_are_separately_identified(self) -> None:
        rows = fetch_market(
            {
                "lookback_hours": 72,
                "feeds": [{"name": "Independent", "url": "https://example.com/rss.xml"}],
            },
            FakeHttp(),
        )
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].source, "marketfeeds")
        self.assertFalse(rows[0].extra["official"])

    def test_duplicate_entries_across_feeds_are_still_deduplicated(self) -> None:
        rows = fetch_market(
            {
                "lookback_hours": 72,
                "max_parallel_feeds": 2,
                "feeds": [
                    {"name": "Writer A", "url": "https://example.com/rss.xml"},
                    {"name": "Writer B", "url": "https://example.com/rss.xml"},
                ],
            },
            FakeHttp(),
        )
        self.assertEqual(len(rows), 1)


if __name__ == "__main__":
    unittest.main()
