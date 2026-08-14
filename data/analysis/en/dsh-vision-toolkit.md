---
slug: dsh-vision-toolkit
name: dsh-vision-toolkit
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

Giving a text-only model a pair of callable eyes — image Q&A, long-screenshot OCR, UI restoration, and pixel diff are packaged as 10 tools the agent invokes on demand, instead of pretending the model can see.

## Who built it

Author Anionex (GitHub @Anionex, X @anion_ex, personal site anionex.me). He first built the upstream general-purpose vision toolkit, agent-vision-toolkit, and then this DSH-native integration layer on top of it. Repo created 2026-08-13, MIT, v0.1.4, 44 commits. A personal open-source project with an optional FUNDING.md (explicitly stating sponsorship buys no roadmap priority and no private support).

_Read: the only author of the six with upstream assets — general purpose first, integration second. That order suggests he is solving the real problem of "text models have no vision," not hastily assembling something to ride DSH's popularity._

## What it actually does

- **10 vision tools** → glance (describe / directed Q&A / OCR / multi-image compare), ground (locate target, return pixel boxes), detect (element inventory + pixel-box location), trace (image to SVG vector), crop, pixel_diff (pixel-difference heatmaps), long_screenshot_ocr, extract_foreground, dominant_colors, html_screenshot
- **Intent-aware execution** → each tool executes a specific intent (locate, detect, trace) rather than taking generic "describe this image" input
- **Artifacts** → produces files that can be previewed, downloaded, and opened (SVG / PNG / JSON reports)
- **Local/remote hybrid** → local tools (crop, trace, pixel diff, color, foreground, HTML screenshot) are free and never leave the machine; remote tools (glance/ground/detect/long-screenshot OCR) require the user's own OpenAI-compatible vision API credentials
- **Progressive exposure** → only an activation tool is exposed by default; all 10 mount only after the vision-tools skill loads — controlling prompt bloat and attack surface
- **Security model** → path restrictions against traversal, image pre-decode validation, credentials never enter logs, sandboxed browser rendering
- **Web + Headless dual profile** → dedicated settings page, health checks, connection tests, version view

**What it deliberately does not do**: it reimplements no vision algorithms — those all live upstream in agent-vision-toolkit; this plugin is only DSH's integration layer (lifecycle, credentials, schema, Artifacts, web presentation). The division of labor is clean.

## What old behavior it replaces

DeepSeek's flagship text model has no vision (testers were explicit: "V4 itself doesn't support vision; image scenarios still require pairing a multimodal model"). Adding vision to a text-only agent previously meant one of two roads: human relay — you type a description of the screenshot to the model; or hand-assembled tooling — you write throwaway Python/OpenAI-API glue scripts, send the image to a vision API, paste the result back into the conversation. Each road is a few tens of minutes of temp work per occurrence, error-prone, and not reusable.

dsh-vision-toolkit replaces that hand-rolled glue. Vision becomes a set of structured tools the agent can call: explicit intent (locate vs detect vs trace), credential management, Artifacts output, web settings pages. It also quietly replaces an implicit old behavior — the QA gesture of "compare screenshots to check whether the UI changed correctly" (pixel-diff tool plus UI restoration verification), which previously meant eyeballing two screens side by side.

## Business model

**Free plus bring-your-own-API-credentials.** The plugin is MIT and free; remote vision tools bill through the user's own OpenAI-compatible vision API credentials; local tools are entirely free. An optional sponsorship channel exists (FUNDING.md), explicitly not buying priority.

_Read: the only one of the six that states its cost structure clearly. "Free plugin, you pay the inference bill" is the standard posture for tool-class AI plugins, because this is essentially a call orchestrator — the money goes to the model API, not the software. Which also means it has no software revenue, only influence revenue._

## Hard numbers

- **264 stars / 17 forks / 4 open issues** (GitHub API, 2026-08-14)
- Created 2026-08-13, 44 commits, v0.1.4
- 17 Vitest files / 136 passing tests — among the hardest test quality in this batch
- UI restoration verification: initial pixel difference 6.04% → final 0% (1200×720)
- Single image ≤10MB / ≤40MP, timeouts 1000-600000ms, concurrency 1-16, inputs PNG/JPEG/GIF/WebP
- Team, users, downloads: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | General-purpose toolkit first, integration layer second; the pain is his own and the path is continuous |
| Product insight | Both "vision is a tool, not a model attribute" and "intent-aware execution" are correct; the verification loop (render → screenshot → pixel diff) is a bonus |
| Execution quality | 136 tests, a security model, dual profiles, pinned dependency versions — one of the most disciplined engineering efforts in this batch |
| Timing | Perfect: the official text model has no vision, and in a 70k-star ecosystem that gap is a real need; but remote tools depend on third-party vision APIs, so the cost chain is unstable |

## The call

**The closest of the six to a real product — real capability, real verification, clear cost boundaries.**

Its core judgment is worth copying into any AI product: **capability is a tool, not a property of the model.** The model can't see, so hand it a tool that can, rather than waiting for the next model generation. This makes "text model + vision tools" functionally equivalent to a multimodal model at an order of magnitude less cost — DeepSeek users don't have to upgrade models just to look at a screenshot.

**Transferable rule: your product's shortcomings can be patched with callable external tools; you don't have to wait for the core capability to upgrade.** Plus "progressive exposure" — capabilities are not loaded by default and mount only when used, saving tokens and shrinking the attack surface. It is the security posture most worth copying when adding capabilities to an agent product.

**Its weakness**: remote vision tools depend on the user's own third-party API credentials, which makes it an orchestrator with zero margin; if DeepSeek ever ships a multimodal model, the value of its remote tools gets cut in half (the local tools survive). It is betting that the "text model + tool combination" paradigm keeps holding.

## What to watch next

① Real usage/cost cases of the remote tools — has anyone published a bill proving "an order of magnitude cheaper than multimodal"
② Whether DeepSeek officially ships a multimodal model — if so, remote-tool value halves
③ Whether stars/tests stay in sync with official rc iterations — fall behind and it stops installing

## What you can take from it

**Product logic**: when adding capabilities to an AI product, prefer "toolification" over "modelfication" — make capabilities on-demand, credentialed, with output, rather than waiting for a model upgrade; it's a generation faster. Also copy progressive exposure: new capabilities are not mounted by default and load only when used — cheaper and safer.

**Positioning language**: borrowable. The description opens with "helping text-only models do visual tasks better" — it admits the model's limitation (text-only) first, then offers the fix (tools). This "acknowledge the limit, then fill the gap" phrasing reads as far more credible in the developer community than empowerment-style language.

**Pricing structure**: borrowable. "Free plugin, you pay the API bill" — expose the cost, price the software at zero, and users can do the math before they trust it. It even wrote a FUNDING.md that declares sponsorship buys no priority, handling the awkwardness of asking for money cleanly.

## Verdict

**Worth watching.** The closest of the six to a real product: real capability, sufficient verification, clear cost boundaries. The "toolify vision" and "progressive exposure" mechanisms can be lifted directly. Its ceiling depends on whether DeepSeek ships a multimodal model — that variable is worth tracking.
