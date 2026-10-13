---
slug: deploy-decision-models-with-llamacpp-on-amazon-sagemaker-ai
name: Deploy decision models with llama.cpp on Amazon SageMaker AI
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
url: https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai/
canonical_url: https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai
summary: 'Applications that route requests, select agent actions, or assign policy outcomes often need
  scores over a fixed set of choices instead of free-form text. Deploying these decision models with llama.cpp
  on Amazon SageMaker AI gives you a managed path for serving quantized models on CPU or GPU infrastructure.
  This post continues a series on specialized AWS Deep Learning Containers (DLCs) for generative AI inference.
  Previous posts cover WhisperX , vLLM-Omni – Part 1 , and vLLM-Omni – Part 2 . In this post, you first
  use the AWS DLC for llama.cpp to serve OpenAI-compatible chat completions through SageMaker AI InvokeEndpoint
  . You then extend the same runtime with SemIf , formerly OpenJev, which returns probabilities over declared
  options without decoding an answer token. The accompanying code sample includes CPU and GPU deployment
  options. Solution overview Figure 1 shows two deployment paths from the same packaged model. The text-generation
  path uses the AWS DLC for llama.cpp and returns generated responses through the OpenAI-compatible API.
  The structured-decision path builds a child image that replaces the default server with a SemIf adapter
  and returns probabilities for declared options. Figure 1: Run the AWS DLC for llama.cpp or the SemIf
  child image on CPU'
first_seen: '2026-10-13T03:04:22Z'
last_seen: '2026-10-13T03:04:22Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai/
  seen_at: '2026-10-13T03:04:22Z'
  metrics: {}
  kind: news
---

# Deploy decision models with llama.cpp on Amazon SageMaker AI

Applications that route requests, select agent actions, or assign policy outcomes often need scores over a fixed set of choices instead of free-form text. Deploying these decision models with llama.cpp on Amazon SageMaker AI gives you a managed path for serving quantized models on CPU or GPU infrastructure. This post continues a series on specialized AWS Deep Learning Containers (DLCs) for generative AI inference. Previous posts cover WhisperX , vLLM-Omni – Part 1 , and vLLM-Omni – Part 2 . In this post, you first use the AWS DLC for llama.cpp to serve OpenAI-compatible chat completions through SageMaker AI InvokeEndpoint . You then extend the same runtime with SemIf , formerly OpenJev, which returns probabilities over declared options without decoding an answer token. The accompanying code sample includes CPU and GPU deployment options. Solution overview Figure 1 shows two deployment paths from the same packaged model. The text-generation path uses the AWS DLC for llama.cpp and returns generated responses through the OpenAI-compatible API. The structured-decision path builds a child image that replaces the default server with a SemIf adapter and returns probabilities for declared options. Figure 1: Run the AWS DLC for llama.cpp or the SemIf child image on CPU

## 笔记


