---
slug: ollama-ollama-v0404
name: 'ollama/ollama: v0.40.4'
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
url: https://github.com/ollama/ollama/releases/tag/v0.40.4
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.40.4
summary: "## Decision models in the CLI\r\nDecision models can now be used directly from the terminal\
  \ with `ollama run` — ask yes/no questions, classify text into labels, or score against a rubric:\r\n\
  `ollama run nimble --ask \"Is a refund being requested?\" < ticket.txt`\r\n\r\n ## What's Changed\r\n\
  \  * Kev decision models are now supported by the MLX runner on Apple silicon\r\n  * `ollama launch`\
  \ can now be used with usage credits without upgrading to a paid plan\r\n  * `ollama launch codex` now\
  \ includes locally installed Ollama models in its model picker. Use `/model` within the Codex CLI to\
  \ swap models.\r\n  * Improved inference performance by reusing verified manifests and already loaded\
  \ models\r\n  * Added support for multimodal embeddings through llama-server\r\n  * Fixed loading multimodal\
  \ embedding models with small context windows\r\n  * Improved Gemma 4 prefill performance on NVIDIA\
  \ GPUs with the MLX runner\r\n  * MLX runner now clips long Laya states instead of rejecting them\r\n\
  \  * Improved speculative decoding reliability in the MLX runner, including recurrent state handling\
  \ after rollback\r\n   * Updated llama.cpp with native decision model support\r\n  * Updated README\
  \ and documentation with clearer privacy and cloud-services wording\r\n\r\n  \r\n  **Full Changelog**:\
  \ https://github.com/ollama/ollama/compare/v0.40.3...v0.40.4"
first_seen: '2026-10-15T00:32:09Z'
last_seen: '2026-10-15T00:32:09Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.40.4
  seen_at: '2026-10-15T00:32:09Z'
  metrics:
    reactions: 18
  kind: news
---

# ollama/ollama: v0.40.4

## Decision models in the CLI
Decision models can now be used directly from the terminal with `ollama run` — ask yes/no questions, classify text into labels, or score against a rubric:
`ollama run nimble --ask "Is a refund being requested?" < ticket.txt`

 ## What's Changed
  * Kev decision models are now supported by the MLX runner on Apple silicon
  * `ollama launch` can now be used with usage credits without upgrading to a paid plan
  * `ollama launch codex` now includes locally installed Ollama models in its model picker. Use `/model` within the Codex CLI to swap models.
  * Improved inference performance by reusing verified manifests and already loaded models
  * Added support for multimodal embeddings through llama-server
  * Fixed loading multimodal embedding models with small context windows
  * Improved Gemma 4 prefill performance on NVIDIA GPUs with the MLX runner
  * MLX runner now clips long Laya states instead of rejecting them
  * Improved speculative decoding reliability in the MLX runner, including recurrent state handling after rollback
   * Updated llama.cpp with native decision model support
  * Updated README and documentation with clearer privacy and cloud-services wording

  
  **Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.3...v0.40.4

## 笔记


