---
slug: best-practices-for-writing-denied-topics-in-amazon-bedrock-g
name: Best practices for writing Denied Topics in Amazon Bedrock Guardrails
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
url: https://aws.amazon.com/blogs/machine-learning/best-practices-for-writing-denied-topics-in-amazon-bedrock-guardrails/
canonical_url: https://aws.amazon.com/blogs/machine-learning/best-practices-for-writing-denied-topics-in-amazon-bedrock-guardrails
summary: 'With Denied Topics in Amazon Bedrock Guardrails , you block a content category by describing
  it in plain language, and the guardrail applies that description to every request by meaning rather
  than by keyword. That same mechanism can also match more than you intend. A topic named Finance, meant
  to keep an assistant out of investment advice, also blocks “When does my direct deposit clear?”. Inputs
  close in meaning to the topic can get caught, not only the requests you intended. When Denied Topics
  blocks too much or too little, the cause is usually one of four authoring patterns: Topics that block
  legitimate queries. A topic framed around a subject domain (Finance, Legal, Compensation) rather than
  the user’s intention can match queries semantically near that domain. This is a frequent failure mode.
  Topics that miss the requests they were written to catch. A definition built from keyword lists (“words
  like invest, portfolio, stock…”) misses phrasings that use other vocabulary and fires on unrelated inputs
  that happen to share those words. Examples that teach the wrong thing. Five paraphrases of one idea
  leave the topic’s boundaries unguarded, and examples that name specific countries, products, or companies
  pull those entities into the'
first_seen: '2026-11-17T04:29:39Z'
last_seen: '2026-11-17T04:29:39Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/best-practices-for-writing-denied-topics-in-amazon-bedrock-guardrails/
  seen_at: '2026-11-17T04:29:39Z'
  metrics: {}
  kind: news
---

# Best practices for writing Denied Topics in Amazon Bedrock Guardrails

With Denied Topics in Amazon Bedrock Guardrails , you block a content category by describing it in plain language, and the guardrail applies that description to every request by meaning rather than by keyword. That same mechanism can also match more than you intend. A topic named Finance, meant to keep an assistant out of investment advice, also blocks “When does my direct deposit clear?”. Inputs close in meaning to the topic can get caught, not only the requests you intended. When Denied Topics blocks too much or too little, the cause is usually one of four authoring patterns: Topics that block legitimate queries. A topic framed around a subject domain (Finance, Legal, Compensation) rather than the user’s intention can match queries semantically near that domain. This is a frequent failure mode. Topics that miss the requests they were written to catch. A definition built from keyword lists (“words like invest, portfolio, stock…”) misses phrasings that use other vocabulary and fires on unrelated inputs that happen to share those words. Examples that teach the wrong thing. Five paraphrases of one idea leave the topic’s boundaries unguarded, and examples that name specific countries, products, or companies pull those entities into the

## 笔记


