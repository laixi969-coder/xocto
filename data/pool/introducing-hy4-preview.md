---
slug: introducing-hy4-preview
name: Tencent Hunyuan
builder: ''
category: ''
summary_zh: 腾讯混元 Hy4 是开源权重的大语言模型，770B 总参数、49B 激活，支持 1M token 上下文，仅文本输入。相比 Hy3 规模大幅提升。
inspiration: ''
summary_en: Tencent Hunyuan Hy4 is an open-weight LLM with 770B total params, 49B active, 1M token context,
  text-only. Significant size increase from Hy3.
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
url: https://simonwillison.net/2026/Aug/29/hy4/
canonical_url: https://simonwillison.net/2026/Aug/29/hy4
summary: "Introducing Hy4 Preview   \nNew open weight text input (no vision)  LLM from Chinese company\
  \ Tencent today: 770B total parameters, 49B active parameters, 1M token context window,  1.56TB on Hugging\
  \ Face . \n This is a big size increase from their previous  Hy3  in July, which was 295B, 21B active,\
  \ 256,000 context, 598GB. \n I recently started using model chat templates to better understand their\
  \ capabilities. Here's Hy4's   chat_template.jinja  on Hugging Face, which includes this section: \n\
  \   {% -  if   not   reasoning_effort   is   defined   %} \n     {% -  set   reasoning_effort  =  'high'\
  \   %} \n {% -  elif   reasoning_effort   not   in  [ 'high' ,  'no_think' ]  %} \n     {% -  if   reasoning_effort\
  \   is   none   %} \n        {{- raise_exception('reasoning_effort error : None, should be no_think/high')\
  \ }}\n     {% -  else   %} \n        {{- raise_exception('reasoning_effort error : ' + reasoning_effort\
  \ + ', should be no_think/high') }}\n     {% -  endif   %} \n {% -  endif   %}   \n So it looks like\
  \ there are just two reasoning effort levels: \"high\" (the default) and \"no_think\" (reason by disabled).\
  \ \n I tried my \"Generate an SVG of a pelican riding a bicycle\" prompt with the default high reasoning\
  \  via OpenRouter  and  got this : \n   \n Quoting the reasoning trace: \n \n [...] Let's maybe add\
  \ a helmet? It could improve riding theme, but may obscure head. Maybe a small cycling cap or helmet?\
  \ The user didn't ask; can add red helmet? Might be cute. But pelican with big beak; a helmet might\
  \ obscure. Better maybe no. \n Maybe add sunglasses? no. \n Maybe add water? no. \n \n It's interesting\
  \ how the reasoning trace uses slightly truncated English, presumably because perfect grammar isn't\
  \ useful or token efficient for hidden reasoning text.\n\n\n     Tags:  ai ,  generative-ai ,  llms\
  \ ,  pelican-riding-a-bicycle ,  llm-reasoning ,  llm-release ,  ai-in-china"
first_seen: '2026-08-29T23:53:13Z'
last_seen: '2026-08-30T00:20:27Z'
status: market_context
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Aug/29/hy4/
  seen_at: '2026-08-30T00:20:27Z'
  metrics: {}
  kind: news
---

# Tencent Hunyuan

Introducing Hy4 Preview   
New open weight text input (no vision)  LLM from Chinese company Tencent today: 770B total parameters, 49B active parameters, 1M token context window,  1.56TB on Hugging Face . 
 This is a big size increase from their previous  Hy3  in July, which was 295B, 21B active, 256,000 context, 598GB. 
 I recently started using model chat templates to better understand their capabilities. Here's Hy4's   chat_template.jinja  on Hugging Face, which includes this section: 
   {% -  if   not   reasoning_effort   is   defined   %} 
     {% -  set   reasoning_effort  =  'high'   %} 
 {% -  elif   reasoning_effort   not   in  [ 'high' ,  'no_think' ]  %} 
     {% -  if   reasoning_effort   is   none   %} 
        {{- raise_exception('reasoning_effort error : None, should be no_think/high') }}
     {% -  else   %} 
        {{- raise_exception('reasoning_effort error : ' + reasoning_effort + ', should be no_think/high') }}
     {% -  endif   %} 
 {% -  endif   %}   
 So it looks like there are just two reasoning effort levels: "high" (the default) and "no_think" (reason by disabled). 
 I tried my "Generate an SVG of a pelican riding a bicycle" prompt with the default high reasoning  via OpenRouter  and  got this : 
   
 Quoting the reasoning trace: 
 
 [...] Let's maybe add a helmet? It could improve riding theme, but may obscure head. Maybe a small cycling cap or helmet? The user didn't ask; can add red helmet? Might be cute. But pelican with big beak; a helmet might obscure. Better maybe no. 
 Maybe add sunglasses? no. 
 Maybe add water? no. 
 
 It's interesting how the reasoning trace uses slightly truncated English, presumably because perfect grammar isn't useful or token efficient for hidden reasoning text.


     Tags:  ai ,  generative-ai ,  llms ,  pelican-riding-a-bicycle ,  llm-reasoning ,  llm-release ,  ai-in-china

## 笔记


