---
slug: github-3
name: Github
builder: treexie
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
inspiration_en: ''
priority_review: false
project_type: new_application
industries: []
industries_en: []
jobs: []
jobs_en: []
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
last_seen: '2026-09-04T00:06:33Z'
status: pending_filter
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
---

# Github

之前用 GPUI （ Zed 编辑器那套 GPU 加速 UI 框架）写过一个 Redis 客户端 [Zedis]( https://github.com/vicanso/zedis)。那时候刚接触 [gpui-component]( https://github.com/longbridge/gpui-component)，生态资料少，基本是大部分代码手写、AI 打辅助的模式——AI 负责查资料、补样板代码，主体逻辑还是自己一行行敲。

这次做新项目 [zstats.app]( https://github.com/vicanso/zstats.app)，两个变化叠在一起，开发体验完全不一样了：

**一是 gpui-component 成熟了很多。** 各种常用组件都是开箱即用，不用再自己从头设计和实现 UI 细节，官方提供了完整的 skill 以及各种示例更方便使用。

**二是我把人和 AI 的分工整个反过来了。** 开工之前先做了两件准备：让 AI 学习了一遍 gpui-component ；再自己定义了一套编码规则，约束它的写法和边界。之后我只做架构设计和编程规划——写清楚模块划分、数据流、每个功能的设计文档，代码由 AI 主写，我负责 review 和关键位置的修正。有了 Zedis 积累的 GPUI 经验，这个模式才跑得通：你得知道什么是对的，才能判断 AI 写得对不对。规划写得越细、规则定得越清楚，返工越少。人的角色从「写代码」变成「定规格 + 把关」。

产品本身是个 macOS 菜单栏系统监控，核心思路是「每个程序可以有自己的告警线」——浏览器允许吃 200% CPU ，但某个后台守护进程超 30% 就该吱声。另外有进程树聚合（浏览器 37 个 helper 合并算账）、慢性占用检测（长期 25% 但从不越线的进程也会被点名）、基于 Spotlight 索引的大文件秒查和可再生缓存清理。清理只走废纸篓、退出进程只发 ⌘Q 级别的请求，不搞 `rm -rf` 和 SIGKILL 。

Rust + GPUI 原生实现，Apache-2.0 开源，签名公证过的通用二进制。

![]( https://i.imgur.com/7SvNgDl.png)

## 笔记


