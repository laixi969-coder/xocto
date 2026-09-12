---
slug: soft-deprecating-rematch
name: Soft-deprecating re.match()
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
url: https://simonwillison.net/2026/Sep/11/soft-deprecating-re-match/
canonical_url: https://simonwillison.net/2026/Sep/11/soft-deprecating-re-match
summary: "Soft-deprecating re.match()   \nPython has a concept of  soft deprecation , where APIs are marked\
  \ as \"should no longer be used to write new code\" without any promise/threat to remove them in the\
  \ future. \n Python 3.15 release manager Hugo van Kemenade describes how in the upcoming 3.15 release\
  \ soft deprecation has come for the venerable but deeply confusing  re.match()  function. It's now available\
  \ with the much clearer alternative  re.prefixmatch()  name - reflecting how it anchors at the beginning\
  \ of the string but not the end. \n Most of the time you probably want  re.search()  (match this pattern\
  \ anywhere in the string) or  re.fullmatch()  (match the entire string) instead.\n\n       Via  Lobste.rs\
  \   \n\n\n     Tags:  python ,  regular-expressions"
first_seen: '2026-09-11T14:47:57Z'
last_seen: '2026-09-12T00:19:09Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/11/soft-deprecating-re-match/
  seen_at: '2026-09-12T00:19:09Z'
  metrics: {}
  kind: news
---

# Soft-deprecating re.match()

Soft-deprecating re.match()   
Python has a concept of  soft deprecation , where APIs are marked as "should no longer be used to write new code" without any promise/threat to remove them in the future. 
 Python 3.15 release manager Hugo van Kemenade describes how in the upcoming 3.15 release soft deprecation has come for the venerable but deeply confusing  re.match()  function. It's now available with the much clearer alternative  re.prefixmatch()  name - reflecting how it anchors at the beginning of the string but not the end. 
 Most of the time you probably want  re.search()  (match this pattern anywhere in the string) or  re.fullmatch()  (match the entire string) instead.

       Via  Lobste.rs   


     Tags:  python ,  regular-expressions

## 笔记


