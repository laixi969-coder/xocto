---
slug: build-a-semantic-layer-for-agentic-ai-with-edb-postgres-ai-a
name: Build a semantic layer for agentic AI with EDB Postgres AI and Amazon Bedrock AgentCore
builder: ''
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
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
url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-with-edb-postgres-ai-and-amazon-bedrock-agentcore/
canonical_url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-with-edb-postgres-ai-and-amazon-bedrock-agentcore
summary: 'In this post, we show how to build a semantic layer for agentic AI using EDB Postgres AI . We
  run a Strands Agents agent on Amazon Bedrock AgentCore that queries the layer to answer customer 360
  (C360) questions. Earlier posts in this series built the same C360 pattern with Stardog’s knowledge
  graph , Denodo’s data virtualization platform , AtScale’s dimensional model , and Strategy Mosaic’s
  linked models . EDB Postgres AI puts the semantic layer inside the operational Postgres database as
  an AIDB extension . Business meaning lives next to the data in standard Postgres COMMENT statements,
  the join graph comes from Postgres foreign keys, and governance uses Postgres GRANT and row-level security
  through the Model Context Protocol (MCP) endpoint that ships with AIDB. By the end of this post you
  will know: How to build an AIDB semantic knowledge base (SemKB) over a Postgres schema, how COMMENT
  ON statements and aidb.create_semantic_alias behave as the authoring surface, and how foreign keys crawl
  into join paths. How to expose the AIDB tool catalog to an external agent through the built-in EDB MCP
  endpoint, fronted by an Application Load Balancer (ALB) and registered as an MCP target on AgentCore
  Gateway ,'
first_seen: '2026-11-04T02:21:16Z'
last_seen: '2026-11-04T02:21:16Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-with-edb-postgres-ai-and-amazon-bedrock-agentcore/
  seen_at: '2026-11-04T02:21:16Z'
  metrics: {}
  kind: news
---

# Build a semantic layer for agentic AI with EDB Postgres AI and Amazon Bedrock AgentCore

In this post, we show how to build a semantic layer for agentic AI using EDB Postgres AI . We run a Strands Agents agent on Amazon Bedrock AgentCore that queries the layer to answer customer 360 (C360) questions. Earlier posts in this series built the same C360 pattern with Stardog’s knowledge graph , Denodo’s data virtualization platform , AtScale’s dimensional model , and Strategy Mosaic’s linked models . EDB Postgres AI puts the semantic layer inside the operational Postgres database as an AIDB extension . Business meaning lives next to the data in standard Postgres COMMENT statements, the join graph comes from Postgres foreign keys, and governance uses Postgres GRANT and row-level security through the Model Context Protocol (MCP) endpoint that ships with AIDB. By the end of this post you will know: How to build an AIDB semantic knowledge base (SemKB) over a Postgres schema, how COMMENT ON statements and aidb.create_semantic_alias behave as the authoring surface, and how foreign keys crawl into join paths. How to expose the AIDB tool catalog to an external agent through the built-in EDB MCP endpoint, fronted by an Application Load Balancer (ALB) and registered as an MCP target on AgentCore Gateway ,

## 笔记


