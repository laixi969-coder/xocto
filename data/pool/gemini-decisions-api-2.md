---
slug: gemini-decisions-api-2
name: Gemini Decisions API
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
url: https://simonwillison.net/2026/Nov/11/gemini-decisions-api/
canonical_url: https://simonwillison.net/2026/Nov/11/gemini-decisions-api
summary: 'Gemini Decisions API Google join Jev and OpenAI in the decision model category with "Gemini
  Decision 1". This new model API is almost identical to Jev: it supports the same three types of questions
  (yes/no, choice, and rubric-scoring) and even reuses Jev''s term "Noul" for a yes/no question. It''s
  priced the same as the GPT-6 Luna decision model: 10 cents per million input tokens, and output is free.
  Jev remains the cheapest of the three, at 4.2 cents per million. Jev is text (and JSON) only. OpenAI
  can handle text and images. Gemini Decision 1 is fully multi-model: it covers text, images, audio, video,
  and PDFs. I tested it against video by passing these questions to it along with my Yonkers stomping
  robot video file: dragon: Does this video have a dragon in it? robot: Does this video have a robot in
  it? france: Is this video set in France? usa: Is this video set in the USA? Jev and OpenAI both return
  1.0 or 0.0 for yes/no questions, but Gemini insists on being a little less confident than that: { "dragon"
  : { "type" : " yes_no " , "probability" : 0.04976021841520312 }, "robot" : { "type" : "'
first_seen: '2026-11-12T03:00:03Z'
last_seen: '2026-11-12T03:00:03Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/11/gemini-decisions-api/
  seen_at: '2026-11-12T03:00:03Z'
  metrics: {}
  kind: news
---

# Gemini Decisions API

Gemini Decisions API Google join Jev and OpenAI in the decision model category with "Gemini Decision 1". This new model API is almost identical to Jev: it supports the same three types of questions (yes/no, choice, and rubric-scoring) and even reuses Jev's term "Noul" for a yes/no question. It's priced the same as the GPT-6 Luna decision model: 10 cents per million input tokens, and output is free. Jev remains the cheapest of the three, at 4.2 cents per million. Jev is text (and JSON) only. OpenAI can handle text and images. Gemini Decision 1 is fully multi-model: it covers text, images, audio, video, and PDFs. I tested it against video by passing these questions to it along with my Yonkers stomping robot video file: dragon: Does this video have a dragon in it? robot: Does this video have a robot in it? france: Is this video set in France? usa: Is this video set in the USA? Jev and OpenAI both return 1.0 or 0.0 for yes/no questions, but Gemini insists on being a little less confident than that: { "dragon" : { "type" : " yes_no " , "probability" : 0.04976021841520312 }, "robot" : { "type" : "

## 笔记


