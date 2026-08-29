---
slug: ollama-ollama-v0332
name: Ollama
builder: ollama
category: 基础层
summary_zh: Ollama是本地运行大语言模型的开源工具，开发者下载后可在个人电脑上启动和管理模型，通过命令行或API调用。本次更新修复了macOS应用重复启动和深色模式问题，并优化了Claude
  Desktop代理的请求处理。具体工作流：开发者安装Ollama后，拉取模型镜像，在本地启动服务，应用通过API发送提示词并接收生成结果。交付是本地可用的模型推理服务，无需联网。
inspiration: 趋势是AI模型部署从云端走向本地，开发者工具链日益成熟。切入点是面向开发者的本地模型管理工具，可借鉴其开源社区驱动和跨平台支持策略，但需注意与云服务的差异化。
summary_en: Ollama is an open-source tool for running large language models locally. Developers download
  it, pull model images, and start a local service, then applications send prompts via API and receive
  generated results. This update fixes macOS app duplicate launch and dark mode, and improves Claude Desktop
  proxy request handling. The deliverable is a local model inference service without internet dependency.
inspiration_en: The trend is AI model deployment moving from cloud to local, with developer toolchains
  maturing. The entry point is local model management tools for developers, leveraging open-source community
  and cross-platform support, but differentiation from cloud services is key.
priority_review: false
project_type: open_source
industries:
- 软件开发者
industries_en:
- Software Developers
jobs:
- 开发者
jobs_en:
- Developers
regions:
- 全球
regions_en:
- Global
open_source: true
url: https://github.com/ollama/ollama/releases/tag/v0.33.2
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.33.2
summary: "## What's Changed\r\n\r\n* Ollama's app now follows the system appearance again, restoring dark\
  \ mode support\r\n* Fixed the macOS app to properly hand off to an already-running instance instead\
  \ of starting a second one\r\n* The Claude Desktop proxy no longer interrupts in-flight requests when\
  \ the model catalog updates\r\n\r\n**Full Changelog**: https://github.com/ollama/ollama/compare/v0.33.1...v0.33.2"
first_seen: '2026-08-27T20:31:47Z'
last_seen: '2026-08-29T15:06:08Z'
status: queued
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.33.2
  seen_at: '2026-08-29T15:06:08Z'
  metrics:
    reactions: 45
  kind: news
---

# Ollama

## What's Changed

* Ollama's app now follows the system appearance again, restoring dark mode support
* Fixed the macOS app to properly hand off to an already-running instance instead of starting a second one
* The Claude Desktop proxy no longer interrupts in-flight requests when the model catalog updates

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.33.1...v0.33.2

## 笔记


