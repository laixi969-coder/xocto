---
slug: how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-am
name: How Airbnb uses cost per task to operate coding agents on Amazon Bedrock
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
url: https://aws.amazon.com/blogs/machine-learning/how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-amazon-bedrock/
canonical_url: https://aws.amazon.com/blogs/machine-learning/how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-amazon-bedrock
summary: Amazon Bedrock provides access to foundation models from multiple providers through a common
  API, with AWS managing the model infrastructure. It integrates with AWS access controls and monitoring,
  and processes prompts, code, and model responses within AWS. As coding agents move into production,
  changes in models and usage can affect latency, capacity, and cost. Amazon Bedrock runtime metrics in
  Amazon CloudWatch help teams investigate latency increases, throttling, and changes in token consumption.
  Evaluations, or evals, complement these operational metrics by assessing the quality of an agent’s work
  on a fixed set of representative tasks. In this post, we show how Airbnb evaluates models for coding
  agents and monitors their use on Amazon Bedrock. We explain how cost per task guides model selection
  and how production data helps us revisit those choices as usage changes. We also describe the runtime
  signals used to investigate latency, throttling, and spend. At Airbnb, thousands of engineers and engineering-adjacent
  people use AirChat, our internal tool for running coding agents, every week. The agents send their model
  requests through our large language model (LLM) gateway, which runs on Amazon Bedrock. Bedrock processes
  Airbnb’s code, prompts, and model responses within AWS. Eight new models came out in
first_seen: '2026-11-19T03:28:37Z'
last_seen: '2026-11-19T03:28:37Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-amazon-bedrock/
  seen_at: '2026-11-19T03:28:37Z'
  metrics: {}
  kind: news
---

# How Airbnb uses cost per task to operate coding agents on Amazon Bedrock

Amazon Bedrock provides access to foundation models from multiple providers through a common API, with AWS managing the model infrastructure. It integrates with AWS access controls and monitoring, and processes prompts, code, and model responses within AWS. As coding agents move into production, changes in models and usage can affect latency, capacity, and cost. Amazon Bedrock runtime metrics in Amazon CloudWatch help teams investigate latency increases, throttling, and changes in token consumption. Evaluations, or evals, complement these operational metrics by assessing the quality of an agent’s work on a fixed set of representative tasks. In this post, we show how Airbnb evaluates models for coding agents and monitors their use on Amazon Bedrock. We explain how cost per task guides model selection and how production data helps us revisit those choices as usage changes. We also describe the runtime signals used to investigate latency, throttling, and spend. At Airbnb, thousands of engineers and engineering-adjacent people use AirChat, our internal tool for running coding agents, every week. The agents send their model requests through our large language model (LLM) gateway, which runs on Amazon Bedrock. Bedrock processes Airbnb’s code, prompts, and model responses within AWS. Eight new models came out in

## 笔记


