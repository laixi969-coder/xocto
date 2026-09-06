---
slug: task-state-guard
name: task-state-guard
builder: MaxHu-xuan
category: AI + 开发
summary_zh: 面向运行 AI 代理的团队，处理代理任务在重启或超时后卡死的问题。它接收代理的任务状态和 SQLite 变更记录，预览待提交的数据库改动，关闭过期的交付状态，避免代理误判成功。最终交付是任务状态的一致性和可审计的数据库变更预览，人工仍可确认后再提交。
inspiration: AI 代理从演示走向生产时，状态一致性和失败恢复成为基础设施刚需。切入点是代理运行平台和运维工具，可围绕状态机、审计日志和可回滚交付做产品化，而非仅提供代码库。
summary_en: For teams running AI agents, this tool handles tasks stuck after restarts or timeouts. It
  ingests agent task states and SQLite change logs, previews pending database modifications, and closes
  stale delivery states to prevent agents from falsely reporting success. The final output is consistent
  task state and auditable database change previews, with human confirmation before commit.
inspiration_en: As AI agents move from demo to production, state consistency and failure recovery become
  infrastructure necessities. The entry point is agent operation platforms and tooling, productizing around
  state machines, audit logs, and reversible delivery rather than just a code library.
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software Development
jobs:
- AI 代理运维工程师
- 平台工程师
jobs_en:
- AI Agent Operations Engineer
- Platform Engineer
regions:
- 全球
regions_en:
- Global
open_source: true
url: https://github.com/MaxHu-xuan/task-state-guard
canonical_url: https://github.com/MaxHu-xuan/task-state-guard
summary: Reconcile stuck AI-agent tasks after restarts and timeouts. Preview SQLite changes, close stale
  delivery states, and never guess success.
first_seen: '2026-08-23T07:10:14Z'
<<<<<<< HEAD
last_seen: '2026-09-06T15:05:43Z'
=======
last_seen: '2026-09-06T15:19:33Z'
>>>>>>> a677347 (chore: 每日采集 2026-09-06)
status: queued
sources:
- github
sightings:
- source: github
  url: https://github.com/MaxHu-xuan/task-state-guard
<<<<<<< HEAD
  seen_at: '2026-09-06T15:05:43Z'
=======
  seen_at: '2026-09-06T15:19:33Z'
>>>>>>> a677347 (chore: 每日采集 2026-09-06)
  metrics:
    stars: 200
    forks: 3
    open_issues: 0
  kind: product
---

# task-state-guard

Reconcile stuck AI-agent tasks after restarts and timeouts. Preview SQLite changes, close stale delivery states, and never guess success.

## 笔记


