---
slug: agent-safe-pipeline
name: agent-safe-pipeline
builder: decionis
category: 基础层
summary_zh: AI只能提出要做什么，真正动手必须等人点头并拿到一次性授权
inspiration: 趋势是AI提议、人拍板会变成高风险自动化的标配。切入是先做付款、发货、改权限这类点错一次就赔钱的环节，把审批做成绕不过去的闸，而不是事后再看日志。
summary_en: AI can only propose an action; a person must approve it and issue a one-time go-ahead before
  anything runs.
inspiration_en: The trend is propose-then-approve becoming the default for high-risk automation. The entry
  is payments, shipping, and permission changes, where one tap costs money; make approval a gate you cannot
  skip, not a log you read later.
priority_review: false
project_type: ''
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: false
url: https://decionis.com/docs?utm_source=github&utm_medium=org_readme&utm_campaign=dev_discovery
canonical_url: https://decionis.com/docs
summary: Reference architecture for AI agents that propose actions but cannot authorize them — immutable
  intent capture, an independent Decionis policy verdict (ALLOW/ESCALATE/BLOCK), verified human approval,
  and a SafeExecutor that consumes a single-use intent-bound grant.
first_seen: '2026-08-13T21:36:19Z'
last_seen: '2026-08-28T06:07:21Z'
status: queued
sources:
- github
sightings:
- source: github
  url: https://decionis.com/docs?utm_source=github&utm_medium=org_readme&utm_campaign=dev_discovery
  seen_at: '2026-08-28T06:07:21Z'
  metrics:
    stars: 530
    forks: 58
    open_issues: 13
- source: github
  url: https://www.decionis.com
  seen_at: '2026-08-28T06:07:21Z'
  metrics:
    stars: 165
    forks: 0
    open_issues: 10
---

# agent-safe-pipeline

Reference architecture for AI agents that propose actions but cannot authorize them — immutable intent capture, an independent Decionis policy verdict (ALLOW/ESCALATE/BLOCK), verified human approval, and a SafeExecutor that consumes a single-use intent-bound grant.

## 笔记


