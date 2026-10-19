---
slug: llm-echo-05
name: llm-echo 0.5
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
url: https://simonwillison.net/2026/Oct/18/llm-echo/
canonical_url: https://simonwillison.net/2026/Oct/18/llm-echo
summary: 'Release: llm-echo 0.5 I''m working towards a new LLM release, and testing PRs caused me to revisit
  the llm-echo debug plugin. This plugin provides a "model" which doesn''t involve an LLM at all - it
  just repeats back the prompts that have been fed to it. The new release now updates the simulated token
  usage counts to take tool calls, system prompts, and reasoning tokens into account. Example usage: uvx
  --with llm-echo llm -m echo ''hi there'' -o thinking 1 --usage Outputs: First I consider the prompt,
  then I decide what to say. { "prompt": "hi there", "system": "", "attachments": [], "stream": true,
  "previous": [] } Token usage: 2 input, 24 output Tags: llm'
first_seen: '2026-10-19T00:13:57Z'
last_seen: '2026-10-19T00:13:57Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/18/llm-echo/
  seen_at: '2026-10-19T00:13:57Z'
  metrics: {}
  kind: news
---

# llm-echo 0.5

Release: llm-echo 0.5 I'm working towards a new LLM release, and testing PRs caused me to revisit the llm-echo debug plugin. This plugin provides a "model" which doesn't involve an LLM at all - it just repeats back the prompts that have been fed to it. The new release now updates the simulated token usage counts to take tool calls, system prompts, and reasoning tokens into account. Example usage: uvx --with llm-echo llm -m echo 'hi there' -o thinking 1 --usage Outputs: First I consider the prompt, then I decide what to say. { "prompt": "hi there", "system": "", "attachments": [], "stream": true, "previous": [] } Token usage: 2 input, 24 output Tags: llm

## 笔记


