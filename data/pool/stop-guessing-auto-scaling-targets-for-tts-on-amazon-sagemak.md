---
slug: stop-guessing-auto-scaling-targets-for-tts-on-amazon-sagemak
name: Stop guessing auto scaling targets for TTS on Amazon SageMaker AI
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
url: https://aws.amazon.com/blogs/machine-learning/stop-guessing-auto-scaling-targets-for-tts-on-amazon-sagemaker-ai/
canonical_url: https://aws.amazon.com/blogs/machine-learning/stop-guessing-auto-scaling-targets-for-tts-on-amazon-sagemaker-ai
summary: A traffic spike hits your self-hosted text-to-speech (TTS) endpoint, and requests start queueing.
  Latency climbs past your service level objective (SLO) right when the most callers are listening. The
  auto scaling policy behind that endpoint was supposed to prevent this, but the target value it scales
  on was a guess, and guesses like that fail silently until real traffic proves them wrong. Get that number
  wrong, and it’s paid for in one of two ways, and neither shows up as an alarm. Guess too conservative,
  and the fleet runs GPU instances that sit mostly idle. That cost lands on every invoice but never trips
  an incident report. Guess too aggressive, and the fleet carries a risk nobody sees. Each instance holds
  more concurrent requests than it can serve inside its latency promise. Nothing looks wrong until a real
  traffic spike pushes queueing time past the SLO. That happens right when the most callers are listening.
  That’s the hidden gap. A policy that looks fine on the console can already be failing the people it’s
  supposed to serve. In this post, we deploy Kokoro-82M , an 82-million-parameter TTS model, as a custom
  container on an Amazon SageMaker AI real-time endpoint. AWS
first_seen: '2026-10-23T00:41:16Z'
last_seen: '2026-10-23T00:41:16Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/stop-guessing-auto-scaling-targets-for-tts-on-amazon-sagemaker-ai/
  seen_at: '2026-10-23T00:41:16Z'
  metrics: {}
  kind: news
---

# Stop guessing auto scaling targets for TTS on Amazon SageMaker AI

A traffic spike hits your self-hosted text-to-speech (TTS) endpoint, and requests start queueing. Latency climbs past your service level objective (SLO) right when the most callers are listening. The auto scaling policy behind that endpoint was supposed to prevent this, but the target value it scales on was a guess, and guesses like that fail silently until real traffic proves them wrong. Get that number wrong, and it’s paid for in one of two ways, and neither shows up as an alarm. Guess too conservative, and the fleet runs GPU instances that sit mostly idle. That cost lands on every invoice but never trips an incident report. Guess too aggressive, and the fleet carries a risk nobody sees. Each instance holds more concurrent requests than it can serve inside its latency promise. Nothing looks wrong until a real traffic spike pushes queueing time past the SLO. That happens right when the most callers are listening. That’s the hidden gap. A policy that looks fine on the console can already be failing the people it’s supposed to serve. In this post, we deploy Kokoro-82M , an 82-million-parameter TTS model, as a custom container on an Amazon SageMaker AI real-time endpoint. AWS

## 笔记


