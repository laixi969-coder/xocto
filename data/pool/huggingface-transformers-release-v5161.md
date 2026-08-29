---
slug: huggingface-transformers-release-v5161
name: Hugging Face Transformers
builder: huggingface
category: ''
summary_zh: 公开模型社区 Transformers 是一个开源深度学习模型库，本次更新加入对 GLM-5.3-Flash 的支持，这是一个高效的多模态模型，适合长上下文和编码任务。
inspiration: ''
summary_en: public model community Transformers is an open-source deep learning model library. This update
  adds support for GLM-5.3-Flash, an efficient multimodal model suitable for long-context and coding tasks.
inspiration_en: ''
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/huggingface/transformers/releases/tag/v5.16.1
canonical_url: https://github.com/huggingface/transformers/releases/tag/v5.16.1
summary: "# Release v5.16.1\r\n\r\nThis is a special release as we include GLM! (and a few small fixes)\r\
  \n\r\n# GLM-5.3-Flash\r\n\r\n<img width=\"4239\" height=\"2643\" alt=\"image\" src=\"https://github.com/user-attachments/assets/17bc9c29-758b-44c8-8230-42f945ded209\"\
  \ />\r\n\r\nGLM-5.3-Flash, the first **natively multimodal model** in the GLM-5 series. With 320B total\
  \ parameters and just 18B active parameters, it outperforms GLM-5.2 across benchmarks and real-world\
  \ workloads at one-tenth the price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.\r\
  \n\r\nGLM-5.3-Flash starts from a newly trained base model, with its architecture and training recipe\
  \ redesigned around capability and efficiency. For the first time in the GLM series, we introduce a\
  \ hybrid architecture combining sparse and linear attention, sharply reducing long-context serving costs\
  \ while preserving precise long-context capabilities. The model also adopts Manifold-Constrained Hyper-Connections\
  \ (mHC) to further improve scaling efficiency. Together with our latest **30T-token** multimodal pre-training\
  \ corpus, these changes enable GLM-5.3-Flash to deliver more intelligence with less compute.\r\n\r\n\
  **Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/glm5_next)\r\n\
  * [Glm 5.3 Flash] GLM 5.3 Flash Support (#48342) by @Dovis01 in [#48342](https://github.com/huggingface/transformers/pull/48342)\r\
  \n\r\n\r\n## Small patch fixes\r\n\r\nMainly BC behavior for TP and pinning a hf kernel for security\
  \ reasons :hugs: \r\n\r\n- Restore BC for the tensor-parallel API (#48300) by @ArthurZucker \r\n- Fix\
  \ kernel commit and repo paths for ESMFold2 (#48186) by @Rocketknight1 \r\n\r\n**Full Changelog**: https://github.com/huggingface/transformers/compare/v5.16.0...v5.16.1"
first_seen: '2026-08-26T14:50:01Z'
last_seen: '2026-08-29T03:43:11Z'
status: market_context
sources:
- github
sightings:
- source: github
  url: https://github.com/huggingface/transformers/releases/tag/v5.16.1
  seen_at: '2026-08-29T03:43:11Z'
  metrics:
    reactions: 6
  kind: news
---

# Hugging Face Transformers

# Release v5.16.1

This is a special release as we include GLM! (and a few small fixes)

# GLM-5.3-Flash

<img width="4239" height="2643" alt="image" src="https://github.com/user-attachments/assets/17bc9c29-758b-44c8-8230-42f945ded209" />

GLM-5.3-Flash, the first **natively multimodal model** in the GLM-5 series. With 320B total parameters and just 18B active parameters, it outperforms GLM-5.2 across benchmarks and real-world workloads at one-tenth the price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.

GLM-5.3-Flash starts from a newly trained base model, with its architecture and training recipe redesigned around capability and efficiency. For the first time in the GLM series, we introduce a hybrid architecture combining sparse and linear attention, sharply reducing long-context serving costs while preserving precise long-context capabilities. The model also adopts Manifold-Constrained Hyper-Connections (mHC) to further improve scaling efficiency. Together with our latest **30T-token** multimodal pre-training corpus, these changes enable GLM-5.3-Flash to deliver more intelligence with less compute.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/glm5_next)
* [Glm 5.3 Flash] GLM 5.3 Flash Support (#48342) by @Dovis01 in [#48342](https://github.com/huggingface/transformers/pull/48342)


## Small patch fixes

Mainly BC behavior for TP and pinning a hf kernel for security reasons :hugs: 

- Restore BC for the tensor-parallel API (#48300) by @ArthurZucker 
- Fix kernel commit and repo paths for ESMFold2 (#48186) by @Rocketknight1 

**Full Changelog**: https://github.com/huggingface/transformers/compare/v5.16.0...v5.16.1

## 笔记


