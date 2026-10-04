---
slug: mcp-audit-tool
name: mcp-audit-tool
builder: graygnatconsole
category: AI + 开发
summary_zh: 开发或安全工程师在把第三方 MCP 服务器接入自家 AI 代理前，打开这个命令行工具，让它读取代理的 MCP 配置文件，扫描工具投毒、硬编码密钥、命令注入和依赖供应链风险，最后拿到一份可接入
  CI 的 SARIF 报告；是否放行仍需人工判断。
inspiration: 趋势：AI 代理开始调用外部工具后，配置本身成了新的攻击面，安全审查从代码前移到代理配置。切入：从已经大规模接入第三方 MCP 服务器的平台团队切入，把扫描做成 CI 必过门禁或上线前审计服务；公开材料未披露定价与客户，具体卖法仍待核验。
summary_en: Before wiring third-party MCP servers into their AI agents, developers or security engineers
  run this CLI, which reads the agent's MCP config files, scans for tool poisoning, hardcoded secrets,
  command injection and dependency supply-chain risks, and returns a SARIF report usable in CI; a human
  still decides whether to allow the server.
inspiration_en: 'Trend: once AI agents call external tools, configuration itself becomes an attack surface
  and security review moves ahead of code into agent configs. Entry: start with platform teams already
  wiring many third-party MCP servers, selling the scan as a CI gate or pre-launch audit; no pricing or
  customers are disclosed, so the selling model remains unverified.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
- 信息安全
industries_en:
- Software and IT services
- Information security
jobs:
- 安全工程师
- 平台工程师
jobs_en:
- Security engineer
- Platform engineer
regions: []
regions_en: []
open_source: true
url: https://github.com/graygnatconsole/mcp-audit-tool
canonical_url: https://github.com/graygnatconsole/mcp-audit-tool
summary: 🛡️ Security audit CLI for Model Context Protocol (MCP) servers — scan AI agent configs for tool
  poisoning, rug pulls, hardcoded secrets, command injection & supply-chain risks. Pure Python, SARIF
  + CI ready.
first_seen: '2026-09-26T02:42:57Z'
last_seen: '2026-10-04T00:37:57Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/graygnatconsole/mcp-audit-tool
  seen_at: '2026-10-04T00:37:57Z'
  metrics:
    stars: 76
    forks: 3
    open_issues: 0
  kind: product
---

# mcp-audit-tool

🛡️ Security audit CLI for Model Context Protocol (MCP) servers — scan AI agent configs for tool poisoning, rug pulls, hardcoded secrets, command injection & supply-chain risks. Pure Python, SARIF + CI ready.

## 笔记


