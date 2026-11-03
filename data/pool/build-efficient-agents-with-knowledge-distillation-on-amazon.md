---
slug: build-efficient-agents-with-knowledge-distillation-on-amazon
name: Build efficient agents with knowledge distillation on Amazon SageMaker AI
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
url: https://aws.amazon.com/blogs/machine-learning/build-efficient-agents-with-knowledge-distillation-on-amazon-sagemaker-ai/
canonical_url: https://aws.amazon.com/blogs/machine-learning/build-efficient-agents-with-knowledge-distillation-on-amazon-sagemaker-ai
summary: 'You built a shopping assistant on a frontier model, and it works. A shopper asks for “a black
  waist bag under twenty dollars from a shop with at least 4.5 stars,” and the agent searches the catalog,
  inspects candidates, checks the constraints, and commits to a recommendation. But what does that interaction
  actually cost? An agentic assistant is not one model call, it is a loop: search, read results, refine,
  verify, decide. A single completed task can be multiple calls to that frontier model, and you pay for
  every one, on every shopper. At production scale, that per-task cost compounds, erodes the project’s
  ROI, and stops the project from shipping. One way to make an agentic application more efficient is to
  use a smaller model, which is faster to respond and more cost-effective to host. The catch is quality:
  a smaller model usually falls short on the task, which is why the larger one was chosen in the first
  place. Knowledge distillation closes that gap by transferring the behavior of the larger “teacher” model
  into a smaller “student”, training the student to reproduce the teacher’s outputs, so it keeps much
  of the quality at the smaller model’s speed and cost.'
first_seen: '2026-11-03T03:29:26Z'
last_seen: '2026-11-03T03:29:26Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/build-efficient-agents-with-knowledge-distillation-on-amazon-sagemaker-ai/
  seen_at: '2026-11-03T03:29:26Z'
  metrics: {}
  kind: news
---

# Build efficient agents with knowledge distillation on Amazon SageMaker AI

You built a shopping assistant on a frontier model, and it works. A shopper asks for “a black waist bag under twenty dollars from a shop with at least 4.5 stars,” and the agent searches the catalog, inspects candidates, checks the constraints, and commits to a recommendation. But what does that interaction actually cost? An agentic assistant is not one model call, it is a loop: search, read results, refine, verify, decide. A single completed task can be multiple calls to that frontier model, and you pay for every one, on every shopper. At production scale, that per-task cost compounds, erodes the project’s ROI, and stops the project from shipping. One way to make an agentic application more efficient is to use a smaller model, which is faster to respond and more cost-effective to host. The catch is quality: a smaller model usually falls short on the task, which is why the larger one was chosen in the first place. Knowledge distillation closes that gap by transferring the behavior of the larger “teacher” model into a smaller “student”, training the student to reproduce the teacher’s outputs, so it keeps much of the quality at the smaller model’s speed and cost.

## 笔记


