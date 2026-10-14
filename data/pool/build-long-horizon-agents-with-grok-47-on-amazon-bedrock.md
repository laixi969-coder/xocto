---
slug: build-long-horizon-agents-with-grok-47-on-amazon-bedrock
name: Build long-horizon agents with Grok 4.7 on Amazon Bedrock
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
url: https://aws.amazon.com/blogs/machine-learning/build-long-horizon-agents-with-grok-4-7-on-amazon-bedrock/
canonical_url: https://aws.amazon.com/blogs/machine-learning/build-long-horizon-agents-with-grok-4-7-on-amazon-bedrock
summary: SpaceXAI’s Grok 4.7 is now available on Amazon Bedrock, which offers a choice of foundation models
  (FMs) from multiple providers. According to SpaceXAI, Grok 4.7 is trained to work longer on more difficult
  tasks and knows when to check its own work. That matters most for agents, which carry a task through
  many steps and must verify what they find along the way. An agent that works this way has to do more
  than look things up. It has to form a candidate answer, check it against what it has learned, and refine
  it until it fits. Grok 4.7 exposes a reasoning effort setting that controls how much deliberation happens
  before each response, and for agent workloads a practical question is which level to run. In this post,
  we build a tool-calling agent on Grok 4.7 and evaluate it on three tasks that require search rather
  than lookup. The tasks are diagnosing a two-service outage from its alerts, scheduling maintenance under
  interacting constraints, and choosing an optimal set of migrations under a budget. Each task has exactly
  one correct answer, verified by brute force. We ran all three at every reasoning effort level, six times
  each, for 72 agent runs.
first_seen: '2026-10-14T01:14:22Z'
last_seen: '2026-10-14T01:14:22Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/build-long-horizon-agents-with-grok-4-7-on-amazon-bedrock/
  seen_at: '2026-10-14T01:14:22Z'
  metrics: {}
  kind: news
---

# Build long-horizon agents with Grok 4.7 on Amazon Bedrock

SpaceXAI’s Grok 4.7 is now available on Amazon Bedrock, which offers a choice of foundation models (FMs) from multiple providers. According to SpaceXAI, Grok 4.7 is trained to work longer on more difficult tasks and knows when to check its own work. That matters most for agents, which carry a task through many steps and must verify what they find along the way. An agent that works this way has to do more than look things up. It has to form a candidate answer, check it against what it has learned, and refine it until it fits. Grok 4.7 exposes a reasoning effort setting that controls how much deliberation happens before each response, and for agent workloads a practical question is which level to run. In this post, we build a tool-calling agent on Grok 4.7 and evaluate it on three tasks that require search rather than lookup. The tasks are diagnosing a two-service outage from its alerts, scheduling maintenance under interacting constraints, and choosing an optimal set of migrations under a budget. Each task has exactly one correct answer, verified by brute force. We ran all three at every reasoning effort level, six times each, for 72 agent runs.

## 笔记


