---
slug: everything-search-skill
name: everything-search-skill
builder: Mayuqi-crypto
category: AI + 开发
summary_zh: 使用 Cursor、Codex 等编程代理的开发者，在代理需要定位本地文件时，通过这个开源技能让代理调用 Voidtools Everything 的索引来检索，而不是逐层遍历目录，最终拿到匹配的文件路径供后续读取。它依赖
  Windows 上的 Everything 索引，公开材料未说明跨平台支持、权限边界与检索结果如何回传给代理，具体集成方式仍待核验。
inspiration: 趋势是编程代理的瓶颈正从“会不会写”转向“能不能快速拿到正确的本地上下文”，索引类工具因此被接进代理。切入不在再做一个通用文件搜索，而在把某类专业本地资料——设计稿、工程图纸、病历影像、合同扫描件——做成代理可直接检索的索引层，卖给已经用代理但受困于检索速度的团队。
summary_en: Developers using coding agents such as Cursor or Codex let the agent query the Voidtools Everything
  index through this open-source skill when it needs to locate local files, instead of walking directories,
  and get back matching file paths for later reading. It depends on the Everything index on Windows; public
  material does not cover cross-platform support, permission boundaries or how results are returned to
  the agent, so the concrete integration still needs verification.
inspiration_en: The trend is that the bottleneck for coding agents is shifting from whether they can write
  code to whether they can quickly pull the right local context, which is why index tools are being wired
  into agents. The opening is not another generic file search but turning a specific class of professional
  local material — design files, engineering drawings, medical images, scanned contracts — into an index
  layer agents can query directly, sold to teams already using agents but blocked by retrieval speed.
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software development
jobs:
- 使用 Cursor、Codex 等编程代理的开发者，在代理需要查找本地代码或文件时，让它通过 Everything 索引检索而不是逐层遍历目录
jobs_en:
- Developers using coding agents such as Cursor or Codex who let the agent retrieve local code or files
  through the Everything index instead of walking directories
regions:
- 全球
regions_en:
- Global
open_source: true
url: https://github.com/Mayuqi-crypto/everything-search-skill
canonical_url: https://github.com/Mayuqi-crypto/everything-search-skill
summary: ⚡ Ultra-fast, index-powered local file search skill for AI agents (Cursor, Codex, PI-Desktop)
  using Voidtools Everything
first_seen: '2026-09-19T06:08:37Z'
last_seen: '2026-09-26T00:37:55Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/Mayuqi-crypto/everything-search-skill
  seen_at: '2026-09-26T00:37:55Z'
  metrics:
    stars: 67
    forks: 2
    open_issues: 0
  kind: product
---

# everything-search-skill

⚡ Ultra-fast, index-powered local file search skill for AI agents (Cursor, Codex, PI-Desktop) using Voidtools Everything

## 笔记


