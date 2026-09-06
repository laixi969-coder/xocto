---
slug: quoting-rick-brewster
name: Paint.NET
builder: ''
category: AI + 开发
summary_zh: Paint.NET 是一款 Windows 图像编辑器。为在 WINE 上运行，作者用 Claude 逆向重写了 Direct2D 图形库，代码约 18 万行，未经全面审查。这展示了
  AI 辅助逆向工程的潜力，但具体工作流和交付质量仍需核验。
inspiration: 趋势：AI 不仅能写新代码，还能辅助逆向工程和兼容层开发，降低维护老旧软件的成本。切入：可关注 AI 辅助的软件兼容性、迁移和逆向工程工具，面向需要维护旧系统的企业或开发者。
summary_en: Paint.NET is a Windows image editor. To run on WINE, the author used Claude to reverse-engineer
  and rewrite the Direct2D graphics library from scratch, about 180,000 lines of code, not thoroughly
  reviewed. This demonstrates AI-assisted reverse engineering potential, but the specific workflow and
  delivery quality need verification.
inspiration_en: 'Trend: AI can not only write new code but also assist reverse engineering and compatibility
  layer development, reducing the cost of maintaining legacy software. Angle: Focus on AI-assisted software
  compatibility, migration, and reverse engineering tools for enterprises or developers maintaining legacy
  systems.'
priority_review: false
project_type: ai_transformation
industries:
- 软件开发
- 桌面应用
industries_en:
- Software Development
- Desktop Applications
jobs:
- 软件开发者
- 桌面应用维护者
jobs_en:
- Software Developers
- Desktop Application Maintainers
regions: []
regions_en: []
open_source: false
url: https://simonwillison.net/2026/Sep/2/rick-brewster/
canonical_url: https://simonwillison.net/2026/Sep/2/rick-brewster
summary: "Direct2D has always been the biggest hurdle for Paint.NET on WINE, and it's clear that it will\
  \ never be completed enough for Paint.NET's use. And I can't just \"disable\" the use of Direct2D. So,\
  \ instead,  Paint.NET now has an internal, from-scratch, clean-room reverse-engineered rewrite of Direct2D\
  \ that it uses on WINE  (triggered by using  /wine ). It lives in  PaintDotNet.Windows.Direct2D1.Managed.dll\
  \ . This was written by our good friend  Claude , without whom this would NOT have been possible and\
  \ would NEVER have happened. [...] \n Most of this code is, as they say, \"vibe coded.\" By that I mean\
  \ that it has not been thoroughly reviewed, it's more \"trust me bro\" style. I cannot possibly review 180,000\
  \ lines of code, it's just way way  way  too much. For reference, the rest of Paint.NET is about 700,000\
  \ lines of code and I've been working on it for over 20 years. [...] \n At times, Claude was working\
  \ with the fury of 10 freshly unshackled Einstein genius-level 10x coders. And other times ... well,\
  \ not so much. I had to babysit Claude quite a bit to make sure it did resource management correctly\
  \ (for awhile it just wasn't doing the COM equivalent of AddRef() for reference counted objects, oops).\
  \ I had to slap it a few times when I found some really bad design or architecture decisions. And I\
  \ was also impressed at some rather clever and tireless reverse engineering work it did to figure out\
  \ all the formulas needed for implementing Direct2D's built-in effects library.  \n —  Rick Brewster\
  \ , author of Paint.NET \n\n     Tags:  reverse-engineering ,  coding-agents ,  claude ,  generative-ai\
  \ ,  ai ,  llms ,  dotnet ,  linux ,  vibe-coding"
first_seen: '2026-09-02T05:50:57Z'
last_seen: '2026-09-02T14:32:03Z'
status: watching
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/2/rick-brewster/
  seen_at: '2026-09-02T14:32:03Z'
  metrics: {}
  kind: news
---

# Paint.NET

Direct2D has always been the biggest hurdle for Paint.NET on WINE, and it's clear that it will never be completed enough for Paint.NET's use. And I can't just "disable" the use of Direct2D. So, instead,  Paint.NET now has an internal, from-scratch, clean-room reverse-engineered rewrite of Direct2D that it uses on WINE  (triggered by using  /wine ). It lives in  PaintDotNet.Windows.Direct2D1.Managed.dll . This was written by our good friend  Claude , without whom this would NOT have been possible and would NEVER have happened. [...] 
 Most of this code is, as they say, "vibe coded." By that I mean that it has not been thoroughly reviewed, it's more "trust me bro" style. I cannot possibly review 180,000 lines of code, it's just way way  way  too much. For reference, the rest of Paint.NET is about 700,000 lines of code and I've been working on it for over 20 years. [...] 
 At times, Claude was working with the fury of 10 freshly unshackled Einstein genius-level 10x coders. And other times ... well, not so much. I had to babysit Claude quite a bit to make sure it did resource management correctly (for awhile it just wasn't doing the COM equivalent of AddRef() for reference counted objects, oops). I had to slap it a few times when I found some really bad design or architecture decisions. And I was also impressed at some rather clever and tireless reverse engineering work it did to figure out all the formulas needed for implementing Direct2D's built-in effects library.  
 —  Rick Brewster , author of Paint.NET 

     Tags:  reverse-engineering ,  coding-agents ,  claude ,  generative-ai ,  ai ,  llms ,  dotnet ,  linux ,  vibe-coding

## 笔记


