---
slug: so-you-want-to-use-openrouter
name: OpenRouter
builder: ''
category: ''
summary_zh: 2026年9月，有开发者指出 OpenRouter 的自动路由与回退机制会导致同一模型 ID 在不同后端提供商上行为不一致，包括部分提供商缺少视觉能力、推理强度参数处理方式不同；用户可通过
  provider.only 选项和 /endpoints 接口限定提供商。这意味着依赖统一 API 端点做模型调用的应用在输出稳定性、能力可用性和成本优化上需要额外做提供商级验证与锁定，多提供商聚合层的抽象泄漏成为
  AI 应用交付中的实际风险。
inspiration: ''
summary_en: In September 2026, developers pointed out that OpenRouter's automatic routing and fallback
  can make the same model ID behave inconsistently across backend providers, including some providers
  lacking vision capability for vision models and differing handling of the reasoning effort option; users
  can pin providers via the provider.only option and the /endpoints method. This means applications relying
  on a single API endpoint for model calls must add provider-level validation and locking to ensure output
  stability, capability availability and cost optimization, making abstraction leakage in multi-provider
  aggregation layers a practical risk in AI application delivery.
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
url: https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/
canonical_url: https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter
summary: "So you want to use OpenRouter?   \nOne of OpenRouter's selling points is that it \"handles fallbacks\
  \ automatically and picks the most cost-effective option for each request\", so you can call a single\
  \ API endpoint for a model and get routed to the best available backend provider. \n Mohamed Moustafa\
  \ points out a whole set of ways that this can cause you problems. Different providers run different\
  \ serving software with different optimizations and settings, which means that the same OpenRouter endpoint\
  \ can serve model requests that behave in different ways. \n Some providers even lack vision capability\
  \ for vision models, and the way the reasoning effort option is processed can differ as well. \n Thankfully\
  \ you can control which provider is routed to using  the provider.only option . The  /endpoints method\
  \  returns the list of available providers for a specific model ID.\n\n       Via  Hacker News   \n\n\
  \n     Tags:  ai ,  generative-ai ,  llms ,  openrouter"
first_seen: '2026-09-11T22:49:18Z'
last_seen: '2026-09-12T00:19:09Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/
  seen_at: '2026-09-12T00:19:09Z'
  metrics: {}
  kind: news
---

# OpenRouter

So you want to use OpenRouter?   
One of OpenRouter's selling points is that it "handles fallbacks automatically and picks the most cost-effective option for each request", so you can call a single API endpoint for a model and get routed to the best available backend provider. 
 Mohamed Moustafa points out a whole set of ways that this can cause you problems. Different providers run different serving software with different optimizations and settings, which means that the same OpenRouter endpoint can serve model requests that behave in different ways. 
 Some providers even lack vision capability for vision models, and the way the reasoning effort option is processed can differ as well. 
 Thankfully you can control which provider is routed to using  the provider.only option . The  /endpoints method  returns the list of available providers for a specific model ID.

       Via  Hacker News   


     Tags:  ai ,  generative-ai ,  llms ,  openrouter

## 笔记


