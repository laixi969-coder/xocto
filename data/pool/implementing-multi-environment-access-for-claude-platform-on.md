---
slug: implementing-multi-environment-access-for-claude-platform-on
name: Claude Platform on AWS
builder: ''
category: ''
summary_zh: 这是 AWS 官方发布的一篇配置指南，面向在 AWS 上调用 Claude 的企业工程团队：他们需要让不同账户、不同开发者、不同外部环境共用一份订阅，同时保持权限隔离。指南给出的做法是用跨账户
  SigV4、工作区级 API key 和 OIDC 联邦分别对接三类调用方，最终交付的是一套可落地的访问控制配置，而非新产品。
inspiration: ''
summary_en: 'This is an AWS official configuration guide for enterprise engineering teams calling Claude
  on AWS: they need different accounts, developers, and external environments to share one subscription
  while keeping permissions isolated. The approach uses cross-account SigV4, workspace-scoped API keys,
  and OIDC federation for the three caller types, delivering an access-control configuration rather than
  a new product.'
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
url: https://aws.amazon.com/blogs/machine-learning/implementing-multi-environment-access-for-claude-platform-on-aws/
canonical_url: https://aws.amazon.com/blogs/machine-learning/implementing-multi-environment-access-for-claude-platform-on-aws
summary: 'Learn how to configure secure, multi-environment access to Claude Platform on AWS from a single
  subscription: cross-account SigV4 for AWS workloads, workspace-scoped API keys for developers, and OIDC
  federation for external environments, with workspace-level isolation in a dedicated AI Services account.'
first_seen: '2026-10-01T16:32:23Z'
last_seen: '2026-10-02T01:42:13Z'
status: market_context
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/implementing-multi-environment-access-for-claude-platform-on-aws/
  seen_at: '2026-10-02T01:42:13Z'
  metrics: {}
  kind: news
---

# Claude Platform on AWS

Learn how to configure secure, multi-environment access to Claude Platform on AWS from a single subscription: cross-account SigV4 for AWS workloads, workspace-scoped API keys for developers, and OIDC federation for external environments, with workspace-level isolation in a dedicated AI Services account.

## 笔记


