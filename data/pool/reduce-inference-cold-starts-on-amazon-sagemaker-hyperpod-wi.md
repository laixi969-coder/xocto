---
slug: reduce-inference-cold-starts-on-amazon-sagemaker-hyperpod-wi
name: Amazon SageMaker HyperPod
builder: ''
category: ''
summary_zh: AWS 于 2026 年 9 月 10 日宣布 Amazon SageMaker HyperPod 支持推理模型缓存，将模型权重和容器镜像预加载到集群节点，使 pod 直接读取本地
  NVMe 存储而非通过网络下载，推理冷启动从数十分钟缩短到秒级。这降低了在 SageMaker 上部署大模型推理的等待时间和运维成本，尤其有利于频繁更新模型和弹性扩缩容的 AI 应用场景。
inspiration: ''
summary_en: On September 10, 2026, AWS announced that Amazon SageMaker HyperPod now supports model caching
  for inference, pre-loading model weights and container images onto cluster nodes so pods read from local
  NVMe storage instead of downloading over the network, cutting inference cold starts from tens of minutes
  to seconds. This reduces wait times and operational overhead for serving large models on SageMaker,
  particularly benefiting AI applications with frequent model updates and elastic scaling.
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
url: https://aws.amazon.com/blogs/machine-learning/reduce-inference-cold-starts-on-amazon-sagemaker-hyperpod-with-model-caching/
canonical_url: https://aws.amazon.com/blogs/machine-learning/reduce-inference-cold-starts-on-amazon-sagemaker-hyperpod-with-model-caching
summary: Amazon SageMaker HyperPod now supports model caching for inference, which pre-loads model weights
  and container images onto cluster nodes so pods read from local NVMe storage instead of downloading
  over the network. Learn how model caching cuts cold starts from tens of minutes to seconds, how it works,
  and how to enable it.
first_seen: '2026-09-10T21:37:49Z'
last_seen: '2026-09-11T00:10:51Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/reduce-inference-cold-starts-on-amazon-sagemaker-hyperpod-with-model-caching/
  seen_at: '2026-09-11T00:10:51Z'
  metrics: {}
  kind: news
---

# Amazon SageMaker HyperPod

Amazon SageMaker HyperPod now supports model caching for inference, which pre-loads model weights and container images onto cluster nodes so pods read from local NVMe storage instead of downloading over the network. Learn how model caching cuts cold starts from tens of minutes to seconds, how it works, and how to enable it.

## 笔记


