---
slug: spreading-the-load-how-salesforce-met-multi-az-ha-with-sagem
name: Salesforce
builder: ''
category: ''
summary_zh: Salesforce 是客户关系管理软件公司，此次使用 AWS SageMaker 推理组件实现多可用区高可用部署，满足合规要求。另有报道讨论其 AI 收费模式变化，但具体细节未披露。
inspiration: ''
summary_en: Salesforce is a CRM software company. It used AWS SageMaker inference components to achieve
  Multi-AZ high availability, meeting compliance. Reports also discuss its AI pricing model changes, but
  details are undisclosed.
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
url: https://aws.amazon.com/blogs/machine-learning/spreading-the-load-how-salesforce-met-multi-az-ha-with-sagemaker-inference-components/
canonical_url: https://aws.amazon.com/blogs/machine-learning/spreading-the-load-how-salesforce-met-multi-az-ha-with-sagemaker-inference-components
summary: Learn how Salesforce used Amazon SageMaker AI Inference Component placement (the SchedulingConfig
  parameter) to distribute model copies across multiple Availability Zones, meeting their Multi-AZ high
  availability compliance requirements without sacrificing the cost efficiency of multi-model co-hosting.
first_seen: '2026-08-28T16:20:40Z'
last_seen: '2026-09-01T14:56:33Z'
status: pending_filter
sources:
- officialfeeds
- newssearch
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/spreading-the-load-how-salesforce-met-multi-az-ha-with-sagemaker-inference-components/
  seen_at: '2026-08-29T03:43:28Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiU0FVX3lxTE1xdmF1X25aSGhuUS1lQlg2VlQ4b2xTczV3OVFnUW4zWTNQaHc4am1ibXdxUXRRblBlT05BV2VsLVloUkYzMVBUN0VodTc5YWFwSXZJ?oc=5
  seen_at: '2026-08-31T17:38:59Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMihwFBVV95cUxNbzFHTkZCUVA1WW4zS2tpR082M2VfbV9BNklQSXRJWlpqNHMwWGdadElTX2JZUGduSHFDamExX1VUU1ppaFlDaG1xNTBEcjBUZW9xMzJnR1l6TU90QkVqTE13azZseWU3bnNkMFlveFpQTVdMTXA4Ykp6bUNzbUtkdnN0clNxdjA?oc=5
  seen_at: '2026-08-31T17:38:59Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiwwFBVV95cUxPSG9hREpQaGFLUFMzbTBRcmpUcmt5UXdVR014ZmMwbW5kQmJkeVAyX19tRDdocTRwdEt6T19YZlNWNXRPQklvNkQxeUhaMnhydVBvcW91VEJIVU1XWkdqYkZoLXBxS3FsQ1dtSjBnQ1V4eEFUTDdtZWtsNUttclhYRUdNU05UVzY1d0l2bm5zMlplVnVNV0tzTmdob1FWbGpRV0xNaGwzczFvMkZmaVVlVWdlN1l5bWNMV0w5U1d4RFNVWm_SAcMBQVVfeXFMT0hvYURKUGhhS1BTM20wUXJqVHJreVF3VUdNeGZjMG1uZEJiZHlQMl9fbUQ3aHE0cHRLek9fWGZTVjV0T0JJbzZEMXlIWjJ4cnVQb3FvdVRCSFVNV1pHamJGaC1wcUtxbENXbUowZ0NVeHhBVEw3bWVrbDVLbXJYWEVHTVNOVFc2NXdJdm5uczJaZVZ1TVdLc05naG9RVmxqUVdMTWhsM3MxbzJGZmlVZVVnZTdZeW1jTFdMOVNXeERTVVpv?oc=5
  seen_at: '2026-09-01T14:56:33Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMipAFBVV95cUxPWU5kdE1Ic2U3M0cxSng3Mm5mbnNxWTVzZHRCRk9kVDk5bnljczBUNWJxR3drbWI2STFwd1liVGdRRXE2VHBuaGtpazRiUzFwVG1VNUVzVHVhX1NlSTMyQnpwcGtpVnYwYW5VY3hjV3RwQlJGYXRfazlQV0Y5ZjgzM0V1UG1zZGpoRzk3UlRESE9HVFFMOUtHUlhYcWRSc3lUYWp6Mw?oc=5
  seen_at: '2026-09-01T14:56:33Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiT0FVX3lxTE9nTzgwLXhuWkI3VzJSX192d1BCQ0ZYNC0wM1BoZGVna2wzaldlMEVqcTY4WFN3SXpXQlJCVENXZUZvZnJ4VEhjTXNraFA2Xzg?oc=5
  seen_at: '2026-09-01T14:56:33Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMib0FVX3lxTE9xS1Z1VjN5cDZvQTR6ekJ0cWFpeEFZbVE2WFM2RERudUdQazUwSHpZWnhOU3NhU21qZXRKS3NqWjB1ZmxrNEM3d2hVSjdnM1JMZ21PNzlPUmh6dEdvNlZLQzNuTmN5QTFjdktRVUxpaw?oc=5
  seen_at: '2026-09-01T14:56:33Z'
  metrics: {}
  kind: news
---

# Salesforce

Learn how Salesforce used Amazon SageMaker AI Inference Component placement (the SchedulingConfig parameter) to distribute model copies across multiple Availability Zones, meeting their Multi-AZ high availability compliance requirements without sacrificing the cost efficiency of multi-model co-hosting.

## 笔记


