---
slug: write-your-own-training-loop-without-managing-gpus-with-amaz
name: Write your own training loop — without managing GPUs — with Amazon SageMaker training session APIs
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
url: https://aws.amazon.com/blogs/machine-learning/write-your-own-training-loop-without-managing-gpus-with-amazon-sagemaker-training-sessions/
canonical_url: https://aws.amazon.com/blogs/machine-learning/write-your-own-training-loop-without-managing-gpus-with-amazon-sagemaker-training-sessions
summary: 'Fine-tuning a large language model (LLM) today usually forces a tradeoff between training loop
  control and operational simplicity. With fully managed services you select a base model, provide data
  and hyperparameters, and the service owns everything else, which works well when a standard, prepackaged
  recipe fits your problem. Less managed services give you more control, but you also manage more of the
  underlying infrastructure and training frameworks. Sometimes a standard recipe isn’t enough: you need
  a custom loss or data curriculum for supervised fine-tuning (SFT), your own preference optimization,
  a reinforcement learning (RL) reward function, or an alignment algorithm published last week. As soon
  as you need to shape the training procedure yourself, you take on that infrastructure work to gain algorithmic
  freedom. Today, serverless model customization in Amazon SageMaker AI expands with training session
  APIs, which remove that tradeoff by drawing the abstraction boundary one level lower. Instead of abstracting
  away the algorithm, they abstract away the compute. Operations like forward_backward() , optim_step()
  , and sample() become SageMaker API calls that you compose into whatever procedure your technique requires:
  SFT, preference optimization, RL, or something new. The calls target a live, stateful session, so the
  model stays loaded on'
first_seen: '2026-10-23T00:41:16Z'
last_seen: '2026-10-23T00:41:16Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/write-your-own-training-loop-without-managing-gpus-with-amazon-sagemaker-training-sessions/
  seen_at: '2026-10-23T00:41:16Z'
  metrics: {}
  kind: news
---

# Write your own training loop — without managing GPUs — with Amazon SageMaker training session APIs

Fine-tuning a large language model (LLM) today usually forces a tradeoff between training loop control and operational simplicity. With fully managed services you select a base model, provide data and hyperparameters, and the service owns everything else, which works well when a standard, prepackaged recipe fits your problem. Less managed services give you more control, but you also manage more of the underlying infrastructure and training frameworks. Sometimes a standard recipe isn’t enough: you need a custom loss or data curriculum for supervised fine-tuning (SFT), your own preference optimization, a reinforcement learning (RL) reward function, or an alignment algorithm published last week. As soon as you need to shape the training procedure yourself, you take on that infrastructure work to gain algorithmic freedom. Today, serverless model customization in Amazon SageMaker AI expands with training session APIs, which remove that tradeoff by drawing the abstraction boundary one level lower. Instead of abstracting away the algorithm, they abstract away the compute. Operations like forward_backward() , optim_step() , and sample() become SageMaker API calls that you compose into whatever procedure your technique requires: SFT, preference optimization, RL, or something new. The calls target a live, stateful session, so the model stays loaded on

## 笔记


