---
slug: kru
name: kru
builder: omaekumiko2-create
category: AI + 开发
summary_zh: 开发者在让 AI 代理跑需要登录或调用接口的任务时，原本要把密钥写进环境变量或配置文件，等于把明文交给模型和日志；kru 以本地优先的 MCP 凭据管理器接收这些密码、API key、SSH
  身份与 TOTP，让代理在任务中调用而不把隐藏明文暴露给模型。用户拿到的是代理可用的凭据调用能力，具体接入方式与人工确认边界仍待核验。
inspiration: 趋势：代理开始真正动手执行任务后，凭据从“人保管”变成“机器要用”，密钥管理这一层被重新拆开做。切入：从已经在跑代理自动化、又不敢把生产密钥交给模型的开发团队进入，卖点是不改代理逻辑就能安全取用凭据；开源仓库可走托管版或团队审计收费，但公开材料未披露任何定价。
summary_en: When developers let an AI agent run tasks that need logins or API calls, they normally put
  secrets in environment variables or config files, handing plaintext to the model and logs; kru is a
  local-first MCP credential manager that takes those passwords, API keys, SSH identities and TOTP so
  the agent can use them without exposing hidden plaintext to the model. The user gets credential access
  usable by the agent; the exact integration path and human confirmation boundary still need verification.
inspiration_en: 'Trend: once agents actually execute tasks, credentials shift from human-held to machine-used,
  and the secrets layer is being rebuilt around that. Entry: start with dev teams already running agent
  automation who will not hand production keys to a model, selling credential access without rewriting
  agent logic; an open-source repo could charge for a hosted or team-audit tier, but no pricing is disclosed.'
priority_review: false
project_type: open_source
industries:
- 软件开发
- 信息安全
industries_en:
- Software development
- Information security
jobs:
- 开发者在让 AI 代理执行需要凭据的任务时，为其提供密码、API key、SSH 身份与 TOTP 而不把明文暴露给模型
jobs_en:
- Developers supplying passwords, API keys, SSH identities and TOTP to an AI agent running credentialed
  tasks without exposing plaintext to the model
regions: []
regions_en: []
open_source: true
url: https://github.com/omaekumiko2-create/kru
canonical_url: https://github.com/omaekumiko2-create/kru
summary: Local-first MCP password and credential manager for AI agents. Use passwords, API keys, SSH identities,
  and TOTP without exposing hidden plaintext to the model.
first_seen: '2026-08-24T21:23:11Z'
last_seen: '2026-09-10T05:13:28Z'
status: queued
sources:
- github
sightings:
- source: github
  url: https://github.com/omaekumiko2-create/kru
  seen_at: '2026-09-10T05:13:28Z'
  metrics:
    stars: 125
    forks: 6
    open_issues: 0
  kind: product
---

# kru

Local-first MCP password and credential manager for AI agents. Use passwords, API keys, SSH identities, and TOTP without exposing hidden plaintext to the model.

## 笔记


