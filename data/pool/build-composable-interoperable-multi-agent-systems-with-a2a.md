---
slug: build-composable-interoperable-multi-agent-systems-with-a2a
name: Build composable, interoperable multi-agent systems with A2A on AWS
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
url: https://aws.amazon.com/blogs/machine-learning/build-composable-interoperable-multi-agent-systems-with-a2a-on-aws/
canonical_url: https://aws.amazon.com/blogs/machine-learning/build-composable-interoperable-multi-agent-systems-with-a2a-on-aws
summary: Agents in multi-agent systems that span organizational boundaries often need to collaborate in
  a composable, interoperable way, with agents that other organizations build and run. They need a way
  to discover each other, communicate, and exchange tasks without exposing internals or requiring the
  same framework on both sides. The Agent-to-Agent (A2A) protocol addresses this constraint. Without A2A,
  building composable multi-agent systems across organizational boundaries requires custom integration
  code for each customer and framework. Independent software vendors (ISVs) can instead build composable,
  interoperable agents that work with the A2A-compatible frameworks their customers already use. While
  we frame this post around the ISV use case, the pattern also applies to organizations that expose agents
  across boundaries, whether to partners, customers, or internal teams that use different frameworks.
  As your system grows, you add skills by registering Agent Cards with the orchestrator, without changing
  the agents already running. In this post, we walk through a deployed reference architecture on AWS.
  A LangChain-based enterprise orchestrator communicates with a Strands Agents-based software as a service
  (SaaS) agent across organizational boundaries using A2A, with the enterprise and the SaaS provider in
  separate AWS accounts. Neither side depends on the other’s framework or SDK, and the two
first_seen: '2026-11-13T02:39:04Z'
last_seen: '2026-11-13T02:39:04Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/build-composable-interoperable-multi-agent-systems-with-a2a-on-aws/
  seen_at: '2026-11-13T02:39:04Z'
  metrics: {}
  kind: news
---

# Build composable, interoperable multi-agent systems with A2A on AWS

Agents in multi-agent systems that span organizational boundaries often need to collaborate in a composable, interoperable way, with agents that other organizations build and run. They need a way to discover each other, communicate, and exchange tasks without exposing internals or requiring the same framework on both sides. The Agent-to-Agent (A2A) protocol addresses this constraint. Without A2A, building composable multi-agent systems across organizational boundaries requires custom integration code for each customer and framework. Independent software vendors (ISVs) can instead build composable, interoperable agents that work with the A2A-compatible frameworks their customers already use. While we frame this post around the ISV use case, the pattern also applies to organizations that expose agents across boundaries, whether to partners, customers, or internal teams that use different frameworks. As your system grows, you add skills by registering Agent Cards with the orchestrator, without changing the agents already running. In this post, we walk through a deployed reference architecture on AWS. A LangChain-based enterprise orchestrator communicates with a Strands Agents-based software as a service (SaaS) agent across organizational boundaries using A2A, with the enterprise and the SaaS provider in separate AWS accounts. Neither side depends on the other’s framework or SDK, and the two

## 笔记


