---
slug: frankensonos
name: frankensonos
builder: Dicklesworthstone
category: AI + 生活
summary_zh: 家里已有 Sonos 音箱的人，在本地局域网里打开这个 Rust 控制器，让它接管音箱的发现与播放控制；它通过 SSDP/UPnP-SOAP/GENA 兼容 S1 与 S2 设备，并暴露
  CLI、HTTP API 和 MCP 服务，使 AI 代理可以按指令选曲、播放或跨网段（Tailscale）操作音箱，最终交付的是音箱实际播放状态的变化，具体曲库与场景流程仍待核验。
inspiration: 趋势：智能家居的控制权正从厂商 App 转向本地可编程接口，AI 代理开始被当作家庭设备的操作者而非聊天窗口。切入：从已有 Sonos 硬件、又嫌官方 App 与语音助手不听话的家庭用户或小型商用空间（咖啡馆、工作室）入手，卖点是本地可控与可被代理调用；可考虑按设备数或按场景配置收费，但公开材料未披露任何定价。
summary_en: For people who already own Sonos speakers, this Rust controller runs on the local LAN and
  takes over device discovery and playback control; it speaks SSDP/UPnP-SOAP/GENA across S1 and S2 hardware
  and exposes a CLI, HTTP API and MCP server so AI agents can select tracks, play, or operate speakers
  even off-LAN via Tailscale. The delivered result is a change in actual speaker playback state; the specific
  library and scenario flows still need verification.
inspiration_en: 'Trend: control of smart-home devices is shifting from vendor apps to local programmable
  interfaces, with AI agents treated as operators of household hardware rather than chat windows. Entry
  point: start with households or small commercial spaces (cafes, studios) that already own Sonos gear
  but find the official app and voice assistants unreliable, selling local control plus agent callability;
  per-device or per-scenario pricing is conceivable but no pricing is disclosed in public materials.'
priority_review: false
project_type: open_source
industries:
- 智能家居
- 消费电子
industries_en:
- Smart home
- Consumer electronics
jobs:
- 家庭音响控制
- 智能家居自动化
jobs_en:
- Home audio control
- Smart home automation
regions: []
regions_en: []
open_source: true
url: https://github.com/Dicklesworthstone/frankensonos
canonical_url: https://github.com/Dicklesworthstone/frankensonos
summary: Memory-safe Rust controller for your own Sonos speakers on your own LAN — reliable SSDP/UPnP-SOAP/GENA
  interoperability (S1 + S2), a Spotify-library classical DJ, and a CLI + HTTP API + MCP server so AI
  agents can run the house, including off-LAN over Tailscale.
first_seen: '2026-10-06T23:30:08Z'
last_seen: '2026-10-09T02:10:18Z'
status: watching
sources:
- github
sightings:
- source: github
  url: https://github.com/Dicklesworthstone/frankensonos
  seen_at: '2026-10-09T02:10:18Z'
  metrics:
    stars: 69
    forks: 4
    open_issues: 1
  kind: product
---

# frankensonos

Memory-safe Rust controller for your own Sonos speakers on your own LAN — reliable SSDP/UPnP-SOAP/GENA interoperability (S1 + S2), a Spotify-library classical DJ, and a CLI + HTTP API + MCP server so AI agents can run the house, including off-LAN over Tailscale.

## 笔记


