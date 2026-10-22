---
slug: openai-openai-python-v3360
name: 'openai/openai-python: v3.36.0'
builder: openai
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
inspiration_en: ''
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/openai/openai-python/releases/tag/v3.36.0
canonical_url: https://github.com/openai/openai-python/releases/tag/v3.36.0
summary: '## [3.36.0](https://github.com/openai/openai-python/compare/v3.35.1...v3.36.0) (2026-10-21)



  ### Features


  * add Vertex AI support for the Responses API ([#4139](https://github.com/openai/openai-python/issues/4139))
  ([3e63d33](https://github.com/openai/openai-python/commit/3e63d33f6258f47285007aaee30df251d5127820))

  * **api:** add 30-minute cache-write usage counts ([#4111](https://github.com/openai/openai-python/issues/4111))
  ([5589146](https://github.com/openai/openai-python/commit/5589146d738e0c38758e117b8383a02c2e4e2ee7))

  * **api:** add compaction trigger IDs ([#4122](https://github.com/openai/openai-python/issues/4122))
  ([0e5794d](https://github.com/openai/openai-python/commit/0e5794dc48b8f8d51f6047f8a0b1814eb1e65850))

  * **api:** add custom voice consent management ([#4135](https://github.com/openai/openai-python/issues/4135))
  ([de6d70d](https://github.com/openai/openai-python/commit/de6d70d5c50ef1b9d3e5068b6e25ea52f447a8cb))

  * **types:** prepare native synchronous WebSocket option type ([#4118](https://github.com/openai/openai-python/issues/4118))
  ([90c0bac](https://github.com/openai/openai-python/commit/90c0bacc07ddd5662598db52b3c3011973011973))



  ### Bug Fixes


  * **api:** accept canonical batch responses in strict mode ([#4106](https://github.com/openai/openai-python/issues/4106))
  ([6eaa90e](https://github.com/openai/openai-python/commit/6eaa90ee20b40bbe84a5b1a5031d7cf672c7d368))

  * clean up failed WebSocket setup and honor native options ([#4121](https://github.com/openai/openai-python/issues/4121))
  ([b1a1a10](https://github.com/openai/openai-python/commit/b1a1a100d38d84dd556319e207880d85d23559cd))

  * end sync WebSocket recovery when an attempt is interrupted ([#4129](https://github.com/openai/openai-python/issues/4129))
  ([337769b](https://github.com/openai/openai-python/commit/337769b3daf5772cf54cf11a14c17ff5b7a3ac27))

  * honor timed Translation receives during terminal cleanup ([#4132](https://github.com/openai/openai-python/issues/4132))
  ([ca54146](https://github.com/openai/openai-python/commit/ca541462ba20dadb66eea6c67775f186dfb17e33))

  * preserve client headers in legacy Beta Realtime connections ([#4130](https://github.com/openai/openai-python/issues/4130))
  ([8a2a2e0](https://github.com/openai/openai-python/commit/8a2a2e0c4fe76297a5dd2395e05ca473561644ac))

  * preserve declared aliases during Pydantic v1 validation ([#4119](https://github.com/openai/openai-python/issues/4119))
  ([8b1cac9](https://github.com/openai/openai-python/commit/8b1cac931ccb32203010471b1f9d82e5c9957cff))

  * preserve Vertex API root for response lifecycle ([#4140](https://github.com/openai/openai-python/issues/4140))
  ([c2b14f5](https://github.com/openai/openai-python/commit/c2b14f538de7af908d8f1fd50e6af60c0d79fcfd))

  * preserve WebSocket close across recovery and cancellation ([#4117](https://github.com/openai/openai-python/issues/4117))
  ([4590ff1](https://github.com/openai/openai-python/commit/4590ff15006dfef3b55f4dc8b1b95c4a790d021b))

  * **realtime:** honor native options for legacy beta sockets ([#4120](https://github.com/openai/openai-python/issues/4120))
  ([8968560](https://github.com/openai/openai-python/commit/8968560fb926240aea5fed8ee24e189eade57118))



  ### Chores


  * **api:** clarify cache-write token totals ([#4136](https://github.com/openai/openai-python/issues/4136))
  ([55b8b8a](https://github.com/openai/openai-python/commit/55b8b8a77c697c10ea89a14d6390456145687152))

  * **api:** clarify project API key update requirements ([#4131](https://github.com/openai/openai-python/issues/4131))
  ([0e6be9f](https://github.com/openai/openai-python/commit/0e6be9f1f6193cdea7a3d9982b69424c22ecafda))

  * **api:** maintain voice consent compatibility ([#4137](https://github.com/openai/openai-python/issues/4137))
  ([07abe06](https://github.com/openai/openai-python/commit/07abe065f058da56a92adc4168b6408b09babd34))

  * **api:** use neutral moderation examples ([#4104](https://github.com/openai/openai-python/issues/4104))
  ([553703e](https://github.com/openai/openai-python/commit/553703e2d3db379a83e3ead9e40436b7a66f639e))

  * restore generated Castiron reporting scripts ([#4113](https://github.com/openai/openai-python/issues/4113))
  ([9d12b56](https://github.com/openai/openai-python/commit/9d12b565554c08bcee6287c0d8f671b8c97ed911))

  * support next checkpoints in the trusted reporter ([#4128](https://github.com/openai/openai-python/issues/4128))
  ([ae2a6c2](https://github.com/openai/openai-python/commit/ae2a6c2a79e462d1e5ee2240354a5714289e1670))



  ### Documentation


  * plan the Python generated-code transition ([#4114](https://github.com/openai/openai-python/issues/4114))
  ([6a52987](https://github.com/openai/openai-python/commit/6a52987f2da5c3bc9b700a7094c0cf14fe7e78dc))

  * record Python transition progress and batch follow-up work ([#4116](https://github.com/openai/openai-python/issues/4116))
  ([46e3680](https://github.com/openai/openai-python/commit/46e36800ba5604044de46c88dc79f20dfd23dd35))'
first_seen: '2026-10-22T00:42:25Z'
last_seen: '2026-10-22T00:42:25Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/openai/openai-python/releases/tag/v3.36.0
  seen_at: '2026-10-22T00:42:25Z'
  metrics:
    reactions: 0
  kind: news
---

# openai/openai-python: v3.36.0

## [3.36.0](https://github.com/openai/openai-python/compare/v3.35.1...v3.36.0) (2026-10-21)


### Features

* add Vertex AI support for the Responses API ([#4139](https://github.com/openai/openai-python/issues/4139)) ([3e63d33](https://github.com/openai/openai-python/commit/3e63d33f6258f47285007aaee30df251d5127820))
* **api:** add 30-minute cache-write usage counts ([#4111](https://github.com/openai/openai-python/issues/4111)) ([5589146](https://github.com/openai/openai-python/commit/5589146d738e0c38758e117b8383a02c2e4e2ee7))
* **api:** add compaction trigger IDs ([#4122](https://github.com/openai/openai-python/issues/4122)) ([0e5794d](https://github.com/openai/openai-python/commit/0e5794dc48b8f8d51f6047f8a0b1814eb1e65850))
* **api:** add custom voice consent management ([#4135](https://github.com/openai/openai-python/issues/4135)) ([de6d70d](https://github.com/openai/openai-python/commit/de6d70d5c50ef1b9d3e5068b6e25ea52f447a8cb))
* **types:** prepare native synchronous WebSocket option type ([#4118](https://github.com/openai/openai-python/issues/4118)) ([90c0bac](https://github.com/openai/openai-python/commit/90c0bacc07ddd5662598db52b3c3011973011973))


### Bug Fixes

* **api:** accept canonical batch responses in strict mode ([#4106](https://github.com/openai/openai-python/issues/4106)) ([6eaa90e](https://github.com/openai/openai-python/commit/6eaa90ee20b40bbe84a5b1a5031d7cf672c7d368))
* clean up failed WebSocket setup and honor native options ([#4121](https://github.com/openai/openai-python/issues/4121)) ([b1a1a10](https://github.com/openai/openai-python/commit/b1a1a100d38d84dd556319e207880d85d23559cd))
* end sync WebSocket recovery when an attempt is interrupted ([#4129](https://github.com/openai/openai-python/issues/4129)) ([337769b](https://github.com/openai/openai-python/commit/337769b3daf5772cf54cf11a14c17ff5b7a3ac27))
* honor timed Translation receives during terminal cleanup ([#4132](https://github.com/openai/openai-python/issues/4132)) ([ca54146](https://github.com/openai/openai-python/commit/ca541462ba20dadb66eea6c67775f186dfb17e33))
* preserve client headers in legacy Beta Realtime connections ([#4130](https://github.com/openai/openai-python/issues/4130)) ([8a2a2e0](https://github.com/openai/openai-python/commit/8a2a2e0c4fe76297a5dd2395e05ca473561644ac))
* preserve declared aliases during Pydantic v1 validation ([#4119](https://github.com/openai/openai-python/issues/4119)) ([8b1cac9](https://github.com/openai/openai-python/commit/8b1cac931ccb32203010471b1f9d82e5c9957cff))
* preserve Vertex API root for response lifecycle ([#4140](https://github.com/openai/openai-python/issues/4140)) ([c2b14f5](https://github.com/openai/openai-python/commit/c2b14f538de7af908d8f1fd50e6af60c0d79fcfd))
* preserve WebSocket close across recovery and cancellation ([#4117](https://github.com/openai/openai-python/issues/4117)) ([4590ff1](https://github.com/openai/openai-python/commit/4590ff15006dfef3b55f4dc8b1b95c4a790d021b))
* **realtime:** honor native options for legacy beta sockets ([#4120](https://github.com/openai/openai-python/issues/4120)) ([8968560](https://github.com/openai/openai-python/commit/8968560fb926240aea5fed8ee24e189eade57118))


### Chores

* **api:** clarify cache-write token totals ([#4136](https://github.com/openai/openai-python/issues/4136)) ([55b8b8a](https://github.com/openai/openai-python/commit/55b8b8a77c697c10ea89a14d6390456145687152))
* **api:** clarify project API key update requirements ([#4131](https://github.com/openai/openai-python/issues/4131)) ([0e6be9f](https://github.com/openai/openai-python/commit/0e6be9f1f6193cdea7a3d9982b69424c22ecafda))
* **api:** maintain voice consent compatibility ([#4137](https://github.com/openai/openai-python/issues/4137)) ([07abe06](https://github.com/openai/openai-python/commit/07abe065f058da56a92adc4168b6408b09babd34))
* **api:** use neutral moderation examples ([#4104](https://github.com/openai/openai-python/issues/4104)) ([553703e](https://github.com/openai/openai-python/commit/553703e2d3db379a83e3ead9e40436b7a66f639e))
* restore generated Castiron reporting scripts ([#4113](https://github.com/openai/openai-python/issues/4113)) ([9d12b56](https://github.com/openai/openai-python/commit/9d12b565554c08bcee6287c0d8f671b8c97ed911))
* support next checkpoints in the trusted reporter ([#4128](https://github.com/openai/openai-python/issues/4128)) ([ae2a6c2](https://github.com/openai/openai-python/commit/ae2a6c2a79e462d1e5ee2240354a5714289e1670))


### Documentation

* plan the Python generated-code transition ([#4114](https://github.com/openai/openai-python/issues/4114)) ([6a52987](https://github.com/openai/openai-python/commit/6a52987f2da5c3bc9b700a7094c0cf14fe7e78dc))
* record Python transition progress and batch follow-up work ([#4116](https://github.com/openai/openai-python/issues/4116)) ([46e3680](https://github.com/openai/openai-python/commit/46e36800ba5604044de46c88dc79f20dfd23dd35))

## 笔记


