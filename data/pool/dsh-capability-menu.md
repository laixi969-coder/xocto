---
slug: dsh-capability-menu
name: dsh-capability-menu
builder: PKUfudawei
category: 基础层
summary_zh: 为代理配置 MCP 工具与技能的开发者在搭建 DeepSeek Harness 时打开它：它把每个工具或技能按 Exposed、Progressive、Blocked 三档设置暴露程度与执行方式，用户拿到的是受控的能力清单与更小的上下文占用。它是否真的降低上下文成本、三档如何影响执行，公开材料未给出实测，具体效果待核验。
inspiration: 趋势：代理能力越多，上下文预算越像稀缺资源，“哪些工具此刻可见”正在变成需要显式管理的配置项。切入：可从代理平台的上下文治理环节进入，做面向团队的能力开关与配额管理，按席位或按调用量收费；也可先服务自建代理、对上下文成本敏感的基础设施团队。价格未披露，不能预设。
summary_en: 'A developer configuring MCP tools and skills for an agent opens it while setting up DeepSeek
  Harness: it sets each tool or skill to Exposed, Progressive or Blocked to control exposure and execution
  mode, so the user gets a governed capability list and a smaller context footprint. Whether it actually
  lowers context cost and how the tiers affect execution are not backed by public measurements; the concrete
  effect needs verification.'
inspiration_en: 'Trend: as agents gain more capabilities, context budget becomes a scarce resource, and
  "which tools are visible right now" turns into a configuration item that must be managed explicitly.
  Entry: start at context governance for agent platforms, offering team-facing capability switches and
  quotas priced per seat or per call, or first serve infrastructure teams building their own agents that
  are sensitive to context cost. No price is disclosed, so none should be assumed.'
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs:
- 为代理配置 MCP 工具与技能的开发者在上下文预算内决定哪些能力可用
jobs_en:
- Developers configuring MCP tools and skills for an agent who decide which capabilities are available
  within a context budget
regions: []
regions_en: []
open_source: true
url: https://github.com/PKUfudawei/dsh-capability-menu
canonical_url: https://github.com/PKUfudawei/dsh-capability-menu
summary: 'Unified capability menu for DeepSeek Harness: manage exposure level (context footprint) and
  execution mode of MCP tools & skills via Exposed/Progressive/Blocked tiers.'
first_seen: '2026-08-19T06:30:08Z'
last_seen: '2026-09-07T15:52:49Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/PKUfudawei/dsh-capability-menu
  seen_at: '2026-09-07T15:52:49Z'
  metrics:
    stars: 84
    forks: 1
    open_issues: 1
  kind: product
---

# dsh-capability-menu

Unified capability menu for DeepSeek Harness: manage exposure level (context footprint) and execution mode of MCP tools & skills via Exposed/Progressive/Blocked tiers.

## 笔记


