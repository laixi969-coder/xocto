---
slug: shared-selective-persistent-memory-for-agentic-llm-systems
name: Shared Selective Persistent Memory
builder: ''
category: ''
summary_zh: 这是苹果公开的一项代理式 LLM 记忆架构研究，不是独立产品：它针对多轮工具调用生成代码时每轮会话丢弃配置、领域约束与数据模式的问题，提出选择性保留四类可复用上下文。对 AI 应用的含义是，代理类产品的上下文成本与生成稳定性可能因此改善，但该研究本身没有定价、客户或采用数据。
inspiration: ''
summary_en: 'This is an Apple research publication on a memory architecture for agentic LLM systems, not
  a standalone product: it targets the problem that multi-turn tool-using code generation discards configuration,
  domain constraints and data schemas each session, and proposes selectively retaining four categories
  of reusable context. For AI applications this implies possible improvements in context cost and generation
  stability for agent products, but the research itself has no pricing, customer or adoption data.'
inspiration_en: ''
priority_review: false
project_type: new_application
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: false
url: https://machinelearning.apple.com/research/shared-selective-persistent-memory
canonical_url: https://machinelearning.apple.com/research/shared-selective-persistent-memory
summary: 'Agentic LLM systems that generate code through multi-turn tool use face a fundamental context
  problem: each session starts from zero, discarding the configuration choices, domain constraints, data
  schemas, and tool-use patterns that made previous sessions productive. Naively persisting entire conversation
  histories is both token-inefficient and counterproductive—irrelevant context degrades generation quality.
  We introduce shared selective persistent memory, a memory architecture for agentic systems that identifies
  and retains four categories of reusable context—task specifications, data…'
first_seen: '2026-09-16T00:00:00Z'
last_seen: '2026-09-17T00:32:59Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://machinelearning.apple.com/research/shared-selective-persistent-memory
  seen_at: '2026-09-17T00:32:59Z'
  metrics: {}
  kind: news
---

# Shared Selective Persistent Memory

Agentic LLM systems that generate code through multi-turn tool use face a fundamental context problem: each session starts from zero, discarding the configuration choices, domain constraints, data schemas, and tool-use patterns that made previous sessions productive. Naively persisting entire conversation histories is both token-inefficient and counterproductive—irrelevant context degrades generation quality. We introduce shared selective persistent memory, a memory architecture for agentic systems that identifies and retains four categories of reusable context—task specifications, data…

## 笔记


