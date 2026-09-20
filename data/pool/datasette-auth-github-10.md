---
slug: datasette-auth-github-10
name: datasette-auth-github 1.0
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
url: https://simonwillison.net/2026/Sep/19/datasette-auth-github/
canonical_url: https://simonwillison.net/2026/Sep/19/datasette-auth-github
summary: "Release:   datasette-auth-github 1.0  \n         I run this GitHub login plugin on the  agent.datasette.io\
  \  demo site and I noticed that my authenticated sessions weren't lasting very long. It turned out that\
  \ the plugin was setting cookies without a  Max-Age  parameter, so they were expiring at the end of\
  \ a browser session (which in Mobile Safari seems to happen pretty often, independently of how you are\
  \ using the app.) \n I fixed that in  #80  and, since this plugin has been around for quite a while\
  \ and is tested against both Datasette 0.65.x and Datasette 1.0ax, I decided to bump it up to a 1.0\
  \ release. I'm trying to get better at promoting stable plugins to 1.0. \n    \n    \n         Tags:\
  \  github ,  plugins ,  datasette"
first_seen: '2026-09-19T19:52:02Z'
last_seen: '2026-09-20T00:09:45Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/19/datasette-auth-github/
  seen_at: '2026-09-20T00:09:45Z'
  metrics: {}
  kind: news
---

# datasette-auth-github 1.0

Release:   datasette-auth-github 1.0  
         I run this GitHub login plugin on the  agent.datasette.io  demo site and I noticed that my authenticated sessions weren't lasting very long. It turned out that the plugin was setting cookies without a  Max-Age  parameter, so they were expiring at the end of a browser session (which in Mobile Safari seems to happen pretty often, independently of how you are using the app.) 
 I fixed that in  #80  and, since this plugin has been around for quite a while and is tested against both Datasette 0.65.x and Datasette 1.0ax, I decided to bump it up to a 1.0 release. I'm trying to get better at promoting stable plugins to 1.0. 
    
    
         Tags:  github ,  plugins ,  datasette

## 笔记


