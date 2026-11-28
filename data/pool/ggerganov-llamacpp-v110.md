---
slug: ggerganov-llamacpp-v110
name: 'ggerganov/llama.cpp: v1.1.0'
builder: ggerganov
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
url: https://github.com/ggml-org/llama.cpp/releases/tag/v1.1.0
canonical_url: https://github.com/ggml-org/llama.cpp/releases/tag/v1.1.0
summary: "## Overview\r\n\r\nllama.cpp v1.1.0 adds the Inkling 2 family (base, Mini and DSpark), Domyn\
  \ Edge 4B, Zaya1 8B, RAON-1-mini and Hy4 flash, splits DFlash speculative decoding into separate draft\
  \ methods, and deprecates the old `llama_batch` API in favour of `llama_batch_ext`. It brings a large\
  \ set of TTS and audio models (Kokoro, Zonos3-Mini, tiny-voca, VoxCPM2, MiniMax-Music3, YuE2, Fish S2,\
  \ Higgs v3/VibeVoice-ASR and Kyutai Hibiki), token-aware chat parsing, named tool choice, automatic\
  \ per-tensor quantization targeting a bpw or size budget, a slot-scheduling refactor in `llama-server`,\
  \ a redesigned Llama Chat web UI with voice messages and agent traces, and updates `ggml` to v1.1.1.\r\
  \n\r\n### API changes\r\n\r\n- llama.h: deprecate the old `llama_batch` API in favour of `llama_batch_ext`\
  \ and `llama_process` ([#32306](https://github.com/ggml-org/llama.cpp/pull/32306), [#32356](https://github.com/ggml-org/llama.cpp/pull/32356))\r\
  \n- llama.h: add `llama_dflash_variant` and `llama_model_dflash_variant()` for the four DFlash draft\
  \ heads ([#32016](https://github.com/ggml-org/llama.cpp/pull/32016))\r\n- llama.h: add `llama_model_meta_arr_n()`\
  \ and `llama_model_meta_arr_str()` to read GGUF string arrays ([#32397](https://github.com/ggml-org/llama.cpp/pull/32397))\r\
  \n- llama.h: add `target_bpw`, `target_size`, `state_file` and abort callback to `llama_model_quantize_params`\
  \ ([#15550](https://github.com/ggml-org/llama.cpp/pull/15550))\r\n- mtmd.h: add audio types for Zonos3,\
  \ YuE2, MiniMax-Music3, Fish S2, Moshi, Kokoro, tiny-voca, VoxCPM2 ([#32020](https://github.com/ggml-org/llama.cpp/pull/32020),\
  \ [#32330](https://github.com/ggml-org/llama.cpp/pull/32330), [#32369](https://github.com/ggml-org/llama.cpp/pull/32369),\
  \ [#32413](https://github.com/ggml-org/llama.cpp/pull/32413), [#32427](https://github.com/ggml-org/llama.cpp/pull/32427),\
  \ [#32435](https://github.com/ggml-org/llama.cpp/pull/32435), [#32443](https://github.com/ggml-org/llama.cpp/pull/32443),\
  \ [#32491](https://github.com/ggml-org/llama.cpp/pull/32491))\r\n- mtmd.h: add `n_channels`, `mtmd_gen_audio_g2p()`\
  \ and `mtmd_gen_state_get_ref_codes()` ([#32413](https://github.com/ggml-org/llama.cpp/pull/32413),\
  \ [#32586](https://github.com/ggml-org/llama.cpp/pull/32586))\r\n- server: accept OpenAI named `tool_choice`\
  \ and add `GET /models/sse` in single-model mode ([#31564](https://github.com/ggml-org/llama.cpp/pull/31564),\
  \ [#32398](https://github.com/ggml-org/llama.cpp/pull/32398))\r\n- server: add `--ui-agent` and `--ui-mcp-proxy-allow-private-urls`\
  \ ([#33004](https://github.com/ggml-org/llama.cpp/pull/33004), [#32633](https://github.com/ggml-org/llama.cpp/pull/32633))\r\
  \n\r\n### New models\r\n\r\n- Inkling 2 (text + vision), Inkling 2 DSpark and Inkling 2 Mini ([#32217](https://github.com/ggml-org/llama.cpp/pull/32217),\
  \ [#32218](https://github.com/ggml-org/llama.cpp/pull/32218), [#32694](https://github.com/ggml-org/llama.cpp/pull/32694))\r\
  \n- Domyn Edge 4B: interleaved SWA with RoPE only on SWA layers and Q/K norm ([#32559](https://github.com/ggml-org/llama.cpp/pull/32559))\r\
  \n- Zaya1 8B ([#32071](https://github.com/ggml-org/llama.cpp/pull/32071))\r\n- MiniMax-M3.1 ([#32301](https://github.com/ggml-org/llama.cpp/pull/32301))\r\
  \n- RAON-1-mini-preview: 30B-A4B MoE ([#32176](https://github.com/ggml-org/llama.cpp/pull/32176))\r\n\
  - Hy4 flash: 220B (12B active) text and vision on the DSA iSWA cache ([#32960](https://github.com/ggml-org/llama.cpp/pull/32960))\r\
  \n- DFlash2 for Recursive Ripple-65B-Preview ([#31904](https://github.com/ggml-org/llama.cpp/pull/31904))\r\
  \n- TTS: Kokoro, Zonos3-Mini and tiny-voca ([#32413](https://github.com/ggml-org/llama.cpp/pull/32413),\
  \ [#32020](https://github.com/ggml-org/llama.cpp/pull/32020), [#32427](https://github.com/ggml-org/llama.cpp/pull/32427))\r\
  \n- Kyutai Hibiki / Moshi realtime full-duplex voice in/out ([#32491](https://github.com/ggml-org/llama.cpp/pull/32491))\r\
  \n\r\n### Core changes\r\n\r\n- split DFlash speculative decoding into `draft-dflash`, `draft-dflash2`,\
  \ `draft-dspark` and `draft-lilicorr` ([#32016](https://github.com/ggml-org/llama.cpp/pull/32016))\r\
  \n- use GDN replay instead of rollback ([#31669](https://github.com/ggml-org/llama.cpp/pull/31669))\r\
  \n- add `--target-bpw`/`--target-size` per-tensor quant selection with a resumable state file ([#15550](https://github.com/ggml-org/llama.cpp/pull/15550))\r\
  \n- match special tokens in chat parsing instead of text (token-aware parsing) ([#29307](https://github.com/ggml-org/llama.cpp/pull/29307))\r\
  \n- speed up BPE tokenization and the PLaMo-2/3 tokenizer table build ([#32859](https://github.com/ggml-org/llama.cpp/pull/32859),\
  \ [#32249](https://github.com/ggml-org/llama.cpp/pull/32249))\r\n- move the MoE cache out of `llama-graph`\
  \ and reserve graph nodes for it ([#32157](https://github.com/ggml-org/llama.cpp/pull/32157), [#32636](https://github.com/ggml-org/llama.cpp/pull/32636))\r\
  \n- move the graph node budget and indexer key rotation choice into the model classes ([#32648](https://github.com/ggml-org/llama.cpp/pull/32648),\
  \ [#32653](https://github.com/ggml-org/llama.cpp/pull/32653))\r\n- apply `.scale` tensors automatically\
  \ and load `ffn_gate_up_exps` scales ([#32669](https://github.com/ggml-org/llama.cpp/pull/32669), [#32657](https://github.com/ggml-org/llama.cpp/pull/32657))\r\
  \n- fix sticky NaN in recurrent state, k-pool layout on sequence edits and QSA k-pool scoring ([#31913](https://github.com/ggml-org/llama.cpp/pull/31913),\
  \ [#32137](https://github.com/ggml-org/llama.cpp/pull/32137), [#32519](https://github.com/ggml-org/llama.cpp/pull/32519))\r\
  \n- fall back to buffered I/O on EIO and allocate the staging buffer from the CPU buffer type ([#32545](https://github.com/ggml-org/llama.cpp/pull/32545),\
  \ [#31438](https://github.com/ggml-org/llama.cpp/pull/31438))\r\n- avoid an O(n_cells) scan per sequence\
  \ removal in the KV cells ([#32380](https://github.com/ggml-org/llama.cpp/pull/32380))\r\n- honor `metaspace_prepend_scheme`\
  \ for SPM and always for BPE, and load YaRN hparams in the model base ([#31986](https://github.com/ggml-org/llama.cpp/pull/31986),\
  \ [#33038](https://github.com/ggml-org/llama.cpp/pull/33038), [#33032](https://github.com/ggml-org/llama.cpp/pull/33032))\r\
  \n- fix per-sequence state restore with ON_DEVICE KV caches ([#30318](https://github.com/ggml-org/llama.cpp/pull/30318))\r\
  \n- use the indexed bias FATTN path in Inkling 2 and map Inkling-2 LoRA tensor names ([#33053](https://github.com/ggml-org/llama.cpp/pull/33053),\
  \ [#33055](https://github.com/ggml-org/llama.cpp/pull/33055))\r\n- add `LLAMA_MOE_RANDOM_ROUTING=1`\
  \ for benchmark-only random expert selection ([#29539](https://github.com/ggml-org/llama.cpp/pull/29539))\r\
  \n- optimize grammar matching with left factoring and fix an integer overflow ([#29557](https://github.com/ggml-org/llama.cpp/pull/29557),\
  \ [#32551](https://github.com/ggml-org/llama.cpp/pull/32551))\r\n- allow up to `llama_max_devices()`\
  \ configs for `--tensor-split` and `--fit-target` ([#31435](https://github.com/ggml-org/llama.cpp/pull/31435))\r\
  \n- jinja: scope-chain key lookup, `sort_keys=true`, 4 missing features and lower rendering overhead\
  \ ([#32396](https://github.com/ggml-org/llama.cpp/pull/32396), [#32366](https://github.com/ggml-org/llama.cpp/pull/32366),\
  \ [#32352](https://github.com/ggml-org/llama.cpp/pull/32352), [#32023](https://github.com/ggml-org/llama.cpp/pull/32023))\r\
  \n- chat: inkling parser, undeclared LFM2 tool calls, tool calls in reasoning, lazy grammar ([#32381](https://github.com/ggml-org/llama.cpp/pull/32381),\
  \ [#32164](https://github.com/ggml-org/llama.cpp/pull/32164), [#32271](https://github.com/ggml-org/llama.cpp/pull/32271),\
  \ [#32232](https://github.com/ggml-org/llama.cpp/pull/32232), [#32497](https://github.com/ggml-org/llama.cpp/pull/32497))\r\
  \n- chat: implement named `tool_choice` and pass `reasoning_effort=none` when supported ([#31564](https://github.com/ggml-org/llama.cpp/pull/31564),\
  \ [#32763](https://github.com/ggml-org/llama.cpp/pull/32763))\r\n- json-schema: accept boolean `\"value\"\
  : true` and reject out-of-range grammar triggers ([#32908](https://github.com/ggml-org/llama.cpp/pull/32908),\
  \ [#31478](https://github.com/ggml-org/llama.cpp/pull/31478))\r\n\r\n### Multi-modality changes\r\n\r\
  \n- add support for VoxCPM2, MiniMax-Music3, YuE2-3B, Fish Audio S2 and Higgs Audio v3/VibeVoice-ASR\
  \ ([#32443](https://github.com/ggml-org/llama.cpp/pull/32443), [#32435](https://github.com/ggml-org/llama.cpp/pull/32435),\
  \ [#32369](https://github.com/ggml-org/llama.cpp/pull/32369), [#32330](https://github.com/ggml-org/llama.cpp/pull/32330),\
  \ [#32329](https://github.com/ggml-org/llama.cpp/pull/32329))\r\n- drama3 voice cloning and Qwen3-TTS\
  \ ICL/reference mode ([#32586](https://github.com/ggml-org/llama.cpp/pull/32586), [#32438](https://github.com/ggml-org/llama.cpp/pull/32438))\r\
  \n- speed up the shared audio FFT and avoid padding-only Whisper audio chunks ([#32815](https://github.com/ggml-org/llama.cpp/pull/32815),\
  \ [#30403](https://github.com/ggml-org/llama.cpp/pull/30403))\r\n- allow a custom video decoder and\
  \ fix video pixel aspect ratio and rotation ([#32188](https://github.com/ggml-org/llama.cpp/pull/32188),\
  \ [#32267](https://github.com/ggml-org/llama.cpp/pull/32267))\r\n- merge Parakeet rel-pos views to avoid\
  \ OOB, fix YuE2 projector loading and the qwen3a audio tail ([#32722](https://github.com/ggml-org/llama.cpp/pull/32722),\
  \ [#32606](https://github.com/ggml-org/llama.cpp/pull/32606), [#32697](https://github.com/ggml-org/llama.cpp/pull/32697))\r\
  \n- add `--tts-lang`, `--tts-voice` and `--tts-speaker-text` for per-model TTS voices ([#32330](https://github.com/ggml-org/llama.cpp/pull/32330),\
  \ [#32586](https://github.com/ggml-org/llama.cpp/pull/32586))\r\n\r\n### Server changes\r\n\r\n- refactor\
  \ slot scheduling into `server_slot_sched` with per-prompt running hashes ([#32154](https://github.com/ggml-org/llama.cpp/pull/32154))\r\
  \n- retry cached prompt restoration after clearing idle slots and preserve entries until restores succeed\
  \ ([#30997](https://github.com/ggml-org/llama.cpp/pull/30997), [#32828](https://github.com/ggml-org/llama.cpp/pull/32828),\
  \ [#28992](https://github.com/ggml-org/llama.cpp/pull/28992))\r\n- clear slot cache when the global\
  \ LoRA config changes ([#30367](https://github.com/ggml-org/llama.cpp/pull/30367))\r\n- reuse HTTP connections\
  \ after streamed responses ([#30492](https://github.com/ggml-org/llama.cpp/pull/30492))\r\n- include\
  \ MCP image and audio data in tool results ([#32064](https://github.com/ggml-org/llama.cpp/pull/32064))\r\
  \n- add offset pagination to `grep_search` and ask `exec_shell_command` for a short description ([#32792](https://github.com/ggml-org/llama.cpp/pull/32792),\
  \ [#32894](https://github.com/ggml-org/llama.cpp/pull/32894))\r\n- return 400 for rejected `reasoning_effort`\
  \ levels and grammar with `ignore_eos`, fix `output_config.effort` ([#32332](https://github.com/ggml-org/llama.cpp/pull/32332),\
  \ [#32377](https://github.com/ggml-org/llama.cpp/pull/32377), [#32321](https://github.com/ggml-org/llama.cpp/pull/32321))\r\
  \n- ignore empty stop strings ([#32093](https://github.com/ggml-org/llama.cpp/pull/32093))\r\n- fit\
  \ non-causal batches in one ubatch and enable packing for d1-2B/d1-Omni-2B ([#32713](https://github.com/ggml-org/llama.cpp/pull/32713),\
  \ [#32553](https://github.com/ggml-org/llama.cpp/pull/32553))\r\n- skip MCP discovery for router children\
  \ ([#32359](https://github.com/ggml-org/llama.cpp/pull/32359))\r\n- fix sleep state and transcription\
  \ prompt for `/v1/realtime` ([#32567](https://github.com/ggml-org/llama.cpp/pull/32567), [#32507](https://github.com/ggml-org/llama.cpp/pull/32507))\r\
  \n- handle `CTRL_BREAK_EVENT` on Windows for clean shutdown ([#32080](https://github.com/ggml-org/llama.cpp/pull/32080))\r\
  \n- fix LoRA and recurrent slot scheduling ([#32434](https://github.com/ggml-org/llama.cpp/pull/32434))\r\
  \n\r\n### UI changes\r\n\r\n- move the web UI to `ui/apps/chat` as Llama Chat, with a Llama UI design\
  \ system and Storybook ([#32032](https://github.com/ggml-org/llama.cpp/pull/32032), [#32468](https://github.com/ggml-org/llama.cpp/pull/32468),\
  \ [#32485](https://github.com/ggml-org/llama.cpp/pull/32485))\r\n- move to SvelteKit 3 and cut first-load\
  \ JavaScript by 63% with on-demand diagrams, math and PDFs ([#32463](https://github.com/ggml-org/llama.cpp/pull/32463),\
  \ [#32555](https://github.com/ggml-org/llama.cpp/pull/32555))\r\n- add voice messages and dictation\
  \ with live waveforms and transcripts ([#32531](https://github.com/ggml-org/llama.cpp/pull/32531))\r\
  \n- show agentic replies as a grouped Agent Trace, with the loop in `@ggml-org/llama-harness` ([#32879](https://github.com/ggml-org/llama.cpp/pull/32879),\
  \ [#32927](https://github.com/ggml-org/llama.cpp/pull/32927))\r\n- run Llama Chat apart from llama-server,\
  \ via `npx @ggml-org/llama-chat` or a config URL ([#32524](https://github.com/ggml-org/llama.cpp/pull/32524),\
  \ [#32945](https://github.com/ggml-org/llama.cpp/pull/32945))\r\n- make Llama Chat a plain chat unless\
  \ the server offers agent features ([#32949](https://github.com/ggml-org/llama.cpp/pull/32949))\r\n\
  - add `--ui-agent` for agent mode without server tools or the MCP proxy ([#33004](https://github.com/ggml-org/llama.cpp/pull/33004))\r\
  \n- set the reasoning effort from the model picker and add a cancel button for model loading ([#32632](https://github.com/ggml-org/llama.cpp/pull/32632),\
  \ [#32225](https://github.com/ggml-org/llama.cpp/pull/32225))\r\n- import conversations or settings\
  \ by dropping them anywhere in the app ([#32958](https://github.com/ggml-org/llama.cpp/pull/32958))\r\
  \n- search message content and Discover models from the search dialog ([#32670](https://github.com/ggml-org/llama.cpp/pull/32670))\r\
  \n- open the context gauge as a popover and add a full-screen diagram preview ([#32685](https://github.com/ggml-org/llama.cpp/pull/32685),\
  \ [#32591](https://github.com/ggml-org/llama.cpp/pull/32591))\r\n- hide Models and MCP behind settings,\
  \ turn conversation tabs and the live markdown preview off by default ([#32527](https://github.com/ggml-org/llama.cpp/pull/32527),\
  \ [#32402](https://github.com/ggml-org/llama.cpp/pull/32402), [#32469](https://github.com/ggml-org/llama.cpp/pull/32469))\r\
  \n- slim the design tokens and set all text through type roles ([#32615](https://github.com/ggml-org/llama.cpp/pull/32615))\r\
  \n- open Settings, the + menu and the model picker as sheets on phones, and manage MCP from Settings\
  \ ([#33036](https://github.com/ggml-org/llama.cpp/pull/33036))\r\n- stop the streaming reply with Escape\
  \ and make `npx llama-chat` default to `:9931` ([#33051](https://github.com/ggml-org/llama.cpp/pull/33051),\
  \ [#33095](https://github.com/ggml-org/llama.cpp/pull/33095))\r\n\r\n### ggml changes\r\n\r\n- [v1.1.0](https://github.com/ggml-org/ggml/releases/tag/v1.1.0):\
  \ ggml v1.1.0 extends the graph API for new model families, strengthens scheduler and backend behavior,\
  \ and brings broad performance work across all backends. The API gains gated-delta-net replay, flash-attention\
  \ indexed bias, ordered asynchronous host input copies, and scheduler scratch reservation, plus new\
  \ SLEEP and SIGMOID_BACK operators. Core adds BF16 coverage for more operations, faster quantization\
  \ and math helpers, and new CPU quant kernels, while backends add stream-k matmul, chunked command buffers,\
  \ NVFP4, CONV_2D acceleration, wider FP8/BF16 support, and many tuning and correctness fixes.\r\n- [v1.1.1](https://github.com/ggml-org/ggml/releases/tag/v1.1.1):\
  \ ggml v1.1.1 lands Hexagon 2.0 with INT-HMX W8A8 matmul, automatic F32 to F16 lowering and generic\
  \ DMA pipelines, and brings a CUDA FlashAttention data-loading refactor, a SYCL gated-delta-net ESIMD\
  \ kernel with fused recurrent convolutions, small-K Metal mat-vec tuning, and a WebGPU log1p for softplus.\
  \ It also adds the TANH backward pass, OpenVINO decode and op-test fixes, and 16-head lightning-indexer\
  \ support on CUDA.\r\n\r\n## Assets\r\n\r\n**Nightly build:** [b12774](https://github.com/ggml-org/llama.cpp/releases/tag/b12774)\r\
  \n\r\n## More info\r\n\r\n- [Releases and versioning of `ggml-org` projects](https://github.com/ggml-org/ggml/discussions/1579)\r\
  \n\r\n## Changelog since [v1.0.0](https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0)\r\n\r\n\
  171527522 sync : ggml\r\n2a59da5bf ggml : bump version to 1.1.1 (ggml/1703)\r\n07ba74bab sycl: update\
  \ linux refer doc (#32583)\r\n267dda818 sycl: Remove check for host waits in fattn-mkl from graph checks\
  \ (#31208)\r\ne0f884d40 ggml-hexagon 2.0 : support for int-hmx, automatic f32 -> f16 lowering, and generic\
  \ dma pipelines (#32582)\r\nf8b7ed525 cuda : fix int overflow of the MMF matrix offsets (#33044)\r\n\
  55b2238be ggml : add TANH backward pass (#32136)\r\na8ad690ca sycl: add gated delta net ESIMD kernel\
  \ (#31762)\r\naee03fbe8 sycl: fuse recurrent convolution windows (#31355)\r\n9c003a97a ui: open settings,\
  \ the + menu and the model picker as sheets on phones, and manage MCP from settings (#33036)\r\n7135e2fd6\
  \ metal : spread the short mat-vec lanes over src1 rows (#33034)\r\n5917b39ff convert : map the Inkling-2\
  \ LoRA tensor names (#33055)\r\n8d35ba4f7 metal : revert \"metal: increase default command buffers on\
  \ iPhone (#31815)\" (#33050)\r\nacb269e51 nix : fix build on darwin (#32955)\r\nd9dae0344 opencl: Adreno\
  \ E17 compiler quirks off by default (#33013)\r\neb5657509 ui: stop the streaming reply with Escape\
  \ (#33051)\r\n5a09582d8 model : add RAON-1-mini-preview support (#32176)\r\n2d5b3ddde model: use the\
  \ indexed bias in the Inkling 2 graph (#33053)\r\n94a1e4b72 CUDA: refactor & deduplicate FA data loading\
  \ (#32901)\r\nc94333133 model : add hy_v4_flash on the DSA iSWA cache (#32960)\r\n244640b7f ggml-openvino:\
  \ fix CI op tests and improve KV cache decode (#33002)\r\n679d8677b llama : fix seq state restore with\
  \ ON_DEVICE (#30318)\r\nbeb9d4933 llama.cpp : bump version to 1.1.0 (#33043)\r\n532d67426 vocab : implement\
  \ Metaspace prepend_scheme always for BPE (#33038)\r\n5e4fda8ed ui: fix for a chat form update loop\
  \ with large fonts and long model names (otherwise web interface gets Error 500) (#33037)\r\na28feb458\
  \ sync : ggml\r\n312504361 ggml : bump version to 1.1.0 (ggml/1699)\r\n98f870c22 llama : honor metaspace_prepend_scheme\
  \ for SPM (#31986)\r\n2e2f5a037 model : load YaRN hparams in llama_model_base::load_hparams (#33032)\r\
  \n41c7a1b49 ui: fix tool result media shown twice, uncapped and dropped after its run (#33010)\r\n77026f6e6\
  \ ui: open the warm microphone only once the pointer rests on its button (#33033)\r\nc8eda101c ui: add\
  \ file extensions to the Vite config's local imports (#33023)\r\n996de35a9 ci : revert disable musa.Dockerfile\
  \ from docker.yml (#33025)\r\nab16df399 webgpu : add log1p for softplus op (#33017)\r\n0cac1220e ui:\
  \ time each tool group by its own loop and show the task time in the reply stats (#33030)\r\n1ed4e77f4\
  \ ui: search home by default in the working-directory picker and pin tool call chevrons (#33028)\r\n\
  48ac73696 server : handle CTRL_BREAK_EVENT on Windows for clean shutdown (#32080)\r\n5220a2d40 quant\
  \ : avoid macro collision on windows (#33014)\r\n0fc7e1716 docs : fix stale CPU support in ops.md (#32796)\r\
  \n6d5f64872 ggml-cpu : accept the flash_attn_ext indexed bias (#33016)\r\n52f6e0247 metal : commit the\
  \ graph in chunks with one command buffer thread (#32947)\r\nde3069728 ui: import conversations or settings\
  \ by dropping them anywhere in the app (#32958)\r\n62d6c8cb3 ggml: allow input async copies (#30685)\r\
  \n5bd90fa0e common : implement named tool choice (#31564)\r\n522d6fdd4 deepseek41 : read quantized indexer\
  \ K in place when fused_idx is set (#32795)\r\n61d456a23 common : accept boolean \"value\": true JSON\
  \ schema (#32908)\r\nea7229481 ggml: allow reserving scratch memory in graph_optimize (#31898)\r\n36d818e16\
  \ ui: edit the system message in the chat form when it is hidden in conversations (#32967)\r\n81ff0cab0\
  \ sycl: F8 e4m3 initial support SET_ROWS, CPY, ADD, MUL_MAT, MUL_MAT_ID (#31871)\r\ncddaa915a SYCL :\
  \ ROLL op handles permuted source (#31799)\r\ne8906e6b0 ui: add --ui-agent for agent mode without server\
  \ tools or the MCP proxy (#33004)\r\nabca69200 model : inkling2 graph with fewer ops in mix() and control()\
  \ (#32948)\r\ne6443bd7e opencl: add clc coopmat moe kernel for q4_0/q4_1/q4_k/q5_0/q5_1/q5_k/q6_k/mxfp4\
  \ (#32971)\r\n79c69f4b0 tests : fix MSVC static build of test-batch-alloc and test-server-component\
  \ (#32870)\r\n33aeb17f8 feat: Inkling 2 DSpark support (#32218)\r\n22b99122e cuda : fix int overflow\
  \ of the MMVF matrix offsets (#32965)\r\ndfdfca22b docs : describe SpacemiT runtime environment variables\
  \ (#32452)\r\na1cee51c9 ggml : fix SpacemiT flash attention null mask, ALiBi and softcap (#32182)\r\n\
  bb692efaa cmake : include the llguidance header from the source tree (#32928)\r\ndbaf582af ci : move\
  \ some jobs to gb10 runners (#32968)\r\n0ce7f213b ui: run Llama Chat apart from llama-server, named\
  \ in config.json or npx --server (#32945)\r\n96eb41bc4 ui: fix prebuilt UI download in shallow clones\
  \ (#32952)\r\n23f0c0182 convert : fix qwen3-omni conversion (#32941)\r\nf20c5907c ggml-cpu: repack kernels\
  \ for targets without dotprod (ARMv8.0 64-bit) for Q4_0/Q8_0 (#32142)\r\n8bf2eae70 ui: expect the Llama\
  \ Chat name in the PWA manifest e2e test (#32959)\r\n5fddd0b99 ggml-cpu: add SVE-optimized q5_0 and\
  \ q5_1 dot-product kernels (#30867)\r\n66a3b01b0 server : include MCP image and audio data in tool results\
  \ (#32064)\r\nd3c257a49 context : prevent excessive CPU polling without OpenMP (#32378)\r\n3090e45a8\
  \ metal : reserve the top-k scratch only for short rows (#32942)\r\nba8521a44 ui: smooth chat form height\
  \ and working directory chip across routes (#32950)\r\n72cda4a22 vulkan: add chunked GDN replay support\
  \ (#32721)\r\n922cff91e cuda : fuse RMS_NORM + MUL + MROPE/IMROPE and tune block size (#32500)\r\n2e779d5e7\
  \ Webui nix fix (#32645)\r\n396ed2cce model : Inkling 2 Mini mix() weighted sum with the scores as src0\
  \ (#32855)\r\n97bbf98fd ui: make Llama Chat a plain chat unless llama-server offers agent features (#32949)\r\
  \n40fe9164f server : retry prompt cache restore after clearing idle slots (#30997)\r\n26f5048d5 fix\
  \ building in symlinked directories (#32903)\r\n9578bd3fe CUDA: ignore strides of size-1 dims in bin_bcast\
  \ (#32854)\r\ne683365a7 model : inkling2 clip with ggml_l2_norm (#32940)\r\n4c92c5bfb CUDA: reduce all\
  \ cooperative softmax partials when nsm > 256 (#32897)\r\n2a487782f vocab : speed up BPE tokenization\
  \ (#32859)\r\n6fb428332 CUDA: NVFP4 dequant, pack 8 blocks per CTA (#32875)\r\n6ac648d7a webgpu : Fix\
  \ indexing bug in softmax kernel (#32691)\r\n94165b288 webgpu : add POOL_1D support (#32254)\r\na8ed77891\
  \ hip: use MMQ over MMVQ for Q4_K,N8 and NVFP4,N7-8 on VEGA20 (#32805)\r\n6970118ef HIP: CDNA1 MMQ config\
  \ without stream-k (#32837)\r\nae6a7ad2c ui: move the agentic loop and trace phrasing into @ggml-org/llama-harness\
  \ (#32927)\r\n5fe490685 ci : disable test-llama-context on ubuntu-llvmpipe (#32932)\r\n82dd97047 server\
  \ : fix skipped prompt cache lookups (#28992)\r\na6ac41c75 ui: match tool call timer font size to its\
  \ title (#32922)\r\n3fccd98e9 ui: let the chat form's model selection decide the submit state (#32920)\r\
  \n4af4bb6d8 rpc : reuse one context for request tensors on the server (#32896)\r\nb12f22d2f ggml : use\
  \ a range-reduced log1p for softplus (#32655)\r\nd141011c2 vulkan: support state size 96 in ssm_scan\
  \ (#32162)\r\n12d47ba2f opencl: fix GDN QK offsets (#32747)\r\naf5c58347 opencl: add c8 q6_k coopk GEMM\
  \ for up to n=8 spec verify (#32909)\r\nc74c71a6f fix editor config in master (#32914)\r\n38b9cad71\
  \ quantize : make local const static for MSVC (#32902)\r\nd35dc4d9e GDN: use replay instead of rollback\
  \ (#31669)\r\nc212d25ad server : preserve a prompt-cache entry until restores succeed (#32828)\r\nfd24ee26a\
  \ opencl: fetch the Adreno binary kernel library at configure time for Windows on Snapdragon (#31759)\r\
  \n8355b8862 ui: remove the Matte theme and the Light surfaces setting (#32906)\r\n51831d47d metal :\
  \ add NVFP4 support (#32825)\r\nab789a246 metal : batch concat rows and copy them in vector chunks (#32824)\r\
  \n239242322 ggml: compact bias on the existing FLASH_ATTN_EXT (#32740)\r\n30ec35ae2 quantize: add option\
  \ to automatically choose optimal quant types to reach a file/bpw target size at lowest error (#15550)\r\
  \n87f816e87 metal : support BF16/F32 src1 for MUL_MAT and MUL_MAT_ID (#32677)\r\n1d3aad2fd server: ask\
  \ exec_shell_command for a short description of the command (#32894)\r\n325914def ui: show an agentic\
  \ reply as a grouped Agent Trace (#32879)\r\n1094646c1 ui: set code in messages at the size of the text\
  \ around it (#32892)\r\n27d0a1fc7 ui: unmount a closed collapsible's body after one transition (#32881)\r\
  \nb6d5ce4bc ui: drop tool calls cut off by Stop from the next request (#32738)\r\n1f3ea67fb metal: resolve\
  \ gpu timeout on iPhone for Bonsai (#31815)\r\na0677c341 ui: use a red edge on the send button's error\
  \ state (#32856)\r\n2359d27a3 ui: name the PWA from the build env and default it to Llama Chat (#32890)\r\
  \n51fc2f90e ggml-openvino: CI fixes, new model support, fixes and improvements. (#32861)\r\n03813c56e\
  \ rpc : typed request helpers and a single validation step on the server (#32651)\r\n46f4da217 ggml-cuda\
  \ : handle zero blocks in few-row MMQ quantization (#32566)\r\n4663f9ca8 ui: smooth height transition\
  \ for every collapsible (#32873)\r\n969d73331 cmake: treat kleidiai files as vendored (#32605)\r\na8f8294c4\
  \ tests : update Qwen3.6-27B snapshot (#32845)\r\n7d9b931df ggml : update cmake MATH_LIBRARY check (#32864)\r\
  \n212c547fe ui: add cancel button to cancel model loading (#32225)\r\nf5e6915c2 webgpu : add ROLL support\
  \ (#31887)\r\ndd53f70d0 chat : improve inkling parser/grammar (#32833)\r\n1f8baae28 opencl: add xielu\
  \ (#32791)\r\n44d50873b opencl: add q4_k coop-k c8 GEMM for spec verify (#32716)\r\n7778de0c3 tests\
  \ : compare only the guaranteed GDN snapshot slots (#32820)\r\nf4f6f2e7d ggml-backend : generic fallback\
  \ in ggml_backend_tensor_memset  (#32574)\r\n253671d88 chat: fix LFM2.5-VL template detection (#32843)\r\
  \n94f3af3d0 mtmd: speed up shared audio FFT (#32815)\r\nf505c30b9 mtmd: fix qwen3a audio tail (#32697)\r\
  \n5bacb7c86 llama : copy all experts of a host weight shared by several nodes (#32807)\r\nd2bceda3d\
  \ vocab: enable ignore_merges for inkling2 (#32799)\r\n56eea9e4b server : add offset pagination to grep_search\
  \ tool (#32792)\r\ne14a2d3a6 skill: Pay attention to tokenizer flags (#32819)\r\n1014775c8 chat : implement\
  \ token aware parsing (#29307)\r\n0b51bb2fe server: support /models/sse on single-model mode (#32398)\r\
  \n8d60873df ggml/gguf : avoid creating invalid enum values from untrusted file data (#32641)\r\nad50351f5\
  \ ggml : add SIGMOID backward pass (#32126)\r\n42f6a58fd chat : trigger lazy grammar on bare JSON tool\
  \ calls (#32497)\r\n9c10c94e1 ggml : fix nonzero clear on WebGPU and non-UMA devices (#32727)\r\n8cb0d98cc\
  \ HIP: fix double halving of NVFP4 scales on CDNA3 (#32790)\r\ne300919cc webgpu : update GDN supports_op\
  \ check (#32782)\r\n5d28d64bf ggml-webgpu : Update to a recent version of Dawn (#32779)\r\n1fb8a2696\
  \ opencl: add coopmat GEMM for Adreno 850 (Q4_0, Q5_0, Q8_0, Q4_K, Q5_K, Q6_K) (#32686)\r\n8a97fa98a\
  \ vulkan : support non-contiguous src in SCALE (#32735)\r\n225a5345b server : fit non-causal batches\
  \ in one ubatch (#32713)\r\nb05204927 vulkan : fix memset for unaligned ranges for non-UMA devices (#32725)\r\
  \ncbb1c1c50 model: fix no_realloc for clef and vllm-decision2 (#32754)\r\nafe77e18f chat : pass reasoning_effort\
  \ = none if supported (#32763)\r\ne6d624b9a mtmd : merge Parakeet rel-pos views to avoid OOB (#32722)\r\
  \n19bc41dbb model: apply .scale tensors automatically + fix correctness (#32669)\r\ne50c254a2 sycl:\
  \ bound CONV_TRANSPOSE_1D input iteration (#31109)\r\n660be5506 ggml : improvements to the memory access\
  \ pattern in `ggml_compute_forward_mul_mat_one_chunk` (#30846)\r\nc622f623f mtmd: support kyutai/hibiki\
  \ realtime full-duplex (#32491)\r\nc66103334 sycl: add IQ4_NL and IQ4_XS weight reorder (#31998)\r\n\
  44c20b1c0 sycl: column-blocked gated_delta_net kernel (#32456)\r\n80325823d ui: open the context gauge\
  \ panel on click as a popover (#32685)\r\na818a46f3 sycl: add fused ADD, RMS_NORM, MUL and vectorize\
  \ rms norm (#31753)\r\nb019be0c8 CUDA: abort on UB in fastdiv (#32698)\r\n362ac9297 vulkan: unroll FA\
  \ coopmat1 array due to a driver bug on AMD Windows (#32466)\r\nfb7090df5 vulkan: improve RDNA4 MMVQ\
  \ performance for Q3_K, Q5_K and IQ4_XS (#31804)\r\n690b87d88 model : inkling2_loop share the loop slots\
  \ after the scale pass (#32704)\r\n838d94243 model : additional shortcut checks for OOB in hrm_text\
  \ (#32720)\r\n3da11de1f ggml-zdnn: fix ztensor load race condition (#32279)\r\n93cb37ea7 ggml-cpu: fix\
  \ nc aligment in tinyBLAS_PPC_Q0 (#32659)\r\n1fdda89a4 ci: switch ppc64le runners to ubuntu 26.04 (#32679)\r\
  \ne412c6f46 llama : remove fused lightning indexer gating (#32650)\r\n40b7a546d ci: temporary disable\
  \ no realloc case for mtmd (#32708)\r\n46eb1742d llama-grammar: Fix integer overflow (#32551)\r\n6792507b7\
  \ llama : score only the k-pools of the ubatch sequences in QSA (#32519)\r\n418fe97b5 sycl: Improve\
  \ Grouped XMX GEMM by avoiding SLM staging (#31428)\r\n7476e4726 docs: openvino backend details, fix\
  \ SYCL docs (#30967)\r\n29b52d398 model : Inkling 2 Mini (#32694)\r\ne3c3f666a hip: add RDNA1 MMVQ parameter\
  \ table (1 warp per block for ncols=1) (#32389)\r\nb2e659ec2 ggml-openvino: update openvino CI runs\
  \ triggers (#32593)\r\n919794500 convert: qwen3-asr: put \"language ...\" output into thinking block\
  \ (#32571)\r\na83d68b56 metal : allow the norm chain in either operand of the fused MUL/ADD (#32300)\r\
  \ne46069c40 ui: fix the flaky reset check of the MermaidPreview Flowchart story (#32675)\r\n427a83673\
  \ ui: stage Llama Voice's sources for CMake and Docker UI builds (#32680)\r\n374d90a9f ci : disable\
  \ musa.Dockerfile from docker.yml (#32674)\r\n98709fd82 server: add more decision tests (#32578)\r\n\
  7716ec8cb ggml : major version bump reminders + deprecate ggml_ftype (#32647)\r\n34ff2e047 mtmd: drama3\
  \ voice cloning (#32586)\r\n6f5c9ad21 vulkan: add support for COL2IM_1D misalign bytes and split workgroups\
  \ (#32673)\r\n184862801 gemma4: Optimized prompt processing for multi-seq queries (#32342)\r\n79e81b0bd\
  \ ui: voice messages and dictation with live waveforms and transcripts (#32531)\r\n059cac284 ui: search\
  \ message content and Discover models from the search dialog (#32670)\r\ncf4153a9b ui: publish llama-ui\
  \ as an alias of @ggml-org/llama-ui (#32667)\r\n8e7862411 tts : forward -t to the mtmd context (#32664)\r\
  \ne626db7ca server-bench : fix TypeError in histogram generation (#32518)\r\nc6a25fc62 ui: load highlight.js\
  \ languages on demand (#32661)\r\n5f837145d server: add more audio tests (#32579)\r\n36cd3aff4 server:\
  \ add --ui-mcp-proxy-allow-private-urls (#32633)\r\n28de970cc ui : focus the chat form when typing with\
  \ nothing focused (#32570)\r\n4b69c79cc cuda : update GDN supports_op check (#32660)\r\na1f422260 model\
  \ : load ffn_gate_up_exps scales (#32657)\r\n4783b1145 llama : move the indexer key rotation choice\
  \ into the model classes (#32653)\r\n6abcbe5d3 remove ui-lib publish verification step (#32658)\r\n\
  b81aa847c ui: slim the design tokens and set all text through type roles (#32615)\r\n9d6f04fa9 ui: show\
  \ vision as glasses and audio as headphones (#32617)\r\n652d559ed llama : move the graph node budget\
  \ into the model classes (#32648)\r\n6aee50801 ui: set the reasoning effort from the model picker (#32632)\r\
  \n55b8d8d89 ui: full-screen diagram preview that zooms around what is on screen, inert diagrams (#32591)\r\
  \n4c4a0f0a4 llama : reserve graph nodes for the MoE cache (#32636)\r\n55d323507 model: add Domyn Edge\
  \ 4B Model (#32559)\r\nbed8ec2f8 llamafile(s390x): add QK data type support (#32600)\r\n52e8db655 kleidiai\
  \ : allow OHOS (HarmonyOS) AArch64 target (#32265)\r\nd7d1b632d webgpu : fix 2D indexing for copy kernel\
  \ (#32576)\r\nea84d7090 CUDA: optimize Orin single-column MMVQ (#31268)\r\n9fbe30c2a CUDA: keep the\
  \ MUL_MAT_ID precision in the per-expert fallback (#31345)\r\nc0b97be0b vulkan: optimize RMS_NORM_MUL_ROPE\
  \ loop control (#31149)\r\n16f80bd0c vulkan: chunked GATED_DELTA_NET implementation (#30207)\r\n2d8d00393\
  \ webgpu : add COL2IM_1D support (#31708)\r\n7e960f40f opencl: fold GQA head for f16 FA for better efficiency\
  \ (#32631)\r\n8bf88ba93 vulkan: disable subgroup arithmetic on Qualcomm's driver (#30826)\r\nb94959a64\
  \ CUDA: implement support for duplicate expert IDs (#32505)\r\n50518b64c model : hrm : do not compute\
  \ slot count as uint32_t (#32601)\r\nc406f4367 opencl: support dp4a for KQ mm in decomposed FA (#32577)\r\
  \n7fce5439f ggml : add BF16 support to ROPE and SET_ROWS (CPU, CUDA) (#32387)\r\n53ecea05a mtmd : fix\
  \ YuE2 projector loading (#32606)\r\n9a080f44b ggml-openvino: fix OpenVINO CI, minor fixes and optimizations\
  \ (#32590)\r\nc7468107e cuda: Scatter kernel for set_n (#32489)\r\nac830a9cb ggml : add backend scheduler\
  \ tests (#27258)\r\n8af68d486 llama: fixes for Inkling 2 attention mask (#32429)\r\nf8caa5ea3 metal\
  \ : fix the second argument of NSMakeRange (#32602)\r\n4db8b7638 webgpu: add POOL_2D support (#32250)\r\
  \n01592dc58 llama : remove redundant fields from llm_graph_params (#32596)\r\n8bf2132c3 readme : fix\
  \ release badge (#32597)\r\n5812201a8 ci : fix build-opencl.yml (#32594)\r\n41d8297fe metal : CONV_2D\
  \ tensor API for M5, split-K for all chips (#32542)\r\n51a77c4f2 qwen3vl : set t_layer_inp for EAGLE-3\
  \ (#32589)\r\n76f186df7 ggml : IQ2 creation speedup through caching (#31910)\r\n95b09b62b llama : remove\
  \ PATH_MAX (#32557)\r\nb5dbca1e4 ci : use LLVM 22 (#32565)\r\n80437488a ui: cut Llama Chat's first-load\
  \ JavaScript by 63%, load diagrams, math and PDFs on demand (#32555)\r\n39039aa27 llama : fall back\
  \ to buffered I/O on EIO (#32545)\r\n7a4117eef vulkan : enable MMQ with mixed signedness integer dots\
  \ (#31045)\r\n573aa89de vulkan: Implement stream-k MUL_MAT (#28528)\r\necafc6714 vulkan: use floating-point\
  \ zero for storage-only FP16 in DIAG/TRI (#32379)\r\nd4f5c2604 CUDA: use 64-bit dst offsets in mul_mat_q\
  \ (#32374)\r\n08c252e22 opencl: allow adjusting KV padding in decomposed FA (#32522)\r\ne4b620af1 mtmd:\
  \ support voxcpm2 (#32443)\r\nb001d7bb2 ggml : WASM Relaxed SIMD Enhancement (#19590)\r\n0a7675746 llama\
  \ : fix sticky NaN in recurrent state (#31913)\r\nb04489040 server: fix sleep state for v1/realtime\
  \ (#32567)\r\n78e05298f model : limite: reject mudd configs that index past mudd_tap_idx on load (#32562)\r\
  \n785f6bac0 ui : keep streaming reasoning box inside the viewport when zoomed (#31966)\r\nedec462cc\
  \ ggml, ci : use llvm 22.1.8 (#32548)\r\n4483b2b98 vendor : update cpp-httplib-0.67.0 [no ci] (#32563)\r\
  \nbafa0420c server : enable packing for d1-2B and d1-Omni-2B models (#32553)\r\n2cbfc3cf3 [CUDA] : Add\
  \ SKU-aware FP16/BF16 accumulation precision gating for NVIDIA GPUs (#30672)\r\n6f311d7ad webgpu: (fix\
  \ CI) allow the FA mask to be broadcast over the Q batch (#32535)\r\nff6b8d176 ggml-cpu : use all threads\
  \ for large GET_ROWS (#32514)\r\n98d67c8d5 model:add Zaya1 8B (Zyphra) (#32071)\r\n387395aa8 ui: install\
  \ @ggml-org/llama-brand from npm (#32544)\r\na693a5f66 ui: llama-chat publish drops the registry check,\
  \ bin paths without ./ (#32543)\r\nb069e526d gguf-py : fix tensor offset overflow in GGUFReader (#32495)\r\
  \nffc87c3a7 ui: soften the action card border and show the split-button divider in dark mode (#32538)\r\
  \n10f173b25 ui: hide Models and MCP behind settings, off by default (#32527)\r\n97069ff6c ui: run Llama\
  \ Chat with npx @ggml-org/llama-chat (#32524)\r\nbba840882 Add LLAMA_MOE_RANDOM_ROUTING=1 for benchmark-only\
  \ random expert selection (#29539)\r\n48a32194e server: fix transcription prompt for v1/realtime (#32507)\r\
  \n6da36139e ui: run the Storybook deploy on HF Jobs, with a token that can write the Space (#32525)\r\
  \n61f182fcd unicode : add continuation check lambda (#31070)\r\n03ec5b432 cuda : fuse NORM + MUL (+\
  \ ADD) (#32454)\r\n7144124a5 vocab : extract bpe_rank loading into function (#30962)\r\n43bd7a2a4 vulkan:\
  \ add bfloat16 support to various ops (#32202)\r\n65758d01f ui: Storybook follow-ups: generated DESIGN.md\
  \ tokens, shared helpers and one Llama Mono (#32523)\r\na300a9c33 cuda : increase Pascal DP4A MMQ I\
  \ tile for J=64 (#31352)\r\n4577932fa ggml-openvino: expand model support, optimize NPU,GPU and memory\
  \ usage (#32172)\r\n398f00d65 CUDA: use MMQ for MoE on V100 (#32504)\r\n9e93cd800 ui: a Storybook for\
  \ Llama UI and Llama Chat (#32485)\r\naaa807c56 cuda: decode the conv2d patch indices with fastdiv (#32492)\r\
  \n401563f10 vulkan: run rms_norm with a runtime loop count on Qualcomm (#30824)\r\n52975342f server:\
  \ slot_sched: fix lora and recurrent (#32434)\r\n3574df84b mtmd: support tiny-voca (#32427)\r\n2e53a0bab\
  \ ggml-cuda: hip: Tune stream_k algo and mmq configs to use stream_k on AMD GCN (#30022)\r\n744c68cd1\
  \ ui: publish @ggml-org/llama-ui from CI, and release 0.4.0 (#32480)\r\n307e3f155 mtmd: add kokoro tts\
  \ support (#32413)\r\n9048bad8d cuda: use the implicit GEMM conv2d path for F32 kernels (#32482)\r\n\
  a9d43ecc3 opencl: add A7 Q5_K non-MoE binary kernel (#31002)\r\n8c16babba mtmd: Add support for Qwen3-TTS'\
  \ ICL/reference mode (#32438)\r\nad9d9e8f5 qwen4exp : fix graph reallocation from the n-gram table scale\
  \ (#32483)\r\n955c4e8ee server : return 400 when grammar and ignore_eos are on (#32377)\r\n10152bc4a\
  \ ggml-cuda: disable quantized matvec fusion on all Pascal GPUs (#32239)\r\n8777c0c83 Title: CUDA: few-row\
  \ MMQ for MUL_MAT_ID (#32065)\r\n918076a63 ui: turn the live markdown preview off by default (#32469)\r\
  \nebc9fb933 CUDA: use block reductions for whole-row pool_1d (#31855)\r\n8b8ca4c98 ggml : decode F8_E4M3\
  \ to fp32 without ldexpf (#32477)\r\n08a9b3589 llama : keep the k-pool layout prefix on sequence edits\
  \ (#32137)\r\nacad5e405 vocab : speed up PLaMo-2/3 tokenizer table build (#32249)\r\nd3064fddc convert\
  \ : fix FP8 qwen4exp checkpoints (n-gram table scale, block-scaled FP8) (#32476)\r\n7f106b545 ui: Llama\
  \ UI design system: tokens, surfaces and fonts (#32468)\r\nd92ea9bb1 mtmd: support Minimax-Music3 (#32435)\r\
  \n8d1599fca chat: add tts_dict for kokoro G2P template (#32397)\r\n054a1babf Rotate  K/V read order\
  \ for better L2 cache hit rates (#32407)\r\n513ad7ae0 ui: turn conversation tabs off by default (#32402)\r\
  \n67cf8967e ui: move Llama Chat to SvelteKit 3 and its built-in service worker (#32463)\r\n4df3f2959\
  \ qwen3next : apply output projection weight scale (#32393)\r\na49db739f cuda : raise shared mem limit\
  \ only for the launched kernel (#32392)\r\neada89c31 nix: expose a SYCL package (#31066)\r\n8f647f1fd\
  \ vulkan: disable flip Flash Attention shader on AMD Windows due to a driver bug (#32415)\r\ndde9de82c\
  \ sycl : Fix FA mkl issue: a mask broadcast over heads or batches (#31536)\r\ne0a9118fe metal : add\
  \ implicit GEMM kernel for CONV_2D (#28069)\r\n140a27987 webgpu : Implement timestep embedding (#31695)\r\
  \nc145db272 webgpu : use f32 while dequantizing to avoid FTZ (#32140)\r\nede610678 opencl: support f16\
  \ and non-contig f32 silu (#32319)\r\n9214bdb55 sycl: use fast division in bin-bcast kernels (#32213)\r\
  \nd3c3e242c opencl: add A7 Q8_0 non-MoE binary kernel (#31003)\r\n9581154a2 mtmd : fix Muse Glimmer\
  \ vision embedding order (#32433)\r\n1ef8c5d68 convert : respect max_position_embeddings for granite\
  \ hybrid (#32436)\r\ne8fbcad85 tests: print the exception message in test-llama-context (#32428)\r\n\
  95e837aaf skills: explicitly specify paths to README-dev.md (#32431)\r\nd998c676f convert: Fix inkling\
  \ 2 mmproj conversion (#32430)\r\n92192d31e mtmd: support YuE2-3B (#32369)\r\nad5cbfa91 opencl: add\
  \ A7 Q4_K non-MoE binary kernel (#30948)\r\nd261e49e7 opencl: fix three defects of the bin flash-attention\
  \ prefill path (#32110)\r\n4ddf2b947 chat : implement inkling parser (#32381)\r\n4303cd94a contributing:\
  \ mark agents.md and code-review as required (#32416)\r\nc7518dbec MMVQ: Tune ne11 Gate for RDNA3_5\
  \ (#32308)\r\na68c6136b mtmd: support fish audio s2 (#32330)\r\n3a7660371 ui: move the web UI to ui/apps/chat\
  \ and call it Llama Chat (#32032)\r\ne8698ac16 fix:- Misc. bug: Settings/Tools is lying about tool picks\
  \ inside a ch… (#32223)\r\n7804be063 arg : allow up to llama_max_devices() configs for --tensor-split\
  \ and --fit-target (#13293) (#31435)\r\nef6bc6f36 jinja: impl scope-chain key lookup (#32396)\r\na06044b93\
  \ llama : deprecate old batch API (#32306)\r\n62a6d3a30 llama : migrate to `llama_batch_ext` (#32356)\r\
  \nef3848f9d vulkan: Support split_k for conv3d. (#29929)\r\n47fe13331 HIP/CUDA: enable GDN mma kernel\
  \ on CDNA (#31327)\r\n301db6337 vulkan: fix Nvidia fp32 FA shmem overflow, disable shmem staging if\
  \ it takes too much memory (#32244)\r\na001af915 hip: add gfx1013 to rdna1 (#32236)\r\n164ab018f webgpu:\
  \ support per-head flash attention masks (#32394)\r\n5cb951679 readme : fix line endings\r\n8bfd64b5a\
  \ readme : update (#32382)\r\ne1925b369 jinja: support json sort_keys=true (#32366)\r\n95db855bc ci\
  \ : use vX.Y.Z tags as docker tags (#32388)\r\n1d2e880ba vulkan : fix 32-bit compilation (#32275)\r\n\
  adf554d23 vulkan: make the radix top-k tie selection deterministic (#31931)\r\n6b01a4767 CI: trigger\
  \ spec dec testing for relevant PRs (#32281)\r\nf477c1b90 cuda : fix MUL_MAT_ID abort with odd src0\
  \ columns on AMD (#32385)\r\n21fa9c043 kv-cells: avoid an O(n_cells) scan per sequence removal (#32380)\r\
  \na946eb541 server: answer reasoning_effort levels the template rejects with 400 (#32332)\r\n05db09a4d\
  \ ggml-cuda: fix MoE regression on HIP with #29948 (#32344)\r\n9fba51d2c convert: fix ripple dflash2\
  \ NoPE metadata (#32363)\r\nb4c0e00a4 jinja: add 4 missing features (#32352)\r\n1719dbb0e server : skip\
  \ MCP discovery for router children (#32359)\r\nfc504f91d mtmd: support higgs v3 STT and vibevoice-ASR\
  \ (#32329)\r\n18b74fa41 model : read qwen3vl output head size from the tensor (#32349)\r\n7ae3c6b23\
  \ mtmd: add zonos3-mini TTS model (#32020)\r\nf4d067391 Revert \"jinja: add 4 missing features\"\r\n\
  a681a53b6 jinja: add 4 missing features\r\n75fd7f9ec docs: move per-model TTS to /docs, refer it from\
  \ other pages (#32304)\r\na68799c60 model: support MiniMax-M3.1 (#32301)\r\n56fd8a375 server : ignore\
  \ empty stop strings (#32093)\r\nb54752df4 ggml-cpu: add x86 VNNI Q2_0 dot product (#26348)\r\n900f01ba0\
  \ CI/HIP: update fattn symbol names in hip-quality-check (#32331)\r\nde32b268c Support DFLASH2 for Recursive\
  \ Ripple-65B-Preview (#31904)\r\n4e5116f47 server : fix output_config.effort being dropped in /v1/messages\
  \ (#32321)\r\n278a89cb7 CUDA/HIP: Refactor the use of _sync warp primitives (#31617)\r\ndd099a6bf chat:\
  \ fix inkling 2 begin/end of image tokens placement (#32294)\r\n73f53317e vendor: sync stb_image (#32305)\r\
  \n429460dc0 server: refactor, add server_slot_sched, prompt running hash (#32154)\r\n58a4a6b49 server\
  \ : clear slot cache when the global lora config changes (#30367)\r\n5a4afd807 tests: Fail `test-backend-ops`\
  \ and exit with error status 1 when missing and/or unsupported types and/or unsupported backends are\
  \ provided in the command line (#30279)\r\n6d3568e31 opencl: add A7 Q6_K non-MoE binary kernel (#30949)\r\
  \ne574a17b0 model : metal : workaround fusion for LFM3 (#32296)\r\n5c008e000 feat: add Inkling 2 support\
  \ (text + vision) (#32217)\r\n9f26fe11c common : reject out-of-range grammar_triggers type instead of\
  \ aborting (#30835) (#31478)\r\ncf9a9957d server : Fix connection reuse after streamed responses (#30492)\r\
  \ndca216ad6 hexagon: add TIMESTEP_EMBEDDING HVX kernel (#32228)\r\nf8cc5774e memory : fix non-consecutive\
  \ position warning for M-RoPE (#32287)\r\nacf5d5456 llamafile: introduce more Q0 quant support for s390x\
  \ (#32203)\r\n3e41ae69d llama : allocate the tensor staging buffer from the CPU buffer type (#31438)\r\
  \n3bc612fe2 vulkan: Explicitly include SPIRV-Headers (#31416)\r\nd8f30a5b6 vulkan: optimize prompt processing\
  \ Flash Attention for RDNA3 and RDNA4 (#31323)\r\ne96417565 cuda : keep columns in registers for cooperative\
  \ softmax (#28982)\r\nd20426bbb vulkan: optimize matrix multiplication for narrow N (#31990)\r\n19f31e61b\
  \ vulkan: use GPU copies on UMA with uncached memory on Intel (#32024)\r\n07037ba13 sycl : optimize\
  \ mtmd image processing (#32109)\r\n0cc522e45 chat : allow undeclared tool calls in LFM2 tool-call grammar\
  \ (#32164)\r\nf08bca8a4 docs : add OpenVINO backend to ops matrix (#32259)\r\n3c311796f chat : allow\
  \ tool calls inside reasoning blocks for Ministral-3 (#32271)\r\n8b4ac2496 common : fix infinite recursion\
  \ in debug build for peg parser dump (#32282)\r\n1ae047c92 opencl: fixes for q4_k mv oob access, f16\
  \ swiglu_oai, cpy with strided dst, batched group_norm and bf16 sigmoid (#32251)\r\n1c2adc75f chat :\
  \ allow Gemma4 tool call during thought (#32232)\r\na956a852c Fix ctz64 on 32bit (#32273)\r\nc6c0ec6d5\
  \ hexagon: fix fa no-mask tail (#32243)\r\nd0764c5ee qwen2vl : apply FFN weight scales (#32241)\r\n\
  3549c274d convert : register Granite4VisionForConditionalGeneration for text (#32237)\r\nc56be864f ggml-backend\
  \ : start a new split at an incompatible weight in a split without inputs (#31775)\r\na9a5d216e convert\
  \ : pplx-decider must match qwen3.5 model_type (#32156)\r\n9d925e7c0 mtmd: fix video pixel aspect ratio\
  \ and video rotation (#32267)\r\ne3483e40b mtmd : allow custom video decoder (#32188)\r\n4f2187e73 jinja\
  \ : reduce template rendering overhead (#32023)\r\n0cce7580b mtmd : avoid padding-only Whisper audio\
  \ chunks (#30403)\r\n32bdc3a89 spec + model: refactor DFlash based speculative decoding methods  (#32016)\r\
  \n61dbf4922 Hexagon: add support for IQ2_XXS and NVFP4 (#31954)\r\n9d25e0014 chat : remove mistral workaround\
  \ (#32230)\r\n9183a552e metal : fix mul_mv destination offset overflow (#32221)\r\nded522f83 hexagon:\
  \ add support for SSM_SCAN op (#31921)\r\n5193ef1d4 ui: configure allow-remote=root in .npmrc for npm\
  \ 12+ (#32158) (#32196)\r\n4df9b4797 ci: reduce qdc timeouts to avoid stalling pipelines and runners\
  \ (#32148)\r\nb79696f1f ggml-cuda: hip: tune GCN MMQ configs (#30021)\r\n4f9dfa0e3 requirements, Fix\
  \ CI: support Python 3.15 (#32199)\r\n9daa0aa22 hexagon: improve buffer allocations and mappings (mmap\
  \ stacking) (#32144)\r\nfe14cad51 CUDA: add SM103 SASS to non-native builds (#30099)\r\n31953bcf7 ggml\
  \ : add BF16 support to RMS_NORM (CPU, CUDA) (#32135)\r\nae93877c8 vulkan: add TOP_K_MASK (#31544)\r\
  \n7874988b4 spec : Warn when --spec-draft-p-min is used with probabilistic draft sampling (#31294)\r\
  \n8c2c4c39c ggml-vulkan: add optional device keepalive (#29267)\r\n108f73adf grammar : optimize matching\
  \ with left factoring (#29557)\r\n951d465f5 llama: move moe-cache code out of llama-graph (#32157)\r\
  \n2d8a32502 CUDA: split the PAD_REFLECT_1D grid to stay within the HIP grid limit (#32179)"
first_seen: '2026-11-27T04:16:07Z'
last_seen: '2026-11-28T03:55:23Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ggml-org/llama.cpp/releases/tag/v1.1.0
  seen_at: '2026-11-28T03:55:23Z'
  metrics:
    reactions: 47
  kind: news
---

# ggerganov/llama.cpp: v1.1.0

## Overview

llama.cpp v1.1.0 adds the Inkling 2 family (base, Mini and DSpark), Domyn Edge 4B, Zaya1 8B, RAON-1-mini and Hy4 flash, splits DFlash speculative decoding into separate draft methods, and deprecates the old `llama_batch` API in favour of `llama_batch_ext`. It brings a large set of TTS and audio models (Kokoro, Zonos3-Mini, tiny-voca, VoxCPM2, MiniMax-Music3, YuE2, Fish S2, Higgs v3/VibeVoice-ASR and Kyutai Hibiki), token-aware chat parsing, named tool choice, automatic per-tensor quantization targeting a bpw or size budget, a slot-scheduling refactor in `llama-server`, a redesigned Llama Chat web UI with voice messages and agent traces, and updates `ggml` to v1.1.1.

### API changes

- llama.h: deprecate the old `llama_batch` API in favour of `llama_batch_ext` and `llama_process` ([#32306](https://github.com/ggml-org/llama.cpp/pull/32306), [#32356](https://github.com/ggml-org/llama.cpp/pull/32356))
- llama.h: add `llama_dflash_variant` and `llama_model_dflash_variant()` for the four DFlash draft heads ([#32016](https://github.com/ggml-org/llama.cpp/pull/32016))
- llama.h: add `llama_model_meta_arr_n()` and `llama_model_meta_arr_str()` to read GGUF string arrays ([#32397](https://github.com/ggml-org/llama.cpp/pull/32397))
- llama.h: add `target_bpw`, `target_size`, `state_file` and abort callback to `llama_model_quantize_params` ([#15550](https://github.com/ggml-org/llama.cpp/pull/15550))
- mtmd.h: add audio types for Zonos3, YuE2, MiniMax-Music3, Fish S2, Moshi, Kokoro, tiny-voca, VoxCPM2 ([#32020](https://github.com/ggml-org/llama.cpp/pull/32020), [#32330](https://github.com/ggml-org/llama.cpp/pull/32330), [#32369](https://github.com/ggml-org/llama.cpp/pull/32369), [#32413](https://github.com/ggml-org/llama.cpp/pull/32413), [#32427](https://github.com/ggml-org/llama.cpp/pull/32427), [#32435](https://github.com/ggml-org/llama.cpp/pull/32435), [#32443](https://github.com/ggml-org/llama.cpp/pull/32443), [#32491](https://github.com/ggml-org/llama.cpp/pull/32491))
- mtmd.h: add `n_channels`, `mtmd_gen_audio_g2p()` and `mtmd_gen_state_get_ref_codes()` ([#32413](https://github.com/ggml-org/llama.cpp/pull/32413), [#32586](https://github.com/ggml-org/llama.cpp/pull/32586))
- server: accept OpenAI named `tool_choice` and add `GET /models/sse` in single-model mode ([#31564](https://github.com/ggml-org/llama.cpp/pull/31564), [#32398](https://github.com/ggml-org/llama.cpp/pull/32398))
- server: add `--ui-agent` and `--ui-mcp-proxy-allow-private-urls` ([#33004](https://github.com/ggml-org/llama.cpp/pull/33004), [#32633](https://github.com/ggml-org/llama.cpp/pull/32633))

### New models

- Inkling 2 (text + vision), Inkling 2 DSpark and Inkling 2 Mini ([#32217](https://github.com/ggml-org/llama.cpp/pull/32217), [#32218](https://github.com/ggml-org/llama.cpp/pull/32218), [#32694](https://github.com/ggml-org/llama.cpp/pull/32694))
- Domyn Edge 4B: interleaved SWA with RoPE only on SWA layers and Q/K norm ([#32559](https://github.com/ggml-org/llama.cpp/pull/32559))
- Zaya1 8B ([#32071](https://github.com/ggml-org/llama.cpp/pull/32071))
- MiniMax-M3.1 ([#32301](https://github.com/ggml-org/llama.cpp/pull/32301))
- RAON-1-mini-preview: 30B-A4B MoE ([#32176](https://github.com/ggml-org/llama.cpp/pull/32176))
- Hy4 flash: 220B (12B active) text and vision on the DSA iSWA cache ([#32960](https://github.com/ggml-org/llama.cpp/pull/32960))
- DFlash2 for Recursive Ripple-65B-Preview ([#31904](https://github.com/ggml-org/llama.cpp/pull/31904))
- TTS: Kokoro, Zonos3-Mini and tiny-voca ([#32413](https://github.com/ggml-org/llama.cpp/pull/32413), [#32020](https://github.com/ggml-org/llama.cpp/pull/32020), [#32427](https://github.com/ggml-org/llama.cpp/pull/32427))
- Kyutai Hibiki / Moshi realtime full-duplex voice in/out ([#32491](https://github.com/ggml-org/llama.cpp/pull/32491))

### Core changes

- split DFlash speculative decoding into `draft-dflash`, `draft-dflash2`, `draft-dspark` and `draft-lilicorr` ([#32016](https://github.com/ggml-org/llama.cpp/pull/32016))
- use GDN replay instead of rollback ([#31669](https://github.com/ggml-org/llama.cpp/pull/31669))
- add `--target-bpw`/`--target-size` per-tensor quant selection with a resumable state file ([#15550](https://github.com/ggml-org/llama.cpp/pull/15550))
- match special tokens in chat parsing instead of text (token-aware parsing) ([#29307](https://github.com/ggml-org/llama.cpp/pull/29307))
- speed up BPE tokenization and the PLaMo-2/3 tokenizer table build ([#32859](https://github.com/ggml-org/llama.cpp/pull/32859), [#32249](https://github.com/ggml-org/llama.cpp/pull/32249))
- move the MoE cache out of `llama-graph` and reserve graph nodes for it ([#32157](https://github.com/ggml-org/llama.cpp/pull/32157), [#32636](https://github.com/ggml-org/llama.cpp/pull/32636))
- move the graph node budget and indexer key rotation choice into the model classes ([#32648](https://github.com/ggml-org/llama.cpp/pull/32648), [#32653](https://github.com/ggml-org/llama.cpp/pull/32653))
- apply `.scale` tensors automatically and load `ffn_gate_up_exps` scales ([#32669](https://github.com/ggml-org/llama.cpp/pull/32669), [#32657](https://github.com/ggml-org/llama.cpp/pull/32657))
- fix sticky NaN in recurrent state, k-pool layout on sequence edits and QSA k-pool scoring ([#31913](https://github.com/ggml-org/llama.cpp/pull/31913), [#32137](https://github.com/ggml-org/llama.cpp/pull/32137), [#32519](https://github.com/ggml-org/llama.cpp/pull/32519))
- fall back to buffered I/O on EIO and allocate the staging buffer from the CPU buffer type ([#32545](https://github.com/ggml-org/llama.cpp/pull/32545), [#31438](https://github.com/ggml-org/llama.cpp/pull/31438))
- avoid an O(n_cells) scan per sequence removal in the KV cells ([#32380](https://github.com/ggml-org/llama.cpp/pull/32380))
- honor `metaspace_prepend_scheme` for SPM and always for BPE, and load YaRN hparams in the model base ([#31986](https://github.com/ggml-org/llama.cpp/pull/31986), [#33038](https://github.com/ggml-org/llama.cpp/pull/33038), [#33032](https://github.com/ggml-org/llama.cpp/pull/33032))
- fix per-sequence state restore with ON_DEVICE KV caches ([#30318](https://github.com/ggml-org/llama.cpp/pull/30318))
- use the indexed bias FATTN path in Inkling 2 and map Inkling-2 LoRA tensor names ([#33053](https://github.com/ggml-org/llama.cpp/pull/33053), [#33055](https://github.com/ggml-org/llama.cpp/pull/33055))
- add `LLAMA_MOE_RANDOM_ROUTING=1` for benchmark-only random expert selection ([#29539](https://github.com/ggml-org/llama.cpp/pull/29539))
- optimize grammar matching with left factoring and fix an integer overflow ([#29557](https://github.com/ggml-org/llama.cpp/pull/29557), [#32551](https://github.com/ggml-org/llama.cpp/pull/32551))
- allow up to `llama_max_devices()` configs for `--tensor-split` and `--fit-target` ([#31435](https://github.com/ggml-org/llama.cpp/pull/31435))
- jinja: scope-chain key lookup, `sort_keys=true`, 4 missing features and lower rendering overhead ([#32396](https://github.com/ggml-org/llama.cpp/pull/32396), [#32366](https://github.com/ggml-org/llama.cpp/pull/32366), [#32352](https://github.com/ggml-org/llama.cpp/pull/32352), [#32023](https://github.com/ggml-org/llama.cpp/pull/32023))
- chat: inkling parser, undeclared LFM2 tool calls, tool calls in reasoning, lazy grammar ([#32381](https://github.com/ggml-org/llama.cpp/pull/32381), [#32164](https://github.com/ggml-org/llama.cpp/pull/32164), [#32271](https://github.com/ggml-org/llama.cpp/pull/32271), [#32232](https://github.com/ggml-org/llama.cpp/pull/32232), [#32497](https://github.com/ggml-org/llama.cpp/pull/32497))
- chat: implement named `tool_choice` and pass `reasoning_effort=none` when supported ([#31564](https://github.com/ggml-org/llama.cpp/pull/31564), [#32763](https://github.com/ggml-org/llama.cpp/pull/32763))
- json-schema: accept boolean `"value": true` and reject out-of-range grammar triggers ([#32908](https://github.com/ggml-org/llama.cpp/pull/32908), [#31478](https://github.com/ggml-org/llama.cpp/pull/31478))

### Multi-modality changes

- add support for VoxCPM2, MiniMax-Music3, YuE2-3B, Fish Audio S2 and Higgs Audio v3/VibeVoice-ASR ([#32443](https://github.com/ggml-org/llama.cpp/pull/32443), [#32435](https://github.com/ggml-org/llama.cpp/pull/32435), [#32369](https://github.com/ggml-org/llama.cpp/pull/32369), [#32330](https://github.com/ggml-org/llama.cpp/pull/32330), [#32329](https://github.com/ggml-org/llama.cpp/pull/32329))
- drama3 voice cloning and Qwen3-TTS ICL/reference mode ([#32586](https://github.com/ggml-org/llama.cpp/pull/32586), [#32438](https://github.com/ggml-org/llama.cpp/pull/32438))
- speed up the shared audio FFT and avoid padding-only Whisper audio chunks ([#32815](https://github.com/ggml-org/llama.cpp/pull/32815), [#30403](https://github.com/ggml-org/llama.cpp/pull/30403))
- allow a custom video decoder and fix video pixel aspect ratio and rotation ([#32188](https://github.com/ggml-org/llama.cpp/pull/32188), [#32267](https://github.com/ggml-org/llama.cpp/pull/32267))
- merge Parakeet rel-pos views to avoid OOB, fix YuE2 projector loading and the qwen3a audio tail ([#32722](https://github.com/ggml-org/llama.cpp/pull/32722), [#32606](https://github.com/ggml-org/llama.cpp/pull/32606), [#32697](https://github.com/ggml-org/llama.cpp/pull/32697))
- add `--tts-lang`, `--tts-voice` and `--tts-speaker-text` for per-model TTS voices ([#32330](https://github.com/ggml-org/llama.cpp/pull/32330), [#32586](https://github.com/ggml-org/llama.cpp/pull/32586))

### Server changes

- refactor slot scheduling into `server_slot_sched` with per-prompt running hashes ([#32154](https://github.com/ggml-org/llama.cpp/pull/32154))
- retry cached prompt restoration after clearing idle slots and preserve entries until restores succeed ([#30997](https://github.com/ggml-org/llama.cpp/pull/30997), [#32828](https://github.com/ggml-org/llama.cpp/pull/32828), [#28992](https://github.com/ggml-org/llama.cpp/pull/28992))
- clear slot cache when the global LoRA config changes ([#30367](https://github.com/ggml-org/llama.cpp/pull/30367))
- reuse HTTP connections after streamed responses ([#30492](https://github.com/ggml-org/llama.cpp/pull/30492))
- include MCP image and audio data in tool results ([#32064](https://github.com/ggml-org/llama.cpp/pull/32064))
- add offset pagination to `grep_search` and ask `exec_shell_command` for a short description ([#32792](https://github.com/ggml-org/llama.cpp/pull/32792), [#32894](https://github.com/ggml-org/llama.cpp/pull/32894))
- return 400 for rejected `reasoning_effort` levels and grammar with `ignore_eos`, fix `output_config.effort` ([#32332](https://github.com/ggml-org/llama.cpp/pull/32332), [#32377](https://github.com/ggml-org/llama.cpp/pull/32377), [#32321](https://github.com/ggml-org/llama.cpp/pull/32321))
- ignore empty stop strings ([#32093](https://github.com/ggml-org/llama.cpp/pull/32093))
- fit non-causal batches in one ubatch and enable packing for d1-2B/d1-Omni-2B ([#32713](https://github.com/ggml-org/llama.cpp/pull/32713), [#32553](https://github.com/ggml-org/llama.cpp/pull/32553))
- skip MCP discovery for router children ([#32359](https://github.com/ggml-org/llama.cpp/pull/32359))
- fix sleep state and transcription prompt for `/v1/realtime` ([#32567](https://github.com/ggml-org/llama.cpp/pull/32567), [#32507](https://github.com/ggml-org/llama.cpp/pull/32507))
- handle `CTRL_BREAK_EVENT` on Windows for clean shutdown ([#32080](https://github.com/ggml-org/llama.cpp/pull/32080))
- fix LoRA and recurrent slot scheduling ([#32434](https://github.com/ggml-org/llama.cpp/pull/32434))

### UI changes

- move the web UI to `ui/apps/chat` as Llama Chat, with a Llama UI design system and Storybook ([#32032](https://github.com/ggml-org/llama.cpp/pull/32032), [#32468](https://github.com/ggml-org/llama.cpp/pull/32468), [#32485](https://github.com/ggml-org/llama.cpp/pull/32485))
- move to SvelteKit 3 and cut first-load JavaScript by 63% with on-demand diagrams, math and PDFs ([#32463](https://github.com/ggml-org/llama.cpp/pull/32463), [#32555](https://github.com/ggml-org/llama.cpp/pull/32555))
- add voice messages and dictation with live waveforms and transcripts ([#32531](https://github.com/ggml-org/llama.cpp/pull/32531))
- show agentic replies as a grouped Agent Trace, with the loop in `@ggml-org/llama-harness` ([#32879](https://github.com/ggml-org/llama.cpp/pull/32879), [#32927](https://github.com/ggml-org/llama.cpp/pull/32927))
- run Llama Chat apart from llama-server, via `npx @ggml-org/llama-chat` or a config URL ([#32524](https://github.com/ggml-org/llama.cpp/pull/32524), [#32945](https://github.com/ggml-org/llama.cpp/pull/32945))
- make Llama Chat a plain chat unless the server offers agent features ([#32949](https://github.com/ggml-org/llama.cpp/pull/32949))
- add `--ui-agent` for agent mode without server tools or the MCP proxy ([#33004](https://github.com/ggml-org/llama.cpp/pull/33004))
- set the reasoning effort from the model picker and add a cancel button for model loading ([#32632](https://github.com/ggml-org/llama.cpp/pull/32632), [#32225](https://github.com/ggml-org/llama.cpp/pull/32225))
- import conversations or settings by dropping them anywhere in the app ([#32958](https://github.com/ggml-org/llama.cpp/pull/32958))
- search message content and Discover models from the search dialog ([#32670](https://github.com/ggml-org/llama.cpp/pull/32670))
- open the context gauge as a popover and add a full-screen diagram preview ([#32685](https://github.com/ggml-org/llama.cpp/pull/32685), [#32591](https://github.com/ggml-org/llama.cpp/pull/32591))
- hide Models and MCP behind settings, turn conversation tabs and the live markdown preview off by default ([#32527](https://github.com/ggml-org/llama.cpp/pull/32527), [#32402](https://github.com/ggml-org/llama.cpp/pull/32402), [#32469](https://github.com/ggml-org/llama.cpp/pull/32469))
- slim the design tokens and set all text through type roles ([#32615](https://github.com/ggml-org/llama.cpp/pull/32615))
- open Settings, the + menu and the model picker as sheets on phones, and manage MCP from Settings ([#33036](https://github.com/ggml-org/llama.cpp/pull/33036))
- stop the streaming reply with Escape and make `npx llama-chat` default to `:9931` ([#33051](https://github.com/ggml-org/llama.cpp/pull/33051), [#33095](https://github.com/ggml-org/llama.cpp/pull/33095))

### ggml changes

- [v1.1.0](https://github.com/ggml-org/ggml/releases/tag/v1.1.0): ggml v1.1.0 extends the graph API for new model families, strengthens scheduler and backend behavior, and brings broad performance work across all backends. The API gains gated-delta-net replay, flash-attention indexed bias, ordered asynchronous host input copies, and scheduler scratch reservation, plus new SLEEP and SIGMOID_BACK operators. Core adds BF16 coverage for more operations, faster quantization and math helpers, and new CPU quant kernels, while backends add stream-k matmul, chunked command buffers, NVFP4, CONV_2D acceleration, wider FP8/BF16 support, and many tuning and correctness fixes.
- [v1.1.1](https://github.com/ggml-org/ggml/releases/tag/v1.1.1): ggml v1.1.1 lands Hexagon 2.0 with INT-HMX W8A8 matmul, automatic F32 to F16 lowering and generic DMA pipelines, and brings a CUDA FlashAttention data-loading refactor, a SYCL gated-delta-net ESIMD kernel with fused recurrent convolutions, small-K Metal mat-vec tuning, and a WebGPU log1p for softplus. It also adds the TANH backward pass, OpenVINO decode and op-test fixes, and 16-head lightning-indexer support on CUDA.

## Assets

**Nightly build:** [b12774](https://github.com/ggml-org/llama.cpp/releases/tag/b12774)

## More info

- [Releases and versioning of `ggml-org` projects](https://github.com/ggml-org/ggml/discussions/1579)

## Changelog since [v1.0.0](https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0)

171527522 sync : ggml
2a59da5bf ggml : bump version to 1.1.1 (ggml/1703)
07ba74bab sycl: update linux refer doc (#32583)
267dda818 sycl: Remove check for host waits in fattn-mkl from graph checks (#31208)
e0f884d40 ggml-hexagon 2.0 : support for int-hmx, automatic f32 -> f16 lowering, and generic dma pipelines (#32582)
f8b7ed525 cuda : fix int overflow of the MMF matrix offsets (#33044)
55b2238be ggml : add TANH backward pass (#32136)
a8ad690ca sycl: add gated delta net ESIMD kernel (#31762)
aee03fbe8 sycl: fuse recurrent convolution windows (#31355)
9c003a97a ui: open settings, the + menu and the model picker as sheets on phones, and manage MCP from settings (#33036)
7135e2fd6 metal : spread the short mat-vec lanes over src1 rows (#33034)
5917b39ff convert : map the Inkling-2 LoRA tensor names (#33055)
8d35ba4f7 metal : revert "metal: increase default command buffers on iPhone (#31815)" (#33050)
acb269e51 nix : fix build on darwin (#32955)
d9dae0344 opencl: Adreno E17 compiler quirks off by default (#33013)
eb5657509 ui: stop the streaming reply with Escape (#33051)
5a09582d8 model : add RAON-1-mini-preview support (#32176)
2d5b3ddde model: use the indexed bias in the Inkling 2 graph (#33053)
94a1e4b72 CUDA: refactor & deduplicate FA data loading (#32901)
c94333133 model : add hy_v4_flash on the DSA iSWA cache (#32960)
244640b7f ggml-openvino: fix CI op tests and improve KV cache decode (#33002)
679d8677b llama : fix seq state restore with ON_DEVICE (#30318)
beb9d4933 llama.cpp : bump version to 1.1.0 (#33043)
532d67426 vocab : implement Metaspace prepend_scheme always for BPE (#33038)
5e4fda8ed ui: fix for a chat form update loop with large fonts and long model names (otherwise web interface gets Error 500) (#33037)
a28feb458 sync : ggml
312504361 ggml : bump version to 1.1.0 (ggml/1699)
98f870c22 llama : honor metaspace_prepend_scheme for SPM (#31986)
2e2f5a037 model : load YaRN hparams in llama_model_base::load_hparams (#33032)
41c7a1b49 ui: fix tool result media shown twice, uncapped and dropped after its run (#33010)
77026f6e6 ui: open the warm microphone only once the pointer rests on its button (#33033)
c8eda101c ui: add file extensions to the Vite config's local imports (#33023)
996de35a9 ci : revert disable musa.Dockerfile from docker.yml (#33025)
ab16df399 webgpu : add log1p for softplus op (#33017)
0cac1220e ui: time each tool group by its own loop and show the task time in the reply stats (#33030)
1ed4e77f4 ui: search home by default in the working-directory picker and pin tool call chevrons (#33028)
48ac73696 server : handle CTRL_BREAK_EVENT on Windows for clean shutdown (#32080)
5220a2d40 quant : avoid macro collision on windows (#33014)
0fc7e1716 docs : fix stale CPU support in ops.md (#32796)
6d5f64872 ggml-cpu : accept the flash_attn_ext indexed bias (#33016)
52f6e0247 metal : commit the graph in chunks with one command buffer thread (#32947)
de3069728 ui: import conversations or settings by dropping them anywhere in the app (#32958)
62d6c8cb3 ggml: allow input async copies (#30685)
5bd90fa0e common : implement named tool choice (#31564)
522d6fdd4 deepseek41 : read quantized indexer K in place when fused_idx is set (#32795)
61d456a23 common : accept boolean "value": true JSON schema (#32908)
ea7229481 ggml: allow reserving scratch memory in graph_optimize (#31898)
36d818e16 ui: edit the system message in the chat form when it is hidden in conversations (#32967)
81ff0cab0 sycl: F8 e4m3 initial support SET_ROWS, CPY, ADD, MUL_MAT, MUL_MAT_ID (#31871)
cddaa915a SYCL : ROLL op handles permuted source (#31799)
e8906e6b0 ui: add --ui-agent for agent mode without server tools or the MCP proxy (#33004)
abca69200 model : inkling2 graph with fewer ops in mix() and control() (#32948)
e6443bd7e opencl: add clc coopmat moe kernel for q4_0/q4_1/q4_k/q5_0/q5_1/q5_k/q6_k/mxfp4 (#32971)
79c69f4b0 tests : fix MSVC static build of test-batch-alloc and test-server-component (#32870)
33aeb17f8 feat: Inkling 2 DSpark support (#32218)
22b99122e cuda : fix int overflow of the MMVF matrix offsets (#32965)
dfdfca22b docs : describe SpacemiT runtime environment variables (#32452)
a1cee51c9 ggml : fix SpacemiT flash attention null mask, ALiBi and softcap (#32182)
bb692efaa cmake : include the llguidance header from the source tree (#32928)
dbaf582af ci : move some jobs to gb10 runners (#32968)
0ce7f213b ui: run Llama Chat apart from llama-server, named in config.json or npx --server (#32945)
96eb41bc4 ui: fix prebuilt UI download in shallow clones (#32952)
23f0c0182 convert : fix qwen3-omni conversion (#32941)
f20c5907c ggml-cpu: repack kernels for targets without dotprod (ARMv8.0 64-bit) for Q4_0/Q8_0 (#32142)
8bf2eae70 ui: expect the Llama Chat name in the PWA manifest e2e test (#32959)
5fddd0b99 ggml-cpu: add SVE-optimized q5_0 and q5_1 dot-product kernels (#30867)
66a3b01b0 server : include MCP image and audio data in tool results (#32064)
d3c257a49 context : prevent excessive CPU polling without OpenMP (#32378)
3090e45a8 metal : reserve the top-k scratch only for short rows (#32942)
ba8521a44 ui: smooth chat form height and working directory chip across routes (#32950)
72cda4a22 vulkan: add chunked GDN replay support (#32721)
922cff91e cuda : fuse RMS_NORM + MUL + MROPE/IMROPE and tune block size (#32500)
2e779d5e7 Webui nix fix (#32645)
396ed2cce model : Inkling 2 Mini mix() weighted sum with the scores as src0 (#32855)
97bbf98fd ui: make Llama Chat a plain chat unless llama-server offers agent features (#32949)
40fe9164f server : retry prompt cache restore after clearing idle slots (#30997)
26f5048d5 fix building in symlinked directories (#32903)
9578bd3fe CUDA: ignore strides of size-1 dims in bin_bcast (#32854)
e683365a7 model : inkling2 clip with ggml_l2_norm (#32940)
4c92c5bfb CUDA: reduce all cooperative softmax partials when nsm > 256 (#32897)
2a487782f vocab : speed up BPE tokenization (#32859)
6fb428332 CUDA: NVFP4 dequant, pack 8 blocks per CTA (#32875)
6ac648d7a webgpu : Fix indexing bug in softmax kernel (#32691)
94165b288 webgpu : add POOL_1D support (#32254)
a8ed77891 hip: use MMQ over MMVQ for Q4_K,N8 and NVFP4,N7-8 on VEGA20 (#32805)
6970118ef HIP: CDNA1 MMQ config without stream-k (#32837)
ae6a7ad2c ui: move the agentic loop and trace phrasing into @ggml-org/llama-harness (#32927)
5fe490685 ci : disable test-llama-context on ubuntu-llvmpipe (#32932)
82dd97047 server : fix skipped prompt cache lookups (#28992)
a6ac41c75 ui: match tool call timer font size to its title (#32922)
3fccd98e9 ui: let the chat form's model selection decide the submit state (#32920)
4af4bb6d8 rpc : reuse one context for request tensors on the server (#32896)
b12f22d2f ggml : use a range-reduced log1p for softplus (#32655)
d141011c2 vulkan: support state size 96 in ssm_scan (#32162)
12d47ba2f opencl: fix GDN QK offsets (#32747)
af5c58347 opencl: add c8 q6_k coopk GEMM for up to n=8 spec verify (#32909)
c74c71a6f fix editor config in master (#32914)
38b9cad71 quantize : make local const static for MSVC (#32902)
d35dc4d9e GDN: use replay instead of rollback (#31669)
c212d25ad server : preserve a prompt-cache entry until restores succeed (#32828)
fd24ee26a opencl: fetch the Adreno binary kernel library at configure time for Windows on Snapdragon (#31759)
8355b8862 ui: remove the Matte theme and the Light surfaces setting (#32906)
51831d47d metal : add NVFP4 support (#32825)
ab789a246 metal : batch concat rows and copy them in vector chunks (#32824)
239242322 ggml: compact bias on the existing FLASH_ATTN_EXT (#32740)
30ec35ae2 quantize: add option to automatically choose optimal quant types to reach a file/bpw target size at lowest error (#15550)
87f816e87 metal : support BF16/F32 src1 for MUL_MAT and MUL_MAT_ID (#32677)
1d3aad2fd server: ask exec_shell_command for a short description of the command (#32894)
325914def ui: show an agentic reply as a grouped Agent Trace (#32879)
1094646c1 ui: set code in messages at the size of the text around it (#32892)
27d0a1fc7 ui: unmount a closed collapsible's body after one transition (#32881)
b6d5ce4bc ui: drop tool calls cut off by Stop from the next request (#32738)
1f3ea67fb metal: resolve gpu timeout on iPhone for Bonsai (#31815)
a0677c341 ui: use a red edge on the send button's error state (#32856)
2359d27a3 ui: name the PWA from the build env and default it to Llama Chat (#32890)
51fc2f90e ggml-openvino: CI fixes, new model support, fixes and improvements. (#32861)
03813c56e rpc : typed request helpers and a single validation step on the server (#32651)
46f4da217 ggml-cuda : handle zero blocks in few-row MMQ quantization (#32566)
4663f9ca8 ui: smooth height transition for every collapsible (#32873)
969d73331 cmake: treat kleidiai files as vendored (#32605)
a8f8294c4 tests : update Qwen3.6-27B snapshot (#32845)
7d9b931df ggml : update cmake MATH_LIBRARY check (#32864)
212c547fe ui: add cancel button to cancel model loading (#32225)
f5e6915c2 webgpu : add ROLL support (#31887)
dd53f70d0 chat : improve inkling parser/grammar (#32833)
1f8baae28 opencl: add xielu (#32791)
44d50873b opencl: add q4_k coop-k c8 GEMM for spec verify (#32716)
7778de0c3 tests : compare only the guaranteed GDN snapshot slots (#32820)
f4f6f2e7d ggml-backend : generic fallback in ggml_backend_tensor_memset  (#32574)
253671d88 chat: fix LFM2.5-VL template detection (#32843)
94f3af3d0 mtmd: speed up shared audio FFT (#32815)
f505c30b9 mtmd: fix qwen3a audio tail (#32697)
5bacb7c86 llama : copy all experts of a host weight shared by several nodes (#32807)
d2bceda3d vocab: enable ignore_merges for inkling2 (#32799)
56eea9e4b server : add offset pagination to grep_search tool (#32792)
e14a2d3a6 skill: Pay attention to tokenizer flags (#32819)
1014775c8 chat : implement token aware parsing (#29307)
0b51bb2fe server: support /models/sse on single-model mode (#32398)
8d60873df ggml/gguf : avoid creating invalid enum values from untrusted file data (#32641)
ad50351f5 ggml : add SIGMOID backward pass (#32126)
42f6a58fd chat : trigger lazy grammar on bare JSON tool calls (#32497)
9c10c94e1 ggml : fix nonzero clear on WebGPU and non-UMA devices (#32727)
8cb0d98cc HIP: fix double halving of NVFP4 scales on CDNA3 (#32790)
e300919cc webgpu : update GDN supports_op check (#32782)
5d28d64bf ggml-webgpu : Update to a recent version of Dawn (#32779)
1fb8a2696 opencl: add coopmat GEMM for Adreno 850 (Q4_0, Q5_0, Q8_0, Q4_K, Q5_K, Q6_K) (#32686)
8a97fa98a vulkan : support non-contiguous src in SCALE (#32735)
225a5345b server : fit non-causal batches in one ubatch (#32713)
b05204927 vulkan : fix memset for unaligned ranges for non-UMA devices (#32725)
cbb1c1c50 model: fix no_realloc for clef and vllm-decision2 (#32754)
afe77e18f chat : pass reasoning_effort = none if supported (#32763)
e6d624b9a mtmd : merge Parakeet rel-pos views to avoid OOB (#32722)
19bc41dbb model: apply .scale tensors automatically + fix correctness (#32669)
e50c254a2 sycl: bound CONV_TRANSPOSE_1D input iteration (#31109)
660be5506 ggml : improvements to the memory access pattern in `ggml_compute_forward_mul_mat_one_chunk` (#30846)
c622f623f mtmd: support kyutai/hibiki realtime full-duplex (#32491)
c66103334 sycl: add IQ4_NL and IQ4_XS weight reorder (#31998)
44c20b1c0 sycl: column-blocked gated_delta_net kernel (#32456)
80325823d ui: open the context gauge panel on click as a popover (#32685)
a818a46f3 sycl: add fused ADD, RMS_NORM, MUL and vectorize rms norm (#31753)
b019be0c8 CUDA: abort on UB in fastdiv (#32698)
362ac9297 vulkan: unroll FA coopmat1 array due to a driver bug on AMD Windows (#32466)
fb7090df5 vulkan: improve RDNA4 MMVQ performance for Q3_K, Q5_K and IQ4_XS (#31804)
690b87d88 model : inkling2_loop share the loop slots after the scale pass (#32704)
838d94243 model : additional shortcut checks for OOB in hrm_text (#32720)
3da11de1f ggml-zdnn: fix ztensor load race condition (#32279)
93cb37ea7 ggml-cpu: fix nc aligment in tinyBLAS_PPC_Q0 (#32659)
1fdda89a4 ci: switch ppc64le runners to ubuntu 26.04 (#32679)
e412c6f46 llama : remove fused lightning indexer gating (#32650)
40b7a546d ci: temporary disable no realloc case for mtmd (#32708)
46eb1742d llama-grammar: Fix integer overflow (#32551)
6792507b7 llama : score only the k-pools of the ubatch sequences in QSA (#32519)
418fe97b5 sycl: Improve Grouped XMX GEMM by avoiding SLM staging (#31428)
7476e4726 docs: openvino backend details, fix SYCL docs (#30967)
29b52d398 model : Inkling 2 Mini (#32694)
e3c3f666a hip: add RDNA1 MMVQ parameter table (1 warp per block for ncols=1) (#32389)
b2e659ec2 ggml-openvino: update openvino CI runs triggers (#32593)
919794500 convert: qwen3-asr: put "language ..." output into thinking block (#32571)
a83d68b56 metal : allow the norm chain in either operand of the fused MUL/ADD (#32300)
e46069c40 ui: fix the flaky reset check of the MermaidPreview Flowchart story (#32675)
427a83673 ui: stage Llama Voice's sources for CMake and Docker UI builds (#32680)
374d90a9f ci : disable musa.Dockerfile from docker.yml (#32674)
98709fd82 server: add more decision tests (#32578)
7716ec8cb ggml : major version bump reminders + deprecate ggml_ftype (#32647)
34ff2e047 mtmd: drama3 voice cloning (#32586)
6f5c9ad21 vulkan: add support for COL2IM_1D misalign bytes and split workgroups (#32673)
184862801 gemma4: Optimized prompt processing for multi-seq queries (#32342)
79e81b0bd ui: voice messages and dictation with live waveforms and transcripts (#32531)
059cac284 ui: search message content and Discover models from the search dialog (#32670)
cf4153a9b ui: publish llama-ui as an alias of @ggml-org/llama-ui (#32667)
8e7862411 tts : forward -t to the mtmd context (#32664)
e626db7ca server-bench : fix TypeError in histogram generation (#32518)
c6a25fc62 ui: load highlight.js languages on demand (#32661)
5f837145d server: add more audio tests (#32579)
36cd3aff4 server: add --ui-mcp-proxy-allow-private-urls (#32633)
28de970cc ui : focus the chat form when typing with nothing focused (#32570)
4b69c79cc cuda : update GDN supports_op check (#32660)
a1f422260 model : load ffn_gate_up_exps scales (#32657)
4783b1145 llama : move the indexer key rotation choice into the model classes (#32653)
6abcbe5d3 remove ui-lib publish verification step (#32658)
b81aa847c ui: slim the design tokens and set all text through type roles (#32615)
9d6f04fa9 ui: show vision as glasses and audio as headphones (#32617)
652d559ed llama : move the graph node budget into the model classes (#32648)
6aee50801 ui: set the reasoning effort from the model picker (#32632)
55b8d8d89 ui: full-screen diagram preview that zooms around what is on screen, inert diagrams (#32591)
4c4a0f0a4 llama : reserve graph nodes for the MoE cache (#32636)
55d323507 model: add Domyn Edge 4B Model (#32559)
bed8ec2f8 llamafile(s390x): add QK data type support (#32600)
52e8db655 kleidiai : allow OHOS (HarmonyOS) AArch64 target (#32265)
d7d1b632d webgpu : fix 2D indexing for copy kernel (#32576)
ea84d7090 CUDA: optimize Orin single-column MMVQ (#31268)
9fbe30c2a CUDA: keep the MUL_MAT_ID precision in the per-expert fallback (#31345)
c0b97be0b vulkan: optimize RMS_NORM_MUL_ROPE loop control (#31149)
16f80bd0c vulkan: chunked GATED_DELTA_NET implementation (#30207)
2d8d00393 webgpu : add COL2IM_1D support (#31708)
7e960f40f opencl: fold GQA head for f16 FA for better efficiency (#32631)
8bf88ba93 vulkan: disable subgroup arithmetic on Qualcomm's driver (#30826)
b94959a64 CUDA: implement support for duplicate expert IDs (#32505)
50518b64c model : hrm : do not compute slot count as uint32_t (#32601)
c406f4367 opencl: support dp4a for KQ mm in decomposed FA (#32577)
7fce5439f ggml : add BF16 support to ROPE and SET_ROWS (CPU, CUDA) (#32387)
53ecea05a mtmd : fix YuE2 projector loading (#32606)
9a080f44b ggml-openvino: fix OpenVINO CI, minor fixes and optimizations (#32590)
c7468107e cuda: Scatter kernel for set_n (#32489)
ac830a9cb ggml : add backend scheduler tests (#27258)
8af68d486 llama: fixes for Inkling 2 attention mask (#32429)
f8caa5ea3 metal : fix the second argument of NSMakeRange (#32602)
4db8b7638 webgpu: add POOL_2D support (#32250)
01592dc58 llama : remove redundant fields from llm_graph_params (#32596)
8bf2132c3 readme : fix release badge (#32597)
5812201a8 ci : fix build-opencl.yml (#32594)
41d8297fe metal : CONV_2D tensor API for M5, split-K for all chips (#32542)
51a77c4f2 qwen3vl : set t_layer_inp for EAGLE-3 (#32589)
76f186df7 ggml : IQ2 creation speedup through caching (#31910)
95b09b62b llama : remove PATH_MAX (#32557)
b5dbca1e4 ci : use LLVM 22 (#32565)
80437488a ui: cut Llama Chat's first-load JavaScript by 63%, load diagrams, math and PDFs on demand (#32555)
39039aa27 llama : fall back to buffered I/O on EIO (#32545)
7a4117eef vulkan : enable MMQ with mixed signedness integer dots (#31045)
573aa89de vulkan: Implement stream-k MUL_MAT (#28528)
ecafc6714 vulkan: use floating-point zero for storage-only FP16 in DIAG/TRI (#32379)
d4f5c2604 CUDA: use 64-bit dst offsets in mul_mat_q (#32374)
08c252e22 opencl: allow adjusting KV padding in decomposed FA (#32522)
e4b620af1 mtmd: support voxcpm2 (#32443)
b001d7bb2 ggml : WASM Relaxed SIMD Enhancement (#19590)
0a7675746 llama : fix sticky NaN in recurrent state (#31913)
b04489040 server: fix sleep state for v1/realtime (#32567)
78e05298f model : limite: reject mudd configs that index past mudd_tap_idx on load (#32562)
785f6bac0 ui : keep streaming reasoning box inside the viewport when zoomed (#31966)
edec462cc ggml, ci : use llvm 22.1.8 (#32548)
4483b2b98 vendor : update cpp-httplib-0.67.0 [no ci] (#32563)
bafa0420c server : enable packing for d1-2B and d1-Omni-2B models (#32553)
2cbfc3cf3 [CUDA] : Add SKU-aware FP16/BF16 accumulation precision gating for NVIDIA GPUs (#30672)
6f311d7ad webgpu: (fix CI) allow the FA mask to be broadcast over the Q batch (#32535)
ff6b8d176 ggml-cpu : use all threads for large GET_ROWS (#32514)
98d67c8d5 model:add Zaya1 8B (Zyphra) (#32071)
387395aa8 ui: install @ggml-org/llama-brand from npm (#32544)
a693a5f66 ui: llama-chat publish drops the registry check, bin paths without ./ (#32543)
b069e526d gguf-py : fix tensor offset overflow in GGUFReader (#32495)
ffc87c3a7 ui: soften the action card border and show the split-button divider in dark mode (#32538)
10f173b25 ui: hide Models and MCP behind settings, off by default (#32527)
97069ff6c ui: run Llama Chat with npx @ggml-org/llama-chat (#32524)
bba840882 Add LLAMA_MOE_RANDOM_ROUTING=1 for benchmark-only random expert selection (#29539)
48a32194e server: fix transcription prompt for v1/realtime (#32507)
6da36139e ui: run the Storybook deploy on HF Jobs, with a token that can write the Space (#32525)
61f182fcd unicode : add continuation check lambda (#31070)
03ec5b432 cuda : fuse NORM + MUL (+ ADD) (#32454)
7144124a5 vocab : extract bpe_rank loading into function (#30962)
43bd7a2a4 vulkan: add bfloat16 support to various ops (#32202)
65758d01f ui: Storybook follow-ups: generated DESIGN.md tokens, shared helpers and one Llama Mono (#32523)
a300a9c33 cuda : increase Pascal DP4A MMQ I tile for J=64 (#31352)
4577932fa ggml-openvino: expand model support, optimize NPU,GPU and memory usage (#32172)
398f00d65 CUDA: use MMQ for MoE on V100 (#32504)
9e93cd800 ui: a Storybook for Llama UI and Llama Chat (#32485)
aaa807c56 cuda: decode the conv2d patch indices with fastdiv (#32492)
401563f10 vulkan: run rms_norm with a runtime loop count on Qualcomm (#30824)
52975342f server: slot_sched: fix lora and recurrent (#32434)
3574df84b mtmd: support tiny-voca (#32427)
2e53a0bab ggml-cuda: hip: Tune stream_k algo and mmq configs to use stream_k on AMD GCN (#30022)
744c68cd1 ui: publish @ggml-org/llama-ui from CI, and release 0.4.0 (#32480)
307e3f155 mtmd: add kokoro tts support (#32413)
9048bad8d cuda: use the implicit GEMM conv2d path for F32 kernels (#32482)
a9d43ecc3 opencl: add A7 Q5_K non-MoE binary kernel (#31002)
8c16babba mtmd: Add support for Qwen3-TTS' ICL/reference mode (#32438)
ad9d9e8f5 qwen4exp : fix graph reallocation from the n-gram table scale (#32483)
955c4e8ee server : return 400 when grammar and ignore_eos are on (#32377)
10152bc4a ggml-cuda: disable quantized matvec fusion on all Pascal GPUs (#32239)
8777c0c83 Title: CUDA: few-row MMQ for MUL_MAT_ID (#32065)
918076a63 ui: turn the live markdown preview off by default (#32469)
ebc9fb933 CUDA: use block reductions for whole-row pool_1d (#31855)
8b8ca4c98 ggml : decode F8_E4M3 to fp32 without ldexpf (#32477)
08a9b3589 llama : keep the k-pool layout prefix on sequence edits (#32137)
acad5e405 vocab : speed up PLaMo-2/3 tokenizer table build (#32249)
d3064fddc convert : fix FP8 qwen4exp checkpoints (n-gram table scale, block-scaled FP8) (#32476)
7f106b545 ui: Llama UI design system: tokens, surfaces and fonts (#32468)
d92ea9bb1 mtmd: support Minimax-Music3 (#32435)
8d1599fca chat: add tts_dict for kokoro G2P template (#32397)
054a1babf Rotate  K/V read order for better L2 cache hit rates (#32407)
513ad7ae0 ui: turn conversation tabs off by default (#32402)
67cf8967e ui: move Llama Chat to SvelteKit 3 and its built-in service worker (#32463)
4df3f2959 qwen3next : apply output projection weight scale (#32393)
a49db739f cuda : raise shared mem limit only for the launched kernel (#32392)
eada89c31 nix: expose a SYCL package (#31066)
8f647f1fd vulkan: disable flip Flash Attention shader on AMD Windows due to a driver bug (#32415)
dde9de82c sycl : Fix FA mkl issue: a mask broadcast over heads or batches (#31536)
e0a9118fe metal : add implicit GEMM kernel for CONV_2D (#28069)
140a27987 webgpu : Implement timestep embedding (#31695)
c145db272 webgpu : use f32 while dequantizing to avoid FTZ (#32140)
ede610678 opencl: support f16 and non-contig f32 silu (#32319)
9214bdb55 sycl: use fast division in bin-bcast kernels (#32213)
d3c3e242c opencl: add A7 Q8_0 non-MoE binary kernel (#31003)
9581154a2 mtmd : fix Muse Glimmer vision embedding order (#32433)
1ef8c5d68 convert : respect max_position_embeddings for granite hybrid (#32436)
e8fbcad85 tests: print the exception message in test-llama-context (#32428)
95e837aaf skills: explicitly specify paths to README-dev.md (#32431)
d998c676f convert: Fix inkling 2 mmproj conversion (#32430)
92192d31e mtmd: support YuE2-3B (#32369)
ad5cbfa91 opencl: add A7 Q4_K non-MoE binary kernel (#30948)
d261e49e7 opencl: fix three defects of the bin flash-attention prefill path (#32110)
4ddf2b947 chat : implement inkling parser (#32381)
4303cd94a contributing: mark agents.md and code-review as required (#32416)
c7518dbec MMVQ: Tune ne11 Gate for RDNA3_5 (#32308)
a68c6136b mtmd: support fish audio s2 (#32330)
3a7660371 ui: move the web UI to ui/apps/chat and call it Llama Chat (#32032)
e8698ac16 fix:- Misc. bug: Settings/Tools is lying about tool picks inside a ch… (#32223)
7804be063 arg : allow up to llama_max_devices() configs for --tensor-split and --fit-target (#13293) (#31435)
ef6bc6f36 jinja: impl scope-chain key lookup (#32396)
a06044b93 llama : deprecate old batch API (#32306)
62a6d3a30 llama : migrate to `llama_batch_ext` (#32356)
ef3848f9d vulkan: Support split_k for conv3d. (#29929)
47fe13331 HIP/CUDA: enable GDN mma kernel on CDNA (#31327)
301db6337 vulkan: fix Nvidia fp32 FA shmem overflow, disable shmem staging if it takes too much memory (#32244)
a001af915 hip: add gfx1013 to rdna1 (#32236)
164ab018f webgpu: support per-head flash attention masks (#32394)
5cb951679 readme : fix line endings
8bfd64b5a readme : update (#32382)
e1925b369 jinja: support json sort_keys=true (#32366)
95db855bc ci : use vX.Y.Z tags as docker tags (#32388)
1d2e880ba vulkan : fix 32-bit compilation (#32275)
adf554d23 vulkan: make the radix top-k tie selection deterministic (#31931)
6b01a4767 CI: trigger spec dec testing for relevant PRs (#32281)
f477c1b90 cuda : fix MUL_MAT_ID abort with odd src0 columns on AMD (#32385)
21fa9c043 kv-cells: avoid an O(n_cells) scan per sequence removal (#32380)
a946eb541 server: answer reasoning_effort levels the template rejects with 400 (#32332)
05db09a4d ggml-cuda: fix MoE regression on HIP with #29948 (#32344)
9fba51d2c convert: fix ripple dflash2 NoPE metadata (#32363)
b4c0e00a4 jinja: add 4 missing features (#32352)
1719dbb0e server : skip MCP discovery for router children (#32359)
fc504f91d mtmd: support higgs v3 STT and vibevoice-ASR (#32329)
18b74fa41 model : read qwen3vl output head size from the tensor (#32349)
7ae3c6b23 mtmd: add zonos3-mini TTS model (#32020)
f4d067391 Revert "jinja: add 4 missing features"
a681a53b6 jinja: add 4 missing features
75fd7f9ec docs: move per-model TTS to /docs, refer it from other pages (#32304)
a68799c60 model: support MiniMax-M3.1 (#32301)
56fd8a375 server : ignore empty stop strings (#32093)
b54752df4 ggml-cpu: add x86 VNNI Q2_0 dot product (#26348)
900f01ba0 CI/HIP: update fattn symbol names in hip-quality-check (#32331)
de32b268c Support DFLASH2 for Recursive Ripple-65B-Preview (#31904)
4e5116f47 server : fix output_config.effort being dropped in /v1/messages (#32321)
278a89cb7 CUDA/HIP: Refactor the use of _sync warp primitives (#31617)
dd099a6bf chat: fix inkling 2 begin/end of image tokens placement (#32294)
73f53317e vendor: sync stb_image (#32305)
429460dc0 server: refactor, add server_slot_sched, prompt running hash (#32154)
58a4a6b49 server : clear slot cache when the global lora config changes (#30367)
5a4afd807 tests: Fail `test-backend-ops` and exit with error status 1 when missing and/or unsupported types and/or unsupported backends are provided in the command line (#30279)
6d3568e31 opencl: add A7 Q6_K non-MoE binary kernel (#30949)
e574a17b0 model : metal : workaround fusion for LFM3 (#32296)
5c008e000 feat: add Inkling 2 support (text + vision) (#32217)
9f26fe11c common : reject out-of-range grammar_triggers type instead of aborting (#30835) (#31478)
cf9a9957d server : Fix connection reuse after streamed responses (#30492)
dca216ad6 hexagon: add TIMESTEP_EMBEDDING HVX kernel (#32228)
f8cc5774e memory : fix non-consecutive position warning for M-RoPE (#32287)
acf5d5456 llamafile: introduce more Q0 quant support for s390x (#32203)
3e41ae69d llama : allocate the tensor staging buffer from the CPU buffer type (#31438)
3bc612fe2 vulkan: Explicitly include SPIRV-Headers (#31416)
d8f30a5b6 vulkan: optimize prompt processing Flash Attention for RDNA3 and RDNA4 (#31323)
e96417565 cuda : keep columns in registers for cooperative softmax (#28982)
d20426bbb vulkan: optimize matrix multiplication for narrow N (#31990)
19f31e61b vulkan: use GPU copies on UMA with uncached memory on Intel (#32024)
07037ba13 sycl : optimize mtmd image processing (#32109)
0cc522e45 chat : allow undeclared tool calls in LFM2 tool-call grammar (#32164)
f08bca8a4 docs : add OpenVINO backend to ops matrix (#32259)
3c311796f chat : allow tool calls inside reasoning blocks for Ministral-3 (#32271)
8b4ac2496 common : fix infinite recursion in debug build for peg parser dump (#32282)
1ae047c92 opencl: fixes for q4_k mv oob access, f16 swiglu_oai, cpy with strided dst, batched group_norm and bf16 sigmoid (#32251)
1c2adc75f chat : allow Gemma4 tool call during thought (#32232)
a956a852c Fix ctz64 on 32bit (#32273)
c6c0ec6d5 hexagon: fix fa no-mask tail (#32243)
d0764c5ee qwen2vl : apply FFN weight scales (#32241)
3549c274d convert : register Granite4VisionForConditionalGeneration for text (#32237)
c56be864f ggml-backend : start a new split at an incompatible weight in a split without inputs (#31775)
a9a5d216e convert : pplx-decider must match qwen3.5 model_type (#32156)
9d925e7c0 mtmd: fix video pixel aspect ratio and video rotation (#32267)
e3483e40b mtmd : allow custom video decoder (#32188)
4f2187e73 jinja : reduce template rendering overhead (#32023)
0cce7580b mtmd : avoid padding-only Whisper audio chunks (#30403)
32bdc3a89 spec + model: refactor DFlash based speculative decoding methods  (#32016)
61dbf4922 Hexagon: add support for IQ2_XXS and NVFP4 (#31954)
9d25e0014 chat : remove mistral workaround (#32230)
9183a552e metal : fix mul_mv destination offset overflow (#32221)
ded522f83 hexagon: add support for SSM_SCAN op (#31921)
5193ef1d4 ui: configure allow-remote=root in .npmrc for npm 12+ (#32158) (#32196)
4df9b4797 ci: reduce qdc timeouts to avoid stalling pipelines and runners (#32148)
b79696f1f ggml-cuda: hip: tune GCN MMQ configs (#30021)
4f9dfa0e3 requirements, Fix CI: support Python 3.15 (#32199)
9daa0aa22 hexagon: improve buffer allocations and mappings (mmap stacking) (#32144)
fe14cad51 CUDA: add SM103 SASS to non-native builds (#30099)
31953bcf7 ggml : add BF16 support to RMS_NORM (CPU, CUDA) (#32135)
ae93877c8 vulkan: add TOP_K_MASK (#31544)
7874988b4 spec : Warn when --spec-draft-p-min is used with probabilistic draft sampling (#31294)
8c2c4c39c ggml-vulkan: add optional device keepalive (#29267)
108f73adf grammar : optimize matching with left factoring (#29557)
951d465f5 llama: move moe-cache code out of llama-graph (#32157)
2d8a32502 CUDA: split the PAD_REFLECT_1D grid to stay within the HIP grid limit (#32179)

## 笔记


