---
slug: iq-routing
name: IQ Routing
builder: George Avila
category: 基础层
summary_zh: 面向构建多步 Agent 的开发者，在 Agent 执行轨迹变长、模型调用费用累积的工作节点上，IQ Routing 接收整条执行轨迹并据此选择调用哪个模型，最终交付的是被改写后的模型调用路径与随之下降的调用成本；具体路由策略、支持模型与计费方式仍待核验。
inspiration: 趋势：Agent 的成本结构正从单次调用转向整条轨迹的累积开销，按轨迹而非按单次请求做决策成为新的优化点。切入：可从客服、数据抓取、代码审查这类长链路 Agent 团队切入，按省下的调用成本分成或按轨迹量计费；但公开材料只有一句产品描述，尚无定价、客户或实测数据，窗口是否已关无法判断。
summary_en: For developers building multi-step agents, at the point where long execution trajectories
  pile up model-call costs, IQ Routing takes the whole trajectory as input and picks which model to call,
  delivering a rewritten call path and lower spend; routing policy, supported models and pricing still
  need verification.
inspiration_en: 'Trend: agent cost is shifting from single calls to cumulative spend across a whole trajectory,
  making trajectory-level routing a new optimization point. Entry: start with long-chain agent teams in
  support, scraping or code review, charging a share of saved spend or per trajectory; public material
  is one line only, so pricing, customers and timing remain unverified.'
priority_review: false
project_type: new_application
industries: []
industries_en: []
jobs:
- AI 应用开发者
- Agent 工程团队
jobs_en:
- AI application developers
- Agent engineering teams
regions: []
regions_en: []
open_source: false
url: https://www.producthunt.com/products/iq-routing
canonical_url: https://producthunt.com/products/iq-routing
summary: Trajectory-aware LLM routing that cuts agent cost
first_seen: '2026-08-27T06:54:14Z'
last_seen: '2026-08-28T06:07:17Z'
status: watching
sources:
- producthunt
sightings:
- source: producthunt
  url: https://www.producthunt.com/products/iq-routing
  seen_at: '2026-08-28T06:07:17Z'
  metrics: {}
  kind: product
---

# IQ Routing

Trajectory-aware LLM routing that cuts agent cost

## 笔记


