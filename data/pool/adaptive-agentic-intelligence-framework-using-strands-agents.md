---
slug: adaptive-agentic-intelligence-framework-using-strands-agents
name: Adaptive agentic intelligence framework using Strands Agents
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
url: https://aws.amazon.com/blogs/machine-learning/adaptive-agentic-intelligence-framework-using-strands-agents/
canonical_url: https://aws.amazon.com/blogs/machine-learning/adaptive-agentic-intelligence-framework-using-strands-agents
summary: 'Organizations building AI agents face a common challenge: Every request, whether a routine status
  check or complex analysis, typically gets routed to a single large, expensive model. This one-size-fits-all
  approach can drive up API costs, introduce unpredictable latency, and remove the possibility of offline
  operation. Even routine queries that could resolve locally end up requiring a full network round-trip
  to a cloud-hosted large language model (LLM). The Adaptive Agentic Intelligence Framework (AAIF), built
  with Strands Agents, takes a different approach. Instead of routing all requests to a single large model,
  AAIF uses small language models (SLMs) to handle routine tasks locally. More complex requests are routed
  to cloud-hosted models through Amazon Bedrock . This approach builds on the research position from Belcak
  et al. at NVIDIA . They argue that small language models are “sufficiently powerful, inherently more
  suitable, and necessarily more economical for many invocations in agentic systems.” Built on Strands
  Agents, the framework demonstrates how intelligent model orchestration can help reduce costs while maintaining
  low latency for local operations. In this post, we walk through the key components of AAIF using Strands
  Agents with local SLMs through Ollama and cloud models through Amazon Bedrock. We use an Internet'
first_seen: '2026-10-22T00:42:46Z'
last_seen: '2026-10-22T00:42:46Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/adaptive-agentic-intelligence-framework-using-strands-agents/
  seen_at: '2026-10-22T00:42:46Z'
  metrics: {}
  kind: news
---

# Adaptive agentic intelligence framework using Strands Agents

Organizations building AI agents face a common challenge: Every request, whether a routine status check or complex analysis, typically gets routed to a single large, expensive model. This one-size-fits-all approach can drive up API costs, introduce unpredictable latency, and remove the possibility of offline operation. Even routine queries that could resolve locally end up requiring a full network round-trip to a cloud-hosted large language model (LLM). The Adaptive Agentic Intelligence Framework (AAIF), built with Strands Agents, takes a different approach. Instead of routing all requests to a single large model, AAIF uses small language models (SLMs) to handle routine tasks locally. More complex requests are routed to cloud-hosted models through Amazon Bedrock . This approach builds on the research position from Belcak et al. at NVIDIA . They argue that small language models are “sufficiently powerful, inherently more suitable, and necessarily more economical for many invocations in agentic systems.” Built on Strands Agents, the framework demonstrates how intelligent model orchestration can help reduce costs while maintaining low latency for local operations. In this post, we walk through the key components of AAIF using Strands Agents with local SLMs through Ollama and cloud models through Amazon Bedrock. We use an Internet

## 笔记


