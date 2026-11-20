---
slug: protect-agent-tool-calls-with-skyflow-and-amazon-bedrock-age
name: Protect agent tool calls with Skyflow and Amazon Bedrock AgentCore Gateway
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
url: https://aws.amazon.com/blogs/machine-learning/protect-agent-tool-calls-with-skyflow-and-amazon-bedrock-agentcore-gateway/
canonical_url: https://aws.amazon.com/blogs/machine-learning/protect-agent-tool-calls-with-skyflow-and-amazon-bedrock-agentcore-gateway
summary: 'In this post, we show how Skyflow and Amazon Bedrock AgentCore Gateway keep sensitive data out
  of the tools your AI agents call, and out of the model context those tools feed. We add Skyflow Detect
  to Amazon Bedrock AgentCore Gateway as a request and response interceptor . The Skyflow interceptor
  de-identifies data before it reaches a tool, restores it before the agent reads the result, and replaces
  documents with clean copies before the agent opens them. Your agents and tools don’t change. Skyflow
  is available in AWS Marketplace, and the interceptor is open source on GitHub. Agents act through tools,
  and tools move data Agents have moved from answering questions to taking action, and they take action
  through tools: Model Context Protocol (MCP) servers, SaaS APIs, document stores, and web search. Every
  agent tool call is a data flow. Most enterprise controls cover what goes into and comes out of the model.
  Far fewer cover what an agent sends to its tools or what those tools send back. That gap shows up in
  three ways: Sensitive data leaves through tool arguments. The model writes the arguments from everything
  in its context, including details the tool doesn’t need. Ask an'
first_seen: '2026-11-20T03:16:25Z'
last_seen: '2026-11-20T03:16:25Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/protect-agent-tool-calls-with-skyflow-and-amazon-bedrock-agentcore-gateway/
  seen_at: '2026-11-20T03:16:25Z'
  metrics: {}
  kind: news
---

# Protect agent tool calls with Skyflow and Amazon Bedrock AgentCore Gateway

In this post, we show how Skyflow and Amazon Bedrock AgentCore Gateway keep sensitive data out of the tools your AI agents call, and out of the model context those tools feed. We add Skyflow Detect to Amazon Bedrock AgentCore Gateway as a request and response interceptor . The Skyflow interceptor de-identifies data before it reaches a tool, restores it before the agent reads the result, and replaces documents with clean copies before the agent opens them. Your agents and tools don’t change. Skyflow is available in AWS Marketplace, and the interceptor is open source on GitHub. Agents act through tools, and tools move data Agents have moved from answering questions to taking action, and they take action through tools: Model Context Protocol (MCP) servers, SaaS APIs, document stores, and web search. Every agent tool call is a data flow. Most enterprise controls cover what goes into and comes out of the model. Far fewer cover what an agent sends to its tools or what those tools send back. That gap shows up in three ways: Sensitive data leaves through tool arguments. The model writes the arguments from everything in its context, including details the tool doesn’t need. Ask an

## 笔记


