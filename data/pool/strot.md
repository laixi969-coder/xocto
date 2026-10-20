---
slug: strot
name: Strot
builder: solohunter001
category: 基础层
summary_zh: 开发者把大模型的决策意图一次性编译，之后在本地运行判断，减少每次决策都调用模型；用户拿到的是可本地执行的决策逻辑。具体编译对象、支持的任务类型与准确率取舍，公开材料未说明，具体流程或交付仍待核验。
inspiration: 趋势是推理成本从按次调用转向一次性编译加本地执行，可能改变高频决策类应用的毛利结构。切入可考虑规则稳定、调用频繁的场景，如客服分流或风控初筛；目前只有一句仓库说明，尚无实测数据。
summary_en: Developers compile an LLM's decision intent once and then run decisions locally, avoiding
  a model call per decision; the user gets decision logic executable on-device. What exactly is compiled,
  which task types are supported, and the accuracy trade-off are not described publicly, so the concrete
  workflow and delivery remain to be verified.
inspiration_en: The trend is inference cost shifting from per-call usage to one-time compilation plus
  local execution, which could change the margin structure of high-frequency decision apps. An entry point
  could be stable, frequently called scenarios such as support triage or first-pass risk screening; today
  there is only a one-line repository description and no measured results.
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs:
- 开发者把大模型的决策意图一次性编译，之后在本地执行判断以降低调用成本
jobs_en:
- Developers compile an LLM's decision intent once and then run decisions locally to cut call costs
regions: []
regions_en: []
open_source: true
url: https://github.com/strot-ai/Project-STROT
canonical_url: https://github.com/strot-ai/Project-STROT
summary: Compile an LLM's intent once, run decisions locally
first_seen: '2026-10-20T01:06:26Z'
last_seen: '2026-10-20T01:06:26Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://github.com/strot-ai/Project-STROT
  seen_at: '2026-10-20T01:06:26Z'
  metrics:
    points: 23
    comments: 12
  kind: product
---

# Strot

Compile an LLM's intent once, run decisions locally

## 笔记


