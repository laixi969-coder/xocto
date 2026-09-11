---
slug: dsh-filesnap
name: dsh-filesnap
builder: extracurricular-ai
category: AI + 开发
summary_zh: 使用 DeepSeek Harness 的开发者在一轮对话改坏文件后，用这个插件把对话记录和它改动过的文件一起回退到某一轮之前，不需要 git 仓库，还能撤销这次回退；由 Rust
  实现，公开材料称其速度快、占用磁盘低，具体恢复边界仍待核验。
inspiration: 趋势是编码代理的配套工具开始围绕“可回退、可审计”做文章，而不是继续堆生成能力。切入可考虑把这类回退与变更记录做成团队级审计能力，卖给已经在生产环境跑编码代理的工程团队，按项目或按席位收费，前提是能证明恢复结果可靠。
summary_en: A developer using DeepSeek Harness who breaks files during a session uses this plugin to roll
  the conversation and the files it changed back to an earlier turn, without a git repository, and can
  undo that rollback. It is written in Rust and the public material claims speed and low disk use; the
  exact recovery boundary remains unverified.
inspiration_en: The trend is that tooling around coding agents is starting to focus on rollback and auditability
  rather than piling on generation. A way in is to turn this kind of rollback and change record into team-level
  audit capability sold to engineering teams already running coding agents in production, priced per project
  or per seat, provided recovery reliability can be shown.
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- software development
jobs:
- 软件开发者
jobs_en:
- software developer
regions: []
regions_en: []
open_source: true
url: http://extracurricular.ai/dsh-filesnap/
canonical_url: https://extracurricular.ai/dsh-filesnap
summary: DSH Rewind & Redo — by FileSnap. 把对话和它改过的文件一起恢复到某一轮之前（受claude code rewind启发并改进）,不需要 git 仓库,并且可以撤销恢复（redo受opencode启发并改进），由rust驱动是市面上最快最可靠的dsh
  rewind插件. A blazing-fast rewind and redo plugin for DeepSeek Harness, powered by a 🦀 Rust core, tracking
  the conversation and the files it changed, no git required, low disk consumption
first_seen: '2026-08-27T02:28:07Z'
last_seen: '2026-09-11T00:10:34Z'
status: watching
sources:
- github
sightings:
- source: github
  url: http://extracurricular.ai/dsh-filesnap/
  seen_at: '2026-09-11T00:10:34Z'
  metrics:
    stars: 43
    forks: 9
    open_issues: 1
  kind: product
---

# dsh-filesnap

DSH Rewind & Redo — by FileSnap. 把对话和它改过的文件一起恢复到某一轮之前（受claude code rewind启发并改进）,不需要 git 仓库,并且可以撤销恢复（redo受opencode启发并改进），由rust驱动是市面上最快最可靠的dsh rewind插件. A blazing-fast rewind and redo plugin for DeepSeek Harness, powered by a 🦀 Rust core, tracking the conversation and the files it changed, no git required, low disk consumption

## 笔记


