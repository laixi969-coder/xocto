---
slug: writemd
name: Write.md
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A free, open-source (Apache-2.0), fully themeable Markdown editor for macOS. It ships no
themes; instead it hands you a set of appearance controls — fonts, sizes, line height,
colors, opacity, glass, image and video backgrounds — so you rebuild the editor's "room"
to your liking and save it as a switchable profile. The document underneath stays an
ordinary local Markdown file.

## Who built it

Solo-developed and solo-maintained by Daniel Bilek (GitHub: danielbilek/writemd), repo
created 2026-07-04, launched as a Show HN on 2026-08-11, already at v1.0.1. The README
notes "Built by Daniel Bilek with Jean2" — Jean2 (jean2.ai) appears to be an AI coding
tool, meaning the editor is itself an AI-assisted build (its exact form is unverified).

**Watch out for a name collision**: the Mac App Store has a different "write.md" by
Gotaru Co., Ltd. (a rich-text editor that saves Markdown). Unrelated to this open-source
project.

_Read: another proof that in the AI era a solo developer can ship a release-grade macOS
app — one person, two months, v1.0.1, top-of-front-page HN quality. The author answered
"why not native" comments on HN honestly (it is Electron), which reads as likeable._

## What it actually does

- **Appearance profiles** → fonts, size, line height, and content width; text, background,
  accent, header, footer, and border colors; window opacity, glass, and borders; unified
  or separated regions; image and video backgrounds — all adjustable and saved as named,
  switchable profiles
- **No bundled themes** → the site says outright it ships no theme pack; the examples were
  all built with the in-app controls. Skinning is a capability you perform, not a catalog
  you buy
- **Optional small tools** → Vim mode (modal editing without opening an IDE), local US
  English spelling and basic style suggestions (no AI service, no account)
- **Three views** → unified editor, rendered preview, or split view
- **Status details** → file name, word count, reading time, correction count, Vim state
- **Plain local files** → open and save .md, .markdown, and .txt; no telemetry, no
  analytics, no login

**What it deliberately does not do**: no cloud binding, no accounts, no AI writing
service, nothing uploaded — the only network call is a check-for-updates request to
GitHub Releases that does not include document content.

## What old behavior it replaces

Desktop Markdown writing previously meant picking between Typora (paid, WYSIWYG),
Obsidian (free, vault/double-link-centric), and MacDown (free but unmaintained — an HN
user noted it may stop working under Rosetta soon). The shared pattern: **the editor
gives you a fixed look and you adapt to it.**

Write.md inverts that — **the editor adapts to you**: not syntax-highlight color schemes
(the surface layer) but the whole material of the writing surface (fonts, opacity,
background). It replaces the old experience of compromising across a hundred settings to
get a late-night writing environment. It does not chase feature-count; it focuses on one
thing — the felt atmosphere of the writing space.

## Business model

**None.** Free, open source, no in-app purchases, no cloud, no paid plan.

_Read: the classic "build it properly, give it away" personal project. Its commercial
value is not revenue; it is the portfolio proof (v1.0.1 quality is itself a résumé), the
HN exposure and personal brand, and an attitude — free against paid Typora, simple
against complex Obsidian. What a reader should copy is not the business model (there is
none) but how it turned "appearance config," a feature nobody else cared about, into the
differentiator._

## Hard numbers

- HN Show HN: 86 points, 68 comments, high-quality discussion (Typora/Obsidian
  comparisons, the Electron debate)
- GitHub: 12 commits (solo), v1.0.1 (2026-08-12), Apache-2.0
- Currently Apple-silicon Macs only; signed and notarized DMG on GitHub Releases
- Stack: Electron + TypeScript + React + CodeMirror 6 + Bun
- Star count and downloads: not surfaced in our scrape; early-stage volume

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | He built a comfortable editor for his own blogging; he is the first user, and the motive is real |
| Product insight | Elevated "appearance configurability" from a fringe feature to the product theme — everyone does syntax highlighting, this one does the whole room |
| Execution quality | Single Electron package, signed and notarized, auto-update, 1.0.1 in twelve commits — a complete engineering loop |
| Timing | Editor red ocean, but "room atmosphere" is unclaimed territory; no timing advantage, no disadvantage |

## The call

**A case of experience-niche differentiation inside a feature red ocean, and the
trade-off logic is what deserves copying.**

Markdown editors have hit the feature ceiling: double links, plugin systems, AI
continuation, sync — anyone can list them. Write.md built none of that and bet on one
point nobody else holds — **the material feel of the writing space**. It made that point
first-class: no bundled themes, users build their own, save them as profiles. That
single choice gives it a clear identity among editors with longer feature lists: not
another Typora, but "the one that turns your editor into a late-night study."

**The cost is legible too**: the audience for this differentiation is finite. The
atmosphere crowd is real but small, and Electron's size and performance count against it
with the native-first crowd (one HN commenter said "Made for Apple silicon" on an
Electron app would put them off). It will most likely stay a small, well-made free tool,
not a business.

**The transferable rule**: when a category is fully feature-packed, find one
experience-oriented slice and go deep. In a functional red ocean, emotional value — the
atmosphere of writing — has no competitor. But note: experience differentiation usually
means a small market; it is a place for an indie to stand, not a place to build a big
business.

## What to watch next

① Whether GitHub stars cross a thousand in three months — the main diffusion signal for
a free open-source editor
② Whether a community of shared user-built profiles emerges — if self-made skins start
being shared, the differentiation is validated
③ Whether the author puts it on the App Store or turns it paid — that tells you whether
this is a portfolio piece or a product

## What you can take from it

**Product logic**: turn what users can change into a capability, not a catalog. Write.md
does not sell themes; it gives you the controls to make themes. Every user's result is
therefore unique, and the product naturally generates a sense of "my personal version."
For personalization products, handing out controls retains people better than handing
out templates.

**Positioning language**: "Your words. Your space." — placing "your words" and "your
space" side by side says the whole philosophy in one line, versus functional language
like "highly customizable editor." The former has a picture in it.

**Pricing structure**: none. But "free + no telemetry + no accounts" as a default stance
is worth copying for personal projects — when a small tool carries no commercial
pressure, clean privacy is itself a differentiator.

## Verdict

**Worth watching.** Nothing new in features, but "the material feel of the writing
space" is genuinely unclaimed in the editor red ocean, and the engineering finish
deserves the HN attention. It is unlikely to become a business, but as a specimen of
experience-niche differentiation in a commodity category, it is highly instructive. In
three months, look for a small community of user-built skins.
