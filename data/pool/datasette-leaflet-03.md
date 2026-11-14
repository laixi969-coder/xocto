---
slug: datasette-leaflet-03
name: datasette-leaflet 0.3
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
url: https://simonwillison.net/2026/Nov/13/datasette-leaflet/
canonical_url: https://simonwillison.net/2026/Nov/13/datasette-leaflet
summary: 'Release: datasette-leaflet 0.3 OpenStreetMap have a very reasonable policy that hits to their
  hosted tile server should send a referrer header . Datasette table pages used the Referrer-Policy: no-referrer
  HTTP header, causing plugins that loaded tiles from OpenStreetMap to violate that policy. datasette-leaflet
  is the plugin that loads a bundled Leaflet so other Datasette plugins can depend on it. It now sets
  the referrer policy on the tile requests themselves to strict-origin-when-cross-origin , passing the
  host but not the full path to the page. Tags: leaflet , datasette , openstreetmap'
first_seen: '2026-11-14T02:28:07Z'
last_seen: '2026-11-14T02:28:07Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/13/datasette-leaflet/
  seen_at: '2026-11-14T02:28:07Z'
  metrics: {}
  kind: news
---

# datasette-leaflet 0.3

Release: datasette-leaflet 0.3 OpenStreetMap have a very reasonable policy that hits to their hosted tile server should send a referrer header . Datasette table pages used the Referrer-Policy: no-referrer HTTP header, causing plugins that loaded tiles from OpenStreetMap to violate that policy. datasette-leaflet is the plugin that loads a bundled Leaflet so other Datasette plugins can depend on it. It now sets the referrer policy on the tile requests themselves to strict-origin-when-cross-origin , passing the host but not the full path to the page. Tags: leaflet , datasette , openstreetmap

## 笔记


