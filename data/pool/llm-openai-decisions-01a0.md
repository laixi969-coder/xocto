---
slug: llm-openai-decisions-01a0
name: llm-openai-decisions 0.1a0
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
url: https://simonwillison.net/2026/Oct/6/llm-openai-decisions/
canonical_url: https://simonwillison.net/2026/Oct/6/llm-openai-decisions
summary: "Release:   llm-openai-decisions 0.1a0  \n         OpenAI released their new Jev-style  Decisions\
  \ API , as previously announced at last week's DevDay. \n Since I already have an  llm-typesafe  plugin\
  \ for talking to Jev, I had GPT-6 Astra read the new OpenAI API documentation and build an  llm-openai-decisions\
  \  plugin inspired by  llm-typesafe . \n Unlike Jev, the new  gpt-6-luna  decision model supports image\
  \ input in addition to text. Both models charge for input it and not for output: OpenAI's is 10 cents\
  \ per million input tokens, Jev's is 4.2 cents per million. \n Otherwise the API shape is  very  similar\
  \ to Jev, at least conceptually. Jev  supports three question types  for yes/no, choices, or scores.\
  \ OpenAI Decisions supports the same three types. \n Install the plugin like this: \n  llm install llm-openai-decisions\n\
  \  \n Here's an example query against an image attachment: \n  llm -m openai-decisions/gpt-6-luna \\\
  \n  -a https://static.simonwillison.net/static/2025/two-pelicans.jpg \\\n  -s   ' Does this image contain\
  \ any mammals? '    \n And example output: \n  { \"type\" :   \" predicate \"  ,  \"name\" :   \" evaluation\
  \ \"  ,  \"probability\" :  0.0 }  \n\n Consult  the README  for full details of how to run the other\
  \ types of questions. \n    \n    \n         Tags:  openai ,  llm ,  coding-agents ,  jev"
first_seen: '2026-10-06T23:04:13Z'
last_seen: '2026-10-07T01:32:55Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/6/llm-openai-decisions/
  seen_at: '2026-10-07T01:32:55Z'
  metrics: {}
  kind: news
---

# llm-openai-decisions 0.1a0

Release:   llm-openai-decisions 0.1a0  
         OpenAI released their new Jev-style  Decisions API , as previously announced at last week's DevDay. 
 Since I already have an  llm-typesafe  plugin for talking to Jev, I had GPT-6 Astra read the new OpenAI API documentation and build an  llm-openai-decisions  plugin inspired by  llm-typesafe . 
 Unlike Jev, the new  gpt-6-luna  decision model supports image input in addition to text. Both models charge for input it and not for output: OpenAI's is 10 cents per million input tokens, Jev's is 4.2 cents per million. 
 Otherwise the API shape is  very  similar to Jev, at least conceptually. Jev  supports three question types  for yes/no, choices, or scores. OpenAI Decisions supports the same three types. 
 Install the plugin like this: 
  llm install llm-openai-decisions
  
 Here's an example query against an image attachment: 
  llm -m openai-decisions/gpt-6-luna \
  -a https://static.simonwillison.net/static/2025/two-pelicans.jpg \
  -s   ' Does this image contain any mammals? '    
 And example output: 
  { "type" :   " predicate "  ,  "name" :   " evaluation "  ,  "probability" :  0.0 }  

 Consult  the README  for full details of how to run the other types of questions. 
    
    
         Tags:  openai ,  llm ,  coding-agents ,  jev

## 笔记


