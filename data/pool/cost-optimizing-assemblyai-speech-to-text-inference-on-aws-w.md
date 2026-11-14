---
slug: cost-optimizing-assemblyai-speech-to-text-inference-on-aws-w
name: Cost-optimizing AssemblyAI speech-to-text inference on AWS with Amazon EC2 Spot
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
url: https://aws.amazon.com/blogs/machine-learning/cost-optimizing-assemblyai-speech-to-text-inference-on-aws-with-amazon-ec2-spot/
canonical_url: https://aws.amazon.com/blogs/machine-learning/cost-optimizing-assemblyai-speech-to-text-inference-on-aws-with-amazon-ec2-spot
summary: Speech-to-text inference is computationally intensive. Each audio file triggers a pipeline of
  deep learning models (acoustic models, language models, and post-processing stages) running on NVIDIA
  GPUs to meet latency requirements. At scale, this means thousands of GPU instances running continuously.
  AssemblyAI needed a way to run GPU-intensive inference workloads cost-effectively at scale, without
  sacrificing the availability and latency guarantees their customers depend on. Running entirely on On-Demand
  Instances would be cost-prohibitive. Spot Instances offer significant savings, while Amazon Elastic
  Compute Cloud (Amazon EC2) can reclaim them with a 2-minute warning when capacity is needed elsewhere.
  AssemblyAI needed an architecture that absorbs Spot interruptions gracefully while maintaining service
  level agreement (SLA) commitments. Additionally, customers in regulated industries, including healthcare,
  finance, and legal, must keep audio data within specific geographic boundaries. They implement strict
  data residency configurations in European AWS Regions. Available on AWS Marketplace , AssemblyAI provides
  an API for transcription, speaker detection, sentiment analysis, chapter detection, and personally identifiable
  information (PII) redaction. Their models transcribe and analyze speech for high-volume workloads across
  industries including technology, media, healthcare, and financial services. In this post, we show you
  how AssemblyAI runs cost-optimized AI inference at scale for their speech-to-text platform. The architecture
first_seen: '2026-11-14T02:28:05Z'
last_seen: '2026-11-14T02:28:05Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/cost-optimizing-assemblyai-speech-to-text-inference-on-aws-with-amazon-ec2-spot/
  seen_at: '2026-11-14T02:28:05Z'
  metrics: {}
  kind: news
---

# Cost-optimizing AssemblyAI speech-to-text inference on AWS with Amazon EC2 Spot

Speech-to-text inference is computationally intensive. Each audio file triggers a pipeline of deep learning models (acoustic models, language models, and post-processing stages) running on NVIDIA GPUs to meet latency requirements. At scale, this means thousands of GPU instances running continuously. AssemblyAI needed a way to run GPU-intensive inference workloads cost-effectively at scale, without sacrificing the availability and latency guarantees their customers depend on. Running entirely on On-Demand Instances would be cost-prohibitive. Spot Instances offer significant savings, while Amazon Elastic Compute Cloud (Amazon EC2) can reclaim them with a 2-minute warning when capacity is needed elsewhere. AssemblyAI needed an architecture that absorbs Spot interruptions gracefully while maintaining service level agreement (SLA) commitments. Additionally, customers in regulated industries, including healthcare, finance, and legal, must keep audio data within specific geographic boundaries. They implement strict data residency configurations in European AWS Regions. Available on AWS Marketplace , AssemblyAI provides an API for transcription, speaker detection, sentiment analysis, chapter detection, and personally identifiable information (PII) redaction. Their models transcribe and analyze speech for high-volume workloads across industries including technology, media, healthcare, and financial services. In this post, we show you how AssemblyAI runs cost-optimized AI inference at scale for their speech-to-text platform. The architecture

## 笔记


