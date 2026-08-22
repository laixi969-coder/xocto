from __future__ import annotations

from pathlib import Path
import unittest

import yaml


WORKFLOW = Path(__file__).parents[1] / ".github" / "workflows" / "daily.yml"


class DailyWorkflowTests(unittest.TestCase):
    def test_daily_run_is_timezoned_tokenized_and_health_checked(self) -> None:
        """防止自动更新在无意改工作流时退化成不定时、缩源或静默失败。"""
        payload = yaml.load(WORKFLOW.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        schedule = payload["on"]["schedule"][0]
        self.assertEqual(schedule["cron"], "17 6 * * *")
        self.assertEqual(schedule["timezone"], "Asia/Shanghai")

        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("GITHUB_TOKEN: ${{ github.token }}", text)
        self.assertIn("uv run xocto health", text)
        self.assertIn("uv run xocto brief", text)


if __name__ == "__main__":
    unittest.main()
