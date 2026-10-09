---
slug: ollama-ollama-v0401
name: Ollama
builder: ollama
category: 基础层
summary_zh: 开发者在本地或内网部署大模型时打开 Ollama，它接收模型文件与运行请求，完成下载、加载与推理服务，并输出可调用的本地接口；本次版本还代理云端用量与余额查询，并简化命令行首次配置。具体交付与计费方式仍待核验。
inspiration: Local inference tooling is absorbing cloud usage and balance into its own interface, suggesting
  metering and quota management for hybrid local-cloud deployment is becoming a distinct layer; the opening
  is resource accounting for private-deployment teams.
summary_en: Developers running models locally or on-premise open Ollama, which takes model files and run
  requests, handles download, loading and inference serving, and exposes a callable local endpoint; this
  release also proxies cloud usage and balance queries and simplifies first-run CLI setup. Delivery and
  billing details remain unverified.
inspiration_en: Validate sustained use in a real workflow before deciding whether the opportunity merits
  investment.
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs:
- 本地模型部署与运维
- 开发者工具集成
jobs_en:
- Local model deployment and operations
- Developer tooling integration
regions: []
regions_en: []
open_source: true
url: https://github.com/ollama/ollama/releases/tag/v0.40.1
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.40.1
summary: "## What's Changed\r\n* server: proxy cloud usage and balance APIs by @drifkin in https://github.com/ollama/ollama/pull/18829\r\
  \n* llama: fix clef head reads past 2GiB on windows by @Gigrise in https://github.com/ollama/ollama/pull/18777\r\
  \n* cmd: remove account step from CLI onboarding by @hoyyeva in https://github.com/ollama/ollama/pull/18826\r\
  \n* manifest: avoid symlinks on Windows by @dhiltgen in https://github.com/ollama/ollama/pull/18852\r\
  \n* docs: fix 6 dead links in README community integrations list by @aniketkrs in https://github.com/ollama/ollama/pull/18814\r\
  \n* docs: fix broken download links in app README by @chenlichao in https://github.com/ollama/ollama/pull/18233\r\
  \n* mlx: drop carried metal residency patch now that it is upstream by @dhiltgen in https://github.com/ollama/ollama/pull/18854\r\
  \n\r\n## New Contributors\r\n* @Gigrise made their first contribution in https://github.com/ollama/ollama/pull/18777\r\
  \n* @aniketkrs made their first contribution in https://github.com/ollama/ollama/pull/18814\r\n* @chenlichao\
  \ made their first contribution in https://github.com/ollama/ollama/pull/18233\r\n\r\n**Full Changelog**:\
  \ https://github.com/ollama/ollama/compare/v0.40.0...v0.40.1-rc0"
first_seen: '2026-10-07T23:22:59Z'
last_seen: '2026-10-09T02:10:18Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.40.1
  seen_at: '2026-10-09T02:10:18Z'
  metrics:
    reactions: 10
  kind: news
---

# Ollama

## What's Changed
* server: proxy cloud usage and balance APIs by @drifkin in https://github.com/ollama/ollama/pull/18829
* llama: fix clef head reads past 2GiB on windows by @Gigrise in https://github.com/ollama/ollama/pull/18777
* cmd: remove account step from CLI onboarding by @hoyyeva in https://github.com/ollama/ollama/pull/18826
* manifest: avoid symlinks on Windows by @dhiltgen in https://github.com/ollama/ollama/pull/18852
* docs: fix 6 dead links in README community integrations list by @aniketkrs in https://github.com/ollama/ollama/pull/18814
* docs: fix broken download links in app README by @chenlichao in https://github.com/ollama/ollama/pull/18233
* mlx: drop carried metal residency patch now that it is upstream by @dhiltgen in https://github.com/ollama/ollama/pull/18854

## New Contributors
* @Gigrise made their first contribution in https://github.com/ollama/ollama/pull/18777
* @aniketkrs made their first contribution in https://github.com/ollama/ollama/pull/18814
* @chenlichao made their first contribution in https://github.com/ollama/ollama/pull/18233

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.0...v0.40.1-rc0

## 笔记


