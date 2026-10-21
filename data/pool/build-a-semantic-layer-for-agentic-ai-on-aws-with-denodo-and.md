---
slug: build-a-semantic-layer-for-agentic-ai-on-aws-with-denodo-and
name: Build a semantic layer for agentic AI on AWS with Denodo and Amazon Bedrock AgentCore
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
url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-on-aws-with-denodo-and-amazon-bedrock-agentcore/
canonical_url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-on-aws-with-denodo-and-amazon-bedrock-agentcore
summary: 'Agentic AI applications need governed access to live enterprise data. That data can live in
  operational systems, analytical warehouses, SaaS applications, other clouds, or on premises. In the
  previous post in this series , we built a semantic layer on AWS using Stardog’s knowledge graph over
  Amazon Aurora and Amazon Redshift. A Strands agent on Amazon Bedrock AgentCore queried that layer. Amazon
  Bedrock AgentCore is a platform to build, connect, and optimize agents at scale, with any framework
  or model. This post uses the same customer 360 pattern, but swaps in a different semantic layer implementation
  and extends the source mix. Two things change here. First, the semantic layer is the Denodo Platform:
  an AI data layer that provides active context and live, zero-copy access to distributed enterprise data.
  The agent talks to it in VQL , Denodo’s SQL dialect. Second, the source mix includes an on-premises
  PostgreSQL database alongside Amazon Aurora and Amazon Redshift, so the federation problem is no longer
  bounded by an Amazon Virtual Private Cloud (Amazon VPC). The rest of the pattern carries over. A foundation
  model on Amazon Bedrock plans and writes queries. The Denodo MCP Server exposes governed views to the
  agent through the'
first_seen: '2026-10-21T00:38:23Z'
last_seen: '2026-10-21T00:38:23Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-on-aws-with-denodo-and-amazon-bedrock-agentcore/
  seen_at: '2026-10-21T00:38:23Z'
  metrics: {}
  kind: news
---

# Build a semantic layer for agentic AI on AWS with Denodo and Amazon Bedrock AgentCore

Agentic AI applications need governed access to live enterprise data. That data can live in operational systems, analytical warehouses, SaaS applications, other clouds, or on premises. In the previous post in this series , we built a semantic layer on AWS using Stardog’s knowledge graph over Amazon Aurora and Amazon Redshift. A Strands agent on Amazon Bedrock AgentCore queried that layer. Amazon Bedrock AgentCore is a platform to build, connect, and optimize agents at scale, with any framework or model. This post uses the same customer 360 pattern, but swaps in a different semantic layer implementation and extends the source mix. Two things change here. First, the semantic layer is the Denodo Platform: an AI data layer that provides active context and live, zero-copy access to distributed enterprise data. The agent talks to it in VQL , Denodo’s SQL dialect. Second, the source mix includes an on-premises PostgreSQL database alongside Amazon Aurora and Amazon Redshift, so the federation problem is no longer bounded by an Amazon Virtual Private Cloud (Amazon VPC). The rest of the pattern carries over. A foundation model on Amazon Bedrock plans and writes queries. The Denodo MCP Server exposes governed views to the agent through the

## 笔记


