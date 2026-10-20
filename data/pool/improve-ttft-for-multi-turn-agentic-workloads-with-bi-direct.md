---
slug: improve-ttft-for-multi-turn-agentic-workloads-with-bi-direct
name: vLLM
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
url: https://aws.amazon.com/blogs/machine-learning/improve-ttft-for-multi-turn-agentic-workloads-with-bi-directional-kv-transfer-in-vllm/
canonical_url: https://aws.amazon.com/blogs/machine-learning/improve-ttft-for-multi-turn-agentic-workloads-with-bi-directional-kv-transfer-in-vllm
summary: 'Multi-turn agentic workloads build on accumulated context as an agent reasons, invokes tools,
  and incorporates earlier results. With each new turn, the client resends the conversation history, including
  system instructions, prior prompts, tool results, and model responses, causing the growing context to
  be processed repeatedly. In Prefill-decode (P-D) disaggregation , each request is split across specialized
  nodes: the prefill node processes the prompt and builds its key-value (KV) cache, then the decode node
  retrieves those KV blocks and generates the response. Conventional disaggregated serving, however, only
  transfers KV cache in one direction: from prefill to decode node. This one-directional flow creates
  two inefficiencies for multi-turn workloads. First, after generating a response, the decode node holds
  KV cache entries for both the prompt and the newly generated tokens. When processing the next turn,
  the prefill node cannot retrieve those entries, so it must recompute the KV projections for the previous
  response tokens. Second, the decode node maintains the session state while the prefill nodes don’t,
  increasing the probability of cache eviction for active sessions on the prefill nodes. On a full cache
  miss, the prefill node must recompute KV projections for the entire conversation history, including
  system instructions, prior user requests,'
first_seen: '2026-10-20T01:06:54Z'
last_seen: '2026-10-20T01:06:54Z'
status: rejected
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/improve-ttft-for-multi-turn-agentic-workloads-with-bi-directional-kv-transfer-in-vllm/
  seen_at: '2026-10-20T01:06:54Z'
  metrics: {}
  kind: news
---

# vLLM

Multi-turn agentic workloads build on accumulated context as an agent reasons, invokes tools, and incorporates earlier results. With each new turn, the client resends the conversation history, including system instructions, prior prompts, tool results, and model responses, causing the growing context to be processed repeatedly. In Prefill-decode (P-D) disaggregation , each request is split across specialized nodes: the prefill node processes the prompt and builds its key-value (KV) cache, then the decode node retrieves those KV blocks and generates the response. Conventional disaggregated serving, however, only transfers KV cache in one direction: from prefill to decode node. This one-directional flow creates two inefficiencies for multi-turn workloads. First, after generating a response, the decode node holds KV cache entries for both the prompt and the newly generated tokens. When processing the next turn, the prefill node cannot retrieve those entries, so it must recompute the KV projections for the previous response tokens. Second, the decode node maintains the session state while the prefill nodes don’t, increasing the probability of cache eviction for active sessions on the prefill nodes. On a full cache miss, the prefill node must recompute KV projections for the entire conversation history, including system instructions, prior user requests,

## 笔记


