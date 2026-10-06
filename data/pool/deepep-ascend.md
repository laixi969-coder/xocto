---
slug: deepep-ascend
name: DeepEP-Ascend
builder: deepseek-ai
category: 基础层
summary_zh: 在昇腾 NPU 集群上做分布式训练或推理的工程师，原本要自己处理多卡之间的通信与集合通信调优；该库接收训练/推理框架的通信请求，在昇腾硬件上执行高性能通信动作，最终交付可被训练或推理流程直接调用的通信能力，具体支持范围与性能数据仍待核验。
inspiration: 趋势是国产算力软件栈开始由模型厂商自己补齐通信这一层，而不是等硬件厂商的通用库。切入可考虑为使用昇腾集群的行业客户做训练/推理性能调优与迁移服务，卖的是可核对的吞吐与稳定性结果，而非又一个库。
summary_en: Engineers running distributed training or inference on Ascend NPU clusters previously had
  to handle inter-card communication and collective tuning themselves; this library takes communication
  requests from training or inference frameworks and performs high-performance communication on Ascend
  hardware, delivering a communication capability callable directly by those pipelines, though supported
  scope and performance figures still need verification.
inspiration_en: The trend is that model vendors, not only hardware vendors, are filling in the communication
  layer of domestic accelerator software stacks. An opening is to offer Ascend-cluster training and inference
  tuning or migration services to industry customers, selling verifiable throughput and stability outcomes
  rather than another library.
priority_review: true
project_type: open_source
industries:
- 云计算与数据中心
- 半导体
- 人工智能基础设施
industries_en:
- Cloud computing and data centers
- Semiconductors
- AI infrastructure
jobs:
- AI 基础设施工程师
- 分布式训练工程师
- 国产算力适配工程师
jobs_en:
- AI infrastructure engineer
- Distributed training engineer
- Domestic accelerator adaptation engineer
regions:
- 中国
regions_en:
- China
open_source: true
url: https://github.com/deepseek-ai/DeepEP-Ascend
canonical_url: https://github.com/deepseek-ai/DeepEP-Ascend
summary: A high-performance communication library for machine learning training and inference on Huawei
  Ascend NPUs.
first_seen: '2026-09-30T00:44:59Z'
last_seen: '2026-10-06T02:18:35Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/deepseek-ai/DeepEP-Ascend
  seen_at: '2026-10-06T02:18:35Z'
  metrics:
    stars: 222
    forks: 23
    open_issues: 3
  kind: product
---

# DeepEP-Ascend

A high-performance communication library for machine learning training and inference on Huawei Ascend NPUs.

## 笔记


