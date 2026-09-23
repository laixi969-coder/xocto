---
slug: llm-typesafe-01a0
name: llm-typesafe 0.1a0
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
url: https://simonwillison.net/2026/Sep/22/llm-typesafe/
canonical_url: https://simonwillison.net/2026/Sep/22/llm-typesafe
summary: "Release:   llm-typesafe 0.1a0  \n         I built this new plugin for  LLM  to add support for\
  \  TypeSafe AI's new Jev model . Install it like this: \n  llm install llm-typesafe\n  \n Then set an\
  \ API key ( get one here , the waitlist seems to move pretty fast): \n  llm keys set typesafe\n# Paste\
  \ key\n  \n And now you can ask yes/no \"noul\" questions like this: \n  llm -m jev 'Please refund my\
  \ last payment.' \\\n  -s 'Does this message explicitly request a refund?'\n  \n Output: \n  {\"type\"\
  : \"noul\", \"noul\": 0.99}\n  \n Or choice questions like this: \n  cat message.txt  |  llm -m jev\
  \ \\\n  -s   ' Which team should handle this message? If billing and technical issues both occur, choose\
  \ billing. '   \\\n  -o answer_type choice \\\n  -o criteria   ' { \n     \"billing\":\"Charges, invoices,\
  \ payments, or refunds\", \n     \"technical\":\"Problems installing or using the product\", \n    \
  \ \"other\":\"Neither category fits\" \n   } '    \n Or scoring questions like this: \n  cat report.txt\
  \  |  llm -m jev \\\n  -s   ' How reproducible is the problem described in this report? '   \\\n  -o\
  \ answer_type score \\\n  -o criteria   ' [ \n     \"No reproduction instructions\", \n     \"Some instructions,\
  \ but important steps are missing\", \n     \"Complete steps with expected and actual results\" \n \
  \  ] '    \n See  the README  for more details. \n    \n    \n         Tags:  projects ,  llm ,  jev"
first_seen: '2026-09-22T15:54:16Z'
last_seen: '2026-09-23T00:34:37Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/22/llm-typesafe/
  seen_at: '2026-09-23T00:34:37Z'
  metrics: {}
  kind: news
---

# llm-typesafe 0.1a0

Release:   llm-typesafe 0.1a0  
         I built this new plugin for  LLM  to add support for  TypeSafe AI's new Jev model . Install it like this: 
  llm install llm-typesafe
  
 Then set an API key ( get one here , the waitlist seems to move pretty fast): 
  llm keys set typesafe
# Paste key
  
 And now you can ask yes/no "noul" questions like this: 
  llm -m jev 'Please refund my last payment.' \
  -s 'Does this message explicitly request a refund?'
  
 Output: 
  {"type": "noul", "noul": 0.99}
  
 Or choice questions like this: 
  cat message.txt  |  llm -m jev \
  -s   ' Which team should handle this message? If billing and technical issues both occur, choose billing. '   \
  -o answer_type choice \
  -o criteria   ' { 
     "billing":"Charges, invoices, payments, or refunds", 
     "technical":"Problems installing or using the product", 
     "other":"Neither category fits" 
   } '    
 Or scoring questions like this: 
  cat report.txt  |  llm -m jev \
  -s   ' How reproducible is the problem described in this report? '   \
  -o answer_type score \
  -o criteria   ' [ 
     "No reproduction instructions", 
     "Some instructions, but important steps are missing", 
     "Complete steps with expected and actual results" 
   ] '    
 See  the README  for more details. 
    
    
         Tags:  projects ,  llm ,  jev

## 笔记


