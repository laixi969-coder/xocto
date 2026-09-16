---
slug: optimizing-cost-and-latency-with-amazon-bedrock-prompt-cachi
name: Amazon Bedrock
builder: ''
category: ''
summary_zh: AWS 在官方博客说明 Bedrock 的提示缓存机制：开发者反复提交同一段上下文时，缓存可复用已处理部分，从而降低输入 token 计费与响应延迟。该能力面向在 Bedrock
  上构建应用的开发者，属于云平台功能更新。
inspiration: ''
summary_en: 'AWS explained Bedrock prompt caching in an official blog post: when developers repeatedly
  submit the same context, the cached portion is reused, lowering input token billing and response latency.
  The capability targets developers building on Bedrock and is a cloud platform feature update.'
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
url: https://aws.amazon.com/blogs/machine-learning/optimizing-cost-and-latency-with-amazon-bedrock-prompt-caching/
canonical_url: https://aws.amazon.com/blogs/machine-learning/optimizing-cost-and-latency-with-amazon-bedrock-prompt-caching
summary: 'Prompt caching in Amazon Bedrock can cut input token costs by up to 90% when you repeatedly
  send the same context to foundation models. This post walks through six practical prompt caching scenarios
  using the Converse API: message content, system prompt, tool definition, mixed TTL, tenant isolation,
  and LangChain integration.'
first_seen: '2026-09-15T16:18:19Z'
last_seen: '2026-09-16T00:21:05Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/optimizing-cost-and-latency-with-amazon-bedrock-prompt-caching/
  seen_at: '2026-09-16T00:21:05Z'
  metrics: {}
  kind: news
---

# Amazon Bedrock

Prompt caching in Amazon Bedrock can cut input token costs by up to 90% when you repeatedly send the same context to foundation models. This post walks through six practical prompt caching scenarios using the Converse API: message content, system prompt, tool definition, mixed TTL, tenant isolation, and LangChain integration.

## 笔记


