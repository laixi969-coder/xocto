---
slug: using-nvidia-runai-gpu-fractioning-on-amazon-eks
name: Using NVIDIA Run:ai GPU Fractioning on Amazon EKS
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
url: https://aws.amazon.com/blogs/machine-learning/using-nvidia-runai-gpu-fractioning-on-amazon-eks/
canonical_url: https://aws.amazon.com/blogs/machine-learning/using-nvidia-runai-gpu-fractioning-on-amazon-eks
summary: 'GPU sharing is not new: Multi-Instance GPU (MIG), time-slicing, and Multi-Process Service (MPS)
  address different isolation and utilization needs. NVIDIA Run:ai GPU Fractioning builds on MPS with
  Kubernetes-integrated scheduling, per-Pod memory contracts, enforcement, and metrics. NVIDIA Run:ai
  is AI workload orchestration software for Kubernetes. Its GPU Fractioning Operator can help several
  teams share one or two GPUs on Amazon Elastic Kubernetes Service (Amazon EKS) . Notebooks, model evaluations,
  and small inference services can leave teams waiting even when GPU memory remains available. In this
  walkthrough’s baseline, the NVIDIA device plugin exposes the single GPU as one nvidia.com/gpu resource,
  with GPU sharing disabled. Two Pods each requesting nvidia.com/gpu: 1 cannot run concurrently on that
  node, even when their combined GPU-memory demand fits. NVIDIA Run:ai GPU Fractioning adds Kubernetes
  scheduling integration, enforced GPU-memory limits, and per-Pod metrics to software-based sharing. The
  approach applies to NVIDIA GPUs that meet the GPU Fractioning Operator’s hardware and software requirements,
  including GPUs without MIG. We use one Amazon Elastic Compute Cloud (Amazon EC2) g5.xlarge instance
  with an NVIDIA A10G Tensor Core GPU as the validated example. Other configurations require compatibility
  checks and validation. NVIDIA announced the open source release of NVIDIA Run:ai on October 13, 2026.'
first_seen: '2026-11-20T03:16:25Z'
last_seen: '2026-11-20T03:16:25Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/using-nvidia-runai-gpu-fractioning-on-amazon-eks/
  seen_at: '2026-11-20T03:16:25Z'
  metrics: {}
  kind: news
---

# Using NVIDIA Run:ai GPU Fractioning on Amazon EKS

GPU sharing is not new: Multi-Instance GPU (MIG), time-slicing, and Multi-Process Service (MPS) address different isolation and utilization needs. NVIDIA Run:ai GPU Fractioning builds on MPS with Kubernetes-integrated scheduling, per-Pod memory contracts, enforcement, and metrics. NVIDIA Run:ai is AI workload orchestration software for Kubernetes. Its GPU Fractioning Operator can help several teams share one or two GPUs on Amazon Elastic Kubernetes Service (Amazon EKS) . Notebooks, model evaluations, and small inference services can leave teams waiting even when GPU memory remains available. In this walkthrough’s baseline, the NVIDIA device plugin exposes the single GPU as one nvidia.com/gpu resource, with GPU sharing disabled. Two Pods each requesting nvidia.com/gpu: 1 cannot run concurrently on that node, even when their combined GPU-memory demand fits. NVIDIA Run:ai GPU Fractioning adds Kubernetes scheduling integration, enforced GPU-memory limits, and per-Pod metrics to software-based sharing. The approach applies to NVIDIA GPUs that meet the GPU Fractioning Operator’s hardware and software requirements, including GPUs without MIG. We use one Amazon Elastic Compute Cloud (Amazon EC2) g5.xlarge instance with an NVIDIA A10G Tensor Core GPU as the validated example. Other configurations require compatibility checks and validation. NVIDIA announced the open source release of NVIDIA Run:ai on October 13, 2026.

## 笔记


