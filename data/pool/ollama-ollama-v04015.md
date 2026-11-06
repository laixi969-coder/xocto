---
slug: ollama-ollama-v04015
name: 'ollama/ollama: v0.40.15'
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
url: https://github.com/ollama/ollama/releases/tag/v0.40.15
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.40.15
summary: "## MiMo V2.6\r\n\r\nXiaomi MiMo's [mimo-v2.6](https://ollama.com/library/mimo-v2.6), a 9B model\
  \ built for code and agent workflows, is now supported in Ollama.\r\n\r\n```sh\r\nollama run mimo-v2.6\r\
  \n```\r\n\r\n## AutoTrust decision models\r\n\r\n[AutoTrust](https://ollama.com/library/autotrust-jev)\
  \ decision models read text and return choices, yes or no probabilities, and ratings for the questions\
  \ you supply. The family includes 9b, 35b, and 27b-vl sizes — the 35b and 27b-vl sizes can also read\
  \ images.\r\n\r\n```sh\r\nollama run autotrust-jev \"A customer says their card was charged twice.\"\
  \ --ask \"Is this a billing issue?\"\r\n```\r\n\r\nNote: autotrust-jev is supported on Apple silicon\
  \ in this release.\r\n\r\n## What's Changed\r\n\r\n - ollama launch now supports Kimi Code CLI — the\
  \ successor to kimi-cli — and offers to migrate existing kimi-cli setups\r\n - ollama launch now fills\
  \ in Pi's model list automatically so models can be picked inside Pi, and Claude Desktop's model\r\n\
  \   picker shows Ollama's actual model names\r\n - Recurrent and vision GGUF models can now serve more\
  \ than one request at a time\r\n - Qwen3 and Qwen3.5 models using long-context (YaRN) scaling\r\n -\
  \ Running ollama with no arguments opens the welcome launcher\r\n\r\n**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.14...v0.40.15"
first_seen: '2026-11-06T02:26:55Z'
last_seen: '2026-11-06T02:26:55Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.40.15
  seen_at: '2026-11-06T02:26:55Z'
  metrics:
    reactions: 14
  kind: news
---

# ollama/ollama: v0.40.15

## MiMo V2.6

Xiaomi MiMo's [mimo-v2.6](https://ollama.com/library/mimo-v2.6), a 9B model built for code and agent workflows, is now supported in Ollama.

```sh
ollama run mimo-v2.6
```

## AutoTrust decision models

[AutoTrust](https://ollama.com/library/autotrust-jev) decision models read text and return choices, yes or no probabilities, and ratings for the questions you supply. The family includes 9b, 35b, and 27b-vl sizes — the 35b and 27b-vl sizes can also read images.

```sh
ollama run autotrust-jev "A customer says their card was charged twice." --ask "Is this a billing issue?"
```

Note: autotrust-jev is supported on Apple silicon in this release.

## What's Changed

 - ollama launch now supports Kimi Code CLI — the successor to kimi-cli — and offers to migrate existing kimi-cli setups
 - ollama launch now fills in Pi's model list automatically so models can be picked inside Pi, and Claude Desktop's model
   picker shows Ollama's actual model names
 - Recurrent and vision GGUF models can now serve more than one request at a time
 - Qwen3 and Qwen3.5 models using long-context (YaRN) scaling
 - Running ollama with no arguments opens the welcome launcher

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.14...v0.40.15

## 笔记


