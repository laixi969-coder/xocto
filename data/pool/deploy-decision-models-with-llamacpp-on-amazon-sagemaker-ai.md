---
slug: deploy-decision-models-with-llamacpp-on-amazon-sagemaker-ai
name: Amazon SageMaker AI
builder: ''
category: ''
summary_zh: AWS 在 2026 年 10 月 12 日的技术文章中给出在 Amazon SageMaker AI 上部署决策模型的两条路径：一条用 llama.cpp 容器提供 OpenAI
  兼容的文本生成接口，另一条用 SemIf 适配器对预先声明的选项直接返回概率，避免解码答案 token，示例代码同时覆盖 CPU 与 GPU。这是云厂商对推理部署方式的一次能力补充，不是独立产品。
inspiration: ''
summary_en: 'In a 2026-10-12 technical post AWS describes two ways to deploy decision models on Amazon
  SageMaker AI: one uses the llama.cpp container to serve an OpenAI-compatible text generation endpoint,
  the other uses a SemIf adapter to return probabilities over declared options without decoding an answer
  token, with sample code for both CPU and GPU. This is a cloud vendor capability addition for inference
  deployment, not an independent product.'
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
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai/
  seen_at: '2026-10-13T03:04:22Z'
  metrics: {}
  kind: news
---

# Amazon SageMaker AI

Applications that route requests, select agent actions, or assign policy outcomes often need scores over a fixed set of choices instead of free-form text. Deploying these decision models with llama.cpp on Amazon SageMaker AI gives you a managed path for serving quantized models on CPU or GPU infrastructure. This post continues a series on specialized AWS Deep Learning Containers (DLCs) for generative AI inference. Previous posts cover WhisperX , vLLM-Omni – Part 1 , and vLLM-Omni – Part 2 . In this post, you first use the AWS DLC for llama.cpp to serve OpenAI-compatible chat completions through SageMaker AI InvokeEndpoint . You then extend the same runtime with SemIf , formerly OpenJev, which returns probabilities over declared options without decoding an answer token. The accompanying code sample includes CPU and GPU deployment options. Solution overview Figure 1 shows two deployment paths from the same packaged model. The text-generation path uses the AWS DLC for llama.cpp and returns generated responses through the OpenAI-compatible API. The structured-decision path builds a child image that replaces the default server with a SemIf adapter and returns probabilities for declared options. Figure 1: Run the AWS DLC for llama.cpp or the SemIf child image on CPU

## 笔记


