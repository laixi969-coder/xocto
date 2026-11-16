---
slug: datasette-10a43
name: datasette 1.0a43
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
url: https://simonwillison.net/2026/Nov/15/datasette/
canonical_url: https://simonwillison.net/2026/Nov/15/datasette
summary: 'Release: datasette 1.0a43 I''ve been leaning hard into Claude Fable 5.2 to help knock things
  off the 1.0 milestone , which is now 53% complete. The biggest 1.0 item in this release is streaming
  support for output renderers - the built-in TSV and CSV export mechanisms now use this as well, and
  plugins can register themselves as capable of streaming every row in a table in one go via the new Response.stream()
  method. There are a couple of security fixes, one of which I deemed deserving of a GitHub advisory :
  private stored queries could be exposed, granting access to the title and SQL of the query (but not
  allowing that query to be executed). There are dozens of smaller improvements. The row page JSON representation
  finally has a design suitable for 1.0 . A new <datasette-copy-button> Web Component provides copy-schema
  in various places. JSON in columns on the row page can be pretty-printed. There''s a new DatasetteModal.confirm()
  JavaScript utility method. Plus dozens of bug fixes, including contributions by Zihan Dai , Peter Olkhovets
  , Ilya Khalafi , and Ankita Advitot . The feature I''m most excited about is a pretty tiny one: I''ve
  added CSS multi-page view transitions to'
first_seen: '2026-11-16T02:08:53Z'
last_seen: '2026-11-16T02:08:53Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/15/datasette/
  seen_at: '2026-11-16T02:08:53Z'
  metrics: {}
  kind: news
---

# datasette 1.0a43

Release: datasette 1.0a43 I've been leaning hard into Claude Fable 5.2 to help knock things off the 1.0 milestone , which is now 53% complete. The biggest 1.0 item in this release is streaming support for output renderers - the built-in TSV and CSV export mechanisms now use this as well, and plugins can register themselves as capable of streaming every row in a table in one go via the new Response.stream() method. There are a couple of security fixes, one of which I deemed deserving of a GitHub advisory : private stored queries could be exposed, granting access to the title and SQL of the query (but not allowing that query to be executed). There are dozens of smaller improvements. The row page JSON representation finally has a design suitable for 1.0 . A new <datasette-copy-button> Web Component provides copy-schema in various places. JSON in columns on the row page can be pretty-printed. There's a new DatasetteModal.confirm() JavaScript utility method. Plus dozens of bug fixes, including contributions by Zihan Dai , Peter Olkhovets , Ilya Khalafi , and Ankita Advitot . The feature I'm most excited about is a pretty tiny one: I've added CSS multi-page view transitions to

## 笔记


