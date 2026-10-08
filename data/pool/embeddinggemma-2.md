---
slug: embeddinggemma-2
name: EmbeddingGemma 2
builder: ilreb
category: ''
summary_zh: EmbeddingGemma 2 是一个以 Apache 2.0 许可发布的嵌入模型，公开讨论集中在许可与托管方式：嵌入向量通常要预先计算成千上万条并长期存储，若模型只由厂商托管，一旦停服就需要重新计算全部存量向量。因此有开发者表示愿意付费使用托管版本，同时要求保留自行运行开放权重或更换供应商的退路。
inspiration: ''
summary_en: 'EmbeddingGemma 2 is an embedding model released under the Apache 2.0 license. Public discussion
  centers on licensing and hosting: embedding vectors are typically precomputed in the thousands or millions
  and stored long term, so if a vendor hosts the model exclusively and later retires it, all stored vectors
  must be recomputed. Some developers say they would pay for a hosted version while keeping the option
  to run the open weights themselves or switch vendors.'
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
url: https://simonwillison.net/2026/Oct/6/hn-49983751/
canonical_url: https://simonwillison.net/2026/Oct/6/hn-49983751
summary: "My comment  on  EmbeddingGemma 2  — Hacker News.  I really appreciate that  EmbeddingGemma 2\
  \  is under the Apache 2.0 license. \n For embedding models in particular, I don't think it makes sense\
  \ to use a closed, proprietary, hosted-only model. \n Most applications of embedding models involve\
  \ calculating thousands or even millions of embedding vectors and storing them for later comparison.\
  \ \n If your model is proprietary, the vendor is likely someday going to decide to stop offering that\
  \ model. They'll have a better model to replace it, but you still need to pay to re-calculate those\
  \ millions of stored existing vectors. \n (In April 2024 OpenAI offered to \"cover the financial cost\
  \ of users re-embedding content with these new models\" -  https://openai.com/index/gpt-4-api-general-availability/\
  \  - but I don't think that's something we can rely on from every provider.) \n Notably, I  don't want\
  \ to host the model myself . I'd much rather pay a provider for a hosted model while knowing that if\
  \ they ever stop hosting it I can run the open weights version myself - or find another vendor who can\
  \ do that for me. \n    \n    \n         Tags:  google ,  ai ,  generative-ai ,  embeddings ,  gemma"
first_seen: '2026-10-06T20:37:53Z'
last_seen: '2026-10-08T01:55:51Z'
status: pending_filter
sources:
- marketfeeds
- hackernews
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/6/hn-49983751/
  seen_at: '2026-10-07T01:32:55Z'
  metrics: {}
  kind: news
- source: hackernews
  url: https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/
  seen_at: '2026-10-08T01:55:51Z'
  metrics:
    points: 416
    comments: 46
  kind: news
---

# EmbeddingGemma 2

My comment  on  EmbeddingGemma 2  — Hacker News.  I really appreciate that  EmbeddingGemma 2  is under the Apache 2.0 license. 
 For embedding models in particular, I don't think it makes sense to use a closed, proprietary, hosted-only model. 
 Most applications of embedding models involve calculating thousands or even millions of embedding vectors and storing them for later comparison. 
 If your model is proprietary, the vendor is likely someday going to decide to stop offering that model. They'll have a better model to replace it, but you still need to pay to re-calculate those millions of stored existing vectors. 
 (In April 2024 OpenAI offered to "cover the financial cost of users re-embedding content with these new models" -  https://openai.com/index/gpt-4-api-general-availability/  - but I don't think that's something we can rely on from every provider.) 
 Notably, I  don't want to host the model myself . I'd much rather pay a provider for a hosted model while knowing that if they ever stop hosting it I can run the open weights version myself - or find another vendor who can do that for me. 
    
    
         Tags:  google ,  ai ,  generative-ai ,  embeddings ,  gemma

## 笔记


