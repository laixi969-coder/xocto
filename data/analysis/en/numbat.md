---
slug: numbat
name: numbat
verdict: Worth watching
analyzed_at: 2026-08-13
---

## What it is in one line

Not another row of permission toggles for your agent, but surveillance for it: what it did on
this machine, whether to stop it mid-action, and how to reconstruct the whole thing afterward.

## Who built it

Perplexity's official repository (`perplexityai/numbat`), Apache-2.0, a single Go binary.

_Read: when a search company shows up building endpoint security for agents, it usually means
the problem bit them first. Perplexity hurts on both sides — heavy internal agent use, and
being one of the most aggressively crawled targets on the outside._

## What it actually does

- **Watches four kinds of agent** → desktop, CLI, IDE, and gateway, observed through local
  hooks, plugins, OTLP/HTTP logs, and on-disk session artifacts, normalized into one event model
- **Decides locally** → built-in CEL rules, multi-step sequence rules, and custom YAML rules;
  detection runs on the endpoint and nothing has to leave it
- **Optional blocking** → only on supported synchronous pre-action hooks, off by default, and
  every shipped rule is **monitor-only**
- **Reconstructs after the fact** → rebuilds sessions from on-disk artifacts, so it can
  investigate activity that predates its own installation
- **Exports case bundles** → SHA-256 manifests, secrets redacted, and normal output never
  contains a complete raw transcript

**What it deliberately does not do**: no cloud control plane, no blocking by default, no full
transcripts in routine records. All three are deliberate restraint — the classic way a security
tool dies is by becoming a new leak in the course of giving you visibility.

## What old behavior it replaces

Companies have watched employee machines with EDR for two decades. EDR's subject is a person
and a process: who installed what, who connected where, who touched which file.

Agents break that. An agent's actions happen inside someone else's process, over someone else's
API, and land in someone else's session files. EDR sees "a terminal program made a network
call." So the question "what exactly did that agent change last week" could only be answered by
a human scrolling back through a chat log — assuming the log still existed.

## Business model

**Not disclosed.** Apache-2.0, no pricing page, no hosted service.

_Read: the money in this category has always been in the enterprise control plane — policy
push across fleets, unified alerting, audit reporting. What has been open-sourced is the
endpoint half: the hardest to build, the least profitable, and the half that determines whether
anyone wants the other one._

## Hard numbers

- **917 stars, 95 forks.** Repository created 2026-07-24
- Go, no cgo, single binary across macOS / Linux / Windows on amd64 and arm64
- Record format is already at JSON Schema v0.2.0 — a version number means someone is taking
  backward compatibility seriously
- Team size and enterprise adoption: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Perplexity is a heavy agent user, so the pain is real — but this is a company project, not a founder's |
| Product insight | Nailed after-the-fact reconstruction; peers require you to install a probe first, this one works backward from leftovers |
| Execution quality | Single Go binary, no cgo, three platforms, versioned schema. Engineering discipline, not a demo |
| Timing | Half a step early. Companies are still getting agents to work, not yet holding them accountable — but that day is coming |

## The call

**This is the employee-management playbook ported to agents, and ported honestly.**

Monitoring, blocking, forensics — the same three pieces companies have used on staff for twenty
years, moved across without alteration, right down to copying the rollout order of "observe
first, never block on day one." Honest is a compliment here: the standard way a security tool
dies is shipping enforcement in v1, blocking one legitimate action, and never being switched on
by that organization again.

**The transferable rule: the correct rollout order for any high-risk automation is watch before
you touch.** Run in observe mode long enough to gather real data, prove your false-positive rate
with that data, and only then talk about intervening. Doing it the other way — enforcement first,
tuning after — gives you exactly one chance, and spends it.

**The cost is that it currently offers almost no protection.** Every shipped rule is
monitor-only, so installing it does not make you safer; it makes you able to explain afterward
what happened. That is valuable for compliance and not very valuable for security, and most of
the people writing checks today are in the second category.

**The bigger question**: the endpoint layer sees actions, not intent. An agent reads three
hundred files and writes one report; every individual step is compliant. Is the sum of them
exfiltration? That judgment cannot be made on the endpoint. numbat is betting on "record every
action first," but the real disagreement is whether the security boundary for agents belongs at
the endpoint, at the model, or at the authorization layer.

## What to watch next

① Whether the number of agents in the coverage matrix is still growing in three months — falling
behind new agents makes it useless
② Whether any company says publicly that it runs this — the hard part for a security tool is not
building it, it is being trusted
③ Whether enforce mode's default flips from off to on — that would mean they believe the
false-positive rate is finally low enough

## What you can take from it

**Product logic**: when a multi-agent video workflow goes into real production, copy this
rollout order — ship an observe-only pass first, collect two weeks of real data to find where it
actually breaks, and only then decide which step deserves a human checkpoint. Guessing where the
checkpoint belongs puts it in the wrong place eight times out of ten.

**Positioning language**: none. This is engineering documentation; there is nothing to steal.

**Pricing structure**: none. Not disclosed.

## Verdict

**Worth watching.** The direction holds and the engineering is solid, but today it delivers
forensic value rather than protective value, and the buyers have not shown up in volume yet.
Write it down and come back in three months against the three checks above.
