---
slug: introducing-managed-cluster-extensions-for-observability-and
name: Introducing managed cluster extensions for observability and user management in Amazon SageMaker
  HyperPod Slurm
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
url: https://aws.amazon.com/blogs/machine-learning/introducing-managed-cluster-extensions-for-observability-and-user-management-in-amazon-sagemaker-hyperpod-slurm/
canonical_url: https://aws.amazon.com/blogs/machine-learning/introducing-managed-cluster-extensions-for-observability-and-user-management-in-amazon-sagemaker-hyperpod-slurm
summary: Keeping a shared Slurm cluster for foundation model development in sync entails keeping several
  separately maintained pieces of configuration matched to what’s running on the nodes. The cluster’s
  shape lives on multiple configuration files, its software in custom scripts, its network topology in
  files that must be edited as nodes change, and its users in a roster that an administrator must maintain
  and rerun. Over time these pieces drift away from what’s actually running, and nothing tells you when
  they do. We believe cluster configurations should be managed the way you manage the rest of your AWS
  infrastructure. You declare what you want through an API or the console, AWS validates it before it’s
  applied, the cluster is kept in that state continuously, and you can see whether it’s working. During
  2026, Amazon SageMaker HyperPod brought that approach to Slurm clusters, with API-driven Slurm configuration,
  AMI-based configuration, continuous provisioning, automatic topology management, and deep health checks.
  Today, we launched cluster extensions, which bring the same approach to the software and settings on
  running nodes, with managed extensions for observability and user management. However, through all of
  it, you still keep full access to every node in your cluster, including the
first_seen: '2026-11-21T03:14:15Z'
last_seen: '2026-11-21T03:14:15Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/introducing-managed-cluster-extensions-for-observability-and-user-management-in-amazon-sagemaker-hyperpod-slurm/
  seen_at: '2026-11-21T03:14:15Z'
  metrics: {}
  kind: news
---

# Introducing managed cluster extensions for observability and user management in Amazon SageMaker HyperPod Slurm

Keeping a shared Slurm cluster for foundation model development in sync entails keeping several separately maintained pieces of configuration matched to what’s running on the nodes. The cluster’s shape lives on multiple configuration files, its software in custom scripts, its network topology in files that must be edited as nodes change, and its users in a roster that an administrator must maintain and rerun. Over time these pieces drift away from what’s actually running, and nothing tells you when they do. We believe cluster configurations should be managed the way you manage the rest of your AWS infrastructure. You declare what you want through an API or the console, AWS validates it before it’s applied, the cluster is kept in that state continuously, and you can see whether it’s working. During 2026, Amazon SageMaker HyperPod brought that approach to Slurm clusters, with API-driven Slurm configuration, AMI-based configuration, continuous provisioning, automatic topology management, and deep health checks. Today, we launched cluster extensions, which bring the same approach to the software and settings on running nodes, with managed extensions for observability and user management. However, through all of it, you still keep full access to every node in your cluster, including the

## 笔记


