---
slug: structured-outputs-for-anthropic-claude-models-on-amazon-bed
name: Amazon Bedrock
builder: ''
category: ''
summary_zh: Amazon Bedrock 是 AWS 的模型托管平台；本次变化是它对 Claude 模型开放结构化输出，让调用方按预先定义的 JSON Schema 拿到合规响应，替代过去在模型输出之后自行解析和重试的环节。
inspiration: ''
summary_en: Amazon Bedrock is AWS's managed model platform; this change exposes structured outputs for
  Claude models so callers receive schema-compliant JSON, replacing the previous step of parsing and retrying
  model output after generation.
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
url: https://aws.amazon.com/blogs/machine-learning/structured-outputs-for-anthropic-claude-models-on-amazon-bedrock/
canonical_url: https://aws.amazon.com/blogs/machine-learning/structured-outputs-for-anthropic-claude-models-on-amazon-bedrock
summary: 'Amazon Bedrock now supports structured outputs for all Anthropic Claude models, on both the
  bedrock-runtime and bedrock-mantle endpoints, where the model is available. Whether you call Claude
  through Boto3 and the bedrock-runtime APIs or through the Messages API and the bedrock-mantle endpoint,
  you can now receive schema-compliant JSON responses that conform to a defined structure. You no longer
  need custom parsing, retry logic, or post-processing. Practical applications With structured outputs
  for Claude on Amazon Bedrock, you can automate reliable, schema-compliant tasks across industries. Examples
  include extracting every required field from financial earnings reports and compliance documents, parsing
  clinical notes into Electronic Health Records (EHR), and enriching product catalogs with consistent,
  validated results. You can also analyze contracts for key terms, parties, and obligations, or power
  intelligent support ticket routing where intents, sentiments, and entities always match your application’s
  data model. What changes with structured outputs on Amazon Bedrock Structured outputs use constrained
  decoding to enforce your JSON schema during token generation, not after the fact. The model doesn’t
  produce tokens that would violate your schema. This changes output formatting from probabilistic to
  deterministic. Two complementary mechanisms are now available on both Amazon Bedrock endpoints: Feature
  Purpose Use case JSON Schema'
first_seen: '2026-10-20T01:06:54Z'
last_seen: '2026-10-20T01:06:54Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/structured-outputs-for-anthropic-claude-models-on-amazon-bedrock/
  seen_at: '2026-10-20T01:06:54Z'
  metrics: {}
  kind: news
---

# Amazon Bedrock

Amazon Bedrock now supports structured outputs for all Anthropic Claude models, on both the bedrock-runtime and bedrock-mantle endpoints, where the model is available. Whether you call Claude through Boto3 and the bedrock-runtime APIs or through the Messages API and the bedrock-mantle endpoint, you can now receive schema-compliant JSON responses that conform to a defined structure. You no longer need custom parsing, retry logic, or post-processing. Practical applications With structured outputs for Claude on Amazon Bedrock, you can automate reliable, schema-compliant tasks across industries. Examples include extracting every required field from financial earnings reports and compliance documents, parsing clinical notes into Electronic Health Records (EHR), and enriching product catalogs with consistent, validated results. You can also analyze contracts for key terms, parties, and obligations, or power intelligent support ticket routing where intents, sentiments, and entities always match your application’s data model. What changes with structured outputs on Amazon Bedrock Structured outputs use constrained decoding to enforce your JSON schema during token generation, not after the fact. The model doesn’t produce tokens that would violate your schema. This changes output formatting from probabilistic to deterministic. Two complementary mechanisms are now available on both Amazon Bedrock endpoints: Feature Purpose Use case JSON Schema

## 笔记


