---
slug: secure-oauth-patterns-for-snowflake-cortex-ai-through-amazon
name: Secure OAuth patterns for Snowflake Cortex AI through Amazon Bedrock AgentCore
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
url: https://aws.amazon.com/blogs/machine-learning/secure-oauth-patterns-for-snowflake-cortex-ai-through-amazon-bedrock-agentcore/
canonical_url: https://aws.amazon.com/blogs/machine-learning/secure-oauth-patterns-for-snowflake-cortex-ai-through-amazon-bedrock-agentcore
summary: 'Enterprises today need a clear way to extend their authentication and authorization controls
  into the agentic layer, often requiring either broad service account permissions or custom-built auth
  integrations that add operational overhead. When an AI agent running on Amazon Bedrock AgentCore (a
  platform to build, connect, and optimize agents at scale, with any framework or model) needs to call
  the Snowflake-managed MCP server (which exposes Snowflake Cortex Agents as one of its tool types) through
  the Model Context Protocol (MCP), the first question enterprises must answer is: how does the agent
  authenticate? In this post, we walk through three Open Authorization (OAuth) configurations we tested
  on Amazon Bedrock AgentCore Identity , a capability of Amazon Bedrock AgentCore: Snowflake OAuth (per-user,
  no external Identity Provider, or IdP), three-legged OAuth with a third-party Identity Provider (corporate
  single sign-on, or SSO), and two-legged OAuth with a third-party Identity Provider (shared service user).
  Amazon Bedrock AgentCore Identity also supports an on-behalf-of (OBO) grant (TOKEN_EXCHANGE) that delivers
  per-user identity for unattended workloads without a consent prompt. We focus on the three configurations
  we tested end-to-end, flagging where OBO fits as we go. By the end, you will be able to identify which
  pattern suits your'
first_seen: '2026-11-18T03:43:37Z'
last_seen: '2026-11-18T03:43:37Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/secure-oauth-patterns-for-snowflake-cortex-ai-through-amazon-bedrock-agentcore/
  seen_at: '2026-11-18T03:43:37Z'
  metrics: {}
  kind: news
---

# Secure OAuth patterns for Snowflake Cortex AI through Amazon Bedrock AgentCore

Enterprises today need a clear way to extend their authentication and authorization controls into the agentic layer, often requiring either broad service account permissions or custom-built auth integrations that add operational overhead. When an AI agent running on Amazon Bedrock AgentCore (a platform to build, connect, and optimize agents at scale, with any framework or model) needs to call the Snowflake-managed MCP server (which exposes Snowflake Cortex Agents as one of its tool types) through the Model Context Protocol (MCP), the first question enterprises must answer is: how does the agent authenticate? In this post, we walk through three Open Authorization (OAuth) configurations we tested on Amazon Bedrock AgentCore Identity , a capability of Amazon Bedrock AgentCore: Snowflake OAuth (per-user, no external Identity Provider, or IdP), three-legged OAuth with a third-party Identity Provider (corporate single sign-on, or SSO), and two-legged OAuth with a third-party Identity Provider (shared service user). Amazon Bedrock AgentCore Identity also supports an on-behalf-of (OBO) grant (TOKEN_EXCHANGE) that delivers per-user identity for unattended workloads without a consent prompt. We focus on the three configurations we tested end-to-end, flagging where OBO fits as we go. By the end, you will be able to identify which pattern suits your

## 笔记


