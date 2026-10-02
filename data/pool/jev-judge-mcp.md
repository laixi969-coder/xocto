---
slug: jev-judge-mcp
name: jev-judge-mcp
builder: PyModel
category: AI + 开发
summary_zh: jev-judge-mcp 为 MCP 智能体提供一组带类型的判断工具，覆盖校验、筛选、查找、分类、重排、决策、比较、抽取、复核、闸门和打分，由模型给出判断，再由策略决定自动通过、人工复核还是升级。公开材料未说明这些工具在真实业务中的准确率与人工复核比例，具体效果仍待核验。
inspiration: 趋势是智能体开始需要可配置的“判断层”，把模型输出与放行策略分开，而不是让模型直接决定动作。切入可以放在对错误放行代价高的环节，例如内容审核、理赔初筛、订单风控，卖的是策略配置与复核流程，而不是又一个模型调用封装。
summary_en: jev-judge-mcp provides typed judgment tools for MCP agents, covering verify, screen, find,
  classify, rerank, decide, compare, extract, review, gate, and score, where the model judges and a policy
  decides auto-approve, review, or escalate. The public material does not state accuracy or human-review
  rates in real business flows, so concrete results remain unverified.
inspiration_en: The trend is that agents increasingly need a configurable judgment layer that separates
  model output from release policy, instead of letting the model decide actions directly. Entry could
  be steps where a wrong release is costly, such as content moderation, insurance claim triage, or order
  risk control, selling policy configuration and review flow rather than another model-call wrapper.
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and information services
jobs:
- 构建 MCP 智能体的开发者在流程中需要对候选内容做校验、筛选、分类、排序或打分，并决定自动通过、人工复核还是升级处理
jobs_en:
- Developers building MCP agents who need to verify, screen, classify, rank, or score candidate content
  in a flow and decide whether to auto-approve, review, or escalate
regions: []
regions_en: []
open_source: true
url: https://github.com/PyModel/jev-judge-mcp
canonical_url: https://github.com/PyModel/jev-judge-mcp
summary: 'Typed judgment tools for MCP agents. TypeSafe''s Jev model as verify, screen, find, classify,
  rerank, decide, compare, extract, review, gate, and score: the model judges, policy decides auto, review,
  or escalate.'
first_seen: '2026-09-23T22:48:43Z'
last_seen: '2026-10-02T01:41:55Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/PyModel/jev-judge-mcp
  seen_at: '2026-10-02T01:41:55Z'
  metrics:
    stars: 84
    forks: 4
    open_issues: 1
  kind: product
---

# jev-judge-mcp

Typed judgment tools for MCP agents. TypeSafe's Jev model as verify, screen, find, classify, rerank, decide, compare, extract, review, gate, and score: the model judges, policy decides auto, review, or escalate.

## 笔记


