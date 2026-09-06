---
slug: datasette-mcp-02
name: datasette-mcp
builder: ''
category: AI + 开发
summary_zh: datasette-mcp 是一个开源插件，让开发者通过 MCP 协议用 AI 助手查询 Datasette 数据库。它接收 SQL 查询请求，执行后返回结果，0.2 版将行数据改为对象数组，便于模型理解列映射。具体使用场景和交付物仍需核验。
inspiration: 趋势：数据库查询正成为 AI 助手的标准能力，MCP 协议在统一接口。切入：面向数据分析师和开发者，可强化对列结构的清晰返回，减少模型出错，但需明确付费场景。
summary_en: datasette-mcp is an open-source plugin that lets developers query Datasette databases via
  AI assistants using the MCP protocol. It receives SQL queries, executes them, and returns results; version
  0.2 changes row data to an array of objects for better column mapping. Specific use cases and deliverables
  still need verification.
inspiration_en: 'Trend: database querying is becoming a standard capability for AI assistants, with MCP
  unifying interfaces. Entry: target data analysts and developers, emphasize clear column structure to
  reduce model errors, but clarify monetization scenarios.'
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software Development
jobs:
- 开发者
jobs_en:
- Developers
regions: []
regions_en: []
open_source: true
url: https://simonwillison.net/2026/Sep/1/datasette-mcp/
canonical_url: https://simonwillison.net/2026/Sep/1/datasette-mcp
summary: "Release:   datasette-mcp 0.2  \n         \n \n  \"rows\"  from  execute_sql  is now an array\
  \ of objects. Previously it was an array of arrays. This should help weaker models avoid losing track\
  \ of which positional array element maps to which column.  #1  \n Now depends on  mcp>=2.1.1 . \n \n\
  \ \n This is the first non-alpha release of the plugin. I'm confident it's ready as I've been using\
  \ it quite a bit myself. \n    \n    \n         Tags:  datasette ,  model-context-protocol"
first_seen: '2026-09-01T15:30:12Z'
last_seen: '2026-09-02T14:32:03Z'
status: watching
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/1/datasette-mcp/
  seen_at: '2026-09-02T14:32:03Z'
  metrics: {}
  kind: news
---

# datasette-mcp

Release:   datasette-mcp 0.2  
         
 
  "rows"  from  execute_sql  is now an array of objects. Previously it was an array of arrays. This should help weaker models avoid losing track of which positional array element maps to which column.  #1  
 Now depends on  mcp>=2.1.1 . 
 
 
 This is the first non-alpha release of the plugin. I'm confident it's ready as I've been using it quite a bit myself. 
    
    
         Tags:  datasette ,  model-context-protocol

## 笔记


