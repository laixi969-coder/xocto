---
slug: deepjit
name: DeepJIT
builder: deepseek-ai
category: 基础层
summary_zh: 面向在非英伟达加速卡上部署推理的工程团队：他们原本要为每种 xPU 手写并维护内核编译流程，DeepJIT 接收内核代码并在运行时完成即时编译，产出可直接调用的编译结果；具体支持的硬件清单与交付形态仍待核验。
inspiration: 趋势是模型厂商把推理栈的编译环节开源出来，让非英伟达加速卡也能跑自家模型。切入可放在国产或自研加速卡的推理部署服务：帮买不起英伟达卡、又不想自己啃编译链的团队把模型跑起来，按部署或调优结果收费。
summary_en: 'For engineering teams deploying inference on non-NVIDIA accelerators: they previously had
  to hand-write and maintain a kernel compilation pipeline per xPU; DeepJIT takes kernel code and performs
  just-in-time compilation at runtime, producing callable compiled output. The supported hardware list
  and delivery form still need verification.'
inspiration_en: 'The trend is model vendors open-sourcing the compilation layer of their inference stack
  so their models can run on non-NVIDIA accelerators. A wedge is inference deployment services for domestic
  or in-house accelerators: helping teams that cannot afford NVIDIA cards and do not want to maintain
  a compiler chain themselves, charged per deployment or tuning outcome.'
priority_review: true
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/deepseek-ai/DeepJIT
canonical_url: https://github.com/deepseek-ai/DeepJIT
summary: A lightweight library for xPU kernel JIT compilation
first_seen: '2026-09-08T03:57:22Z'
last_seen: '2026-09-12T00:18:44Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/deepseek-ai/DeepJIT
  seen_at: '2026-09-12T00:18:44Z'
  metrics:
    stars: 272
    forks: 22
    open_issues: 9
  kind: product
---

# DeepJIT

A lightweight library for xPU kernel JIT compilation

## 笔记


