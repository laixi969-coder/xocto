---
slug: titan-engine
name: titan-engine
builder: deathg0d
category: 基础层
summary_zh: 面向需要在网页里嵌入表格的前端工程师：把用 Rust/WASM 写的表格计算引擎放进浏览器，由它在本地完成大表的计算与渲染，用户拿到的是可嵌入的表格组件而非在线表格服务。具体支持的数据规模、公式覆盖范围与交付形态仍待核验。
inspiration: 趋势是浏览器端算力被重新拿来做重计算，表格这类高频、重交互的旧软件第一次有机会脱离桌面端和云端往返。切入可以放在把表格能力嵌进已有行业软件（财务对账、保险保单台账、地产台账）的组件层，卖的是嵌入与性能，而不是再做一个在线表格；是否有人愿意为此付费尚无公开证据。
summary_en: 'For frontend engineers who need to embed a spreadsheet in a web page: a Rust/WASM calculation
  engine runs inside the browser and handles computation and rendering of large tables locally, delivered
  as an embeddable component rather than an online spreadsheet service. Supported data scale, formula
  coverage and delivery format still need verification.'
inspiration_en: The trend is that browser-side compute is being reused for heavy calculation, giving high-frequency,
  interaction-heavy legacy software like spreadsheets a chance to leave the desktop and the cloud round-trip.
  The entry point is the component layer that embeds spreadsheet capability into existing industry software
  (financial reconciliation, insurance policy ledgers, property ledgers), selling embedding and performance
  rather than another online spreadsheet; there is no public evidence yet that anyone will pay for it.
priority_review: false
project_type: open_source
industries:
- 企业软件
- 金融与保险
- 数据分析服务
industries_en:
- Enterprise Software
- Financial Services
- Data & Analytics
jobs:
- 前端工程师在浏览器内嵌表格组件时，把大体量数据表的计算与渲染放到本地完成
- 数据分析师在网页端打开大表格时，需要在不安装桌面软件的情况下完成排序、筛选与公式重算
jobs_en:
- Frontend engineers embedding spreadsheet components in the browser, running computation and rendering
  of large tables locally
- Data analysts opening large tables in a web page who need sorting, filtering and formula recalculation
  without installing desktop software
regions: []
regions_en: []
open_source: true
url: https://github.com/podraven/titan-engine
canonical_url: https://github.com/podraven/titan-engine
summary: I built a fast spreadsheet engine for the web in Rust/WASM
first_seen: '2026-10-08T21:51:03Z'
last_seen: '2026-10-10T01:45:59Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://github.com/podraven/titan-engine
  seen_at: '2026-10-10T01:45:59Z'
  metrics:
    points: 8
    comments: 2
  kind: product
---

# titan-engine

I built a fast spreadsheet engine for the web in Rust/WASM

## 笔记


