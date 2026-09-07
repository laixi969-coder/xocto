from __future__ import annotations

import gzip
import tempfile
import unittest
from pathlib import Path

from xocto.cases import (
    CaseStudy,
    _story_item,
    _trustmrr_items,
    _validate,
    case_study_from_dict,
    collect_cases,
    load_settings,
)
from xocto.models import RawItem
from xocto.store import Store


def _raw_case(slug: str = "expandi") -> RawItem:
    return RawItem(
        source="casestudies",
        external_id=f"starterstory:{slug}",
        title="How Expandi Grew",
        url=f"https://www.starterstory.com/stories/{slug}",
        summary="LinkedIn automation SaaS",
        published_at="",
        collected_at="2026-09-06T00:00:00Z",
        metrics={},
        extra={
            "kind": "casestudy",
            "case_kind": "story",
            "case_slug": slug,
            "case_site": "starterstory",
            "evidence_level": "interviewed",
        },
        payload={"text": "interview body"},
    )


class StoryItemTests(unittest.TestCase):
    def test_story_item_extracts_title_text_and_evidence_level(self) -> None:
        page = (
            "<html><head><title>How Expandi Grew - Starter Story</title>"
            '<meta property="og:description" content="A LinkedIn automation story"></head>'
            "<body><script>var tracking = 1;</script>"
            + "<p>nav junk " * 30
            + "<article>The interview body about cold outreach</article></body></html>"
        )
        item = _story_item("expandi", "https://www.starterstory.com/stories/expandi", page, "2026-09-06T00:00:00Z")
        self.assertEqual(item.source, "casestudies")
        self.assertEqual(item.external_id, "starterstory:expandi")
        self.assertEqual(item.title, "How Expandi Grew")
        self.assertEqual(item.extra["evidence_level"], "interviewed")
        self.assertNotIn("tracking", item.payload["text"])
        self.assertIn("interview body", item.payload["text"])

    def test_story_item_title_survives_entities(self) -> None:
        page = "<html><head><title>BrüMate &amp; Cold Starts &#8212; Starter Story</title></head><body></body></html>"
        item = _story_item("brumate", "https://www.starterstory.com/stories/brumate", page, "2026-09-06T00:00:00Z")
        self.assertIn("BrüMate", item.title)


TRUSTMRR_LD = """
<script type="application/ld+json">
[{"position":1,"url":"https://trustmrr.com/startup/gumroad","item":{"@type":"Organization",
"name":"Gumroad","url":"https://trustmrr.com/startup/gumroad","description":"Go from 0 to $1",
"additionalProperty":[{"@type":"PropertyValue","name":"Verified GMV, last 30 days","value":7143937.99,"unitText":"USD"},
{"@type":"PropertyValue","name":"Verified total revenue","value":878595860.5,"unitText":"USD"}]}}]
</script>
<script type="application/ld+json">
{"@type":"Organization","name":"Chatbase","url":"https://trustmrr.com/startup/chatbase",
"additionalProperty":[{"@type":"PropertyValue","name":"Verified GMV, last 30 days","value":91000}]}
</script>
"""


class TrustMrrTests(unittest.TestCase):
    def test_parses_nested_and_flat_orgs_with_verified_monthly(self) -> None:
        items = _trustmrr_items(TRUSTMRR_LD, max_startups=10, collected_at="2026-09-06T00:00:00Z")
        self.assertEqual(len(items), 2)
        gumroad = items[0]
        self.assertEqual(gumroad.external_id, "trustmrr:gumroad")
        self.assertEqual(gumroad.metrics["monthly_revenue_usd"], 7143938)
        self.assertEqual(gumroad.extra["evidence_level"], "stripe_verified")

    def test_respects_max_startups(self) -> None:
        items = _trustmrr_items(TRUSTMRR_LD, max_startups=1, collected_at="2026-09-06T00:00:00Z")
        self.assertEqual(len(items), 1)


class ValidateTests(unittest.TestCase):
    def test_publish_requires_verdict_and_summary(self) -> None:
        ok = {
            "publish": True, "verdict": "real", "ai_relevance": "high",
            "summary_zh": "一条 LinkedIn 自动化 SaaS", "verdict_reason_zh": "替代手工加好友",
        }
        self.assertEqual(_validate(ok), "")
        missing = dict(ok, summary_zh="")
        self.assertIn("summary_zh", _validate(missing))
        bad_verdict = dict(ok, verdict="maybe")
        self.assertIn("verdict", _validate(bad_verdict))
        self.assertEqual(_validate({"publish": False}), "")


class StoreRoundtripTests(unittest.TestCase):
    def test_case_study_survives_save_load_and_keeps_notes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            case = CaseStudy(
                slug="expandi", name="Expandi", url="https://www.starterstory.com/stories/expandi",
                source="starterstory", evidence_level="interviewed", status="published",
                name_zh="扩展家", monthly_revenue_usd=60000.0,
                revenue_note_zh="创始人自报，未经审计", revenue_note_en="Founder self-reported, unaudited",
                verdict="real", ai_relevance="high",
                channels=("LinkedIn",), first_seen="2026-09-06T00:00:00Z", last_seen="2026-09-06T00:00:00Z",
                texts={"summary_zh": "LinkedIn 自动化 SaaS", "playbooks_zh": "自动化冷启动\n联盟计划"},
            )
            store.save_case_study(case)
            # 手写笔记不被机器覆盖
            path = store.case_path("expandi")
            path.write_text(path.read_text(encoding="utf-8").replace("## 笔记\n\n", "## 笔记\n\n我的批注\n"))
            loaded = store.load_case_study("expandi")
            assert loaded is not None
            self.assertEqual(loaded.monthly_revenue_usd, 60000.0)
            self.assertEqual(loaded.text("summary", "zh"), "LinkedIn 自动化 SaaS")
            self.assertEqual(loaded.text_list("playbooks", "zh"), ["自动化冷启动", "联盟计划"])
            self.assertIn("我的批注", loaded.notes)
            # 双语缺英文时退回中文
            self.assertEqual(loaded.text("summary", "en"), "LinkedIn 自动化 SaaS")

    def test_iter_filters_by_status(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            published = CaseStudy(
                slug="a", name="A", url="https://example.com/a", source="starterstory",
                evidence_level="interviewed", status="published",
            )
            rejected = CaseStudy(
                slug="b", name="B", url="https://example.com/b", source="starterstory",
                evidence_level="interviewed", status="rejected",
            )
            store.save_case_study(published)
            store.save_case_study(rejected)
            self.assertEqual([c.slug for c in store.iter_case_studies(status="published")], ["a"])


class _FakeHttp:
    """最小 Http 桩：sitemap 返回压缩包，正文页返回固定 HTML。"""

    def __init__(self, story_urls: list[str], pages: dict[str, str], home: str = "") -> None:
        locs = "".join(f"<loc>{url}</loc>" for url in story_urls)
        self._gz = gzip.compress(f"<urlset>{locs}</urlset>".encode("utf-8"))
        self._pages = pages
        self._home = home
        self.requested: list[str] = []

    def get_bytes(self, url: str, **_: object) -> bytes:
        self.requested.append(url)
        return self._gz

    def get_text(self, url: str, **_: object) -> str:
        self.requested.append(url)
        if url in self._pages:
            return self._pages[url]
        if url == "https://trustmrr.com/":
            return self._home
        raise AssertionError(f"意外的请求 {url}")


class CollectCasesTests(unittest.TestCase):
    def _settings(self) -> dict:
        return {
            "enabled": True, "first_run_max": 2, "max_pages_per_run": 1,
            "request_interval_seconds": 0.0, "enrich_limit_per_run": 5,
            "starterstory": {"enabled": True},
            "trustmrr": {"enabled": False, "max_startups": 5},
        }

    def test_first_run_respects_budget_and_manifest_makes_next_run_incremental(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            urls = [f"https://www.starterstory.com/stories/case-{i}" for i in range(3)]
            pages = {
                url: (
                    f"<html><head><title>Case {i}</title></head><body>"
                    + "<p>nav </p>" * 40
                    + f"<p>story body {i}</p></body></html>"
                )
                for i, url in enumerate(urls)
            }
            http = _FakeHttp(urls, pages)
            report = collect_cases(store, http=http, settings=self._settings())  # type: ignore[arg-type]
            self.assertEqual(report["starterstory"], 2)  # first_run_max
            self.assertEqual(report["new_items"], 2)
            day = store.raw_days()[-1]
            slugs = {
                item.extra.get("case_slug") for item in store.read_raw(day)
                if item.extra.get("kind") == "casestudy"
            }
            self.assertEqual(slugs, {"case-0", "case-1"})

            # manifest 记住了已抓的 URL：下一次只抓剩下那一篇
            report2 = collect_cases(store, http=http, settings=self._settings())  # type: ignore[arg-type]
            self.assertEqual(report2["starterstory"], 1)
            self.assertEqual(report2["starterstory_new"], 1)

    def test_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            urls = ["https://www.starterstory.com/stories/only"]
            pages = {urls[0]: "<html><head><title>Only</title></head><body><p>body</p></body></html>"}
            http = _FakeHttp(urls, pages)
            report = collect_cases(store, http=http, settings=self._settings(), dry_run=True)  # type: ignore[arg-type]
            self.assertEqual(report["new_items"], 1)
            self.assertEqual(store.raw_days(), [])
            self.assertEqual(store.read_case_manifest(), {})

    def test_disabled_settings_skip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            store.ensure_dirs()
            settings = self._settings() | {"enabled": False}
            report = collect_cases(store, http=_FakeHttp([], {}), settings=settings)  # type: ignore[arg-type]
            self.assertIn("skipped", report)


class CaseStudyFromDictTests(unittest.TestCase):
    def test_bilingual_fields_land_in_texts(self) -> None:
        front = {
            "slug": "x", "name": "X", "url": "https://example.com", "source": "starterstory",
            "evidence_level": "interviewed", "status": "published",
            "summary_zh": "中文", "summary_en": "English", "channels": ["SEO"],
            "monthly_revenue_usd": 12000,
        }
        case = case_study_from_dict("x", front, "notes here")
        self.assertEqual(case.text("summary", "zh"), "中文")
        self.assertEqual(case.text("summary", "en"), "English")
        self.assertEqual(case.channels, ("SEO",))
        self.assertEqual(case.notes, "notes here")

    def test_settings_defaults_when_config_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Store(Path(tmp))
            settings = load_settings(store)
            self.assertTrue(settings["enabled"])
            self.assertIn("max_pages_per_run", settings)


if __name__ == "__main__":
    unittest.main()
