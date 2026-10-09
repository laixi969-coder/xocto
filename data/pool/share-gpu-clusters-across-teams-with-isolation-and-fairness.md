---
slug: share-gpu-clusters-across-teams-with-isolation-and-fairness
name: Amazon SageMaker HyperPod
builder: ''
category: ''
summary_zh: AWS 于 2026 年 10 月 8 日发布参考架构，让多个团队共享同一个 SageMaker HyperPod EKS 集群：用 IAM Identity Center 做认证，按团队划分
  SageMaker Domain 与 Kubernetes 命名空间做隔离，用 HyperPod Task Governance 做公平调度，并按命名空间分摊成本。对 AI 应用团队而言，这意味着自建
  GPU 集群的隔离与计费方式有了官方可照搬的配置路径，可能降低多团队共用算力的管理成本；这是平台方给出的架构指引，不是独立产品，其实际采用效果仍待观察。
inspiration: ''
summary_en: 'On October 8, 2026, AWS published a reference architecture for sharing one SageMaker HyperPod
  EKS cluster across teams: IAM Identity Center for authentication, per-team SageMaker Domains and Kubernetes
  namespaces for isolation, HyperPod Task Governance for fair scheduling, and namespace-level cost allocation.
  For AI application teams this means an official configuration path for isolation and chargeback on self-managed
  GPU clusters, potentially lowering the management cost of shared compute; it is a platform architecture
  guide rather than an independent product, and actual adoption remains to be seen.'
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
url: https://aws.amazon.com/blogs/machine-learning/share-gpu-clusters-across-teams-with-isolation-and-fairness-using-amazon-sagemaker-hyperpod/
canonical_url: https://aws.amazon.com/blogs/machine-learning/share-gpu-clusters-across-teams-with-isolation-and-fairness-using-amazon-sagemaker-hyperpod
summary: A reference architecture for securely sharing one Amazon SageMaker HyperPod EKS cluster across
  multiple teams, using AWS IAM Identity Center for authentication, per-team SageMaker Domains and Kubernetes
  namespaces for isolation, HyperPod Task Governance for fairness, and namespace-level cost allocation
  for chargeback.
first_seen: '2026-10-08T16:20:04Z'
last_seen: '2026-10-09T02:10:46Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/share-gpu-clusters-across-teams-with-isolation-and-fairness-using-amazon-sagemaker-hyperpod/
  seen_at: '2026-10-09T02:10:46Z'
  metrics: {}
  kind: news
---

# Amazon SageMaker HyperPod

A reference architecture for securely sharing one Amazon SageMaker HyperPod EKS cluster across multiple teams, using AWS IAM Identity Center for authentication, per-team SageMaker Domains and Kubernetes namespaces for isolation, HyperPod Task Governance for fairness, and namespace-level cost allocation for chargeback.

## 笔记


