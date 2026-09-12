---
slug: datasette-10a39-and-0654-security-releases
name: Datasette
builder: ''
category: ''
summary_zh: Datasette 是一个开源的数据发布与探索工具，本次是安全补丁版本发布，不是新产品。值得注意的变化是维护者把前沿模型引入代码安全审计，并称模型帮助发现了非常隐蔽的缺陷，随后由两名人类开发者分别写测试与实现修复。
inspiration: ''
summary_en: Datasette is an open-source tool for publishing and exploring data; this is a security patch
  release rather than a new product. The notable change is that the maintainer brought frontier models
  into code security auditing, saying they surfaced very subtle bugs, with two human developers splitting
  test-writing and fix implementation.
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
url: https://simonwillison.net/2026/Sep/11/datasette-security/
canonical_url: https://simonwillison.net/2026/Sep/11/datasette-security
summary: "Datasette 1.0a39 and 0.65.4 security releases   \nToday we're releasing two new security patch\
  \ versions of Datasette:  1.0a39  and  0.65.4  - one for the current alpha series and one for the stable\
  \ 0.65.x family. \n These are security fixes which you should apply if you are running a Datasette instance\
  \ on the public web - in particular if that instance mixes both public and private tables. \n Following\
  \ issues reported by  Sevban Dönmez ,  Alex Garcia  and I ran an extensive audit of Datasette using\
  \ Claude Fable 5.1, GPT-5.6, and GPT-6 Astra. We then spent almost a week collaborating on and reviewing\
  \ the fixes. \n They helped find some  very  subtle bugs. We'll be incorporating security audits by\
  \ frontier models into all of our development work going forward. \n Alex came up with a way of splitting\
  \ the work which I found extremely productive: \n \n Alex Garcia and I worked together running and then\
  \ responding to the audit, working in a shared private repository. For most of the issues we split the\
  \ work: one of us would create the automated tests highlighting the issue, then the other would implement\
  \ the fix. This ensured that two separate humans had eyes on each of the issues, in addition to our\
  \ coding agents running different models. \n \n\n\n     Tags:  releases ,  security ,  ai ,  datasette\
  \ ,  generative-ai ,  llms ,  agentic-engineering ,  ai-security-research"
first_seen: '2026-09-11T03:27:16Z'
last_seen: '2026-09-12T00:19:09Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/11/datasette-security/
  seen_at: '2026-09-12T00:19:09Z'
  metrics: {}
  kind: news
---

# Datasette

Datasette 1.0a39 and 0.65.4 security releases   
Today we're releasing two new security patch versions of Datasette:  1.0a39  and  0.65.4  - one for the current alpha series and one for the stable 0.65.x family. 
 These are security fixes which you should apply if you are running a Datasette instance on the public web - in particular if that instance mixes both public and private tables. 
 Following issues reported by  Sevban Dönmez ,  Alex Garcia  and I ran an extensive audit of Datasette using Claude Fable 5.1, GPT-5.6, and GPT-6 Astra. We then spent almost a week collaborating on and reviewing the fixes. 
 They helped find some  very  subtle bugs. We'll be incorporating security audits by frontier models into all of our development work going forward. 
 Alex came up with a way of splitting the work which I found extremely productive: 
 
 Alex Garcia and I worked together running and then responding to the audit, working in a shared private repository. For most of the issues we split the work: one of us would create the automated tests highlighting the issue, then the other would implement the fix. This ensured that two separate humans had eyes on each of the issues, in addition to our coding agents running different models. 
 


     Tags:  releases ,  security ,  ai ,  datasette ,  generative-ai ,  llms ,  agentic-engineering ,  ai-security-research

## 笔记


