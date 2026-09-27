---
slug: vercel-ai-ai-sdk-perplexity500
name: '@ai-sdk/perplexity'
builder: vercel
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
url: https://github.com/vercel/ai/releases/tag/%40ai-sdk/perplexity%405.0.0
canonical_url: https://github.com/vercel/ai/releases/tag/%40ai-sdk/perplexity%405.0.0
summary: '### Major Changes


  - 38fe0e5: BREAKING: Migrate language generation from the Sonar Chat Completions API to the Agent API.
  Replace Sonar model IDs and provider options with Agent API presets, models, and tools. The new API
  changes request and response metadata, raw stream events, usage and cost data, and does not support
  Sonar PDF input or image and video results.


  ### Patch Changes


  - 38fe0e5: Recover missing text from Agent API terminal events and output items, including incomplete
  responses, without repeating text already received as deltas. Track each message content part separately.

  - 38fe0e5: Accept native Agent API tool traces such as finance results without validating them as web
  search results. Preserve these traces in raw responses and stream chunks.

  - 38fe0e5: Preserve URL citation annotations as sources in Agent API streams, including completed and
  incomplete terminal responses.

  - 38fe0e5: Emit each Agent API source URL once while preserving search result IDs for citation correlation
  when a URL is fetched or annotated before it appears in search results.'
first_seen: '2026-09-26T01:59:37Z'
last_seen: '2026-09-27T00:36:20Z'
status: rejected
sources:
- github
sightings:
- source: github
  url: https://github.com/vercel/ai/releases/tag/%40ai-sdk/perplexity%405.0.0
  seen_at: '2026-09-27T00:36:20Z'
  metrics:
    reactions: 0
  kind: news
---

# @ai-sdk/perplexity

### Major Changes

- 38fe0e5: BREAKING: Migrate language generation from the Sonar Chat Completions API to the Agent API. Replace Sonar model IDs and provider options with Agent API presets, models, and tools. The new API changes request and response metadata, raw stream events, usage and cost data, and does not support Sonar PDF input or image and video results.

### Patch Changes

- 38fe0e5: Recover missing text from Agent API terminal events and output items, including incomplete responses, without repeating text already received as deltas. Track each message content part separately.
- 38fe0e5: Accept native Agent API tool traces such as finance results without validating them as web search results. Preserve these traces in raw responses and stream chunks.
- 38fe0e5: Preserve URL citation annotations as sources in Agent API streams, including completed and incomplete terminal responses.
- 38fe0e5: Emit each Agent API source URL once while preserving search result IDs for citation correlation when a URL is fetched or annotated before it appears in search results.

## 笔记


