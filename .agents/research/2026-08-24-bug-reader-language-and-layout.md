# Bug Report: Reader-facing method name and unstable judgment layout

**Date:** 2026-08-24  
**Severity:** medium  
**Status:** fixed and verified

## Symptom

Readers saw the internal name `/req` in headings, filters, empty states, and
event labels. On product pages, the three-item summary used a two-column grid:
the third item started a new row and left a large empty area beside it. Section
notes were right-aligned in a narrow side column, which produced visually
arbitrary Chinese line breaks. On the homepage, a region could be orphaned on
its own line after a dimension separator.

## Expected Behavior

- Reader-facing Chinese calls the assessment `真需求`; the English edition uses
  `Demand assessment`.
- The summary's conclusion, review state, and next check share a compact,
  responsive overview instead of creating an empty grid cell.
- Explanatory notes read left to right in a natural width, and opportunity
  dimensions wrap only between semantic units.

## Reproduction Steps

1. Open any product detail page with a completed assessment, for example
   `site/p/biosecurity-agent.html`.
2. Observe `/req` in the assessment header and its three fields arranged as
   two cells plus an orphaned third cell.
3. Open the home page at a width where the dimension string wraps and observe
   the region on a line by itself.

## Root Cause Analysis

### Location

- **Files:** `src/xocto/i18n.py:313-453`, `templates/product.html:47-60`,
  `templates/index.html:24-31`, `templates/style.css:144-146,265-273`
- **Functions:** static page localisation and template rendering

### Cause

The internal research protocol was copied directly into public localisation
strings and one hard-coded template eyebrow. The generic `.decision-grid` is a
two-column grid with a minimum card height; it was reused for a three-field
overview. This deterministically creates an empty fourth cell. The shared
header style additionally assigned notes to a right-aligned narrow column, and
the dimensions were emitted as one unrestricted text node.

### When Introduced

- **Commit:** `f349af4c`
- **Date:** 2026-08-21
- **Author:** laixi969-coder
- The two-column grid and fixed-height rule were introduced with the product
  detail redesign. Public `/req` wording was subsequently propagated through
  localisation and the product template.

## Fix

1. Replace every reader-facing `/req` label with `真需求` in Chinese and
   `Demand assessment` in English; remove the hard-coded template label.
2. Add a three-column `decision-overview` variant, with two-column and
   one-column responsive layouts, and remove its fixed card height.
3. Left-align explanatory notes, shorten their copy, and use semantic inline
   dimension units so a region is never separated from its associated work.
4. Add a design scan that fails a build when `/req` reappears in rendered HTML,
   plus a localisation regression test.

## Verification

- `uv run python -m unittest tests.test_site.PublishabilityTests -q` — passed
- `uv run xocto build` — generated 922 pages
- `python3 scripts/check_design.py` — all nine checks passed, including
  internal-method leakage
- `rg -n -i '/req' site` — no matches

## Failure Count

One `fix_failed_tests` event: the first version of the new localisation test
assumed every localisation value was a string. It was narrowed to direct
strings and then passed. No root-cause or design hypothesis failed.

## Follow-up: 2026-08-24

The first layout correction left `.sec-head .note` in the second column. The
copy was left-aligned but still constrained to 32% of the section width, so it
continued to wrap despite unused horizontal space. The note now explicitly
spans the entire grid row (`templates/style.css`), and a regression test
asserts that invariant. This is a corrected root cause, not a copy change.

### Deployment correction

The rendered HTML referenced the shared stylesheet only as `style.css`. Browsers
could therefore retain an older stylesheet after Vercel had served the updated
HTML, reproducing the retired two-column layout online. The build now hashes
the stylesheet and appends that hash to every stylesheet URL, so a style change
always has a new URL and cannot be hidden by an old browser cache.

### Content-grid correction

The screenshot of the business judgment section exposed a second unresolved
layout family: desktop `decision-grid` and `role-grid` split prose across fixed
side columns. These were a poor fit for variable-length Chinese analysis and
could leave a narrow or off-screen companion column. Both grids now render one
full-width, content-sized row per judgment; this applies at every viewport,
not only below a mobile breakpoint. A regression test rejects a return to
desktop side columns.
