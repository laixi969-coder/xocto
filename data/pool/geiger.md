---
slug: geiger
name: Geiger
builder: atomburst
category: AI + 开发
summary_zh: 开发者和安全工程师在本地或开发机上装过多个 AI agent、MCP server 和插件后，往往说不清机器上到底有哪些组件、各自能碰到什么。Geiger 用一条只读命令扫描并列出这些
  agent、MCP server、插件与 AI 扩展，输出一份清单供人核对；它只做清点，不负责拦截或修复，具体覆盖范围与权限判定细节仍待核验。
inspiration: 趋势是 AI agent 与 MCP 插件正在像依赖包一样散落到每台开发机上，但清点与权限可见性还停留在手工翻目录。切入可以从“先看清再治理”这一环做起：面向把 agent 装进生产环境的团队，把清点结果接进已有的资产台账或合规检查流程，而不是再做一个通用安全扫描器。
summary_en: After installing several AI agents, MCP servers and plugins on a local or developer machine,
  developers and security engineers often cannot say which components are present or what each can reach.
  Geiger runs a single read-only command that scans and lists those agents, MCP servers, plugins and AI
  extensions, producing an inventory for human review; it only inventories and does not block or remediate,
  and its exact coverage and permission-judgement details remain to be verified.
inspiration_en: 'The trend is that AI agents and MCP plugins are spreading across every developer machine
  like dependencies, while inventory and permission visibility are still done by hand. The opening is
  to start from the ''see it before governing it'' step: for teams putting agents into production environments,
  feed the inventory into existing asset registers or compliance checks rather than building another general-purpose
  security scanner.'
priority_review: false
project_type: open_source
industries:
- 软件与信息技术服务
- 信息安全
industries_en:
- Software and IT services
- Information security
jobs:
- 开发者与安全工程师在本地或开发机上排查已安装的 AI agent、MCP server 与插件，需要先弄清有哪些组件、各自能访问什么，再决定是否保留或收紧权限
jobs_en:
- Developers and security engineers auditing a local or developer machine for installed AI agents, MCP
  servers and plugins, needing to know which components exist and what they can reach before deciding
  what to keep or restrict
regions:
- 全球
regions_en:
- Global
open_source: true
url: https://github.com/Atomburstofficial/geiger
canonical_url: https://github.com/Atomburstofficial/geiger
summary: See every AI agent on your machine and what it can touch
first_seen: '2026-09-09T14:54:49Z'
last_seen: '2026-09-12T00:18:44Z'
status: watching
sources:
- hackernews
- github
sightings:
- source: hackernews
  url: https://github.com/Atomburstofficial/geiger
  seen_at: '2026-09-11T00:10:31Z'
  metrics:
    points: 47
    comments: 24
  kind: product
- source: github
  url: https://atomburst.io/geiger
  seen_at: '2026-09-12T00:18:44Z'
  metrics:
    stars: 110
    forks: 2
    open_issues: 0
  kind: product
---

# Geiger

See every AI agent on your machine and what it can touch

## 笔记


