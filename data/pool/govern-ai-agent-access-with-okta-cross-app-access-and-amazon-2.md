---
slug: govern-ai-agent-access-with-okta-cross-app-access-and-amazon-2
name: Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 1
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
url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-1/
canonical_url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-1
summary: 'An AI agent that updates a ticket or reads a customer record acts for a person, inside applications
  that person can reach. Your identity team then has to answer a question that per-app OAuth consent and
  shared service accounts leave open: which agent might act for which user in which application, and how
  you stop it. Okta Cross App Access (XAA) answers it in your identity provider (IdP). You register the
  agent in Okta, an administrator approves the applications it might reach, and Okta evaluates policy
  each time the agent asks to act for a user. In our tests, after an administrator removed a user’s assignment
  to the agent, Okta refused the agent’s new requests for that user within about 1 second, and tokens
  already issued expired within 5 minutes. Amazon Bedrock AgentCore is a platform to build, connect, and
  optimize agents at scale, with any framework or model. This solution uses two of its capabilities to
  carry out Okta’s decision on AWS. Amazon Bedrock AgentCore runtime, a capability of Amazon Bedrock AgentCore,
  validates Okta’s grant. Amazon Bedrock AgentCore Identity, a capability of Amazon Bedrock AgentCore,
  redeems it for a short-lived access token with credentials your agent code doesn’t see,'
first_seen: '2026-11-07T01:57:08Z'
last_seen: '2026-11-07T01:57:08Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-1/
  seen_at: '2026-11-07T01:57:08Z'
  metrics: {}
  kind: news
---

# Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 1

An AI agent that updates a ticket or reads a customer record acts for a person, inside applications that person can reach. Your identity team then has to answer a question that per-app OAuth consent and shared service accounts leave open: which agent might act for which user in which application, and how you stop it. Okta Cross App Access (XAA) answers it in your identity provider (IdP). You register the agent in Okta, an administrator approves the applications it might reach, and Okta evaluates policy each time the agent asks to act for a user. In our tests, after an administrator removed a user’s assignment to the agent, Okta refused the agent’s new requests for that user within about 1 second, and tokens already issued expired within 5 minutes. Amazon Bedrock AgentCore is a platform to build, connect, and optimize agents at scale, with any framework or model. This solution uses two of its capabilities to carry out Okta’s decision on AWS. Amazon Bedrock AgentCore runtime, a capability of Amazon Bedrock AgentCore, validates Okta’s grant. Amazon Bedrock AgentCore Identity, a capability of Amazon Bedrock AgentCore, redeems it for a short-lived access token with credentials your agent code doesn’t see,

## 笔记


