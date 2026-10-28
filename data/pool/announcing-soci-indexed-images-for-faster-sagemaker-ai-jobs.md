---
slug: announcing-soci-indexed-images-for-faster-sagemaker-ai-jobs
name: Announcing SOCI-indexed images for faster SageMaker AI jobs
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
url: https://aws.amazon.com/blogs/machine-learning/announcing-soci-indexed-images-for-faster-sagemaker-ai-jobs/
canonical_url: https://aws.amazon.com/blogs/machine-learning/announcing-soci-indexed-images-for-faster-sagemaker-ai-jobs
summary: 'Every minute your deep learning container image spends downloading is a minute you pay for and
  a minute your team waits. Container image download is pure overhead: billable job time that produces
  no model progress. For modern deep learning images, that overhead is several minutes on every single
  job. Today, we’re excited to announce Seekable OCI (SOCI) indexing for Amazon SageMaker AI Training
  and Amazon SageMaker AI processing jobs , which takes full container image download off the critical
  path of every job. With SOCI indexing, SageMaker AI lazy-loads your container image. It fetches only
  the files needed to start the container and streams the rest in the background as your code runs, so
  your job begins in seconds instead of minutes. You adopt it by pointing to a pre-indexed AWS Deep Learning
  Container (DLC) or adding an index to your own image. Neither approach requires changes to your job
  definition, entry point, or data channels. The result is faster job starts, lower job cost, and more
  time spent building models rather than waiting on infrastructure. SOCI-indexed images start Amazon SageMaker
  AI training containers in seconds, with no impact on training performance. As we show in the What we
  measured'
first_seen: '2026-10-28T01:23:01Z'
last_seen: '2026-10-28T01:23:01Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/announcing-soci-indexed-images-for-faster-sagemaker-ai-jobs/
  seen_at: '2026-10-28T01:23:01Z'
  metrics: {}
  kind: news
---

# Announcing SOCI-indexed images for faster SageMaker AI jobs

Every minute your deep learning container image spends downloading is a minute you pay for and a minute your team waits. Container image download is pure overhead: billable job time that produces no model progress. For modern deep learning images, that overhead is several minutes on every single job. Today, we’re excited to announce Seekable OCI (SOCI) indexing for Amazon SageMaker AI Training and Amazon SageMaker AI processing jobs , which takes full container image download off the critical path of every job. With SOCI indexing, SageMaker AI lazy-loads your container image. It fetches only the files needed to start the container and streams the rest in the background as your code runs, so your job begins in seconds instead of minutes. You adopt it by pointing to a pre-indexed AWS Deep Learning Container (DLC) or adding an index to your own image. Neither approach requires changes to your job definition, entry point, or data channels. The result is faster job starts, lower job cost, and more time spent building models rather than waiting on infrastructure. SOCI-indexed images start Amazon SageMaker AI training containers in seconds, with no impact on training performance. As we show in the What we measured

## 笔记


