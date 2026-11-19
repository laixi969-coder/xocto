---
slug: how-salesforce-is-advancing-global-scale-model-serving-with
name: How Salesforce is advancing global-scale model serving with cross-Region inference routing in Amazon
  SageMaker AI
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
url: https://aws.amazon.com/blogs/machine-learning/how-salesforce-is-advancing-global-scale-model-serving-with-cross-region-inference-routing-in-amazon-sagemaker-ai/
canonical_url: https://aws.amazon.com/blogs/machine-learning/how-salesforce-is-advancing-global-scale-model-serving-with-cross-region-inference-routing-in-amazon-sagemaker-ai
summary: Thanks to Amit Gupta, Senior Director- AI/ML and Mark Wang, Software Engineering PMTS from Salesforce
  for your contributions in the vision and partnership of cross-Region inference routing on SageMaker
  AI. Salesforce’s Agentforce Foundation team serves a wide variety of models for products across Salesforce,
  including Agentforce and the Salesforce Trust Layer, in 30+ global Regions. These include both models
  trained in house and open source models. Hosting models separately in each Region splits capacity and
  makes traffic spikes harder to absorb, which turns a capacity shortfall into an availability problem.
  This post shows how Salesforce set up the cross-Region inference routing in SageMaker AI and how it
  lets the team add capacity securely while keeping its data residency commitments. It also walks through
  how Salesforce sees where each request was served and why. The cross-Region inference routing gives
  an application one invocation path across SageMaker AI endpoints in several Regions and accounts, and
  sends each request to an endpoint that can serve it. Those endpoints are Salesforce’s own, already deployed.
  The post starts with the capacity problem Salesforce faced, explains how the router works and how Salesforce
  integrated it into its Internal Gateway, walks through an example setup, and then
first_seen: '2026-11-19T03:28:37Z'
last_seen: '2026-11-19T03:28:37Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/how-salesforce-is-advancing-global-scale-model-serving-with-cross-region-inference-routing-in-amazon-sagemaker-ai/
  seen_at: '2026-11-19T03:28:37Z'
  metrics: {}
  kind: news
---

# How Salesforce is advancing global-scale model serving with cross-Region inference routing in Amazon SageMaker AI

Thanks to Amit Gupta, Senior Director- AI/ML and Mark Wang, Software Engineering PMTS from Salesforce for your contributions in the vision and partnership of cross-Region inference routing on SageMaker AI. Salesforce’s Agentforce Foundation team serves a wide variety of models for products across Salesforce, including Agentforce and the Salesforce Trust Layer, in 30+ global Regions. These include both models trained in house and open source models. Hosting models separately in each Region splits capacity and makes traffic spikes harder to absorb, which turns a capacity shortfall into an availability problem. This post shows how Salesforce set up the cross-Region inference routing in SageMaker AI and how it lets the team add capacity securely while keeping its data residency commitments. It also walks through how Salesforce sees where each request was served and why. The cross-Region inference routing gives an application one invocation path across SageMaker AI endpoints in several Regions and accounts, and sends each request to an endpoint that can serve it. Those endpoints are Salesforce’s own, already deployed. The post starts with the capacity problem Salesforce faced, explains how the router works and how Salesforce integrated it into its Internal Gateway, walks through an example setup, and then

## 笔记


