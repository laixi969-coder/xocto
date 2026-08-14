from __future__ import annotations

import unittest

from xocto.i18n import ZH
from xocto.report import parse_report


class ReportParsingTests(unittest.TestCase):
    def test_inline_numbered_top_picks_become_separate_cards(self) -> None:
        report = """# AI 应用雷达 · 2026-08-14

## AI 应用雷达 · 2026-08-14

今天几乎所有候选都围绕 DeepSeek Harness 展开。

### 今天最值得看的3个

1. deepseek-harness：官方插件化框架。 2. dsh-tui：全屏终端插件。 3. dsh-workflow：可治理的工作流层。

### 其余入选清单

- other：另一项。
"""

        section = parse_report(report, ZH).sections[0]
        picks = section.picks

        self.assertEqual(
            [pick.name for pick in picks[:3]],
            ["deepseek-harness", "dsh-tui", "dsh-workflow"],
        )
        self.assertEqual(picks[0].rank, "01")
        self.assertNotIn("dsh-tui", picks[0].lead)
        self.assertEqual(picks[1].lead, "全屏终端插件。")
        self.assertIn("今天几乎所有候选", section.lead_html)


if __name__ == "__main__":
    unittest.main()
