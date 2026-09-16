---
slug: ollama-ollama-v0341
name: 'ollama/ollama: v0.34.1'
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
url: https://github.com/ollama/ollama/releases/tag/v0.34.1
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.34.1
summary: "## What's Changed\r\n* MLX safetensors `ollama create` no longer experimental.  GGUF model creation\
  \ now requires using llama.cpp tooling for safetensor conversion and quantization.\r\n* Improved MLX\
  \ memory handling on Apple Silicon\r\n* Runaway repeat token detection now requires 100 repeat tokens\
  \ for reduced false positives (e.g. OCR)\r\n* `/api/tags` is much faster on large model libraries (3.1\
  \ s → 294 ms cold in testing), and model capabilities are now reported consistently.\r\n* Deprecated\
  \ `typical_p`: it can no longer be set when creating new models, existing GGUF models retain support.\r\
  \n* MLX and llama.cpp updates\r\n\r\n\r\n**Full Changelog**: https://github.com/ollama/ollama/compare/v0.34.0...v0.34.1-rc1"
first_seen: '2026-09-14T22:14:03Z'
last_seen: '2026-09-16T00:20:40Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.34.1
  seen_at: '2026-09-16T00:20:40Z'
  metrics:
    reactions: 24
  kind: news
---

# ollama/ollama: v0.34.1

## What's Changed
* MLX safetensors `ollama create` no longer experimental.  GGUF model creation now requires using llama.cpp tooling for safetensor conversion and quantization.
* Improved MLX memory handling on Apple Silicon
* Runaway repeat token detection now requires 100 repeat tokens for reduced false positives (e.g. OCR)
* `/api/tags` is much faster on large model libraries (3.1 s → 294 ms cold in testing), and model capabilities are now reported consistently.
* Deprecated `typical_p`: it can no longer be set when creating new models, existing GGUF models retain support.
* MLX and llama.cpp updates


**Full Changelog**: https://github.com/ollama/ollama/compare/v0.34.0...v0.34.1-rc1

## 笔记


