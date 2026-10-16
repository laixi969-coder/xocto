---
slug: plan-or-retrieve-first-a-scale-study-of-tool-discovery-archi
name: Plan or Retrieve First? A Scale Study of Tool Discovery Architectures
builder: ''
category: ''
summary_zh: 该研究比较了工具增强型 LLM 智能体从大型 API 注册表中发现工具的两类架构：先检索后规划（RtP）与先规划后检索（PtR），后者让模型先生成抽象工具桩再作为检索查询。这为智能体在有限上下文窗口下接入大规模工具生态提供了可复用的架构参考，可能影响智能体工具发现环节的准确率与工程实现成本。
inspiration: ''
summary_en: 'The study compares two architectures for tool-augmented LLM agents to discover tools from
  large API registries: Retrieve-then-Plan (RtP) and Plan-then-Retrieve (PtR), in which the model first
  generates abstract tool stubs that serve as retrieval queries. It offers a reusable architectural reference
  for agents connecting to large tool ecosystems under finite context windows, potentially affecting accuracy
  and engineering cost in the tool-discovery stage of agents.'
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
url: https://machinelearning.apple.com/research/plan-retrieve-tool-discovery
canonical_url: https://machinelearning.apple.com/research/plan-retrieve-tool-discovery
summary: Tool-augmented LLM agents discover relevant APIs from large registries before planning execution,
  yet finite context windows prohibit injecting all tool definitions into a single prompt. The dominant
  approach, which we term Retrieve-then-Plan (RtP), embeds the user query and retrieves similar tools
  via approximate nearest-neighbor search. We study an alternative Plan-then-Retrieve (PtR) paradigm in
  which the LLM first generates Abstract Tool Stubs (hypothesized function signatures describing needed
  capabilities) which then serve as retrieval queries against the registry. Evaluating on…
first_seen: '2026-10-16T00:25:39Z'
last_seen: '2026-10-16T00:25:39Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://machinelearning.apple.com/research/plan-retrieve-tool-discovery
  seen_at: '2026-10-16T00:25:39Z'
  metrics: {}
  kind: news
---

# Plan or Retrieve First? A Scale Study of Tool Discovery Architectures

Tool-augmented LLM agents discover relevant APIs from large registries before planning execution, yet finite context windows prohibit injecting all tool definitions into a single prompt. The dominant approach, which we term Retrieve-then-Plan (RtP), embeds the user query and retrieves similar tools via approximate nearest-neighbor search. We study an alternative Plan-then-Retrieve (PtR) paradigm in which the LLM first generates Abstract Tool Stubs (hypothesized function signatures describing needed capabilities) which then serve as retrieval queries against the registry. Evaluating on…

## 笔记


