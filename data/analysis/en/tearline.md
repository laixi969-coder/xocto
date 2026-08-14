---
slug: tearline
name: Tearline
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A custom element, `<tear-line>`, that wraps whatever HTML you already have and renders it as a torn-edge thermal receipt — then hands you a PNG. Not a template language, not an image service.

## Who built it

Isaiah Kim (kyisaiah47 on HN/GitHub), an indie developer, hosted on his personal domain kynth.studio. It is his open-source project: MIT, zero dependencies, one file.

_Read: the classic "built a receipt generator for myself and it turned into a general component." The docs (dom-to-png, share-image-custom-element, receipt-ui, spotify-receipt-generator) are more complete than most commercial products; this author has genuinely worked the technical problem to the bone._

## What it actually does

- **Wrap any HTML** — headings, tables, images, lists — inside `<tear-line>` and it renders as a thermal receipt: torn edge, barcode, paper texture
- **One call exports a PNG** (`el.download()` / `el.toBlob()`), at any scale
- **Real text, not a canvas**: the receipt is real text in the light DOM — selectable, searchable (⌘F), translatable, read by screen readers in document order
- **Deterministic rendering**: the torn edge and barcode come from a seed, so the same seed always renders the same paper and the export matches what the user saw
- **Zero dependencies, zero build steps**: works in any framework (React/Vue/Svelte/plain script tag)
- Four deep technical essays included, one of which walks through why Receiptify-style apps die (Spotify's five-user cap kills most of them)

**What it deliberately does not do**: no scannable barcode (decorative only), no server-side image service; images inside must be data: URIs because SVG foreignObject cannot fetch over the network — and the export throws rather than hand you a receipt with a hole in it.

## What old behavior it replaces

Making an order summary, year in review, or set list into "a receipt image" previously meant one of two roads:
- html2canvas-style libraries that screenshot in the browser — and fail with tainted canvas, or produce an image that does not match what the user saw
- spinning up a puppeteer screenshot service or paying an image-service API, writing server code per template, paying for servers

The Receiptify phenomenon is the best footnote: everyone loves a receipt-style share image, but everyone building one dies on API limits. Tearline compresses receipt generation into "one tag + browser-local export," and the server simply disappears.

## Business model

**Free.** MIT, zero dependencies, no account, no server. There is no commercial form and none is planned.

_Read: this is a high-quality open-source component. The value flows to the author as reputation and to users as zero acquisition cost. For the reader there is no business model to analyze — but there is a format insight to steal._

## Hard numbers

- **HN: 6 points, 0 comments** (2026-08-13)
- The `package.json` shown in the docs lists an empty dependencies array; a single ES module, no build steps
- License: MIT. Download counts and npm installs: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author lives in the receipt/share-image use case; the pain is first-hand |
| Product insight | Nailed the format intuition — a receipt is more shareable than a screenshot of a table — and made it a general component |
| Execution quality | One file, zero dependencies, deterministic seed rendering, real accessibility work: textbook component engineering |
| Timing | Share images (OG cards, order cards, year-in-review) are a permanent need, but html2canvas and peers already exist |

## The call

**The most valuable thing this product proves is a format insight: the receipt is a more natural share object than a screenshot.**

Orders, playlists, year-in-review, lab reports — humans are already trained on "receipt" as an information container. Dress a table screenshot in it and it becomes "something worth posting." Receiptify's virality proved the demand; Tearline proves the demand can be satisfied at the cost of one tag.

**The transferable rule: find an old format your users already reflexively want to share, and slot your new feature into that format.** Receipts, boarding passes, lab reports, certificates — any is "tabular data plus ceremonial layout" turned into a share object. If your product has data a user wants to show off, it is worth asking which old format to dress it in.

**The problem**: the format insight is stealable, but the component has no commercial space — no charge, no hosting, and the code is small enough to copy without guilt. It is a fine part, not a business.

## What to watch next

① npm downloads / GitHub star growth — how many people actually use the format
② Whether someone builds a viral share-image app on top of `<tear-line>` (a Receiptify replacement)
③ Whether the author turns it into a hosted service

## What you can take from it

**Product logic**: old formats like receipts/tickets/certificates are native share objects — wrap the data your user wants to show off in a ceremonial format and sharing intent rises on its own. AI product builders can use this for share cards instead of another plain results page.

**Positioning language**: "anything a user might want to keep or post: an order summary, a workout, a year in review, a booking, a set list, a diff." The phrase "want to keep or post" as a feature filter is directly borrowable.

**Pricing structure**: none. Free, MIT.

## Verdict

**Unproven.** Engineering quality is among the best in this batch, but there is no business model. Keep it as evidence for the "receipt format" distribution insight; in three months, check whether someone ships a viral share app on top of it.
