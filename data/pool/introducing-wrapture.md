---
slug: introducing-wrapture
name: Wrapture
builder: ''
category: AI + 开发
summary_zh: Python 开发者在为现有项目添加测试替身或追踪时，把要包装的函数或方法交给 Wrapture；它通过配置或代码包装这些调用，记录出入参或返回指定值，交付可追踪的日志或测试替身。项目刚起步，具体工作流细节仍待核验。
inspiration: 趋势是 AI 辅助编程从生成代码走向生成完整工程，作者用 AI 编写整个库并公开过程。切入可从测试与可观测性工具链入手，强调 AI 生成代码的可验证性，但需先积累社区采用证据。
summary_en: Python developers use Wrapture to wrap functions or methods for testing or tracing; it records
  call data or returns stubbed values, delivering trace logs or test doubles. The project is young, and
  workflow details are still to be verified.
inspiration_en: The trend is AI-assisted programming moving from code generation to full engineering.
  Entry could focus on testing and observability tooling, emphasizing verifiability of AI-generated code,
  but community adoption evidence is needed first.
priority_review: false
project_type: open_source
industries:
- 软件开发
industries_en:
- Software Development
jobs:
- 软件工程师
- 测试工程师
jobs_en:
- Software Engineer
- Test Engineer
regions: []
regions_en: []
open_source: true
url: https://simonwillison.net/2026/Aug/31/introducing-wrapture/
canonical_url: https://simonwillison.net/2026/Aug/31/introducing-wrapture
summary: "Introducing wrapture   \nNew from Graham Dumpleton (of  wrapt , mod_wsgi, and New Relic's Python\
  \ agent fame), who describes Wrapture as taking the monkeypatching ideas from wrapt and extending them\
  \ to apply to testing and tracing at the same time. \n Wrapture ( full documentation here ) makes it\
  \ easy to wrap any function or method such that all access can be traced, or can be overridden to return\
  \ a different value. \n It acts as both an alternative to  unittest.mock  and a way to implement tracing\
  \ against an existing project: \n \n Attaching observation to code you do not control, recording what\
  \ flows through it, and doing so without disturbing the program being watched, is a problem I have never\
  \ really stopped thinking about. \n \n Wrapture includes  OpenTelemetry support  and even has an entirely\
  \ configuration-based mechanism for adding tracing to an existing Python project, which looks like this:\
  \ \n   capture  =   \" summary \"  \n\n[[ observe ]]\n target  =   \" domain:Calculator \"  \n name\
  \  = [  \" outer \"  ,   \" inner \"  ]\n\n[[ sink ]]\n type  =   \" jsonlines \"  \n path  =   \" trace.jsonl\
  \ \"    \n This is still a very young project - just a few weeks old - but it's off to a very promising\
  \ start. \n Interestingly, this is also Graham's first attempt at  large entirely agent-driven project:\
  \ \n \n Every line of code and documentation in wrapture was written by an AI assistant working under\
  \ my direction. I want to be upfront about that, and equally upfront about what it was not. This was\
  \ not vibe coding, where a one-shot prompt produces a pile of generated code and the person driving\
  \ hopes for the best because they lack the knowledge to judge what came back. Vibe coding has earned\
  \ its bad reputation. I engineered wrapture carefully from the start. I have spent a long time in this\
  \ particular corner of Python and knew exactly what the result needed to be, and the AI was the means\
  \ of producing it rather than the source of the design. \n \n In a follow-up post,  Unit testing with\
  \ wrapture , Graham shows the testing patterns supported by the new library: \n  def   test_stub_with_wrapture\
  \ ():\n     with   wrapture . binding (\n         Gateway ,  \"charge\" \n    ). on_call . returns ({\n\
  \         \"id\" :  \"stub\" ,  \"amount\" :  0 }\n    ):\n         assert   OrderService (). place\
  \ (\n             500 \n        )[ \"id\" ]  ==   \"stub\"  \n And this neat example of a test that\
  \ calls and then modifies the return value from the original method: \n  def   test_pinned_result_with_wrapture\
  \ ():\n     charge   =   wrapture . binding (\n         Gateway ,  \"charge\" \n    )\n     charge .\
  \ on_call . transforms_result (\n         lambda   r : { **  r ,  \"id\" :  \"ch_TEST\" }\n    )\n \
  \    with   charge :\n         assert   OrderService (). place (\n            500 \n        )  ==  {\n\
  \             \"id\" :  \"ch_TEST\" ,  \"amount\" :  500 \n        } \n\n (In both of these examples\
  \ the  OrderService().place(...)  method calls  Gateway().charge(...) .)\n\n\n     Tags:  graham-dumpleton\
  \ ,  monkey-patching ,  python ,  testing ,  pytest ,  observability ,  ai-assisted-programming ,  agentic-engineering\
  \ ,  opentelemetry"
first_seen: '2026-08-31T23:59:36Z'
last_seen: '2026-09-01T01:18:41Z'
status: queued
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Aug/31/introducing-wrapture/
  seen_at: '2026-09-01T01:18:41Z'
  metrics: {}
  kind: news
---

# Wrapture

Introducing wrapture   
New from Graham Dumpleton (of  wrapt , mod_wsgi, and New Relic's Python agent fame), who describes Wrapture as taking the monkeypatching ideas from wrapt and extending them to apply to testing and tracing at the same time. 
 Wrapture ( full documentation here ) makes it easy to wrap any function or method such that all access can be traced, or can be overridden to return a different value. 
 It acts as both an alternative to  unittest.mock  and a way to implement tracing against an existing project: 
 
 Attaching observation to code you do not control, recording what flows through it, and doing so without disturbing the program being watched, is a problem I have never really stopped thinking about. 
 
 Wrapture includes  OpenTelemetry support  and even has an entirely configuration-based mechanism for adding tracing to an existing Python project, which looks like this: 
   capture  =   " summary "  

[[ observe ]]
 target  =   " domain:Calculator "  
 name  = [  " outer "  ,   " inner "  ]

[[ sink ]]
 type  =   " jsonlines "  
 path  =   " trace.jsonl "    
 This is still a very young project - just a few weeks old - but it's off to a very promising start. 
 Interestingly, this is also Graham's first attempt at  large entirely agent-driven project: 
 
 Every line of code and documentation in wrapture was written by an AI assistant working under my direction. I want to be upfront about that, and equally upfront about what it was not. This was not vibe coding, where a one-shot prompt produces a pile of generated code and the person driving hopes for the best because they lack the knowledge to judge what came back. Vibe coding has earned its bad reputation. I engineered wrapture carefully from the start. I have spent a long time in this particular corner of Python and knew exactly what the result needed to be, and the AI was the means of producing it rather than the source of the design. 
 
 In a follow-up post,  Unit testing with wrapture , Graham shows the testing patterns supported by the new library: 
  def   test_stub_with_wrapture ():
     with   wrapture . binding (
         Gateway ,  "charge" 
    ). on_call . returns ({
         "id" :  "stub" ,  "amount" :  0 }
    ):
         assert   OrderService (). place (
             500 
        )[ "id" ]  ==   "stub"  
 And this neat example of a test that calls and then modifies the return value from the original method: 
  def   test_pinned_result_with_wrapture ():
     charge   =   wrapture . binding (
         Gateway ,  "charge" 
    )
     charge . on_call . transforms_result (
         lambda   r : { **  r ,  "id" :  "ch_TEST" }
    )
     with   charge :
         assert   OrderService (). place (
            500 
        )  ==  {
             "id" :  "ch_TEST" ,  "amount" :  500 
        } 

 (In both of these examples the  OrderService().place(...)  method calls  Gateway().charge(...) .)


     Tags:  graham-dumpleton ,  monkey-patching ,  python ,  testing ,  pytest ,  observability ,  ai-assisted-programming ,  agentic-engineering ,  opentelemetry

## 笔记


