---
slug: govern-ai-agent-access-with-okta-cross-app-access-and-amazon
name: Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 2
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
url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-2/
canonical_url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-2
summary: 'In Part 1 , you built a task agent on Amazon Bedrock AgentCore , a platform to build, connect,
  and optimize agents at scale, with any framework or model. The agent runs on Amazon Bedrock AgentCore
  runtime, a capability of Amazon Bedrock AgentCore, and acts for signed-in users through Okta Cross App
  Access (XAA). Okta decided which agent might act for which user, and Amazon Bedrock AgentCore Identity,
  a capability of Amazon Bedrock AgentCore, redeemed Okta’s grant inside the agent. That proves the governance
  mechanism, and it runs on a deliberately small topology: one agent, two Model Context Protocol (MCP)
  servers, and the authorization check written into each server. The mechanism scales. The topology doesn’t.
  Three things that are fine for one agent and two tools become the work in an enterprise with hundreds
  of agents and thousands of tools: What Part 1 does Why it stops scaling What Part 2 does instead The
  agent holds each MCP server’s runtime ARN and calls it directly N agents against M servers is a wiring
  matrix, and every new tool touches every agent that needs it Agents reach one Gateway endpoint, and
  the Gateway holds the target registry The agent’s role holds'
first_seen: '2026-11-07T01:57:08Z'
last_seen: '2026-11-07T01:57:08Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-2/
  seen_at: '2026-11-07T01:57:08Z'
  metrics: {}
  kind: news
---

# Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 2

In Part 1 , you built a task agent on Amazon Bedrock AgentCore , a platform to build, connect, and optimize agents at scale, with any framework or model. The agent runs on Amazon Bedrock AgentCore runtime, a capability of Amazon Bedrock AgentCore, and acts for signed-in users through Okta Cross App Access (XAA). Okta decided which agent might act for which user, and Amazon Bedrock AgentCore Identity, a capability of Amazon Bedrock AgentCore, redeemed Okta’s grant inside the agent. That proves the governance mechanism, and it runs on a deliberately small topology: one agent, two Model Context Protocol (MCP) servers, and the authorization check written into each server. The mechanism scales. The topology doesn’t. Three things that are fine for one agent and two tools become the work in an enterprise with hundreds of agents and thousands of tools: What Part 1 does Why it stops scaling What Part 2 does instead The agent holds each MCP server’s runtime ARN and calls it directly N agents against M servers is a wiring matrix, and every new tool touches every agent that needs it Agents reach one Gateway endpoint, and the Gateway holds the target registry The agent’s role holds

## 笔记


