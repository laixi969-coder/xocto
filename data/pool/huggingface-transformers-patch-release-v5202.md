---
slug: huggingface-transformers-patch-release-v5202
name: 'huggingface/transformers: Patch release v5.20.2'
builder: huggingface
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
url: https://github.com/huggingface/transformers/releases/tag/v5.20.2
canonical_url: https://github.com/huggingface/transformers/releases/tag/v5.20.2
summary: "# Patch release: v5.20.2\r\n\r\nThis patch notably solves an issue where some inputs could loose\
  \ their original type inside `prepare_inputs_for_generation` in `generate`, leading to problems with\
  \ multimodal models. It also fixes some other issues listed on the below commits.\r\n\r\nIt contains\
  \ the following commits:\r\n\r\n- Fix inputs dict casting in generate (#49731) by @Cyrilvallez\r\n-\
  \ Fix zero expert gradients in bfloat16 with expert parallelism and ep_size < fsdp_size (#49688) by\
  \ @qgallouedec \r\n- Declare the input modalities of the VLMs that report text only (#49677) by @qgallouedec\
  \ \r\n- Avoid a host-to-device copy in eager_mask (#49684) by @hmellor"
first_seen: '2026-10-20T01:06:30Z'
last_seen: '2026-10-20T01:06:30Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/huggingface/transformers/releases/tag/v5.20.2
  seen_at: '2026-10-20T01:06:30Z'
  metrics:
    reactions: 0
  kind: news
---

# huggingface/transformers: Patch release v5.20.2

# Patch release: v5.20.2

This patch notably solves an issue where some inputs could loose their original type inside `prepare_inputs_for_generation` in `generate`, leading to problems with multimodal models. It also fixes some other issues listed on the below commits.

It contains the following commits:

- Fix inputs dict casting in generate (#49731) by @Cyrilvallez
- Fix zero expert gradients in bfloat16 with expert parallelism and ep_size < fsdp_size (#49688) by @qgallouedec 
- Declare the input modalities of the VLMs that report text only (#49677) by @qgallouedec 
- Avoid a host-to-device copy in eager_mask (#49684) by @hmellor

## 笔记


