---
slug: gotcha
name: Gotcha
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

An open-source "copilot" for Android: you say a sentence and it acts on your phone — sending texts, opening apps, changing volume, running Termux scripts — instead of just replying with text.

## Who built it

Rishabh Bajpai and one co-founder. Their launch-post trigger: almost every mobile AI assistant is "a glorified text box wrapped in a fancy UI. You ask it a question, it types back a response, and then you still have to manually open your calendar, copy text, and act yourself." They wanted a locally executed agent that actually does things. License: AGPL-3.0.

_Read: a direct response to the "mobile AI only chats" pain, differentiated by local execution and open source rather than head-on competition with cloud assistants._

## What it actually does

- **Natural-language phone control** → 100+ device tools: calls, SMS, contacts, calendar, alarms, files, apps, location, camera, notifications, screen automation, device admin, root operations
- **Autonomous loop** → plan → execute → observe → adapt, reading screen and terminal output for context
- **UI automation** → drives Android Accessibility Services to tap, fill forms, and scroll like a human; also runs bash/Python/git/curl inside Termux
- **Dual safety modes** → Monitor (read-only inspection and planning) and Operator (action-capable). Destructive actions and outgoing email require confirmation; dangerous shell commands are blocked; actions land in an append-only audit log
- **Cross-app floating ball** → floats over any app, push-to-talk with current screen context
- **Bring-your-own model** → local LLMs (Ollama, LM Studio, llama.cpp with Qwen 2.5) or cloud (Gemini, Groq, OpenAI); free starter credits come from the Samosa AIR proxy
- **Ecosystem integrations** → Home Assistant, Notion, contacts, SMS, health data

## What old behavior it replaces

"Say it and it's done" on a phone used to have only a few implementations: Google Assistant/Siri's limited action set (system-level basics, no deep cross-app links), "voice command" apps (preset triggers only), or manual labor — unlock, open the app, tap a few times, paste text.

Gotcha wants to replace that whole middle stretch by putting an agent inside the phone that can see the screen, tap the UI, run scripts, and cross app boundaries. Comparable options are Rabbit R1-style hardware (expensive, another device) and cloud phone agents (your data leaves the device). Gotcha's selling point is **local execution, data never leaves the phone**.

## Business model

**Free and open source (AGPL-3.0), APK sideloaded from GitHub Releases.** Models are bring-your-own: the user connects their own LLM and pays any provider cost; Samosa AIR offers free starter credits, giving that proxy router a funnel.

_Read: no direct revenue short-term. The paths forward are a hosted/Pro layer or converting Samosa AIR into a model reseller. Free credits to funnel users into your own API is the standard play right now._

## Hard numbers

- launch (2026-08-11): **95 upvotes, 3 comments, #15 of the day**
- GitHub (samosa-ai-com/Gotcha): 9 stars, newly created
- 100+ device tools, wake word in 9 languages
- Requires Android 11+, sideloaded APK
- Users, DAU: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. They are exactly the people frustrated by "mobile AI only chats" |
| Product insight | Making safety tiers (Monitor/Operator + audit log) a first-class feature is rare in an early product |
| Execution quality | Early APK; the authors explicitly ask testers to report OEM compatibility differences. Needs time to prove out |
| Timing | Phone agents are widely accepted as the next wave, but competitors (built-in assistants, cloud agents) are bigger |

## The call

**The bet is whether "local execution" differentiation holds.** Cloud agents hit permission and privacy walls; built-in assistants are limited and don't cross apps. Gotcha's open source + local + bring-your-own-model position targets privacy-sensitive technical users. The position is real; the problem is scale.

**The bigger variable is OEM fragmentation.** Accessibility behavior, background limits, and permission screens differ across ROMs — the authors themselves list Pixel/Samsung/Xiaomi differences as the feedback they most want. The failure mode for this category is not a weak model; it is "doesn't work on someone else's phone."

**Collision risks**: several products already use the name Gotcha, and big vendors will move into the phone-copilot lane soon. It has to buy time with engineering speed and community trust.

## What to watch next

① Whether GitHub stars pass 100 in three months — the honest heat signal for an open-source tool
② Whether users share real "complex cross-app task executed successfully" cases, not just demo videos
③ Whether Samosa AIR's free-credit strategy converts into a real paid tier — that determines if it's a business

## What you can take from it

**Product logic**: when building high-risk automation, make the safety mode a product feature (read-only/action tiers + audit log) rather than a buried setting. Let users try in read-only confidence before granting power; that beats any permission-popup copy.

**Positioning language**: "You talk. It acts." — four words that draw the line between a chat AI and an action AI. The single most copyable sentence in this product.

**Distribution**: open source + sideload + bring-your-own-model pushes both distribution cost and cloud cost onto the ecosystem, in exchange for a "completely free" talking point. Worth copying for any trust-heavy infrastructure tool.

## Verdict

**Worth watching, but very early.** Direction is right, the safety design is serious, and the launch heat is real (PH #15 of the day), but the code just shipped, adoption is negligible, and OEM compatibility is unknown. Note it and check the three points above in three months.
