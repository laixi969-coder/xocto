---
slug: introducing-amazon-sagemaker-hyperpod-global-inference-gatew
name: 'Introducing Amazon SageMaker HyperPod Global Inference Gateway: One endpoint across Regions and
  clusters'
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
url: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-global-inference-gateway-one-endpoint-across-regions-and-clusters/
canonical_url: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-global-inference-gateway-one-endpoint-across-regions-and-clusters
summary: 'During a traffic peak, a request can sit in a queue on a saturated HyperPod cluster while GPUs
  on another cluster, sometimes in another AWS Region, sit idle. You have already paid for that capacity,
  but your requests can’t reach it. In Introducing Amazon SageMaker HyperPod Inference Gateway , we showed
  how the Inference Gateway gives each Amazon SageMaker HyperPod cluster a single, GPU-aware endpoint.
  It reads real-time signals such as key-value (KV) cache utilization and queue depth to place every request
  on the best-suited pod. That solves routing inside one cluster, but not across clusters. Today, SageMaker
  HyperPod introduces the Global Inference Gateway. It is one SageMaker-managed gateway that routes across
  every cluster you register, in one Region or across Regions. The gateway picks the cluster and carries
  the request over the AWS backbone, with automatic failover and authentication through AWS Signature
  Version 4 (SigV4) and AWS Identity and Access Management (IAM). Inside each cluster, the Inference Gateway
  keeps picking the pod, unchanged. The Global Inference Gateway is the second tier of the architecture
  we described in part 1. The challenge: Capacity spread across clusters and Regions Models are getting
  larger, and the GPU capacity to serve them is'
first_seen: '2026-11-21T03:14:15Z'
last_seen: '2026-11-21T03:14:15Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-global-inference-gateway-one-endpoint-across-regions-and-clusters/
  seen_at: '2026-11-21T03:14:15Z'
  metrics: {}
  kind: news
---

# Introducing Amazon SageMaker HyperPod Global Inference Gateway: One endpoint across Regions and clusters

During a traffic peak, a request can sit in a queue on a saturated HyperPod cluster while GPUs on another cluster, sometimes in another AWS Region, sit idle. You have already paid for that capacity, but your requests can’t reach it. In Introducing Amazon SageMaker HyperPod Inference Gateway , we showed how the Inference Gateway gives each Amazon SageMaker HyperPod cluster a single, GPU-aware endpoint. It reads real-time signals such as key-value (KV) cache utilization and queue depth to place every request on the best-suited pod. That solves routing inside one cluster, but not across clusters. Today, SageMaker HyperPod introduces the Global Inference Gateway. It is one SageMaker-managed gateway that routes across every cluster you register, in one Region or across Regions. The gateway picks the cluster and carries the request over the AWS backbone, with automatic failover and authentication through AWS Signature Version 4 (SigV4) and AWS Identity and Access Management (IAM). Inside each cluster, the Inference Gateway keeps picking the pod, unchanged. The Global Inference Gateway is the second tier of the architecture we described in part 1. The challenge: Capacity spread across clusters and Regions Models are getting larger, and the GPU capacity to serve them is

## 笔记


