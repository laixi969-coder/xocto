---
slug: datasette-llm-01a11
name: datasette-llm 0.1a11
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
url: https://simonwillison.net/2026/Nov/14/datasette-llm/
canonical_url: https://simonwillison.net/2026/Nov/14/datasette-llm
summary: 'Release: datasette-llm 0.1a11 datasette-llm is the intermediate plugin for Datasette that supports
  configuring LLMs for use with other Datasette plugins. This release adds support for OpenAI-compatible
  endpoints, so you can configure Datasette to use an LLM hosted anywhere that talks the OpenAI pseudo-standard
  web protocol. This means that if you''re running local models with LM Studio or Ollama or llama.cpp
  (which just hit v1.0.0 ) you can run Datasette via uvx like this: wget https://datasette.io/content.db
  uvx --with datasette-agent datasette \ --root --secret 1 \ -s plugins.datasette-llm.default_model ''
  { "model": "lmstudio-qwen", "model_name": "qwen/qwen3.8-27b", "api_base": "http://localhost:1234/v1"
  } '' content.db And you''ll get a local server running a Datasette Agent instance powered by your local
  model! Tags: uv , datasette-agent , llm , datasette , llms , ai , generative-ai'
first_seen: '2026-11-15T01:56:29Z'
last_seen: '2026-11-15T01:56:29Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/14/datasette-llm/
  seen_at: '2026-11-15T01:56:29Z'
  metrics: {}
  kind: news
---

# datasette-llm 0.1a11

Release: datasette-llm 0.1a11 datasette-llm is the intermediate plugin for Datasette that supports configuring LLMs for use with other Datasette plugins. This release adds support for OpenAI-compatible endpoints, so you can configure Datasette to use an LLM hosted anywhere that talks the OpenAI pseudo-standard web protocol. This means that if you're running local models with LM Studio or Ollama or llama.cpp (which just hit v1.0.0 ) you can run Datasette via uvx like this: wget https://datasette.io/content.db uvx --with datasette-agent datasette \ --root --secret 1 \ -s plugins.datasette-llm.default_model ' { "model": "lmstudio-qwen", "model_name": "qwen/qwen3.8-27b", "api_base": "http://localhost:1234/v1" } ' content.db And you'll get a local server running a Datasette Agent instance powered by your local model! Tags: uv , datasette-agent , llm , datasette , llms , ai , generative-ai

## 笔记


