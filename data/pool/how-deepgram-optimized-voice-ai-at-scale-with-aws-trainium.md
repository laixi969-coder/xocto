---
slug: how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium
name: How Deepgram optimized voice AI at scale with AWS Trainium
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
url: https://aws.amazon.com/blogs/machine-learning/how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium/
canonical_url: https://aws.amazon.com/blogs/machine-learning/how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium
summary: As voice becomes a first-class modality for AI, Deepgram’s models span speech-to-text, text-to-speech,
  and voice agents. They now process quadrillions of audio tokens a year for more than 200,000 developers
  and 1,400 organizations. Customers use them through the Deepgram API or run them in their own environments,
  including on Amazon SageMaker AI. For Deepgram, serving efficiency determines how much audio the system
  can process for a given infrastructure budget. High-volume batch workloads put heavy pressure on that
  budget, so the more efficiently each accelerator hour is used, the more audio Deepgram can serve on
  the same fleet. That made inference efficiency a natural target and Deepgram turned to AWS AI chips
  to improve it. They worked with AWS to bring its Nova-3 speech-to-text model to AWS Trainium2 for offline
  batch workloads such as contact-center analytics and medical transcription. The engagement began with
  Deepgram delivering Nova-3 as standard PyTorch code. Over several months, Deepgram and the AWS Forward
  Deployed Engineering (FDE) team ported Nova-3 to AWS Trainium2 in PyTorch reconstruction and tuned it
  for the new hardware. The final configuration runs eight model replicas on a single Amazon Elastic Compute
  Cloud (Amazon EC2) trn2.3xlarge instance. On Deepgram’s offline, throughput-oriented batch workloads,
first_seen: '2026-10-20T01:06:54Z'
last_seen: '2026-10-20T01:06:54Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium/
  seen_at: '2026-10-20T01:06:54Z'
  metrics: {}
  kind: news
---

# How Deepgram optimized voice AI at scale with AWS Trainium

As voice becomes a first-class modality for AI, Deepgram’s models span speech-to-text, text-to-speech, and voice agents. They now process quadrillions of audio tokens a year for more than 200,000 developers and 1,400 organizations. Customers use them through the Deepgram API or run them in their own environments, including on Amazon SageMaker AI. For Deepgram, serving efficiency determines how much audio the system can process for a given infrastructure budget. High-volume batch workloads put heavy pressure on that budget, so the more efficiently each accelerator hour is used, the more audio Deepgram can serve on the same fleet. That made inference efficiency a natural target and Deepgram turned to AWS AI chips to improve it. They worked with AWS to bring its Nova-3 speech-to-text model to AWS Trainium2 for offline batch workloads such as contact-center analytics and medical transcription. The engagement began with Deepgram delivering Nova-3 as standard PyTorch code. Over several months, Deepgram and the AWS Forward Deployed Engineering (FDE) team ported Nova-3 to AWS Trainium2 in PyTorch reconstruction and tuned it for the new hardware. The final configuration runs eight model replicas on a single Amazon Elastic Compute Cloud (Amazon EC2) trn2.3xlarge instance. On Deepgram’s offline, throughput-oriented batch workloads,

## 笔记


