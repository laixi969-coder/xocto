---
slug: context-attachment-manager
name: context-attachment-manager
builder: chipfighter
category: AI + 开发
summary_zh: 面向使用 Codex、Claude Code 或 Claude Desktop 的开发者，在继续多轮对话时勾选哪些历史图片随下一条消息发给模型，未勾选的图片变成占位符，对话可以继续而请求体积保持较小；候选未说明占位符是否影响模型对历史内容的理解，实际效果仍待核验。
inspiration: 趋势：随着编码代理进入长会话，上下文体积本身成了需要被用户手动管理的对象，而不只是模型侧自动压缩。切入：可从「长会话成本与上下文治理」这一环节进入，面向重度使用编码代理的团队做可审计的上下文裁剪与费用可见性；候选未披露定价，不能预设收费方式。
summary_en: For developers using Codex, Claude Code, or Claude Desktop, it lets them choose which past
  images are sent with the next message in a multi-turn conversation; unchecked images become placeholders
  so the conversation continues while requests stay small. The candidate does not say whether placeholders
  affect the model's understanding of history, so real effects still need verification.
inspiration_en: 'Trend: as coding agents move into long sessions, context size itself becomes something
  users must manage manually rather than relying only on model-side compression. Entry point: start from
  long-session cost and context governance, offering auditable context trimming and spend visibility to
  teams that heavily use coding agents; no pricing is disclosed in the candidate, so no revenue model
  should be assumed.'
priority_review: false
project_type: open_source
industries:
- 软件开发
- AI 应用开发
industries_en:
- software development
- AI application development
jobs:
- 开发者在使用 Codex 或 Claude Code 进行多轮对话时管理历史图片上下文
jobs_en:
- Developers managing historical image context during multi-turn sessions in Codex or Claude Code
regions: []
regions_en: []
open_source: true
url: https://github.com/chipfighter/context-attachment-manager
canonical_url: https://github.com/chipfighter/context-attachment-manager
summary: 'Codex and Claude Code plugin (works in Claude Desktop): choose which past images go to the model
  with your next message. Unchecked images become placeholders, the conversation goes on, and requests
  stay small.'
first_seen: '2026-10-11T01:01:22Z'
last_seen: '2026-10-11T01:01:22Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/chipfighter/context-attachment-manager
  seen_at: '2026-10-11T01:01:22Z'
  metrics:
    stars: 224
    forks: 9
    open_issues: 0
  kind: product
---

# context-attachment-manager

Codex and Claude Code plugin (works in Claude Desktop): choose which past images go to the model with your next message. Unchecked images become placeholders, the conversation goes on, and requests stay small.

## 笔记


