---
slug: ollama-ollama-v0350
name: Ollama
builder: ollama
category: ''
summary_zh: Ollama 是一个在本地运行大模型的推理运行时，开发者通过命令行拉取模型并调用本地接口。v0.35.0 新增的 /v1/systemone 让调用方提交一段上下文和若干问题，模型不再返回文本，而是返回选项、概率与置信度分数，官方列出的用途是工单分流、模型路由和内容分类；具体业务流程与交付形态仍待核验。
inspiration: ''
summary_en: Ollama is a local inference runtime that runs large models on a developer's own machine, pulled
  via CLI and called through a local endpoint. The new /v1/systemone endpoint in v0.35.0 lets a caller
  submit context plus questions and receive choices, probabilities and confidence scores instead of text,
  with ticket triage, model routing and content classification named as intended uses; the concrete business
  workflow and delivery form still need verification.
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
url: https://github.com/ollama/ollama/releases/tag/v0.35.0
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.35.0
summary: "## Decision models\r\n\r\nOllama now supports decision models through `/v1/systemone`, based\
  \ on [TypeSafe’s Jev API](https://typesafe.ai).\r\n\r\nDecision models return choices, probabilities,\
  \ and scores instead of text. Use them for tasks such as ticket triage, model routing, and content classification.\r\
  \n\r\nAvailable models:\r\n- [**Nimble**](https://ollama.com/library/nimble) from Bespoke Labs\r\n-\
  \ [**Tev1**](https://ollama.com/library/tev1) from Together AI\r\n\r\n```sh\r\nollama pull nimble\r\n\
  ```\r\n\r\nSend context and one or more questions:\r\n\r\n```sh\r\ncurl http://localhost:11434/v1/systemone\
  \ \\\r\n  -H 'Content-Type: application/json' \\\r\n  -d '{\r\n    \"model\": \"nimble\",\r\n    \"\
  state\": \"Our checkout has returned 500 errors since 9am.\",\r\n    \"questions\": {\r\n      \"label\"\
  : {\r\n        \"type\": \"choice\",\r\n        \"instructions\": \"Which label fits this ticket?\"\
  ,\r\n        \"criteria\": {\r\n          \"billing\": \"Payments and refunds\",\r\n          \"bug\"\
  : \"Software errors\",\r\n          \"account\": \"Login and account access\"\r\n        }\r\n     \
  \ }\r\n    }\r\n  }'\r\n```\r\n\r\nExample response:\r\n\r\n```json\r\n{\r\n  \"model\": \"nimble\"\
  ,\r\n  \"answers\": {\r\n    \"label\": {\r\n      \"type\": \"choice\",\r\n      \"choice\": \"bug\"\
  ,\r\n      \"probabilities\": {\r\n        \"billing\": 0.0125,\r\n        \"bug\": 0.9781,\r\n    \
  \    \"account\": 0.0093\r\n      },\r\n      \"confidence\": 0.8906\r\n    }\r\n  },\r\n  \"usage\"\
  : {\r\n    \"input_tokens\": 174,\r\n    \"output_tokens\": 1\r\n  }\r\n}\r\n```\r\n\r\nThe API supports\
  \ three question types:\r\n- `choice`: Select an option and return probabilities for each.\r\n- `noul`:\
  \ Return the probability that a condition is true.\r\n- `score`: Return a score across an ordered set\
  \ of criteria\r\n\r\n## What's Changed\r\n\r\n- Settings now opens without waiting for model discovery.\r\
  \n- Fixed the macOS update menu and icon not reflecting an available update at startup.\r\n- Fixed stalled\
  \ MLX model downloads hanging indefinitely.\r\n- Requests containing the deprecated `typical_p` parameter\
  \ now log a warning instead of failing.\r\n\r\n**Full Changelog:** https://github.com/ollama/ollama/compare/v0.34.4...v0.35.0"
first_seen: '2026-09-28T21:23:22Z'
last_seen: '2026-10-01T01:18:42Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.35.0
  seen_at: '2026-10-01T01:18:42Z'
  metrics:
    reactions: 35
  kind: news
---

# Ollama

## Decision models

Ollama now supports decision models through `/v1/systemone`, based on [TypeSafe’s Jev API](https://typesafe.ai).

Decision models return choices, probabilities, and scores instead of text. Use them for tasks such as ticket triage, model routing, and content classification.

Available models:
- [**Nimble**](https://ollama.com/library/nimble) from Bespoke Labs
- [**Tev1**](https://ollama.com/library/tev1) from Together AI

```sh
ollama pull nimble
```

Send context and one or more questions:

```sh
curl http://localhost:11434/v1/systemone \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "nimble",
    "state": "Our checkout has returned 500 errors since 9am.",
    "questions": {
      "label": {
        "type": "choice",
        "instructions": "Which label fits this ticket?",
        "criteria": {
          "billing": "Payments and refunds",
          "bug": "Software errors",
          "account": "Login and account access"
        }
      }
    }
  }'
```

Example response:

```json
{
  "model": "nimble",
  "answers": {
    "label": {
      "type": "choice",
      "choice": "bug",
      "probabilities": {
        "billing": 0.0125,
        "bug": 0.9781,
        "account": 0.0093
      },
      "confidence": 0.8906
    }
  },
  "usage": {
    "input_tokens": 174,
    "output_tokens": 1
  }
}
```

The API supports three question types:
- `choice`: Select an option and return probabilities for each.
- `noul`: Return the probability that a condition is true.
- `score`: Return a score across an ordered set of criteria

## What's Changed

- Settings now opens without waiting for model discovery.
- Fixed the macOS update menu and icon not reflecting an available update at startup.
- Fixed stalled MLX model downloads hanging indefinitely.
- Requests containing the deprecated `typical_p` parameter now log a warning instead of failing.

**Full Changelog:** https://github.com/ollama/ollama/compare/v0.34.4...v0.35.0

## 笔记


