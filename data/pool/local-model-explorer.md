---
slug: local-model-explorer
name: Local Model Explorer
builder: LocalLLaMA
category: 基础层
summary_zh: 个人开发者或小团队在本地跑开源大模型前，需要先判断某个 GGUF 量化版本能否装进自己的 GPU、Mac 或 CPU 显存与内存。该工具接收硬件条件与量化规格，给出可运行的量化档位匹配结果，用户据此决定下载哪个版本；具体匹配口径与是否含实测数据仍待核验。
inspiration: 本地推理的瓶颈正从“有没有模型”转向“选哪个量化档位跑得动”，选型试错成了新的手工环节。切入可放在把硬件清单、量化规格与实测吞吐绑成一份可核验的选型结论，面向自建推理的小团队或做本地部署交付的服务商，按部署方案而非按席位收费。
summary_en: Before running an open-source model locally, an individual developer or small team must judge
  whether a given GGUF quant fits their GPU, Mac or CPU memory. The tool takes hardware constraints and
  quant specs and returns which quant levels are runnable, so the user knows which file to download; the
  matching criteria and whether measured throughput is included still need verification.
inspiration_en: The bottleneck in local inference is shifting from model availability to picking a quant
  that actually runs, making selection trial-and-error a new manual step. An entry point is to bind hardware
  inventory, quant specs and measured throughput into one verifiable selection result, sold to small self-hosting
  teams or local-deployment service providers as a deployment deliverable rather than per seat.
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs:
- 本地大模型部署与选型
- 个人开发者与小型团队的推理环境配置
jobs_en:
- Local LLM deployment and model selection
- Inference environment setup for individual developers and small teams
regions: []
regions_en: []
open_source: true
url: https://huggingface.co/spaces/LocalLLaMA/local-model-explorer
canonical_url: https://huggingface.co/spaces/LocalLLaMA/local-model-explorer
summary: See which GGUF quants fit your GPU, Mac or CPU
first_seen: '2026-09-17T02:45:37Z'
last_seen: '2026-09-18T00:20:09Z'
status: watching
sources:
- huggingface
sightings:
- source: huggingface
  url: https://huggingface.co/spaces/LocalLLaMA/local-model-explorer
  seen_at: '2026-09-18T00:20:09Z'
  metrics:
    likes: 8
  kind: product
---

# Local Model Explorer

See which GGUF quants fit your GPU, Mac or CPU

## 笔记


