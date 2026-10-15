---
slug: generate-presentations-with-amazon-bedrock-agentcore
name: Generate presentations with Amazon Bedrock AgentCore
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
url: https://aws.amazon.com/blogs/machine-learning/generate-presentations-with-amazon-bedrock-agentcore/
canonical_url: https://aws.amazon.com/blogs/machine-learning/generate-presentations-with-amazon-bedrock-agentcore
summary: A financial services team spends significant time each week manually creating client PowerPoint
  presentations from quarterly reports, compliance documents, and market analyses. Each presentation requires
  reading hundreds of pages, extracting key data points, structuring slides, and generating supporting
  visuals. This post walks you through building an AI agent system using Amazon Bedrock AgentCore that
  automates this workflow, completing in under 90 seconds in our internal testing. This approach reduces
  presentation creation time while grounding content in source documents. The solution deploys a supervisor
  agent on AgentCore runtime, a capability of Amazon Bedrock AgentCore, using the Strands Agents framework
  to orchestrate document generation and summarization tools. Anthropic Claude Sonnet 4.6 (available on
  Amazon Bedrock) handles content creation, Amazon Titan Text Embeddings v2 powers vector search, and
  Stability AI Stable Image Inpaint (available on Amazon Bedrock) generates slide images. This post includes
  a public repository with the code assets. Solution overview The solution deploys a single supervisor
  agent on Amazon Bedrock AgentCore runtime that selects between document generation and summarization
  tools based on user requests. A Retrieval Augmented Generation (RAG) pipeline uses Amazon OpenSearch
  Serverless for vector storage and semantic search across multimodal content. The solution includes a
  REST API built with
first_seen: '2026-10-15T00:32:31Z'
last_seen: '2026-10-15T00:32:31Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/generate-presentations-with-amazon-bedrock-agentcore/
  seen_at: '2026-10-15T00:32:31Z'
  metrics: {}
  kind: news
---

# Generate presentations with Amazon Bedrock AgentCore

A financial services team spends significant time each week manually creating client PowerPoint presentations from quarterly reports, compliance documents, and market analyses. Each presentation requires reading hundreds of pages, extracting key data points, structuring slides, and generating supporting visuals. This post walks you through building an AI agent system using Amazon Bedrock AgentCore that automates this workflow, completing in under 90 seconds in our internal testing. This approach reduces presentation creation time while grounding content in source documents. The solution deploys a supervisor agent on AgentCore runtime, a capability of Amazon Bedrock AgentCore, using the Strands Agents framework to orchestrate document generation and summarization tools. Anthropic Claude Sonnet 4.6 (available on Amazon Bedrock) handles content creation, Amazon Titan Text Embeddings v2 powers vector search, and Stability AI Stable Image Inpaint (available on Amazon Bedrock) generates slide images. This post includes a public repository with the code assets. Solution overview The solution deploys a single supervisor agent on Amazon Bedrock AgentCore runtime that selects between document generation and summarization tools based on user requests. A Retrieval Augmented Generation (RAG) pipeline uses Amazon OpenSearch Serverless for vector storage and semantic search across multimodal content. The solution includes a REST API built with

## 笔记


