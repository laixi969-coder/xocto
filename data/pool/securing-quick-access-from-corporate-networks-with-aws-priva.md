---
slug: securing-quick-access-from-corporate-networks-with-aws-priva
name: Securing Quick access from corporate networks with AWS PrivateLink
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
url: https://aws.amazon.com/blogs/machine-learning/securing-quick-access-from-corporate-networks-with-aws-privatelink/
canonical_url: https://aws.amazon.com/blogs/machine-learning/securing-quick-access-from-corporate-networks-with-aws-privatelink
summary: When enterprise data sits behind a corporate firewall or in a private on-premises data center,
  there’s no direct network path from AWS, even though the AI agents and dashboards in Amazon Quick can
  query virtually any data source. Administrators must make sure their sensitive enterprise data isn’t
  exposed to the public internet while being accessible for AI-driven insights and actions. For many enterprises,
  routing traffic over the public internet introduces unacceptable risk. Regulatory frameworks such as
  HIPAA, FedRAMP, and PCI-DSS often mandate that sensitive data remain within controlled network boundaries.
  Even where compliance isn’t the primary driver, exposing internal data paths increases the attack surface,
  complicates audit trails and introduces variable latency that can degrade the user experience. This
  walkthrough shows you how to connect on-premises data sources to Amazon Quick privately, without traffic
  traversing the public internet. It assumes you already have AWS Direct Connect or an AWS Site-to-Site
  VPN linking your on-premises environment to your virtual private cloud (VPC). From that foundation,
  we configure VPC endpoints powered by AWS PrivateLink so that Quick can reach your private resources
  over the AWS backbone, then layer security groups and VPC endpoint policies for defense in depth. By
  the end, you
first_seen: '2026-10-22T00:42:46Z'
last_seen: '2026-10-22T00:42:46Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/securing-quick-access-from-corporate-networks-with-aws-privatelink/
  seen_at: '2026-10-22T00:42:46Z'
  metrics: {}
  kind: news
---

# Securing Quick access from corporate networks with AWS PrivateLink

When enterprise data sits behind a corporate firewall or in a private on-premises data center, there’s no direct network path from AWS, even though the AI agents and dashboards in Amazon Quick can query virtually any data source. Administrators must make sure their sensitive enterprise data isn’t exposed to the public internet while being accessible for AI-driven insights and actions. For many enterprises, routing traffic over the public internet introduces unacceptable risk. Regulatory frameworks such as HIPAA, FedRAMP, and PCI-DSS often mandate that sensitive data remain within controlled network boundaries. Even where compliance isn’t the primary driver, exposing internal data paths increases the attack surface, complicates audit trails and introduces variable latency that can degrade the user experience. This walkthrough shows you how to connect on-premises data sources to Amazon Quick privately, without traffic traversing the public internet. It assumes you already have AWS Direct Connect or an AWS Site-to-Site VPN linking your on-premises environment to your virtual private cloud (VPC). From that foundation, we configure VPC endpoints powered by AWS PrivateLink so that Quick can reach your private resources over the AWS backbone, then layer security groups and VPC endpoint policies for defense in depth. By the end, you

## 笔记


