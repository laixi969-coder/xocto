---
slug: gutta
name: Gutta
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A tiny task list in the Mac menu bar: press ⌘⇧Space, type tasks the way you'd say them, hit return, and get back to work. Local storage, no account, no subscription.

## Who built it

Vaibhav Pathak, an independent developer whose launch post says "capturing a task should take seconds, not pull you into another app." First public release.

_Read: a classic personal tool — the author couldn't stand heavyweight todo apps and built one that stays out of his way. The weakness of this category is "small, beautiful, and unknown"; PH heat is currently its only external validation._

## What it actually does

- **Keyboard-first** → ⌘⇧Space to summon, type, return, done — no mouse for the whole loop
- **Natural-language time** → "buy bread tomorrow morning" and "call mom at 5pm" parse into scheduled tasks; morning/afternoon/evening get sensible defaults, explicit times win
- **Batch entry** → semicolon-separated input splits into individual tasks
- **Local reminders** → global default lead time (15/20/30 minutes, etc.), overridable per task; it only asks for notification permission when there's actually a future reminder
- **Folder-based sync** → sync across Macs through a folder you choose in iCloud Drive, Dropbox, or OneDrive; one JSON record per task, no database conflicts; no Gutta account, no developer-owned cloud
- **Offline-first** → SwiftData local storage; works without a network and catches up when connectivity returns

## What old behavior it replaces

Capturing a small task like "buy bread tomorrow morning" used to mean: open Things/Todoist (slow, forms, login, subscription), use system Notes (no reminders, no time awareness), or just hold it in your head (you will forget).

Gutta replaces the mismatch of **paying a whole app's cost for one small task** — it compresses task capture to two seconds and leaves data ownership with the user.

## Business model

**Free.** Open source, no subscription, no account, no in-app purchase. The only "cost" is the user's own cloud folder.

_Read: there is no business model. Authors of this kind of tool typically monetize via visibility (freelance, other products) or it's simply the author's tool fetish. Judge it purely on whether it's good to use._

## Hard numbers

- launch (2026-08-10): **145 upvotes, 6 comments, #7 of the day**
- Requires macOS 14+; SwiftData; open source on GitHub
- One JSON per task, folder sync, no database conflicts
- Users: not disclosed (first release)

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. The author is the target user; the feature set is literally his habits |
| Product insight | "Your task data belongs to you" and "keyboard-first" are two genuinely real differentiators |
| Execution quality | Code unverifiable, but the first release is feature-complete (capture, reminders, sync) |
| Timing | To-dos are the reddest of red oceans, yet "local-first, no subscription" is still pulling paying users |

## The call

**It wins by refusing.** Other todo apps stack on teams, calendars, boards, and AI; Gutta cuts down — no account, no subscription, no cloud, no developer database. That "we provide nothing" stance is exactly the product definition: your data stays in your folder, and the entry point shrinks to one keyboard shortcut.

**Its risk is the edge of "less."** No reminders-that-expire handling beyond scheduled ones, no scheduling beyond natural-language time, macOS 14+ only — it can't serve heavy task-management users; and light users usually won't install a new tool to save two seconds. PH #7 shows it captured the first wave of attention, but the retention curve for todo tools is crueler than most categories.

**Market read**: local-first tools (Things with its one-time purchase) keep a loyal paying base, which proves "no cloud, no subscription" is a sellable stance. Gutta's problem isn't positioning; it's whether the author treats it as a long-term project.

## What to watch next

① GitHub stars and release cadence — whether the author treats it as a long-term project
② Whether "it replaced my previous todo app" user testimonials appear in three months
③ Whether it extends to iOS (a menu-bar tool's natural ceiling is the number of Mac users)

## What you can take from it

**Product logic**: for productivity tools, cutting friction from thought to capture beats adding features — it compresses the input path to one shortcut plus natural language, and that's the entire design. Any capture-class tool should ask first: from "I thought of it" to "it's recorded," how fast can it get?

**Positioning language**: "data stays on your Mac, sync goes through your own folder" — "your" instead of "our" builds trust. The most effective sentence pattern for local-first products.

**Pricing**: no pricing is itself the selling point (free + open source + no account). For small tools like this, defer the business model and first verify whether anyone actually keeps using it.

## Verdict

**Worth watching.** PH #7 of the day (145 upvotes) means it captured its first attention; the positioning is clear and the stance is rare. But it's a free tool with no business model and unknown retention. Note it and check in three months whether it's still being iterated.
