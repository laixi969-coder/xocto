---
slug: automate-remediation-post-aws-devops-agent-investigation
name: AWS DevOps Agent
builder: ''
category: ''
summary_zh: 这是 AWS 官方博客给出的平台能力说明：DevOps Agent 负责诊断生产事故但保持只读，修复动作由用户自己用 Lambda、EventBridge 和 Bedrock 拼出，最终由值班工程师一键确认。它描述的是云厂商把事故诊断与修复审批串起来的一种做法，不是独立产品。
inspiration: ''
summary_en: 'This is an AWS official blog describing platform capability: the DevOps Agent diagnoses production
  incidents but stays read-only, while the fix path is assembled by the customer using Lambda, EventBridge
  and Bedrock, with an on-call engineer confirming in one action. It describes a cloud vendor''s way of
  linking incident diagnosis to remediation approval, not a standalone product.'
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
url: https://aws.amazon.com/blogs/machine-learning/automate-remediation-post-aws-devops-agent-investigation/
canonical_url: https://aws.amazon.com/blogs/machine-learning/automate-remediation-post-aws-devops-agent-investigation
summary: AWS DevOps Agent can diagnose production incidents but is kept in observe-and-report mode so
  it does not change resources directly. This post shows how to use AWS Lambda Durable Functions, Amazon
  EventBridge, and Amazon Bedrock to turn its investigation summaries into pre-validated fixes an on-call
  engineer can approve with a single action.
first_seen: '2026-10-07T15:46:49Z'
last_seen: '2026-10-08T01:56:15Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/automate-remediation-post-aws-devops-agent-investigation/
  seen_at: '2026-10-08T01:56:15Z'
  metrics: {}
  kind: news
---

# AWS DevOps Agent

AWS DevOps Agent can diagnose production incidents but is kept in observe-and-report mode so it does not change resources directly. This post shows how to use AWS Lambda Durable Functions, Amazon EventBridge, and Amazon Bedrock to turn its investigation summaries into pre-validated fixes an on-call engineer can approve with a single action.

## 笔记


