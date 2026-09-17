---
slug: ollama-ollama-v0341
name: Ollama
builder: ollama
category: ''
summary_zh: 这是本地模型运行工具的一次版本更新，不是新的独立产品。它把 Apple Silicon 上的 MLX 模型创建从实验状态转为正式支持，并大幅加快大模型库的列表查询速度，影响的是本地部署与推理环节的开发者体验。
inspiration: ''
summary_en: This is a version update to a local model runtime, not a new standalone product. It promotes
  MLX model creation on Apple Silicon out of experimental status and speeds up listing large model libraries,
  affecting developer experience in local deployment and inference.
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
last_seen: '2026-09-17T00:32:43Z'
status: market_context
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.34.1
  seen_at: '2026-09-17T00:32:43Z'
  metrics:
    reactions: 28
  kind: news
---

# Ollama

## What's Changed
* MLX safetensors `ollama create` no longer experimental.  GGUF model creation now requires using llama.cpp tooling for safetensor conversion and quantization.
* Improved MLX memory handling on Apple Silicon
* Runaway repeat token detection now requires 100 repeat tokens for reduced false positives (e.g. OCR)
* `/api/tags` is much faster on large model libraries (3.1 s → 294 ms cold in testing), and model capabilities are now reported consistently.
* Deprecated `typical_p`: it can no longer be set when creating new models, existing GGUF models retain support.
* MLX and llama.cpp updates


**Full Changelog**: https://github.com/ollama/ollama/compare/v0.34.0...v0.34.1-rc1

## 笔记


