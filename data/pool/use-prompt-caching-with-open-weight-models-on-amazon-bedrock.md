---
slug: use-prompt-caching-with-open-weight-models-on-amazon-bedrock
name: Use prompt caching with open-weight models on Amazon Bedrock
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
url: https://aws.amazon.com/blogs/machine-learning/use-prompt-caching-with-open-weight-models-on-amazon-bedrock/
canonical_url: https://aws.amazon.com/blogs/machine-learning/use-prompt-caching-with-open-weight-models-on-amazon-bedrock
summary: Many generative AI applications send the same long context with every request, and prompt caching
  avoids processing it again each time. That context can be a system prompt, reference documents, tool
  definitions, or the conversation so far. Open-weight models on Amazon Bedrock can reuse it across requests,
  which helps reduce input costs and response latency. Prompt caching reuses the computed state of a matching
  prompt prefix, so repeated context is read from cache instead of being processed again. Amazon Bedrock
  manages the cache for you. Depending on the model, you can use implicit caching, which works automatically,
  explicit caching, where you mark the reusable prefix, or both. The more context you reuse, and the more
  often you reuse it, the more you can save. As with other models on Amazon Bedrock, your prompts and
  outputs aren’t shared with the model provider or used to train models. For more information, see Data
  protection in the Amazon Bedrock User Guide. Open-weight models on Amazon Bedrock now support explicit
  prompt caching. In this post, we use both modes with an open-weight model through the Chat Completions
  API and show how to read cache usage from each response. We then apply implicit caching to
first_seen: '2026-11-17T04:29:39Z'
last_seen: '2026-11-17T04:29:39Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/use-prompt-caching-with-open-weight-models-on-amazon-bedrock/
  seen_at: '2026-11-17T04:29:39Z'
  metrics: {}
  kind: news
---

# Use prompt caching with open-weight models on Amazon Bedrock

Many generative AI applications send the same long context with every request, and prompt caching avoids processing it again each time. That context can be a system prompt, reference documents, tool definitions, or the conversation so far. Open-weight models on Amazon Bedrock can reuse it across requests, which helps reduce input costs and response latency. Prompt caching reuses the computed state of a matching prompt prefix, so repeated context is read from cache instead of being processed again. Amazon Bedrock manages the cache for you. Depending on the model, you can use implicit caching, which works automatically, explicit caching, where you mark the reusable prefix, or both. The more context you reuse, and the more often you reuse it, the more you can save. As with other models on Amazon Bedrock, your prompts and outputs aren’t shared with the model provider or used to train models. For more information, see Data protection in the Amazon Bedrock User Guide. Open-weight models on Amazon Bedrock now support explicit prompt caching. In this post, we use both modes with an open-weight model through the Chat Completions API and show how to read cache usage from each response. We then apply implicit caching to

## 笔记


