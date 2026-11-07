---
slug: taxonomy-of-agentic-primitives-in-amazon-quick
name: Taxonomy of agentic primitives in Amazon Quick
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
url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-agentic-primitives-in-amazon-quick/
canonical_url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-agentic-primitives-in-amazon-quick
summary: 'Over the past year, as we built Amazon Quick, our agents went from answering questions to taking
  actions: scheduling meetings, running research, generating reports. As the system evolved, one problem
  kept resurfacing: there was no shared definition of the primitives that agentic work is built from.
  The same few ideas kept getting rebuilt under different names: an actor that does the work, a signal
  that starts it, a packaged procedure, and a memory that carries lessons forward. This repetition leaked
  into product design and onto the user. Take the user who says “ monitor my Slack channel and send me
  a daily digest ”. Is that a new agent, a scheduled instruction to an existing one, a workflow, or a
  skill? These are different questions, but without a shared vocabulary they collapse into one confusing
  choice. This post shares the taxonomy we converged on: one set of primitives found by decomposing agentic
  work into four plain questions: When? , What? , Who? , and How? Most of the framework stays invisible
  to end users by design, but a shared vocabulary makes the system easier to reason about for anyone building
  beneath it. The framework at a glance Figure 1: How'
first_seen: '2026-11-07T01:57:08Z'
last_seen: '2026-11-07T01:57:08Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-agentic-primitives-in-amazon-quick/
  seen_at: '2026-11-07T01:57:08Z'
  metrics: {}
  kind: news
---

# Taxonomy of agentic primitives in Amazon Quick

Over the past year, as we built Amazon Quick, our agents went from answering questions to taking actions: scheduling meetings, running research, generating reports. As the system evolved, one problem kept resurfacing: there was no shared definition of the primitives that agentic work is built from. The same few ideas kept getting rebuilt under different names: an actor that does the work, a signal that starts it, a packaged procedure, and a memory that carries lessons forward. This repetition leaked into product design and onto the user. Take the user who says “ monitor my Slack channel and send me a daily digest ”. Is that a new agent, a scheduled instruction to an existing one, a workflow, or a skill? These are different questions, but without a shared vocabulary they collapse into one confusing choice. This post shares the taxonomy we converged on: one set of primitives found by decomposing agentic work into four plain questions: When? , What? , Who? , and How? Most of the framework stays invisible to end users by design, but a shared vocabulary makes the system easier to reason about for anyone building beneath it. The framework at a glance Figure 1: How

## 笔记


