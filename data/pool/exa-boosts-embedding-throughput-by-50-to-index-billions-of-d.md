---
slug: exa-boosts-embedding-throughput-by-50-to-index-billions-of-d
name: Exa boosts embedding throughput by 50% to index billions of documents on AWS AI chips
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
url: https://aws.amazon.com/blogs/machine-learning/exa-boosts-embedding-throughput-by-50-to-index-billions-of-documents-on-aws-ai-chips/
canonical_url: https://aws.amazon.com/blogs/machine-learning/exa-boosts-embedding-throughput-by-50-to-index-billions-of-documents-on-aws-ai-chips
summary: At Exa , we are building one of the few true web indexes by aggregating and serving knowledge
  from across the web, along with private and synthetic sources. We optimize the index for semantic search,
  grounding agents and humans in true, high-quality data. We use multi-tower semantic machine learning
  (ML) models to embed web data and query data into the same vector space, so users can express complex
  queries in natural language alongside traditional keyword search. The keystone technology behind this
  is an in-house vector database. It must ingest as much high-quality web data as possible and embed all
  of it. The unit economics of embedding therefore underlie everything we do. At the scale of tens or
  hundreds of billions of documents, finding the hardware that delivers the best performance per dollar
  isn’t a tuning detail. Any per-document cost improvement compounds into a significant number. This post
  details how we optimized our embedding infrastructure for cheaper, more flexible inference workloads
  on AWS Neuron hardware ( AWS Inferentia2 and AWS Trainium2 ), and how an agentic development workflow
  drove the optimization. Inference runs on an asynchronous pipeline, but it must be high-volume and fast
  to serve recent data quickly and shrink
first_seen: '2026-11-19T03:28:37Z'
last_seen: '2026-11-19T03:28:37Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/exa-boosts-embedding-throughput-by-50-to-index-billions-of-documents-on-aws-ai-chips/
  seen_at: '2026-11-19T03:28:37Z'
  metrics: {}
  kind: news
---

# Exa boosts embedding throughput by 50% to index billions of documents on AWS AI chips

At Exa , we are building one of the few true web indexes by aggregating and serving knowledge from across the web, along with private and synthetic sources. We optimize the index for semantic search, grounding agents and humans in true, high-quality data. We use multi-tower semantic machine learning (ML) models to embed web data and query data into the same vector space, so users can express complex queries in natural language alongside traditional keyword search. The keystone technology behind this is an in-house vector database. It must ingest as much high-quality web data as possible and embed all of it. The unit economics of embedding therefore underlie everything we do. At the scale of tens or hundreds of billions of documents, finding the hardware that delivers the best performance per dollar isn’t a tuning detail. Any per-document cost improvement compounds into a significant number. This post details how we optimized our embedding infrastructure for cheaper, more flexible inference workloads on AWS Neuron hardware ( AWS Inferentia2 and AWS Trainium2 ), and how an agentic development workflow drove the optimization. Inference runs on an asynchronous pipeline, but it must be high-volume and fast to serve recent data quickly and shrink

## 笔记


