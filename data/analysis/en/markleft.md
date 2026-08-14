---
slug: markleft
name: Markleft
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A "suggestion mode" for Markdown: you annotate the document in place — text, code, tables,
diagrams, SVGs — and the AI appends suggestions instead of rewriting the whole file, leaving each
one for you to accept.

## Who built it

Martin R. Lysk (HN: mlysk), an individual developer. A Chrome bookmarklet, an annotation spec, and
an 11-minute blog post (2026-08-09); code at github.com/martin-lysk/markleft.

_Read: this is a methodology-before-product project — the article first argues why the current flow
is absurd, then gives you the tool. That order is itself noteworthy: it assumes readers are people
who want to improve the AI writing-iteration loop, not people who want to install a plugin._

## What it actually does

- **Annotate in place** → comment on selected text, code lines, tables, Mermaid diagrams, SVGs;
  image annotations use normalized coordinates (image-X-Y)
- **Comments are Markdown footnotes** → annotations are encoded into footnote ids
  (range-prev-12-chars, image-X-Y, code-line-L-col-C-len-N); a normal renderer like GitHub just
  sees footnotes, so the Markdown stays intact
- **Stable block ids** → an HTML comment `markleft:block id=...` before each document block makes
  structural changes addressable
- **Append-only suggestions** → suggestions are unreferenced footnotes
  ([^suggestion-s2-update-block-xxx]); the AI can append proposals but cannot alter the document
  it reviews
- **Suggestion rendering in the editor** → diffs within rendered elements (list items and table
  cells are paired before comparing); image-only replacements become before/after sliders
- **Bookmarklet workflow** → open a local Markdown file in Chrome, click the bookmark, get an
  editor with annotations and accept/reject; saving compiles a prompt teaching the AI the Markleft
  syntax

**What it deliberately does not do**: does not change the Markdown format, no cloud service, no
default path of "AI rewrites the whole file."

## What old behavior it replaces

The default flow of iterating a long document with AI: you describe in chat, in prose, what's
wrong → AI rewrites everything → you play spot-the-difference between two versions → and you have
to remember which of your original words maps to which change. The author's analogy: mailing a
colleague a five-page document, getting back a prose essay of dislikes, then a fully rewritten
version, and being asked to compare the two yourself to judge whether they understood — a flow
document collaboration solved decades ago with comments and tracked changes.

markleft replaces the absurd chain of "prose feedback + full rewrite + manual diff" with
"in-place annotation + append-only suggestions + diffs anchored to comments." The idea transfers
to any AI-generated-document review scenario, not just Markdown.

## Business model

**None.** Free bookmarklet, open source (github.com/martin-lysk/markleft), no pricing page.

_Read: this is a technical/methodological essay with no trace of commercial intent. Its value is in
the method, not the product form._

## Hard numbers

- **HN: 8 points, 1 comment** (2026-08-13), Show HN; the only comment is the author's own repo link
- Blog post: 11-minute read, published 2026-08-09
- Annotatable targets: text, code lines, tables, Mermaid, images (SVG), blocks
- Users, usage: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | The author is clearly a heavy AI-documentation user; pain firsthand; methodology written with unusual clarity |
| Product insight | "Append-only suggestions" against "full rewrite" is one of the biggest unsolved problems in current AI writing tools, and the entry point is well chosen |
| Execution quality | The comments-as-footnotes spec is clever and stays compatible with ordinary Markdown renderers; but the bookmarklet form limits reach |
| Timing | AI document generation is entering a "output exceeds review capacity" phase; review tools are in rising demand, but buyers are not yet clear |

## The call

**A textbook case of retranslating a problem document collaboration solved two decades ago for the
AI era.**

Comments and tracked changes solved "how humans edit one document" in Word/Google Docs, but when
AI arrived, everyone regressed to the primitive flow of describe + rewrite + manual diff. markleft
doesn't invent a new interaction; it translates the constraints of an old one into a format AI can
consume — append-only, addressable, acceptable or rejectable.

**The transferable rule: for feedback channels to AI tools, prefer "append" over "rewrite."**
Appending is both a permission boundary and an auditability boundary: the AI may propose anything,
but it cannot touch your original. That single constraint solves two problems at once — preventing
overreach, and letting a human quickly confirm "what changed, and which comment does it answer."

**Its ceiling is equally honest**: a bookmarklet is a personal-tool shape, and 8 points means
almost nobody saw it. The real destiny of this method is probably absorption by an editor, Claude's
artifacts, or a document tool — not growing into a product itself.

## What to watch next

① Whether any editor or writing tool absorbs the "append-only suggestions" interaction — validation
that the method is a public good
② Whether the repo's stars/issues move — the most common fate of bookmarklet projects is author
self-use
③ Whether the author grows the spec into a cross-tool standard — "comments as footnotes" is
meaningless confined to one bookmarklet

## What you can take from it

**Product logic**: any review loop in an AI content tool should copy the "append-only suggestions +
addressable annotations" pair — it gives you both a permission boundary and auditability.
Implementation-wise, encoding annotations into footnote ids to keep format compatibility is a
low-cost high-return move.

**Positioning language**: the author's opening analogy ("you wouldn't send a colleague a prose
essay of criticism and ask for a full rewrite") is a reusable template for explaining why a current
flow is absurd — usable in any AI-workflow product pitch.

**Pricing structure**: none. Free and open source.

## Verdict

**The method is worth something; the product hasn't grown yet.** "Append-only suggestions" is one
of the few designs in AI document collaboration that solves permission and auditability at once;
8 points doesn't change the value of the method. But the bookmarklet form and zero commercialization
signs likely keep it at the personal-tool level. Note the interaction pattern and wait for it to be
absorbed elsewhere.
