---
slug: tokenomics-at-scale-track-and-cap-amazon-bedrock-spend-per-i
name: 'Tokenomics at scale: Track and cap Amazon Bedrock spend per IAM principal with CUR 2.0 and AWS
  Budgets'
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
url: https://aws.amazon.com/blogs/machine-learning/tokenomics-at-scale-track-and-cap-amazon-bedrock-spend-per-iam-principal-with-cur-2-0-and-aws-budgets/
canonical_url: https://aws.amazon.com/blogs/machine-learning/tokenomics-at-scale-track-and-cap-amazon-bedrock-spend-per-iam-principal-with-cur-2-0-and-aws-budgets
summary: 'Generative AI spend is hard to attribute. Before an organization expands AI access, CFOs and
  CTOs usually want three answers: what do we spend per person or per team, can we cap it, and how much
  work does it take to get there. In our previous post, Tokenomics at Scale: How Jamf Built Real-Time
  Spend Enforcement for Amazon Bedrock , we explained a custom enforcement loop built on AWS IAM Identity
  Center , Amazon Athena over Amazon Bedrock model invocation logs , and AWS Lambda . This approach gives
  near-real-time control, but it requires code you then own and operate. This post shows how to get per-identity
  Amazon Bedrock cost visibility and enforceable spend limits using only AWS-native features, with no
  application code to write for the common case. The approach relies on three things: IAM principal attribution
  , which Amazon Bedrock records automatically; AWS Cost and Usage Reports (CUR) 2.0 or AWS Cost Explorer
  for reporting; and AWS Budgets with budget actions for enforcement. By the end, you will have per-identity
  cost reporting and an automatic guardrail that restricts Amazon Bedrock access when a threshold is crossed.
  Solution overview The solution has three parts: attribute, report, and enforce. Attribute.'
first_seen: '2026-11-13T02:39:04Z'
last_seen: '2026-11-13T02:39:04Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/tokenomics-at-scale-track-and-cap-amazon-bedrock-spend-per-iam-principal-with-cur-2-0-and-aws-budgets/
  seen_at: '2026-11-13T02:39:04Z'
  metrics: {}
  kind: news
---

# Tokenomics at scale: Track and cap Amazon Bedrock spend per IAM principal with CUR 2.0 and AWS Budgets

Generative AI spend is hard to attribute. Before an organization expands AI access, CFOs and CTOs usually want three answers: what do we spend per person or per team, can we cap it, and how much work does it take to get there. In our previous post, Tokenomics at Scale: How Jamf Built Real-Time Spend Enforcement for Amazon Bedrock , we explained a custom enforcement loop built on AWS IAM Identity Center , Amazon Athena over Amazon Bedrock model invocation logs , and AWS Lambda . This approach gives near-real-time control, but it requires code you then own and operate. This post shows how to get per-identity Amazon Bedrock cost visibility and enforceable spend limits using only AWS-native features, with no application code to write for the common case. The approach relies on three things: IAM principal attribution , which Amazon Bedrock records automatically; AWS Cost and Usage Reports (CUR) 2.0 or AWS Cost Explorer for reporting; and AWS Budgets with budget actions for enforcement. By the end, you will have per-identity cost reporting and an automatic guardrail that restricts Amazon Bedrock access when a threshold is crossed. Solution overview The solution has three parts: attribute, report, and enforce. Attribute.

## 笔记


