from __future__ import annotations

import unittest

from xocto.sources.modelscope import API, fetch


class FakeHttp:
    def __init__(self, payload: dict) -> None:
        self.payload = payload
        self.calls: list[tuple[str, dict]] = []

    def get_json(self, url: str, *, params: dict) -> dict:
        self.calls.append((url, params))
        return self.payload


class ModelScopeTests(unittest.TestCase):
    def test_recent_open_source_model_with_adoption_signal_is_collected_as_chinese_ecosystem(self) -> None:
        http = FakeHttp({"data": {"models": [{
            "id": "maker/freight-ai", "display_name": "Freight AI", "description": "Freight exception model.",
            "created_at": "2026-08-22T10:00:00Z", "likes": 5, "downloads": 120,
        }]}})

        items = fetch({"lookback_hours": 999999, "limit": 10, "min_likes": 3, "min_downloads": 25}, http)

        self.assertEqual(http.calls, [(API, {"PageNumber": 1, "PageSize": 10})])
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].url, "https://modelscope.cn/models/maker/freight-ai")
        self.assertEqual(items[0].extra["ecosystem"], "zh")
        self.assertEqual(items[0].metrics["downloads"], 120)

    def test_low_signal_model_is_not_collected(self) -> None:
        http = FakeHttp({"data": {"models": [{
            "id": "maker/experiment", "created_at": "2026-08-22T10:00:00Z", "likes": 0, "downloads": 1,
        }]}})
        self.assertEqual(fetch({"lookback_hours": 999999}, http), [])
