from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from xocto.health import SEVERITY_DEAD, check
from xocto.models import RawItem, today
from xocto.store import Store


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

            dead = [item for item in findings if item.severity == SEVERITY_DEAD]
            self.assertEqual([item.source for item in dead], ["newssearch:China commercial"])


if __name__ == "__main__":
    unittest.main()
