---
slug: andromeld
name: AndroMeld
verdict: Worth watching
analyzed_at: 2026-08-14
---

## What it is in one line

A Continuity-style experience for the "Android phone + Mac" combination: Android
apps mirrored into separate native-like Mac windows, app handoff, Android storage
in Finder, two-way notifications and clipboard — with all data traveling directly
between devices, never through a cloud server.

## Who built it

Ruoxin He, an independent developer. Public track record: creator of IceBox
(5M+ downloads on Google Play) and FilterBox. This time he is wiring the Android
ecosystem into the Mac.

_Read: someone who has shipped a 5M-download app is not a beginner testing the
water. IceBox was exactly this kind of gap-filler (more control over Android
TV-box devices), and AndroMeld is the same judgment applied again — the seam left
by platform exclusivity is worth sewing repeatedly._

## What it actually does

- **App-by-app mirroring** → not whole-screen mirroring in one fixed window like
  scrcpy; multiple Android apps, each in its own resizable, native-feeling Mac
  window at the same time
- **Handoff** → continue an app that is already open on your phone
- **Input and control** → type with the Mac keyboard, navigate with trackpad
  gestures; launch Android apps from Spotlight, see them in the Dock, pin app
  shortcuts to the desktop
- **Finder integration** → browse Android storage in Finder with drag-and-drop and
  Quick Look; drop files directly into the current Android app
- **Notifications and clipboard** → synced both ways, flattening the boundary
  between the two systems
- **Connections** → USB and Wi-Fi with automatic reconnection; APK preview and
  install
- **An MCP server** → for tools like Claude Code and Codex, which effectively lets
  an agent operate the phone
- **A free Web App** → control up to four Android apps from a browser at once

**What it deliberately does not do**: relay screen/audio streams, clipboard
content or files through a cloud server; no account system — all data travels
directly between devices.

## What old behavior it replaces

"Moving things between an Android phone and a Mac" used to be a chain of
compromises:

**scrcpy** — the developer's path: command line and adb, whole-screen mirroring
in one fixed window, one app at a time, no Finder integration, and ordinary
people will never install it.

**Cloud relays like AirDroid** — accounts required, data through servers,
sending sensitive files is nerve-racking, and the experience is web-like rather
than local.

**"Emailing files to yourself"** — AirDrop is unavailable (Apple ecosystem
lock-in), so the workaround was email to self, WeChat file-transfer, cloud-drive
relay, and copy-paste back and forth. Notifications and clipboard had no
cross-device solution at all.

AndroMeld replaces the whole chain: scrcpy's capability in a GUI normal people
can use, cloud relays replaced by direct connection, "email files to myself"
replaced by dragging in Finder. It is sewing the seam Apple created with its own
closed ecosystem — a seam Apple will never close.

## Business model

Published on the Mac App Store; the official line is "every feature is free to
try," plus a completely free Web App. Full pricing (subscription vs. one-time,
exact price) is **not disclosed**.

_Read: independent developer plus one-time purchase (most likely) is the standard
path for this category — no cloud cost, no account system, marginal cost near
zero, which gives pricing flexibility. But see the ceiling too: the Android 16+
requirement plus the fact that Mac users who also use Android is a small pool. Like
IceBox, this is a "small but stable" seam business._

## Hard numbers

- Author's prior work: IceBox, 5M+ downloads on Google Play
- Device requirement: Android 16+ devices, USB or Wi-Fi
- Platforms: Mac App Store (product), plus a free Web App (browser control of up
  to 4 apps)
- Price, users, downloads: **not disclosed**
- launch around 2026-08-05; no upvote data captured

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | High. The author has shipped a 5M-download gap-filler before; device-ecosystem seams are his specialty |
| Product insight | The per-app windows + handoff + Finder combination is exactly Apple Continuity translated to Android; precise direction |
| Execution quality | Direct transfer, no accounts, an MCP server, Finder integration; substantial build, and the author has delivery precedent |
| Timing | A stable seam. The Android-plus-Mac dual-user population persists, and Apple will never close it |

## The call

**The most complete sample of a "seam-sewing" product.** The trick is not
building features; it is translating an experience that already exists in a big
vendor's ecosystem (Continuity) to a place where it does not. Every feature here
has a counterpart in Apple Continuity — per-app windows, handoff, Finder,
clipboard — which is far more reliable than inventing features from scratch.

**Three signals worth noting.** First, direct connection plus no accounts is a
selling point that hits privacy-sensitive users at their decision point. Second,
an MCP server for Claude Code and Codex — letting agents operate the phone — is
more forward-looking than the mirroring itself. Third, the author's 5M-download
precedent means he knows how to distribute this kind of tool.

**Stay sober, though.** The Android 16+ requirement cuts off many devices; the
Mac-plus-Android dual-user pool is small; and the ecosystem already has partial
substitutes. The ceiling is "small but stable," not explosive growth.

## What to watch next

① First-month downloads and ratings on the Mac App Store — retention and word of
mouth are the hard metrics for a seam tool
② Whether the Android 16+ floor gets lowered (broadening the usable device base)
③ Evidence that the MCP server is actually adopted by agent toolchains — that is
the extra future curve beyond being a mirroring tool

## What you can take from it

**Product logic**: when hunting for a market seam, first find experiences that a
big ecosystem has already taught users, then translate them into the other
ecosystem — users do not need to be educated, only migrated. The best starting
point for a gap-filler is "the other side already has it."

**Positioning language**: "Bring a Continuity-style experience to Android and
Mac" names an unknown feature with a known product (Continuity) at zero
explanation cost. Stealable.

**Pricing structure**: free to try, a free Web App, direct transfer with no
accounts — earn trust first, then sell on experience; and make "does not go
through the cloud" an explicit selling point.

## Verdict

**Worth watching.** Right seam, complete experience, an author with a 5M-download
track record, and two points — direct transfer with no accounts, and the MCP
server — that go further than its peers. But it is destined to be a small-pool
business; verify it by first-month downloads and word of mouth, not by a growth
curve. It is another validation of the "seams left by platform lock-in" thesis.
