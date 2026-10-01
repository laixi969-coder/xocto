---
slug: token-compression-cli-to-save-codex-astra-costs
name: Token compression CLI to save Codex/Astra costs
builder: yolandac
category: 基础层
summary_zh: 开发者在调用 Codex 等编码模型时，把提示词与上下文交给这个命令行工具，由它压缩 token 后再发给模型，目标是降低按量计费的账单；用户拿到的是压缩后的请求与更低的调用成本，但压缩是否损失回答质量、具体流程与交付仍待核验。
inspiration: 趋势是编码模型的按量成本已成为独立于模型能力的一条工程问题，围绕上下文压缩、缓存与路由的成本层正在被单独拆出来做。切入可以从重度使用编码模型的团队入手，按节省的账单比例收费，而不是按席位卖工具；但压缩质量与可核对的效果数据尚未公开，先观察其是否给出可复现的评测。
summary_en: When calling coding models such as Codex, developers pass prompts and context through this
  CLI, which compresses tokens before sending them to the model in order to lower metered billing; the
  user gets a compressed request and a lower call cost, while whether compression degrades answer quality,
  the exact workflow and the deliverable still need verification.
inspiration_en: 'The trend is that metered cost of coding models has become an engineering problem separate
  from model capability, and a cost layer around context compression, caching and routing is being carved
  out on its own. Entry point: heavy coding-model teams, charged as a share of the bill saved rather than
  per seat; but compression quality and verifiable results are not public, so watch for a reproducible
  evaluation first.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- AI 应用开发者的模型调用成本控制
jobs_en:
- Model API cost control for AI application developers
regions: []
regions_en: []
open_source: true
url: https://news.ycombinator.com/item?id=49911910
canonical_url: https://news.ycombinator.com/item?id=49911910
summary: Hey HN! Yolanda and Spencer here - wanted to share a token compression tool that we’ve built
  for ourselves to save 30% costs on codex! After maxing out sub and burning $700&#x2F;day per person
  on api, we fine tuned a com…
first_seen: '2026-09-30T17:30:54Z'
last_seen: '2026-10-01T01:18:38Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://news.ycombinator.com/item?id=49911910
  seen_at: '2026-10-01T01:18:38Z'
  metrics:
    points: 8
    comments: 4
  kind: product
---

# Token compression CLI to save Codex/Astra costs

Hey HN! Yolanda and Spencer here - wanted to share a token compression tool that we’ve built for ourselves to save 30% costs on codex! After maxing out sub and burning $700&#x2F;day per person on api, we fine tuned a com…

## 笔记


