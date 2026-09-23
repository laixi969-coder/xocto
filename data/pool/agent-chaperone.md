---
slug: agent-chaperone
name: Agent Chaperone
builder: sepehrsafari
category: 基础层
summary_zh: 当团队把 AI agent 接入真实工具后，运维或安全工程师需要在 agent 每次调用工具、拿到返回结果时先做一遍筛查，避免越权操作或异常输出进入下游。Agent Chaperone
  宣称由 Jev 接收这些工具调用与结果并执行筛查动作，但筛查后输出什么、由谁确认、如何接入现有流程，公开材料均未说明，具体流程与交付仍待核验。
inspiration: 趋势是 agent 开始真正动手改数据、发请求，出错代价从“答错一句话”变成“改错一条记录”，于是调用前后的把关环节第一次被单独拆出来。切入可以放在对操作后果敏感的具体行业，例如电商后台改价、财务系统记账、医疗预约改期，把“哪些调用必须人工点确认、哪些可自动放行”做成可配置的规则，并按被拦截或放行的调用量收费；目前公开材料不足以判断它是否已经这样做。
summary_en: Once teams connect AI agents to real tools, operations or security engineers need to screen
  each tool call and its returned result before it reaches downstream systems, to avoid unauthorised actions
  or abnormal output. Agent Chaperone claims a component called Jev receives those tool calls and results
  and performs the screening, but what it outputs, who confirms it and how it plugs into existing workflows
  are not described in the public material; the concrete flow and deliverable remain unverified.
inspiration_en: The trend is that agents now actually change data and send requests, so the cost of an
  error shifts from a wrong sentence to a wrong record, and the checkpoint around each call is being split
  out as its own step. An entry point is to target industries where actions have consequences, such as
  repricing in e-commerce back offices, bookkeeping in finance systems or rescheduling in clinics, turning
  'which calls need human confirmation and which can pass automatically' into configurable rules and charging
  per intercepted or approved call; the public material is not enough to tell whether this project already
  does so.
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs:
- AI 应用运维工程师在 agent 上线前审查工具调用与返回结果
jobs_en:
- AI application operations engineers reviewing agent tool calls and results before release
regions: []
regions_en: []
open_source: true
url: https://github.com/agent-chaperone/agent-chaperone
canonical_url: https://github.com/agent-chaperone/agent-chaperone
summary: Screen AI agent tool calls and results with Jev
first_seen: '2026-09-21T16:34:27Z'
last_seen: '2026-09-23T00:34:15Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://github.com/agent-chaperone/agent-chaperone
  seen_at: '2026-09-23T00:34:15Z'
  metrics:
    points: 5
    comments: 0
  kind: product
---

# Agent Chaperone

Screen AI agent tool calls and results with Jev

## 笔记


