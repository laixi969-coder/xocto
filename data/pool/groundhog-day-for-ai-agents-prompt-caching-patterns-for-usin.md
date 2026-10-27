---
slug: groundhog-day-for-ai-agents-prompt-caching-patterns-for-usin
name: 'Groundhog Day for AI agents: Prompt caching patterns for using OpenAI models on Amazon Bedrock'
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
url: https://aws.amazon.com/blogs/machine-learning/groundhog-day-for-ai-agents-prompt-caching-patterns-for-using-openai-models-on-amazon-bedrock/
canonical_url: https://aws.amazon.com/blogs/machine-learning/groundhog-day-for-ai-agents-prompt-caching-patterns-for-using-openai-models-on-amazon-bedrock
summary: 'Every time you spin off your agent, it has to re-read its whole life story before performing
  an action. Here’s how to make it remember without having to feed it the same context again. In the movie
  Groundhog Day , Bill Murray’s character re-lives the same February 2 every day. He wakes up to the same
  song playing on the radio, in the same inn, and the same small town, again and again for what some movie
  fans estimate to be 34 years. Nothing he accomplished the day before carries over unless he works it
  out again from scratch. AI agents live in a version of Groundhog Day. Every time an agent takes a step
  (calls a tool, reads the result, decides what to do next), it has to send the model its entire story
  so far to maintain continuity: the tool definitions, the instructions, every previous tool call, and
  every result. The model only predicts the next token based on the input you provide. It has no internal
  memory between requests, so it must read all of it again. By turn 20 of a coding session, the model
  re-reads turns 1–19, and it’s you who pays for every one'
first_seen: '2026-10-27T01:30:17Z'
last_seen: '2026-10-27T01:30:17Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/groundhog-day-for-ai-agents-prompt-caching-patterns-for-using-openai-models-on-amazon-bedrock/
  seen_at: '2026-10-27T01:30:17Z'
  metrics: {}
  kind: news
---

# Groundhog Day for AI agents: Prompt caching patterns for using OpenAI models on Amazon Bedrock

Every time you spin off your agent, it has to re-read its whole life story before performing an action. Here’s how to make it remember without having to feed it the same context again. In the movie Groundhog Day , Bill Murray’s character re-lives the same February 2 every day. He wakes up to the same song playing on the radio, in the same inn, and the same small town, again and again for what some movie fans estimate to be 34 years. Nothing he accomplished the day before carries over unless he works it out again from scratch. AI agents live in a version of Groundhog Day. Every time an agent takes a step (calls a tool, reads the result, decides what to do next), it has to send the model its entire story so far to maintain continuity: the tool definitions, the instructions, every previous tool call, and every result. The model only predicts the next token based on the input you provide. It has no internal memory between requests, so it must read all of it again. By turn 20 of a coding session, the model re-reads turns 1–19, and it’s you who pays for every one

## 笔记


