---
slug: jevcrawl
name: Jevcrawl
builder: rayenmlayeh
category: 基础层
summary_zh: 面向给 AI Agent 接网页数据的开发者，在 Agent 需要从网站取回答案页的工作节点上，Jevcrawl 以 MCP 服务与命令行形式接收目标站点，用不含大模型的爬取循环定位答案页并返回内容，交付的是抓取结果与更低的单次答案成本；其对比数据来自项目自述，尚待独立复现。
inspiration: 趋势：Agent 取数环节开始把大模型从爬取循环里拿掉，用确定性抓取换成本与稳定性，模型只留在理解环节。切入：可从需要批量取网页答案的 Agent 团队切入，按抓取量或按答案条数收费；项目自述的
  2 倍命中率与 10 倍成本优势尚未被独立复现，这是判断窗口的关键缺口。
summary_en: For developers feeding web data to AI agents, at the point where an agent needs the answer
  page from a site, Jevcrawl ships as an MCP server and CLI that takes a target site, locates the answer
  page with a crawl loop containing no LLM, and returns the content plus a lower per-answer cost; its
  comparison figures are self-reported and await independent reproduction.
inspiration_en: 'Trend: the agent data-fetching step is removing LLMs from the crawl loop, trading deterministic
  crawling for cost and stability while models stay in the understanding step. Entry: target agent teams
  that fetch web answers at volume, charging per crawl or per answer; the self-reported 2x hit rate and
  10x cost advantage are not independently reproduced, which is the key gap.'
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs:
- AI Agent 开发者
- 数据采集工程团队
jobs_en:
- AI agent developers
- Data collection engineering teams
regions: []
regions_en: []
open_source: true
url: https://github.com/RayenMlayeh/jevcrawl
canonical_url: https://github.com/RayenMlayeh/jevcrawl
summary: A web crawler for AI agents with no LLM in the crawl loop
first_seen: '2026-10-15T00:32:05Z'
last_seen: '2026-10-16T00:25:17Z'
status: watching
sources:
- hackernews
- github
sightings:
- source: hackernews
  url: https://github.com/RayenMlayeh/jevcrawl
  seen_at: '2026-10-15T00:32:05Z'
  metrics:
    points: 20
    comments: 3
  kind: product
- source: github
  url: https://github.com/RayenMlayeh/jevcrawl
  seen_at: '2026-10-16T00:25:17Z'
  metrics:
    stars: 66
    forks: 6
    open_issues: 6
  kind: product
---

# Jevcrawl

A web crawler for AI agents with no LLM in the crawl loop

## 笔记


