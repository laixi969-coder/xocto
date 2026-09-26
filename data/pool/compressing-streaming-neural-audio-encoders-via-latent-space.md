---
slug: compressing-streaming-neural-audio-encoders-via-latent-space
name: Compressing Streaming Neural Audio Encoders via Latent-Space Distillation
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
url: https://machinelearning.apple.com/research/latent-space-distillation
canonical_url: https://machinelearning.apple.com/research/latent-space-distillation
summary: 'System-wide Dictation on Apple devices runs entirely on-device, and the speech it transcribes
  reaches the foundation model through a tokenizer: an encoder that maps short windows of waveform onto
  the representation the language model reads. Because that model is sparsely activated under Instruction-Following
  Pruning, only a small subset of its experts occupies DRAM at any time, so the always-on tokenizer competes
  for the same memory, and its parameter count bears directly on power and latency. In this work we study
  how to compress such a tokenizer by distillation, taking as the supervision…'
first_seen: '2026-09-24T00:00:00Z'
last_seen: '2026-09-26T00:38:19Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://machinelearning.apple.com/research/latent-space-distillation
  seen_at: '2026-09-26T00:38:19Z'
  metrics: {}
  kind: news
---

# Compressing Streaming Neural Audio Encoders via Latent-Space Distillation

System-wide Dictation on Apple devices runs entirely on-device, and the speech it transcribes reaches the foundation model through a tokenizer: an encoder that maps short windows of waveform onto the representation the language model reads. Because that model is sparsely activated under Instruction-Following Pruning, only a small subset of its experts occupies DRAM at any time, so the always-on tokenizer competes for the same memory, and its parameter count bears directly on power and latency. In this work we study how to compress such a tokenizer by distillation, taking as the supervision…

## 笔记


