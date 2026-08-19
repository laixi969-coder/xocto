from __future__ import annotations

from datetime import datetime, timedelta, timezone
import unittest

from xocto.sources.huggingface import API, fetch


def recent_time() -> str:
    return (datetime.now(timezone.utc) - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S.000Z")


class FakeHttp:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict | None]] = []

    def get_json(self, url: str, *, params: dict | None = None, headers: dict | None = None):  # type: ignore[no-untyped-def]
        self.calls.append((url, params))
        if url == f"{API}/spaces":
            return [{
                "id": "octo/brief-maker",
                "author": "octo",
                "createdAt": recent_time(),
                "likes": 4,
                "tags": ["gradio", "text-generation"],
                "sdk": "gradio",
                "cardData": {"title": "Brief Maker", "short_description": "Turns notes into a concise brief."},
            }]
        if url == f"{API}/models":
            return [{
                "id": "octo/mini-model",
                "author": "octo",
                "createdAt": recent_time(),
                "likes": 8,
                "downloads": 120,
                "tags": ["text-generation", "transformers"],
                "cardData": {},
            }]
        return []


class HuggingFaceTests(unittest.TestCase):
    def test_public_spaces_and_models_become_product_candidates(self) -> None:
        http = FakeHttp()
        rows = fetch(
            {
                "lookback_hours": 72,
                "spaces": {"min_likes": 2},
                "models": {"min_likes": 5, "min_downloads": 50},
            },
            http,
        )
        self.assertEqual([item.external_id for item in rows], ["space:octo/brief-maker", "model:octo/mini-model"])
        self.assertTrue(all(item.extra["kind"] == "product" for item in rows))
        self.assertEqual(rows[1].summary, "Open model tags: text-generation, transformers")
        self.assertTrue(all(params and params["sort"] == "createdAt" for _, params in http.calls))

    def test_models_must_meet_both_community_thresholds(self) -> None:
        rows = fetch(
            {"models": {"min_likes": 9, "min_downloads": 50}, "spaces": {"enabled": False}},
            FakeHttp(),
        )
        self.assertEqual(rows, [])


if __name__ == "__main__":
    unittest.main()
