---
slug: foxprofile-2
name: foxprofile
builder: chienbm98
category: AI + 开发
summary_zh: 多账号运营或自动化工程师在需要同时登录多个店铺、广告或采集账号时，打开 foxprofile 为每个账号建立独立浏览器档案，分别绑定指纹、Cookie 与代理，并可选 Camoufox
  或 Chrome 内核；桌面端之外还提供 REST API 与 MCP 服务，供 AI 代理调用这些档案。最终交付是一批可被程序调用的隔离浏览器会话，具体合规边界与交付细节仍待核验。
inspiration: 趋势是浏览器身份隔离正从商业反检测软件下沉为可自托管、可被 AI 代理调用的开源基础设施，指纹与代理不再只是工具功能，而是代理执行任务时的环境层。切入可考虑跨境电商多店铺、广告投放与数据采集团队，把档案托管、代理轮换与合规审计打包成按账号数或按会话量计费的服务；开源版本已存在，卖点应落在托管稳定性与合规记录，而非内核本身。
summary_en: When multi-account operators or automation engineers need to stay logged into several storefront,
  ad or scraping accounts at once, they open foxprofile to create an isolated browser profile per account,
  binding its own fingerprint, cookies and proxy, with a choice of Camoufox or Chrome engines; beyond
  the desktop app it exposes a REST API and an MCP server so AI agents can drive those profiles. The deliverable
  is a set of programmatically callable isolated browser sessions, while compliance boundaries and delivery
  details remain to be verified.
inspiration_en: The trend is that browser identity isolation is sinking from commercial anti-detect suites
  into self-hosted open-source infrastructure that AI agents can call, making fingerprints and proxies
  an environment layer rather than a tool feature. A wedge is cross-border e-commerce multi-store, ad-buying
  and scraping teams, packaging profile hosting, proxy rotation and compliance logging as a service billed
  per account or per session; since the open-source version exists, the sellable part is hosting reliability
  and compliance records, not the engine itself.
priority_review: false
project_type: open_source
industries:
- 跨境电商
- 广告营销
- 数据采集
industries_en:
- cross-border e-commerce
- advertising and marketing
- data collection
jobs:
- 多账号运营人员在同一台电脑上为不同店铺或广告账户维护独立浏览器环境
- 自动化工程师为 AI 代理批量调度带独立指纹与代理的浏览器会话
jobs_en:
- multi-account operators maintaining separate browser environments for different storefronts or ad accounts
  on one machine
- automation engineers dispatching browser sessions with isolated fingerprints and proxies for AI agents
regions: []
regions_en: []
open_source: true
url: https://github.com/chienbm98/foxprofile/releases/latest
canonical_url: https://github.com/chienbm98/foxprofile/releases/latest
summary: 'Free, open-source anti-detect browser profile manager: per-profile fingerprint, cookies and
  proxy, Camoufox and Chrome engines, desktop app, REST API and MCP server for AI agents. Self-hosted
  alternative to GoLogin / MoreLogin.'
first_seen: '2026-10-12T01:20:35Z'
last_seen: '2026-10-26T00:24:22Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/chienbm98/foxprofile/releases/latest
  seen_at: '2026-10-26T00:24:22Z'
  metrics:
    stars: 162
    forks: 77
    open_issues: 8
  kind: product
---

# foxprofile

Free, open-source anti-detect browser profile manager: per-profile fingerprint, cookies and proxy, Camoufox and Chrome engines, desktop app, REST API and MCP server for AI agents. Self-hosted alternative to GoLogin / MoreLogin.

## 笔记


