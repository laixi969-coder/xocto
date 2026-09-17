---
slug: fault-tolerant-distributed-training-on-amazon-eks-using-nvrx
name: NVIDIA Resiliency Extension (NVRx)
builder: ''
category: ''
summary_zh: 这是云厂商与芯片厂商联合给出的分布式训练容错方案说明，不是独立产品：它面向在 EKS 上跑多节点大模型训练的工程团队，把异步 checkpoint、进程内重启和作业内重启组合起来，让
  GPU 故障后不必整批重跑。具体交付形态与商业边界仍待核验。
inspiration: ''
summary_en: 'This is a joint cloud-vendor and chip-vendor description of fault-tolerant distributed training,
  not a standalone product: it targets engineering teams running multi-node large-model training on EKS,
  combining asynchronous checkpointing, in-process restart and in-job restart so a GPU fault does not
  force a full rerun. The concrete delivery form and commercial boundary remain unverified.'
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
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/fault-tolerant-distributed-training-on-amazon-eks-using-nvrx/
  seen_at: '2026-09-17T00:32:59Z'
  metrics: {}
  kind: news
---

# NVIDIA Resiliency Extension (NVRx)

Integrate NVIDIA Resiliency Extension (NVRx) into PyTorch FSDP training on Amazon EKS to overlap checkpoint I/O with training and recover from GPU faults in seconds. This post covers async checkpointing, in-process restart, and ft_launcher in-job restart, with H100 benchmarks at 2 to 8 nodes showing 99%+ training efficiency and second-scale recovery.

## 笔记


