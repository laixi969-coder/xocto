---
slug: bend
name: Bend
builder: nicolas-siplis
category: AI + 开发
summary_zh: 开发者在编写并行或 GPU 程序时，需要同时处理正确性验证与硬件调度，通常要分别写验证代码和并行代码。Bend 让开发者用同一份源码表达并行计算，并借助证明机制在编译阶段拦截 AI
  生成代码中的错误，最终产出可在 CPU 或 GPU 上运行的程序；具体语言特性、工具链成熟度与交付流程仍待核验。
inspiration: 趋势：AI 写代码的速度已经超过人工审查速度，正确性验证正从“事后测试”前移到语言与编译层。切入：可从对错误零容忍的环节进入，例如金融清算、芯片验证、自动驾驶感知模块的并行内核，卖法可以是按项目交付可验证内核，而非按席位卖编辑器；该语言本身尚处早期，不宜从通用应用开发切入。
summary_en: Developers writing parallel or GPU programs must handle both correctness verification and
  hardware scheduling, usually by writing verification code and parallel code separately. Bend lets developers
  express parallel computation in one source and uses a proof mechanism to catch errors in AI-generated
  code at compile time, producing programs that run on CPU or GPU; specific language features, toolchain
  maturity and delivery flow still need verification.
inspiration_en: 'Trend: AI writes code faster than humans can review it, so correctness verification is
  moving from post-hoc testing into the language and compiler layer. Entry: start where errors are intolerable,
  such as clearing and settlement, chip verification or parallel kernels in autonomous-driving perception,
  selling verifiable kernels per project rather than per seat; the language itself is early, so general
  application development is not the entry point.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 编译器与运行时工程师
jobs_en:
- Compiler and runtime engineers
regions: []
regions_en: []
open_source: true
url: https://bend-lang.com/
canonical_url: https://bend-lang.com
summary: A language that blocks AI mistakes via proof, on CPU and GPU
first_seen: '2026-09-17T20:36:13Z'
last_seen: '2026-09-19T00:21:15Z'
status: watching
sources:
- hackernews
sightings:
- source: hackernews
  url: https://bend-lang.com/
  seen_at: '2026-09-19T00:21:15Z'
  metrics:
    points: 589
    comments: 302
  kind: news
---

# Bend

A language that blocks AI mistakes via proof, on CPU and GPU

## 笔记


