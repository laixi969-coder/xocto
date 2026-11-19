---
slug: connect-amazon-bedrock-agentcore-gateway-to-private-apis-in
name: Connect Amazon Bedrock AgentCore Gateway to private APIs in a hub-and-spoke network with centralized
  inspection
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
url: https://aws.amazon.com/blogs/machine-learning/connect-amazon-bedrock-agentcore-gateway-to-private-apis-in-a-hub-and-spoke-network-with-centralized-inspection/
canonical_url: https://aws.amazon.com/blogs/machine-learning/connect-amazon-bedrock-agentcore-gateway-to-private-apis-in-a-hub-and-spoke-network-with-centralized-inspection
summary: In many enterprises, a central network team owns every virtual private cloud (VPC) and subnet,
  and every flow between VPCs must pass a central firewall in both directions. Agents that call internal
  REST APIs and Model Context Protocol (MCP) servers through Amazon Bedrock AgentCore Gateway , a capability
  of Amazon Bedrock AgentCore, must meet the same two requirements. Amazon Bedrock AgentCore is a platform
  to build, connect, and optimize agents at scale, with any framework or model. This post shows a pattern
  that meets both requirements. The network team keeps ownership of every subnet, and traffic between
  the Gateway and your private APIs and MCP servers crosses the central firewall in both directions. It
  covers where to place the Amazon VPC Lattice resource gateway that the Gateway uses to reach private
  targets. It also covers who owns each piece, six configuration decisions, and the checks that confirm
  the pattern works. We built and tested the pattern in the US East (N. Virginia) AWS Region ( us-east-1
  ), in a lab with three member accounts and a management account in AWS Organizations. The AWS CloudFormation
  templates, test scripts, test evidence, and reference material (address plan, full validation checks,
  troubleshooting, quotas) are
first_seen: '2026-11-19T03:28:37Z'
last_seen: '2026-11-19T03:28:37Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/connect-amazon-bedrock-agentcore-gateway-to-private-apis-in-a-hub-and-spoke-network-with-centralized-inspection/
  seen_at: '2026-11-19T03:28:37Z'
  metrics: {}
  kind: news
---

# Connect Amazon Bedrock AgentCore Gateway to private APIs in a hub-and-spoke network with centralized inspection

In many enterprises, a central network team owns every virtual private cloud (VPC) and subnet, and every flow between VPCs must pass a central firewall in both directions. Agents that call internal REST APIs and Model Context Protocol (MCP) servers through Amazon Bedrock AgentCore Gateway , a capability of Amazon Bedrock AgentCore, must meet the same two requirements. Amazon Bedrock AgentCore is a platform to build, connect, and optimize agents at scale, with any framework or model. This post shows a pattern that meets both requirements. The network team keeps ownership of every subnet, and traffic between the Gateway and your private APIs and MCP servers crosses the central firewall in both directions. It covers where to place the Amazon VPC Lattice resource gateway that the Gateway uses to reach private targets. It also covers who owns each piece, six configuration decisions, and the checks that confirm the pattern works. We built and tested the pattern in the US East (N. Virginia) AWS Region ( us-east-1 ), in a lab with three member accounts and a management account in AWS Organizations. The AWS CloudFormation templates, test scripts, test evidence, and reference material (address plan, full validation checks, troubleshooting, quotas) are

## 笔记


