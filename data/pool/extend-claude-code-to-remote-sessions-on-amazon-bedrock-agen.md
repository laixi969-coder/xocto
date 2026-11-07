---
slug: extend-claude-code-to-remote-sessions-on-amazon-bedrock-agen
name: Extend Claude Code to remote sessions on Amazon Bedrock AgentCore with security controls
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
url: https://aws.amazon.com/blogs/machine-learning/extend-claude-code-to-remote-sessions-on-amazon-bedrock-agentcore-with-security-controls/
canonical_url: https://aws.amazon.com/blogs/machine-learning/extend-claude-code-to-remote-sessions-on-amazon-bedrock-agentcore-with-security-controls
summary: 'You might already run Claude Code locally on your laptop, backed by Amazon Bedrock. This post
  shows how to go a step further: run it as a remote agent on Amazon Bedrock AgentCore, a platform to
  build, connect, and optimize agents at scale, with any framework or model. The sample uses AgentCore
  runtime, a capability of Amazon Bedrock AgentCore, so every task runs in its own isolated session inside
  your AWS account. You offload a coding task, close the laptop, and come back to the result. We first
  discuss why teams choose Amazon Bedrock for Claude Code and highlight a few key security characteristics.
  Then, we discuss the remote agent architecture and walk through an accompanying sample, sample-remote-coding-agent
  , that implements it. The sample runs each task in its own AgentCore runtime session and returns a GitHub
  pull request for you to review and merge. Along the way, we show how the Amazon Bedrock data controls
  stay intact when a task runs remotely. Why customers run Claude Code on Amazon Bedrock Customers choose
  Amazon Bedrock as Claude Code’s model provider for many reasons. These include billing and credits through
  their existing AWS account with no per-seat licenses, audit logging in'
first_seen: '2026-11-07T01:57:08Z'
last_seen: '2026-11-07T01:57:08Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/extend-claude-code-to-remote-sessions-on-amazon-bedrock-agentcore-with-security-controls/
  seen_at: '2026-11-07T01:57:08Z'
  metrics: {}
  kind: news
---

# Extend Claude Code to remote sessions on Amazon Bedrock AgentCore with security controls

You might already run Claude Code locally on your laptop, backed by Amazon Bedrock. This post shows how to go a step further: run it as a remote agent on Amazon Bedrock AgentCore, a platform to build, connect, and optimize agents at scale, with any framework or model. The sample uses AgentCore runtime, a capability of Amazon Bedrock AgentCore, so every task runs in its own isolated session inside your AWS account. You offload a coding task, close the laptop, and come back to the result. We first discuss why teams choose Amazon Bedrock for Claude Code and highlight a few key security characteristics. Then, we discuss the remote agent architecture and walk through an accompanying sample, sample-remote-coding-agent , that implements it. The sample runs each task in its own AgentCore runtime session and returns a GitHub pull request for you to review and merge. Along the way, we show how the Amazon Bedrock data controls stay intact when a task runs remotely. Why customers run Claude Code on Amazon Bedrock Customers choose Amazon Bedrock as Claude Code’s model provider for many reasons. These include billing and credits through their existing AWS account with no per-seat licenses, audit logging in

## 笔记


