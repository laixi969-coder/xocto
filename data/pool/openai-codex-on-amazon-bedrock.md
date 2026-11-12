---
slug: openai-codex-on-amazon-bedrock
name: OpenAI Codex on Amazon Bedrock
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
url: https://aws.amazon.com/blogs/machine-learning/openai-codex-on-amazon-bedrock/
canonical_url: https://aws.amazon.com/blogs/machine-learning/openai-codex-on-amazon-bedrock
summary: 'Developers increasingly use Codex with Amazon Bedrock to explore unfamiliar code, make changes,
  and handle repetitive engineering work. For platform teams, the challenge is to make those tools available
  without creating a second model-access, identity, and operations stack. Codex can use Amazon Bedrock
  for inference with supported OpenAI models. In this post, we show how to fit that path into the AWS
  identity, AWS Identity and Access Management (IAM), Regional, and observability practices your organization
  already uses. Codex still runs on the developer workstation. The main design choice is how its model
  requests reach Amazon Bedrock and where your organization applies policy and operational controls. We
  begin with a small, least-privilege pilot and work through the checks that matter before access expands.
  The examples use GPT-5.6 Sol. Before starting the pilot, review Supported models by AWS Region in Amazon
  Bedrock to confirm that Sol, Terra, or Luna is available in the AWS Region and inference path you plan
  to use. Recommended default: Start with Native AWS Access for a small, least-privilege pilot. Choose
  AgentCore Gateway, a capability of Amazon Bedrock AgentCore, when you want AWS managed gateway infrastructure
  for routing or Amazon Bedrock Guardrails. Choose an LLM Gateway when a'
first_seen: '2026-11-12T03:00:02Z'
last_seen: '2026-11-12T03:00:02Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/openai-codex-on-amazon-bedrock/
  seen_at: '2026-11-12T03:00:02Z'
  metrics: {}
  kind: news
---

# OpenAI Codex on Amazon Bedrock

Developers increasingly use Codex with Amazon Bedrock to explore unfamiliar code, make changes, and handle repetitive engineering work. For platform teams, the challenge is to make those tools available without creating a second model-access, identity, and operations stack. Codex can use Amazon Bedrock for inference with supported OpenAI models. In this post, we show how to fit that path into the AWS identity, AWS Identity and Access Management (IAM), Regional, and observability practices your organization already uses. Codex still runs on the developer workstation. The main design choice is how its model requests reach Amazon Bedrock and where your organization applies policy and operational controls. We begin with a small, least-privilege pilot and work through the checks that matter before access expands. The examples use GPT-5.6 Sol. Before starting the pilot, review Supported models by AWS Region in Amazon Bedrock to confirm that Sol, Terra, or Luna is available in the AWS Region and inference path you plan to use. Recommended default: Start with Native AWS Access for a small, least-privilege pilot. Choose AgentCore Gateway, a capability of Amazon Bedrock AgentCore, when you want AWS managed gateway infrastructure for routing or Amazon Bedrock Guardrails. Choose an LLM Gateway when a

## 笔记


