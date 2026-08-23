from __future__ import annotations

import unittest

from xocto.sources.v2ex import API, fetch


class FakeHttp:
    def __init__(self, payload: list[dict]) -> None:
        self.payload = payload
        self.calls: list[tuple[str, dict]] = []

    def get_json(self, url: str, *, params: dict) -> list[dict]:
        self.calls.append((url, params))
        return self.payload


class V2exDiscoveryTests(unittest.TestCase):
    def test_chinese_launch_uses_product_url_but_keeps_post_as_independent_evidence(self) -> None:
        http = FakeHttp([
            {
                "id": 101,
                "title": "发布：面向货代的 AI 异常处理工具",
                "url": "https://www.v2ex.com/t/101",
                "content": "我们上线了 AI 货运异常处理产品：https://freight-ai.cn",
                "created": 1787500000,
                "replies": 7,
                "member": {"username": "maker"},
            }
        ])

        items = fetch({"lookback_hours": 999999, "nodes": [{"name": "programmer", "strict": True}]}, http)

        self.assertEqual(http.calls, [(API, {"node_name": "programmer"})])
        self.assertEqual(len(items), 1)
        item = items[0]
        self.assertEqual(item.url, "https://freight-ai.cn")
        self.assertEqual(item.title, "Freight Ai")
        self.assertEqual(item.extra["ecosystem"], "zh")
        self.assertEqual(item.extra["evidence_url"], "https://www.v2ex.com/t/101")
        self.assertEqual(item.extra["evidence_tier"], "independent")

    def test_strict_node_rejects_ai_discussion_without_a_launch_or_product_link(self) -> None:
        http = FakeHttp([
            {
                "id": 102,
                "title": "AI 模型哪个好用",
                "url": "https://www.v2ex.com/t/102",
                "content": "想讨论一下大模型。",
                "created": 1787500000,
            }
        ])

        self.assertEqual(fetch({"lookback_hours": 999999, "nodes": ["programmer"]}, http), [])
