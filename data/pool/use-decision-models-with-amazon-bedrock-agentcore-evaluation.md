---
slug: use-decision-models-with-amazon-bedrock-agentcore-evaluation
name: Use decision models with Amazon Bedrock AgentCore Evaluations
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
url: https://aws.amazon.com/blogs/machine-learning/use-decision-models-with-amazon-bedrock-agentcore-evaluations/
canonical_url: https://aws.amazon.com/blogs/machine-learning/use-decision-models-with-amazon-bedrock-agentcore-evaluations
summary: Some of the questions you ask when evaluating an agent are narrow and repeatable. Did this response
  stay on policy? Is this tool call safe to approve? Does this answer match the retrieved context? Decision
  models answer exactly that kind of question. They take a structured state and a fixed set of allowed
  answers and return a calibrated probability over them, rather than free-form text whose confidence drifts
  from run to run. That makes them a strong fit for the scoring step in an agent evaluation, where you
  want a label and a number you can threshold and trust. Amazon Bedrock AgentCore Evaluations , a capability
  of Amazon Bedrock AgentCore, scores an agent through its entire lifecycle, on demand during development,
  in batch jobs against stored sessions, and online against production traffic. Alongside 15 built-in
  evaluators, AgentCore Evaluations supports custom evaluators that you define as either an LLM-as-a-judge
  or a code-based evaluator. Custom LLM-as-a-judge evaluators apply your instructions and rating scale
  with a model in Amazon Bedrock. Code-based evaluators run your own logic in an AWS Lambda function,
  and that logic can call your choice of external system, model, or API, including a decision model. Decision
  models suit questions with
first_seen: '2026-11-05T02:30:05Z'
last_seen: '2026-11-05T02:30:05Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/use-decision-models-with-amazon-bedrock-agentcore-evaluations/
  seen_at: '2026-11-05T02:30:05Z'
  metrics: {}
  kind: news
---

# Use decision models with Amazon Bedrock AgentCore Evaluations

Some of the questions you ask when evaluating an agent are narrow and repeatable. Did this response stay on policy? Is this tool call safe to approve? Does this answer match the retrieved context? Decision models answer exactly that kind of question. They take a structured state and a fixed set of allowed answers and return a calibrated probability over them, rather than free-form text whose confidence drifts from run to run. That makes them a strong fit for the scoring step in an agent evaluation, where you want a label and a number you can threshold and trust. Amazon Bedrock AgentCore Evaluations , a capability of Amazon Bedrock AgentCore, scores an agent through its entire lifecycle, on demand during development, in batch jobs against stored sessions, and online against production traffic. Alongside 15 built-in evaluators, AgentCore Evaluations supports custom evaluators that you define as either an LLM-as-a-judge or a code-based evaluator. Custom LLM-as-a-judge evaluators apply your instructions and rating scale with a model in Amazon Bedrock. Code-based evaluators run your own logic in an AWS Lambda function, and that logic can call your choice of external system, model, or API, including a decision model. Decision models suit questions with

## 笔记


