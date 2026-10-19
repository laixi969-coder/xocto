---
slug: inline-rendering-with-documentcurrentscript
name: Inline rendering with document​.currentScript
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
url: https://simonwillison.net/2026/Oct/17/document-currentscript/
canonical_url: https://simonwillison.net/2026/Oct/17/document-currentscript
summary: 'Inline rendering with document​.currentScript Lean Rada describes a neat trick that takes advantage
  of the document.currentScript property. You can use that to drop in a tiny inline <script> element that
  replaces itself when the page loads: The year is <script> document.currentScript.replaceWith( new Date().getFullYear())</script>
  If you define a shortcut function like this: $=(...n)=>document.currentScript.replaceWith(...n) You
  get a tiny template language: The year is <script>$(new Date().getFullYear())</script> Tags: javascript'
first_seen: '2026-10-19T00:13:57Z'
last_seen: '2026-10-19T00:13:57Z'
status: rejected
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/17/document-currentscript/
  seen_at: '2026-10-19T00:13:57Z'
  metrics: {}
  kind: news
---

# Inline rendering with document​.currentScript

Inline rendering with document​.currentScript Lean Rada describes a neat trick that takes advantage of the document.currentScript property. You can use that to drop in a tiny inline <script> element that replaces itself when the page loads: The year is <script> document.currentScript.replaceWith( new Date().getFullYear())</script> If you define a shortcut function like this: $=(...n)=>document.currentScript.replaceWith(...n) You get a tiny template language: The year is <script>$(new Date().getFullYear())</script> Tags: javascript

## 笔记


