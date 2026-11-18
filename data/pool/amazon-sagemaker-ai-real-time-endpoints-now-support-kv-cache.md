---
slug: amazon-sagemaker-ai-real-time-endpoints-now-support-kv-cache
name: Amazon SageMaker AI real-time endpoints now support KV cache aware routing
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
url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-real-time-endpoints-now-support-kv-cache-aware-routing/
canonical_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-real-time-endpoints-now-support-kv-cache-aware-routing
summary: 'Today, Amazon SageMaker AI introduces KV cache-aware routing (KV-aware routing), a new routing
  strategy for real-time endpoints. It uses the cache state that the model container reports. It sends
  each request to an instance that already holds a long cached match for its prompt and isn’t too busy.
  It’s for teams that serve large language models (LLMs) with multi-turn conversations, long shared prompts,
  or heavy load. You turn it on in two places: add one environment variable to your model so the container
  reports its cache contents, and set RoutingStrategy to KV_AWARE in the endpoint configuration. Your
  clients call the endpoint with the same APIs as before. Here’s the problem it solves: LLM applications
  such as chat assistants, Retrieval Augmented Generation (RAG), and agents with long system prompts send
  many requests that start with the same text. A model keeps the work it did on a prompt in GPU memory,
  the KV cache, and skips that work when the same start reaches the same instance again. In part 1 of
  this series , we introduced prefix-aware routing for Amazon SageMaker AI, which sends requests that
  start the same way to the same instance. Prefix-aware routing infers where a prefix is'
first_seen: '2026-11-18T03:43:37Z'
last_seen: '2026-11-18T03:43:37Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-real-time-endpoints-now-support-kv-cache-aware-routing/
  seen_at: '2026-11-18T03:43:37Z'
  metrics: {}
  kind: news
---

# Amazon SageMaker AI real-time endpoints now support KV cache aware routing

Today, Amazon SageMaker AI introduces KV cache-aware routing (KV-aware routing), a new routing strategy for real-time endpoints. It uses the cache state that the model container reports. It sends each request to an instance that already holds a long cached match for its prompt and isn’t too busy. It’s for teams that serve large language models (LLMs) with multi-turn conversations, long shared prompts, or heavy load. You turn it on in two places: add one environment variable to your model so the container reports its cache contents, and set RoutingStrategy to KV_AWARE in the endpoint configuration. Your clients call the endpoint with the same APIs as before. Here’s the problem it solves: LLM applications such as chat assistants, Retrieval Augmented Generation (RAG), and agents with long system prompts send many requests that start with the same text. A model keeps the work it did on a prompt in GPU memory, the KV cache, and skips that work when the same start reaches the same instance again. In part 1 of this series , we introduced prefix-aware routing for Amazon SageMaker AI, which sends requests that start the same way to the same instance. Prefix-aware routing infers where a prefix is

## 笔记


