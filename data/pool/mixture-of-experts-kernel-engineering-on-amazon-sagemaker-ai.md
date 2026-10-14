---
slug: mixture-of-experts-kernel-engineering-on-amazon-sagemaker-ai
name: Mixture-of-Experts kernel engineering on Amazon SageMaker AI
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
url: https://aws.amazon.com/blogs/machine-learning/mixture-of-experts-kernel-engineering-on-amazon-sagemaker-ai/
canonical_url: https://aws.amazon.com/blogs/machine-learning/mixture-of-experts-kernel-engineering-on-amazon-sagemaker-ai
summary: Mixture-of-Experts (MoE) is a sparsely-activated architecture that scales large language model
  (LLM) capacity while keeping per-token compute low. Because its operations account for a large share
  of total compute time, inefficiencies there directly raise request latency and cost. Therefore, optimizing
  MoE operations through kernel engineering offers the largest opportunity for performance gains. Fused
  MoE is a key optimization technique for the MoE architecture. A fused MoE system merges token routing,
  data shuffling, and specialized network calculations into a single batched operation on the GPU. This
  replaces executing those routing and expert computations as separate, sequential loop operations. While
  this provides latency advantages, it also brings complexity in kernel implementations and debugging
  capability. High GPU utilization for this architecture requires hardware-specific optimizations. In
  this post, we describe the different kernel optimizations we implemented for fused MoE models and show
  you how you can benefit from this work. We used a representative MoE model as our primary example. Swap-AB
  for WGMMA utilization To maximize tensor processing throughput, the NVIDIA Hopper architecture relies
  on the Warp Group Matrix Multiply Accumulate (WGMMA) instruction protocol, which executes collectively
  across a cooperative warpgroup of 128 threads. This operand asymmetry is fundamentally an instruction
  set architecture (ISA)-level
first_seen: '2026-10-14T01:14:22Z'
last_seen: '2026-10-14T01:14:22Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/mixture-of-experts-kernel-engineering-on-amazon-sagemaker-ai/
  seen_at: '2026-10-14T01:14:22Z'
  metrics: {}
  kind: news
---

# Mixture-of-Experts kernel engineering on Amazon SageMaker AI

Mixture-of-Experts (MoE) is a sparsely-activated architecture that scales large language model (LLM) capacity while keeping per-token compute low. Because its operations account for a large share of total compute time, inefficiencies there directly raise request latency and cost. Therefore, optimizing MoE operations through kernel engineering offers the largest opportunity for performance gains. Fused MoE is a key optimization technique for the MoE architecture. A fused MoE system merges token routing, data shuffling, and specialized network calculations into a single batched operation on the GPU. This replaces executing those routing and expert computations as separate, sequential loop operations. While this provides latency advantages, it also brings complexity in kernel implementations and debugging capability. High GPU utilization for this architecture requires hardware-specific optimizations. In this post, we describe the different kernel optimizations we implemented for fused MoE models and show you how you can benefit from this work. We used a representative MoE model as our primary example. Swap-AB for WGMMA utilization To maximize tensor processing throughput, the NVIDIA Hopper architecture relies on the Warp Group Matrix Multiply Accumulate (WGMMA) instruction protocol, which executes collectively across a cooperative warpgroup of 128 threads. This operand asymmetry is fundamentally an instruction set architecture (ISA)-level

## 笔记


