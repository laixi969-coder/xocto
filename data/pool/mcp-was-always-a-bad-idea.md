---
slug: mcp-was-always-a-bad-idea
name: Model Context Protocol
builder: ''
category: ''
summary_zh: 2026年9月20日，围绕 Model Context Protocol（MCP）是否已过时出现公开讨论：有观点认为，具备完整终端与不受限网络访问能力的编码代理可直接调用 API，因而无需
  MCP；反驳意见指出，在需要限制代理可访问的外部服务、避免代理直接接触 API 密钥的认证方式、提供用户连接与授权的界面以及强审计日志等场景下，MCP 仍显著降低实现难度。该讨论表明，代理接入层的竞争焦点正从“能否调用工具”转向权限控制、凭证隔离与可审计性，这会影响
  AI 应用在企业环境中的交付方式与合规成本（推断）。
inspiration: ''
summary_en: 'On September 20, 2026, a public debate emerged over whether the Model Context Protocol (MCP)
  is obsolete: one view holds that full terminal coding agents with unfettered internet access can call
  APIs directly and therefore do not need MCP, while a rebuttal argues MCP still makes it far easier to
  control exactly which external services an agent can access, handle authentication without exposing
  API keys to the agent, provide a UI for users to connect and authorize services, and maintain strong
  audit logging. The discussion indicates that competition in the agent integration layer is shifting
  from whether tools can be called to permission control, credential isolation and auditability, which
  affects how AI applications are delivered and their compliance costs in enterprise settings (inference).'
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
url: https://simonwillison.net/2026/Sep/20/hn-49779718/
canonical_url: https://simonwillison.net/2026/Sep/20/hn-49779718
summary: "My comment  on  MCP was always a bad idea?  — Hacker News.  This article entirely misses the\
  \ value that MCP brings today. \n Sure, there's almost no reason to use MCPs if you are running a full-blown\
  \ terminal agent (Claude Code, Codex, Meta Muse, OpenClaw etc) with unfettered internet access - just\
  \ let it call APIs directly. \n If you want to operate something that's less YOLO than that, you'll\
  \ find yourself wanting: \n \n Control over exactly which external services it can access \n A way to\
  \ handle authentication that doesn't allow the agent to directly access API keys \n A sensible UI to\
  \ allow users to connect and authenticate further services \n Strong audit logging for what's going\
  \ on \n \n MCP makes all of that so much easier to provide. \n Thinking MCP is obsolete because full\
  \ coding agents don't need it misses out on all of the other things we might want to build. \n    \n\
  \    \n         Tags:  hacker-news ,  model-context-protocol"
first_seen: '2026-09-20T20:24:41Z'
last_seen: '2026-09-22T00:50:51Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/20/hn-49779718/
  seen_at: '2026-09-22T00:50:51Z'
  metrics: {}
  kind: news
---

# Model Context Protocol

My comment  on  MCP was always a bad idea?  — Hacker News.  This article entirely misses the value that MCP brings today. 
 Sure, there's almost no reason to use MCPs if you are running a full-blown terminal agent (Claude Code, Codex, Meta Muse, OpenClaw etc) with unfettered internet access - just let it call APIs directly. 
 If you want to operate something that's less YOLO than that, you'll find yourself wanting: 
 
 Control over exactly which external services it can access 
 A way to handle authentication that doesn't allow the agent to directly access API keys 
 A sensible UI to allow users to connect and authenticate further services 
 Strong audit logging for what's going on 
 
 MCP makes all of that so much easier to provide. 
 Thinking MCP is obsolete because full coding agents don't need it misses out on all of the other things we might want to build. 
    
    
         Tags:  hacker-news ,  model-context-protocol

## 笔记


