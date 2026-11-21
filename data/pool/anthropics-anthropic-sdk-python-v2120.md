---
slug: anthropics-anthropic-sdk-python-v2120
name: 'anthropics/anthropic-sdk-python: v2.12.0'
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
url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.12.0
canonical_url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.12.0
summary: "### Features\n\n* **api:** add the image_dimensions_too_large error code\n\n\n### Bug Fixes\n\
  \n* **bedrock:** send the user profile ID in the request body\n\n  Amazon Bedrock reads `user_profile_id`\
  \ from the request body and ignores the `anthropic-user-profile-id` header, so a profile ID given to\
  \ `AnthropicBedrock` or `AsyncAnthropicBedrock` was not applied. Both clients now move it into the body\
  \ of Messages requests and no longer send the header. A `user_profile_id` already in the body takes\
  \ priority over the header.\n\n  Some models on Bedrock do not support user profiles. A request to one\
  \ of them with a profile ID now fails with a 400 error; before, the ID was ignored. Leave the ID off\
  \ requests to those models.\n\n\n### Chores\n\n* **docs:** clarify billing_policy in batches and two\
  \ billing errors"
first_seen: '2026-11-21T03:13:53Z'
last_seen: '2026-11-21T03:13:53Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.12.0
  seen_at: '2026-11-21T03:13:53Z'
  metrics:
    reactions: 0
  kind: news
---

# anthropics/anthropic-sdk-python: v2.12.0

### Features

* **api:** add the image_dimensions_too_large error code


### Bug Fixes

* **bedrock:** send the user profile ID in the request body

  Amazon Bedrock reads `user_profile_id` from the request body and ignores the `anthropic-user-profile-id` header, so a profile ID given to `AnthropicBedrock` or `AsyncAnthropicBedrock` was not applied. Both clients now move it into the body of Messages requests and no longer send the header. A `user_profile_id` already in the body takes priority over the header.

  Some models on Bedrock do not support user profiles. A request to one of them with a profile ID now fails with a 400 error; before, the ID was ignored. Leave the ID off requests to those models.


### Chores

* **docs:** clarify billing_policy in batches and two billing errors

## 笔记


