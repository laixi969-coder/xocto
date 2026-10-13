---
slug: run-multi-node-inference-workloads-using-ray-llm-deep-learni
name: Ray LLM Deep Learning Containers
builder: ''
category: ''
summary_zh: 这是 AWS 官方发布的一篇部署说明，不是独立产品：它讲的是在 Amazon EKS 上把单个大模型拆到两块 GPU 节点上跑推理，prefill 与 decode 分节点、对外只暴露一个
  OpenAI 兼容端点，容器里已带好 CUDA 等 GPU 依赖。对自建推理的团队来说，它减少的是自己拼依赖链和调多节点并行的那部分工作。
inspiration: ''
summary_en: 'This is an AWS official deployment walkthrough rather than a standalone product: it covers
  running one large model across two GPU nodes on Amazon EKS, with prefill and decode on separate nodes
  behind a single OpenAI-compatible endpoint, and CUDA and other GPU dependencies pre-bundled in the container.
  For teams self-hosting inference, it removes part of the work of assembling the dependency chain and
  tuning multi-node parallelism.'
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
url: https://aws.amazon.com/blogs/machine-learning/run-multi-node-inference-workloads-using-ray-llm-deep-learning-containers/
canonical_url: https://aws.amazon.com/blogs/machine-learning/run-multi-node-inference-workloads-using-ray-llm-deep-learning-containers
summary: 'This post shows how to deploy one large language model (LLM) across two GPU nodes on Amazon
  Elastic Kubernetes Service (Amazon EKS) with the multi-node Ray LLM Deep Learning Containers . It uses
  separate prefill and decode nodes behind one OpenAI-compatible endpoint. This kind of multi-node setup
  is common for tensor, pipeline, and data parallelism, as well as prefill/decode disaggregation inference
  workloads. In a previous post , we introduced the Ray Serve DLC and used it to stand up a small model
  behind an HTTP endpoint on a single GPU node. You had a working inference endpoint, and the container
  keeps the GPU stack compatible, including CUDA libraries, so you did not need to write boilerplate code.
  Ray is a distributed compute framework, so Ray Serve deployments can span multiple nodes. Customers
  use multi-node Ray Serve for several reasons. Some want to run foundation or open-weight models that
  are too large for a single GPU. Others need more throughput than one replica can deliver. Still others
  want to separate the two phases of inference to improve performance. In each case, customers must build
  the dependency chain themselves: choosing compatible libraries for the GPU stack and debugging issues
  when a component'
first_seen: '2026-10-13T03:04:22Z'
last_seen: '2026-10-13T03:04:22Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/run-multi-node-inference-workloads-using-ray-llm-deep-learning-containers/
  seen_at: '2026-10-13T03:04:22Z'
  metrics: {}
  kind: news
---

# Ray LLM Deep Learning Containers

This post shows how to deploy one large language model (LLM) across two GPU nodes on Amazon Elastic Kubernetes Service (Amazon EKS) with the multi-node Ray LLM Deep Learning Containers . It uses separate prefill and decode nodes behind one OpenAI-compatible endpoint. This kind of multi-node setup is common for tensor, pipeline, and data parallelism, as well as prefill/decode disaggregation inference workloads. In a previous post , we introduced the Ray Serve DLC and used it to stand up a small model behind an HTTP endpoint on a single GPU node. You had a working inference endpoint, and the container keeps the GPU stack compatible, including CUDA libraries, so you did not need to write boilerplate code. Ray is a distributed compute framework, so Ray Serve deployments can span multiple nodes. Customers use multi-node Ray Serve for several reasons. Some want to run foundation or open-weight models that are too large for a single GPU. Others need more throughput than one replica can deliver. Still others want to separate the two phases of inference to improve performance. In each case, customers must build the dependency chain themselves: choosing compatible libraries for the GPU stack and debugging issues when a component

## 笔记


