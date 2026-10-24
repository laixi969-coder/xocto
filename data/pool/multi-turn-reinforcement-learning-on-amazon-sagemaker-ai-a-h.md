---
slug: multi-turn-reinforcement-learning-on-amazon-sagemaker-ai-a-h
name: 'Multi-Turn Reinforcement Learning on Amazon SageMaker AI: A hands-on guide'
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
url: https://aws.amazon.com/blogs/machine-learning/multi-turn-reinforcement-learning-on-amazon-sagemaker-ai-a-hands-on-guide/
canonical_url: https://aws.amazon.com/blogs/machine-learning/multi-turn-reinforcement-learning-on-amazon-sagemaker-ai-a-hands-on-guide
summary: Most fine-tuning teaches a model to produce a better answer to a single prompt. Agentic tasks
  are different. An agent that files an expense report or triages a support ticket takes a sequence of
  actions, and each step depends on what came before. There’s rarely one correct sequence to imitate,
  and the only reliable feedback is whether the whole sequence succeeded. Supervised fine-tuning has no
  labels for that, and single-turn reinforcement learning cannot credit a decision made three steps before
  the outcome. Multi-Turn Reinforcement Learning (MTRL) on Amazon SageMaker AI trains models on exactly
  that signal. SageMaker AI sends prompts to an agent you host on Amazon Bedrock AgentCore, or on your
  own infrastructure, such as Amazon Elastic Kubernetes Service (Amazon EKS), Amazon Elastic Compute Cloud
  (Amazon EC2), or AWS Fargate, through an AWS Lambda forwarder . The example here uses AgentCore. The
  agent calls the policy model being trained, acts in your environment over as many turns as the task
  needs, and reports one reward when the episode ends. You don’t specify the right trajectory, only how
  to score the result. This post uses Wordle , a game in which a player has six tries to guess a hidden
first_seen: '2026-10-24T00:43:47Z'
last_seen: '2026-10-24T00:43:47Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/multi-turn-reinforcement-learning-on-amazon-sagemaker-ai-a-hands-on-guide/
  seen_at: '2026-10-24T00:43:47Z'
  metrics: {}
  kind: news
---

# Multi-Turn Reinforcement Learning on Amazon SageMaker AI: A hands-on guide

Most fine-tuning teaches a model to produce a better answer to a single prompt. Agentic tasks are different. An agent that files an expense report or triages a support ticket takes a sequence of actions, and each step depends on what came before. There’s rarely one correct sequence to imitate, and the only reliable feedback is whether the whole sequence succeeded. Supervised fine-tuning has no labels for that, and single-turn reinforcement learning cannot credit a decision made three steps before the outcome. Multi-Turn Reinforcement Learning (MTRL) on Amazon SageMaker AI trains models on exactly that signal. SageMaker AI sends prompts to an agent you host on Amazon Bedrock AgentCore, or on your own infrastructure, such as Amazon Elastic Kubernetes Service (Amazon EKS), Amazon Elastic Compute Cloud (Amazon EC2), or AWS Fargate, through an AWS Lambda forwarder . The example here uses AgentCore. The agent calls the policy model being trained, acts in your environment over as many turns as the task needs, and reports one reward when the episode ends. You don’t specify the right trajectory, only how to score the result. This post uses Wordle , a game in which a player has six tries to guess a hidden

## 笔记


