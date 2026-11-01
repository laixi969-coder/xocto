---
slug: how-we-took-over-chatgpt-accounts
name: How We Took Over ChatGPT Accounts
builder: ''
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
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
url: https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/
canonical_url: https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts
summary: How We Took Over ChatGPT Accounts Parameter Labs describe an exploit they found against ChatGPT's
  implementation of the artifacts pattern (OpenAI used to call this "Canvas" but it looks like the latest
  revision is called HTML previews ), where interactive custom HTML apps are displayed in a sandboxed
  iframe. It's important that HTML in these stays tightly sandboxed to avoid untrusted code interacting
  with OpenAI APIs and accessing private data. Parameter found quite a complex attack chain. OpenAI use
  the MathLive JavaScript library as part of their graph support, and that library includes its own virtual
  keyboard , which can be triggered in the parent page via postMessage() from the sandboxed iframe. That
  message receiving code uses innerHTML , so anything that sends a message can add custom HTML to the
  parent - and there was no mechanism to prevent other sandboxed frames, including HTML preview frames,
  from calling that method. This meant untrusted code in an iframe could insert HTML, and while innerHTML
  doesn't directly execute script elements it could be used to inject a new iframe without sandbox restrictions.
  OpenAI’s CSP rules blocked inline scripts entirely, and only allowed script loading from a handful of
  domains, but one
first_seen: '2026-11-01T01:10:59Z'
last_seen: '2026-11-01T01:10:59Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/
  seen_at: '2026-11-01T01:10:59Z'
  metrics: {}
  kind: news
---

# How We Took Over ChatGPT Accounts

How We Took Over ChatGPT Accounts Parameter Labs describe an exploit they found against ChatGPT's implementation of the artifacts pattern (OpenAI used to call this "Canvas" but it looks like the latest revision is called HTML previews ), where interactive custom HTML apps are displayed in a sandboxed iframe. It's important that HTML in these stays tightly sandboxed to avoid untrusted code interacting with OpenAI APIs and accessing private data. Parameter found quite a complex attack chain. OpenAI use the MathLive JavaScript library as part of their graph support, and that library includes its own virtual keyboard , which can be triggered in the parent page via postMessage() from the sandboxed iframe. That message receiving code uses innerHTML , so anything that sends a message can add custom HTML to the parent - and there was no mechanism to prevent other sandboxed frames, including HTML preview frames, from calling that method. This meant untrusted code in an iframe could insert HTML, and while innerHTML doesn't directly execute script elements it could be used to inject a new iframe without sandbox restrictions. OpenAI’s CSP rules blocked inline scripts entirely, and only allowed script loading from a handful of domains, but one

## 笔记


