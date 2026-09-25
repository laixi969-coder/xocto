---
slug: skillranker
name: skillranker
builder: Dicklesworthstone
category: AI + 开发
summary_zh: 使用编码代理的开发者在一轮会话中打开它，由 CLI 读取当前会话上下文，对可用技能排序并输出结构化 JSON，必要时弃权，用户据此决定下一步调用哪个技能；它依赖外部 API key，实际排序质量与本地反馈效果仍待核验。
inspiration: 趋势：代理能力从“模型自己选工具”转向外挂一层技能路由，把选择动作独立出来。切入：面向已经维护大量内部技能库的工程团队，做技能检索与弃权判断这一层；但依赖第三方 API key，且技能路由本身可能被模型厂商内置，窗口偏窄。
summary_en: Developers using coding agents open it mid-session; the CLI reads live session context, ranks
  available skills, emits structured JSON and can abstain, so the user can decide which skill to invoke
  next; it depends on an external API key and the real ranking quality and local feedback effect still
  need verification.
inspiration_en: 'Trend: agent capability is moving from the model picking tools itself to an external
  skill-routing layer that isolates the choice. Entry: target engineering teams already maintaining large
  internal skill libraries with a retrieval-and-abstention layer; but it depends on a third-party API
  key and model vendors may absorb skill routing, so the window is narrow.'
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software development
jobs:
- 使用编码代理的开发者在一轮会话中，处理当前上下文与可用技能列表，决定下一步调用哪个技能
jobs_en:
- Developers using coding agents, within a session, working from current context and an available skill
  list to decide which skill to invoke next
regions: []
regions_en: []
open_source: true
url: https://github.com/Dicklesworthstone/skillranker
canonical_url: https://github.com/Dicklesworthstone/skillranker
summary: Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live
  session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires
  a TypeSafe API key.
first_seen: '2026-09-17T06:58:19Z'
last_seen: '2026-09-25T00:33:47Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/Dicklesworthstone/skillranker
  seen_at: '2026-09-25T00:33:47Z'
  metrics:
    stars: 117
    forks: 8
    open_issues: 4
  kind: product
---

# skillranker

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

## 笔记


