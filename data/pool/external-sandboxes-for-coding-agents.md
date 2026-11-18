---
slug: external-sandboxes-for-coding-agents
name: External sandboxes for coding agents
builder: ''
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
inspiration_en: ''
priority_review: false
project_type: new_application
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: false
url: https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/
canonical_url: https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents
summary: 'External sandboxes for coding agents I''ve been exploring new ways to sandbox code that is executed
  by agents, with a focus on making it safer to try out local models without worrying that a mistake or
  prompt injection attack might cause them to take damaging actions on a machine. I worked on this project
  with Prime Radiant , the AI research lab behind Superpowers and other projects . My post on the Prime
  Radiant blog introduces the external sandbox pattern, where code executed by the agent runs inside a
  dedicated sandbox while the agent itself lives outside of that sandbox. To demonstrate this pattern
  we''ve released three sandbox server implementations: external-sandbox-v86 runs a Node.js server which
  then uses v86 to run Alpine Linux inside WebAssembly. external-sandbox-container is a Python web server
  which runs the sandbox in Alpine Linux inside an Apple Containers instance. external-sandbox-quicksand
  is another Python web server, this time using Microsoft''s Quicksand sandboxing library, which bundles
  QEMU and Alpine Linux in a Python package! Each of these implementations offers the same localhost API.
  You can then configure Pi, Claude Code, or Codex to send API calls to that sandbox any time they want
  to execute code. The sandboxes'
first_seen: '2026-11-18T03:43:38Z'
last_seen: '2026-11-18T03:43:38Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/
  seen_at: '2026-11-18T03:43:38Z'
  metrics: {}
  kind: news
---

# External sandboxes for coding agents

External sandboxes for coding agents I've been exploring new ways to sandbox code that is executed by agents, with a focus on making it safer to try out local models without worrying that a mistake or prompt injection attack might cause them to take damaging actions on a machine. I worked on this project with Prime Radiant , the AI research lab behind Superpowers and other projects . My post on the Prime Radiant blog introduces the external sandbox pattern, where code executed by the agent runs inside a dedicated sandbox while the agent itself lives outside of that sandbox. To demonstrate this pattern we've released three sandbox server implementations: external-sandbox-v86 runs a Node.js server which then uses v86 to run Alpine Linux inside WebAssembly. external-sandbox-container is a Python web server which runs the sandbox in Alpine Linux inside an Apple Containers instance. external-sandbox-quicksand is another Python web server, this time using Microsoft's Quicksand sandboxing library, which bundles QEMU and Alpine Linux in a Python package! Each of these implementations offers the same localhost API. You can then configure Pi, Claude Code, or Codex to send API calls to that sandbox any time they want to execute code. The sandboxes

## 笔记


