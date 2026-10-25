---
slug: openai-openai-python-v3370
name: 'openai/openai-python: v3.37.0'
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
url: https://github.com/openai/openai-python/releases/tag/v3.37.0
canonical_url: https://github.com/openai/openai-python/releases/tag/v3.37.0
summary: '## [3.37.0](https://github.com/openai/openai-python/compare/v3.36.1...v3.37.0) (2026-10-22)



  ### ⚠ BREAKING CHANGES


  * **api:** This minor release includes a breaking change to Decisions types. In Live response models,
  question `instructions` can now be a string or a list of structured text, image, or JSON parts; check
  `isinstance(question.instructions, str)` before using string operations and handle the structured form.
  Decisions request input types also include additional message roles and tool-history items, so update
  exhaustive type checks accordingly. Existing string instructions and `DecisionInputMessageParam` user-message
  inputs remain supported.



  ### Features


  * **api:** expand Decisions input and question types ([#4158](https://github.com/openai/openai-python/issues/4158))
  ([1e45ad1](https://github.com/openai/openai-python/commit/1e45ad180ba409e3c31897710aa2a40129d58994))



  ### Chores


  * **api:** preserve file and video polling helpers ([#4155](https://github.com/openai/openai-python/issues/4155))
  ([7db9d88](https://github.com/openai/openai-python/commit/7db9d884c33b0d5ef252e9a4b6e7ae0bbd217e5b))

  * **api:** preserve upload helpers and Live connection defaults ([#4152](https://github.com/openai/openai-python/issues/4152))
  ([a29dc39](https://github.com/openai/openai-python/commit/a29dc3947aeccecc2e85d8fbad4d7c03b8af13e9))

  * **deps:** bump astral-sh/setup-uv from 10.2.0 to 10.3.0 ([#4109](https://github.com/openai/openai-python/issues/4109))
  ([fa9a161](https://github.com/openai/openai-python/commit/fa9a1616fd175e68dec9960d33dee2caefc0e8d3))'
first_seen: '2026-10-23T00:40:56Z'
last_seen: '2026-10-25T00:21:05Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/openai/openai-python/releases/tag/v3.37.0
  seen_at: '2026-10-25T00:21:05Z'
  metrics:
    reactions: 5
  kind: news
---

# openai/openai-python: v3.37.0

## [3.37.0](https://github.com/openai/openai-python/compare/v3.36.1...v3.37.0) (2026-10-22)


### ⚠ BREAKING CHANGES

* **api:** This minor release includes a breaking change to Decisions types. In Live response models, question `instructions` can now be a string or a list of structured text, image, or JSON parts; check `isinstance(question.instructions, str)` before using string operations and handle the structured form. Decisions request input types also include additional message roles and tool-history items, so update exhaustive type checks accordingly. Existing string instructions and `DecisionInputMessageParam` user-message inputs remain supported.


### Features

* **api:** expand Decisions input and question types ([#4158](https://github.com/openai/openai-python/issues/4158)) ([1e45ad1](https://github.com/openai/openai-python/commit/1e45ad180ba409e3c31897710aa2a40129d58994))


### Chores

* **api:** preserve file and video polling helpers ([#4155](https://github.com/openai/openai-python/issues/4155)) ([7db9d88](https://github.com/openai/openai-python/commit/7db9d884c33b0d5ef252e9a4b6e7ae0bbd217e5b))
* **api:** preserve upload helpers and Live connection defaults ([#4152](https://github.com/openai/openai-python/issues/4152)) ([a29dc39](https://github.com/openai/openai-python/commit/a29dc3947aeccecc2e85d8fbad4d7c03b8af13e9))
* **deps:** bump astral-sh/setup-uv from 10.2.0 to 10.3.0 ([#4109](https://github.com/openai/openai-python/issues/4109)) ([fa9a161](https://github.com/openai/openai-python/commit/fa9a1616fd175e68dec9960d33dee2caefc0e8d3))

## 笔记


