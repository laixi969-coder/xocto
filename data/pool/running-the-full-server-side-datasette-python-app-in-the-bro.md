---
slug: running-the-full-server-side-datasette-python-app-in-the-bro
name: Running the full server-side Datasette Python app in the browser with service workers and Pyodide
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
url: https://simonwillison.net/2026/Nov/17/datasette-lite/
canonical_url: https://simonwillison.net/2026/Nov/17/datasette-lite
summary: 'Datasette Lite is my port of the Datasette Python application to run directly in the browser
  using WebAssembly and Pyodide . I''ve released a complete rewrite of Datasette Lite using service workers,
  and it''s now almost indistinguishable from the real server-side application. You can now do all of
  the following, using a carefully crafted URL to lite.datasette.io : Load client-side Datasette to browse
  any SQLite database, JSON file, CSV file or SQL script Select a released version of Datasette to load
  from PyPI Load a specific commit, tag, or branch name from the Datasette GitHub repository Pick from
  over 100 versions of SQLite to use with Datasette Install additional Datasette plugins from PyPI or
  URLs to wheel files, including JavaScript visualization tools The ability to load specific Datasette
  references, plugins, and SQLite versions makes this a fantastic tool for linking to demos of work-in-progress
  features or bug reproductions, without needing to spin up a full web server to serve that demo. As an
  example, consider the following URL: https://lite.datasette.io/?install=datasette-maplibre&url=https://gist.githubusercontent.com/simonw/39fa5d399465766039549912e2b3d291/raw/f6dfba99a75cbb8b5d9386223220eb52272767ee/demo.db&metadata=https://gist.githubusercontent.com/simonw/39fa5d399465766039549912e2b3d291/raw/f6dfba99a75cbb8b5d9386223220eb52272767ee/metadata.yml#/demo/capitals_and_countries%23map=0/4.2/180&color=continent
  Follow that link and, after a short loading screen, you''ll find yourself on a page that looks like
  this: That''s Datasette running the new datasette-maplibre plugin, loading up a database of'
first_seen: '2026-11-18T03:43:38Z'
last_seen: '2026-11-18T03:43:38Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/17/datasette-lite/
  seen_at: '2026-11-18T03:43:38Z'
  metrics: {}
  kind: news
---

# Running the full server-side Datasette Python app in the browser with service workers and Pyodide

Datasette Lite is my port of the Datasette Python application to run directly in the browser using WebAssembly and Pyodide . I've released a complete rewrite of Datasette Lite using service workers, and it's now almost indistinguishable from the real server-side application. You can now do all of the following, using a carefully crafted URL to lite.datasette.io : Load client-side Datasette to browse any SQLite database, JSON file, CSV file or SQL script Select a released version of Datasette to load from PyPI Load a specific commit, tag, or branch name from the Datasette GitHub repository Pick from over 100 versions of SQLite to use with Datasette Install additional Datasette plugins from PyPI or URLs to wheel files, including JavaScript visualization tools The ability to load specific Datasette references, plugins, and SQLite versions makes this a fantastic tool for linking to demos of work-in-progress features or bug reproductions, without needing to spin up a full web server to serve that demo. As an example, consider the following URL: https://lite.datasette.io/?install=datasette-maplibre&url=https://gist.githubusercontent.com/simonw/39fa5d399465766039549912e2b3d291/raw/f6dfba99a75cbb8b5d9386223220eb52272767ee/demo.db&metadata=https://gist.githubusercontent.com/simonw/39fa5d399465766039549912e2b3d291/raw/f6dfba99a75cbb8b5d9386223220eb52272767ee/metadata.yml#/demo/capitals_and_countries%23map=0/4.2/180&color=continent Follow that link and, after a short loading screen, you'll find yourself on a page that looks like this: That's Datasette running the new datasette-maplibre plugin, loading up a database of

## 笔记


