---
slug: reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagem
name: Amazon SageMaker Inference
builder: ''
category: ''
summary_zh: AWS 于 2026 年 9 月 10 日为 Amazon SageMaker Inference 推出前缀感知路由，将共享相同提示前缀的请求路由到同一实例以保持 KV 缓存热度；在
  Llama 3.1 70B 基准上，P50 首 token 时间最高降低 77%，KV 缓存命中率从约 25% 提升至 80% 以上。这直接降低 LLM 应用的推理延迟和缓存成本，使多轮对话和共享系统提示类工作负载更节省算力。
inspiration: ''
summary_en: On September 10, 2026, AWS launched prefix-aware routing on Amazon SageMaker Inference, sending
  requests that share the same prompt prefix to the same instance to keep the KV cache warm; on Llama
  3.1 70B benchmarks it reduced P50 time-to-first-token by up to 77% and raised KV cache hit rates from
  about 25% to over 80%. This directly lowers latency and cache costs for LLM applications, making multi-turn
  and shared-system-prompt workloads more compute-efficient.
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
url: https://aws.amazon.com/blogs/machine-learning/reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagemaker-inference/
canonical_url: https://aws.amazon.com/blogs/machine-learning/reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagemaker-inference
summary: Amazon SageMaker Inference now offers prefix-aware routing, a routing strategy that sends requests
  sharing the same prompt prefix to the same instance so the KV cache stays warm. In benchmarks on Llama
  3.1 70B, it reduced P50 time-to-first-token by up to 77% and raised KV cache hit rates from about 25%
  to over 80%.
first_seen: '2026-09-10T21:58:09Z'
last_seen: '2026-09-11T00:10:51Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagemaker-inference/
  seen_at: '2026-09-11T00:10:51Z'
  metrics: {}
  kind: news
---

# Amazon SageMaker Inference

Amazon SageMaker Inference now offers prefix-aware routing, a routing strategy that sends requests sharing the same prompt prefix to the same instance so the KV cache stays warm. In benchmarks on Llama 3.1 70B, it reduced P50 time-to-first-token by up to 77% and raised KV cache hit rates from about 25% to over 80%.

## 笔记


