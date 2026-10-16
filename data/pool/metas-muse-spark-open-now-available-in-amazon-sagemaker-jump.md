---
slug: metas-muse-spark-open-now-available-in-amazon-sagemaker-jump
name: Muse Spark Open
builder: ''
category: ''
summary_zh: 这是模型发布与托管渠道变化，不是独立应用：Meta 把编码优化模型放进 AWS 托管目录，开发者可直接部署调用。对 AI 应用的含义是编码类 agent 的模型供给又多一条低成本、免运维的采购路径，托管平台之间的模型上架竞争加剧；这是推断，尚无采用或付费数据。
inspiration: ''
summary_en: 'This is a model release and hosting-channel change, not a standalone application: Meta placed
  a coding-optimized model into AWS''s managed catalog for direct deployment. For AI applications it means
  one more low-cost, ops-free procurement path for coding agents and sharper competition among hosting
  platforms; this is inference, with no adoption or payment data yet.'
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
url: https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart/
canonical_url: https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart
summary: 'Muse Spark Open, Meta’s coding-optimized open-weight model, is now available in Amazon SageMaker
  JumpStart , the machine learning (ML) hub of Amazon SageMaker AI . The model was trained on real developer
  workflows, such as multi-file refactors and long debugging sessions, and it supports a context window
  of 1 million tokens. You can deploy it to a SageMaker AI endpoint in your own AWS account in a few steps,
  without managing the serving infrastructure yourself. SageMaker JumpStart offers two variants: BF16
  ( Muse-Spark-Open-816B-A42B ) and NVFP4 quantized ( Muse-Spark-Open-816B-A42B-NVFP4 ). In this post,
  we introduce Muse Spark Open and show you how to deploy the model with Amazon SageMaker Studio and the
  SageMaker Python SDK , send it a first inference request, and clean up. Overview of Muse Spark Open
  Meta describes Muse Spark Open as a coding-optimized model trained for agentic coding workflows, with
  a focus on first-attempt accuracy, tool calling, and understanding of large codebases. It’s a reasoning
  model, and it accepts text, images, documents, audio, and audio-video as input and returns text. Muse
  Spark Open uses a mixture-of-experts (MoE) architecture with 816 billion total parameters, of which
  42 billion are active for each token. The model holds'
first_seen: '2026-10-16T00:25:39Z'
last_seen: '2026-10-16T00:25:39Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart/
  seen_at: '2026-10-16T00:25:39Z'
  metrics: {}
  kind: news
---

# Muse Spark Open

Muse Spark Open, Meta’s coding-optimized open-weight model, is now available in Amazon SageMaker JumpStart , the machine learning (ML) hub of Amazon SageMaker AI . The model was trained on real developer workflows, such as multi-file refactors and long debugging sessions, and it supports a context window of 1 million tokens. You can deploy it to a SageMaker AI endpoint in your own AWS account in a few steps, without managing the serving infrastructure yourself. SageMaker JumpStart offers two variants: BF16 ( Muse-Spark-Open-816B-A42B ) and NVFP4 quantized ( Muse-Spark-Open-816B-A42B-NVFP4 ). In this post, we introduce Muse Spark Open and show you how to deploy the model with Amazon SageMaker Studio and the SageMaker Python SDK , send it a first inference request, and clean up. Overview of Muse Spark Open Meta describes Muse Spark Open as a coding-optimized model trained for agentic coding workflows, with a focus on first-attempt accuracy, tool calling, and understanding of large codebases. It’s a reasoning model, and it accepts text, images, documents, audio, and audio-video as input and returns text. Muse Spark Open uses a mixture-of-experts (MoE) architecture with 816 billion total parameters, of which 42 billion are active for each token. The model holds

## 笔记


