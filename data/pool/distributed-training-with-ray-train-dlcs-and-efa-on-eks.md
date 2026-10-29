---
slug: distributed-training-with-ray-train-dlcs-and-efa-on-eks
name: Distributed training with Ray Train DLCs and EFA on EKS
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
url: https://aws.amazon.com/blogs/machine-learning/distributed-training-with-ray-train-dlcs-and-efa-on-eks/
canonical_url: https://aws.amazon.com/blogs/machine-learning/distributed-training-with-ray-train-dlcs-and-efa-on-eks
summary: 'What usually stops PyTorch training from scaling out to a cluster is the container, not the
  model code. Every container needs the same CUDA runtime , a PyTorch build compiled against it, NCCL
  (NVIDIA Collective Communications Library), the Elastic Fabric Adapter (EFA) userspace libraries, the
  AWS OFI NCCL plugin that connects NCCL to EFA, and a Ray version the cluster operator agrees with. Building
  that image and rebuilding it each time one of those pieces moves is a project of its own, and it has
  nothing to do with the model you set out to train. The Ray Train Deep Learning Container (DLC) is that
  image, built by AWS. AWS assembles the stack, tests it as one unit, publishes it in Amazon Elastic Container
  Registry (Amazon ECR) Public and keeps it patched. Figure 1: One EKS cluster with a control plane managed
  by AWS, a CPU system node (m7i.xlarge) running the KubeRay operator and Ray head, and two EFA-enabled
  g6.12xlarge nodes in one Availability Zone. KubeRay builds it from one RayCluster manifest, Ray Train
  places eight workers, one per GPU, and inter-node collectives cross over EFA. Ray runs a job across
  machines as a single cluster with two roles. The'
first_seen: '2026-10-29T01:48:58Z'
last_seen: '2026-10-29T01:48:58Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/distributed-training-with-ray-train-dlcs-and-efa-on-eks/
  seen_at: '2026-10-29T01:48:58Z'
  metrics: {}
  kind: news
---

# Distributed training with Ray Train DLCs and EFA on EKS

What usually stops PyTorch training from scaling out to a cluster is the container, not the model code. Every container needs the same CUDA runtime , a PyTorch build compiled against it, NCCL (NVIDIA Collective Communications Library), the Elastic Fabric Adapter (EFA) userspace libraries, the AWS OFI NCCL plugin that connects NCCL to EFA, and a Ray version the cluster operator agrees with. Building that image and rebuilding it each time one of those pieces moves is a project of its own, and it has nothing to do with the model you set out to train. The Ray Train Deep Learning Container (DLC) is that image, built by AWS. AWS assembles the stack, tests it as one unit, publishes it in Amazon Elastic Container Registry (Amazon ECR) Public and keeps it patched. Figure 1: One EKS cluster with a control plane managed by AWS, a CPU system node (m7i.xlarge) running the KubeRay operator and Ray head, and two EFA-enabled g6.12xlarge nodes in one Availability Zone. KubeRay builds it from one RayCluster manifest, Ray Train places eight workers, one per GPU, and inter-node collectives cross over EFA. Ray runs a job across machines as a single cluster with two roles. The

## 笔记


