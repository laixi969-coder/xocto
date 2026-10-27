---
slug: fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagema
name: Fleet-wide computer vision lifecycle at the edge with SageMaker SDK v3
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
url: https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
canonical_url: https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3
summary: Fleet-wide computer vision model lifecycle management is a problem that shows up the moment a
  quality inspection proof of concept succeeds. One camera and one model work fine. Then the plant asks
  for the same result on 40 lines, each with several cameras, and every camera sees the world differently.
  Each has a different angle, different glare off the same stainless surface, and different ambient light
  depending on which bay door is open. In production deployments we have worked on, a single model trained
  on pooled footage underperforms enough individual cameras that each camera ends up with its own fine-tuned
  model. Now the real problem is no longer training one model well. It’s training, evaluating, versioning,
  and shipping thousands of them without a human in the loop for each one. This post updates the pattern
  introduced in the 2023 series Build an end-to-end MLOps pipeline for visual quality inspection at the
  edge for the current Amazon SageMaker Python SDK v3. It replaces the since-deprecated Amazon SageMaker
  Edge Manager with Amazon SageMaker Neo for edge optimization. I walk through a dual-branch Amazon SageMaker
  Pipeline that trains an anomaly detector and a defect classifier per camera, with quality gates that
  block underperforming
first_seen: '2026-10-27T01:30:17Z'
last_seen: '2026-10-27T01:30:17Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
  seen_at: '2026-10-27T01:30:17Z'
  metrics: {}
  kind: news
---

# Fleet-wide computer vision lifecycle at the edge with SageMaker SDK v3

Fleet-wide computer vision model lifecycle management is a problem that shows up the moment a quality inspection proof of concept succeeds. One camera and one model work fine. Then the plant asks for the same result on 40 lines, each with several cameras, and every camera sees the world differently. Each has a different angle, different glare off the same stainless surface, and different ambient light depending on which bay door is open. In production deployments we have worked on, a single model trained on pooled footage underperforms enough individual cameras that each camera ends up with its own fine-tuned model. Now the real problem is no longer training one model well. It’s training, evaluating, versioning, and shipping thousands of them without a human in the loop for each one. This post updates the pattern introduced in the 2023 series Build an end-to-end MLOps pipeline for visual quality inspection at the edge for the current Amazon SageMaker Python SDK v3. It replaces the since-deprecated Amazon SageMaker Edge Manager with Amazon SageMaker Neo for edge optimization. I walk through a dual-branch Amazon SageMaker Pipeline that trains an anomaly detector and a defect classifier per camera, with quality gates that block underperforming

## 笔记


