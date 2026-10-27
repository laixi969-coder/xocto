---
slug: build-agentic-retrieval-on-a-managed-amazon-bedrock-knowledg
name: Build agentic retrieval on a Managed Amazon Bedrock Knowledge Base with CDK
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
url: https://aws.amazon.com/blogs/machine-learning/build-agentic-retrieval-on-a-managed-amazon-bedrock-knowledge-base-with-cdk/
canonical_url: https://aws.amazon.com/blogs/machine-learning/build-agentic-retrieval-on-a-managed-amazon-bedrock-knowledge-base-with-cdk
summary: 'This post builds enterprise agentic retrieval on a Managed Amazon Bedrock Knowledge Base with
  the AWS Cloud Development Kit (AWS CDK). To see why that’s worth building, it helps to start with where
  ordinary Retrieval Augmented Generation (RAG) breaks down. Most RAG systems start the same way: they
  embed the question, fetch the nearest chunks from one index, hand them to a model, and return the answer.
  One retrieval, one generation. For a large class of questions that’s the right design, and there’s no
  reason to build anything more complicated. It fails in a recognizable way. Ask a question whose answer
  spans two corpora, and a single retrieval returns half of what the model needs, which is worse than
  returning nothing, because the answer comes back fluent and incomplete. Ask a question where the right
  source depends on the question , and a single index has no mechanism to choose. Ask a question that
  needs a second look at the corpus after seeing the first result, and there is nowhere for that second
  look to happen. Enterprise agentic retrieval answers all three by putting a reasoning agent in the loop.
  The agent decides whether to retrieve, which knowledge base to'
first_seen: '2026-10-27T01:30:17Z'
last_seen: '2026-10-27T01:30:17Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/build-agentic-retrieval-on-a-managed-amazon-bedrock-knowledge-base-with-cdk/
  seen_at: '2026-10-27T01:30:17Z'
  metrics: {}
  kind: news
---

# Build agentic retrieval on a Managed Amazon Bedrock Knowledge Base with CDK

This post builds enterprise agentic retrieval on a Managed Amazon Bedrock Knowledge Base with the AWS Cloud Development Kit (AWS CDK). To see why that’s worth building, it helps to start with where ordinary Retrieval Augmented Generation (RAG) breaks down. Most RAG systems start the same way: they embed the question, fetch the nearest chunks from one index, hand them to a model, and return the answer. One retrieval, one generation. For a large class of questions that’s the right design, and there’s no reason to build anything more complicated. It fails in a recognizable way. Ask a question whose answer spans two corpora, and a single retrieval returns half of what the model needs, which is worse than returning nothing, because the answer comes back fluent and incomplete. Ask a question where the right source depends on the question , and a single index has no mechanism to choose. Ask a question that needs a second look at the corpus after seeing the first result, and there is nowhere for that second look to happen. Enterprise agentic retrieval answers all three by putting a reasoning agent in the loop. The agent decides whether to retrieve, which knowledge base to

## 笔记


