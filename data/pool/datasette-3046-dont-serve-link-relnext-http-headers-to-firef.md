---
slug: datasette-3046-dont-serve-link-relnext-http-headers-to-firef
name: 'datasette #3046: Don''t serve link: rel=next HTTP headers to Firefox for HTML pages'
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
url: https://simonwillison.net/2026/Nov/7/link-rel-next/
canonical_url: https://simonwillison.net/2026/Nov/7/link-rel-next
summary: 'datasette #3046: Don''t serve link: rel=next HTTP headers to Firefox for HTML pages I was looking
  at the Firefox network panel today when I noticed that requests to a Datasette table page were triggering
  an HTTP prefetch to the next page of rows in that table. This was happening because Datasette pages
  serve an HTTP link header like this: link: <https://latest.datasette.io/fixtures/compound_three_primary_keys?_next=a%2Cd%2Cv>;
  rel="next" This is bad. A tiny fraction of the visitors to one of those pages will click the "next"
  link, which means their browser is fetching unnecessary data and the Datasette server is having to render
  an entire page that then gets thrown away. I dug in and learned that Firefox has an issue that has been
  open for 24 years about this behavior... And one of the early comments on that issue links to my blog
  post from 2002 complaining about this feature. I hadn''t just forgotten that I had written about it,
  I had forgotten the feature entirely! Tags: firefox , html , mozilla , datasette'
first_seen: '2026-11-08T01:27:32Z'
last_seen: '2026-11-08T01:27:32Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/7/link-rel-next/
  seen_at: '2026-11-08T01:27:32Z'
  metrics: {}
  kind: news
---

# datasette #3046: Don't serve link: rel=next HTTP headers to Firefox for HTML pages

datasette #3046: Don't serve link: rel=next HTTP headers to Firefox for HTML pages I was looking at the Firefox network panel today when I noticed that requests to a Datasette table page were triggering an HTTP prefetch to the next page of rows in that table. This was happening because Datasette pages serve an HTTP link header like this: link: <https://latest.datasette.io/fixtures/compound_three_primary_keys?_next=a%2Cd%2Cv>; rel="next" This is bad. A tiny fraction of the visitors to one of those pages will click the "next" link, which means their browser is fetching unnecessary data and the Datasette server is having to render an entire page that then gets thrown away. I dug in and learned that Firefox has an issue that has been open for 24 years about this behavior... And one of the early comments on that issue links to my blog post from 2002 complaining about this feature. I hadn't just forgotten that I had written about it, I had forgotten the feature entirely! Tags: firefox , html , mozilla , datasette

## 笔记


