---
slug: using-parseable-with-datasette-for-opentelemetry-traces
name: Using Parseable with Datasette for OpenTelemetry traces
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
url: https://simonwillison.net/2026/Oct/6/datasette-parseable-opentelemetry/
canonical_url: https://simonwillison.net/2026/Oct/6/datasette-parseable-opentelemetry
summary: "TIL:   Using Parseable with Datasette for OpenTelemetry traces  \n         I  saw Parseable\
  \ in a Show HN  today - it's a new observability platform with both an  open source (AGPL)  Rust implementation\
  \ (a single ~180MB binary), an \"Enterprise\" version with extra features and a cloud hosted option.\
  \ \n Since  Datasette 1.0a41 added OpenTelemetry support  (thanks, Alex Garcia), I decided to fire up\
  \ Codex and have it figure out how to run Parseable and feed it traces from Datasette. \n Here's my\
  \ (human-written) TIL showing the patterns that worked, and here's a screenshot of a Datasette trace\
  \ displayed within the Parseable localhost web application: \n   \n    \n    \n         Tags:  datasette\
  \ ,  observability ,  alex-garcia ,  opentelemetry"
first_seen: '2026-10-06T19:07:31Z'
last_seen: '2026-10-07T01:32:55Z'
status: rejected
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/6/datasette-parseable-opentelemetry/
  seen_at: '2026-10-07T01:32:55Z'
  metrics: {}
  kind: news
---

# Using Parseable with Datasette for OpenTelemetry traces

TIL:   Using Parseable with Datasette for OpenTelemetry traces  
         I  saw Parseable in a Show HN  today - it's a new observability platform with both an  open source (AGPL)  Rust implementation (a single ~180MB binary), an "Enterprise" version with extra features and a cloud hosted option. 
 Since  Datasette 1.0a41 added OpenTelemetry support  (thanks, Alex Garcia), I decided to fire up Codex and have it figure out how to run Parseable and feed it traces from Datasette. 
 Here's my (human-written) TIL showing the patterns that worked, and here's a screenshot of a Datasette trace displayed within the Parseable localhost web application: 
   
    
    
         Tags:  datasette ,  observability ,  alex-garcia ,  opentelemetry

## 笔记


