---
slug: latex-renderer
name: LaTeX renderer
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
url: https://simonwillison.net/2026/Oct/15/latex/
canonical_url: https://simonwillison.net/2026/Oct/15/latex
summary: 'Tool: LaTeX renderer Inspired by Paul Ford and Aboard Foundary''s new web app Tiny Little Office
  , which provides a suite of web app content editors (a Word Processor, Outliner, Presentation Builder,
  Spreadsheet, Calculator, Drawing Tool, Diagram Maker, Animator, Calendar, and Trip Planner). Tiny Little
  Office''s signature trick is to store all of the document data in the #fragment section of the URL,
  so every document created using it becomes a bookmarkable and shareable link. It also has an llms.txt
  file telling agents how to construct URLs that will render as documents. Claude used that file to generate
  this link to a deck that explains how the URL format works: Tiny Little Office inspired me to have Claude
  Code (Opus 5.5 Extra) build a similar tool that works with LaTeX. Here''s the sequence of prompts I
  used: I want a tool where you can link to it with a fragment hash #code-here and it treats that code
  as LaTeX and renders it really effectively. It should also support a prefix which means the latex is
  compressed with a custom compression dictionary optimized for latex. Use the best available latex render
  library from a CDN (consider WebAssembly too). If loaded without'
first_seen: '2026-10-17T00:31:00Z'
last_seen: '2026-10-17T00:31:00Z'
status: pending_filter
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Oct/15/latex/
  seen_at: '2026-10-17T00:31:00Z'
  metrics: {}
  kind: news
---

# LaTeX renderer

Tool: LaTeX renderer Inspired by Paul Ford and Aboard Foundary's new web app Tiny Little Office , which provides a suite of web app content editors (a Word Processor, Outliner, Presentation Builder, Spreadsheet, Calculator, Drawing Tool, Diagram Maker, Animator, Calendar, and Trip Planner). Tiny Little Office's signature trick is to store all of the document data in the #fragment section of the URL, so every document created using it becomes a bookmarkable and shareable link. It also has an llms.txt file telling agents how to construct URLs that will render as documents. Claude used that file to generate this link to a deck that explains how the URL format works: Tiny Little Office inspired me to have Claude Code (Opus 5.5 Extra) build a similar tool that works with LaTeX. Here's the sequence of prompts I used: I want a tool where you can link to it with a fragment hash #code-here and it treats that code as LaTeX and renders it really effectively. It should also support a prefix which means the latex is compressed with a custom compression dictionary optimized for latex. Use the best available latex render library from a CDN (consider WebAssembly too). If loaded without

## 笔记


