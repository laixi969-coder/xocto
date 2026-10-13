---
slug: accessing-openai-gpt-models-on-amazon-bedrock-with-global-cr
name: Amazon Bedrock
builder: ''
category: ''
summary_zh: 这是云平台侧的模型分发与容量调度变化，不是独立产品：AWS 把 OpenAI 的 GPT-6 系列模型通过跨区域推理配置到东南亚与台湾等区域，缓解单区域容量不足导致的限流。对当地团队而言，模型获取路径从单一区域扩展到多区域路由，但具体成本、延迟与配额影响仍待核验。
inspiration: ''
summary_en: 'This is a cloud-platform model distribution and capacity-routing change, not a standalone
  product: AWS exposes OpenAI''s GPT-6 family through cross-Region inference profiles in Southeast Asia
  and Taiwan to relieve single-Region throttling. For local teams the model access path widens from one
  Region to multi-Region routing, though cost, latency and quota effects remain unverified.'
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
url: https://aws.amazon.com/blogs/machine-learning/accessing-openai-gpt-models-on-amazon-bedrock-with-global-cross-region-inference-in-thailand-malaysia-singapore-indonesia-and-taiwan/
canonical_url: https://aws.amazon.com/blogs/machine-learning/accessing-openai-gpt-models-on-amazon-bedrock-with-global-cross-region-inference-in-thailand-malaysia-singapore-indonesia-and-taiwan
summary: Single-Region inference can throttle when demand exceeds local capacity. Teams in Thailand, Malaysia,
  Singapore, Indonesia, and Taiwan need access to the newest OpenAI models beyond that capacity. Amazon
  Bedrock offers OpenAI GPT-6 Sol and GPT-6 Luna through global cross-Region inference from all five AWS
  Regions, and GPT-6 Astra from Asia Pacific (Singapore). This post shows you how to configure the call,
  set permissions, and monitor inference from your source Region. GPT-6 Sol, GPT-6 Luna, and GPT-6 Astra
  are all available through global cross-Region inference from the preceding Regions, on the bedrock-runtime
  endpoint. See Cross-Region inference in the Amazon Bedrock User Guide. For the full list of source and
  destination Regions in each profile, see Supported Regions and models for inference profiles . In this
  post, we introduce the global cross-Region inference profiles and invoke them from Asia Pacific (Singapore)
  using the Converse API, the OpenAI-compatible APIs, and coding clients. We then cover the AWS Identity
  and Access Management (IAM) and service control policy (SCP) configuration, quota management, and monitoring.
  Global cross-Region inference profiles for OpenAI GPT-6 The GPT-6 family offers three models, each available
  through global cross-Region inference. GPT-6 Sol brings strong reasoning and coding capabilities to
  complex tasks performed
first_seen: '2026-10-13T03:04:22Z'
last_seen: '2026-10-13T03:04:22Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/accessing-openai-gpt-models-on-amazon-bedrock-with-global-cross-region-inference-in-thailand-malaysia-singapore-indonesia-and-taiwan/
  seen_at: '2026-10-13T03:04:22Z'
  metrics: {}
  kind: news
---

# Amazon Bedrock

Single-Region inference can throttle when demand exceeds local capacity. Teams in Thailand, Malaysia, Singapore, Indonesia, and Taiwan need access to the newest OpenAI models beyond that capacity. Amazon Bedrock offers OpenAI GPT-6 Sol and GPT-6 Luna through global cross-Region inference from all five AWS Regions, and GPT-6 Astra from Asia Pacific (Singapore). This post shows you how to configure the call, set permissions, and monitor inference from your source Region. GPT-6 Sol, GPT-6 Luna, and GPT-6 Astra are all available through global cross-Region inference from the preceding Regions, on the bedrock-runtime endpoint. See Cross-Region inference in the Amazon Bedrock User Guide. For the full list of source and destination Regions in each profile, see Supported Regions and models for inference profiles . In this post, we introduce the global cross-Region inference profiles and invoke them from Asia Pacific (Singapore) using the Converse API, the OpenAI-compatible APIs, and coding clients. We then cover the AWS Identity and Access Management (IAM) and service control policy (SCP) configuration, quota management, and monitoring. Global cross-Region inference profiles for OpenAI GPT-6 The GPT-6 family offers three models, each available through global cross-Region inference. GPT-6 Sol brings strong reasoning and coding capabilities to complex tasks performed

## 笔记


