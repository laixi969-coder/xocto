---
slug: task-state-guard
name: task-state-guard
builder: MaxHu-xuan
category: AI + 开发
summary_zh: task-state-guard 是一个开源工具，面向使用 AI 编程代理的开发者，在代理任务因重启或超时中断后，用于核对和修复任务状态。它接收代理遗留的 SQLite 状态文件，预览待提交的数据库变更，关闭过期的交付状态，并明确标记未完成的任务，避免误判成功。具体工作流细节仍需进一步核验。
inspiration: AI 代理在长时间运行或中断后状态不一致是普遍痛点，此工具通过状态核对和预览机制降低风险。切入点是 AI 开发工具链的可靠性环节，可考虑与 CI/CD 集成或提供托管服务。
summary_en: task-state-guard is an open-source tool for developers using AI coding agents, used to reconcile
  and fix task states after agent tasks are interrupted by restarts or timeouts. It takes the agent's
  leftover SQLite state files, previews pending database changes, closes stale delivery states, and explicitly
  marks unfinished tasks to avoid false success. Specific workflow details still need verification.
inspiration_en: State inconsistency after long-running or interrupted AI agent tasks is a common pain
  point; this tool reduces risk through state reconciliation and preview mechanisms. The entry point is
  the reliability layer of AI development toolchains, potentially integrating with CI/CD or offering managed
  services.
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software Development
jobs:
- AI Agent 开发者
- DevOps 工程师
jobs_en:
- AI Agent Developers
- DevOps Engineers
regions: []
regions_en: []
open_source: true
url: https://github.com/MaxHu-xuan/task-state-guard
canonical_url: https://github.com/MaxHu-xuan/task-state-guard
summary: Reconcile stuck AI-agent tasks after restarts and timeouts. Preview SQLite changes, close stale
  delivery states, and never guess success.
first_seen: '2026-08-23T07:10:14Z'
last_seen: '2026-09-12T00:18:44Z'
status: queued
sources:
- github
sightings:
- source: github
  url: https://github.com/MaxHu-xuan/task-state-guard
  seen_at: '2026-09-12T00:18:44Z'
  metrics:
    stars: 290
    forks: 3
    open_issues: 0
  kind: product
---

# task-state-guard

Reconcile stuck AI-agent tasks after restarts and timeouts. Preview SQLite changes, close stale delivery states, and never guess success.

## 笔记


