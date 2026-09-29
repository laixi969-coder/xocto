---
slug: collabosm
name: collabosm
builder: architectds
category: 基础层
summary_zh: 开发者在本地打开它，用自己的 Colab 账号租一块 GPU 跑 Qwen 等开源模型，启动前先看到费用，再通过本地 /v1 接口供 Codex 或任意 OpenAI 客户端调用；用户拿到的是可调用的本地推理端点，具体计费与稳定性仍待核验。
inspiration: 趋势：推理成本成为应用方的核心变量，个人开发者开始把闲置算力账户变成自有推理端点。切入：面向预算敏感的小团队做按用量结算的托管推理，卖点是费用可预期而非模型能力。
summary_en: A developer opens it locally, rents a GPU inside their own Colab account to serve open models
  such as Qwen, sees the cost before start, and exposes a local /v1 endpoint for Codex or any OpenAI client;
  the deliverable is a callable local inference endpoint, with billing and reliability still to verify.
inspiration_en: 'Trend: inference cost is becoming the core variable for application builders, and individual
  developers are turning idle compute accounts into their own endpoints. Entry: offer usage-metered hosted
  inference to budget-sensitive small teams, selling predictable cost rather than model capability.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 开发者在自有 Colab 账号上租用 GPU 并本地调用开源模型
jobs_en:
- Developers renting a GPU in their own Colab account to serve open models locally
regions: []
regions_en: []
open_source: true
url: https://github.com/architectds/collabosm
canonical_url: https://github.com/architectds/collabosm
summary: 'A local app that rents a GPU in your own Colab account and serves Qwen3.8 on it: 27B on an A100-40G,
  or Flash-Next (125B-A6B MoE) on an A100-80G. The cost is shown before it starts; chat with images; Codex
  or any OpenAI client uses a fixed local /v1. Auto-stop, CU ledger, live prefill/decode. Windows, macOS,
  Linux.'
first_seen: '2026-09-25T00:46:02Z'
last_seen: '2026-09-29T01:57:46Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/architectds/collabosm
  seen_at: '2026-09-29T01:57:46Z'
  metrics:
    stars: 89
    forks: 2
    open_issues: 0
  kind: product
---

# collabosm

A local app that rents a GPU in your own Colab account and serves Qwen3.8 on it: 27B on an A100-40G, or Flash-Next (125B-A6B MoE) on an A100-80G. The cost is shown before it starts; chat with images; Codex or any OpenAI client uses a fixed local /v1. Auto-stop, CU ledger, live prefill/decode. Windows, macOS, Linux.

## 笔记


