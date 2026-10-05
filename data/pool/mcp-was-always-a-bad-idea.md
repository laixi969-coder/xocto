---
slug: mcp-was-always-a-bad-idea
name: Model Context Protocol
builder: ''
category: ''
summary_zh: 围绕 Model Context Protocol 是否过时的讨论指出，在拥有不受限网络访问的终端智能体之外，MCP 仍提供对外部服务访问范围的控制、不让智能体直接接触 API 密钥的认证方式、供用户连接并认证更多服务的界面以及审计日志；这意味着在受控、可审计的智能体部署中，MCP
  仍是连接外部服务的实际接口层。
inspiration: ''
summary_en: Discussion over whether the Model Context Protocol is obsolete notes that beyond terminal
  agents with unfettered internet access, MCP still provides control over which external services an agent
  can reach, authentication that keeps API keys away from the agent, a UI for users to connect and authenticate
  further services, and audit logging; this means MCP remains the practical interface layer for connecting
  external services in controlled, auditable agent deployments.
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
last_seen: '2026-10-05T00:56:35Z'
status: market_context
sources:
- marketfeeds
- newssearch
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/20/hn-49779718/
  seen_at: '2026-09-22T00:50:51Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMifEFVX3lxTFBsaVhNdGpWbEFySHNJaWo4aG5HLVlxakg5TTlhVDBqLVBCU0NQQlJrZWlyaHAwVHduZ0dIUk9hWlFVQmRSNGtTSzZjLUhiS20zNGF1cmtWQ2xfUTdVT0J4cnlCR1BTOFVlX3BIaEYyOXMzZXhBQ0loZFVsV2w?oc=5
  seen_at: '2026-09-28T00:47:18Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMifEFVX3lxTE44WjlMcGRmRUstejJtVDZSa3JFRm82bFVmS01JQ2hkUk1UdTJEQ3ZsZURIT2p3YnlhR0g3cUZVX3JjMURMdEhaS0ViT3NRWmx0NTFmdnQzbUxNOFVQZmNRb0xseV8yUjB1TXdqVFZXUHA0ODJzOE96THozTEY?oc=5
  seen_at: '2026-10-05T00:56:35Z'
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


