---
slug: pig
name: PiG
builder: MichaelKinsy
category: AI + 开发
summary_zh: 开发者在自建或受限环境里部署编码代理时，原本要处理 Pi 的 TypeScript 代码库；PiG 把上游 Pi 的 TypeScript 实现按行为对齐方式翻译成 Go，上游行为作为契约，用户拿到的是可编译、易分发的
  Go 版本编码代理。具体交付流程与人工确认环节仍待核验。
inspiration: 趋势是编码代理开始出现语言与运行时的分叉实现，能力不再只锁在原始技术栈里。切入可放在需要把代理塞进自有构建链、内网或边缘环境的团队，卖点是可编译分发与行为对齐，而不是又一个代理功能；但这类移植的维护成本与上游同步节奏是主要风险。
summary_en: When developers deploy a coding agent in self-hosted or constrained environments they previously
  had to work with Pi's TypeScript codebase; PiG translates the upstream Pi TypeScript implementation
  into Go as a parity-bound port, treating upstream behavior as the contract, so users get a compilable,
  easily distributed Go coding agent. The concrete delivery flow and human confirmation steps still need
  verification.
inspiration_en: The trend is that coding agents are starting to get forked implementations across languages
  and runtimes, so capability is no longer locked to the original stack. The entry point is teams that
  must fit an agent into their own build chain, intranet or edge environment, sold on compilable distribution
  and behavioral parity rather than yet another agent feature; the main risk is maintenance cost and keeping
  pace with upstream.
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 开发者在自建或受限运行环境中部署编码代理时，需要把原 TypeScript 代理换成可编译、易分发的 Go 版本并保持行为一致
jobs_en:
- Developers deploying a coding agent in self-hosted or constrained runtime environments need a compilable,
  easily distributed Go build of the original TypeScript agent while keeping behavior identical
regions: []
regions_en: []
open_source: true
url: https://pi-in-go.dev
canonical_url: https://pi-in-go.dev
summary: 'PiG (Pi in Go) is a faithful Go port of upstream Pi, the TypeScript codebase behind the Pi coding
  agent. It is a parity-bound translation, not a rewrite: upstream behavior is the contract, and Go is
  the implementation language.'
first_seen: '2026-09-17T15:52:38Z'
last_seen: '2026-09-28T00:46:44Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://pi-in-go.dev
  seen_at: '2026-09-28T00:46:44Z'
  metrics:
    stars: 285
    forks: 15
    open_issues: 7
  kind: product
---

# PiG

PiG (Pi in Go) is a faithful Go port of upstream Pi, the TypeScript codebase behind the Pi coding agent. It is a parity-bound translation, not a rewrite: upstream behavior is the contract, and Go is the implementation language.

## 笔记


