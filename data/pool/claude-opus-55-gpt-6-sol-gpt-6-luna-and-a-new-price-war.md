---
slug: claude-opus-55-gpt-6-sol-gpt-6-luna-and-a-new-price-war
name: Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war
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
url: https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/
canonical_url: https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna
summary: "Yesterday was  Grok 4.7  ( pelicans ) and  MiMo v2.6 Flash/Pro  ( more pelicans ). Today Anthropic\
  \  released Claude Opus 5.5 , and around an hour later OpenAI  released GPT-6 Sol and GPT-6 Luna . It's\
  \ going to take a while to get a good read on all of these new models, but here are my impressions so\
  \ far. \n GPT-6 Sol and Luna are half the price of their GPT-5.6 equivalents \n GPT-5.6 Luna was already\
  \ my favorite model for building applications against, because it combined excellent performance with\
  \ being  really cheap . Somehow GPT-6 Luna is half the price of that again - and GPT-6 Sol had a similar\
  \ reduction compared to GPT-5.6 Sol. \n Here's what the pricing landscape looks like today: \n  \n \
  \  \n     \n       Model \n       Input \n       Cached input \n       Output \n     \n   \n   \n  \
  \   \n       GPT-6 Luna \n       $0.10/M \n       $0.01/M \n       $0.50/M \n     \n     \n       GPT-5.6\
  \ Luna \n       $0.20/M \n       $0.02/M \n       $1.20/M \n     \n     \n       Grok 4.7 \n       $2/M\
  \ \n       $0.50/M \n       $6/M \n     \n     \n       GPT-6 Sol \n       $2/M \n       $0.20/M \n\
  \       $10/M \n     \n     \n       GPT-5.6 Terra \n       $2/M \n       $0.20/M \n       $12/M \n\
  \     \n     \n       Claude Opus 5.5 \n       $4/M \n       $0.20/M \n       $20/M \n     \n     \n\
  \       GPT-5.6 Sol \n       $4/M \n       $0.40/M \n       $20/M \n     \n     \n       Claude Fable\
  \ 5.1 \n       $10/M \n       $0.25/M \n       $50/M \n     \n     \n       GPT-6 Astra \n       $10/M\
  \ \n       $1/M \n       $50/M \n     \n   \n  \n Note that GPT-5.6 has a scheduled 25% price increase\
  \ for November, so GPT-6 is half the price of the  promotional  pricing for those models. \n (With GPT-5.6\
  \ Terra priced the same as GPT-6 Sol, any remaining reasons to use Terra just evaporated.) \n It's hard\
  \ to overstate how competitive this pricing is. Grok 4.7 priced itself at $2/$6, less than half the\
  \ price of GPT-5.6 Sol, but is now equally priced to GPT-6 Sol on input and closer on output.  At $0.10/$0.50\
  \ GPT-6 Luna is one of the cheapest models OpenAI have ever released, beaten only by the far weaker\
  \ GPT-4.1 Nano ($0.10/$0.40, April 2025) and GPT-5 Nano ($0.05/$0.40, August 2025). \n I rendered  pelicans\
  \ for GPT-6 Luna  and  for GPT-6 Sol , then I combined them all together in  this comparison grid  along\
  \ with the GPT-5.6 pelicans. I like how you can instantly see that the 5.6 family chose bolder, brighter\
  \ colors, while the 6 family is a lot more muted. I still think GPT-6 Astra on max produced the best\
  \ pelican. \n   \n Claude Opus 5.5 got a price cut too \n Opus 5.5 looks like it addresses the biggest\
  \ complaints people had about Opus in terms of its communication style.  Thariq Shihipar : \n \n Opus\
  \ 5.5 is the result of your feedback. \n It communicates clearly, it's cheaper per token than Opus 5.0\
  \ with the intelligence of Fable 5.1 it's very token efficient and works across every effort level.\
  \ \n \n It's also meant to be  better at Blender . I'm looking forward to putting it through its paces\
  \ there. \n Opus 4.5, 4.6, 4.7, 4.8, and 5 all shared the same price: $5/million tokens for input and\
  \ $25/million for output. 5.5 is a 20% reduction - $4/million and $20/million. \n The price for cache\
  \ reads fell 60%. That's significant for longer agentic conversations, where 90%+ of input tokens are\
  \ processed at cached token prices. \n The new price for Opus 5.5 is the same as the price for GPT-5.6\
  \ Sol, but that was  before  OpenAI dropped their Sol prices by half. \n GPT-6 Astra and Claude Fable\
  \ 5.1 are both priced at $10/million input and $50/million output. The price war currently affects the\
  \ next tier of models below that. \n Anthropic say that Sonnet 5.5 and Haiku 5.5 are coming soon. It's\
  \ going to be interesting to see if Haiku can regain its price competitiveness at the lower end, given\
  \ current Haiku 4.5 is $1/$5 while the latest GPT-6 Luna is  one tenth  of that price at $0.10/$0.50.\
  \ \n Claude Opus 5.5 max over-thinks to the point of breaking \n In a first for my \" Generate an SVG\
  \ of a pelican riding a bicycle \" test, Claude Opus 5.5 at \"max\" thinking level failed to return\
  \ a response! \n It started by calling this \"a classic test request\", and then thought really,  really\
  \  hard about what it was doing: \n \n This is a classic test request, so I want to plan out a well-composed\
  \ pelican with its distinctive beak and pouch riding a bicycle with proper wheels, frame, and pedals,\
  \ set against a simple sky and ground backdrop. [...] \n Verifying the shin length checks out at roughly\
  \ 95.2, close enough. Now I'm working out the near leg path from hip to knee to ankle, then sketching\
  \ the foot shape resting on the pedal — outlining the heel, toe tips, and sole contour with a path using\
  \ lines and curves to sit naturally on the pedal surface around y=478-494. [...] \n I like the fish\
  \ sticking prominently out of the basket with the pelican eyeing it as a fun detail worth keeping. I'm\
  \ also confirming the eye placement near the bill base matches typical pelican anatomy, and considering\
  \ giving it a slightly happier expression. [...] \n The far leg reads correctly as passing behind the\
  \ frame, so I'm moving on to check the chainring teeth and confirm layer ordering—the far crank arm\
  \ should be mostly hidden by the seat tube and chainring. I'm settling on the final SVG's width and\
  \ height attributes alongside the viewBox to ensure proper scaling, noting there's no text so no font-family\
  \ is needed. [...] \n \n I was so excited to see this pelican... but then it  stopped . Opus 5.5 has\
  \ a 128,000 maximum output token limit (as do the other Claude models), and it hit that while it was\
  \ still reasoning about the SVG! \n I tried a second time and got the same result. This makes me suspect\
  \ that \"max\" is effectively useless - if it over-thinks to breaking point on a stupid SVG prompt I\
  \ don't trust it not to do the same for more interesting work. \n (Those two failures each cost me \
  \ $2.56  and took nearly 20 minutes.) \n Fable 5.1 on \"max\" didn't over-think and did give me  the\
  \ best pelican I've seen  from any Anthropic model. \n Here are  the Opus 5.5 pelicans , excluding 5.5\
  \ max. \n I also built  this comparison grid  comparing them with pelicans by Opus 5, Fable 5.1, and\
  \ Sonnet 5: \n   \n Comparing different model vendors by how well they draw a pelican riding a bicycle\
  \ may not make much sense now (if it ever did), but I'm still finding value in using them for comparisons\
  \ of the same model families at different reasoning levels. \n I'm now using GPT-6 Sol and Claude Opus\
  \ 5.5 as my default models in Codex and Claude Code. I've upgraded the Datasette Agent demo at  agent.datasette.io\
  \  to use GPT-6 Luna, and it seems to be fast and competent at both SQL queries and building HTML and\
  \ JavaScript for  Datasette Apps . \n    \n         Tags:  ai ,  openai ,  generative-ai ,  llms , \
  \ anthropic ,  claude ,  llm-pricing ,  pelican-riding-a-bicycle ,  gpt"
first_seen: '2026-09-22T23:46:41Z'
last_seen: '2026-09-23T00:34:37Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/
  seen_at: '2026-09-23T00:34:37Z'
  metrics: {}
  kind: news
---

# Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war

Yesterday was  Grok 4.7  ( pelicans ) and  MiMo v2.6 Flash/Pro  ( more pelicans ). Today Anthropic  released Claude Opus 5.5 , and around an hour later OpenAI  released GPT-6 Sol and GPT-6 Luna . It's going to take a while to get a good read on all of these new models, but here are my impressions so far. 
 GPT-6 Sol and Luna are half the price of their GPT-5.6 equivalents 
 GPT-5.6 Luna was already my favorite model for building applications against, because it combined excellent performance with being  really cheap . Somehow GPT-6 Luna is half the price of that again - and GPT-6 Sol had a similar reduction compared to GPT-5.6 Sol. 
 Here's what the pricing landscape looks like today: 
  
   
     
       Model 
       Input 
       Cached input 
       Output 
     
   
   
     
       GPT-6 Luna 
       $0.10/M 
       $0.01/M 
       $0.50/M 
     
     
       GPT-5.6 Luna 
       $0.20/M 
       $0.02/M 
       $1.20/M 
     
     
       Grok 4.7 
       $2/M 
       $0.50/M 
       $6/M 
     
     
       GPT-6 Sol 
       $2/M 
       $0.20/M 
       $10/M 
     
     
       GPT-5.6 Terra 
       $2/M 
       $0.20/M 
       $12/M 
     
     
       Claude Opus 5.5 
       $4/M 
       $0.20/M 
       $20/M 
     
     
       GPT-5.6 Sol 
       $4/M 
       $0.40/M 
       $20/M 
     
     
       Claude Fable 5.1 
       $10/M 
       $0.25/M 
       $50/M 
     
     
       GPT-6 Astra 
       $10/M 
       $1/M 
       $50/M 
     
   
  
 Note that GPT-5.6 has a scheduled 25% price increase for November, so GPT-6 is half the price of the  promotional  pricing for those models. 
 (With GPT-5.6 Terra priced the same as GPT-6 Sol, any remaining reasons to use Terra just evaporated.) 
 It's hard to overstate how competitive this pricing is. Grok 4.7 priced itself at $2/$6, less than half the price of GPT-5.6 Sol, but is now equally priced to GPT-6 Sol on input and closer on output.  At $0.10/$0.50 GPT-6 Luna is one of the cheapest models OpenAI have ever released, beaten only by the far weaker GPT-4.1 Nano ($0.10/$0.40, April 2025) and GPT-5 Nano ($0.05/$0.40, August 2025). 
 I rendered  pelicans for GPT-6 Luna  and  for GPT-6 Sol , then I combined them all together in  this comparison grid  along with the GPT-5.6 pelicans. I like how you can instantly see that the 5.6 family chose bolder, brighter colors, while the 6 family is a lot more muted. I still think GPT-6 Astra on max produced the best pelican. 
   
 Claude Opus 5.5 got a price cut too 
 Opus 5.5 looks like it addresses the biggest complaints people had about Opus in terms of its communication style.  Thariq Shihipar : 
 
 Opus 5.5 is the result of your feedback. 
 It communicates clearly, it's cheaper per token than Opus 5.0 with the intelligence of Fable 5.1 it's very token efficient and works across every effort level. 
 
 It's also meant to be  better at Blender . I'm looking forward to putting it through its paces there. 
 Opus 4.5, 4.6, 4.7, 4.8, and 5 all shared the same price: $5/million tokens for input and $25/million for output. 5.5 is a 20% reduction - $4/million and $20/million. 
 The price for cache reads fell 60%. That's significant for longer agentic conversations, where 90%+ of input tokens are processed at cached token prices. 
 The new price for Opus 5.5 is the same as the price for GPT-5.6 Sol, but that was  before  OpenAI dropped their Sol prices by half. 
 GPT-6 Astra and Claude Fable 5.1 are both priced at $10/million input and $50/million output. The price war currently affects the next tier of models below that. 
 Anthropic say that Sonnet 5.5 and Haiku 5.5 are coming soon. It's going to be interesting to see if Haiku can regain its price competitiveness at the lower end, given current Haiku 4.5 is $1/$5 while the latest GPT-6 Luna is  one tenth  of that price at $0.10/$0.50. 
 Claude Opus 5.5 max over-thinks to the point of breaking 
 In a first for my " Generate an SVG of a pelican riding a bicycle " test, Claude Opus 5.5 at "max" thinking level failed to return a response! 
 It started by calling this "a classic test request", and then thought really,  really  hard about what it was doing: 
 
 This is a classic test request, so I want to plan out a well-composed pelican with its distinctive beak and pouch riding a bicycle with proper wheels, frame, and pedals, set against a simple sky and ground backdrop. [...] 
 Verifying the shin length checks out at roughly 95.2, close enough. Now I'm working out the near leg path from hip to knee to ankle, then sketching the foot shape resting on the pedal — outlining the heel, toe tips, and sole contour with a path using lines and curves to sit naturally on the pedal surface around y=478-494. [...] 
 I like the fish sticking prominently out of the basket with the pelican eyeing it as a fun detail worth keeping. I'm also confirming the eye placement near the bill base matches typical pelican anatomy, and considering giving it a slightly happier expression. [...] 
 The far leg reads correctly as passing behind the frame, so I'm moving on to check the chainring teeth and confirm layer ordering—the far crank arm should be mostly hidden by the seat tube and chainring. I'm settling on the final SVG's width and height attributes alongside the viewBox to ensure proper scaling, noting there's no text so no font-family is needed. [...] 
 
 I was so excited to see this pelican... but then it  stopped . Opus 5.5 has a 128,000 maximum output token limit (as do the other Claude models), and it hit that while it was still reasoning about the SVG! 
 I tried a second time and got the same result. This makes me suspect that "max" is effectively useless - if it over-thinks to breaking point on a stupid SVG prompt I don't trust it not to do the same for more interesting work. 
 (Those two failures each cost me  $2.56  and took nearly 20 minutes.) 
 Fable 5.1 on "max" didn't over-think and did give me  the best pelican I've seen  from any Anthropic model. 
 Here are  the Opus 5.5 pelicans , excluding 5.5 max. 
 I also built  this comparison grid  comparing them with pelicans by Opus 5, Fable 5.1, and Sonnet 5: 
   
 Comparing different model vendors by how well they draw a pelican riding a bicycle may not make much sense now (if it ever did), but I'm still finding value in using them for comparisons of the same model families at different reasoning levels. 
 I'm now using GPT-6 Sol and Claude Opus 5.5 as my default models in Codex and Claude Code. I've upgraded the Datasette Agent demo at  agent.datasette.io  to use GPT-6 Luna, and it seems to be fast and competent at both SQL queries and building HTML and JavaScript for  Datasette Apps . 
    
         Tags:  ai ,  openai ,  generative-ai ,  llms ,  anthropic ,  claude ,  llm-pricing ,  pelican-riding-a-bicycle ,  gpt

## 笔记


