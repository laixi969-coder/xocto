---
slug: mcp-auth-keydris-template
name: mcp-auth-keydris-template
builder: b4timer
category: 基础层
summary_zh: 开发者在给智能体接入 MCP 工具时使用该模板，把凭据留在授权层、只向智能体暴露可调用的工具权限，最终得到一次被授权的工具调用；具体授权流程、支持的工具范围与部署方式仍待核验。
inspiration: 趋势是智能体开始调用真实系统后，凭据管理从「给人发密钥」变成「给智能体发受限权限」。切入可考虑为特定行业系统（如财务、医疗、工业设备）做权限代理与审计交付，按接入的系统数或审计报告收费，而不是再做一个通用授权模板。
summary_en: Developers wiring agents to MCP tools use this template to keep credentials in an authorization
  layer and expose only callable tool permissions to the agent, ending in an authorized tool call; the
  exact authorization flow, supported tool scope, and deployment method still need verification.
inspiration_en: The trend is that once agents call real systems, credential management shifts from issuing
  keys to people to issuing scoped permissions to agents. A wedge is to build permission brokering and
  audit delivery for specific industry systems such as finance, healthcare, or industrial equipment, charging
  per connected system or per audit report instead of shipping another generic authorization template.
priority_review: false
project_type: open_source
industries:
- 软件开发
- 信息安全服务
industries_en:
- Software development
- Information security services
jobs:
- 后端与平台工程师
- 安全工程师
jobs_en:
- Backend and platform engineers
- Security engineers
regions: []
regions_en: []
open_source: true
url: https://github.com/keydrisLabs/mcp-auth-keydris-template
canonical_url: https://github.com/keydrisLabs/mcp-auth-keydris-template
summary: Authorize MCP tool calls without giving agents the credentials
first_seen: '2026-09-14T11:52:07Z'
last_seen: '2026-09-15T00:38:38Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://github.com/keydrisLabs/mcp-auth-keydris-template
  seen_at: '2026-09-15T00:38:38Z'
  metrics:
    points: 6
    comments: 6
  kind: product
---

# mcp-auth-keydris-template

Authorize MCP tool calls without giving agents the credentials

## 笔记


