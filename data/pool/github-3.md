---
slug: github-3
name: CoDock
builder: treexie
category: AI + 开发
summary_zh: CoDock 是一个本地桌面工作台，面向同时使用多个 Coding Agent（如 Claude Code、Codex、Gemini CLI 等）的开发者。它把分散在多个终端窗口的
  Agent 会话聚合到一个统一界面，支持多 Tab 并行运行、会话管理和多行 Prompt 输入。开发者无需在多个终端间切换，即可集中管理不同项目的 AI 编码任务。
inspiration: 趋势：开发者工作流正从单一 AI 工具转向多 Agent 并行协作，催生对统一管理界面的需求。切入：可从会话历史搜索、任务状态追踪、跨 Agent 结果对比等环节切入，提供更细粒度的管理能力，而非仅做终端聚合。
summary_en: CoDock is a local desktop workbench for developers who use multiple coding agents (e.g., Claude
  Code, Codex, Gemini CLI). It aggregates agent sessions scattered across terminal windows into a unified
  interface, supporting multi-tab parallel running, session management, and multi-line prompt input. Developers
  can manage AI coding tasks for different projects without switching between terminals.
inspiration_en: 'Trend: Developer workflows are shifting from single AI tools to multi-agent parallel
  collaboration, creating demand for unified management interfaces. Entry: Could focus on session history
  search, task status tracking, cross-agent result comparison, offering finer-grained management rather
  than just terminal aggregation.'
priority_review: false
project_type: new_application
industries:
- 软件开发
industries_en:
- Software Development
jobs:
- 开发者
- 软件工程师
jobs_en:
- Developer
- Software Engineer
regions: []
regions_en: []
open_source: false
url: https://github.com/vicanso/zedis
canonical_url: https://github.com/vicanso/zedis
summary: "之前用 GPUI （ Zed 编辑器那套 GPU 加速 UI 框架）写过一个 Redis 客户端 [Zedis]( https://github.com/vicanso/zedis)。那时候刚接触\
  \ [gpui-component]( https://github.com/longbridge/gpui-component)，生态资料少，基本是大部分代码手写、AI 打辅助的模式——AI 负责查资料、补样板代码，主体逻辑还是自己一行行敲。\r\
  \n\r\n这次做新项目 [zstats.app]( https://github.com/vicanso/zstats.app)，两个变化叠在一起，开发体验完全不一样了：\r\n\r\n**一是 gpui-component\
  \ 成熟了很多。** 各种常用组件都是开箱即用，不用再自己从头设计和实现 UI 细节，官方提供了完整的 skill 以及各种示例更方便使用。\r\n\r\n**二是我把人和 AI 的分工整个反过来了。**\
  \ 开工之前先做了两件准备：让 AI 学习了一遍 gpui-component ；再自己定义了一套编码规则，约束它的写法和边界。之后我只做架构设计和编程规划——写清楚模块划分、数据流、每个功能的设计文档，代码由\
  \ AI 主写，我负责 review 和关键位置的修正。有了 Zedis 积累的 GPUI 经验，这个模式才跑得通：你得知道什么是对的，才能判断 AI 写得对不对。规划写得越细、规则定得越清楚，返工越少。人的角色从「写代码」变成「定规格\
  \ + 把关」。\r\n\r\n产品本身是个 macOS 菜单栏系统监控，核心思路是「每个程序可以有自己的告警线」——浏览器允许吃 200% CPU ，但某个后台守护进程超 30% 就该吱声。另外有进程树聚合（浏览器\
  \ 37 个 helper 合并算账）、慢性占用检测（长期 25% 但从不越线的进程也会被点名）、基于 Spotlight 索引的大文件秒查和可再生缓存清理。清理只走废纸篓、退出进程只发 ⌘Q 级别的请求，不搞\
  \ `rm -rf` 和 SIGKILL 。\r\n\r\nRust + GPUI 原生实现，Apache-2.0 开源，签名公证过的通用二进制。\r\n\r\n![]( https://i.imgur.com/7SvNgDl.png)"
first_seen: '2026-08-30T22:46:08Z'
last_seen: '2026-09-06T02:59:18Z'
status: queued
sources:
- v2ex
- marketfeeds
sightings:
- source: v2ex
  url: https://github.com/vicanso/zedis
  seen_at: '2026-08-31T00:37:15Z'
  metrics:
    comments: 1
  kind: product
- source: marketfeeds
  url: https://www.qbitai.com/2026/09/482469.html
  seen_at: '2026-09-01T14:56:29Z'
  metrics: {}
  kind: news
- source: v2ex
  url: https://github.com/gesta-run/subpool
  seen_at: '2026-09-03T00:16:04Z'
  metrics:
    comments: 10
  kind: product
- source: v2ex
  url: https://github.com/bybit-exchange/svg-diagram
  seen_at: '2026-09-04T00:06:33Z'
  metrics:
    comments: 5
  kind: product
- source: v2ex
  url: https://github.com/othorizon/easy-agent-team
  seen_at: '2026-09-04T00:06:33Z'
  metrics:
    comments: 6
  kind: product
- source: v2ex
  url: https://github.com/fusion-foo/zipo-frontend
  seen_at: '2026-09-05T00:06:28Z'
  metrics:
    comments: 0
  kind: product
- source: v2ex
  url: https://github.com/juejijianghuaa/CoDock-Release/releases/latest
  seen_at: '2026-09-06T02:59:18Z'
  metrics:
    comments: 2
  kind: product
---

# CoDock

之前用 GPUI （ Zed 编辑器那套 GPU 加速 UI 框架）写过一个 Redis 客户端 [Zedis]( https://github.com/vicanso/zedis)。那时候刚接触 [gpui-component]( https://github.com/longbridge/gpui-component)，生态资料少，基本是大部分代码手写、AI 打辅助的模式——AI 负责查资料、补样板代码，主体逻辑还是自己一行行敲。

这次做新项目 [zstats.app]( https://github.com/vicanso/zstats.app)，两个变化叠在一起，开发体验完全不一样了：

**一是 gpui-component 成熟了很多。** 各种常用组件都是开箱即用，不用再自己从头设计和实现 UI 细节，官方提供了完整的 skill 以及各种示例更方便使用。

**二是我把人和 AI 的分工整个反过来了。** 开工之前先做了两件准备：让 AI 学习了一遍 gpui-component ；再自己定义了一套编码规则，约束它的写法和边界。之后我只做架构设计和编程规划——写清楚模块划分、数据流、每个功能的设计文档，代码由 AI 主写，我负责 review 和关键位置的修正。有了 Zedis 积累的 GPUI 经验，这个模式才跑得通：你得知道什么是对的，才能判断 AI 写得对不对。规划写得越细、规则定得越清楚，返工越少。人的角色从「写代码」变成「定规格 + 把关」。

产品本身是个 macOS 菜单栏系统监控，核心思路是「每个程序可以有自己的告警线」——浏览器允许吃 200% CPU ，但某个后台守护进程超 30% 就该吱声。另外有进程树聚合（浏览器 37 个 helper 合并算账）、慢性占用检测（长期 25% 但从不越线的进程也会被点名）、基于 Spotlight 索引的大文件秒查和可再生缓存清理。清理只走废纸篓、退出进程只发 ⌘Q 级别的请求，不搞 `rm -rf` 和 SIGKILL 。

Rust + GPUI 原生实现，Apache-2.0 开源，签名公证过的通用二进制。

![]( https://i.imgur.com/7SvNgDl.png)

## 笔记


