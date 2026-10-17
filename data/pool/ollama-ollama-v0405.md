---
slug: ollama-ollama-v0405
name: Ollama
builder: ollama
category: ''
summary_zh: Ollama 是本地运行开源大模型的工具，开发者用一条命令拉取并运行模型。本次更新让它在本地直接跑 Nemotron 3.5 Super/Bolt 这类视觉语言模型，并新增云端决策模型调用通道。
inspiration: ''
summary_en: Ollama is a tool for running open-source large models locally, letting developers pull and
  run a model with a single command. This release lets it run vision-language models such as Nemotron
  3.5 Super/Bolt locally and adds a cloud channel for decision models.
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
url: https://github.com/ollama/ollama/releases/tag/v0.40.5
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.40.5
summary: "## NVIDIA Nemotron 3.5 Super\r\n\r\n[NVIDIA Nemotron 3.5 Super](https://ollama.com/library/nemotron-3.5-super)\
  \ is a vision-language model for coding, reasoning, tool use, and document understanding. It pairs a\
  \ 120B-parameter hybrid Mamba-2/Transformer mixture-of-experts backbone (12B active per token) with\
  \ a C-RADIO vision encoder, and supports tool calling, an on/off thinking mode, and context up to 1M\
  \ tokens.\r\n\r\n```\r\nollama run nemotron-3.5-super\r\n```\r\n\r\nA compact sibling, [Nemotron 3.5\
  \ Bolt](https://ollama.com/library/nemotron-3.5-bolt), distills Super down to 74B parameters (9B active)\
  \ tuned to fit a 24 GB NVIDIA GPU for everyday agentic tasks, with speculative decoding via its included\
  \ drafter.\r\n\r\n## What's Changed\r\n* Decision models are now available on cloud — use `clef:cloud`\
  \ and `clef-flash:cloud` to run decision models through ollama.com cloud without pulling them locally\r\
  \n* Continuing an OpenAI-compatible Responses conversation that includes custom tool calls no longer\
  \ fails with an error\r\n* Clearer error messages when cloud access fails: sign-in problems, payment\
  \ issues in the desktop app, and upstream access errors from the ChatGPT gateway now explain what went\
  \ wrong\r\n* Updated llama.cpp (adding Nemotron 3.5 support) and MLX\r\n\r\n## New Contributors\r\n\
  * @willietran made their first contribution in https://github.com/ollama/ollama/pull/18986\r\n\r\n**Full\
  \ Changelog**: https://github.com/ollama/ollama/compare/v0.40.4...v0.40.5"
first_seen: '2026-10-16T00:25:17Z'
last_seen: '2026-10-17T00:30:30Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.40.5
  seen_at: '2026-10-17T00:30:30Z'
  metrics:
    reactions: 18
  kind: news
---

# Ollama

## NVIDIA Nemotron 3.5 Super

[NVIDIA Nemotron 3.5 Super](https://ollama.com/library/nemotron-3.5-super) is a vision-language model for coding, reasoning, tool use, and document understanding. It pairs a 120B-parameter hybrid Mamba-2/Transformer mixture-of-experts backbone (12B active per token) with a C-RADIO vision encoder, and supports tool calling, an on/off thinking mode, and context up to 1M tokens.

```
ollama run nemotron-3.5-super
```

A compact sibling, [Nemotron 3.5 Bolt](https://ollama.com/library/nemotron-3.5-bolt), distills Super down to 74B parameters (9B active) tuned to fit a 24 GB NVIDIA GPU for everyday agentic tasks, with speculative decoding via its included drafter.

## What's Changed
* Decision models are now available on cloud — use `clef:cloud` and `clef-flash:cloud` to run decision models through ollama.com cloud without pulling them locally
* Continuing an OpenAI-compatible Responses conversation that includes custom tool calls no longer fails with an error
* Clearer error messages when cloud access fails: sign-in problems, payment issues in the desktop app, and upstream access errors from the ChatGPT gateway now explain what went wrong
* Updated llama.cpp (adding Nemotron 3.5 support) and MLX

## New Contributors
* @willietran made their first contribution in https://github.com/ollama/ollama/pull/18986

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.4...v0.40.5

## 笔记


