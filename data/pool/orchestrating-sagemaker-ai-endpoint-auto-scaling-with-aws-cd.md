---
slug: orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cd
name: Orchestrating SageMaker AI endpoint auto scaling with AWS CDK
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
url: https://aws.amazon.com/blogs/machine-learning/orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cdk/
canonical_url: https://aws.amazon.com/blogs/machine-learning/orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cdk
summary: 'Updating the Amazon Sagemaker AI real-time endpoint configuration (changing the instance type,
  instance count, or environment variables) causes deployments through AWS CloudFormation or the AWS Cloud
  Development Kit (AWS CDK) to fail. SageMaker AI requires you to deregister the scalable target before
  updating the endpoint, but when you deregister it, CloudFormation can’t track the AWS Application Auto
  Scaling resources. In this post, we show you how to use a reusable CDK construct with AWS CloudFormation
  custom resources to orchestrate deregister and register auto scaling automatically during endpoint updates.
  You can update your endpoint configuration and auto scaling parameters in a single deployment without
  manual intervention. Why this problem occurs When you deploy a SageMaker AI endpoint with native CloudFormation
  auto scaling resources, then change the endpoint configuration and redeploy, several failure modes emerge.
  The specific failure depends on what you change and how you work around the issue. Changing the endpoint
  configuration with auto scaling registered CloudFormation tries to update the endpoint while the scalable
  target is still registered. SageMaker AI rejects the update with the following error: The variant(s)
  "[AllTraffic]" must be deregistered as scalable targets with Application Auto Scaling before they can
  be removed or have their instance'
first_seen: '2026-10-24T00:43:47Z'
last_seen: '2026-10-24T00:43:47Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cdk/
  seen_at: '2026-10-24T00:43:47Z'
  metrics: {}
  kind: news
---

# Orchestrating SageMaker AI endpoint auto scaling with AWS CDK

Updating the Amazon Sagemaker AI real-time endpoint configuration (changing the instance type, instance count, or environment variables) causes deployments through AWS CloudFormation or the AWS Cloud Development Kit (AWS CDK) to fail. SageMaker AI requires you to deregister the scalable target before updating the endpoint, but when you deregister it, CloudFormation can’t track the AWS Application Auto Scaling resources. In this post, we show you how to use a reusable CDK construct with AWS CloudFormation custom resources to orchestrate deregister and register auto scaling automatically during endpoint updates. You can update your endpoint configuration and auto scaling parameters in a single deployment without manual intervention. Why this problem occurs When you deploy a SageMaker AI endpoint with native CloudFormation auto scaling resources, then change the endpoint configuration and redeploy, several failure modes emerge. The specific failure depends on what you change and how you work around the issue. Changing the endpoint configuration with auto scaling registered CloudFormation tries to update the endpoint while the scalable target is still registered. SageMaker AI rejects the update with the following error: The variant(s) "[AllTraffic]" must be deregistered as scalable targets with Application Auto Scaling before they can be removed or have their instance

## 笔记


