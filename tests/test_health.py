from __future__ import annotations

from datetime import timedelta
from pathlib import Path
import tempfile
import unittest

from xocto.health import SEVERITY_DEAD, SEVERITY_WARN, check
from xocto.models import RawItem, today
from xocto.store import Store


CONFIG = {
    "sources": {
        "newssearch": {"enabled": True, "queries": []},
        "github": {"enabled": True},
    }
}


def item(source: str, external_id: str, day) -> RawItem:
    return RawItem(
        source=source,
        external_id=external_id,
        title="t",
        url=f"https://example.com/{external_id}",
        summary="",
        published_at="",
        collected_at=f"{day.isoformat()}T00:00:00Z",
        metrics={},
        extra={"kind": "product"},
    )


class CoverageLaneHealthTests(unittest.TestCase):
    def test_one_healthy_search_market_does_not_hide_a_dead_market_lane(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            day = today()
            store.append_raw(
                [RawItem(
                    source="newssearch",
                    external_id="us-1",
                    title="US launch",
                    url="https://news.example/us",
                    summary="",
                    published_at="",
                    collected_at=f"{day.isoformat()}T00:00:00Z",
                    metrics={},
                    extra={"kind": "news", "query_lane": "US commercial"},
                )],
                day,
            )
            config = {
                "sources": {
                    "newssearch": {
                        "enabled": True,
                        "queries": [
                            {"name": "US commercial"},
                            {"name": "China commercial"},
                        ],
                    }
                }
            }

            findings = check(store, config, today=day)

            dead = [finding for finding in findings if finding.severity == SEVERITY_DEAD]
            self.assertEqual([finding.source for finding in dead], ["newssearch:China commercial"])


class DeadSourceTests(unittest.TestCase):
    def test_single_zero_day_after_yield_is_a_warning_not_death(self) -> None:
        # 低产源本来就有空窗日，一次瞬时拉取失败也不该把当天的定时任务染红。
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            day = today()
            store.append_raw([item("newssearch", "n-1", day)], day)
            store.append_raw(
                [item("github", "g-1", day - timedelta(days=1))], day - timedelta(days=1)
            )

            findings = check(store, CONFIG, today=day)

            dead = [finding for finding in findings if finding.severity == SEVERITY_DEAD]
            self.assertEqual(dead, [])
            github = next(finding for finding in findings if finding.source == "github")
            self.assertEqual(github.severity, SEVERITY_WARN)

    def test_two_consecutive_zero_days_are_a_dead_source(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            day = today()
            store.append_raw([item("newssearch", "n-1", day)], day)
            store.append_raw(
                [item("github", "g-1", day - timedelta(days=2))], day - timedelta(days=2)
            )

            findings = check(store, CONFIG, today=day)

            dead = [finding for finding in findings if finding.severity == SEVERITY_DEAD]
            self.assertEqual([finding.source for finding in dead], ["github"])


if __name__ == "__main__":
    unittest.main()
