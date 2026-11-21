---
slug: cut-self-hosted-llm-cost-and-latency-with-the-distributed-kv
name: Cut self-hosted LLM cost and latency with the distributed KV caching agent skill
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
url: https://aws.amazon.com/blogs/machine-learning/cut-self-hosted-llm-cost-and-latency-with-the-distributed-kv-caching-agent-skill/
canonical_url: https://aws.amazon.com/blogs/machine-learning/cut-self-hosted-llm-cost-and-latency-with-the-distributed-kv-caching-agent-skill
summary: Customers increasingly self-host large language models (LLMs) on GPUs for control over cost,
  accuracy, and latency. However, self-hosting often means paying for redundant GPU work because small,
  isolated caches on each server can’t hold or share the growing context AI agents and chat applications
  resend. Consider a legal AI assistant that can accumulate hundreds of thousands of tokens of case history
  in each conversation. When a lawyer returns to a thread after lunch, responses from the LLM can take
  minutes. The GPU server that picks up the request has none of that history in its memory. So, the GPU
  recomputes the key-value (KV) attention states for all of those tokens, a step called prefill, before
  it writes a word. The same pattern slows down resumed coding agents, agentic AI assistants, and document
  Q&A assistants. Distributed KV caching with Amazon ElastiCache can cut self-hosted LLM inference costs
  by up to 40% and time to first token (TTFT) by up to 80%. Distributed KV caching extends GPU-local caches
  with a shared tier beside your GPU fleet so any server can reuse KV state for days across sessions,
  routing shifts, and server failures. “ Announcing distributed KV caching for self-hosted LLMs with Amazon
first_seen: '2026-11-21T03:14:15Z'
last_seen: '2026-11-21T03:14:15Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/cut-self-hosted-llm-cost-and-latency-with-the-distributed-kv-caching-agent-skill/
  seen_at: '2026-11-21T03:14:15Z'
  metrics: {}
  kind: news
---

# Cut self-hosted LLM cost and latency with the distributed KV caching agent skill

Customers increasingly self-host large language models (LLMs) on GPUs for control over cost, accuracy, and latency. However, self-hosting often means paying for redundant GPU work because small, isolated caches on each server can’t hold or share the growing context AI agents and chat applications resend. Consider a legal AI assistant that can accumulate hundreds of thousands of tokens of case history in each conversation. When a lawyer returns to a thread after lunch, responses from the LLM can take minutes. The GPU server that picks up the request has none of that history in its memory. So, the GPU recomputes the key-value (KV) attention states for all of those tokens, a step called prefill, before it writes a word. The same pattern slows down resumed coding agents, agentic AI assistants, and document Q&A assistants. Distributed KV caching with Amazon ElastiCache can cut self-hosted LLM inference costs by up to 40% and time to first token (TTFT) by up to 80%. Distributed KV caching extends GPU-local caches with a shared tier beside your GPU fleet so any server can reuse KV state for days across sessions, routing shifts, and server failures. “ Announcing distributed KV caching for self-hosted LLMs with Amazon

## 笔记


