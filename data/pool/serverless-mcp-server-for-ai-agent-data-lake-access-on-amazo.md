---
slug: serverless-mcp-server-for-ai-agent-data-lake-access-on-amazo
name: Serverless MCP server for AI agent data lake access on Amazon ECS Fargate
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
url: https://aws.amazon.com/blogs/machine-learning/serverless-mcp-server-for-ai-agent-data-lake-access-on-amazon-ecs-fargate/
canonical_url: https://aws.amazon.com/blogs/machine-learning/serverless-mcp-server-for-ai-agent-data-lake-access-on-amazon-ecs-fargate
summary: 'Organizations building applications powered by artificial intelligence (AI) face a recurring
  challenge: giving large language model (LLM) agents access to enterprise data lakes without duplicating
  integration logic across every agent and application. Most teams begin by wiring agents directly to
  databases and APIs, with no shared gateway such as a Model Context Protocol (MCP) server in between.
  Each new dataset demands custom code, and each agent reimplements its own access control. As the number
  of datasets or agents grows, permission enforcement drifts, and onboarding a new data source becomes
  a multi-day engineering effort. Our team supports Amazon’s North America Sort Center (NASC) network,
  where planning teams rely on operational data to manage capacity, labor, and package flow. To give those
  teams conversational access to that data, we built a serverless Model Context Protocol (MCP) server
  on Amazon Elastic Container Service (Amazon ECS) with AWS Fargate to address this problem for planning
  teams in NASC. The server acts as a centralized, agent-agnostic gateway between AI agents and our enterprise
  data lake. Exposing a new dataset requires only a JSON metadata file that the server discovers automatically
  on the next pipeline sync. In this post, we describe the architecture, show how a'
first_seen: '2026-11-07T01:57:08Z'
last_seen: '2026-11-07T01:57:08Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/serverless-mcp-server-for-ai-agent-data-lake-access-on-amazon-ecs-fargate/
  seen_at: '2026-11-07T01:57:08Z'
  metrics: {}
  kind: news
---

# Serverless MCP server for AI agent data lake access on Amazon ECS Fargate

Organizations building applications powered by artificial intelligence (AI) face a recurring challenge: giving large language model (LLM) agents access to enterprise data lakes without duplicating integration logic across every agent and application. Most teams begin by wiring agents directly to databases and APIs, with no shared gateway such as a Model Context Protocol (MCP) server in between. Each new dataset demands custom code, and each agent reimplements its own access control. As the number of datasets or agents grows, permission enforcement drifts, and onboarding a new data source becomes a multi-day engineering effort. Our team supports Amazon’s North America Sort Center (NASC) network, where planning teams rely on operational data to manage capacity, labor, and package flow. To give those teams conversational access to that data, we built a serverless Model Context Protocol (MCP) server on Amazon Elastic Container Service (Amazon ECS) with AWS Fargate to address this problem for planning teams in NASC. The server acts as a centralized, agent-agnostic gateway between AI agents and our enterprise data lake. Exposing a new dataset requires only a JSON metadata file that the server discovers automatically on the next pipeline sync. In this post, we describe the architecture, show how a

## 笔记


