---
slug: claude-fable-51-made-me-a-really-nice-animated-pelican
name: Claude Fable 5.1 made me a really nice animated pelican
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
url: https://simonwillison.net/2026/Sep/1/claude-fable-5-1/
canonical_url: https://simonwillison.net/2026/Sep/1/claude-fable-5-1
summary: "Today is  Claude Fable (and Mythos) 5.1 day . Anthropic say that Fable 5.1 \"sets a new standard\
  \ for coding, knowledge work, and long-running problem-solving tasks\". Their announcement spends a\
  \ notable amount of time on scientific research, boasting of a 52.6% score on the brand new  Terminal-Bench-Science\
  \ 0.1  benchmark (first announced  on August 27th ), up from 24.7% for Fable 5, 29.0% for Opus 5 and\
  \ 22.4% for GPT-5.6 Sol. Other benchmarks show slightly improved scores, but none as impressive as the\
  \ Science one. \n But how well can it pelican? \n Back in July  I wrote about  how I was losing faith\
  \ in the pelican benchmark - its connection to how good the models were at other tasks didn't seem to\
  \ hold as strongly as it did  back in 2025 . The most interesting insights I get from it now are comparisons\
  \ within model families, and particularly comparisons for the same prompt at different reasoning effort\
  \ levels. \n Fable 5.1 has five reasoning levels: low, medium, high, xhigh, max - and no option to turn\
  \ off reasoning entirely. \n I fixed  an issue  in  llm-anthropic  which caused reasoning traces not\
  \ to be correctly recorded, then ran some prompts. \n Here's  the full set of pelicans  for all of the\
  \ reasoning levels, each with the full reasoning transcript. I'll replicate them here: \n Low and medium,\
  \ both without reasoning? \n Next, a bit of a mystery. This is what I got for effort  low : \n   \n\
  \ The  transcript  doesn't show any summarized reasoning tokens, and the output token count is 1,998.\
  \ With Claude that output token count includes reasoning tokens. It took 23.8 seconds and cost  10.017\
  \ cents . \n I bumped that up to  medium  and got this: \n   \n Weirdly, that one also shows  no reasoning\
  \ text   and used 1,977 output tokens - 21 tokens  less  than  low . It took 23 seconds and cost  9.912\
  \ cents . \n So for this particular prompt (\"Generate an SVG of a pelican riding a bicycle\") Fable\
  \ 5.1 appeared to skip reasoning entirely at both  low  and  medium  settings. \n High \n Here's  high\
  \  - 29.6 seconds, 2,612 output tokens,  13.087 cents : \n   \n This one did do a  bit  of reasoning,\
  \  summary here : \n \n I'm planning the SVG layout for a pelican riding a bicycle, with a sky and ground\
  \ background, a bicycle with two spoked wheels, frame, seat and handlebars, and a white-bodied pelican\
  \ with a long neck and orange beak positioned on top. \n \n Really not much difference from  low  and\
  \  medium , though. \n Extra High \n At  xhigh  things got  radically  different.  36,767 output tokens,\
  \ 7 minutes 51 seconds,  $1.83 ! \n   \n The reasoning trace  is pretty lengthy , and includes details\
  \ like this: \n \n Adding the eye, wings stretching down to the handlebar grip, orange legs reaching\
  \ to the pedals, and a small tail feather, while keeping the pelican intentionally oversized compared\
  \ to the bike for comic effect. [...] \n I'll accept the slight thickness as charming rather than overengineering\
  \ it. \n \n Max \n Setting effort to  max  gave me the best pelican I've seen from any of Anthropic's\
  \ models. 65,927 output tokens, 13 minutes and 54 seconds,  $3.30 : \n   \n There's a lot to like about\
  \ this. The  background is tasteful, the legs are clearly on either side of the frame, the feet are\
  \ on the pedals, the wing is on the handlebars, the pelican has a cute blue hat and there's a basket\
  \ with a fish. \n It's still not showing nearly the same level of flair  as Gemini 3.7 Flash , but I\
  \ didn't  ask  for flair - I asked for an SVG, and that's what I got. \n Some highlights from  that\
  \ reasoning trace : \n \n Adding pedal shapes near both feet, with the far foot on the second leg partially\
  \ visible behind the frame. I'm considering whether to add a small scarf or cap for extra character,\
  \ but leaning toward keeping it simple to avoid clutter. \n Now I'm debating a bicycle helmet on the\
  \ head versus the pelican's signature crest—the beak and pouch already read clearly as \"pelican,\"\
  \ so a helmet could reinforce the bicycle theme without losing identity, though it might compete with\
  \ the crest for visual space. \n I realize the beak at (484,84) would overlap with the dome helmet,\
  \ so I need to shrink the helmet so it only covers the top of the head, adjusting its arc endpoints\
  \ to sit higher and narrower so the beak can attach cleanly at the front without collision. [...] \n\
  \ I'm adding a darker tip region to represent the primary feathers, then reconsidering the trailing\
  \ edge to include scalloped feather curves instead of one smooth line for a more natural look. [...]\
  \ \n Now I'm checking the vent line placements on the helmet, making sure they sit far enough inside\
  \ the helmet's edge given the stroke width and rounded caps, and confirming each vent stays within the\
  \ helmet's circular boundary. [...] \n I decide skipping a handlebar bell and tire highlights since\
  \ they're unnecessary additions. Now I'm reconsidering the front fork's curve — the current control\
  \ point pulls the shape backward when it should bow forward for a proper rake, so I need to shift the\
  \ control point rightward to fix the fork's lean. \n \n OK, let's animate it \n On Hacker News,  swalsh\
  \ commented  on that Max pelican: \n \n Now that it's a solved benchmark, can we get the animated version?\
  \ \n \n I didn't want to spend another $3 so I took the Max pelican and piped it into the default thinking\
  \ level of High: \n  llm logs -cx  |  llm -m claude-fable-5.1 -s   ' animate this '    \n 6,121 input,\
  \ 26,201 output =  $1.37 . The result  looked like this , exported here as video since some people have\
  \ trouble viewing animated SVGs: \n  \n     \n    Your browser does not support HTML5 video.\n   \n\
  \ \n\n The wheels in the video are rotating in the wrong direction, but I think that's an artifact of\
  \ the conversion to MP4 - they seem to be going in the correct direction in the original SVG. \n   \
  \ \n         Tags:  ai ,  generative-ai ,  llms ,  anthropic ,  claude ,  pelican-riding-a-bicycle ,\
  \  llm-reasoning ,  llm-release"
first_seen: '2026-09-01T23:57:28Z'
last_seen: '2026-09-02T00:14:54Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/1/claude-fable-5-1/
  seen_at: '2026-09-02T00:14:54Z'
  metrics: {}
  kind: news
---

# Claude Fable 5.1 made me a really nice animated pelican

Today is  Claude Fable (and Mythos) 5.1 day . Anthropic say that Fable 5.1 "sets a new standard for coding, knowledge work, and long-running problem-solving tasks". Their announcement spends a notable amount of time on scientific research, boasting of a 52.6% score on the brand new  Terminal-Bench-Science 0.1  benchmark (first announced  on August 27th ), up from 24.7% for Fable 5, 29.0% for Opus 5 and 22.4% for GPT-5.6 Sol. Other benchmarks show slightly improved scores, but none as impressive as the Science one. 
 But how well can it pelican? 
 Back in July  I wrote about  how I was losing faith in the pelican benchmark - its connection to how good the models were at other tasks didn't seem to hold as strongly as it did  back in 2025 . The most interesting insights I get from it now are comparisons within model families, and particularly comparisons for the same prompt at different reasoning effort levels. 
 Fable 5.1 has five reasoning levels: low, medium, high, xhigh, max - and no option to turn off reasoning entirely. 
 I fixed  an issue  in  llm-anthropic  which caused reasoning traces not to be correctly recorded, then ran some prompts. 
 Here's  the full set of pelicans  for all of the reasoning levels, each with the full reasoning transcript. I'll replicate them here: 
 Low and medium, both without reasoning? 
 Next, a bit of a mystery. This is what I got for effort  low : 
   
 The  transcript  doesn't show any summarized reasoning tokens, and the output token count is 1,998. With Claude that output token count includes reasoning tokens. It took 23.8 seconds and cost  10.017 cents . 
 I bumped that up to  medium  and got this: 
   
 Weirdly, that one also shows  no reasoning text   and used 1,977 output tokens - 21 tokens  less  than  low . It took 23 seconds and cost  9.912 cents . 
 So for this particular prompt ("Generate an SVG of a pelican riding a bicycle") Fable 5.1 appeared to skip reasoning entirely at both  low  and  medium  settings. 
 High 
 Here's  high  - 29.6 seconds, 2,612 output tokens,  13.087 cents : 
   
 This one did do a  bit  of reasoning,  summary here : 
 
 I'm planning the SVG layout for a pelican riding a bicycle, with a sky and ground background, a bicycle with two spoked wheels, frame, seat and handlebars, and a white-bodied pelican with a long neck and orange beak positioned on top. 
 
 Really not much difference from  low  and  medium , though. 
 Extra High 
 At  xhigh  things got  radically  different.  36,767 output tokens, 7 minutes 51 seconds,  $1.83 ! 
   
 The reasoning trace  is pretty lengthy , and includes details like this: 
 
 Adding the eye, wings stretching down to the handlebar grip, orange legs reaching to the pedals, and a small tail feather, while keeping the pelican intentionally oversized compared to the bike for comic effect. [...] 
 I'll accept the slight thickness as charming rather than overengineering it. 
 
 Max 
 Setting effort to  max  gave me the best pelican I've seen from any of Anthropic's models. 65,927 output tokens, 13 minutes and 54 seconds,  $3.30 : 
   
 There's a lot to like about this. The  background is tasteful, the legs are clearly on either side of the frame, the feet are on the pedals, the wing is on the handlebars, the pelican has a cute blue hat and there's a basket with a fish. 
 It's still not showing nearly the same level of flair  as Gemini 3.7 Flash , but I didn't  ask  for flair - I asked for an SVG, and that's what I got. 
 Some highlights from  that reasoning trace : 
 
 Adding pedal shapes near both feet, with the far foot on the second leg partially visible behind the frame. I'm considering whether to add a small scarf or cap for extra character, but leaning toward keeping it simple to avoid clutter. 
 Now I'm debating a bicycle helmet on the head versus the pelican's signature crest—the beak and pouch already read clearly as "pelican," so a helmet could reinforce the bicycle theme without losing identity, though it might compete with the crest for visual space. 
 I realize the beak at (484,84) would overlap with the dome helmet, so I need to shrink the helmet so it only covers the top of the head, adjusting its arc endpoints to sit higher and narrower so the beak can attach cleanly at the front without collision. [...] 
 I'm adding a darker tip region to represent the primary feathers, then reconsidering the trailing edge to include scalloped feather curves instead of one smooth line for a more natural look. [...] 
 Now I'm checking the vent line placements on the helmet, making sure they sit far enough inside the helmet's edge given the stroke width and rounded caps, and confirming each vent stays within the helmet's circular boundary. [...] 
 I decide skipping a handlebar bell and tire highlights since they're unnecessary additions. Now I'm reconsidering the front fork's curve — the current control point pulls the shape backward when it should bow forward for a proper rake, so I need to shift the control point rightward to fix the fork's lean. 
 
 OK, let's animate it 
 On Hacker News,  swalsh commented  on that Max pelican: 
 
 Now that it's a solved benchmark, can we get the animated version? 
 
 I didn't want to spend another $3 so I took the Max pelican and piped it into the default thinking level of High: 
  llm logs -cx  |  llm -m claude-fable-5.1 -s   ' animate this '    
 6,121 input, 26,201 output =  $1.37 . The result  looked like this , exported here as video since some people have trouble viewing animated SVGs: 
  
     
    Your browser does not support HTML5 video.
   
 

 The wheels in the video are rotating in the wrong direction, but I think that's an artifact of the conversion to MP4 - they seem to be going in the correct direction in the original SVG. 
    
         Tags:  ai ,  generative-ai ,  llms ,  anthropic ,  claude ,  pelican-riding-a-bicycle ,  llm-reasoning ,  llm-release

## 笔记


