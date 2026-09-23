---
slug: jev-dsh-decision
name: jev-dsh-decision
builder: Devin-AXIS
category: AI + 开发
summary_zh: 开发者在给编码 agent 接入工具调用时安装这个插件，由它接收 agent 的上下文并输出结构化的决策结果，再交给 harness 执行；支持哪些 harness、决策结果如何被消费以及是否需要人工复核，公开材料只给出插件定位与仓库数据。
inspiration: 趋势是 agent 的工具选择环节开始被拆成可替换的独立组件，而不是绑死在某个 harness 里。切入可考虑为特定行业的 agent 提供带合规或审计约束的决策层，例如金融或医疗场景下必须留痕的动作选择，按部署或调用量收费。
summary_en: Developers install this plugin when wiring tool calling into coding agents; it takes the agent's
  context and returns structured decisions for the harness to execute. Which harnesses are supported,
  how decisions are consumed and whether human review is required are only partially covered by the plugin
  positioning and repository data.
inspiration_en: The trend is that the tool-selection step of agents is being split into replaceable standalone
  components rather than being locked into one harness. A wedge is to offer a decision layer with compliance
  or audit constraints for agents in specific industries, such as traceable action selection in finance
  or healthcare, charging per deployment or per call.
priority_review: false
project_type: open_source
industries:
- 软件与信息技术服务
industries_en:
- Software and IT services
jobs:
- 开发者在给编码 agent 接入工具调用时，需要让 agent 在多个动作之间做出可解释的选择
jobs_en:
- Developers wiring tool calling into coding agents need the agent to make explainable choices among multiple
  actions
regions: []
regions_en: []
open_source: true
url: https://github.com/Devin-AXIS/jev-dsh-decision
canonical_url: https://github.com/Devin-AXIS/jev-dsh-decision
summary: Jev DSH 决策引擎｜面向 Agent Harness 的结构化决策插件。原生支持 DeepSeek Harness，通过 iPolloWork 支持 OpenCode、Codex
  Harness。
first_seen: '2026-09-20T04:39:05Z'
last_seen: '2026-09-23T00:34:19Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/Devin-AXIS/jev-dsh-decision
  seen_at: '2026-09-23T00:34:19Z'
  metrics:
    stars: 111
    forks: 39
    open_issues: 1
  kind: product
---

# jev-dsh-decision

Jev DSH 决策引擎｜面向 Agent Harness 的结构化决策插件。原生支持 DeepSeek Harness，通过 iPolloWork 支持 OpenCode、Codex Harness。

## 笔记


