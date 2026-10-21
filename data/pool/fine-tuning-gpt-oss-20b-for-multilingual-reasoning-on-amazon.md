---
slug: fine-tuning-gpt-oss-20b-for-multilingual-reasoning-on-amazon
name: Fine-tuning GPT-OSS-20B for multilingual reasoning on Amazon SageMaker HyperPod
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
url: https://aws.amazon.com/blogs/machine-learning/fine-tuning-gpt-oss-20b-for-multilingual-reasoning-on-amazon-sagemaker-hyperpod/
canonical_url: https://aws.amazon.com/blogs/machine-learning/fine-tuning-gpt-oss-20b-for-multilingual-reasoning-on-amazon-sagemaker-hyperpod
summary: 'GPT-OSS-20B is an open-weight reasoning model that thinks in English. Ask it to reason in French,
  German, Spanish, or Italian and it acknowledges the instruction, then produces its chain-of-thought
  in English anyway. On a 50-example multilingual reasoning test, the base model reasoned in the correct
  target language only 22 percent of the time. That 22 percent was almost entirely the English examples
  (English 100 percent, French 0 percent, German 10 percent, Spanish 0 percent, Italian 0 percent). For
  teams deploying reasoning models for non-English users, that gap matters. A user who asks a question
  in French expects the model to reason and answer in French, not to switch to English mid-thought. Closing
  that gap is a fine-tuning problem. It raises a question every team faces once they start customizing
  open-weight models: supervised fine-tuning (SFT), reinforcement learning with Group Relative Policy
  Optimization (GRPO), or both? In this post, we walk through how we fine-tuned GPT-OSS-20B for multilingual
  reasoning on Amazon SageMaker HyperPod . We show when SFT alone was sufficient and when GRPO added measurable
  value on top. To understand more broadly when GRPO helps, we also ran a controlled Qwen2.5-7B experiment
  across two tasks with different capability gaps. The short'
first_seen: '2026-10-21T00:38:23Z'
last_seen: '2026-10-21T00:38:23Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/fine-tuning-gpt-oss-20b-for-multilingual-reasoning-on-amazon-sagemaker-hyperpod/
  seen_at: '2026-10-21T00:38:23Z'
  metrics: {}
  kind: news
---

# Fine-tuning GPT-OSS-20B for multilingual reasoning on Amazon SageMaker HyperPod

GPT-OSS-20B is an open-weight reasoning model that thinks in English. Ask it to reason in French, German, Spanish, or Italian and it acknowledges the instruction, then produces its chain-of-thought in English anyway. On a 50-example multilingual reasoning test, the base model reasoned in the correct target language only 22 percent of the time. That 22 percent was almost entirely the English examples (English 100 percent, French 0 percent, German 10 percent, Spanish 0 percent, Italian 0 percent). For teams deploying reasoning models for non-English users, that gap matters. A user who asks a question in French expects the model to reason and answer in French, not to switch to English mid-thought. Closing that gap is a fine-tuning problem. It raises a question every team faces once they start customizing open-weight models: supervised fine-tuning (SFT), reinforcement learning with Group Relative Policy Optimization (GRPO), or both? In this post, we walk through how we fine-tuned GPT-OSS-20B for multilingual reasoning on Amazon SageMaker HyperPod . We show when SFT alone was sufficient and when GRPO added measurable value on top. To understand more broadly when GRPO helps, we also ran a controlled Qwen2.5-7B experiment across two tasks with different capability gaps. The short

## 笔记


