---
slug: stepshot
name: StepShot
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

Records what you actually do on your Mac and turns it into polished step-by-step
guides on the spot — processed locally, one-time purchase, no account, no uploads.

## Who built it

Solo indie developer Thomas Ellon (goes by Stewie at launch).
Self-launched on PH on 2026-08-07: 91 upvotes, daily rank #18. Site: stepshot.app.

_Read: the launch line "an hour of work to describe four minutes of clicking" is true
for anyone who has ever written a tutorial. He positions the browser-extension gap as
his main differentiation — Scribe and Tango, the category leaders, are browser
extensions that die the moment a workflow touches System Settings, a native app, or a
terminal. That is one of the few desktop-native arguments that actually holds._

## What it actually does

- **Event-driven capture**: listens for clicks and keystrokes, generates one step per
  meaningful action, screenshotting the frame *before* the click lands (the button you
  are about to press, not the menu that just opened)
- **Screen-recording mode**: continuous H.264 video with cursor-pause segmentation,
  keeping the full footage as evidence
- **Local AI**: macOS Vision OCR plus the Accessibility tree produce step titles
  ("Click Save Draft", not "click the third toolbar button"), smart crop, and decide
  which steps to keep or skip
- **Editor**: reorder, merge, skip, annotate; redaction is destructive — sensitive
  regions are downsampled and upscaled, burned into the bitmap, not a peelable blur
- **Export**: PDF / Markdown / HTML, all three sharing one renderer, so the preview is
  the export
- **Privacy**: no account, no telemetry, password fields excluded at the engine level
  (characters never reach memory); cloud AI polish is off by default and uses your own
  OpenAI-compatible endpoint if enabled

**What it deliberately does not do**: Notion export, auto-translation, cloud sync,
team accounts. Windows is a private test build, not a release.

## What old behavior it replaces

The fully manual pipeline of making a tutorial or SOP: perform the steps once, screen
capture each screen, crop, draw arrows, number, write the descriptions, format. Four
minutes of clicking, an hour of writing. At the tool level it replaces "screenshot plus
manual assembly" (the Snagit way) and "record video then cut it into frames by hand";
at the human level it replaces the large block of time technical writers, support
leads, and implementation consultants spend on docs that are usually stale by the time
they ship.

## Business model

One-time purchase: Pro $129, Team $599 (5 seats), perpetual license including all
future versions. The free tier is not a trial — capture and editing are unlimited and
never expire, exports are capped at the first 10 steps (Markdown/HTML). No
subscription. Paid user count and revenue: not disclosed.

_Read: a one-time price is healthy for a solo Mac tool, but it also means no recurring
revenue to fund development — sustainability rests entirely on word-of-mouth velocity._

## Hard numbers

- launch 2026-08-07: 91 upvotes, 5 comments, daily rank #18
- Independent third-party review (pidune, 3 days of testing): 3.5/5 — correctly
  identified labeled buttons in 11 of 12 steps; one crash during a 45-step recording
  with autosave recovering only the last 12 steps; complex docs still need 15-20%
  post-processing
- macOS 14+, Apple Silicon and Intel, signed and notarized; UI in English, Simplified
  Chinese, and Japanese
- Team size: 1. Paid users: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Built from the founder's own recurring pain, and the decisions are specific enough (down to which frame to screenshot) to prove it |
| Product insight | "Preview is the export", "AI is a polish layer, not a generator", "redaction must be destructive" — three clean calls |
| Execution quality | Native macOS, no telemetry, engine-level password exclusion. Engineered like a real product, not a demo |
| Timing | Scribe/Tango already educated the market, but they are browser extensions; the native-desktop gap is real but small |

## The call

**Among this batch of small tools, the product decisions are the cleanest — and the
business validation is zero.** Three calls worth copying: "preview is the export" (the
editor, preview pane, and all three exporters share one renderer, so you cannot approve
one image and ship another), "AI sits on the polish layer" (a complete local draft
exists first; the model only refines wording, sidestepping the data-exfiltration
objection), and "redaction is irreversible" (no fake, peelable security).

**The fatal flaw is a mismatch.** The real buyers for SOP tooling are company document
teams, who want collaboration, cloud sync, and cross-platform support. StepShot is
solo, Mac-only, and has no team accounts. Individual knowledge workers will like it —
but individual knowledge workers rarely pay $129 for a documentation tool. The paying
audience, if any, is freelancers and independent consultants who deliver documents to
clients, not enterprises.

**Competitive pressure**: Scribe is free, in the browser, zero setup. StepShot demands
accessibility permissions, macOS 14+, and caps free exports at 10 steps. The whole
differentiation rests on the user agreeing that "the browser extension is not enough" —
and StepShot pays that education cost itself.

## What to watch next

① Whether paid users or independent reviews appear within three months — a one-time
purchase product with no growth data runs on reputation alone
② Whether the Team tier ($599) sees any real purchases — enterprise adoption is the
only thing that proves the replacement story
③ Whether the Windows build goes public — staying Mac-only caps the market at Mac share

## What you can take from it

**Product logic**: for any "AI writes your docs/content" tool, generate a complete,
usable draft locally first and put AI on the polish layer (with the user's own API
key). That defuses the data-privacy sales objection and keeps model hallucination from
contaminating the core flow — AI is garnish, not foundation.

**Pricing structure**: free tier that limits export volume instead of features — putting
the paywall on output completeness rather than functionality is a more honest tiering
for content-production tools.

**Positioning language**: nothing worth copying verbatim; the launch pitch earns trust
through specificity (the pre-click frame decision), not slogans.

## Verdict

**Unproven.** The product-level decisions are clean, but business validation is zero and
the audience (company doc teams) is mismatched with the form (a solo Mac app). Write it
down and check back in three months against the three tests above.
