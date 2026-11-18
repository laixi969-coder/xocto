---
slug: reducing-token-costs-and-latency-in-amazon-bedrock-agentcore
name: Reducing token costs and latency in Amazon Bedrock AgentCore JSON workloads
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
url: https://aws.amazon.com/blogs/machine-learning/reducing-token-costs-and-latency-in-amazon-bedrock-agentcore-json-workloads/
canonical_url: https://aws.amazon.com/blogs/machine-learning/reducing-token-costs-and-latency-in-amazon-bedrock-agentcore-json-workloads
summary: As enterprises build production agents with dozens of tools and large structured inputs, token
  consumption and latency become the primary blockers to a good user experience. When these agents process
  large JSON data, every additional tool invocation injects the full payload into the large language model
  (LLM) context window, causing token usage and response latency to spike. Over multi-turn conversations,
  this pressure compounds, driving up costs and degrading response quality. Effectively managing context-window
  pressure in agentic systems is key to reliability and responsiveness at scale. In this post, we share
  three composable strategies we used to build a production agent for Flightscape that handles 20 MB+
  JSON payloads. You can apply them to reduce token costs, lower latency, and maintain full reasoning
  capability across extended sessions. Together, these optimizations reduced token consumption by up to
  71% and cut average latency by up to 80% across our benchmark runs on a representative 23 MB payload.
  Solution overview Flightscape is an airline operations platform that helps airlines plan and manage
  their crews, flights, and operations. As part of Flightscape’s crew management capabilities, we built
  a Training Schedule Optimization agent that verifies crew training schedule assignments against business
  rules. With 40+ tools and
first_seen: '2026-11-18T03:43:37Z'
last_seen: '2026-11-18T03:43:37Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/reducing-token-costs-and-latency-in-amazon-bedrock-agentcore-json-workloads/
  seen_at: '2026-11-18T03:43:37Z'
  metrics: {}
  kind: news
---

# Reducing token costs and latency in Amazon Bedrock AgentCore JSON workloads

As enterprises build production agents with dozens of tools and large structured inputs, token consumption and latency become the primary blockers to a good user experience. When these agents process large JSON data, every additional tool invocation injects the full payload into the large language model (LLM) context window, causing token usage and response latency to spike. Over multi-turn conversations, this pressure compounds, driving up costs and degrading response quality. Effectively managing context-window pressure in agentic systems is key to reliability and responsiveness at scale. In this post, we share three composable strategies we used to build a production agent for Flightscape that handles 20 MB+ JSON payloads. You can apply them to reduce token costs, lower latency, and maintain full reasoning capability across extended sessions. Together, these optimizations reduced token consumption by up to 71% and cut average latency by up to 80% across our benchmark runs on a representative 23 MB payload. Solution overview Flightscape is an airline operations platform that helps airlines plan and manage their crews, flights, and operations. As part of Flightscape’s crew management capabilities, we built a Training Schedule Optimization agent that verifies crew training schedule assignments against business rules. With 40+ tools and

## 笔记


