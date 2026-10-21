---
slug: access-openai-gpt-models-on-amazon-bedrock-from-canada-with
name: Access OpenAI GPT models on Amazon Bedrock from Canada with cross-Region inference
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
url: https://aws.amazon.com/blogs/machine-learning/access-openai-gpt-models-on-amazon-bedrock-from-canada-with-cross-region-inference/
canonical_url: https://aws.amazon.com/blogs/machine-learning/access-openai-gpt-models-on-amazon-bedrock-from-canada-with-cross-region-inference
summary: Canadian organizations building generative AI applications on Amazon Bedrock often need the latest
  foundation models (FMs), such as OpenAI GPT-6.1, OpenAI GPT-6, and GPT-5.6, accessible from the Canadian
  AWS Regions. With Amazon Bedrock cross-Region inference (CRIS), you can now access these models from
  Canada. OpenAI GPT-5.6 models (Sol, Terra, and Luna), GPT-6 (Astra, Sol, and Luna), and GPT-6.1 Sol
  are available from the Canada (Central) and Canada West (Calgary) Regions. Inference is processed in
  North America, with data-residency controls described later in this post. Cross-Region inference is
  a capacity mechanism. Your application calls the Amazon Bedrock Runtime endpoint in your source Region.
  Amazon Bedrock then routes the request to a supported destination Region for processing. With this approach,
  you get access to a broader capacity pool that can help your application sustain throughput during demand
  spikes. You don’t need to manage destination Region routing in your application. In this post, we walk
  through the GPT-5.6, GPT-6, and GPT-6.1 models available from Canada and the cross-Region inference
  profiles that serve them. We then show how to set up permissions and invoke the models with the OpenAI
  Responses API, Chat Completions API, and the Amazon Bedrock Converse API. For the Responses API,
first_seen: '2026-10-21T00:38:23Z'
last_seen: '2026-10-21T00:38:23Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/access-openai-gpt-models-on-amazon-bedrock-from-canada-with-cross-region-inference/
  seen_at: '2026-10-21T00:38:23Z'
  metrics: {}
  kind: news
---

# Access OpenAI GPT models on Amazon Bedrock from Canada with cross-Region inference

Canadian organizations building generative AI applications on Amazon Bedrock often need the latest foundation models (FMs), such as OpenAI GPT-6.1, OpenAI GPT-6, and GPT-5.6, accessible from the Canadian AWS Regions. With Amazon Bedrock cross-Region inference (CRIS), you can now access these models from Canada. OpenAI GPT-5.6 models (Sol, Terra, and Luna), GPT-6 (Astra, Sol, and Luna), and GPT-6.1 Sol are available from the Canada (Central) and Canada West (Calgary) Regions. Inference is processed in North America, with data-residency controls described later in this post. Cross-Region inference is a capacity mechanism. Your application calls the Amazon Bedrock Runtime endpoint in your source Region. Amazon Bedrock then routes the request to a supported destination Region for processing. With this approach, you get access to a broader capacity pool that can help your application sustain throughput during demand spikes. You don’t need to manage destination Region routing in your application. In this post, we walk through the GPT-5.6, GPT-6, and GPT-6.1 models available from Canada and the cross-Region inference profiles that serve them. We then show how to set up permissions and invoke the models with the OpenAI Responses API, Chat Completions API, and the Amazon Bedrock Converse API. For the Responses API,

## 笔记


