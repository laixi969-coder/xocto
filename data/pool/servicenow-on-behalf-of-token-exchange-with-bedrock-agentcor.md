---
slug: servicenow-on-behalf-of-token-exchange-with-bedrock-agentcor
name: ServiceNow on-behalf-of token exchange with Bedrock AgentCore Gateway
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
url: https://aws.amazon.com/blogs/machine-learning/servicenow-on-behalf-of-token-exchange-with-bedrock-agentcore-gateway/
canonical_url: https://aws.amazon.com/blogs/machine-learning/servicenow-on-behalf-of-token-exchange-with-bedrock-agentcore-gateway
summary: 'AI agents that interact with enterprise APIs on behalf of users need to maintain user identity
  throughout the request chain. Without identity propagation, API calls arrive at downstream services
  as the application itself rather than the user who initiated the action. This breaks audit trails, bypasses
  user-level access controls, and violates the principle of least privilege. Amazon Bedrock AgentCore
  is a platform to build, connect, and optimize agents at scale, with any framework or model. This post
  shows how to configure AgentCore Gateway , a capability of Amazon Bedrock AgentCore, for an on-behalf-of
  (OBO) token exchange with Microsoft Entra ID. An AI agent can then call the ServiceNow REST API while
  preserving the calling user’s identity. You configure the token exchange on the gateway target, and
  AgentCore Gateway performs the exchange on each request. The pattern can be applied to other REST APIs
  protected by OAuth. In production, you can additionally pair identity propagation with Amazon Bedrock
  Guardrails to filter harmful content and validate the agent’s inputs and outputs. Solution overview
  The architecture involves three key components connected through AgentCore Gateway: An AI agent application,
  protected by Microsoft Entra ID through an OAuth application registration. A Model Context Protocol
  (MCP)'
first_seen: '2026-11-04T02:21:16Z'
last_seen: '2026-11-04T02:21:16Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/servicenow-on-behalf-of-token-exchange-with-bedrock-agentcore-gateway/
  seen_at: '2026-11-04T02:21:16Z'
  metrics: {}
  kind: news
---

# ServiceNow on-behalf-of token exchange with Bedrock AgentCore Gateway

AI agents that interact with enterprise APIs on behalf of users need to maintain user identity throughout the request chain. Without identity propagation, API calls arrive at downstream services as the application itself rather than the user who initiated the action. This breaks audit trails, bypasses user-level access controls, and violates the principle of least privilege. Amazon Bedrock AgentCore is a platform to build, connect, and optimize agents at scale, with any framework or model. This post shows how to configure AgentCore Gateway , a capability of Amazon Bedrock AgentCore, for an on-behalf-of (OBO) token exchange with Microsoft Entra ID. An AI agent can then call the ServiceNow REST API while preserving the calling user’s identity. You configure the token exchange on the gateway target, and AgentCore Gateway performs the exchange on each request. The pattern can be applied to other REST APIs protected by OAuth. In production, you can additionally pair identity propagation with Amazon Bedrock Guardrails to filter harmful content and validate the agent’s inputs and outputs. Solution overview The architecture involves three key components connected through AgentCore Gateway: An AI agent application, protected by Microsoft Entra ID through an OAuth application registration. A Model Context Protocol (MCP)

## 笔记


