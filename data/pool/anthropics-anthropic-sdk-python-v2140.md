---
slug: anthropics-anthropic-sdk-python-v2140
name: 'anthropics/anthropic-sdk-python: v2.14.0'
builder: anthropics
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
url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.14.0
canonical_url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.14.0
summary: "### Features\n\n* **api:** add Google-managed data controls for Google Cloud projects\n* **api:**\
  \ add Google-managed data controls for user profiles\n* **api:** add support for compliance review cases,\
  \ notices, and items\n\n\n### Bug Fixes\n\n* **client:** honor proxy and trust_env when proxy variables\
  \ are set\n\n  `DefaultHttpxClient` and `DefaultAsyncHttpxClient` read `HTTP_PROXY`, `HTTPS_PROXY`,\
  \ `ALL_PROXY` and `NO_PROXY` even when the caller passed `proxy=` or `trust_env=False`, and the variables\
  \ won. Now `proxy=` is used for every request and the variables are not read, and `trust_env=False`\
  \ ignores them, as in plain `httpx2`.\n\n  What you may notice: with `proxy=` set, a host listed in\
  \ `NO_PROXY` used to be reached directly and now goes through your proxy. To keep a host off the proxy,\
  \ pass `mounts={\"all://that.host\": None}`.\n\n\n### Chores\n\n* **docs:** drop the provisional naming\
  \ note from the Google Cloud client README\n* **docs:** name both causes of the tool use limit error\n\
  * **docs:** update example workspace and API key IDs\n\n\n### Documentation\n\n* show what enum values\
  \ mean"
first_seen: '2026-11-25T04:54:21Z'
last_seen: '2026-11-25T04:54:21Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.14.0
  seen_at: '2026-11-25T04:54:21Z'
  metrics:
    reactions: 0
  kind: news
---

# anthropics/anthropic-sdk-python: v2.14.0

### Features

* **api:** add Google-managed data controls for Google Cloud projects
* **api:** add Google-managed data controls for user profiles
* **api:** add support for compliance review cases, notices, and items


### Bug Fixes

* **client:** honor proxy and trust_env when proxy variables are set

  `DefaultHttpxClient` and `DefaultAsyncHttpxClient` read `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY` and `NO_PROXY` even when the caller passed `proxy=` or `trust_env=False`, and the variables won. Now `proxy=` is used for every request and the variables are not read, and `trust_env=False` ignores them, as in plain `httpx2`.

  What you may notice: with `proxy=` set, a host listed in `NO_PROXY` used to be reached directly and now goes through your proxy. To keep a host off the proxy, pass `mounts={"all://that.host": None}`.


### Chores

* **docs:** drop the provisional naming note from the Google Cloud client README
* **docs:** name both causes of the tool use limit error
* **docs:** update example workspace and API key IDs


### Documentation

* show what enum values mean

## 笔记


