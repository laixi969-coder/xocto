---
slug: kenfold
name: kenfold
builder: jeonjw85
category: 基础层
summary_zh: 面向同时使用多个 AI 编码工具的开发者，提供可自托管的记忆服务，通过 MCP 在 Claude Code、Codex、OpenCode 和 ChatGPT 之间共享上下文。用户自行部署后，各工具读取同一份记忆，减少重复交代项目背景；具体存储格式、检索方式与冲突处理仍待核验。
inspiration: 趋势是编码助手从单一工具变成多工具并存，上下文因此被切碎在各自账号里，谁掌握跨工具的上下文层谁就掌握切换成本。切入不在做通用记忆中间件，而在垂直场景：例如外包团队或咨询公司按客户隔离记忆并做交付留痕，卖的是可审计的上下文资产，而不是又一个
  MCP 服务。
summary_en: For developers using several AI coding tools at once, it offers a self-hosted memory service
  that shares context across Claude Code, Codex, OpenCode and ChatGPT over MCP. After self-deployment,
  each tool reads the same memory, reducing repeated project briefing; the storage format, retrieval method
  and conflict handling still need verification.
inspiration_en: 'The trend is that coding assistants have gone from one tool to many coexisting tools,
  fragmenting context across separate accounts, so whoever owns the cross-tool context layer owns the
  switching cost. The opening is not generic memory middleware but vertical use: for example outsourcing
  or consulting teams isolating memory per client and keeping delivery trails, selling an auditable context
  asset rather than another MCP service.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 同时使用 Claude Code、Codex、ChatGPT 等多个 AI 编码工具的开发者，需要在切换工具时复用同一份项目上下文与历史记忆
jobs_en:
- Developers using several AI coding tools such as Claude Code, Codex and ChatGPT who need to reuse the
  same project context and history when switching tools
regions: []
regions_en: []
open_source: true
url: https://github.com/jeonjw85/kenfold
canonical_url: https://github.com/jeonjw85/kenfold
summary: Self-hosted memory server for AI agents. Share context across Claude Code, Codex, OpenCode, and
  ChatGPT over MCP.
first_seen: '2026-09-27T07:05:58Z'
last_seen: '2026-10-10T01:46:04Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/jeonjw85/kenfold
  seen_at: '2026-10-10T01:46:04Z'
  metrics:
    stars: 64
    forks: 1
    open_issues: 0
  kind: product
---

# kenfold

Self-hosted memory server for AI agents. Share context across Claude Code, Codex, OpenCode, and ChatGPT over MCP.

## 笔记


