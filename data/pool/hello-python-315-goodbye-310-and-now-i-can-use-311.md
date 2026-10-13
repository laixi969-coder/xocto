---
slug: hello-python-315-goodbye-310-and-now-i-can-use-311
name: Python 3.15
builder: ''
category: ''
summary_zh: Python 3.15 发布，带来 PEP 810 显式惰性导入等新特性，同时 Python 3.10 结束支持。惰性导入可降低插件与重依赖模块的启动开销，对依赖 Python 构建的
  AI 工具与应用的启动成本和交付效率有直接影响。
inspiration: ''
summary_en: Python 3.15 was released with features including PEP 810 explicit lazy imports, while Python
  3.10 reached end of support. Lazy imports reduce startup overhead from plugins and heavy dependencies,
  directly affecting the startup cost and delivery efficiency of AI tools and applications built on Python.
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
url: https://simonwillison.net/2026/Oct/12/python-3-15/
canonical_url: https://simonwillison.net/2026/Oct/12/python-3-15
summary: 'Python 3.15 is here ! Here''s the essential What''s new in Python 3.15 guide, this year curated
  by 3.14 and 3.15 release manager Hugo van Kemenade. As someone who builds open source software that
  works in every supported Python version, I get to say goodbye to Python 3.10 and start embracing features
  from Python 3.11. First, some highlights from Python 3.15. Explicit lazy imports I''m most excited about
  Explicit lazy imports from PEP 810 . These let you import modules like so: lazy import json lazy from
  pathlib import Path The module will then be imported the first time those symbols are used in the code
  that follows. My LLM CLI tool implements plugins. I had to recommend manual lazy imports in the plugin
  author documentation, because simply installing plugins that used heavy dependencies such as sentence_transformers
  could add multiple seconds to every invocation of the llm command. Lazy imports directly address this
  startup cost. Unpacking in comprehensions The new [*sublist for sublist in lists] unpacking syntax is
  neat. Here''s an illustration lifted from the documentation : lists = [[ 1 , 2 ], [ 3 , 4 ], [ 5 ]]
  [ * L for L in lists ]'
first_seen: '2026-10-13T03:04:22Z'
last_seen: '2026-10-13T03:04:22Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/12/python-3-15/
  seen_at: '2026-10-13T03:04:22Z'
  metrics: {}
  kind: news
---

# Python 3.15

Python 3.15 is here ! Here's the essential What's new in Python 3.15 guide, this year curated by 3.14 and 3.15 release manager Hugo van Kemenade. As someone who builds open source software that works in every supported Python version, I get to say goodbye to Python 3.10 and start embracing features from Python 3.11. First, some highlights from Python 3.15. Explicit lazy imports I'm most excited about Explicit lazy imports from PEP 810 . These let you import modules like so: lazy import json lazy from pathlib import Path The module will then be imported the first time those symbols are used in the code that follows. My LLM CLI tool implements plugins. I had to recommend manual lazy imports in the plugin author documentation, because simply installing plugins that used heavy dependencies such as sentence_transformers could add multiple seconds to every invocation of the llm command. Lazy imports directly address this startup cost. Unpacking in comprehensions The new [*sublist for sublist in lists] unpacking syntax is neat. Here's an illustration lifted from the documentation : lists = [[ 1 , 2 ], [ 3 , 4 ], [ 5 ]] [ * L for L in lists ]

## 笔记


