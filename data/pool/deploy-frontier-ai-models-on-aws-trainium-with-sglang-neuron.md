---
slug: deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron
name: Deploy frontier AI models on AWS Trainium with SGLang-Neuron
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
url: https://aws.amazon.com/blogs/machine-learning/deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron/
canonical_url: https://aws.amazon.com/blogs/machine-learning/deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron
summary: 'Today, Amazon announced that SGLang-Neuron is publicly available and can be accessed through
  an AWS Deep Learning Container, released by RadixArk in collaboration with Annapurna Labs. With SGLang-Neuron,
  you can serve models and generate reinforcement learning (RL) rollouts with SGLang on AWS Trainium using
  the same SGLang interface you use today. Trainium is a portfolio of AWS AI chips that delivers strong
  economics for AI training and inference at scale. Now, running SGLang on Trainium follows the SGLang
  workflow you already know: you launch models through SGLang’s server interface and invoke the endpoint
  using the same generation APIs. Underneath that interface, SGLang-Neuron runs on native PyTorch. With
  its out-of-tree plugin design, Trainium support and SGLang core develop independently and iterate faster.
  How SGLang runs on Trainium SGLang-Neuron is an out-of-tree plugin that connects SGLang with AWS Trainium.
  Installing the plugin registers the neuron platform through SGLang’s plugin entry points, and setting
  SGLANG_PLATFORM=neuron selects it when the server starts. SGLang core continues to provide the API server,
  request lifecycle, RadixAttention, and prefix-cache bookkeeping. The plugin implements the Trainium-specific
  models, attention, mixture of experts (MoE), and the graph runner. Figure 1: SGLang-Neuron on AWS Trainium
  TorchNeuron registers Trainium as a native PyTorch'
first_seen: '2026-11-13T02:39:04Z'
last_seen: '2026-11-13T02:39:04Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron/
  seen_at: '2026-11-13T02:39:04Z'
  metrics: {}
  kind: news
---

# Deploy frontier AI models on AWS Trainium with SGLang-Neuron

Today, Amazon announced that SGLang-Neuron is publicly available and can be accessed through an AWS Deep Learning Container, released by RadixArk in collaboration with Annapurna Labs. With SGLang-Neuron, you can serve models and generate reinforcement learning (RL) rollouts with SGLang on AWS Trainium using the same SGLang interface you use today. Trainium is a portfolio of AWS AI chips that delivers strong economics for AI training and inference at scale. Now, running SGLang on Trainium follows the SGLang workflow you already know: you launch models through SGLang’s server interface and invoke the endpoint using the same generation APIs. Underneath that interface, SGLang-Neuron runs on native PyTorch. With its out-of-tree plugin design, Trainium support and SGLang core develop independently and iterate faster. How SGLang runs on Trainium SGLang-Neuron is an out-of-tree plugin that connects SGLang with AWS Trainium. Installing the plugin registers the neuron platform through SGLang’s plugin entry points, and setting SGLANG_PLATFORM=neuron selects it when the server starts. SGLang core continues to provide the API server, request lifecycle, RadixAttention, and prefix-cache bookkeeping. The plugin implements the Trainium-specific models, attention, mixture of experts (MoE), and the graph runner. Figure 1: SGLang-Neuron on AWS Trainium TorchNeuron registers Trainium as a native PyTorch

## 笔记


