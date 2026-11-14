---
slug: route-coding-agent-requests-to-the-right-model-on-amazon-bed
name: Route coding agent requests to the right model on Amazon Bedrock with NVIDIA NeMo Switchyard
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
url: https://aws.amazon.com/blogs/machine-learning/route-coding-agent-requests-to-the-right-model-on-amazon-bedrock-with-nvidia-nemo-switchyard/
canonical_url: https://aws.amazon.com/blogs/machine-learning/route-coding-agent-requests-to-the-right-model-on-amazon-bedrock-with-nvidia-nemo-switchyard
summary: 'Coding agents such as Claude Code and OpenAI Codex CLI work in tasks. A developer asks for a
  change, and the agent reads files, edits code, and runs tests until the work is done. One task can take
  a few model calls or dozens. What the developer pays for is the task, not one call. The price per token
  alone doesn’t tell you what a whole task costs. The total depends on how many turns a model needs, how
  much history each turn replays, and how often a task has to be retried or never finishes. You pay for
  every attempt, including attempts on tasks that never finish. So when you route a coding agent’s requests
  between models, judge the routing by cost per solved task: the total cost of your runs divided by the
  number of runs whose tests pass. NVIDIA NeMo Switchyard is an open source library that helps an AI agent
  choose which model handles each request. You define the models that it can use and the strategy that
  it follows. Its LiteLLM integration supports two strategies. Stage routing reads the recent tool activity
  and results in the request history, and then picks one of two candidate'
first_seen: '2026-11-14T02:28:05Z'
last_seen: '2026-11-14T02:28:05Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/route-coding-agent-requests-to-the-right-model-on-amazon-bedrock-with-nvidia-nemo-switchyard/
  seen_at: '2026-11-14T02:28:05Z'
  metrics: {}
  kind: news
---

# Route coding agent requests to the right model on Amazon Bedrock with NVIDIA NeMo Switchyard

Coding agents such as Claude Code and OpenAI Codex CLI work in tasks. A developer asks for a change, and the agent reads files, edits code, and runs tests until the work is done. One task can take a few model calls or dozens. What the developer pays for is the task, not one call. The price per token alone doesn’t tell you what a whole task costs. The total depends on how many turns a model needs, how much history each turn replays, and how often a task has to be retried or never finishes. You pay for every attempt, including attempts on tasks that never finish. So when you route a coding agent’s requests between models, judge the routing by cost per solved task: the total cost of your runs divided by the number of runs whose tests pass. NVIDIA NeMo Switchyard is an open source library that helps an AI agent choose which model handles each request. You define the models that it can use and the strategy that it follows. Its LiteLLM integration supports two strategies. Stage routing reads the recent tool activity and results in the request history, and then picks one of two candidate

## 笔记


