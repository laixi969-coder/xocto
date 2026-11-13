---
slug: four-amazon-bedrock-inference-choices-that-affect-cost
name: Four Amazon Bedrock inference choices that affect cost
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
url: https://aws.amazon.com/blogs/machine-learning/four-amazon-bedrock-inference-choices-that-affect-cost/
canonical_url: https://aws.amazon.com/blogs/machine-learning/four-amazon-bedrock-inference-choices-that-affect-cost
summary: Your Amazon Bedrock inference bill can keep climbing after you tune prompts and application logic.
  Request-level choices can still change how many tokens the service processes and the rate applied to
  them. Cache duration, service tier, reasoning effort, and maxTokens can affect cost without changing
  your model or prompt. Each choice depends on the model and workload. This post shows how we tested each
  choice and how to verify its effect from response metadata, logs, and billing data. To try these settings
  yourself, start with the Amazon Bedrock Samples notebooks Mixed TTL Caching and Tenant Isolation with
  Prompt Caching . For maxTokens and reasoning effort, see the 01-low-effort folder of the sample-code-for-genai-cost-management-workshop
  GitHub repo. Each sample sets its own model ID, so change it, and the inference parameters, to match
  the model you call. For model availability by AWS Region, refer to Models at a glance . For broader
  decisions such as model selection, batch inference, routing, and distillation, see Effective cost optimization
  strategies for Amazon Bedrock . Where inference cost comes from Every Amazon Bedrock response carries
  usage metadata. Input and output tokens bill at the rate for the model and tier that served the request.
  Cache reads and
first_seen: '2026-11-13T02:39:04Z'
last_seen: '2026-11-13T02:39:04Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/four-amazon-bedrock-inference-choices-that-affect-cost/
  seen_at: '2026-11-13T02:39:04Z'
  metrics: {}
  kind: news
---

# Four Amazon Bedrock inference choices that affect cost

Your Amazon Bedrock inference bill can keep climbing after you tune prompts and application logic. Request-level choices can still change how many tokens the service processes and the rate applied to them. Cache duration, service tier, reasoning effort, and maxTokens can affect cost without changing your model or prompt. Each choice depends on the model and workload. This post shows how we tested each choice and how to verify its effect from response metadata, logs, and billing data. To try these settings yourself, start with the Amazon Bedrock Samples notebooks Mixed TTL Caching and Tenant Isolation with Prompt Caching . For maxTokens and reasoning effort, see the 01-low-effort folder of the sample-code-for-genai-cost-management-workshop GitHub repo. Each sample sets its own model ID, so change it, and the inference parameters, to match the model you call. For model availability by AWS Region, refer to Models at a glance . For broader decisions such as model selection, batch inference, routing, and distillation, see Effective cost optimization strategies for Amazon Bedrock . Where inference cost comes from Every Amazon Bedrock response carries usage metadata. Input and output tokens bill at the rate for the model and tier that served the request. Cache reads and

## 笔记


