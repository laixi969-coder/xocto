---
slug: building-a-self-service-llm-gateway-with-amazon-bedrock-and
name: Building a self-service LLM gateway with Amazon Bedrock and LiteLLM
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
url: https://aws.amazon.com/blogs/machine-learning/building-a-self-service-llm-gateway-with-amazon-bedrock-and-litellm/
canonical_url: https://aws.amazon.com/blogs/machine-learning/building-a-self-service-llm-gateway-with-amazon-bedrock-and-litellm
summary: Developers want AI coding assistants with minimal setup. With a large language model (LLM) gateway
  and LiteLLM, they can quickly access foundation models (FMs) available on Amazon Bedrock while you gain
  visibility and usage control. Platform teams need to monitor latency and errors, finance teams need
  to attribute inference costs to teams and projects, and security teams need consistent access controls.
  An LLM gateway can help address these needs by providing a centrally managed access point to the models
  that power coding assistants. In this post, we show how to build a self-service LLM gateway using Amazon
  Bedrock Application Inference Profiles with LiteLLM running on AWS Fargate to abstract Amazon Bedrock
  behind an OpenAI-compatible API. With this pattern, developers can access foundation models through
  a single API with a dedicated key while you gain per-user cost controls and model performance observability.
  By the end, you will understand the pattern well enough to build your own version from the illustrative
  snippets and AWS Cloud Development Kit (AWS CDK) constructs. This post uses Claude Sonnet and Claude
  Haiku models for example purposes. For a list of models and availability by AWS Region, see Supported
  models by AWS Region in Amazon Bedrock .
first_seen: '2026-11-13T02:39:04Z'
last_seen: '2026-11-13T02:39:04Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/building-a-self-service-llm-gateway-with-amazon-bedrock-and-litellm/
  seen_at: '2026-11-13T02:39:04Z'
  metrics: {}
  kind: news
---

# Building a self-service LLM gateway with Amazon Bedrock and LiteLLM

Developers want AI coding assistants with minimal setup. With a large language model (LLM) gateway and LiteLLM, they can quickly access foundation models (FMs) available on Amazon Bedrock while you gain visibility and usage control. Platform teams need to monitor latency and errors, finance teams need to attribute inference costs to teams and projects, and security teams need consistent access controls. An LLM gateway can help address these needs by providing a centrally managed access point to the models that power coding assistants. In this post, we show how to build a self-service LLM gateway using Amazon Bedrock Application Inference Profiles with LiteLLM running on AWS Fargate to abstract Amazon Bedrock behind an OpenAI-compatible API. With this pattern, developers can access foundation models through a single API with a dedicated key while you gain per-user cost controls and model performance observability. By the end, you will understand the pattern well enough to build your own version from the illustrative snippets and AWS Cloud Development Kit (AWS CDK) constructs. This post uses Claude Sonnet and Claude Haiku models for example purposes. For a list of models and availability by AWS Region, see Supported models by AWS Region in Amazon Bedrock .

## 笔记


