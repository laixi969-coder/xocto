---
slug: mod-earshot
name: mod_earshot
builder: wiringai
category: 基础层
summary_zh: 呼叫中心运维工程师在改造 FreeSWITCH 电话系统时，打开这个模块，把实时通话音频通过 WebSocket 双向传给 AI 语音代理，再把代理的语音回放到通话中。它交付的是一个可接入现有电话交换机的双向音频通道，具体延迟、并发与稳定性仍待核验。
inspiration: 趋势是语音 AI 正从独立通话应用下沉到既有电话交换机的音频层，谁掌握这一层谁就掌握通话入口。切入可从呼叫中心、外呼团队或电信集成商入手，卖的是把现有 PBX 接上语音代理的部署与运维，而不是再做一个语音助手；开源模块本身难直接收费，可考虑托管与合规录音等配套。
summary_en: Call-center operations engineers modifying a FreeSWITCH phone system open this module to stream
  live call audio over WebSocket to an AI voice agent and play the agent's voice back into the call. It
  delivers a full-duplex audio channel into an existing phone switch; latency, concurrency and stability
  remain unverified.
inspiration_en: The trend is voice AI sinking from standalone calling apps into the audio layer of existing
  phone switches, and whoever owns that layer owns the call entry point. A wedge is call centers, outbound
  teams or telecom integrators, selling deployment and operations that connect existing PBX systems to
  voice agents rather than another voice assistant; the open-source module itself is hard to charge for,
  so hosting and compliant recording are the plausible paid layers.
priority_review: false
project_type: open_source
industries:
- 电信与呼叫中心
- 客户服务
industries_en:
- Telecom and Call Centers
- Customer Service
jobs:
- 呼叫中心运维工程师在部署或改造 FreeSWITCH 电话系统时，把实时通话音频接入 AI 语音代理并回放其语音
jobs_en:
- Call-center operations engineers wiring live call audio into AI voice agents and playing their voice
  back when deploying or modifying a FreeSWITCH phone system
regions: []
regions_en: []
open_source: true
url: https://github.com/wiringai/mod_earshot
canonical_url: https://github.com/wiringai/mod_earshot
summary: FreeSWITCH module that streams live call audio to AI voice agents over WebSocket and plays their
  voice back — full-duplex.
first_seen: '2026-08-03T15:33:18Z'
last_seen: '2026-08-22T22:38:00Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/wiringai/mod_earshot
  seen_at: '2026-08-22T22:38:00Z'
  metrics:
    stars: 47
    forks: 20
    open_issues: 0
  kind: product
---

# mod_earshot

FreeSWITCH module that streams live call audio to AI voice agents over WebSocket and plays their voice back — full-duplex.

## 笔记


