---
slug: ollama-ollama-v04012
name: 'ollama/ollama: v0.40.12'
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
url: https://github.com/ollama/ollama/releases/tag/v0.40.12
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.40.12
summary: "## Liquid AI LFM3\r\n\r\n[LFM3](https://ollama.com/library/lfm3) is Liquid AI's new family of\
  \ small models built for local agents, tool calling, and structured output, on Liquid's new tri-hybrid\
  \ architecture. The family includes:\r\n\r\n- [lfm3](https://ollama.com/library/lfm3): a 1.7B text model\
  \ with a 256K-token context window\r\n- [lfm3-vl](https://ollama.com/library/lfm3-vl): adds image understanding\r\
  \n- [lfm3-audio](https://ollama.com/library/lfm3-audio): speech recognition, translation, and text-to-speech\
  \ in 18 languages\r\n- [lfm3-omni](https://ollama.com/library/lfm3-omni): text, images, and audio in\
  \ one model\r\n\r\n```sh\r\nollama run lfm3\r\n```\r\n\r\n## d1 decision models\r\n\r\nLiquid AI's d1\
  \ models now come in a 2B size, built on LFM3. [d1](https://ollama.com/library/d1) makes decisions about\
  \ text and images, and [d1-omni](https://ollama.com/library/d1-omni) adds audio.\r\n\r\n```sh\r\nollama\
  \ run d1:2b \"I was charged twice for order 4417.\" --ask \"Is this a billing issue?\"\r\n```\r\n\r\n\
  Note: lfm3 and d1 2b are supported on Apple hardware in this release.  Support for Linux/Windows coming\
  \ soon.\r\n\r\n## What's Changed\r\n- Faster prompt processing on Apple silicon for Gemma 4, Flint and\
  \ Laguna models\r\n- Speculative decoding now supports DFlash2 draft models on MLX\r\n- Gemma 4 keeps\
  \ more detail in small images\r\n- `ollama launch` now works with OpenCode v2\r\n- Fixed tool-only assistant\
  \ turns from Kimi CLI\r\n- Updated MLX and llama.cpp\r\n\r\n**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.11...v0.40.12"
first_seen: '2026-10-28T01:22:33Z'
last_seen: '2026-10-29T01:48:31Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.40.12
  seen_at: '2026-10-29T01:48:31Z'
  metrics:
    reactions: 26
  kind: news
---

# ollama/ollama: v0.40.12

## Liquid AI LFM3

[LFM3](https://ollama.com/library/lfm3) is Liquid AI's new family of small models built for local agents, tool calling, and structured output, on Liquid's new tri-hybrid architecture. The family includes:

- [lfm3](https://ollama.com/library/lfm3): a 1.7B text model with a 256K-token context window
- [lfm3-vl](https://ollama.com/library/lfm3-vl): adds image understanding
- [lfm3-audio](https://ollama.com/library/lfm3-audio): speech recognition, translation, and text-to-speech in 18 languages
- [lfm3-omni](https://ollama.com/library/lfm3-omni): text, images, and audio in one model

```sh
ollama run lfm3
```

## d1 decision models

Liquid AI's d1 models now come in a 2B size, built on LFM3. [d1](https://ollama.com/library/d1) makes decisions about text and images, and [d1-omni](https://ollama.com/library/d1-omni) adds audio.

```sh
ollama run d1:2b "I was charged twice for order 4417." --ask "Is this a billing issue?"
```

Note: lfm3 and d1 2b are supported on Apple hardware in this release.  Support for Linux/Windows coming soon.

## What's Changed
- Faster prompt processing on Apple silicon for Gemma 4, Flint and Laguna models
- Speculative decoding now supports DFlash2 draft models on MLX
- Gemma 4 keeps more detail in small images
- `ollama launch` now works with OpenCode v2
- Fixed tool-only assistant turns from Kimi CLI
- Updated MLX and llama.cpp

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.11...v0.40.12

## 笔记


