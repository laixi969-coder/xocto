---
slug: push-based-kv-transfer-to-improve-ttft-and-tpot-for-disaggre
name: vLLM push-based KV transfer
builder: ''
category: ''
summary_zh: vLLM 在分离式推理中引入基于推送的 KV 缓存传输，通过 NIXL 连接器在 AWS EFA 的 RDMA 网络上于 GPU 或 Trainium 设备内存间直接搬运 KV 块，以减少预填充到解码阶段的传输开销。该优化针对首
  token 延迟和每 token 输出时间，若能稳定生效，将降低长上下文推理的延迟与资源占用，对推理服务的成本与吞吐有直接影响；实际收益幅度材料未量化（推断）。
inspiration: ''
summary_en: vLLM introduced push-based KV cache transfer for disaggregated inference, moving KV blocks
  directly between GPU or Trainium device memory over AWS EFA RDMA via the NIXL connector to cut prefill-to-decode
  transfer overhead. The optimization targets time-to-first-token and time-per-output-token; if it holds
  up, it would lower latency and resource use for long-context inference, directly affecting serving cost
  and throughput, though the material does not quantify the gains (inference).
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
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/push-based-kv-transfer-to-improve-ttft-and-tpot-for-disaggregated-inference-in-vllm/
  seen_at: '2026-10-20T01:06:54Z'
  metrics: {}
  kind: news
---

# vLLM push-based KV transfer

vLLM is an open-source inference and serving engine for large language models (LLMs). LLM inference has two distinct phases: prefill, which processes the input prompt and builds the key-value (KV) cache, and decode, which uses that cache to generate output one token at a time. These phases have different compute, memory, and scaling characteristics. Prefill-decode (P-D) disaggregation runs them on separate engine instances, allowing each phase to scale and be optimized independently. This can improve resource utilization, throughput, and latency under load. However, it also requires transferring the KV cache from the prefill instance to the decode instance before token generation can begin, making efficient KV transfer critical to time-to-first-token (TTFT). One of the ways vLLM performs this transfer is through the NVIDIA Inference Xfer Library (NIXL) connector , which moves KV blocks over interconnects that support Remote Direct Memory Access (RDMA), such as AWS Elastic Fabric Adapter ( AWS EFA , the low-latency RDMA network used across servers in AWS). On supported instance types , AWS EFA supports GPUDirect RDMA and Neuron Direct RDMA. NIXL can therefore transfer KV blocks directly between GPU or AWS Trainium device memory without staging through host memory. The default mode for NIXL connector

## 笔记


