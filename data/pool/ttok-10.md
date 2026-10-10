---
slug: ttok-10
name: ttok 1.0
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
url: https://simonwillison.net/2026/Oct/9/ttok/
canonical_url: https://simonwillison.net/2026/Oct/9/ttok
summary: 'Release: ttok 1.0 I released ttok 0.4 , ran uv tool upgrade ttok , piped a file into the new
  version... and realized that it was defaulting to the GPT-4 tokenizer when it should very clearly default
  to GPT-5/GPT-6 instead! I figured switching the default was a reasonable excuse to finally ship a 1.0.
  OpenAI haven''t actually confirmed that GPT-6 uses the same tokenizer as the GPT-5 family yet - there''s
  an angry issue about it - but I found this commit by William Liu which reports on an experiment he ran
  confirming that the tokenizers are likely the same: All seven GPT models (5.5, 5.6 Sol/Terra/Luna, 6
  Astra/Sol/Luna) report 44,794 tokens and match each other on every one of the 31 fixtures. GPT-6 introduces
  no input-count change on this corpus. Tags: projects , ai , openai , generative-ai , llms , tokenization'
first_seen: '2026-10-10T01:46:29Z'
last_seen: '2026-10-10T01:46:29Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/9/ttok/
  seen_at: '2026-10-10T01:46:29Z'
  metrics: {}
  kind: news
---

# ttok 1.0

Release: ttok 1.0 I released ttok 0.4 , ran uv tool upgrade ttok , piped a file into the new version... and realized that it was defaulting to the GPT-4 tokenizer when it should very clearly default to GPT-5/GPT-6 instead! I figured switching the default was a reasonable excuse to finally ship a 1.0. OpenAI haven't actually confirmed that GPT-6 uses the same tokenizer as the GPT-5 family yet - there's an angry issue about it - but I found this commit by William Liu which reports on an experiment he ran confirming that the tokenizers are likely the same: All seven GPT models (5.5, 5.6 Sol/Terra/Luna, 6 Astra/Sol/Luna) report 44,794 tokens and match each other on every one of the 31 fixtures. GPT-6 introduces no input-count change on this corpus. Tags: projects , ai , openai , generative-ai , llms , tokenization

## 笔记


