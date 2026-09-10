from __future__ import annotations

from pathlib import Path
import unittest

import yaml


WORKFLOW = Path(__file__).parents[1] / ".github" / "workflows" / "daily.yml"


class DailyWorkflowTests(unittest.TestCase):
    def test_daily_run_is_timezoned_tokenized_and_health_checked(self) -> None:
        """防止自动更新在无意改工作流时退化成不定时、缩源或静默失败。"""
        payload = yaml.load(WORKFLOW.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        schedules = payload["on"]["schedule"]
        self.assertEqual([item["cron"] for item in schedules], ["17 6 * * *"])
        self.assertTrue(all(item["timezone"] == "Asia/Shanghai" for item in schedules))

        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("GITHUB_TOKEN: ${{ github.token }}", text)
        self.assertIn("uv run xocto health", text)
        self.assertIn("uv run xocto brief", text)
        self.assertIn("uv run xocto market", text)
        self.assertIn("uv run xocto req", text)
        self.assertIn("if ! run_brief; then", text)
        self.assertIn("- name: 检查当日交付是否存在", text)
        self.assertIn('test -s "data/reports/$target_date.md"', text)
        self.assertIn('test -s "data/reports/en/$target_date.md"', text)
        self.assertIn("- name: 保存判断数据", text)
        self.assertIn("git add data/pool data/reports data/reviews data/markets data/evidence data/events", text)
        self.assertIn("id: market", text)
        self.assertIn("id: full_req", text)
        self.assertIn("- name: 检查判断链是否完整", text)
        self.assertRegex(
            text,
            r"- name: 检查采集有没有静默变质(?:\n\s+#.*)*\n\s+id: health\n\s+continue-on-error: true",
        )
        self.assertIn("steps.health.outcome", text)
        self.assertIn("steps.freshness.outcome", text)
        self.assertRegex(
            text,
            r"- name: 复算日报发布约束(?:\n\s+#.*)*\n\s+id: design\n\s+continue-on-error: true",
        )
        self.assertIn("steps.design.outcome", text)
        self.assertIn("if: ${{ always() }}", text)
        self.assertIn('commit_label="每日降级构建"', text)
        self.assertIn('steps.brief.outcome', text)


if __name__ == "__main__":
    unittest.main()
