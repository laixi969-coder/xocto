---
slug: agent-jev
name: AgentJev
builder: malevrigns
category: 基础层
summary_zh: 当 agent 跑在多步流程里，开发者需要在每一步根据当前的 diff、trace 或日志判断该继续、重试还是升级处理。AgentJev 宣称把这类非结构化状态和结构化问题一起输入一个
  0.6B 模型，在一次约 50 毫秒的前向计算中返回概率分布，不做逐 token 生成，从而把判断动作压缩成一次快速打分；概率如何被消费、阈值由谁设定、误判如何处理，公开材料未说明，具体流程与交付仍待核验。
inspiration: 趋势是 agent 的瓶颈从“生成一句话”转向“在几十毫秒内决定下一步走哪条分支”，判断本身开始被做成独立的小模型而不是塞进大模型对话。切入可以放在对延迟和成本敏感的自动化环节，例如客服工单分流、订单异常判定、内容审核的二次复核，把“继续/重试/升级”的概率阈值做成按调用量计费的判断服务；目前公开材料不足以判断它是否已进入这类生产流程。
summary_en: When an agent runs a multi-step flow, developers must decide at each step whether to continue,
  retry or escalate based on the current diff, trace or log. AgentJev claims to feed such unstructured
  state together with structured questions into a 0.6B model that returns a probability distribution in
  a single roughly 50 ms forward pass without token-by-token generation, compressing the decision into
  one fast scoring call; how the probabilities are consumed, who sets thresholds and how misjudgements
  are handled are not described, so the concrete flow and deliverable remain unverified.
inspiration_en: The trend is that the agent bottleneck is shifting from generating a sentence to deciding
  within tens of milliseconds which branch to take, and the decision itself is becoming a small dedicated
  model rather than a large-model conversation. An entry point is latency- and cost-sensitive automation,
  such as routing support tickets, judging order anomalies or second-pass content review, turning continue/retry/escalate
  probability thresholds into a decision service billed per call; the public material is not enough to
  tell whether it has entered such production flows.
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs:
- agent 开发者在编排流程中判断下一步动作是否继续、重试或升级
jobs_en:
- Agent developers deciding inside an orchestration flow whether to continue, retry or escalate the next
  action
regions: []
regions_en: []
open_source: true
url: https://github.com/malevrigns/agent-jev
canonical_url: https://github.com/malevrigns/agent-jev
summary: 'AgentJev-0.6B - a fast ''System One'' decision model for AI Agents: feed it any unstructured
  state (diffs, traces, logs) and structured questions, get calibrated probability distributions back
  in one ~50ms forward pass. Zero output-token decoding.'
first_seen: '2026-09-21T16:24:42Z'
last_seen: '2026-09-24T00:30:54Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/malevrigns/agent-jev
  seen_at: '2026-09-24T00:30:54Z'
  metrics:
    stars: 267
    forks: 24
    open_issues: 4
  kind: product
---

# AgentJev

AgentJev-0.6B - a fast 'System One' decision model for AI Agents: feed it any unstructured state (diffs, traces, logs) and structured questions, get calibrated probability distributions back in one ~50ms forward pass. Zero output-token decoding.

## 笔记


