---
slug: taxonomy-of-multi-agent-design-patterns-anti-patterns-and-le
name: Taxonomy of multi-agent design patterns, anti-patterns, and lessons from manufacturing
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
url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-multi-agent-design-patterns-anti-patterns-and-lessons-from-manufacturing/
canonical_url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-multi-agent-design-patterns-anti-patterns-and-lessons-from-manufacturing
summary: 'Enterprise teams are building multi-agent systems, and when early implementations fall short,
  the cause is rarely the model. Multi-agent coordination is a distributed systems problem, and many teams
  taking it on haven’t yet built distributed systems instincts. The numbers are consistent across sources:
  ~88% of AI pilots never reach production . Stanford HAI demonstrated that two models can perform worse
  collaborating than either alone when coordination overhead exceeds the benefit. The pattern is clear:
  teams are adding complexity faster than they build understanding. Ten steps that are each 95 percent
  reliable deliver only 59.9 percent end-to-end reliability, and 20 steps deliver 35.8 percent. This illustrative
  model assumes a strictly sequential chain with no retries, but the direction holds: each dependent handoff
  multiplies risk. In this post, you learn how to decide whether a use case needs multiple agents, choose
  a coordination pattern, and spot costly anti-patterns early. You also see how takt time, safety boundaries,
  edge data, and shift cycles shape the architecture. Multi-agent coordination patterns Coordination patterns
  fall into two tiers, based on who controls the flow. In Tier 1, you define the path. In Tier 2, the
  model chooses the path at runtime. That flexibility handles work whose'
first_seen: '2026-11-17T04:29:39Z'
last_seen: '2026-11-17T04:29:39Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-multi-agent-design-patterns-anti-patterns-and-lessons-from-manufacturing/
  seen_at: '2026-11-17T04:29:39Z'
  metrics: {}
  kind: news
---

# Taxonomy of multi-agent design patterns, anti-patterns, and lessons from manufacturing

Enterprise teams are building multi-agent systems, and when early implementations fall short, the cause is rarely the model. Multi-agent coordination is a distributed systems problem, and many teams taking it on haven’t yet built distributed systems instincts. The numbers are consistent across sources: ~88% of AI pilots never reach production . Stanford HAI demonstrated that two models can perform worse collaborating than either alone when coordination overhead exceeds the benefit. The pattern is clear: teams are adding complexity faster than they build understanding. Ten steps that are each 95 percent reliable deliver only 59.9 percent end-to-end reliability, and 20 steps deliver 35.8 percent. This illustrative model assumes a strictly sequential chain with no retries, but the direction holds: each dependent handoff multiplies risk. In this post, you learn how to decide whether a use case needs multiple agents, choose a coordination pattern, and spot costly anti-patterns early. You also see how takt time, safety boundaries, edge data, and shift cycles shape the architecture. Multi-agent coordination patterns Coordination patterns fall into two tiers, based on who controls the flow. In Tier 1, you define the path. In Tier 2, the model chooses the path at runtime. That flexibility handles work whose

## 笔记


