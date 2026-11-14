---
slug: production-mlops-at-gs-caltex-with-amazon-sagemaker-canvas-p
name: Production MLOps at GS Caltex with Amazon SageMaker Canvas, part 1
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
url: https://aws.amazon.com/blogs/machine-learning/production-mlops-at-gs-caltex-with-amazon-sagemaker-canvas-part-1/
canonical_url: https://aws.amazon.com/blogs/machine-learning/production-mlops-at-gs-caltex-with-amazon-sagemaker-canvas-part-1
summary: 'GS Caltex uses Amazon SageMaker Canvas and Amazon SageMaker Pipelines to connect process engineers’
  models to production workflows. The South Korean energy and chemical company divides model development
  and operations between engineers with complementary skills. Process engineers build and validate models
  in SageMaker Canvas without writing code, drawing on their process knowledge. Machine learning (ML)
  engineers configure SageMaker Pipelines workflows for deployment and scheduled inference. Moving assets
  from SageMaker Canvas into SageMaker Pipelines still required integration work. ML engineers had to
  set data paths for production, supply the model configuration, and connect preprocessing and inference
  jobs. GS Caltex automated this handoff while reusing the assets created in SageMaker Canvas. GS Caltex
  reports that its ML engineers now deploy models within a few hours, compared with about a week before.
  The company runs batch inference every 30 minutes, reducing the need for continuously running endpoints.
  GS Caltex reports that this has meaningfully lowered its inference costs. This post explains how GS
  Caltex connects SageMaker Canvas to SageMaker Pipelines and reuses validated preprocessing flows and
  models in production. Solution overview The machine learning operations (MLOps) workflow has two paths:
  preparing a new model version for deployment, and running batch inference with the'
first_seen: '2026-11-14T02:28:05Z'
last_seen: '2026-11-14T02:28:05Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/production-mlops-at-gs-caltex-with-amazon-sagemaker-canvas-part-1/
  seen_at: '2026-11-14T02:28:05Z'
  metrics: {}
  kind: news
---

# Production MLOps at GS Caltex with Amazon SageMaker Canvas, part 1

GS Caltex uses Amazon SageMaker Canvas and Amazon SageMaker Pipelines to connect process engineers’ models to production workflows. The South Korean energy and chemical company divides model development and operations between engineers with complementary skills. Process engineers build and validate models in SageMaker Canvas without writing code, drawing on their process knowledge. Machine learning (ML) engineers configure SageMaker Pipelines workflows for deployment and scheduled inference. Moving assets from SageMaker Canvas into SageMaker Pipelines still required integration work. ML engineers had to set data paths for production, supply the model configuration, and connect preprocessing and inference jobs. GS Caltex automated this handoff while reusing the assets created in SageMaker Canvas. GS Caltex reports that its ML engineers now deploy models within a few hours, compared with about a week before. The company runs batch inference every 30 minutes, reducing the need for continuously running endpoints. GS Caltex reports that this has meaningfully lowered its inference costs. This post explains how GS Caltex connects SageMaker Canvas to SageMaker Pipelines and reuses validated preprocessing flows and models in production. Solution overview The machine learning operations (MLOps) workflow has two paths: preparing a new model version for deployment, and running batch inference with the

## 笔记


