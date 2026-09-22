---
slug: how-benchling-secured-multi-tenant-ai-agents-with-amazon-bed
name: Benchling
builder: ''
category: AI + 开发
summary_zh: 生命科学研发团队在平台上让 AI 智能体生成并运行科学计算代码时，需要处理多租户隔离与数据外泄风险；Benchling 通过 VPC 模式代码解释器加 DNS 防火墙与端点策略执行这些代码，最终交付的是受控环境下的分析结果，具体租户规模与人工审核环节仍待核验。
inspiration: 趋势是 AI 智能体开始进入受监管行业的研发流程，安全与隔离成为能否落地的关键环节。切入可考虑为生命科学、医疗等强合规行业提供智能体执行沙箱与审计层，按合规交付收费，而不是再做一个通用代码解释器。
summary_en: Life sciences R&D teams letting AI agents generate and run scientific computing code on a
  platform must handle multi-tenant isolation and data exfiltration risk; Benchling executes that code
  through a VPC-mode code interpreter plus DNS firewall and endpoint policies, delivering analysis results
  in a controlled environment, while tenant scale and human review steps still need verification.
inspiration_en: The trend is AI agents entering R&D workflows in regulated industries, where security
  and isolation decide whether deployment happens. A possible entry is an agent execution sandbox and
  audit layer for highly regulated sectors such as life sciences and healthcare, charged per compliance
  delivery, rather than another general code interpreter.
priority_review: false
project_type: ai_transformation
industries:
- 生命科学
- 生物医药研发
industries_en:
- Life Sciences
- Biopharma R&D
jobs:
- 生物信息工程师
- 研发平台安全工程师
jobs_en:
- Bioinformatics Engineer
- R&D Platform Security Engineer
regions:
- 美国
regions_en:
- United States
open_source: false
url: https://aws.amazon.com/blogs/machine-learning/how-benchling-secured-multi-tenant-ai-agents-with-amazon-bedrock-agentcore/
canonical_url: https://aws.amazon.com/blogs/machine-learning/how-benchling-secured-multi-tenant-ai-agents-with-amazon-bedrock-agentcore
summary: Learn how Benchling built a defense-in-depth security architecture to run untrusted, AI agent-generated
  scientific code across thousands of life sciences tenants using Amazon Bedrock AgentCore Code Interpreter
  in VPC mode, combined with Amazon Route 53 Resolver DNS Firewall and VPC endpoint policies to block
  data exfiltration, including through DNS.
first_seen: '2026-09-21T16:27:34Z'
last_seen: '2026-09-22T00:50:50Z'
status: watching
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/how-benchling-secured-multi-tenant-ai-agents-with-amazon-bedrock-agentcore/
  seen_at: '2026-09-22T00:50:50Z'
  metrics: {}
  kind: news
---

# Benchling

Learn how Benchling built a defense-in-depth security architecture to run untrusted, AI agent-generated scientific code across thousands of life sciences tenants using Amazon Bedrock AgentCore Code Interpreter in VPC mode, combined with Amazon Route 53 Resolver DNS Firewall and VPC endpoint policies to block data exfiltration, including through DNS.

## 笔记


