---
slug: parse-number-as-a-sqlite-extension-c-vs-rust
name: 'parse_number() as a SQLite extension: C vs Rust'
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
url: https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/
canonical_url: https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust
summary: 'Research: parse_number() as a SQLite extension: C vs Rust I was out walking the dog when I got
  curious about how easy/difficult it would be to write a SQLite C extension that adds a parse_number()
  function for turning strings like -$1,234.56 or ''12.5%'' into numeric values that could be summed and
  sorted. I fired up regular Claude chat (Opus 5.5) and prompted : I''m thinking about a SQLite custom
  function ''parse_number(value)'' that strips '','', ''$'', ''£'' and ''%'', handles a leading ''-'',
  and returns ''NULL'' for anything it can’t parse Explore the difference between building this as a SQLite
  extension in C v.s. in Rust - I want to compare performance and code complexity and size of the resulting
  .so (or whatever) file This gave me a solid starting point - the Rust extension was 321 KB (using Rusqlite
  ) and 298 KB (using sqlite-loadable-rs ), while the C extension was 14 KB. But the Rust extension was
  faster! Turns out that''s because the Rust equivalent of C''s strtod is "twice as fast". So I prompted:
  Try writing your own C function for parsing text into a decimal number that catches up to or beats the
  Rust implementation And it'
first_seen: '2026-11-09T01:45:11Z'
last_seen: '2026-11-09T01:45:11Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/
  seen_at: '2026-11-09T01:45:11Z'
  metrics: {}
  kind: news
---

# parse_number() as a SQLite extension: C vs Rust

Research: parse_number() as a SQLite extension: C vs Rust I was out walking the dog when I got curious about how easy/difficult it would be to write a SQLite C extension that adds a parse_number() function for turning strings like -$1,234.56 or '12.5%' into numeric values that could be summed and sorted. I fired up regular Claude chat (Opus 5.5) and prompted : I'm thinking about a SQLite custom function 'parse_number(value)' that strips ',', '$', '£' and '%', handles a leading '-', and returns 'NULL' for anything it can’t parse Explore the difference between building this as a SQLite extension in C v.s. in Rust - I want to compare performance and code complexity and size of the resulting .so (or whatever) file This gave me a solid starting point - the Rust extension was 321 KB (using Rusqlite ) and 298 KB (using sqlite-loadable-rs ), while the C extension was 14 KB. But the Rust extension was faster! Turns out that's because the Rust equivalent of C's strtod is "twice as fast". So I prompted: Try writing your own C function for parsing text into a decimal number that catches up to or beats the Rust implementation And it

## 笔记


