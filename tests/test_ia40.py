from __future__ import annotations

import unittest

from xocto.sources.base import HttpError
from xocto.sources.ia40 import OFFICIAL_SITES, fetch

PAGE = """
<html><head>
<meta property="article:published_time" content="2026-08-31T15:00:01+00:00" />
</head><body>
<p>Customer service with Sierra, design with Paper, agentic browsing with Yutori.
The winners will connect AI capability to an end customer and prove the ROI.</p>
<h5>The 2026 IA40</h5>
<h4>Early</h4>
<ol><li>Yutori</li><li>Mystery Labs</li></ol>
<h4>Enabler</h4>
<ol><li>Anthropic</li></ol>
<h4>Emerging Enabler</h4>
<ul><li>Mastra</li></ul>
</body></html>
"""


class FakeHttp:
    def get_text(self, url: str) -> str:
        if "example.com" in url:
            return PAGE
        raise HttpError(f"{url} 返回 404")


class Ia40Tests(unittest.TestCase):
    def test_list_is_parsed_with_stage_and_official_site(self) -> None:
        rows = fetch({"url": "https://example.com/ia40/"}, FakeHttp())
        # Mystery Labs 不在域名表里：宁可跳过并告警，也不编一个 URL。
        self.assertEqual([item.title for item in rows], ["Yutori", "Anthropic", "Mastra"])
        self.assertTrue(all(item.source == "ia40" for item in rows))
        by_name = {item.title: item for item in rows}
        self.assertEqual(by_name["Yutori"].url, OFFICIAL_SITES["Yutori"])
        self.assertEqual(by_name["Yutori"].external_id, "2026:yutori")
        self.assertEqual(
            by_name["Anthropic"].metrics, {"stage": "Enabler", "edition": "2026"}
        )
        self.assertEqual(by_name["Anthropic"].published_at, "2026-08-31T15:00:01+00:00")

    def test_summary_carries_listing_fact_and_narrative_mentions(self) -> None:
        rows = fetch({"url": "https://example.com/ia40/"}, FakeHttp())
        by_name = {item.title: item for item in rows}
        self.assertIn("Named to Madrona's 2026 Intelligent Applications 40 (Early stage)", by_name["Yutori"].summary)
        self.assertIn("design with Paper", by_name["Yutori"].summary)
        # 正文没提 Anthropic，只有上榜事实，不硬凑。
        self.assertEqual(
            by_name["Anthropic"].summary,
            "Named to Madrona's 2026 Intelligent Applications 40 (Enabler stage).",
        )

    def test_restructured_page_fails_loudly_instead_of_returning_silently_empty(self) -> None:
        with self.assertRaises(RuntimeError):
            fetch({"url": "https://example.com/ia40/"}, _Static("<html>改版了</html>"))

    def test_disabled_url_yields_nothing(self) -> None:
        self.assertEqual(fetch({"url": ""}, FakeHttp()), [])

    def test_every_curated_site_is_https(self) -> None:
        # 域名表是手工数据，写错协议或留空会直接污染产品池的展示链接。
        for name, site in OFFICIAL_SITES.items():
            self.assertTrue(site.startswith("https://"), f"{name}: {site}")


class _Static:
    def __init__(self, body: str) -> None:
        self._body = body

    def get_text(self, url: str) -> str:
        return self._body


if __name__ == "__main__":
    unittest.main()
