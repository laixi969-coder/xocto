---
slug: ollama-ollama-v0406
name: Ollama
builder: ollama
category: 基础层
summary_zh: 开发者在本地或自有服务器上运行开源模型时，用 Ollama 拉取模型、管理运行进程并通过命令行提问，最终得到可调用的本地模型服务；本次版本只涉及进程修复、新量化格式与云服务上线，具体使用流程仍以官方文档为准。
inspiration: 趋势：本地模型运行工具在补稳定性与量化格式，同时向托管云延伸，说明自托管推理正从实验走向日常部署。切入：不要重做运行时，可在企业内网模型分发、权限与审计这一层做交付。
summary_en: Developers running open models locally or on their own servers use Ollama to pull models,
  manage runner processes and query via command line, ending with a callable local model service; this
  release only covers process fixes, a new quantization format and a cloud launch, with workflow details
  per official docs.
inspiration_en: 'Trend: local model runtimes are shoring up stability and quantization formats while extending
  into hosted cloud, showing self-hosted inference moving from experiment to routine deployment. Entry:
  do not rebuild the runtime; deliver on intranet model distribution, permissions and audit for enterprises.'
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs:
- 开发者在本地或自有服务器上部署和运行开源大模型时，用 Ollama 拉取模型、管理运行进程并通过命令行提问，得到可调用的本地模型服务
jobs_en:
- Developers deploying and running open models locally or on their own servers use Ollama to pull models,
  manage runner processes and query via command line, obtaining a callable local model service
regions: []
regions_en: []
open_source: true
url: https://github.com/ollama/ollama/releases/tag/v0.40.6
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.40.6
summary: "## What's Changed\r\n* win: prevent orphaned runners by @dhiltgen in https://github.com/ollama/ollama/pull/18500\r\
  \n* gguf: add the q2_0 tensor and file types by @jmorganca in https://github.com/ollama/ollama/pull/18967\r\
  \n* Launch clef in Ollama's cloud by @jberg5 in https://github.com/ollama/ollama/pull/19036\r\n* use\
  \ identifiers for --ask mode question keys by @jberg5 in https://github.com/ollama/ollama/pull/19041\r\
  \n\r\n\r\n**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.5...v0.40.6-rc0"
first_seen: '2026-10-18T00:03:49Z'
last_seen: '2026-10-19T00:13:37Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.40.6
  seen_at: '2026-10-19T00:13:37Z'
  metrics:
    reactions: 21
  kind: news
---

# Ollama

## What's Changed
* win: prevent orphaned runners by @dhiltgen in https://github.com/ollama/ollama/pull/18500
* gguf: add the q2_0 tensor and file types by @jmorganca in https://github.com/ollama/ollama/pull/18967
* Launch clef in Ollama's cloud by @jberg5 in https://github.com/ollama/ollama/pull/19036
* use identifiers for --ask mode question keys by @jberg5 in https://github.com/ollama/ollama/pull/19041


**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.5...v0.40.6-rc0

## 笔记


