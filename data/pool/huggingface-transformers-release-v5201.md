---
slug: huggingface-transformers-release-v5201
name: Transformers
builder: huggingface
category: ''
summary_zh: 这是开源模型加载库的版本更新，不是独立产品；它把 Reflection AI 的 Beam 模型纳入支持范围，并修复旧版 torch 的加载问题。对应用方而言，可自托管的前沿编码模型多了一个接入选项，但成本与采用影响尚无材料支持。
inspiration: ''
summary_en: This is a version update to an open-source model-loading library, not a standalone product;
  it adds support for Reflection AI's Beam model and fixes loading on older torch versions. For application
  builders it adds one more self-hostable frontier coding model option, but the material does not support
  claims about cost or adoption impact.
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
url: https://github.com/huggingface/transformers/releases/tag/v5.20.1
canonical_url: https://github.com/huggingface/transformers/releases/tag/v5.20.1
summary: "# Release v5.20.1\r\n\r\nSpecial surprise including the new model Beam from Reflection AI :partying_face:\
  \ \r\n\r\n<img width=\"2912\" height=\"1440\" alt=\"Gemini_Generated_Image_ox4hjlox4hjlox4h\" src=\"\
  https://github.com/user-attachments/assets/bfc7ff16-4340-490c-925c-b1512e4ceb32\" />\r\n\r\nBeam is\
  \ a token-efficient, frontier-scale model focused on coding and agentic use cases. It is built for teams\
  \ that want to run a powerful model on their own hardware, infrastructure, or cloud, and customize it\
  \ to their specific needs.\r\n\r\n**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/beam)\r\
  \n* Fix small bug in auto mappings (#49664) by @yonigozlan in [#49664](https://github.com/huggingface/transformers/pull/49664)\r\
  \n\r\n\r\n## Some real patch fixes\r\n\r\nWe broke loading models on older torch versions :cry: should\
  \ be fixed now. But here is the full list of fixes\r\n\r\n- Fix HunYuan-VL image assignment during batched\
  \ generation (#49557) by @Arnav66692\r\n- Fix DeepGEMM Mega MoE under expert parallelism(#49428) by\
  \ @IlyasMoutawwakil\r\n- Fix from_pretrained on torch 2.7: require torch>=2.8 for distributed checkpointing\
  \ (#49652) by @naveecode \r\n- Make DtensorShardOperation work on torch 2.6 and 2.7 (#49657) by @hazelxue\r\
  \n\r\n**Full Changelog**: https://github.com/huggingface/transformers/compare/v5.20.0...v5.20.1"
first_seen: '2026-10-17T00:30:30Z'
last_seen: '2026-10-19T00:13:37Z'
status: market_context
sources:
- github
sightings:
- source: github
  url: https://github.com/huggingface/transformers/releases/tag/v5.20.1
  seen_at: '2026-10-19T00:13:37Z'
  metrics:
    reactions: 9
  kind: news
---

# Transformers

# Release v5.20.1

Special surprise including the new model Beam from Reflection AI :partying_face: 

<img width="2912" height="1440" alt="Gemini_Generated_Image_ox4hjlox4hjlox4h" src="https://github.com/user-attachments/assets/bfc7ff16-4340-490c-925c-b1512e4ceb32" />

Beam is a token-efficient, frontier-scale model focused on coding and agentic use cases. It is built for teams that want to run a powerful model on their own hardware, infrastructure, or cloud, and customize it to their specific needs.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/beam)
* Fix small bug in auto mappings (#49664) by @yonigozlan in [#49664](https://github.com/huggingface/transformers/pull/49664)


## Some real patch fixes

We broke loading models on older torch versions :cry: should be fixed now. But here is the full list of fixes

- Fix HunYuan-VL image assignment during batched generation (#49557) by @Arnav66692
- Fix DeepGEMM Mega MoE under expert parallelism(#49428) by @IlyasMoutawwakil
- Fix from_pretrained on torch 2.7: require torch>=2.8 for distributed checkpointing (#49652) by @naveecode 
- Make DtensorShardOperation work on torch 2.6 and 2.7 (#49657) by @hazelxue

**Full Changelog**: https://github.com/huggingface/transformers/compare/v5.20.0...v5.20.1

## 笔记


