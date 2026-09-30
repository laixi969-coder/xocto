---
slug: ollama-ollama-v0350
name: 'ollama/ollama: v0.35.0'
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
last_seen: '2026-09-30T01:18:17Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.35.0
  seen_at: '2026-09-30T01:18:17Z'
  metrics:
    reactions: 26
  kind: news
---

# ollama/ollama: v0.35.0

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


