---
slug: dotpals
name: dotpals
builder: Rikinshah787
category: AI + 开发
summary_zh: 使用编码代理的工程师在代理改完代码后打开它：它从代理输出里读取测试结果，标出被伪造或跳过的通过，并把 Claude Code 打回修复它改坏的部分，用户拿到的是对代理本次改动是否真的通过测试的判断，以及一个可供其他
  AI 工具查询的 MCP server。人工仍需确认修复结果，具体判定规则与误报情况待核验。
inspiration: 趋势：编码代理开始自己改代码后，“谁来验收代理的产出”成了新环节，测试结果本身也需要被怀疑。切入：可从代理产出的验收环节进入，做面向团队的“代理改动审计”，按仓库或按席位收费；也可先服务对测试可信度敏感的后端与基础设施团队。价格未披露，不能预设。
summary_en: 'An engineer using a coding agent opens it after the agent edits code: it reads test results
  from the agent''s output, flags faked or skipped passes, and sends Claude Code back to fix what it broke,
  so the user gets a judgement on whether this change really passed tests plus an MCP server other AI
  tools can query. A human still confirms the fix, and the exact detection rules and false-positive behaviour
  need verification.'
inspiration_en: 'Trend: once coding agents edit code themselves, verifying the agent''s output becomes
  a new step, and even test results have to be doubted. Entry: start at agent-output verification with
  team-facing "agent change audits", priced per repository or per seat, or first serve backend and infrastructure
  teams that care about test trustworthiness. No price is disclosed, so none should be assumed.'
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software development
jobs:
- 使用编码代理的工程师在代理改完代码后核对测试是否真的通过
jobs_en:
- Engineers using coding agents who check whether tests really pass after the agent edits code
regions: []
regions_en: []
open_source: true
url: https://dotpals.vercel.app
canonical_url: https://dotpals.vercel.app
summary: 'See what your coding agent actually did. A desktop pal and notch for Claude Code, Codex, Cursor,
  Gemini CLI and any agent: test results read from the output, faked passes caught, Claude Code sent back
  to fix what it broke, and an MCP server any AI tool can ask.'
first_seen: '2026-10-12T01:20:35Z'
last_seen: '2026-10-14T01:14:00Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://dotpals.vercel.app
  seen_at: '2026-10-14T01:14:00Z'
  metrics:
    stars: 42
    forks: 8
    open_issues: 2
  kind: product
---

# dotpals

See what your coding agent actually did. A desktop pal and notch for Claude Code, Codex, Cursor, Gemini CLI and any agent: test results read from the output, faked passes caught, Claude Code sent back to fix what it broke, and an MCP server any AI tool can ask.

## 笔记


