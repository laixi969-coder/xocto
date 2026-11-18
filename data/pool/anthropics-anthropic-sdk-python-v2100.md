---
slug: anthropics-anthropic-sdk-python-v2100
name: 'anthropics/anthropic-sdk-python: v2.10.0'
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
url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.10.0
canonical_url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.10.0
summary: "### Features\n\n* **api:** add beta support for the billing_policy request parameter\n* **api:**\
  \ add contract_spend_limit_reached error code to messages\n* **api:** add error codes for linked billing\
  \ refusals\n* **api:** add the user_profile_billing_not_authorized error code\n* **api:** add webhook\
  \ events for external key failure and recovery\n\n\n### Bug Fixes\n\n* **client:** stop reporting failed\
  \ aiohttp connections as timeouts\n* **types:** keep deprecated model aliases and the types nested under\
  \ them working\n\n\n### Chores\n\n* **api:** rename error data models, deprecating the old names\n*\
  \ **docs:** clarify which AWS KMS keys a workspace can use on Claude Platform on AWS\n* **docs:** clarify\
  \ which credential work get, update and list accept\n* **docs:** clarify which uploads a plugin pin\
  \ holds back\n* **docs:** note that a plugin scan's reason also covers errored scans\n\n  `content_scan.reason`\
  \ on an errored scan now says why there is no verdict. It is not a security finding, so code that treats\
  \ any `reason` as a concern should also check `status`.\n\n* **internal:** don't report moved classes\
  \ as breaking changes\n\n\n### Documentation\n\n* name each SDK's own types in rename deprecations"
first_seen: '2026-11-18T03:43:16Z'
last_seen: '2026-11-18T03:43:16Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.10.0
  seen_at: '2026-11-18T03:43:16Z'
  metrics:
    reactions: 0
  kind: news
---

# anthropics/anthropic-sdk-python: v2.10.0

### Features

* **api:** add beta support for the billing_policy request parameter
* **api:** add contract_spend_limit_reached error code to messages
* **api:** add error codes for linked billing refusals
* **api:** add the user_profile_billing_not_authorized error code
* **api:** add webhook events for external key failure and recovery


### Bug Fixes

* **client:** stop reporting failed aiohttp connections as timeouts
* **types:** keep deprecated model aliases and the types nested under them working


### Chores

* **api:** rename error data models, deprecating the old names
* **docs:** clarify which AWS KMS keys a workspace can use on Claude Platform on AWS
* **docs:** clarify which credential work get, update and list accept
* **docs:** clarify which uploads a plugin pin holds back
* **docs:** note that a plugin scan's reason also covers errored scans

  `content_scan.reason` on an errored scan now says why there is no verdict. It is not a security finding, so code that treats any `reason` as a concern should also check `status`.

* **internal:** don't report moved classes as breaking changes


### Documentation

* name each SDK's own types in rename deprecations

## 笔记


