---
slug: huggingface-transformers-patch-release-v5241
name: 'huggingface/transformers: Patch release v5.24.1'
builder: huggingface
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
inspiration_en: ''
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/huggingface/transformers/releases/tag/v5.24.1
canonical_url: https://github.com/huggingface/transformers/releases/tag/v5.24.1
summary: "# Patch release v5.24.1\r\n\r\nA patch to fix a bunch of stuff for vLLM, a few distributed issues,\
  \ and some model fixes (llama4, dory); see the full list\r\n\r\n### vLLM related\r\n- Fix backward compatibility\
  \ of the cache rename for remote code (#51085) by @hmellor\r\n- Restore modeling_attn_mask_utils for\
  \ remote code (one-off to unblock vLLM) (#51124) by @hmellor \r\n- Expose past_key_values in MBartDecoderLayer.forward\
  \ signature for remote code (#51177) by @hmellor \r\n- [OmniASR] Support a padding_mask kept on the\
  \ CPU in the audio encoder (#51100) by @El-euchidali\r\n\r\n### Model fixes\r\n- Fix Llama4 forward\
  \ crash on missing image_outputs (#51144) by @kylesayrs\r\n- Fix dory static cache (#50993) by @ArthurZucker\
  \ \r\n\r\n### Distributed\r\n- Allow expert parallelism alone with tp_plan={} (#50996) by @3outeille\
  \ \r\n- Fix strided checkpoint reads on PyTorch 2.9 (#51042) by @satsuki2486441738\r\n\r\n**Full Changelog**:\
  \ https://github.com/huggingface/transformers/compare/v5.24.0...v5.24.1"
first_seen: '2026-11-25T04:54:21Z'
last_seen: '2026-11-25T04:54:21Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/huggingface/transformers/releases/tag/v5.24.1
  seen_at: '2026-11-25T04:54:21Z'
  metrics:
    reactions: 0
  kind: news
---

# huggingface/transformers: Patch release v5.24.1

# Patch release v5.24.1

A patch to fix a bunch of stuff for vLLM, a few distributed issues, and some model fixes (llama4, dory); see the full list

### vLLM related
- Fix backward compatibility of the cache rename for remote code (#51085) by @hmellor
- Restore modeling_attn_mask_utils for remote code (one-off to unblock vLLM) (#51124) by @hmellor 
- Expose past_key_values in MBartDecoderLayer.forward signature for remote code (#51177) by @hmellor 
- [OmniASR] Support a padding_mask kept on the CPU in the audio encoder (#51100) by @El-euchidali

### Model fixes
- Fix Llama4 forward crash on missing image_outputs (#51144) by @kylesayrs
- Fix dory static cache (#50993) by @ArthurZucker 

### Distributed
- Allow expert parallelism alone with tp_plan={} (#50996) by @3outeille 
- Fix strided checkpoint reads on PyTorch 2.9 (#51042) by @satsuki2486441738

**Full Changelog**: https://github.com/huggingface/transformers/compare/v5.24.0...v5.24.1

## 笔记


