---
slug: openqodex
name: openqodex
builder: openqodex
category: AI + 开发
summary_zh: 开发者在把改动推送到仓库前，用 openqodex 对本次改动的代码行运行 SAST、密钥、依赖与 lint 扫描，再由一个独立审查进程逐条复核扫描发现，最终得到针对改动行的审查结论；仍需开发者自行判断是否采纳，误报率与人工确认比例仍待核验。
inspiration: 趋势是代码审查从人工评审转向“扫描器 + 模型复核”的组合，且发生在推送之前。切入可考虑面向中小工程团队，把安全与依赖检查打包成推送前的按仓库或按席位订阅，替代只在上线后才发现问题的旧流程；价格未披露，不预设。
summary_en: Before pushing changes to a repository, developers run openqodex to scan the changed lines
  with SAST, secrets, dependency and lint scanners, then a separate reviewer process rechecks each scanner
  finding, ending with review conclusions scoped to the changed lines; developers still decide whether
  to act, and false-positive rates and human confirmation ratios still need verification.
inspiration_en: The trend is code review shifting from manual reading to a scanner-plus-model combination
  that runs before push. A wedge is packaging security and dependency checks as a per-repository or per-seat
  pre-push subscription for small engineering teams, replacing a process that only surfaces problems after
  release; no pricing is disclosed and none is assumed.
priority_review: false
project_type: open_source
industries:
- 软件开发
- 信息安全
industries_en:
- software development
- information security
jobs:
- 提交代码前的开发者
- 负责代码安全审查的工程团队
jobs_en:
- developers preparing to push code
- engineering teams responsible for code security review
regions: []
regions_en: []
open_source: true
url: https://qodex.ai/openqodex
canonical_url: https://qodex.ai/openqodex
summary: Open source AI code review for Claude Code and Codex, before you push. Scanners (SAST, secrets,
  dependencies, lint) on the lines you changed, then a separate reviewer process that checks every scanner
  finding and is given every changed line. No other API key.
first_seen: '2026-10-02T06:19:06Z'
last_seen: '2026-10-10T01:46:04Z'
status: queued
sources:
- github
sightings:
- source: github
  url: https://qodex.ai/openqodex
  seen_at: '2026-10-10T01:46:04Z'
  metrics:
    stars: 508
    forks: 33
    open_issues: 24
  kind: product
---

# openqodex

Open source AI code review for Claude Code and Codex, before you push. Scanners (SAST, secrets, dependencies, lint) on the lines you changed, then a separate reviewer process that checks every scanner finding and is given every changed line. No other API key.

## 笔记


