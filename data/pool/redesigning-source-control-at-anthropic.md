---
slug: redesigning-source-control-at-anthropic
name: Redesigning source control at Anthropic
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
url: https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/
canonical_url: https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic
summary: 'Redesigning source control at Anthropic Interesting piece from Anthropic describing why and
  how they built their own custom alternative to Git, based on the dramatic increase in rate of changes
  to their code after the past six months. In May 2026, Anthropic averaged around 2,500 code changes merged
  per day; as of September, we merged over 30,000 per day. They included a chart showing those changes.
  I had Claude modify their chart ( code here ) to add markers for the public releases of each of their
  models in 2026: This shows public release dates, not the date when models became available for Anthropic''s
  internal use. My guess is that the introduction of Fable/Mythos class models is a key factor in the
  increased coding velocity. "Antique" is their new code review system. The source control system is called
  Scion, and sounds to me like a reinvention of centralized source control along the lines of Subversion.
  They had some pretty extreme requirements: The history of our main branch alone is almost 100 GB, and
  a compressed working copy is over 25 GB. We perform on the order of 25 million code checkouts per day
  for CI, before counting developer environments, agent'
first_seen: '2026-10-14T01:14:23Z'
last_seen: '2026-10-14T01:14:23Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/
  seen_at: '2026-10-14T01:14:23Z'
  metrics: {}
  kind: news
---

# Redesigning source control at Anthropic

Redesigning source control at Anthropic Interesting piece from Anthropic describing why and how they built their own custom alternative to Git, based on the dramatic increase in rate of changes to their code after the past six months. In May 2026, Anthropic averaged around 2,500 code changes merged per day; as of September, we merged over 30,000 per day. They included a chart showing those changes. I had Claude modify their chart ( code here ) to add markers for the public releases of each of their models in 2026: This shows public release dates, not the date when models became available for Anthropic's internal use. My guess is that the introduction of Fable/Mythos class models is a key factor in the increased coding velocity. "Antique" is their new code review system. The source control system is called Scion, and sounds to me like a reinvention of centralized source control along the lines of Subversion. They had some pretty extreme requirements: The history of our main branch alone is almost 100 GB, and a compressed working copy is over 25 GB. We perform on the order of 25 million code checkouts per day for CI, before counting developer environments, agent

## 笔记


