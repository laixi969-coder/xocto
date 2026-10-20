---
slug: understanding-chatgpt-work
name: ChatGPT Work
builder: ''
category: 通用助手
summary_zh: 知识工作者在网页、移动端或桌面应用里打开 ChatGPT Work，把文档、本地文件和需要运行的程序交给它，由它读取材料并执行多步任务，最终产出整理结果或程序输出；桌面版可访问本地文件并运行程序，人工仍需核对结果。具体流程与交付边界仍待核验。
inspiration: 趋势：大厂把通用助手从对话推进到能读文件、跑程序的工作代理，办公与开发之间的旧分工正在被重新切分。切入：不要正面做通用工作代理；可从某个垂直行业的具体交付物切入，例如把本地文件处理与结果核对封装成按份交付的服务，卖结果而非席位。
summary_en: Knowledge workers open ChatGPT Work on web, mobile or desktop, hand over documents, local
  files and programs to run, and it reads the material and executes multi-step tasks, producing organized
  output or program results; the desktop version can access local files and run programs, and a person
  still has to check the results. The exact workflow and delivery boundary remain to be verified.
inspiration_en: 'Trend: a major lab is pushing the general assistant from chat toward a work agent that
  reads files and runs programs, redrawing the old split between office and development work. Entry: do
  not build a general work agent head-on; start from one vertical deliverable, for example packaging local-file
  handling and result checking into a per-deliverable service that sells outcomes rather than seats.'
priority_review: false
project_type: new_application
industries:
- 专业服务
- 软件开发
- 办公行政
industries_en:
- professional services
- software development
- office administration
jobs:
- 知识工作者在整理本地文件与运行脚本时，让云端或桌面版 ChatGPT Work 读取材料并执行多步任务，最终拿到整理结果或程序输出，仍需人工核对
- 办公团队在跨网页与桌面环境处理文档和程序时，用 ChatGPT Work 串联读取、执行与产出，交付前由人确认
jobs_en:
- Knowledge workers handling local files and scripts ask cloud or desktop ChatGPT Work to read materials
  and run multi-step tasks, receiving organized output or program results that still need human review
- Office teams working across web and desktop environments use ChatGPT Work to chain reading, execution
  and output, with a person confirming before delivery
regions:
- 全球
regions_en:
- global
open_source: false
url: https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/
canonical_url: https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work
summary: "OpenAI  announced ChatGPT Work  on July 9th, and have been furiously iterating on it ever since.\
  \ It is an extraordinarily confusing and very powerful product. Here's what I've figured out about it\
  \ so far. \n ChatGPT Work is actually two products \n The more interesting version of ChatGPT Work is\
  \ the one that runs in the cloud. This can be accessed via  chatgpt.com  or through the ChatGPT mobile\
  \ apps. Let's call it  Work Cloud . \n If you install the ChatGPT desktop app - the app that used to\
  \ be called Codex - you gain access to a thing called ChatGPT Work that can access files and run programs\
  \ directly on your computer. Let's call that one  Work Local . This one feels more like regular Codex\
  \ re-skinned to be less intimidating to non-software-developers. \n For the rest of this article I'm\
  \ going to talk exclusively about Work Cloud. \n Work is for paid subscribers only \n Right now, ChatGPT\
  \ Work (in both flavors) is available only to $20/month and up subscribers. Free users and $8/month\
  \ Go users do not have access. \n Work has features that aren't available in Chat \n The interface for\
  \ accessing Work is a tab selector, which presents it as an alternative to Chat: \n   \n The obvious\
  \ question is  when should I use Chat, and when should I use Work?  \n OpenAI's  official answer  to\
  \ that question is: \n \n Use Chat when you want an answer, explanation, brainstorm, or short draft.\
  \ Use ChatGPT Work when you want ChatGPT to complete a task with a clear outcome, such as a brief, deck,\
  \ analysis, recurring update, workflow, or file you can review and use. \n \n I find that almost entirely\
  \ useless, because I've been using regular ChatGPT Chat for all of those task categories for years!\
  \ \n The better question then is  what features does Work have that are missing from Chat?  \n After\
  \ extensive experimentation I think I've mostly figured that out: \n \n  Options to use Luna and Terra\
  \ in place of Sol  \n  A code execution environment with Internet access  \n  A headless Chrome browser\
  \  \n  A persistent filesystem shared between sessions  \n  The ability to publish ChatGPT Sites  \n\
  \  The ability to run sub-agent sessions with Sol, Luna, and Terra  \n  Scheduled prompt automations\
  \  (may be in ChatGPT Chat too) \n \n Model selection \n In Work, you get the option to pick GPT-5.6\
  \ Sol, Luna, or Terra, each with Light, Medium, High, Extra High, Max, or Ultra reasoning levels. You\
  \ can also pick GPT-5.5 at Light, Medium, High, or Extra High. \n These look to be the same models that\
  \ are available through the OpenAI API. \n Chat offers a different selection: 5.6 Instant, Medium, High,\
  \ Extra High, and Pro. It doesn't explain if those are Luna or Terra or Sol (I'm assuming Sol?). 5.6\
  \ Pro appears to be exclusive to Chat, with no equivalent in Work. \n My current understanding from\
  \ using Codex is that Ultra is a special mode that more eagerly delegates to sub-agents. \n I believe\
  \ ChatGPT Work sessions are billed against your Codex allowance, while ChatGPT Chat Sessions get their\
  \ own, separate allowance. This may help explain the model availability differences. \n Code execution\
  \ with Internet access! \n As a long-time fan of the  Code Interpreter pattern  - pioneered by OpenAI\
  \ in 2023 - this is by far the most exciting feature of ChatGPT Work (Cloud) for me. \n The code execution\
  \ environment can now talk to the rest of the internet! \n ChatGPT Chat can't do this - if you ask it\
  \ to install additional software packages or interact with websites or APIs that access will be blocked\
  \ by the container proxy. \n (Weirdly, back in January it  grew the ability to install packages , but\
  \ that doesn't seem to work any more. I wish they had better changelogs!) \n Claude's equivalent container\
  \ has allowed restricted internet access since it launched  last September . Claude can install packages\
  \ from PYPI and NPM and clone repositories from GitHub. But that is about it: the allowlist of domains\
  \ is very short. \n ChatGPT Work allows a whole lot more than that. It can be configured with a specific\
  \ list of allowed domains, but the default appears to be open to all. \n This makes Work an incredibly\
  \ useful tool. You can have it clone GitHub repositories, install their dependencies, then use them\
  \ to interact with the rest of the web! \n A full, headless Chrome browser \n Another killer feature\
  \ of ChatGPT Work is  the browser tool . ChatGPT Work can launch a full Chrome instance, load websites,\
  \ fill out forms, and take screenshots. \n If a site requires sign in the browser can prompt you to\
  \ take over and enter both passwords and 2FA codes, without round-tripping those credentials through\
  \ the model itself. \n\n It can even run JavaScript against the DOM of loaded pages. I prompted: \n\
  \ \n  Load simonwillison.net in your browser and extract the headings using JavaScript  \n \n ChatGPT\
  \ Work fired up a browser instance and ran the code: \n   await   tab  .  playwright  .  evaluate  (\
  \  (  )   =>   { \n   return   Array  .  from  (  document  .  querySelectorAll  (  \"h1,h2,h3,h4,h5,h6\"\
  \  )  ,   heading   =>   (  { \n     level :  heading  .  tagName  .  toLowerCase  (  )  , \n     text\
  \ :  heading  .  innerText  .  trim  (  )  .  replace  (   /  \\s  +  / g  ,   \" \"  )  , \n     id\
  \ :  heading  .  id   ||   null \n   }  )  )  ; \n }  )  ;   \n This feels a lot like my  shot-scraper\
  \ javascript  tool, only now I can access it on my phone! \n A persistent, shared filesystem \n ChatGPT\
  \ Chat gets a fresh filesystem for each chat session. These cannot be accessed from any other session.\
  \ \n In ChatGPT Work each session gets its own scratch folder - named something like  /workspace/scratch/e00a0a017944\
  \  - but each of those are persisted across sessions, so you can access files from previous chats. I\
  \ have 171 folders in  /workspace/scratch  right now! \n As far as I can tell that  /workspace  volume\
  \ is mounted to all Work sessions that are currently running - file edits from one can be instantly\
  \ seen by the others. They don't seem to share the same process space though, and localhost servers\
  \ running in one can't be accessed from another. \n ChatGPT Sites \n ChatGPT Work has the ability to\
  \ build  and deploy  entire websites, using Cloudflare Workers. These can have HTML and JavaScript and\
  \ can run server-side features too, including stateful features on top of Cloudflare D1 and R2. \n Here's\
  \ a simple site I built with this feature: \n  london-pelicans-in-her-piety.simonw.chatgpt.site  \n\
  \   \n My prompt was: \n \n  Figure out all of the places in London with a pelican in her piety, then\
  \ turn that into a JSON file and build a ChatGPT sites site about them  \n \n (A pelican in her piety\
  \ is a fascinating piece of  medieval Christian imagery  - once you know about them you'll find them\
  \ all over the place.) \n These sites default to being private to the user that created them, but you\
  \ can make them public and (on team plans) share them with other specific individuals. \n Sub-agents\
  \ with Sol, Luna, and Terra \n There's not much to say about this one. ChatGPT Chat can't run sub-agents.\
  \ ChatGPT Work can. This is very much a power-user feature: if you are running a complex project that\
  \ can benefit from multiple parallel agents working together, Work can do that. \n Scheduled prompt\
  \ automations \n Another feature that seems to have migrated from regular ChatGPT to ChatGPT Work at\
  \ some point. You can prompt ChatGPT Work like this: \n \n  run a search to see if Waymo have announced\
  \ a launch date for Half Moon Bay every day at 8am  \n \n This will schedule a prompt to run on that\
  \ frequency. These prompts can decide that nothing interesting has happened, or they can decide to notify\
  \ you of some new information. \n  Update : Actually this seems to work in ChatGPT Chat as well. \n\
  \ It's still worth noting here though, as it can be used in conjunction with other ChatGPT Work exclusive\
  \ features. You can set a scheduled task to update a ChatGPT Site on an hourly basis, for example. \n\
  \ Is this safe? \n An open question for me right now is how  safe  all of this stuff is. \n My  lethal\
  \ trifecta model  warns about the risks inherent in any agent system that combines access to private\
  \ data with exposure to untrusted content and a way to communicate stolen information back to an attacker.\
  \ \n ChatGPT Work combines all three! \n I'd love to hear more from OpenAI about how they protect ChatGPT\
  \ Work sessions against prompt injection attacks. I expect their answer is the same  auto-review mechanism\
  \  as Codex. \n OpenAI could make this a lot less confusing \n Figuring this all out took way more work\
  \ than it should have. \n I think there are two key problems here: \n \n OpenAI explain Work in terms\
  \ of what it's for, not what it actually does \n OpenAI still insist on hiding their system prompts\
  \ and tools descriptions \n \n If the ChatGPT Work documentation included the exact system prompt and\
  \ tool descriptions used by the agent I wouldn't have needed to write this post. \n    \n         Tags:\
  \  ai ,  openai ,  generative-ai ,  chatgpt ,  llms ,  code-interpreter ,  general-agents"
first_seen: '2026-08-30T23:59:47Z'
last_seen: '2026-08-31T00:37:42Z'
status: queued
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/
  seen_at: '2026-08-31T00:37:42Z'
  metrics: {}
  kind: news
---

# ChatGPT Work

OpenAI  announced ChatGPT Work  on July 9th, and have been furiously iterating on it ever since. It is an extraordinarily confusing and very powerful product. Here's what I've figured out about it so far. 
 ChatGPT Work is actually two products 
 The more interesting version of ChatGPT Work is the one that runs in the cloud. This can be accessed via  chatgpt.com  or through the ChatGPT mobile apps. Let's call it  Work Cloud . 
 If you install the ChatGPT desktop app - the app that used to be called Codex - you gain access to a thing called ChatGPT Work that can access files and run programs directly on your computer. Let's call that one  Work Local . This one feels more like regular Codex re-skinned to be less intimidating to non-software-developers. 
 For the rest of this article I'm going to talk exclusively about Work Cloud. 
 Work is for paid subscribers only 
 Right now, ChatGPT Work (in both flavors) is available only to $20/month and up subscribers. Free users and $8/month Go users do not have access. 
 Work has features that aren't available in Chat 
 The interface for accessing Work is a tab selector, which presents it as an alternative to Chat: 
   
 The obvious question is  when should I use Chat, and when should I use Work?  
 OpenAI's  official answer  to that question is: 
 
 Use Chat when you want an answer, explanation, brainstorm, or short draft. Use ChatGPT Work when you want ChatGPT to complete a task with a clear outcome, such as a brief, deck, analysis, recurring update, workflow, or file you can review and use. 
 
 I find that almost entirely useless, because I've been using regular ChatGPT Chat for all of those task categories for years! 
 The better question then is  what features does Work have that are missing from Chat?  
 After extensive experimentation I think I've mostly figured that out: 
 
  Options to use Luna and Terra in place of Sol  
  A code execution environment with Internet access  
  A headless Chrome browser  
  A persistent filesystem shared between sessions  
  The ability to publish ChatGPT Sites  
  The ability to run sub-agent sessions with Sol, Luna, and Terra  
  Scheduled prompt automations  (may be in ChatGPT Chat too) 
 
 Model selection 
 In Work, you get the option to pick GPT-5.6 Sol, Luna, or Terra, each with Light, Medium, High, Extra High, Max, or Ultra reasoning levels. You can also pick GPT-5.5 at Light, Medium, High, or Extra High. 
 These look to be the same models that are available through the OpenAI API. 
 Chat offers a different selection: 5.6 Instant, Medium, High, Extra High, and Pro. It doesn't explain if those are Luna or Terra or Sol (I'm assuming Sol?). 5.6 Pro appears to be exclusive to Chat, with no equivalent in Work. 
 My current understanding from using Codex is that Ultra is a special mode that more eagerly delegates to sub-agents. 
 I believe ChatGPT Work sessions are billed against your Codex allowance, while ChatGPT Chat Sessions get their own, separate allowance. This may help explain the model availability differences. 
 Code execution with Internet access! 
 As a long-time fan of the  Code Interpreter pattern  - pioneered by OpenAI in 2023 - this is by far the most exciting feature of ChatGPT Work (Cloud) for me. 
 The code execution environment can now talk to the rest of the internet! 
 ChatGPT Chat can't do this - if you ask it to install additional software packages or interact with websites or APIs that access will be blocked by the container proxy. 
 (Weirdly, back in January it  grew the ability to install packages , but that doesn't seem to work any more. I wish they had better changelogs!) 
 Claude's equivalent container has allowed restricted internet access since it launched  last September . Claude can install packages from PYPI and NPM and clone repositories from GitHub. But that is about it: the allowlist of domains is very short. 
 ChatGPT Work allows a whole lot more than that. It can be configured with a specific list of allowed domains, but the default appears to be open to all. 
 This makes Work an incredibly useful tool. You can have it clone GitHub repositories, install their dependencies, then use them to interact with the rest of the web! 
 A full, headless Chrome browser 
 Another killer feature of ChatGPT Work is  the browser tool . ChatGPT Work can launch a full Chrome instance, load websites, fill out forms, and take screenshots. 
 If a site requires sign in the browser can prompt you to take over and enter both passwords and 2FA codes, without round-tripping those credentials through the model itself. 

 It can even run JavaScript against the DOM of loaded pages. I prompted: 
 
  Load simonwillison.net in your browser and extract the headings using JavaScript  
 
 ChatGPT Work fired up a browser instance and ran the code: 
   await   tab  .  playwright  .  evaluate  (  (  )   =>   { 
   return   Array  .  from  (  document  .  querySelectorAll  (  "h1,h2,h3,h4,h5,h6"  )  ,   heading   =>   (  { 
     level :  heading  .  tagName  .  toLowerCase  (  )  , 
     text :  heading  .  innerText  .  trim  (  )  .  replace  (   /  \s  +  / g  ,   " "  )  , 
     id :  heading  .  id   ||   null 
   }  )  )  ; 
 }  )  ;   
 This feels a lot like my  shot-scraper javascript  tool, only now I can access it on my phone! 
 A persistent, shared filesystem 
 ChatGPT Chat gets a fresh filesystem for each chat session. These cannot be accessed from any other session. 
 In ChatGPT Work each session gets its own scratch folder - named something like  /workspace/scratch/e00a0a017944  - but each of those are persisted across sessions, so you can access files from previous chats. I have 171 folders in  /workspace/scratch  right now! 
 As far as I can tell that  /workspace  volume is mounted to all Work sessions that are currently running - file edits from one can be instantly seen by the others. They don't seem to share the same process space though, and localhost servers running in one can't be accessed from another. 
 ChatGPT Sites 
 ChatGPT Work has the ability to build  and deploy  entire websites, using Cloudflare Workers. These can have HTML and JavaScript and can run server-side features too, including stateful features on top of Cloudflare D1 and R2. 
 Here's a simple site I built with this feature: 
  london-pelicans-in-her-piety.simonw.chatgpt.site  
   
 My prompt was: 
 
  Figure out all of the places in London with a pelican in her piety, then turn that into a JSON file and build a ChatGPT sites site about them  
 
 (A pelican in her piety is a fascinating piece of  medieval Christian imagery  - once you know about them you'll find them all over the place.) 
 These sites default to being private to the user that created them, but you can make them public and (on team plans) share them with other specific individuals. 
 Sub-agents with Sol, Luna, and Terra 
 There's not much to say about this one. ChatGPT Chat can't run sub-agents. ChatGPT Work can. This is very much a power-user feature: if you are running a complex project that can benefit from multiple parallel agents working together, Work can do that. 
 Scheduled prompt automations 
 Another feature that seems to have migrated from regular ChatGPT to ChatGPT Work at some point. You can prompt ChatGPT Work like this: 
 
  run a search to see if Waymo have announced a launch date for Half Moon Bay every day at 8am  
 
 This will schedule a prompt to run on that frequency. These prompts can decide that nothing interesting has happened, or they can decide to notify you of some new information. 
  Update : Actually this seems to work in ChatGPT Chat as well. 
 It's still worth noting here though, as it can be used in conjunction with other ChatGPT Work exclusive features. You can set a scheduled task to update a ChatGPT Site on an hourly basis, for example. 
 Is this safe? 
 An open question for me right now is how  safe  all of this stuff is. 
 My  lethal trifecta model  warns about the risks inherent in any agent system that combines access to private data with exposure to untrusted content and a way to communicate stolen information back to an attacker. 
 ChatGPT Work combines all three! 
 I'd love to hear more from OpenAI about how they protect ChatGPT Work sessions against prompt injection attacks. I expect their answer is the same  auto-review mechanism  as Codex. 
 OpenAI could make this a lot less confusing 
 Figuring this all out took way more work than it should have. 
 I think there are two key problems here: 
 
 OpenAI explain Work in terms of what it's for, not what it actually does 
 OpenAI still insist on hiding their system prompts and tools descriptions 
 
 If the ChatGPT Work documentation included the exact system prompt and tool descriptions used by the agent I wouldn't have needed to write this post. 
    
         Tags:  ai ,  openai ,  generative-ai ,  chatgpt ,  llms ,  code-interpreter ,  general-agents

## 笔记


