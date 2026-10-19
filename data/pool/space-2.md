---
slug: space-2
name: SPACE
builder: perplexityai
category: 基础层
summary_zh: 平台或后端工程师在自建 agent 执行环境时，把 agent 生成的代码和用户提交的代码交给 SPACE，由可插拔运行时在隔离沙箱里跑完并回传结果；交付物是隔离执行能力本身，不是面向终端用户的成品，具体接入流程与运维边界仍待核验。
inspiration: 趋势：agent 写代码、跑代码正在从演示走向生产，隔离执行从附属组件变成必须自建的一层。切入：不要做通用沙箱，而是绑定一类受监管或高敏感场景（如金融、医疗数据处理），把审计日志、数据不出域和配额计费一起交付，按执行时长或任务数收费。
summary_en: Platform or backend engineers building self-hosted agent execution environments hand agent-generated
  and user-submitted code to SPACE, which runs it in isolated sandboxes via pluggable runtimes and returns
  results; the deliverable is isolated execution capability rather than an end-user product, and the concrete
  integration and operational boundaries still need verification.
inspiration_en: 'Trend: agents writing and running code are moving from demos into production, so isolated
  execution is becoming a layer teams must build themselves. Entry: avoid a generic sandbox and bind to
  a regulated or high-sensitivity setting such as financial or medical data processing, shipping audit
  logs, data-residency guarantees and quota billing together, charged by execution time or task count.'
priority_review: false
project_type: open_source
industries:
- 软件开发
- 云计算
industries_en:
- Software Development
- Cloud Computing
jobs:
- 平台工程师在自建 agent 执行环境时，处理不可信代码与工具调用，需要隔离运行并回收结果
jobs_en:
- Platform engineers building self-hosted agent execution environments handle untrusted code and tool
  calls, needing isolated runs and retrievable results
regions:
- 美国
regions_en:
- United States
open_source: true
url: https://github.com/perplexityai/SPACE
canonical_url: https://github.com/perplexityai/SPACE
summary: 'Sandboxed Platform for Agentic Code Execution: pluggable-runtime sandboxes for running agent
  and user code in isolation.'
first_seen: '2026-10-16T00:25:17Z'
last_seen: '2026-10-19T00:13:37Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/perplexityai/SPACE
  seen_at: '2026-10-19T00:13:37Z'
  metrics:
    stars: 1543
    forks: 125
    open_issues: 98
  kind: product
---

# SPACE

Sandboxed Platform for Agentic Code Execution: pluggable-runtime sandboxes for running agent and user code in isolation.

## 笔记


