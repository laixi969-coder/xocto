---
slug: eggshell
name: Eggshell
builder: Momo
category: 基础层
summary_zh: 开发者在搭建需要反复调用模型的 agent 时，把历史任务记录交给 Eggshell，由它在本地保存并复用这些记忆，让 agent 不必每次从零重算，最终减少重复调用产生的 token
  消耗；具体记忆写入与复用流程仍待核验。
inspiration: 趋势是 agent 的长期记忆正从模型侧能力变成独立的一层基础设施。切入可考虑为特定行业 agent（如客服、法务检索）做带行业语料的记忆层，按节省的调用量或按席位收费，而不是做通用记忆组件。
summary_en: When developers build agents that repeatedly call models, they hand past task records to Eggshell,
  which stores and reuses that memory locally so the agent does not recompute from scratch, cutting token
  spend from repeated calls; the exact write and reuse flow still needs verification.
inspiration_en: The trend is that long-term agent memory is becoming its own infrastructure layer rather
  than a model-side feature. A wedge is to build memory layers with vertical corpora for specific agent
  types such as support or legal retrieval, charging by saved calls or seats instead of shipping a generic
  memory component.
priority_review: false
project_type: new_application
industries: []
industries_en: []
jobs:
- AI 应用开发者
jobs_en:
- AI application developers
regions: []
regions_en: []
open_source: false
url: https://www.producthunt.com/products/eggshell-2
canonical_url: https://producthunt.com/products/eggshell-2
summary: Local memory for AI agents to reuse work, spend fewer tokens
first_seen: '2026-09-12T11:59:22Z'
last_seen: '2026-09-19T00:21:15Z'
status: watching
sources:
- producthunt
sightings:
- source: producthunt
  url: https://www.producthunt.com/products/eggshell-2
  seen_at: '2026-09-19T00:21:15Z'
  metrics: {}
  kind: product
---

# Eggshell

Local memory for AI agents to reuse work, spend fewer tokens

## 笔记


