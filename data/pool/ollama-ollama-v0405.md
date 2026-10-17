---
slug: ollama-ollama-v0405
name: Ollama
builder: ollama
category: ''
summary_zh: Ollama 是本地运行开源大模型的工具，本次更新让开发者能在自己的机器或它的云端直接跑 Nemotron 3.5 系列模型，并修复了带自定义工具调用的会话报错。它属于模型分发与运行层的变化，不是面向具体行业旧流程的独立应用。
inspiration: ''
summary_en: Ollama is a tool for running open-source large models locally; this update lets developers
  run the Nemotron 3.5 family on their own machine or through its cloud, and fixes an error in conversations
  with custom tool calls. It is a change in the model distribution and runtime layer, not a standalone
  application aimed at a specific industry's old workflow.
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
status: market_context
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


