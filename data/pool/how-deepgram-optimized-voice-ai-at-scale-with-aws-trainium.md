---
slug: how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium
name: Deepgram
builder: ''
category: 基础层
summary_zh: 呼叫中心质检、医院病案转写和媒体字幕团队在需要把大批录音转成文字与分析结果时，把音频交给 Deepgram 的语音转写与语音代理模型，由模型输出文字稿、通话分析和语音回复；本次新增的是这些离线批量任务可跑在
  AWS Trainium2 上，单实例承载八个模型副本，具体交付质量与人工复核环节仍待核验。
inspiration: 趋势：语音转写正从按分钟计费的云 API 变成可自建、可压成本的批量基础设施，推理效率直接决定同样预算能处理多少小时音频。切入：不要做通用转写 API，而是从呼叫中心质检或病案转写这类有合规与结构化要求的环节进入，按处理小时或按质检报告收费，把行业词表、脱敏和人工复核流程做成壁垒。
summary_en: When contact-centre QA, hospital transcription and media subtitle teams need to turn large
  volumes of recordings into text and analysis, they send audio to Deepgram's speech-to-text and voice-agent
  models, which return transcripts, call analysis and spoken replies; the new fact is that these offline
  batch jobs can run on AWS Trainium2 with eight model replicas per instance, while delivery quality and
  human review steps remain to be verified.
inspiration_en: 'Trend: speech transcription is moving from per-minute cloud APIs to batch infrastructure
  that can be self-hosted and cost-tuned, so inference efficiency decides how many audio hours a fixed
  budget buys. Entry: avoid a generic transcription API and start from a compliance-heavy step such as
  contact-centre QA or medical transcription, charging per processed hour or per QA report, with domain
  vocabularies, de-identification and human review as the moat.'
priority_review: false
project_type: ai_transformation
industries:
- 呼叫中心与客户服务
- 医疗健康
- 媒体与内容
industries_en:
- Call centres and customer service
- Healthcare
- Media and content
jobs:
- 呼叫中心质检人员批量回听通话录音并整理合规与满意度分析
- 医院病案与转写人员把门诊或住院录音整理成结构化病历文本
- 媒体团队把长音频节目转成可检索的文字稿与字幕
jobs_en:
- Contact-centre QA staff replaying call recordings in bulk to produce compliance and satisfaction analysis
- Hospital transcription staff turning clinic or ward recordings into structured medical records
- Media teams converting long audio programmes into searchable transcripts and subtitles
regions:
- 美国
regions_en:
- United States
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
status: queued
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium/
  seen_at: '2026-10-20T01:06:54Z'
  metrics: {}
  kind: news
---

# Deepgram

As voice becomes a first-class modality for AI, Deepgram’s models span speech-to-text, text-to-speech, and voice agents. They now process quadrillions of audio tokens a year for more than 200,000 developers and 1,400 organizations. Customers use them through the Deepgram API or run them in their own environments, including on Amazon SageMaker AI. For Deepgram, serving efficiency determines how much audio the system can process for a given infrastructure budget. High-volume batch workloads put heavy pressure on that budget, so the more efficiently each accelerator hour is used, the more audio Deepgram can serve on the same fleet. That made inference efficiency a natural target and Deepgram turned to AWS AI chips to improve it. They worked with AWS to bring its Nova-3 speech-to-text model to AWS Trainium2 for offline batch workloads such as contact-center analytics and medical transcription. The engagement began with Deepgram delivering Nova-3 as standard PyTorch code. Over several months, Deepgram and the AWS Forward Deployed Engineering (FDE) team ported Nova-3 to AWS Trainium2 in PyTorch reconstruction and tuned it for the new hardware. The final configuration runs eight model replicas on a single Amazon Elastic Compute Cloud (Amazon EC2) trn2.3xlarge instance. On Deepgram’s offline, throughput-oriented batch workloads,

## 笔记


