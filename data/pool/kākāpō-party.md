---
slug: kākāpō-party
name: Kākāpō Party
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
url: https://simonwillison.net/2026/Sep/26/kakapo-party/
canonical_url: https://simonwillison.net/2026/Sep/26/kakapo-party
summary: "Tool:   Kākāpō Party  \n         I gave presented a closing keynote for the  WeAreDevelopers\
  \ World Congress North America  yesterday. As  a STAR moment  I decided to weave in references to the\
  \ record breaking  kākāpō breeding season  we had in 2026. \n For my closing slide I wanted to celebrate,\
  \ and I had seen some buzz around how good Claude Opus 5.5 was at creating pixel art animations. So\
  \ I rounded up three Kakapo photos from Google image search and dropped them into Claude with this prompt:\
  \ \n \n  Here are some photos of kakapo parrots just to remind you what they look like  \n  I need you\
  \ to make an animation in animated pixel art on HTML 5 canvas of obviously pixel art kakapo jumping\
  \ up and down having a party with confetti and suchlike - there should be at least 20 of them  \n \n\
  \ Here's  the transcript , and this is the  resulting page . It's pretty great! \n I wanted to embed\
  \ it in a Keynote presentation file, so I downloaded the HTML and told a local Claude Code session:\
  \ \n \n  Make me a video of file:///Users/simon/Downloads/kakapo-party.html - you need to load it in\
  \ a browser and click on it a few times to get the confetti effect, the video should be 15s long  \n\
  \  don't start clicking until 3s in  \n  make sure several clicks are spread around the clickable area\
  \  \n \n Claude Code used Playwright ( transcript here ) and produced this video, which was exactly\
  \ what I needed for my final slide: \n  \n     \n    Your browser does not support HTML5 video.\n  \
  \ \n \n\n Here's the full Playwright script it used, which was pleasingly short: \n  # /// script \n\
  \ # dependencies = [\"playwright\"] \n # /// \n import   time \n from   playwright . sync_api   import\
  \   sync_playwright \n W ,  H   =   1280 ,  720 \n # Canvas fills the viewport; spread clicks across\
  \ corners, edges and centre \n clicks   =  [\n    ( 3.0 ,  640 ,  360 ),    # centre \n    ( 4.2 , \
  \ 160 ,  120 ),    # top-left \n    ( 5.4 ,  1120 ,  120 ),   # top-right \n    ( 6.6 ,  180 ,  600\
  \ ),    # bottom-left \n    ( 7.8 ,  1100 ,  600 ),   # bottom-right \n    ( 9.0 ,  640 ,  100 ),  \
  \  # top-centre \n    ( 10.0 ,  380 ,  380 ),   # mid-left \n    ( 11.0 ,  900 ,  380 ),   # mid-right\
  \ \n    ( 12.2 ,  640 ,  620 ),   # bottom-centre \n    ( 13.2 ,  640 ,  300 ),   # finale centre \n\
  ]\n with   sync_playwright ()  as   p :\n     b   =   p . chromium . launch ()\n     ctx   =   b . new_context\
  \ ( viewport  = { \"width\" : W , \"height\" : H },  record_video_dir  =  \"vids\" ,  record_video_size\
  \  = { \"width\" : W , \"height\" : H })\n     page   =   ctx . new_page ()\n     t0   =   time . time\
  \ ()\n     page . goto ( \"file:///Users/simon/Downloads/kakapo-party.html\" )\n     for   t , x , y\
  \   in   clicks :\n         time . sleep ( max ( 0 ,  t  - ( time . time () -  t0 )))\n         page\
  \ . mouse . click ( x , y )\n     time . sleep ( max ( 0 ,  16.0  - ( time . time () -  t0 )))\n   \
  \  ctx . close ();  b . close () \n    \n    \n         Tags:  animation ,  speaking ,  ai ,  kakapo\
  \ ,  playwright ,  generative-ai ,  llms ,  anthropic ,  claude ,  claude-code"
first_seen: '2026-09-26T23:39:06Z'
last_seen: '2026-09-27T00:36:45Z'
status: rejected
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/26/kakapo-party/
  seen_at: '2026-09-27T00:36:45Z'
  metrics: {}
  kind: news
---

# Kākāpō Party

Tool:   Kākāpō Party  
         I gave presented a closing keynote for the  WeAreDevelopers World Congress North America  yesterday. As  a STAR moment  I decided to weave in references to the record breaking  kākāpō breeding season  we had in 2026. 
 For my closing slide I wanted to celebrate, and I had seen some buzz around how good Claude Opus 5.5 was at creating pixel art animations. So I rounded up three Kakapo photos from Google image search and dropped them into Claude with this prompt: 
 
  Here are some photos of kakapo parrots just to remind you what they look like  
  I need you to make an animation in animated pixel art on HTML 5 canvas of obviously pixel art kakapo jumping up and down having a party with confetti and suchlike - there should be at least 20 of them  
 
 Here's  the transcript , and this is the  resulting page . It's pretty great! 
 I wanted to embed it in a Keynote presentation file, so I downloaded the HTML and told a local Claude Code session: 
 
  Make me a video of file:///Users/simon/Downloads/kakapo-party.html - you need to load it in a browser and click on it a few times to get the confetti effect, the video should be 15s long  
  don't start clicking until 3s in  
  make sure several clicks are spread around the clickable area  
 
 Claude Code used Playwright ( transcript here ) and produced this video, which was exactly what I needed for my final slide: 
  
     
    Your browser does not support HTML5 video.
   
 

 Here's the full Playwright script it used, which was pleasingly short: 
  # /// script 
 # dependencies = ["playwright"] 
 # /// 
 import   time 
 from   playwright . sync_api   import   sync_playwright 
 W ,  H   =   1280 ,  720 
 # Canvas fills the viewport; spread clicks across corners, edges and centre 
 clicks   =  [
    ( 3.0 ,  640 ,  360 ),    # centre 
    ( 4.2 ,  160 ,  120 ),    # top-left 
    ( 5.4 ,  1120 ,  120 ),   # top-right 
    ( 6.6 ,  180 ,  600 ),    # bottom-left 
    ( 7.8 ,  1100 ,  600 ),   # bottom-right 
    ( 9.0 ,  640 ,  100 ),    # top-centre 
    ( 10.0 ,  380 ,  380 ),   # mid-left 
    ( 11.0 ,  900 ,  380 ),   # mid-right 
    ( 12.2 ,  640 ,  620 ),   # bottom-centre 
    ( 13.2 ,  640 ,  300 ),   # finale centre 
]
 with   sync_playwright ()  as   p :
     b   =   p . chromium . launch ()
     ctx   =   b . new_context ( viewport  = { "width" : W , "height" : H },  record_video_dir  =  "vids" ,  record_video_size  = { "width" : W , "height" : H })
     page   =   ctx . new_page ()
     t0   =   time . time ()
     page . goto ( "file:///Users/simon/Downloads/kakapo-party.html" )
     for   t , x , y   in   clicks :
         time . sleep ( max ( 0 ,  t  - ( time . time () -  t0 )))
         page . mouse . click ( x , y )
     time . sleep ( max ( 0 ,  16.0  - ( time . time () -  t0 )))
     ctx . close ();  b . close () 
    
    
         Tags:  animation ,  speaking ,  ai ,  kakapo ,  playwright ,  generative-ai ,  llms ,  anthropic ,  claude ,  claude-code

## 笔记


