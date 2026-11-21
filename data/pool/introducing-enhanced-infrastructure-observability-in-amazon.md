---
slug: introducing-enhanced-infrastructure-observability-in-amazon
name: Introducing enhanced infrastructure observability in Amazon SageMaker HyperPod
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
url: https://aws.amazon.com/blogs/machine-learning/introducing-enhanced-observability-in-amazon-sagemaker-hyperpod-to-diagnose-gpu-training-issues/
canonical_url: https://aws.amazon.com/blogs/machine-learning/introducing-enhanced-observability-in-amazon-sagemaker-hyperpod-to-diagnose-gpu-training-issues
summary: 'Large-scale model training is one of the most expensive workloads you can run on GPUs, and a
  single unhealthy accelerator can stall an entire distributed job. When training throughput drops, the
  hard part is rarely noticing that something is wrong. It is figuring out why and where. Teams often
  spend hours or days sifting through logs and disconnected dashboards to decide whether a slowdown came
  from a throttled GPU, a saturated network link, or a stalled data pipeline on the host. Today, we are
  announcing enhanced observability in Amazon SageMaker HyperPod, a new capability that helps you diagnose
  GPU training issues faster. It brings together diagnostic and profiling capabilities for training workloads
  that run on both Amazon Elastic Kubernetes Service (Amazon EKS) and Slurm orchestrators: Diagnostic
  summary uses Amazon CloudWatch’s DetectGroupOutliers API to compare each GPU in a training job on utilization,
  memory, temperature, power, and SM clock, and flags GPUs that deviate from their peers. Static diagnostic
  rules surface common failure patterns such as GPU hardware faults (XID errors, ECC memory errors), EFA
  throughput drops, thermal throttling, and overheating, so you catch degradation before it affects training.
  Why you need it Distributed training is expensive, and small inefficiencies compound'
first_seen: '2026-11-21T03:14:15Z'
last_seen: '2026-11-21T03:14:15Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/introducing-enhanced-observability-in-amazon-sagemaker-hyperpod-to-diagnose-gpu-training-issues/
  seen_at: '2026-11-21T03:14:15Z'
  metrics: {}
  kind: news
---

# Introducing enhanced infrastructure observability in Amazon SageMaker HyperPod

Large-scale model training is one of the most expensive workloads you can run on GPUs, and a single unhealthy accelerator can stall an entire distributed job. When training throughput drops, the hard part is rarely noticing that something is wrong. It is figuring out why and where. Teams often spend hours or days sifting through logs and disconnected dashboards to decide whether a slowdown came from a throttled GPU, a saturated network link, or a stalled data pipeline on the host. Today, we are announcing enhanced observability in Amazon SageMaker HyperPod, a new capability that helps you diagnose GPU training issues faster. It brings together diagnostic and profiling capabilities for training workloads that run on both Amazon Elastic Kubernetes Service (Amazon EKS) and Slurm orchestrators: Diagnostic summary uses Amazon CloudWatch’s DetectGroupOutliers API to compare each GPU in a training job on utilization, memory, temperature, power, and SM clock, and flags GPUs that deviate from their peers. Static diagnostic rules surface common failure patterns such as GPU hardware faults (XID errors, ECC memory errors), EFA throughput drops, thermal throttling, and overheating, so you catch degradation before it affects training. Why you need it Distributed training is expensive, and small inefficiencies compound

## 笔记


