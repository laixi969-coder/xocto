---
slug: mcp-was-always-a-bad-idea
name: Model Context Protocol
builder: ''
category: ''
summary_zh: 围绕 Model Context Protocol 是否仍有价值的公开讨论指出，在拥有不受限网络访问的终端智能体场景下可直接调用 API，但 MCP 在受控外部服务访问、避免智能体直接接触
  API 密钥的鉴权、用户连接与授权界面以及审计日志方面仍提供价值。这意味着在需要权限控制与合规审计的企业级 AI 应用中，MCP 仍是降低集成与治理成本的候选方案；该判断来自评论者观点，属于推断。
inspiration: ''
summary_en: Public discussion over whether the Model Context Protocol still has value notes that terminal
  agents with unfettered internet access can call APIs directly, yet MCP still helps with controlled access
  to external services, authentication that keeps API keys away from the agent, user-facing connection
  and authorization flows, and audit logging. This implies MCP remains a candidate for lowering integration
  and governance costs in enterprise AI applications that need permission control and compliance auditing;
  the claim comes from a commentator and is an inference.
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
status: pending_filter
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


