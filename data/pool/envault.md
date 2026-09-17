---
slug: envault
name: envault
builder: MildyNora
category: AI + 开发
summary_zh: 让编码智能体跑任务的工程师，在需要把 API key、数据库口令等密钥交给 AI 使用时打开这个本地加密保险库；它把密钥加密保存，智能体在调用外部服务时使用密钥但不读取明文，用户拿到的是可继续运行的编码流程和一份本地密钥存储。具体隔离机制与人工确认环节仍待核验。
inspiration: 趋势是编码智能体开始接触真实凭证，密钥暴露从人的问题变成机器的问题。切入可以从需要让 AI 代跑部署、调用第三方 API 的小团队做起，卖点是把密钥托管和智能体执行分开，而不是再做一个通用密码管理器。
summary_en: Engineers running coding agents open this local encrypted vault when they must hand API keys
  or database credentials to an AI; it stores secrets encrypted so the agent can use them to call external
  services without reading plaintext, leaving the user with a runnable coding flow and a local secret
  store. The isolation mechanism and human review steps still need verification.
inspiration_en: The trend is that coding agents now touch real credentials, turning key exposure from
  a human problem into a machine problem. A wedge is small teams that let AI run deployments or call third-party
  APIs, sold on separating secret custody from agent execution rather than building another general password
  manager.
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software Development
jobs:
- 后端工程师
- DevOps 工程师
jobs_en:
- Backend Engineer
- DevOps Engineer
regions: []
regions_en: []
open_source: true
url: https://github.com/MildyNora/envault
canonical_url: https://github.com/MildyNora/envault
summary: A local, minimum, encrypted secrets vault for coding agents — let your AI works with your keys
  and secret, but never sees them.
first_seen: '2026-08-28T03:52:41Z'
last_seen: '2026-09-17T00:32:43Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/MildyNora/envault
  seen_at: '2026-09-17T00:32:43Z'
  metrics:
    stars: 84
    forks: 10
    open_issues: 2
  kind: product
---

# envault

A local, minimum, encrypted secrets vault for coding agents — let your AI works with your keys and secret, but never sees them.

## 笔记


