---
slug: human-review
name: human-review
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An AI skill: it makes Claude Code, Codex, or ChatGPT open an HTML or Markdown file in a local browser, where you edit directly and leave comments like a Google Doc, then send everything to the agent in one batch.

## Who built it

Peter Yang. He's an influential product person (ex-Reddit growth, now runs the "Behind the Craft" personal AI system — a dozen-plus skills, a YouTube channel, and a newsletter). This is a personal-brand project, not an anonymous open-source one.

_Read: the author has built-in distribution, which explains part of why it hit ~958 stars two weeks after launch. But the problem is real — he keeps hammering on "giving AI feedback in chat is painful."_

## What it actually does

- **Visual editing** → edit text and basic formatting (bold, italic, lists, indent) directly in the browser; no more "third paragraph, second sentence"
- **Image operations** → resize by dragging a corner, move by dragging, paste new images from clipboard (saved into an assets/ folder and inserted at the cursor)
- **Block rearrangement** → drag a block's left-edge handle to move whole sections, no chat explanation needed
- **Anchored comments** → select a phrase to comment on it, or click an element to comment on an image, chart, or section — like Google Docs
- **Multi-page review** → Command-click links to review several pages without losing your feedback
- **One-shot send** → every edit and comment goes to the agent in a single batch; the agent updates the source and the page auto-refreshes
- **Runs locally** → no account, no cloud, no database, no API key; the review service listens on localhost and comments/state live on your machine
- **Harness-compatible** → installs as a skill into Claude Code, Codex, ChatGPT Work, and any AI harness

## What old behavior it replaces

Giving AI feedback used to mean typing into the chat: "in the third paragraph change X to Y," "cut the right card, it repeats the first one," "rewrite the CTA" — then waiting, then checking each item to see if the agent understood. Reviewing a long doc (PRD, landing page, multi-page site) stacks that translate-to-chat-instructions pain on top of itself.

human-review replaces **the entire "translate visual intent into text instructions" segment** — you edit and comment on the artifact itself, and the agent receives structured feedback instead of a paragraph of natural language. The feedback carrier shifts from description to action.

## Business model

**Free and open source (MIT), no monetization.** The author's value flows to personal brand: the skill is content-asset that feeds the "Behind the Craft" ecosystem (courses, YouTube, newsletter).

_Read: "free skill + personal brand" is 2026's new economy form for AI developer content — build reputation with high-quality free tools, then monetize reputation via courses and content. It doesn't need to charge for the tool itself._

## Hard numbers

- GitHub (petergyang/human-review): **959 stars / 61 forks** (2026-08-14, measured); created 2026-07-27; ~958 stars within two weeks of launch
- Passed SkillsLLM's automated security scan (dependency audit + prompt-injection heuristics), no high-severity findings
- Core files: cli.js (commands), server.js (local session), sdk.js (editing/comments), chrome-client.js (visual UI), markdown.js (Markdown rendering)
- Users: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. A heavy AI content creator who spends daily hours on giving agents feedback |
| Product insight | "The shape of feedback decides whether it gets used" — reuse an interaction humans already know instead of teaching them to write prompts |
| Execution quality | Engineering-complete (clean CLI/server/sdk/frontend layering), passed a security scan, explicit local boundaries |
| Timing | Exactly when "the final 10% of human polish in human-machine work" is widely discussed. Well timed |

## The call

**It proves the "feedback interface" is an undervalued product layer.** Everyone optimizes prompts, models, and agent frameworks; almost nobody optimizes the act of a human handing opinions to an AI. human-review substitutes Google-Doc-style annotation — an interaction two billion people already know — for writing precisely-located chat instructions. That's the real reason for 959 stars.

**Its boundary is equally clear**: it only solves text-content feedback (HTML, Markdown, landing pages, PRDs), not code review, data, or audio. The bet is that "text review" is a big enough scenario.

**The extension worth watching**: review is training signal. Every edit and comment you leave on an artifact is a labeled sample of "what good looks like." If that feedback is captured structurally, the next agent run starts from your standards instead of guessing your taste from zero. That "review-as-data" direction matters more than the tool itself.

## What to watch next

① Whether stars pass 3,000 — it would become the representative project of the "human-machine review interaction" category
② Whether teams integrate the review-feedback loop into daily delivery, not just individuals
③ Whether the review data/comments it collects evolve into "style memory" features — the move from tool to standard

## What you can take from it

**Product logic**: in any "a human corrects an AI" scenario, first ask what interaction the user already knows — Google Doc comments, Word tracked changes, browser highlight — and make the AI fit that shape instead of making the user fit prompt syntax. Feedback interfaces beat instruction interfaces on adoption.

**Positioning language**: "Stop editing paragraph 3 in chat." Opening with the user's specific pain outperforms "AI review workflow platform" by an order of magnitude.

**Distribution**: free + open source + personal brand + one pain-point slogan — that three-piece kit took a two-week tool to nearly a thousand stars. Skills are becoming a distribution unit: packaging a feature as a one-line installable skill spreads faster than shipping your own app.

## Verdict

**Worth watching.** It validates the feedback-interface layer with an engineering-complete open-source skill and real heat (959 stars in two weeks). It has no business model, but it may define the standard shape of human-machine review interaction. Note it and watch how far it goes toward "review as data."
