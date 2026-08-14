from __future__ import annotations

from datetime import date
import unittest

from xocto.sources.github import API, ORGS_API, fetch


def harness_repo() -> dict:
    today = date.today().isoformat()
    return {
        "id": 123,
        "name": "deepseek-harness",
        "full_name": "deepseek-ai/deepseek-harness",
        "html_url": "https://github.com/deepseek-ai/deepseek-harness",
        "homepage": "",
        "description": "DeepSeek Harness: Everything is a Plugin.",
        "created_at": f"{today}T12:00:00Z",
        "pushed_at": f"{today}T13:00:00Z",
        "stargazers_count": 71000,
        "forks_count": 6000,
        "open_issues_count": 12,
        "owner": {"login": "deepseek-ai"},
        "topics": ["dsh", "dsh-plugin"],
        "language": "Python",
    }


class FakeHttp:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict | None]] = []

    def get_json(self, url: str, *, params: dict | None = None, headers: dict | None = None):  # type: ignore[no-untyped-def]
        self.calls.append((url, params))
        query = (params or {}).get("q", "")
        if url == API and ("topic:dsh" in query or query.startswith("created:")):
            return {"items": [harness_repo()]}
        if url == f"{ORGS_API}/deepseek-ai/repos":
            return [harness_repo()]
        return {"items": []}


class GithubDiscoveryTests(unittest.TestCase):
    def test_keyword_only_search_reproduces_official_release_miss(self) -> None:
        rows = fetch(
            {"queries": ["ai agent"], "created_within_days": 21, "min_stars": 40},
            FakeHttp(),
        )
        self.assertEqual(rows, [])

    def test_structured_discovery_marks_major_official_project_for_review(self) -> None:
        http = FakeHttp()
        rows = fetch(
            {
                "queries": ["ai agent"],
                "topics": ["dsh"],
                "created_within_days": 21,
                "min_stars": 40,
                "breakout": {"enabled": True, "within_days": 3, "min_stars": 5000},
                "official_organizations": ["deepseek-ai"],
            },
            http,
        )

        self.assertEqual(len(rows), 1)
        item = rows[0]
        self.assertEqual(item.title, "deepseek-harness")
        self.assertTrue(item.extra["priority_review"])
        self.assertEqual(
            item.extra["discovery_paths"],
            ["topic:dsh", "breakout", "official:deepseek-ai"],
        )
        self.assertTrue(
            any(url == API and params and params.get("per_page") == 100 for url, params in http.calls)
        )


if __name__ == "__main__":
    unittest.main()
