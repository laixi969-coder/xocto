---
slug: spinifex
name: Spinifex
builder: toddyholiday
category: 基础层
summary_zh: 基础设施工程师在数据不能出机房或要压云成本时，把现有的 AWS 脚本和配置交给 Spinifex，由它在自有硬件上提供 EC2/S3/IAM/EKS 兼容服务，命令行工具保持不变；交付物是本地可运行的兼容云环境，具体兼容程度与运维成本仍待核验。
inspiration: 趋势：云成本与数据合规压力让“自有硬件跑云 API”从极客玩具变成可选项，兼容层比重新学一套私有云更省迁移成本。切入：面向有合规要求的中型机构（医院、律所、制造厂）做托管式私有云兼容层，按节点或机柜收费，把迁移与运维一起包掉。
summary_en: When data cannot leave the premises or cloud cost must be cut, infrastructure engineers point
  existing AWS scripts and configs at Spinifex, which provides EC2/S3/IAM/EKS-compatible services on their
  own hardware while keeping CLI tooling unchanged; the deliverable is a locally runnable compatible cloud
  environment, and the degree of compatibility and operational cost still need verification.
inspiration_en: 'Trend: cloud cost and data-compliance pressure are turning ''run cloud APIs on your own
  hardware'' from a hobbyist toy into an option, and a compatibility layer costs less migration effort
  than learning a private cloud. Entry: offer a managed private-cloud compatibility layer to mid-sized
  regulated organizations such as hospitals, law firms and manufacturers, charged per node or rack, bundling
  migration and operations.'
priority_review: false
project_type: open_source
industries:
- 云计算
- 软件开发
industries_en:
- Cloud Computing
- Software Development
jobs:
- 基础设施工程师在需要数据不出机房或控制云成本时，处理既有 AWS 脚本与配置，要在自有硬件上跑起兼容服务而不改命令行工具
jobs_en:
- Infrastructure engineers needing data to stay on-premises or to control cloud cost handle existing AWS
  scripts and configs, and must run compatible services on their own hardware without changing CLI tooling
regions:
- 澳大利亚
regions_en:
- Australia
open_source: true
url: https://github.com/mulgadc/spinifex
canonical_url: https://github.com/mulgadc/spinifex
summary: run EC2/S3/IAM/EKS on your own hardware, AWS CLI unchanged
first_seen: '2026-08-26T06:23:18Z'
last_seen: '2026-09-10T05:13:24Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://github.com/mulgadc/spinifex
  seen_at: '2026-08-27T03:18:34Z'
  metrics:
    points: 5
    comments: 0
  kind: product
- source: hackernews
  url: https://mulgadc.com/blog/spinifex-1-19-0-release
  seen_at: '2026-09-10T05:13:24Z'
  metrics:
    points: 7
    comments: 7
  kind: news
---

# Spinifex

run EC2/S3/IAM/EKS on your own hardware, AWS CLI unchanged

## 笔记


