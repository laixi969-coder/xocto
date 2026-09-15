---
slug: codex-memories
name: codex-memories
builder: libenxier-beep
category: AI + 开发
summary_zh: 开发者在用 Codex 连续处理同一代码库、需要跨会话保留上下文时打开它：它把历史会话与项目信息写入本地存储，在提问时按受控规则召回相关片段并逐步展开给模型，最终让 Codex 在后续会话中直接带着这些上下文继续改代码；召回内容是否准确仍需开发者自行确认。具体流程与交付细节仍待核验。
inspiration: 趋势：编码助手正从单次补全走向跨会话的长期上下文，记忆层开始被单独拆出来做。切入：从受合规或数据不能出本机约束的开发团队进入，做本地记忆与召回治理，而不是再做一个编码助手；可考虑按团队席位或私有部署收费，但公开材料未披露价格。
summary_en: 'Developers open it when working on the same codebase across Codex sessions and need context
  to persist: it writes past sessions and project information to local storage, recalls relevant fragments
  under governed rules and discloses them progressively to the model, so Codex continues editing code
  with that context in later sessions; whether the recalled content is accurate still needs the developer''s
  own confirmation. The exact workflow and deliverables remain to be verified.'
inspiration_en: 'Trend: coding assistants are moving from single-shot completion toward long-lived cross-session
  context, and the memory layer is being split out as its own component. Entry point: start with development
  teams whose code or compliance rules keep data on the machine, and sell local memory plus recall governance
  rather than another coding assistant; per-seat or private-deployment pricing is conceivable, but no
  price is disclosed in public materials.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 软件开发工程师
jobs_en:
- Software developer
regions: []
regions_en: []
open_source: true
url: https://github.com/libenxier-beep/codex-memories
canonical_url: https://github.com/libenxier-beep/codex-memories
summary: 'Local-first persistent memory for OpenAI Codex: governed recall, progressive disclosure, no
  hosted vector database.'
first_seen: '2026-08-27T06:44:18Z'
last_seen: '2026-09-15T00:38:44Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/libenxier-beep/codex-memories
  seen_at: '2026-09-15T00:38:44Z'
  metrics:
    stars: 102
    forks: 2
    open_issues: 0
  kind: product
---

# codex-memories

Local-first persistent memory for OpenAI Codex: governed recall, progressive disclosure, no hosted vector database.

## 笔记


