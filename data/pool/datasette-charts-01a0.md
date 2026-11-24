---
slug: datasette-charts-01a0
name: datasette-charts 0.1a0
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
url: https://simonwillison.net/2026/Nov/23/datasette-charts/
canonical_url: https://simonwillison.net/2026/Nov/23/datasette-charts
summary: 'Release: datasette-charts 0.1a0 I''ve been thinking about this problem for over a year now,
  but on Sunday I finally fired up Claude Fable 5.2 to build an initial prototype. The prototype went
  so well that this is now a full plugin. You can try it out in Datasette Lite here . It looks like this:
  The new charts plugin works against any table or arbitrary SQL query in Datasette. It defines several
  different chart types (using vendored D3 , Observable Plot , and topojson-client ), each with a set
  of heuristics for identifying when they might be a good match for a specific set of rows. Those suggestion
  thumbnails at the top are actual visualizations driven by the data, and selecting one pulls up the full
  chart along with tools for modifying it. You can also manually construct a chart from scratch. As with
  other Datasette visualization plugins, the current state of your chart is persisted in a #fragment in
  the URL - so you can bookmark charts or share them with others. The most important feature is that the
  charts take all rows into account . Previous charting plugins like datasette-vega would only show charts
  for the current page'
first_seen: '2026-11-24T06:03:57Z'
last_seen: '2026-11-24T06:03:57Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/23/datasette-charts/
  seen_at: '2026-11-24T06:03:57Z'
  metrics: {}
  kind: news
---

# datasette-charts 0.1a0

Release: datasette-charts 0.1a0 I've been thinking about this problem for over a year now, but on Sunday I finally fired up Claude Fable 5.2 to build an initial prototype. The prototype went so well that this is now a full plugin. You can try it out in Datasette Lite here . It looks like this: The new charts plugin works against any table or arbitrary SQL query in Datasette. It defines several different chart types (using vendored D3 , Observable Plot , and topojson-client ), each with a set of heuristics for identifying when they might be a good match for a specific set of rows. Those suggestion thumbnails at the top are actual visualizations driven by the data, and selecting one pulls up the full chart along with tools for modifying it. You can also manually construct a chart from scratch. As with other Datasette visualization plugins, the current state of your chart is persisted in a #fragment in the URL - so you can bookmark charts or share them with others. The most important feature is that the charts take all rows into account . Previous charting plugins like datasette-vega would only show charts for the current page

## 笔记


