---
slug: web-edit-01a0
name: web-edit
builder: ''
category: AI + 开发
summary_zh: 开发者在手机上通过远程代理操作项目时，需要查看和修改服务器文件夹里的凭据等文件，又不想把这些内容送进大模型。web-edit 是一个 Python 网页应用，在指定文件夹上提供浏览与编辑界面，编辑用
  CodeMirror 6，设计上跑在 Tailscale 网络内，由代理启动后手机直接访问。具体交付与权限边界仍待核验。
inspiration: 趋势：代理开始替人跑长任务，但敏感文件不该经过模型，于是出现“让代理起服务、人自己上手改”的旁路。切入：从需要远程运维又受合规约束的小团队入手，把凭据、配置、密钥这类不能进模型的文件单独做成可审计的编辑通道，而不是继续塞进对话里。
summary_en: When developers work on a project from a phone through a remote agent, they sometimes need
  to view or edit files such as credentials in a server folder without sending that content through the
  LLM. web-edit is a Python web app that offers a browsing and editing UI over a folder, using CodeMirror
  6, designed to run over Tailscale so an agent can start it and the phone can reach it directly. Exact
  delivery and permission boundaries still need verification.
inspiration_en: 'Trend: as agents run longer tasks, sensitive files should not pass through the model,
  so a side channel appears where the agent starts a service and the human edits directly. Entry: start
  with small teams doing remote ops under compliance constraints, giving credentials, configs and keys
  a separate auditable editing path instead of routing them through chat.'
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software Development
jobs:
- 开发者在手机上远程查看和编辑服务器文件夹中的配置文件
jobs_en:
- Developers viewing and editing config files in a server folder from a phone
regions: []
regions_en: []
open_source: true
url: https://simonwillison.net/2026/Oct/12/web-edit/
canonical_url: https://simonwillison.net/2026/Oct/12/web-edit
summary: 'Release: web-edit 0.1a0 I was working on a project from my phone using Codex Remote when I found
  myself wanting to edit a credentials file without round-tripping those credentials through the LLM itself.
  So... I had Codex and GPT-6 Astra Extra High build this Python web app which provides a web UI for viewing
  and editing files in a folder. It''s intended to be run over Tailscale, so I can have an agent start
  this running and then edit files via my Tailscale network directly from my phone. Here''s the interface
  for browsing files in a folder: Editing uses CodeMirror 6 - I was going to use Monaco but that still
  doesn''t have a great mobile experience yet. Tags: projects , python , ai , tailscale , generative-ai
  , llms , codex'
first_seen: '2026-10-13T03:04:22Z'
last_seen: '2026-10-13T03:04:22Z'
status: watching
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/12/web-edit/
  seen_at: '2026-10-13T03:04:22Z'
  metrics: {}
  kind: news
---

# web-edit

Release: web-edit 0.1a0 I was working on a project from my phone using Codex Remote when I found myself wanting to edit a credentials file without round-tripping those credentials through the LLM itself. So... I had Codex and GPT-6 Astra Extra High build this Python web app which provides a web UI for viewing and editing files in a folder. It's intended to be run over Tailscale, so I can have an agent start this running and then edit files via my Tailscale network directly from my phone. Here's the interface for browsing files in a folder: Editing uses CodeMirror 6 - I was going to use Monaco but that still doesn't have a great mobile experience yet. Tags: projects , python , ai , tailscale , generative-ai , llms , codex

## 笔记


