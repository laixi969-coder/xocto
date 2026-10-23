---
slug: stream-low-latency-speech-from-ai-agents-using-kokoro-tts-on
name: Stream low-latency speech from AI agents using Kokoro TTS on Amazon SageMaker AI
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
url: https://aws.amazon.com/blogs/machine-learning/stream-low-latency-speech-from-ai-agents-using-kokoro-tts-on-amazon-sagemaker-ai/
canonical_url: https://aws.amazon.com/blogs/machine-learning/stream-low-latency-speech-from-ai-agents-using-kokoro-tts-on-amazon-sagemaker-ai
summary: A customer asks an AI voice agent a question and waits. The agent already has an answer, it’s
  midway through generating a long, multi-paragraph response, but the customer hears nothing for five
  seconds. By the time an answer arrives, the customer is frustrated, confused, and no longer paying attention.
  Text-to-speech integrations create exactly that gap. A one-sentence response might generate in 600 milliseconds,
  but the full response takes five seconds, and the integration waits for all of it before synthesis starts.
  This post shows how to close that gap. We stream each sentence to a hosted Kokoro-82M text-to-speech
  (TTS) model on Amazon SageMaker AI as soon as an agent produces it, so synthesis begins on sentence
  one instead of the finished response. Getting that audio back to a browser needs its own solution too,
  so we also cover both transports for doing it and what each costs in practice. Solution overview This
  solution closes the gap by streaming synthesis alongside generation instead of waiting for it to finish.
  As the agent produces each sentence, that sentence streams immediately to a hosted Kokoro-82M text-to-speech
  model, so audio playback can start before the agent finishes speaking its full response. Kokoro-82M
  holds only
first_seen: '2026-10-23T00:41:16Z'
last_seen: '2026-10-23T00:41:16Z'
status: pending_filter
sources:
- officialfeeds
sightings:
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/stream-low-latency-speech-from-ai-agents-using-kokoro-tts-on-amazon-sagemaker-ai/
  seen_at: '2026-10-23T00:41:16Z'
  metrics: {}
  kind: news
---

# Stream low-latency speech from AI agents using Kokoro TTS on Amazon SageMaker AI

A customer asks an AI voice agent a question and waits. The agent already has an answer, it’s midway through generating a long, multi-paragraph response, but the customer hears nothing for five seconds. By the time an answer arrives, the customer is frustrated, confused, and no longer paying attention. Text-to-speech integrations create exactly that gap. A one-sentence response might generate in 600 milliseconds, but the full response takes five seconds, and the integration waits for all of it before synthesis starts. This post shows how to close that gap. We stream each sentence to a hosted Kokoro-82M text-to-speech (TTS) model on Amazon SageMaker AI as soon as an agent produces it, so synthesis begins on sentence one instead of the finished response. Getting that audio back to a browser needs its own solution too, so we also cover both transports for doing it and what each costs in practice. Solution overview This solution closes the gap by streaming synthesis alongside generation instead of waiting for it to finish. As the agent produces each sentence, that sentence streams immediately to a hosted Kokoro-82M text-to-speech model, so audio playback can start before the agent finishes speaking its full response. Kokoro-82M holds only

## 笔记


