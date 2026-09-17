---
slug: fault-tolerant-distributed-training-on-amazon-eks-using-nvrx
name: Fault tolerant distributed training on Amazon EKS using NVRx
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
url: https://aws.amazon.com/blogs/machine-learning/fault-tolerant-distributed-training-on-amazon-eks-using-nvrx/
canonical_url: https://aws.amazon.com/blogs/machine-learning/fault-tolerant-distributed-training-on-amazon-eks-using-nvrx
summary: Integrate NVIDIA Resiliency Extension (NVRx) into PyTorch FSDP training on Amazon EKS to overlap
  checkpoint I/O with training and recover from GPU faults in seconds. This post covers async checkpointing,
  in-process restart, and ft_launcher in-job restart, with H100 benchmarks at 2 to 8 nodes showing 99%+
  training efficiency and second-scale recovery.
first_seen: '2026-09-16T18:59:25Z'
last_seen: '2026-09-17T00:32:59Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/fault-tolerant-distributed-training-on-amazon-eks-using-nvrx/
  seen_at: '2026-09-17T00:32:59Z'
  metrics: {}
  kind: news
---

# Fault tolerant distributed training on Amazon EKS using NVRx

Integrate NVIDIA Resiliency Extension (NVRx) into PyTorch FSDP training on Amazon EKS to overlap checkpoint I/O with training and recover from GPU faults in seconds. This post covers async checkpointing, in-process restart, and ft_launcher in-job restart, with H100 benchmarks at 2 to 8 nodes showing 99%+ training efficiency and second-scale recovery.

## 笔记


