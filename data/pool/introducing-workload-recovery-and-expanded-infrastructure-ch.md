---
slug: introducing-workload-recovery-and-expanded-infrastructure-ch
name: Introducing workload recovery and expanded infrastructure checks on Amazon SageMaker HyperPod
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
url: https://aws.amazon.com/blogs/machine-learning/introducing-workload-recovery-and-expanded-infrastructure-checks-on-amazon-sagemaker-hyperpod/
canonical_url: https://aws.amazon.com/blogs/machine-learning/introducing-workload-recovery-and-expanded-infrastructure-checks-on-amazon-sagemaker-hyperpod
summary: Large training jobs can fail even when every node looks healthy. A GPU with a subtle fault can
  pass its stress tests and still return wrong values. When a job stalls on an NCCL timeout, it keeps
  its GPUs, and Slurm still shows it as running. If a device plugin crashes on one node, the job fails
  with an error that never mentions the plugin. Teams usually find these problems only after the loss
  diverges or the job fails, and by then the compute is spent. Each of these failures lowers goodput,
  the share of your cluster’s time that goes to useful training. Today, we’re introducing workload recovery
  and infrastructure checks on Amazon SageMaker HyperPod that catch these failures sooner and raise the
  goodput of your training workloads. SageMaker HyperPod already handles nodes that report hardware faults.
  The health monitoring agent (HMA) watches each node for GPU errors, deep health checks test nodes during
  provisioning, and automatic node recovery reboots or replaces faulty hardware. These features look at
  one node’s hardware at a time. They can’t tell whether the GPUs train correctly, whether a job is still
  making progress, or whether the Kubernetes components a job depends on are working.
first_seen: '2026-11-19T03:28:37Z'
last_seen: '2026-11-19T03:28:37Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/introducing-workload-recovery-and-expanded-infrastructure-checks-on-amazon-sagemaker-hyperpod/
  seen_at: '2026-11-19T03:28:37Z'
  metrics: {}
  kind: news
---

# Introducing workload recovery and expanded infrastructure checks on Amazon SageMaker HyperPod

Large training jobs can fail even when every node looks healthy. A GPU with a subtle fault can pass its stress tests and still return wrong values. When a job stalls on an NCCL timeout, it keeps its GPUs, and Slurm still shows it as running. If a device plugin crashes on one node, the job fails with an error that never mentions the plugin. Teams usually find these problems only after the loss diverges or the job fails, and by then the compute is spent. Each of these failures lowers goodput, the share of your cluster’s time that goes to useful training. Today, we’re introducing workload recovery and infrastructure checks on Amazon SageMaker HyperPod that catch these failures sooner and raise the goodput of your training workloads. SageMaker HyperPod already handles nodes that report hardware faults. The health monitoring agent (HMA) watches each node for GPU errors, deep health checks test nodes during provisioning, and automatic node recovery reboots or replaces faulty hardware. These features look at one node’s hardware at a time. They can’t tell whether the GPUs train correctly, whether a job is still making progress, or whether the Kubernetes components a job depends on are working.

## 笔记


