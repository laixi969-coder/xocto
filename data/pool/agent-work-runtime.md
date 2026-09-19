---
slug: agent-work-runtime
name: agent-work-runtime
builder: originoneai
category: 基础层
summary_zh: 开发者在构建需要跑很久的 AI agent 时接入它，原本要自己维护会话状态、上下文裁剪和中断恢复；它接收 agent 的运行状态与上下文材料，保存持久工作状态并只保留最小上下文，让长任务能接着跑。具体接口、部署方式与交付结果仍待核验。
inspiration: 趋势是 agent 从一次性问答走向长时任务，状态与上下文管理成为独立一层。切入可放在需要长流程的垂直场景（如批量单据处理、持续监控）里做托管运行时，按任务时长或并发收费；目前只有开源仓库，付费路径未披露。
summary_en: Developers adopt it when building AI agents that must run for a long time, where they previously
  maintained session state, context trimming and crash recovery themselves; it takes the agent's runtime
  state and context material, persists work state and keeps only minimal context so long tasks can continue.
  Concrete interfaces, deployment and delivered results still need verification.
inspiration_en: The trend is agents moving from one-shot Q&A to long-running tasks, making state and context
  management its own layer. An entry point is a managed runtime for long-flow vertical scenarios such
  as batch document processing or continuous monitoring, charged by task duration or concurrency; today
  only an open-source repository exists and the payment path is undisclosed.
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- AI 应用后端开发者
- agent 平台工程师
jobs_en:
- AI application backend developers
- Agent platform engineers
regions: []
regions_en: []
open_source: true
url: https://github.com/originoneai/agent-work-runtime
canonical_url: https://github.com/originoneai/agent-work-runtime
summary: Persistent work state and minimal context for long-running AI agents.
first_seen: '2026-09-07T16:09:21Z'
last_seen: '2026-09-19T00:21:19Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/originoneai/agent-work-runtime
  seen_at: '2026-09-19T00:21:19Z'
  metrics:
    stars: 130
    forks: 18
    open_issues: 2
  kind: product
---

# agent-work-runtime

Persistent work state and minimal context for long-running AI agents.

## 笔记


