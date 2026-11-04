---
slug: qwen-38-27b-on-my-laptop-can-interpret-model-weights-too
name: Qwen 3.8 27B on my laptop can interpret model weights, too
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
url: https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
canonical_url: https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights
summary: 'Yesterday''s hot paper was Sparks of Weight-Space Programming: LLMs can natively read & write
  neural network weights by Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab. The paper (OK, the
  authors classify is as a "blog post", but it''s paper-shaped) found that frontier models, in particular
  GPT-6 Astra, can both interpret and modify the raw weights of a machine learning model - literally a
  text description of the model containing a bunch of floating point numbers. I''ve been playing with
  one of the examples from the paper and I''m delighted to share that Qwen 3.8 27B running on my laptop
  can do this as well! Weight-Space Programming Here''s the highlight from their abstract, describing
  impressive capabilities for GPT-6 Astra and coining the term Weight-Space Programming for when LLMs
  analyze and modify model weights: Just by looking at the raw weights, GPT-6 Astra can tell what a network
  was trained to do . And without any environment feedback, it has no trouble writing, from scratch, small
  game-playing networks that outplay networks trained with PPO for 100 million steps. Likewise, asked
  to make Qwen3.5-0.8B better at math without gradients, Astra identifies an issue in its weights causing
  reasoning loops that Qwen’s'
first_seen: '2026-11-04T02:21:17Z'
last_seen: '2026-11-04T02:21:17Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
  seen_at: '2026-11-04T02:21:17Z'
  metrics: {}
  kind: news
---

# Qwen 3.8 27B on my laptop can interpret model weights, too

Yesterday's hot paper was Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights by Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab. The paper (OK, the authors classify is as a "blog post", but it's paper-shaped) found that frontier models, in particular GPT-6 Astra, can both interpret and modify the raw weights of a machine learning model - literally a text description of the model containing a bunch of floating point numbers. I've been playing with one of the examples from the paper and I'm delighted to share that Qwen 3.8 27B running on my laptop can do this as well! Weight-Space Programming Here's the highlight from their abstract, describing impressive capabilities for GPT-6 Astra and coining the term Weight-Space Programming for when LLMs analyze and modify model weights: Just by looking at the raw weights, GPT-6 Astra can tell what a network was trained to do . And without any environment feedback, it has no trouble writing, from scratch, small game-playing networks that outplay networks trained with PPO for 100 million steps. Likewise, asked to make Qwen3.5-0.8B better at math without gradients, Astra identifies an issue in its weights causing reasoning loops that Qwen’s

## 笔记


