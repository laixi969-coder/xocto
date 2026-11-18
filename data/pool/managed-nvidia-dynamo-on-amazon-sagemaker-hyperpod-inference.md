---
slug: managed-nvidia-dynamo-on-amazon-sagemaker-hyperpod-inference
name: Managed NVIDIA Dynamo on Amazon SageMaker HyperPod Inference
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
url: https://aws.amazon.com/blogs/machine-learning/managed-nvidia-dynamo-on-amazon-sagemaker-hyperpod-inference/
canonical_url: https://aws.amazon.com/blogs/machine-learning/managed-nvidia-dynamo-on-amazon-sagemaker-hyperpod-inference
summary: 'Serving large language models (LLMs) efficiently requires sufficient GPU memory and careful
  coordination of prompt processing and token generation. GLM-5.3’s FP8 weights, for example, exceed the
  640 GB of GPU memory on a single ml.p5.48xlarge instance, before accounting for KV cache and runtime
  overhead. Long prompts can also slow token generation when both share the same GPUs. Amazon SageMaker
  HyperPod Inference now supports NVIDIA Dynamo , combining Dynamo’s distributed inference capabilities
  with the infrastructure management of HyperPod to address these challenges. Dynamo is an open source
  distributed inference framework that supports multi-node deployment, disaggregated prefill and decode,
  and KV-aware routing with engines such as vLLM, SGLang, and TensorRT-LLM. HyperPod supports these deployments
  with high-performance Elastic Fabric Adapter (EFA) networking, coordinated GPU scheduling, and node
  health monitoring and recovery. In this post, we illustrate multi-node and disaggregated serving through
  a deployment example, share benchmark results, and outline best practices for optimizing inference on
  HyperPod. How the integration works The HyperPod Inference add-on installs the Dynamo custom resource
  definitions and these serving and scheduling components: HyperPod Inference Operator manages endpoint
  deployment through an InferenceEndpointConfig (IEC) custom resource. Its dynamoSpec section supplies
  the Dynamo configuration. Dynamo operator manages resources defined in a DynamoGraphDeployment'
first_seen: '2026-11-18T03:43:37Z'
last_seen: '2026-11-18T03:43:37Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/managed-nvidia-dynamo-on-amazon-sagemaker-hyperpod-inference/
  seen_at: '2026-11-18T03:43:37Z'
  metrics: {}
  kind: news
---

# Managed NVIDIA Dynamo on Amazon SageMaker HyperPod Inference

Serving large language models (LLMs) efficiently requires sufficient GPU memory and careful coordination of prompt processing and token generation. GLM-5.3’s FP8 weights, for example, exceed the 640 GB of GPU memory on a single ml.p5.48xlarge instance, before accounting for KV cache and runtime overhead. Long prompts can also slow token generation when both share the same GPUs. Amazon SageMaker HyperPod Inference now supports NVIDIA Dynamo , combining Dynamo’s distributed inference capabilities with the infrastructure management of HyperPod to address these challenges. Dynamo is an open source distributed inference framework that supports multi-node deployment, disaggregated prefill and decode, and KV-aware routing with engines such as vLLM, SGLang, and TensorRT-LLM. HyperPod supports these deployments with high-performance Elastic Fabric Adapter (EFA) networking, coordinated GPU scheduling, and node health monitoring and recovery. In this post, we illustrate multi-node and disaggregated serving through a deployment example, share benchmark results, and outline best practices for optimizing inference on HyperPod. How the integration works The HyperPod Inference add-on installs the Dynamo custom resource definitions and these serving and scheduling components: HyperPod Inference Operator manages endpoint deployment through an InferenceEndpointConfig (IEC) custom resource. Its dynamoSpec section supplies the Dynamo configuration. Dynamo operator manages resources defined in a DynamoGraphDeployment

## 笔记


