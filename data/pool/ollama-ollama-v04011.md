---
slug: ollama-ollama-v04011
name: 'ollama/ollama: v0.40.11'
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
url: https://github.com/ollama/ollama/releases/tag/v0.40.11
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.40.11
summary: "## Speech\r\n\r\nOllama can now generate [speech](https://docs.ollama.com/capabilities/speech)\
  \ on macOS. `ollama run` plays text or a chat model's reply aloud as the audio is generated, and apps\
  \ can stream audio through the OpenAI-compatible `/v1/audio/speech` endpoint.\r\n\r\n```sh\r\nollama\
  \ run phonon \"Hello from Ollama.\"\r\n```\r\n\r\n## d3 decision models\r\n\r\n[d3](https://ollama.com/library/d3)\
  \ brings vLLM Semantic Router's decision models to Ollama. Give a model text, structured state, or an\
  \ image, and ask it to classify, answer yes or no, or score options with probabilities. The family includes\
  \ 2B, 4B, 9B, and 27B sizes.\r\n\r\n```sh\r\nollama run d3 \"A customer says their card was charged\
  \ twice.\" --ask \"Is this a billing issue?\"\r\n```\r\n\r\n## New Contributors\r\n* @SynapShift made\
  \ their first contribution in https://github.com/ollama/ollama/pull/19173\r\n\r\n**Full Changelog**:\
  \ https://github.com/ollama/ollama/compare/v0.40.10...v0.40.11-rc0"
first_seen: '2026-10-25T00:21:05Z'
last_seen: '2026-10-26T00:24:22Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.40.11
  seen_at: '2026-10-26T00:24:22Z'
  metrics:
    reactions: 20
  kind: news
---

# ollama/ollama: v0.40.11

## Speech

Ollama can now generate [speech](https://docs.ollama.com/capabilities/speech) on macOS. `ollama run` plays text or a chat model's reply aloud as the audio is generated, and apps can stream audio through the OpenAI-compatible `/v1/audio/speech` endpoint.

```sh
ollama run phonon "Hello from Ollama."
```

## d3 decision models

[d3](https://ollama.com/library/d3) brings vLLM Semantic Router's decision models to Ollama. Give a model text, structured state, or an image, and ask it to classify, answer yes or no, or score options with probabilities. The family includes 2B, 4B, 9B, and 27B sizes.

```sh
ollama run d3 "A customer says their card was charged twice." --ask "Is this a billing issue?"
```

## New Contributors
* @SynapShift made their first contribution in https://github.com/ollama/ollama/pull/19173

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.10...v0.40.11-rc0

## 笔记


