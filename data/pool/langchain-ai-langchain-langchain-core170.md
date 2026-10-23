---
slug: langchain-ai-langchain-langchain-core170
name: 'langchain-ai/langchain: langchain-core==1.7.0'
builder: langchain-ai
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
url: https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.7.0
canonical_url: https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.7.0
summary: 'Changes since langchain-core==1.6.13


  release(core): 1.7.0 (#41418)

  feat(core): emit `tool-call-delta` for streamed tool-call args (#41257)


  ## Notes


  - Tool-call args now stream as `tool-call-delta` slices instead of `block-delta` snapshots of the args
  so far. If you read raw stream events and their `block-delta` args mid-stream, read `tool-call-delta`
  instead. `.tool_calls.get()` and `.output` are unchanged. To keep snapshots, pin `langchain-core<1.7`.

  - Since 1.6.13, iterating `ChatModelStream.tool_calls` yields each call''s new args slice, not a snapshot
  of the args so far.'
first_seen: '2026-10-23T00:40:56Z'
last_seen: '2026-10-23T00:40:56Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.7.0
  seen_at: '2026-10-23T00:40:56Z'
  metrics:
    reactions: 0
  kind: news
---

# langchain-ai/langchain: langchain-core==1.7.0

Changes since langchain-core==1.6.13

release(core): 1.7.0 (#41418)
feat(core): emit `tool-call-delta` for streamed tool-call args (#41257)

## Notes

- Tool-call args now stream as `tool-call-delta` slices instead of `block-delta` snapshots of the args so far. If you read raw stream events and their `block-delta` args mid-stream, read `tool-call-delta` instead. `.tool_calls.get()` and `.output` are unchanged. To keep snapshots, pin `langchain-core<1.7`.
- Since 1.6.13, iterating `ChatModelStream.tool_calls` yields each call's new args slice, not a snapshot of the args so far.

## 笔记


