---
slug: codex-attachment-manager
name: codex-attachment-manager
builder: chipfighter
category: AI + 开发
summary_zh: 开发者在 Codex 会话里连续贴过多张图片、导致后续请求越来越重时，这个插件让人选择哪些历史图片随下一条消息发给模型，未勾选的图片变成占位符，任务继续而请求体积保持较小。它接收的是历史图片附件与下一条消息，产出是裁剪后的请求；具体节省幅度与是否影响回答质量，公开材料未说明，效果仍待核验。
inspiration: 趋势是编码代理的会话越拉越长，上下文里堆积的截图和附件开始直接变成成本和延迟。切入可以选长会话成本敏感的场景，例如按 token 计费的团队或需要保留大量设计稿的移动端开发，做上下文清理与计费可见性，而不是再做一个代理外壳。
summary_en: When a developer has pasted many images into a Codex session and later requests grow heavy,
  this plugin lets them choose which past images go to the model with the next message; unchecked images
  become placeholders so the task continues while requests stay small. It takes historical image attachments
  plus the next message as input and produces a trimmed request; the actual savings and any effect on
  answer quality are not stated in the public material, so the effect remains unverified.
inspiration_en: The trend is that coding-agent sessions grow long, and screenshots and attachments piling
  up in context turn directly into cost and latency. A wedge is cost-sensitive long sessions, such as
  token-billed teams or mobile development that keeps many design mockups, selling context cleanup and
  billing visibility rather than another agent shell.
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 开发者
jobs_en:
- Software developers
regions: []
regions_en: []
open_source: true
url: https://github.com/chipfighter/codex-attachment-manager
canonical_url: https://github.com/chipfighter/codex-attachment-manager
summary: 'Codex plugin: choose which past images go to the model with your next message. Unchecked images
  become placeholders, the task goes on, and requests stay small.'
first_seen: '2026-09-24T05:00:09Z'
last_seen: '2026-10-05T00:56:02Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/chipfighter/codex-attachment-manager
  seen_at: '2026-10-05T00:56:02Z'
  metrics:
    stars: 90
    forks: 0
    open_issues: 0
  kind: product
---

# codex-attachment-manager

Codex plugin: choose which past images go to the model with your next message. Unchecked images become placeholders, the task goes on, and requests stay small.

## 笔记


