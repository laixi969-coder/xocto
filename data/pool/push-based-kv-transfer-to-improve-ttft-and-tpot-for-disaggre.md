---
slug: push-based-kv-transfer-to-improve-ttft-and-tpot-for-disaggre
name: Push-based KV transfer to improve TTFT and TPOT for disaggregated inference in vLLM
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
url: https://aws.amazon.com/blogs/machine-learning/push-based-kv-transfer-to-improve-ttft-and-tpot-for-disaggregated-inference-in-vllm/
canonical_url: https://aws.amazon.com/blogs/machine-learning/push-based-kv-transfer-to-improve-ttft-and-tpot-for-disaggregated-inference-in-vllm
summary: 'vLLM is an open-source inference and serving engine for large language models (LLMs). LLM inference
  has two distinct phases: prefill, which processes the input prompt and builds the key-value (KV) cache,
  and decode, which uses that cache to generate output one token at a time. These phases have different
  compute, memory, and scaling characteristics. Prefill-decode (P-D) disaggregation runs them on separate
  engine instances, allowing each phase to scale and be optimized independently. This can improve resource
  utilization, throughput, and latency under load. However, it also requires transferring the KV cache
  from the prefill instance to the decode instance before token generation can begin, making efficient
  KV transfer critical to time-to-first-token (TTFT). One of the ways vLLM performs this transfer is through
  the NVIDIA Inference Xfer Library (NIXL) connector , which moves KV blocks over interconnects that support
  Remote Direct Memory Access (RDMA), such as AWS Elastic Fabric Adapter ( AWS EFA , the low-latency RDMA
  network used across servers in AWS). On supported instance types , AWS EFA supports GPUDirect RDMA and
  Neuron Direct RDMA. NIXL can therefore transfer KV blocks directly between GPU or AWS Trainium device
  memory without staging through host memory. The default mode for NIXL connector'
first_seen: '2026-10-20T01:06:54Z'
last_seen: '2026-10-20T01:06:54Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/push-based-kv-transfer-to-improve-ttft-and-tpot-for-disaggregated-inference-in-vllm/
  seen_at: '2026-10-20T01:06:54Z'
  metrics: {}
  kind: news
---

# Push-based KV transfer to improve TTFT and TPOT for disaggregated inference in vLLM

vLLM is an open-source inference and serving engine for large language models (LLMs). LLM inference has two distinct phases: prefill, which processes the input prompt and builds the key-value (KV) cache, and decode, which uses that cache to generate output one token at a time. These phases have different compute, memory, and scaling characteristics. Prefill-decode (P-D) disaggregation runs them on separate engine instances, allowing each phase to scale and be optimized independently. This can improve resource utilization, throughput, and latency under load. However, it also requires transferring the KV cache from the prefill instance to the decode instance before token generation can begin, making efficient KV transfer critical to time-to-first-token (TTFT). One of the ways vLLM performs this transfer is through the NVIDIA Inference Xfer Library (NIXL) connector , which moves KV blocks over interconnects that support Remote Direct Memory Access (RDMA), such as AWS Elastic Fabric Adapter ( AWS EFA , the low-latency RDMA network used across servers in AWS). On supported instance types , AWS EFA supports GPUDirect RDMA and Neuron Direct RDMA. NIXL can therefore transfer KV blocks directly between GPU or AWS Trainium device memory without staging through host memory. The default mode for NIXL connector

## 笔记


