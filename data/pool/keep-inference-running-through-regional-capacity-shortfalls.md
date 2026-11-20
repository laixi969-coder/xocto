---
slug: keep-inference-running-through-regional-capacity-shortfalls
name: Keep inference running through regional capacity shortfalls with cross-Region inference routing
  in Amazon SageMaker AI
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
url: https://aws.amazon.com/blogs/machine-learning/keep-inference-running-through-regional-capacity-shortfalls-with-cross-region-inference-routing-in-amazon-sagemaker-ai/
canonical_url: https://aws.amazon.com/blogs/machine-learning/keep-inference-running-through-regional-capacity-shortfalls-with-cross-region-inference-routing-in-amazon-sagemaker-ai
summary: 'Serving a model from more than one AWS Region is a well-established pattern for highly available
  inference: when one Region runs short of GPU capacity, requests move to another. The pattern is simple
  to describe and hard to operate. Until now, if you served models on Amazon SageMaker AI managed endpoints,
  cross-Region routing was a piece you still had to build yourself. Today, we’re introducing cross-Region
  inference routing in Amazon SageMaker AI. It uses a new resource, the inference router, that gives your
  application one invocation path across the endpoints and inference components you already run, in one
  or more AWS Regions and AWS accounts. You register the destinations that serve a model, and your application
  invokes the router instead of a specific endpoint. The router keeps requests in its own Region while
  the local destination is healthy, shifts new requests to another registered destination when it isn’t,
  and returns traffic gradually after recovery. In this post, we explain how cross-Region inference routing
  decides where each request runs, walk through an example with one model in two Regions, and cover monitoring,
  limits, and what you pay. For a cross-account deployment that serves several models, see How Salesforce
  is advancing global-scale'
first_seen: '2026-11-20T03:16:25Z'
last_seen: '2026-11-20T03:16:25Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/keep-inference-running-through-regional-capacity-shortfalls-with-cross-region-inference-routing-in-amazon-sagemaker-ai/
  seen_at: '2026-11-20T03:16:25Z'
  metrics: {}
  kind: news
---

# Keep inference running through regional capacity shortfalls with cross-Region inference routing in Amazon SageMaker AI

Serving a model from more than one AWS Region is a well-established pattern for highly available inference: when one Region runs short of GPU capacity, requests move to another. The pattern is simple to describe and hard to operate. Until now, if you served models on Amazon SageMaker AI managed endpoints, cross-Region routing was a piece you still had to build yourself. Today, we’re introducing cross-Region inference routing in Amazon SageMaker AI. It uses a new resource, the inference router, that gives your application one invocation path across the endpoints and inference components you already run, in one or more AWS Regions and AWS accounts. You register the destinations that serve a model, and your application invokes the router instead of a specific endpoint. The router keeps requests in its own Region while the local destination is healthy, shifts new requests to another registered destination when it isn’t, and returns traffic gradually after recovery. In this post, we explain how cross-Region inference routing decides where each request runs, walk through an example with one model in two Regions, and cover monitoring, limits, and what you pay. For a cross-account deployment that serves several models, see How Salesforce is advancing global-scale

## 笔记


