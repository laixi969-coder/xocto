---
slug: agent-skills-collection
name: agent-skills-collection
verdict: Unproven
analyzed_at: 2026-08-14
---

## What it is in one line

A GitHub repo that presents itself as a "curated collection of modular agent skills," but whose
installation path is: download a password-protected archive, temporarily disable Windows Defender,
and run an .exe installer as Administrator. Those two facts appearing together are the most
important information in this entire review.

## Who built it

The author's GitHub handle is `oliverb-io1902e8` — a random-suffix name consistent with a
disposable account. The repo was created 2026-08-06, has 14 commits, and an MIT license. The README
claims 8 skills: Web Research, Data Analysis, API Integration, Memory Manager, File Operations,
Email Automation, Social Media, and Database Query.

_Read: the author's identity cannot be verified. The README's installation instructions contradict
its claimed identity as an open-source Python library, and the contradiction itself is the signal._

## What it actually does

What the README claims it can do:
- 8 skill modules covering web research, data analysis, API access, memory management, file
  operations, email, social media, and databases
- A Python interface example (`from agent_skills import WebResearch`), claiming compatibility with
  Claude Code, Cursor, and other CLI agents
- 5 skills marked Stable, 3 marked Beta

What it actually asks you to do:
- Download an archive from Releases and extract it with the password `cv4PE+pSgUjd`
- Temporarily disable Windows Defender (self-described as a "false positive — the installer
  registers system components")
- Run `AgentSkillInstaller.exe` as Administrator

## What old behavior it replaces

**It cannot be determined what old behavior it replaces, because there is no evidence it actually
runs.** What is certain is the inverse: a legitimate open-source Python skill library delivers via
git clone or pip install — source readable and auditable. Instead, this repo asks you to download a
password-protected binary installer, turn off the antivirus, and run it with administrator rights.
Those two conditions never coexist in a legitimate open-source project, and the installation path
itself replaces the user's basic caution.

(This is the only product this batch where I cannot write "what it replaces" — because the
installation path is itself the warning.)

## Business model

**Not disclosed.** MIT license, no paid offering, no commercial trace of any kind.

_Read: there is no business model to discuss — its "what it is" has not even been independently
verified._

## Hard numbers

- **209 stars / 4 forks**, 14 commits, created 2026-08-06
- 8 claimed skills, of which 5 are marked Stable and 3 Beta
- The only auditable deliverables are roughly ten lines of Python in the README and a
  requirements.txt; there is no readable implementation
- Author identity, team, and usage data: not disclosed

## Four-way read

| Dimension | Call |
|-----------|------|
| Founder-product fit | Not assessable — the author's identity cannot be verified |
| Product insight | Not assessable — every skill exists only inside the README's description |
| Execution quality | Serious red flags: password-protected archive + disabling Windows Defender + running an exe as administrator is the classic malware delivery combination |
| Timing | Not applicable — there is no point discussing timing before the safety question is cleared |

## The call

**This is not a "wait and see" repository; it is a "assume it is malware until proven harmless"
repository.** The chain of evidence:

① It claims to be a Python open-source library yet delivers via a Windows exe installer and asks
you to disable Windows Defender
② A password-protected archive evades almost all static scanning
③ The handle carries a random suffix (`oliverb-io1902e8`), consistent with a throwaway account
④ The asymmetry of 209 stars against 4 forks does not match a repo with virtually no record of real
use

If it were genuinely a false positive, the author could clear it up in one sentence — publish the
full source, remove the exe installer, and switch to git-clone delivery. Until that happens, running
this exe means granting administrator privileges to software of unknown origin.

## What to watch next

① Whether the .exe in Releases is removed or matched by a public source tree
② Whether the README drops the "disable Windows Defender" instruction in favor of an auditable
install path
③ Whether stars keep rising in three months — inflated repos typically stall once momentum cools

## What you can take from it

**What is transferable lives in the negative of this repo**: if you ship an open-source tool, the
install path must be auditable — git clone or a package manager, visible source, no demand to
disable antivirus, no password-protected archives. When any of those appears, the user's first
reaction should be "run," not "trust."

**Positioning language**: none.

**Pricing structure**: none.

## Verdict

**Unproven — and the direction of observation is not "will it succeed" but "is it malware."** Treat
it as untrusted until clarified.
