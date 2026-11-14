---
slug: build-a-model-improvement-flywheel-with-amazon-sagemaker-hyp
name: Build a model improvement flywheel with Amazon SageMaker HyperPod Data Capture
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
url: https://aws.amazon.com/blogs/machine-learning/build-a-model-improvement-flywheel-with-amazon-sagemaker-hyperpod-data-capture/
canonical_url: https://aws.amazon.com/blogs/machine-learning/build-a-model-improvement-flywheel-with-amazon-sagemaker-hyperpod-data-capture
summary: 'Foundation models deployed on Amazon SageMaker HyperPod meet inputs that no pre-curated dataset
  covers: domain-specific jargon, unexpected formats, new products, and changing user behavior. Without
  a record of production inference data, teams can’t detect drift, find failure patterns, or use real
  interactions to improve the model. Amazon SageMaker HyperPod now provides Data Capture, a built-in capability
  that records live inference inputs and outputs to Amazon Simple Storage Service (Amazon S3) at three
  independent tiers, with minimal latency impact and zero impact on model availability. In this post,
  we walk through one complete example on a single SageMaker HyperPod cluster. A home-appliance support
  router captures its production traffic, Amazon Athena queries surface a new-product blind spot, a SQL
  policy labels the captured records, and a fine-tune on that data teaches the router the new product.
  We measure accuracy before and after, on data that could not have existed before the model was deployed.
  The inference operator serves the model on one node, and the training operator runs the fine-tuning
  on another. We use synthetic data for the walkthrough. The scripts, manifests, SQL, synthetic datasets,
  and expected outputs are available in the accompanying GitHub repository . Three-tier Data Capture architecture
  HyperPod Data'
first_seen: '2026-11-14T02:28:05Z'
last_seen: '2026-11-14T02:28:05Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/build-a-model-improvement-flywheel-with-amazon-sagemaker-hyperpod-data-capture/
  seen_at: '2026-11-14T02:28:05Z'
  metrics: {}
  kind: news
---

# Build a model improvement flywheel with Amazon SageMaker HyperPod Data Capture

Foundation models deployed on Amazon SageMaker HyperPod meet inputs that no pre-curated dataset covers: domain-specific jargon, unexpected formats, new products, and changing user behavior. Without a record of production inference data, teams can’t detect drift, find failure patterns, or use real interactions to improve the model. Amazon SageMaker HyperPod now provides Data Capture, a built-in capability that records live inference inputs and outputs to Amazon Simple Storage Service (Amazon S3) at three independent tiers, with minimal latency impact and zero impact on model availability. In this post, we walk through one complete example on a single SageMaker HyperPod cluster. A home-appliance support router captures its production traffic, Amazon Athena queries surface a new-product blind spot, a SQL policy labels the captured records, and a fine-tune on that data teaches the router the new product. We measure accuracy before and after, on data that could not have existed before the model was deployed. The inference operator serves the model on one node, and the training operator runs the fine-tuning on another. We use synthetic data for the walkthrough. The scripts, manifests, SQL, synthetic datasets, and expected outputs are available in the accompanying GitHub repository . Three-tier Data Capture architecture HyperPod Data

## 笔记


