---
slug: ollama-ollama-v0403
name: Ollama
builder: ollama
category: 基础层
summary_zh: 本地运行大模型的开源工具，开发者在自己机器上拉取并运行模型，再通过命令行把 Claude、Codex 等编码代理接到本地模型上。本次 v0.40.3 只是取消了两处连接器与服务档位的警告提示，并暂停了嵌入等请求的后台模型自动升级；具体交付流程仍待核验。
inspiration: 趋势：本地推理工具正在从“跑模型”转向“给编码代理当后端”，把模型调用从云端 API 挪回本机。切入：面向对数据出域敏感、又想让代理写代码的团队，做本地模型与代理之间的合规与成本对账层；但该层已被开源项目占据，窗口偏窄，需从具体行业的数据合规要求切入。
summary_en: 'An open-source tool for running large models locally: developers pull and run models on their
  own machines and wire coding agents such as Claude and Codex to a local model via the command line.
  Release v0.40.3 only removes two connector and service-tier warnings and pauses background model upgrades
  for embedding and other requests; the concrete delivery flow still needs verification.'
inspiration_en: 'Trend: local inference tools are shifting from "run a model" to "be the backend for coding
  agents", moving model calls off cloud APIs onto the machine. Entry: for teams that cannot let data leave
  their network but still want agents writing code, build a compliance and cost-accounting layer between
  local models and agents; that layer is already held by open-source projects, so the window is narrow
  and entry must come from a specific industry''s data rules.'
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/ollama/ollama/releases/tag/v0.40.3
canonical_url: https://github.com/ollama/ollama/releases/tag/v0.40.3
summary: "## What's Changed\r\n* `ollama launch claude` no longer shows a warning about Claude connectors\
  \ by @hoyyeva in https://github.com/ollama/ollama/pull/18878\r\n* `ollama launch codex` no longer warns\
  \ about service tiers by @hoyyeva in https://github.com/ollama/ollama/pull/18879\r\n* Paused background\
  \ model upgrade for embedding and other request performance, by @jmorganca in https://github.com/ollama/ollama/pull/18908\r\
  \n\r\n\r\n**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.2...v0.40.3"
first_seen: '2026-10-12T01:20:35Z'
last_seen: '2026-10-13T03:03:58Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/ollama/ollama/releases/tag/v0.40.3
  seen_at: '2026-10-13T03:03:58Z'
  metrics:
    reactions: 24
  kind: news
---

# Ollama

## What's Changed
* `ollama launch claude` no longer shows a warning about Claude connectors by @hoyyeva in https://github.com/ollama/ollama/pull/18878
* `ollama launch codex` no longer warns about service tiers by @hoyyeva in https://github.com/ollama/ollama/pull/18879
* Paused background model upgrade for embedding and other request performance, by @jmorganca in https://github.com/ollama/ollama/pull/18908


**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.2...v0.40.3

## 笔记


