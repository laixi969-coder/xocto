---
slug: cloudflare-python-workers-are-now-generally-available
name: Cloudflare Python Workers
builder: ''
category: ''
summary_zh: 这是 Cloudflare 开发者平台的一项运行时能力变化，不是独立产品：原本只能用 JavaScript 等语言编写的边缘函数，现在可以直接用 Python 编写并部署，开发者拿到的是可部署的服务端函数，而不是一个可独立购买的应用。
inspiration: ''
summary_en: 'This is a runtime capability change on Cloudflare''s developer platform rather than a standalone
  product: edge functions that previously had to be written in JavaScript and similar languages can now
  be written and deployed in Python, and what developers get is a deployable server-side function, not
  an independently purchasable application.'
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
url: https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/
canonical_url: https://simonwillison.net/2026/Sep/21/cloudflare-python-worker
summary: "Cloudflare Python Workers are now generally available   \nAfter a two year preview, Cloudflare's\
  \ support for running Python code in their server-side Workers platform is now stable: \"Python is now\
  \ a first-class, fully supported language on the Cloudflare Developer Platform\". \n A neat thing about\
  \ this is how it works. Cloudflare are running Python compiled to WebAssembly via Pyodide in their V8-based\
  \  workerd  runtime. \n This comes with some limitations,  documented here  - most notably both  multiprocessing\
  \  and  threading  are non-functional in the WebAssembly VM. \n One particularly interesting detail\
  \ of this is the local development environment story - their  pywrangler  development tool (confusingly\
  \ packaged as  workers-py  on PyPI) runs a full local simulation of their stack, including executing\
  \ code with Pyodide in WebAssembly in V8 in a 123MB  workerd  binary, which for me ended up in  node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd\
  \ . \n Python Workers represent a significant investment in the wider Python ecosystem by Cloudflare.\
  \ The release announcement is credited to Gyeongjae Choi, Dominik Picheta, and Hood Chatham - Gyeongjae\
  \ and Hood are both Pyodide core maintainers.\n\n       Via  Hacker News   \n\n\n     Tags:  python\
  \ ,  cloudflare ,  webassembly ,  pyodide"
first_seen: '2026-09-21T22:25:44Z'
last_seen: '2026-09-22T00:50:51Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/
  seen_at: '2026-09-22T00:50:51Z'
  metrics: {}
  kind: news
---

# Cloudflare Python Workers

Cloudflare Python Workers are now generally available   
After a two year preview, Cloudflare's support for running Python code in their server-side Workers platform is now stable: "Python is now a first-class, fully supported language on the Cloudflare Developer Platform". 
 A neat thing about this is how it works. Cloudflare are running Python compiled to WebAssembly via Pyodide in their V8-based  workerd  runtime. 
 This comes with some limitations,  documented here  - most notably both  multiprocessing  and  threading  are non-functional in the WebAssembly VM. 
 One particularly interesting detail of this is the local development environment story - their  pywrangler  development tool (confusingly packaged as  workers-py  on PyPI) runs a full local simulation of their stack, including executing code with Pyodide in WebAssembly in V8 in a 123MB  workerd  binary, which for me ended up in  node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd . 
 Python Workers represent a significant investment in the wider Python ecosystem by Cloudflare. The release announcement is credited to Gyeongjae Choi, Dominik Picheta, and Hood Chatham - Gyeongjae and Hood are both Pyodide core maintainers.

       Via  Hacker News   


     Tags:  python ,  cloudflare ,  webassembly ,  pyodide

## 笔记


