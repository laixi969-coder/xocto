---
slug: foxprofile
name: foxprofile
builder: chienbm98
category: AI + 开发
summary_zh: 多账号运营或采集人员要同时管理多个店铺、广告或抓取账号时，打开 foxprofile 为每个账号建立独立浏览器档案，由它分别保存指纹、Cookie 与代理，并可用 REST API
  或 MCP 让 AI 代理调用这些档案；最终交付是彼此隔离、可复用的浏览器会话，具体隔离强度与合规边界仍待核验。
inspiration: 趋势是反检测浏览器从按月订阅的闭源工具，变成可自托管、可被 AI 代理调用的开源组件，指纹与代理这类“环境资产”开始和自动化脚本解耦。切入可放在跨境电商多店铺或广告投放团队：他们本来按账号数买闭源席位，若自托管能省下席位费并让脚本直接接管会话，卖法可能从卖席位转向卖托管、代理资源或合规审计，价格未披露不做假设。
summary_en: When operators juggling multiple storefronts, ad accounts or scraping identities need separate
  browser environments, they open foxprofile to create one profile per account; it stores each profile's
  fingerprint, cookies and proxy, and exposes them through a REST API and MCP server so AI agents can
  drive the sessions. The deliverable is isolated, reusable browser sessions; actual isolation strength
  and compliance boundaries still need checking.
inspiration_en: The shift is that anti-detect browsers are moving from closed monthly subscriptions to
  self-hosted open components that AI agents can call, decoupling fingerprint and proxy 'environment assets'
  from automation scripts. The entry point is cross-border e-commerce or ad-buying teams that today pay
  per-seat for closed tools; if self-hosting removes seat fees and lets scripts take over sessions, the
  sell could move to hosting, proxy supply or compliance auditing, with no disclosed pricing assumed.
priority_review: false
project_type: open_source
industries:
- 跨境电商
- 广告技术
- 数据采集
industries_en:
- Cross-border e-commerce
- Ad tech
- Data collection
jobs:
- 多账号运营人员在同一台电脑上为不同店铺或广告账户维护互相隔离的浏览器环境
- 数据采集工程师为批量抓取任务配置独立指纹与代理
jobs_en:
- Multi-account operators maintaining isolated browser environments for separate storefronts or ad accounts
  on one machine
- Data-collection engineers configuring separate fingerprints and proxies for bulk scraping tasks
regions: []
regions_en: []
open_source: true
url: https://github.com/chienbm98/foxprofile
canonical_url: https://github.com/chienbm98/foxprofile
summary: 'Free, open-source anti-detect browser profile manager: per-profile fingerprint, cookies and
  proxy, Camoufox and Chrome engines, desktop app, REST API and MCP server for AI agents. Self-hosted
  alternative to GoLogin / MoreLogin.'
first_seen: '2026-10-11T01:01:22Z'
last_seen: '2026-10-11T01:01:22Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/chienbm98/foxprofile
  seen_at: '2026-10-11T01:01:22Z'
  metrics:
    stars: 56
    forks: 42
    open_issues: 1
  kind: product
---

# foxprofile

Free, open-source anti-detect browser profile manager: per-profile fingerprint, cookies and proxy, Camoufox and Chrome engines, desktop app, REST API and MCP server for AI agents. Self-hosted alternative to GoLogin / MoreLogin.

## 笔记


