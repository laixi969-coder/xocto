---
slug: normalizing-trajectory-models
name: Normalizing Trajectory Models
builder: ''
category: ''
summary_zh: 这是一项模型方法研究：把扩散生成的反向过程拆成带精确似然的归一化流步骤，目标是让少步采样不再牺牲似然框架。它面向的是训练和推理生成模型的研究与工程环节，不是终端用户打开使用的产品；对应用层的成本与交付影响目前没有材料支持，属于推断。
inspiration: ''
summary_en: 'This is a model-method research release: it recasts the reverse diffusion process as normalizing-flow
  steps with exact likelihood training, aiming to keep the likelihood framework while sampling in few
  steps. It targets research and engineering of generative model training and inference, not an end-user
  product; any effect on application-layer cost or delivery is not supported by the material and remains
  an inference.'
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
url: https://machinelearning.apple.com/research/normalizing-trajectory-models
canonical_url: https://machinelearning.apple.com/research/normalizing-trajectory-models
summary: Diffusion-based models decompose sampling into many small Gaussian denoising steps, an assumption
  that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods
  address this through distillation, consistency training, or adversarial objectives, but sacrifice the
  likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models
  each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally,
  NTM combines shallow invertible blocks within each step with a deep parallel…
first_seen: '2026-10-08T00:00:00Z'
last_seen: '2026-10-09T02:10:46Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://machinelearning.apple.com/research/normalizing-trajectory-models
  seen_at: '2026-10-09T02:10:46Z'
  metrics: {}
  kind: news
---

# Normalizing Trajectory Models

Diffusion-based models decompose sampling into many small Gaussian denoising steps, an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel…

## 笔记


