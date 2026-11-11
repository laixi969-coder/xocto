---
slug: anthropics-anthropic-sdk-python-v280
name: 'anthropics/anthropic-sdk-python: v2.8.0'
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
url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.8.0
canonical_url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.8.0
summary: '### Features


  * **api:** add Claude Tag metrics to the analytics summaries and users reports

  * **api:** add reply_mode to Claude Tag Slack channel settings



  ### Bug Fixes


  * **bedrock:** send ";" in a model ID as is, and refuse a model ID whose part before the first ";" is
  empty, "." or ".."

  * **google-cloud:** percent-encode the project, location and workspace ID in the workspace and organization
  base URL paths

  * **google-cloud:** refuse an empty project, location or workspace ID that would be written into a derived
  base URL

  * **vertex:** refuse an empty model, project ID or region instead of writing it into the request path

  * **vertex:** send ";" in the model as %3B in the request path



  ### Chores


  * **docs:** clarify display_name for RBAC Roles created by Anthropic

  * **docs:** clarify plugin delete and skill name conflict descriptions

  * **docs:** clarify when to omit user_profile_id on external keys

  * **docs:** note that Claude Tag settings accept self-hosted runner pools

  * **internal:** make three timing tests tolerate slow test machines

  * **internal:** remove a redundant import from the message types



  ### Documentation


  * **examples:** show multiagent when creating a Managed Agents agent'
first_seen: '2026-11-11T01:56:55Z'
last_seen: '2026-11-11T01:56:55Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.8.0
  seen_at: '2026-11-11T01:56:55Z'
  metrics:
    reactions: 0
  kind: news
---

# anthropics/anthropic-sdk-python: v2.8.0

### Features

* **api:** add Claude Tag metrics to the analytics summaries and users reports
* **api:** add reply_mode to Claude Tag Slack channel settings


### Bug Fixes

* **bedrock:** send ";" in a model ID as is, and refuse a model ID whose part before the first ";" is empty, "." or ".."
* **google-cloud:** percent-encode the project, location and workspace ID in the workspace and organization base URL paths
* **google-cloud:** refuse an empty project, location or workspace ID that would be written into a derived base URL
* **vertex:** refuse an empty model, project ID or region instead of writing it into the request path
* **vertex:** send ";" in the model as %3B in the request path


### Chores

* **docs:** clarify display_name for RBAC Roles created by Anthropic
* **docs:** clarify plugin delete and skill name conflict descriptions
* **docs:** clarify when to omit user_profile_id on external keys
* **docs:** note that Claude Tag settings accept self-hosted runner pools
* **internal:** make three timing tests tolerate slow test machines
* **internal:** remove a redundant import from the message types


### Documentation

* **examples:** show multiagent when creating a Managed Agents agent

## 笔记


