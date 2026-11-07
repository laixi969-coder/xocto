---
slug: sagemaker-inference-now-supports-multi-instance-gpu-to-maxim
name: SageMaker Inference now supports Multi-Instance GPU to maximize GPU utilization for model endpoints
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
url: https://aws.amazon.com/blogs/machine-learning/sagemaker-inference-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-model-endpoints/
canonical_url: https://aws.amazon.com/blogs/machine-learning/sagemaker-inference-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-model-endpoints
summary: 'When you deploy a model to a GPU endpoint, the smallest unit of GPU you can request is one whole
  accelerator. This constraint can cost you twice. First, you can’t host more models on an instance than
  it has accelerators. An ml.p4d.24xlarge has eight A100s, so it holds eight models, whether each one
  needs 40 GB or 14 GB. Second, and less obvious, it makes every deployment come down to a choice of which
  full GPU to deploy to. As your concurrency and prompt lengths grow, a full GPU on an older instance
  stops being enough, but a full GPU on a newer one is more than your model can use. You end up either
  under-served or paying for capability you never reach. Today, Amazon SageMaker Inference supports GPU
  partitioning, which uses NVIDIA Multi-Instance GPU (MIG) to divide a physical GPU into independent partitions.
  Each partition receives a fixed share of the GPU’s compute units and a dedicated block of its memory,
  with isolation enforced in hardware. That changes both constraints: you can place a different model
  in each partition, and you can choose a fraction of a newer accelerator instead of a whole one of either
  generation. This post'
first_seen: '2026-11-07T01:57:08Z'
last_seen: '2026-11-07T01:57:08Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/sagemaker-inference-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-model-endpoints/
  seen_at: '2026-11-07T01:57:08Z'
  metrics: {}
  kind: news
---

# SageMaker Inference now supports Multi-Instance GPU to maximize GPU utilization for model endpoints

When you deploy a model to a GPU endpoint, the smallest unit of GPU you can request is one whole accelerator. This constraint can cost you twice. First, you can’t host more models on an instance than it has accelerators. An ml.p4d.24xlarge has eight A100s, so it holds eight models, whether each one needs 40 GB or 14 GB. Second, and less obvious, it makes every deployment come down to a choice of which full GPU to deploy to. As your concurrency and prompt lengths grow, a full GPU on an older instance stops being enough, but a full GPU on a newer one is more than your model can use. You end up either under-served or paying for capability you never reach. Today, Amazon SageMaker Inference supports GPU partitioning, which uses NVIDIA Multi-Instance GPU (MIG) to divide a physical GPU into independent partitions. Each partition receives a fixed share of the GPU’s compute units and a dedicated block of its memory, with isolation enforced in hardware. That changes both constraints: you can place a different model in each partition, and you can choose a fraction of a newer accelerator instead of a whole one of either generation. This post

## 笔记


