---
slug: sqlite3-rsync-database-remote-copy-tool-for-sqlite
name: 'sqlite3_rsync: Database Remote-Copy Tool For SQLite'
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
url: https://simonwillison.net/2026/Nov/26/sqlite3-rsync/
canonical_url: https://simonwillison.net/2026/Nov/26/sqlite3-rsync
summary: 'sqlite3_rsync: Database Remote-Copy Tool For SQLite This additional SQLite tool has been around
  for a while now - it was added as "experimental" in SQLite 3.47.0 in October 2024 and enhanced in SQLite
  3.50.0 in May 2025 . It was only today that I understood one of its most attractive characteristics.
  Normally, if you want to grab a snapshot copy of a SQLite database, you need to use either the backup
  API or VACUUM INTO . In both cases you need enough disk space to create a duplicate copy of your database,
  so if you''re on a small instance and you already use more than half of the available disk you are plain
  out of luck. sqlite3_rsync can copy a snapshot of your database over an SSH connection to another machine,
  without first needing to create a full local copy! It''s also good for synchronizing an existing copy
  of a database without re-transmitting the entire thing over the network. It works in a similar way to
  regular rsync: The core idea behind the protocol is that the replica sends cryptographic hashes for
  pages or groups of pages over to the origin side. The origin sends back page content that differs,'
first_seen: '2026-11-27T04:16:33Z'
last_seen: '2026-11-27T04:16:33Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/26/sqlite3-rsync/
  seen_at: '2026-11-27T04:16:33Z'
  metrics: {}
  kind: news
---

# sqlite3_rsync: Database Remote-Copy Tool For SQLite

sqlite3_rsync: Database Remote-Copy Tool For SQLite This additional SQLite tool has been around for a while now - it was added as "experimental" in SQLite 3.47.0 in October 2024 and enhanced in SQLite 3.50.0 in May 2025 . It was only today that I understood one of its most attractive characteristics. Normally, if you want to grab a snapshot copy of a SQLite database, you need to use either the backup API or VACUUM INTO . In both cases you need enough disk space to create a duplicate copy of your database, so if you're on a small instance and you already use more than half of the available disk you are plain out of luck. sqlite3_rsync can copy a snapshot of your database over an SSH connection to another machine, without first needing to create a full local copy! It's also good for synchronizing an existing copy of a database without re-transmitting the entire thing over the network. It works in a similar way to regular rsync: The core idea behind the protocol is that the replica sends cryptographic hashes for pages or groups of pages over to the origin side. The origin sends back page content that differs,

## 笔记


