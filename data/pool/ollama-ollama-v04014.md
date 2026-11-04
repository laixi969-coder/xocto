---
slug: ollama-ollama-v04014
name: 'ollama/ollama: v0.40.14'
builder: ollama
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
inspiration_en: ''
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/ollama/ollama/releases/tag/v0.40.14
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.40.14
summary: "## What's Changed\r\n* `ollama launch claude` now applies the model's output token limit for\
  \ Claude Code, so cloud models no longer run into the 128k default cap\r\n* Cloud web search responses\
  \ on `/api/chat` are now decoded correctly, including compressed responses\r\n* OpenAI-compatible endpoints\
  \ no longer override a model's packaged sampler defaults — clients that send no `temperature`/`top_p`\
  \ get the model's own values instead of 1.0, matching `/api/chat`\r\n* `/v1/responses` now preserves\
  \ readable input content, including prior assistant refusals, instead of flattening it\r\n* Ollama's\
  \ app can now retry ChatGPT disconnect failures instead of leaving the connection in a broken state\r\
  \n* `ollama launch codex` verifies ChatGPT routing before configuring, and reports a clear error when\
  \ routing is unavailable\r\n* Faster top-k sampling on MLX for large vocabularies\r\n\r\n**Full Changelog**:\
  \ https://github.com/ollama/ollama/compare/v0.40.13...v0.40.14"
first_seen: '2026-11-04T02:20:51Z'
last_seen: '2026-11-04T02:20:51Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.40.14
  seen_at: '2026-11-04T02:20:51Z'
  metrics:
    reactions: 21
  kind: news
---

# ollama/ollama: v0.40.14

## What's Changed
* `ollama launch claude` now applies the model's output token limit for Claude Code, so cloud models no longer run into the 128k default cap
* Cloud web search responses on `/api/chat` are now decoded correctly, including compressed responses
* OpenAI-compatible endpoints no longer override a model's packaged sampler defaults — clients that send no `temperature`/`top_p` get the model's own values instead of 1.0, matching `/api/chat`
* `/v1/responses` now preserves readable input content, including prior assistant refusals, instead of flattening it
* Ollama's app can now retry ChatGPT disconnect failures instead of leaving the connection in a broken state
* `ollama launch codex` verifies ChatGPT routing before configuring, and reports a clear error when routing is unavailable
* Faster top-k sampling on MLX for large vocabularies

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.13...v0.40.14

## 笔记


