---
slug: dont-sleep-on-wrapture
name: wrapture
builder: ''
category: AI + 开发
summary_zh: Python 开发者在不改动业务代码的情况下，通过一份 TOML 配置让 wrapture 对指定模块、函数、属性甚至生成器打补丁，把方法调用记录成时间线并汇总耗时，再导出为 OpenTelemetry
  链路；测试场景下它可替代 unittest.mock 的部分用法。用户最终拿到的是调用树、耗时统计和可导出的追踪数据，仍需自己判断哪段代码有问题。
inspiration: 趋势是观测与测试这两件原本分开的事，正被同一套运行时插桩机制合并，且配置化到不改代码就能开启。切入可放在中小团队没有专职 SRE、却要排查线上 Python 服务性能的环节：把插桩配置、慢调用归因和链路导出打包成按服务或按次交付的排查服务，而不是再卖一个通用可观测性平台。
summary_en: Without editing application code, Python developers point wrapture at modules, functions,
  attributes or even generators through a TOML file; it records method calls as timelines, aggregates
  timing and exports traces to OpenTelemetry, and can stand in for parts of unittest.mock in tests. The
  deliverable is a call tree, timing statistics and exportable trace data, while judging which code is
  at fault remains the user's job.
inspiration_en: 'The trend is that observability and testing, previously separate chores, are being merged
  by one runtime instrumentation mechanism that can be switched on through configuration rather than code
  changes. The opening is in small and mid-sized teams that have no dedicated SRE but still must diagnose
  slow Python services: package instrumentation setup, slow-call attribution and trace export as a per-service
  or per-incident diagnostic service instead of selling yet another general observability platform.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- Python 后端工程师在排查线上服务变慢或行为异常时，对运行中的应用做方法级追踪与调用记录，定位耗时调用并导出链路数据
jobs_en:
- Python backend engineers tracing a running service at method level when diagnosing slowness or unexpected
  behaviour, locating slow calls and exporting trace data
regions: []
regions_en: []
open_source: true
url: https://simonwillison.net/2026/Sep/11/wrapture/
canonical_url: https://simonwillison.net/2026/Sep/11/wrapture
summary: "Graham Dumpleton's new monkey patching package  wrapture  is shaping up to be an indispensable\
  \ tool for Python developers. I'm not sure why I've seen so little buzz about it! \n Graham has been\
  \ posting new tutorials for it almost daily since  the initial release  on August 31st. Here's everything\
  \ he's published so far: \n \n  Introducing wrapture  - a new monkey patching library that serves both\
  \ testing and observability (think New Relic style tracing) at the same time. \n  Unit testing with\
  \ wrapture  - how to use it for the same kinds of thing as  unittest.mock . \n  Recording calls with\
  \ wrapture   - recording method calls as timelines and processing and displaying them as trees. \n \
  \ Phased behaviour in wrapture   - arranging patched methods to change behavior across multiple calls.\
  \ \n  Beyond callables in wrapture  - monkey patching attributes, dictionaries, generators. \n  Live\
  \ tracing with wrapture   - tracing a live application to see exactly how it works. \n  Zero-code tracing\
  \ with wrapture   - configuring tracing in a separate TOML file without modifying Python code at all.\
  \ \n  Tracing Flask with wrapture   - using the separate  wrapture-instrumenation  package to instrument\
  \ a Flask application. That package also provides instrumentation for  aiohttp.client ,  aiohttp.web\
  \ ,  django ,  fastapi ,  flask ,  grpc ,  http.client ,  httpx ,  jinja2 ,  requests ,  sqlalchemy\
  \ ,  sqlite3 ,  starlette ,  urllib.request ,  urllib3 ,  uvicorn ,  werkzeug.serving ,  wsgiref.simple_server\
  \ ,  xmlrpc.client ,  xmlrpc.server . \n  Finding slow code with wrapture  - wrapture's tools for recording\
  \ timing information, both individually and aggregated across multiple calls. \n  OpenTelemetry export\
  \ in wrapture  - exporting traces to OpenTelemetry. \n \n Graham also has a  set of interactive workshops\
  \  for wrapture, implemented as JupyterLab notebooks. \n Wrapture is still alpha software but it's already\
  \ very usable - especially given you can configure and try it out with a TOML file without modifying\
  \ any Python code at all. \n This feels like one of those Swiss Army Knife packages that, once mastered,\
  \ will provide value against all sorts of problems for years to come. \n\n     Tags:  graham-dumpleton\
  \ ,  open-source ,  testing ,  python ,  observability ,  monkey-patching"
first_seen: '2026-09-11T13:51:32Z'
last_seen: '2026-09-12T00:19:09Z'
status: watching
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/11/wrapture/
  seen_at: '2026-09-12T00:19:09Z'
  metrics: {}
  kind: news
---

# wrapture

Graham Dumpleton's new monkey patching package  wrapture  is shaping up to be an indispensable tool for Python developers. I'm not sure why I've seen so little buzz about it! 
 Graham has been posting new tutorials for it almost daily since  the initial release  on August 31st. Here's everything he's published so far: 
 
  Introducing wrapture  - a new monkey patching library that serves both testing and observability (think New Relic style tracing) at the same time. 
  Unit testing with wrapture  - how to use it for the same kinds of thing as  unittest.mock . 
  Recording calls with wrapture   - recording method calls as timelines and processing and displaying them as trees. 
  Phased behaviour in wrapture   - arranging patched methods to change behavior across multiple calls. 
  Beyond callables in wrapture  - monkey patching attributes, dictionaries, generators. 
  Live tracing with wrapture   - tracing a live application to see exactly how it works. 
  Zero-code tracing with wrapture   - configuring tracing in a separate TOML file without modifying Python code at all. 
  Tracing Flask with wrapture   - using the separate  wrapture-instrumenation  package to instrument a Flask application. That package also provides instrumentation for  aiohttp.client ,  aiohttp.web ,  django ,  fastapi ,  flask ,  grpc ,  http.client ,  httpx ,  jinja2 ,  requests ,  sqlalchemy ,  sqlite3 ,  starlette ,  urllib.request ,  urllib3 ,  uvicorn ,  werkzeug.serving ,  wsgiref.simple_server ,  xmlrpc.client ,  xmlrpc.server . 
  Finding slow code with wrapture  - wrapture's tools for recording timing information, both individually and aggregated across multiple calls. 
  OpenTelemetry export in wrapture  - exporting traces to OpenTelemetry. 
 
 Graham also has a  set of interactive workshops  for wrapture, implemented as JupyterLab notebooks. 
 Wrapture is still alpha software but it's already very usable - especially given you can configure and try it out with a TOML file without modifying any Python code at all. 
 This feels like one of those Swiss Army Knife packages that, once mastered, will provide value against all sorts of problems for years to come. 

     Tags:  graham-dumpleton ,  open-source ,  testing ,  python ,  observability ,  monkey-patching

## 笔记


