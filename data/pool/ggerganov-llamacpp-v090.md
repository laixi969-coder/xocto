---
slug: ggerganov-llamacpp-v090
name: 'ggerganov/llama.cpp: v0.9.0'
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
url: https://github.com/ggml-org/llama.cpp/releases/tag/v0.9.0
canonical_url: https://github.com/ggml-org/llama.cpp/releases/tag/v0.9.0
summary: "## Overview\r\n\r\nThis release adds OCP FP8 E4M3 quantization support, a new `flash_attn_ext_rows`\
  \ op that makes the unified KV cache efficient for multi-sequence inference, and a generic batched tensor\
  \ copy API. Four new architectures are supported (Clover, Limite, Metis-1.6 and Mistral Large 4), audio\
  \ generation and transcription expand with Chatterbox TTS, Nemotron 3.5 Transcribe and predefined Pocket\
  \ TTS voices, and the Gemma 4 E2B/E4B models get major prefill optimizations. `ggml` is updated to v0.29.0,\
  \ bringing FP8 E4M3, flash attention rows, NCCL-based multi-node tensor parallelism and performance\
  \ work across the CPU, CUDA, SYCL, Metal, Vulkan, OpenCL and Hexagon backends. The server and UI receive\
  \ a round of fixes and refinements.\r\n\r\n### Highlights\r\n\r\n- Quant: OCP FP8 E4M3 tensor type (saturating\
  \ mode) with conversion helpers and a new ftype ([#27512](https://github.com/ggml-org/llama.cpp/pull/27512))\r\
  \n- llama: `flash_attn_ext_rows` - more efficient unified KV for multi-seq, restoring non-unified KV\
  \ prefill performance ([#29510](https://github.com/ggml-org/llama.cpp/pull/29510))\r\n- ggml: batched\
  \ tensor copy API (`ggml_backend_tensor_copy_n`/`set_n`/`get_n`) superseding the `_2d` API, implemented\
  \ for Metal and CUDA ([#30881](https://github.com/ggml-org/llama.cpp/pull/30881))\r\n\r\n- For a 3rd\
  \ year in a row, `llama.cpp` is a featured repo in the [Github Octoverse report](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/):\r\
  \n\r\n  <img width=\"1920\" height=\"1080\" alt=\"image\" src=\"https://github.com/user-attachments/assets/1ac82af7-576f-487b-bba3-2b56bb641022\"\
  \ />\r\n\r\n\r\n### API changes\r\n\r\n- llama.h: add `LLAMA_FTYPE_MOSTLY_F8_E4M3` ([#27512](https://github.com/ggml-org/llama.cpp/pull/27512))\r\
  \n- mtmd.h: add `MTMD_GEN_AUDIO_TYPE_CHATTERBOX` and `n_voices` to `mtmd_gen_audio_info` ([#30993](https://github.com/ggml-org/llama.cpp/pull/30993))\r\
  \n- mtmd.h: add predefined-voice APIs: `mtmd_gen_audio_voice_name()`, `mtmd_gen_audio_get_voice()`,\
  \ `mtmd_gen_state_set_ref()` ([#30993](https://github.com/ggml-org/llama.cpp/pull/30993))\r\n- mtmd.h:\
  \ add `mtmd_bitmap_is_voice()` and `mtmd_gen_audio_read_tensor()` ([#30993](https://github.com/ggml-org/llama.cpp/pull/30993))\r\
  \n- mtmd.h: add `MTMD_VIDEO_TEMPLATE_QWEN3VL` video prompt template ([#31619](https://github.com/ggml-org/llama.cpp/pull/31619))\r\
  \n- server: `GET /props` reports the model's predefined TTS `voices`; the TTS endpoint accepts predefined\
  \ voice names ([#30993](https://github.com/ggml-org/llama.cpp/pull/30993))\r\n- server: `/v1/responses`\
  \ now merges `extra_params` (seed, min_p, ...) into the converted chat-completions response ([#30959](https://github.com/ggml-org/llama.cpp/pull/30959))\r\
  \n\r\n### New models\r\n\r\n- Clover-35B-A3B-Preview diffusion model, AR mode ([#31306](https://github.com/ggml-org/llama.cpp/pull/31306))\r\
  \n- Limite 1B - Violetto ([#29433](https://github.com/ggml-org/llama.cpp/pull/29433))\r\n- Metis-1.6\
  \ (Praxis ~2.9B and Logos ~10.2B): hybrid Mamba-2 / GQA attention with fixed-depth recurrence and LatentMoE\
  \ ([#31134](https://github.com/ggml-org/llama.cpp/pull/31134))\r\n- Mistral Large 4 ([#31376](https://github.com/ggml-org/llama.cpp/pull/31376))\r\
  \n\r\n### Core changes\r\n\r\n- gemma4: graph optimizations with massive prefill gains for E2B and E4B\
  \ ([#31356](https://github.com/ggml-org/llama.cpp/pull/31356)); create `token_embd` before the tied\
  \ output in gemma3n and gemma4 ([#31394](https://github.com/ggml-org/llama.cpp/pull/31394))\r\n- LFM3:\
  \ enable NVFP4 GGUFs ([#31608](https://github.com/ggml-org/llama.cpp/pull/31608)), enable tensor split\
  \ ([#31431](https://github.com/ggml-org/llama.cpp/pull/31431)), quantize the audio codec decoder ([#31386](https://github.com/ggml-org/llama.cpp/pull/31386))\r\
  \n- spec dec: save and restore MTP hidden state in context checkpoints ([#30141](https://github.com/ggml-org/llama.cpp/pull/30141))\
  \ and record LFM3 layer inputs ([#31598](https://github.com/ggml-org/llama.cpp/pull/31598))\r\n- dflash:\
  \ copy hidden features via device copies ([#31506](https://github.com/ggml-org/llama.cpp/pull/31506));\
  \ qwen4exp: write the conv state tail without an intermediate cont ([#31443](https://github.com/ggml-org/llama.cpp/pull/31443))\r\
  \n- model loading: reuse the tensor staging buffer and skip the direct-IO bounce buffer ([#31321](https://github.com/ggml-org/llama.cpp/pull/31321))\r\
  \n- kv-cache: keep Hadamard rotation constants on the GPU ([#31073](https://github.com/ggml-org/llama.cpp/pull/31073))\
  \ and fix attention tensor rotation in layers with shared KV ([#31406](https://github.com/ggml-org/llama.cpp/pull/31406))\r\
  \n- kv-cache: never return 0 `kv_rows` for sequences without cells ([#31570](https://github.com/ggml-org/llama.cpp/pull/31570))\
  \ and refuse rollbacks past the snapshots of the last ubatch ([#31368](https://github.com/ggml-org/llama.cpp/pull/31368))\r\
  \n- Gemma4 MTP assistant: follow `ctx_other` devices and flash-attention setting ([#31635](https://github.com/ggml-org/llama.cpp/pull/31635));\
  \ DSV4: remove simple batch splitting ([#31300](https://github.com/ggml-org/llama.cpp/pull/31300))\r\
  \n- chat: strip the qwen3-coder think block with `reasoning_format none` ([#31380](https://github.com/ggml-org/llama.cpp/pull/31380))\
  \ and end reasoning budget forcing on a prompt end tag ([#31374](https://github.com/ggml-org/llama.cpp/pull/31374))\r\
  \n- chat: allow a constraint type after the gpt-oss final channel ([#31556](https://github.com/ggml-org/llama.cpp/pull/31556));\
  \ common: fix `-hf` tag matching inside longer quant names ([#31620](https://github.com/ggml-org/llama.cpp/pull/31620))\
  \ and bound control vector layer indices ([#31336](https://github.com/ggml-org/llama.cpp/pull/31336))\r\
  \n- tools: reject mismatched shards in GGUF split merge ([#31579](https://github.com/ggml-org/llama.cpp/pull/31579)),\
  \ fix `imatrix --nextn` crash ([#31522](https://github.com/ggml-org/llama.cpp/pull/31522)), fix `gguf-py`\
  \ `np_roundf` dropping the sign ([#31310](https://github.com/ggml-org/llama.cpp/pull/31310))\r\n- vendor:\
  \ miniaudio 0.11.26 ([#31459](https://github.com/ggml-org/llama.cpp/pull/31459)) and cpp-httplib 0.64.0\
  \ ([#31400](https://github.com/ggml-org/llama.cpp/pull/31400)); embed an app manifest in all Windows\
  \ executables ([#31329](https://github.com/ggml-org/llama.cpp/pull/31329))\r\n\r\n### Multi-modality\
  \ changes\r\n\r\n- add Chatterbox TTS support ([#30993](https://github.com/ggml-org/llama.cpp/pull/30993))\r\
  \n- add Nemotron 3.5 Transcribe support: offline transcription in 40 languages with prompt context and\
  \ speaker attribution ([#31471](https://github.com/ggml-org/llama.cpp/pull/31471))\r\n- Pocket TTS:\
  \ support predefined voices without voice cloning ([#31429](https://github.com/ggml-org/llama.cpp/pull/31429))\r\
  \n- accurate support for the qwen3-vl video prompt format ([#31619](https://github.com/ggml-org/llama.cpp/pull/31619))\r\
  \n- resize Gemma 4 images without letterbox padding ([#30922](https://github.com/ggml-org/llama.cpp/pull/30922))\
  \ and fix InternVL CLS token order ([#30886](https://github.com/ggml-org/llama.cpp/pull/30886))\r\n\r\
  \n### Server changes\r\n\r\n- cap shared decision prefixes at the first output ([#30710](https://github.com/ggml-org/llama.cpp/pull/30710))\r\
  \n- restore the speculative checkpoint for drafts longer than `n_rs_seq` ([#31350](https://github.com/ggml-org/llama.cpp/pull/31350))\r\
  \n\r\n### UI changes\r\n\r\n- add MCP group checkboxes in the tools settings ([#31303](https://github.com/ggml-org/llama.cpp/pull/31303))\
  \ and request persistent storage on startup ([#31299](https://github.com/ggml-org/llama.cpp/pull/31299))\r\
  \n- keep chats at the bottom until the reader scrolls up ([#31311](https://github.com/ggml-org/llama.cpp/pull/31311))\
  \ and show the submit button when the input has content ([#31324](https://github.com/ggml-org/llama.cpp/pull/31324))\r\
  \n- reveal the collapsed sidebar from its logo ([#31307](https://github.com/ggml-org/llama.cpp/pull/31307))\
  \ and align alert dialog styling ([#31312](https://github.com/ggml-org/llama.cpp/pull/31312))\r\n- keep\
  \ queued steering messages in their own conversation ([#31304](https://github.com/ggml-org/llama.cpp/pull/31304))\
  \ and show an interrupted state for tool calls that never returned ([#31314](https://github.com/ggml-org/llama.cpp/pull/31314))\r\
  \n- disable model deletion the server would refuse ([#31305](https://github.com/ggml-org/llama.cpp/pull/31305))\
  \ and prefer a loading model in pre-selection ([#31326](https://github.com/ggml-org/llama.cpp/pull/31326))\r\
  \n- add a Playwright harness for recording demo videos ([#31318](https://github.com/ggml-org/llama.cpp/pull/31318))\
  \ and run local browser tests in installed Chrome ([#31596](https://github.com/ggml-org/llama.cpp/pull/31596))\r\
  \n\r\n### ggml changes\r\n\r\n- [v0.29.0](https://github.com/ggml-org/ggml/releases/tag/v0.29.0): ggml\
  \ v0.29.0 adds an OCP FP8 E4M3 tensor type, a new `ggml_flash_attn_ext_rows` op where each query slice\
  \ attends to its own list of K/V rows, a batched tensor copy API, and initial support for multi-node\
  \ tensor parallelism through a new multi-process communicator interface. Core improvements include bounding\
  \ tensor views by the bytes their strides reach, zero-copy GGUF export of host-buffer tensors, and `vm_allocate`-based\
  \ allocations on Apple platforms. Performance work spans all major backends: new SVE kernels in the\
  \ CPU backend, DPAS flash attention for quantized KV in SYCL, fused MoE MMQ in CUDA, faster MXFP4 mat-vec\
  \ in Metal, split-K tuning in Vulkan, and a large expansion of quantized GEMM/GEMV coverage in OpenCL.\
  \ The Hexagon backend gains support for several new ops, including the lightning indexer, top-k mask,\
  \ conv2d and upscale.\r\n\r\n## Assets\r\n\r\n**Nightly build:** [b12110](https://github.com/ggml-org/llama.cpp/releases/tag/b12110)\r\
  \n\r\n## More info\r\n\r\n- [Releases and versioning of `ggml-org` projects](https://github.com/ggml-org/ggml/discussions/1579)\r\
  \n\r\n## Changelog since [v0.8.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.8.0)\r\n\r\n\
  cd959bae9 llama.cpp : bump version to 0.9.0 (#31646)\r\n13ec8f614 sync : ggml\r\ncca14f64f ggml : bump\
  \ version to 0.29.0 (ggml/1680)\r\ne853ec9a8 llama : follow ctx_other devices and flash attention in\
  \ Gemma4 assistant (#31635)\r\nfeaf80006 ggml : Gate RVV code on the target extension (#31607)\r\n4c4ca5b18\
  \ common : do not allow `_` in sidecar (#31639)\r\n162e2bb2e ggml : fix bf16 (#31609)\r\n6900fb5ac opencl:\
  \ improve q2_0 GEMV for Adreno (#31577)\r\nbbb02c93e ggml: bound views by the bytes their strides reach\
  \ (#31584)\r\n960b1d51b ggml : write host-buffer tensor data directly in gguf writer (#31144)\r\n4b29d0262\
  \ common : fix -hf tag matching inside longer quant names (#31620)\r\nbee23322f hexagon: add LIGHTNING_INDEXER\
  \ support (#31289)\r\n149f5641b mtmd: accurate support for qwen3-vl video prompt format (#31619)\r\n\
  b97627967 model, mtmd: add chatterbox TTS support (#30993)\r\n7071ba378 hexagon: add TOP_K_MASK op (#31552)\r\
  \n6cb3e672e gemma4: graph optimizations (massive gains on pp for E2B and E4B) (#31356)\r\n6b9c0cfcb\
  \ hexagon: faster TOP_K for the backend sampler (#31279)\r\nd1c4e5bec ui: run local browser tests in\
  \ installed Chrome with its sandbox on (#31596)\r\n20a51f24a hexagon: add DSV4_HC_PRE and DSV4_HC_POST\
  \ ops (#30953)\r\n0f35d6d7b spec : save and restore MTP hidden state (#30141)\r\na464960ed ggml-zdnn:\
  \ fix fattn test failure (#31583)\r\n9309bf1bc model : Add support for Metis-1.6 models (#31134)\r\n\
  d1044bc82 model : enable NVFP4 LFM3 ggufs (#31608)\r\n28b812d6c mtmd : add Nemotron 3.5 Transcribe support\
  \ (#31471)\r\n749db7f03 qwen4exp: write the conv state tail without an intermediate cont (#31443)\r\n\
  0943ca547 ui: add Playwright harness for recording demo videos (#31318)\r\nf9448cddc model : record\
  \ layer inputs in LFM3 for spec dec (#31598)\r\n0978a6e90 ggml: avoid signed overflow in ggml_roll bounds\
  \ check (#30375)\r\n0ef27309b conversion : use original model tensor names in _flush_nvfp4_experts (#31427)\r\
  \n8fc037672 cuda: potential fix for Q8_1 correction sum (#31247)\r\n740251a92 cuda : gather batched\
  \ tensor reads into mapped host memory (PR to master) (#31391)\r\n71efc559a Add nccl support for multi-node\
  \ tensor parallelism (#28967)\r\n19e8a86fe tools : reject mismatched shards in GGUF split merge (#31579)\r\
  \n259d91709 meta: support GLM-5.3 next sm tensor (#30499)\r\n36ee3caf7 metal : fix cpy kernel for dst\
  \ non-contiguous in dim 0 (#31581)\r\nfac3a894f vulkan: skip maxStorageBufferRange pre-check for non-compute\
  \ tensors (#31114)\r\nb74298c10 delta_net_base: refactor conv state (#30878)\r\n37b0f9c36 vulkan: fix\
  \ out-of-bounds NVFP4 UE4M3 scale lookup (#31079)\r\nca8daad19 llama : drop the redundant cnv from llm_attn_mask\
  \ (#31558)\r\n0f663d247 dsv4.1: fix llama-context tests with partial offload (#31292)\r\n00f113ece cuda\
  \ : prevent premature eviction of graphs about to be used (#30662)\r\ne6192de0a opencl: add initial\
  \ iq4_xs support (#31339)\r\n4402e6540 chat : allow constraint type after gpt-oss final channel (#31556)\r\
  \n74101b3cd ci : update the HIP VGPR spill ignore list for the kv_rows FA kernel argument (#31550)\r\
  \n713319e28 webgpu: add ARANGE support (#31455)\r\nee17f293b kv-cache : never return 0 kv_rows for sequences\
  \ without cells (#31570)\r\n51fe42c5d hexagon: tiled hvx permute (#31446)\r\n2cbca389f dflash: copy\
  \ hidden features via device copies (#31506)\r\n29c720eaf docs: update s390x build docs (#31546)\r\n\
  d02b4c0d6 mtmd: Pocket tts - support for voices without voice cloning (#31429)\r\ne4b6c8ca6 model: add\
  \ Clover support (#31306)\r\n1b6935b22 llama : flash_attn_ext_rows - more efficient unified kv for multi-seq\
  \ (#29510)\r\n3f8af15a7 imatrix : fix --nextn crash (#31522)\r\ncd8427d01 context : simplify setters\
  \ (#29730)\r\n6b00d5627 readme : fix links in README.md for maintainer PRs (#31487)\r\n458fcfc34 docs:\
  \ CANN backend supports BF16 on 910B, document GGML_CANN_NO_PINNED (#31249)\r\n6ed812057 ggml-zdnn:\
  \ share buffers with host (#31481)\r\nea24b952c ggml : use `vm_allocate` instead of `posix_memalign`\
  \ on all Apple platforms (#31437)\r\n84d9ce0fa opencl: add topk_mask (#31441)\r\ndcbb09167 vulkan: add\
  \ tensor-parallel allreduce function (#25051)\r\n07ec7c8af vulkan: improve small-n split-K selection\
  \ on RDNA3 and RDNA4 (#30146)\r\ncb02250b5 vulkan: avoid redundant scans when zeroing skipped rows (#31266)\r\
  \n2c93f0b6e sycl : fast ggml_sycl_comm_exchange() on Intel Arc Pro B70s  (#30956)\r\n5e18eb021 sycl:\
  \ dmmv code cleanup (#31325)\r\n5c2ea1ab1 ui: disable model deletion the server would refuse (#31305)\r\
  \n23426d797 ui: align alert dialog styling with other overlay surfaces (#31312)\r\n90080ce09 ui: keep\
  \ queued steering messages in their own conversation (#31304)\r\n64be95b16 ui: show interrupted state\
  \ for tool calls that never returned (#31314)\r\nb12b405c1 ui: don't reload a loading model on select,\
  \ prefer it in pre-selection (#31326)\r\naac6da801 docs : fix Vulkan example command in build.md (#31530)\r\
  \n00ef13664 tests : merge identical if branches (#31523)\r\n59695669f jinja : implement map('filter')\
  \ (#24033)\r\na7a490a49 ggml : fix clang-cl build with AVX512 BF16 (#31276)\r\nf72dc3092 docs: fix Huawei\
  \ ascend brand (#31463)\r\nfcfe4b59d requirements : minor adjustments for python 3.14 wheels (#31534)\r\
  \n4e910a86e cmake : add explicit thread linkage (#31414)\r\n1c5ed702c webgpu : fix CI by keeping scratch\
  \ alloc sizes monotonic in batch length (#31422)\r\n785322d17 requirements : fix numpy dependencies\
  \ (#31508)\r\ndde879bc4 sycl: Try PkgConfig for LevelZero includes / libs (#31076)\r\n060b2fea4 opencl:\
  \ add initial iq3 support (#31338)\r\na91eab67d hexagon : fix DMA transfers with strides > 24 bits (#31442)\r\
  \nd5ef408e2 mtmd : fix InternVL CLS token order (#30886)\r\n79bce0c88 tests : enable Gemma 4 in `test-llama-archs`\
  \ (#31401)\r\nbc428e407 llama : enable tensor split for LFM3 (#31431)\r\nf6312ad75 vendor : update miniaudio\
  \ to 0.11.26 (#31459)\r\n0138937e3 llama : fix rotation of attention tensors in layers with shared KV\
  \ (#31406)\r\nddf48f85c reshaping so mm on 2d instead of 3d tensor for lfm sc (#30831)\r\nf3586e66b\
  \ server: cap shared decision prefixes at the first output (#30710)\r\n2871678a1 server : fix /v1/responses\
  \ endpoint to accept extra_params (#30959)\r\n7bd180830 mtmd : resize Gemma 4 images without letterbox\
  \ padding (#30922)\r\n0ec4027a2 opencl: add fwht (#31434)\r\n1052f7e1d chat : strip the think block\
  \ in the qwen3-coder with reasoning_format none (#31380)\r\n8956c769e sycl: fix f32 to q2_0/q4_0/q5_0\
  \ rounding in CPY (#31120)\r\n5047748f1 rpc : delete fs_path_to_utf8() (#31424)\r\n792fcf4e7 opencl:\
  \ add initial iq1 support (#31341)\r\na34de8618 common : delete fs_path_to_utf8() (#31423)\r\naa588a346\
  \ common : drop the Windows argv reconstruction (#31417)\r\n889f2ec96 quant : allow quantization for\
  \ LFM3-Audio codec decoder (#31386)\r\n1ab23c33b vendor : update cpp-httplib to 0.64.0 (#31400)\r\n\
  27b8464e8 ci : add missing ccache-clear to windows behavior check (#31413)\r\nd63fbfe79 cmake : embed\
  \ an app manifest in all Windows exes (#31329)\r\ne216f4ec8 ci : extract most apple jobs into daily\
  \ workflow (#31408)\r\n344846b4f gemma3n, gemma4 : create token_embd before the tied output (#31394)\r\
  \nfb5997274 kv-cache : keep rotation constants on the GPU (#31073)\r\nab3768cdc memory: refuse rollbacks\
  \ past the snapshots of the last ubatch (#31368)\r\ne0f142d5d opencl: add initial q2_0 support (#31340)\r\
  \n3c809f443 common : end reasoning budget forcing on an end tag from the prompt (#31374)\r\n36a0e2ffc\
  \ sycl: FLASH_ATTN_EXT failures (#30761)\r\n418f905a4 ggml : add batched tensor copy API (#30881)\r\n\
  eb4e244be ROCm/HIP: add RDNA4_M family for gfx1170/gfx1171 (#31373)\r\n68d20b884 Quant: OCP FP8 E4M3\
  \ support (#27512)\r\n0893ec98f skills: specify rule about ggml_build_forward_expand (#31375)\r\n78feec062\
  \ model: mistral le chonk (#31376)\r\n0ac1a7fd3 llama : reuse the tensor staging buffer and skip the\
  \ direct-io bounce buffer (#31321)\r\n7df8b876b server : restore the spec checkpoint for drafts longer\
  \ than n_rs_seq (#31350)\r\n8ab29faec ui: keep chats at the bottom until the reader scrolls up (#31311)\r\
  \nf5d4d7541 ui: show submit button when the chat input has content (#31324)\r\n3ed915e30 ui: reveal\
  \ the collapsed sidebar from its logo and toggle it there (#31307)\r\nf8fcef254 ui: add MCP group checkboxes\
  \ in tools settings and fix indeterminate checkbox colors (#31303)\r\nb7cde589e ui: request persistent\
  \ storage on startup (#31299)\r\n3dd0f60bb doc: update ops for opencl (#31347)\r\n78febbad9 HIP/CUDA:\
  \ enable sparse attn on CDNA (#31259)\r\nabb76ab38 model : Support Limite 1B - Violetto (#29433)\r\n\
  41be0bdc9 common: select A100 cores for SpaceMiT default threads (#30284)\r\n22183e51f opencl: initial\
  \ support for iq2 (#31267)\r\n6d194531e metal : faster MXFP4 mat-vec, full threadgroups for unary/binary/GLU\
  \ (#31075)\r\nfade717ed tests : remove duplicate FA test cases added in #31125 (#31357)\r\nc9daee149\
  \ ggml-metal : fix unary kernels compile on older Metal toolchains (#31360)\r\n8a199ad31 hexagon: support\
  \ for UPSCALE op (#31331)\r\nda6c30ade hexagon: improve DDR bw utilization in transposed CONCAT (#31277)\r\
  \nf7c01c522 [SYCL] add DPAS flash attention kernel for quantized KV cache (#31125)\r\nbf48103ad sycl\
  \ : vectorize reordered-layout dequantization stores (Q4_0, K-quants, IQ3, MXFP4) (#30976)\r\n6d5ac3c8d\
  \ tests : fix comp_padding CUDA graph reservation (#31344)\r\n7ac5727d6 ggml-openvino: slice view inputs\
  \ of SCALE (#31334)\r\n2e0d86beb Hexagon: IM2COL improvement - block based HVX parallelization (#31050)\r\
  \ne09a78a25 tests: fix CI flakes in server cancel and sleep tests (#31330)\r\n369dcf309 ggml-cpu: add\
  \ SVE implementation of ggml_gemv_q8_0_4x8_q8_0 (#30585)\r\nd0ff6317c docs : fix DSpark confidence threshold\
  \ flag name (--spec-draft-p-min) (#31178)\r\ncf24317be common, mtmd: bound control vector layer indices\
  \ and M-RoPE position loops (#31336)\r\n74a4fb003 opencl: add tiled q4_k GEMM for adreno (#30412)\r\n\
  522021325 hexagon: add conv2d support (#30995)\r\nc3df4b7e2 Speed up IQ4 quant creation with pre-computed\
  \ halfway points (#31201)\r\nac8e1694d ggml-cpu: SVE 256 bit implementation of gemm_q6_K_8x8_q8_K kernel\
  \ (#27472)\r\nc02b5c641 ggml-cpu: SVE 256-bit Implementation of mxfp4 gemv kernel (#28141)\r\nff0d396e3\
  \ ci(s390x): switch to Ubuntu 26.04 runners (#31317)\r\n838093f19 llama : remove simple batch splitting\
  \ for DSV4 (#31300)\r\n604cc4302 codeowners : refresh teams and maintainer PRs link (#31316)\r\n39febd2ad\
  \ sycl: work-group argmax for short TOP_K rows (#31110)\r\nf5222f25c cuda: fuse MoE (MUL_MAT_ID) gate/up\
  \ and GLU in MMQ (#31188)\r\n28cb47c7c gguf-py: fix np_roundf dropping the sign (#31310)"
first_seen: '2026-11-05T02:29:39Z'
last_seen: '2026-11-06T02:26:55Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ggml-org/llama.cpp/releases/tag/v0.9.0
  seen_at: '2026-11-06T02:26:55Z'
  metrics:
    reactions: 45
  kind: news
---

# ggerganov/llama.cpp: v0.9.0

## Overview

This release adds OCP FP8 E4M3 quantization support, a new `flash_attn_ext_rows` op that makes the unified KV cache efficient for multi-sequence inference, and a generic batched tensor copy API. Four new architectures are supported (Clover, Limite, Metis-1.6 and Mistral Large 4), audio generation and transcription expand with Chatterbox TTS, Nemotron 3.5 Transcribe and predefined Pocket TTS voices, and the Gemma 4 E2B/E4B models get major prefill optimizations. `ggml` is updated to v0.29.0, bringing FP8 E4M3, flash attention rows, NCCL-based multi-node tensor parallelism and performance work across the CPU, CUDA, SYCL, Metal, Vulkan, OpenCL and Hexagon backends. The server and UI receive a round of fixes and refinements.

### Highlights

- Quant: OCP FP8 E4M3 tensor type (saturating mode) with conversion helpers and a new ftype ([#27512](https://github.com/ggml-org/llama.cpp/pull/27512))
- llama: `flash_attn_ext_rows` - more efficient unified KV for multi-seq, restoring non-unified KV prefill performance ([#29510](https://github.com/ggml-org/llama.cpp/pull/29510))
- ggml: batched tensor copy API (`ggml_backend_tensor_copy_n`/`set_n`/`get_n`) superseding the `_2d` API, implemented for Metal and CUDA ([#30881](https://github.com/ggml-org/llama.cpp/pull/30881))

- For a 3rd year in a row, `llama.cpp` is a featured repo in the [Github Octoverse report](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/):

  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1ac82af7-576f-487b-bba3-2b56bb641022" />


### API changes

- llama.h: add `LLAMA_FTYPE_MOSTLY_F8_E4M3` ([#27512](https://github.com/ggml-org/llama.cpp/pull/27512))
- mtmd.h: add `MTMD_GEN_AUDIO_TYPE_CHATTERBOX` and `n_voices` to `mtmd_gen_audio_info` ([#30993](https://github.com/ggml-org/llama.cpp/pull/30993))
- mtmd.h: add predefined-voice APIs: `mtmd_gen_audio_voice_name()`, `mtmd_gen_audio_get_voice()`, `mtmd_gen_state_set_ref()` ([#30993](https://github.com/ggml-org/llama.cpp/pull/30993))
- mtmd.h: add `mtmd_bitmap_is_voice()` and `mtmd_gen_audio_read_tensor()` ([#30993](https://github.com/ggml-org/llama.cpp/pull/30993))
- mtmd.h: add `MTMD_VIDEO_TEMPLATE_QWEN3VL` video prompt template ([#31619](https://github.com/ggml-org/llama.cpp/pull/31619))
- server: `GET /props` reports the model's predefined TTS `voices`; the TTS endpoint accepts predefined voice names ([#30993](https://github.com/ggml-org/llama.cpp/pull/30993))
- server: `/v1/responses` now merges `extra_params` (seed, min_p, ...) into the converted chat-completions response ([#30959](https://github.com/ggml-org/llama.cpp/pull/30959))

### New models

- Clover-35B-A3B-Preview diffusion model, AR mode ([#31306](https://github.com/ggml-org/llama.cpp/pull/31306))
- Limite 1B - Violetto ([#29433](https://github.com/ggml-org/llama.cpp/pull/29433))
- Metis-1.6 (Praxis ~2.9B and Logos ~10.2B): hybrid Mamba-2 / GQA attention with fixed-depth recurrence and LatentMoE ([#31134](https://github.com/ggml-org/llama.cpp/pull/31134))
- Mistral Large 4 ([#31376](https://github.com/ggml-org/llama.cpp/pull/31376))

### Core changes

- gemma4: graph optimizations with massive prefill gains for E2B and E4B ([#31356](https://github.com/ggml-org/llama.cpp/pull/31356)); create `token_embd` before the tied output in gemma3n and gemma4 ([#31394](https://github.com/ggml-org/llama.cpp/pull/31394))
- LFM3: enable NVFP4 GGUFs ([#31608](https://github.com/ggml-org/llama.cpp/pull/31608)), enable tensor split ([#31431](https://github.com/ggml-org/llama.cpp/pull/31431)), quantize the audio codec decoder ([#31386](https://github.com/ggml-org/llama.cpp/pull/31386))
- spec dec: save and restore MTP hidden state in context checkpoints ([#30141](https://github.com/ggml-org/llama.cpp/pull/30141)) and record LFM3 layer inputs ([#31598](https://github.com/ggml-org/llama.cpp/pull/31598))
- dflash: copy hidden features via device copies ([#31506](https://github.com/ggml-org/llama.cpp/pull/31506)); qwen4exp: write the conv state tail without an intermediate cont ([#31443](https://github.com/ggml-org/llama.cpp/pull/31443))
- model loading: reuse the tensor staging buffer and skip the direct-IO bounce buffer ([#31321](https://github.com/ggml-org/llama.cpp/pull/31321))
- kv-cache: keep Hadamard rotation constants on the GPU ([#31073](https://github.com/ggml-org/llama.cpp/pull/31073)) and fix attention tensor rotation in layers with shared KV ([#31406](https://github.com/ggml-org/llama.cpp/pull/31406))
- kv-cache: never return 0 `kv_rows` for sequences without cells ([#31570](https://github.com/ggml-org/llama.cpp/pull/31570)) and refuse rollbacks past the snapshots of the last ubatch ([#31368](https://github.com/ggml-org/llama.cpp/pull/31368))
- Gemma4 MTP assistant: follow `ctx_other` devices and flash-attention setting ([#31635](https://github.com/ggml-org/llama.cpp/pull/31635)); DSV4: remove simple batch splitting ([#31300](https://github.com/ggml-org/llama.cpp/pull/31300))
- chat: strip the qwen3-coder think block with `reasoning_format none` ([#31380](https://github.com/ggml-org/llama.cpp/pull/31380)) and end reasoning budget forcing on a prompt end tag ([#31374](https://github.com/ggml-org/llama.cpp/pull/31374))
- chat: allow a constraint type after the gpt-oss final channel ([#31556](https://github.com/ggml-org/llama.cpp/pull/31556)); common: fix `-hf` tag matching inside longer quant names ([#31620](https://github.com/ggml-org/llama.cpp/pull/31620)) and bound control vector layer indices ([#31336](https://github.com/ggml-org/llama.cpp/pull/31336))
- tools: reject mismatched shards in GGUF split merge ([#31579](https://github.com/ggml-org/llama.cpp/pull/31579)), fix `imatrix --nextn` crash ([#31522](https://github.com/ggml-org/llama.cpp/pull/31522)), fix `gguf-py` `np_roundf` dropping the sign ([#31310](https://github.com/ggml-org/llama.cpp/pull/31310))
- vendor: miniaudio 0.11.26 ([#31459](https://github.com/ggml-org/llama.cpp/pull/31459)) and cpp-httplib 0.64.0 ([#31400](https://github.com/ggml-org/llama.cpp/pull/31400)); embed an app manifest in all Windows executables ([#31329](https://github.com/ggml-org/llama.cpp/pull/31329))

### Multi-modality changes

- add Chatterbox TTS support ([#30993](https://github.com/ggml-org/llama.cpp/pull/30993))
- add Nemotron 3.5 Transcribe support: offline transcription in 40 languages with prompt context and speaker attribution ([#31471](https://github.com/ggml-org/llama.cpp/pull/31471))
- Pocket TTS: support predefined voices without voice cloning ([#31429](https://github.com/ggml-org/llama.cpp/pull/31429))
- accurate support for the qwen3-vl video prompt format ([#31619](https://github.com/ggml-org/llama.cpp/pull/31619))
- resize Gemma 4 images without letterbox padding ([#30922](https://github.com/ggml-org/llama.cpp/pull/30922)) and fix InternVL CLS token order ([#30886](https://github.com/ggml-org/llama.cpp/pull/30886))

### Server changes

- cap shared decision prefixes at the first output ([#30710](https://github.com/ggml-org/llama.cpp/pull/30710))
- restore the speculative checkpoint for drafts longer than `n_rs_seq` ([#31350](https://github.com/ggml-org/llama.cpp/pull/31350))

### UI changes

- add MCP group checkboxes in the tools settings ([#31303](https://github.com/ggml-org/llama.cpp/pull/31303)) and request persistent storage on startup ([#31299](https://github.com/ggml-org/llama.cpp/pull/31299))
- keep chats at the bottom until the reader scrolls up ([#31311](https://github.com/ggml-org/llama.cpp/pull/31311)) and show the submit button when the input has content ([#31324](https://github.com/ggml-org/llama.cpp/pull/31324))
- reveal the collapsed sidebar from its logo ([#31307](https://github.com/ggml-org/llama.cpp/pull/31307)) and align alert dialog styling ([#31312](https://github.com/ggml-org/llama.cpp/pull/31312))
- keep queued steering messages in their own conversation ([#31304](https://github.com/ggml-org/llama.cpp/pull/31304)) and show an interrupted state for tool calls that never returned ([#31314](https://github.com/ggml-org/llama.cpp/pull/31314))
- disable model deletion the server would refuse ([#31305](https://github.com/ggml-org/llama.cpp/pull/31305)) and prefer a loading model in pre-selection ([#31326](https://github.com/ggml-org/llama.cpp/pull/31326))
- add a Playwright harness for recording demo videos ([#31318](https://github.com/ggml-org/llama.cpp/pull/31318)) and run local browser tests in installed Chrome ([#31596](https://github.com/ggml-org/llama.cpp/pull/31596))

### ggml changes

- [v0.29.0](https://github.com/ggml-org/ggml/releases/tag/v0.29.0): ggml v0.29.0 adds an OCP FP8 E4M3 tensor type, a new `ggml_flash_attn_ext_rows` op where each query slice attends to its own list of K/V rows, a batched tensor copy API, and initial support for multi-node tensor parallelism through a new multi-process communicator interface. Core improvements include bounding tensor views by the bytes their strides reach, zero-copy GGUF export of host-buffer tensors, and `vm_allocate`-based allocations on Apple platforms. Performance work spans all major backends: new SVE kernels in the CPU backend, DPAS flash attention for quantized KV in SYCL, fused MoE MMQ in CUDA, faster MXFP4 mat-vec in Metal, split-K tuning in Vulkan, and a large expansion of quantized GEMM/GEMV coverage in OpenCL. The Hexagon backend gains support for several new ops, including the lightning indexer, top-k mask, conv2d and upscale.

## Assets

**Nightly build:** [b12110](https://github.com/ggml-org/llama.cpp/releases/tag/b12110)

## More info

- [Releases and versioning of `ggml-org` projects](https://github.com/ggml-org/ggml/discussions/1579)

## Changelog since [v0.8.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.8.0)

cd959bae9 llama.cpp : bump version to 0.9.0 (#31646)
13ec8f614 sync : ggml
cca14f64f ggml : bump version to 0.29.0 (ggml/1680)
e853ec9a8 llama : follow ctx_other devices and flash attention in Gemma4 assistant (#31635)
feaf80006 ggml : Gate RVV code on the target extension (#31607)
4c4ca5b18 common : do not allow `_` in sidecar (#31639)
162e2bb2e ggml : fix bf16 (#31609)
6900fb5ac opencl: improve q2_0 GEMV for Adreno (#31577)
bbb02c93e ggml: bound views by the bytes their strides reach (#31584)
960b1d51b ggml : write host-buffer tensor data directly in gguf writer (#31144)
4b29d0262 common : fix -hf tag matching inside longer quant names (#31620)
bee23322f hexagon: add LIGHTNING_INDEXER support (#31289)
149f5641b mtmd: accurate support for qwen3-vl video prompt format (#31619)
b97627967 model, mtmd: add chatterbox TTS support (#30993)
7071ba378 hexagon: add TOP_K_MASK op (#31552)
6cb3e672e gemma4: graph optimizations (massive gains on pp for E2B and E4B) (#31356)
6b9c0cfcb hexagon: faster TOP_K for the backend sampler (#31279)
d1c4e5bec ui: run local browser tests in installed Chrome with its sandbox on (#31596)
20a51f24a hexagon: add DSV4_HC_PRE and DSV4_HC_POST ops (#30953)
0f35d6d7b spec : save and restore MTP hidden state (#30141)
a464960ed ggml-zdnn: fix fattn test failure (#31583)
9309bf1bc model : Add support for Metis-1.6 models (#31134)
d1044bc82 model : enable NVFP4 LFM3 ggufs (#31608)
28b812d6c mtmd : add Nemotron 3.5 Transcribe support (#31471)
749db7f03 qwen4exp: write the conv state tail without an intermediate cont (#31443)
0943ca547 ui: add Playwright harness for recording demo videos (#31318)
f9448cddc model : record layer inputs in LFM3 for spec dec (#31598)
0978a6e90 ggml: avoid signed overflow in ggml_roll bounds check (#30375)
0ef27309b conversion : use original model tensor names in _flush_nvfp4_experts (#31427)
8fc037672 cuda: potential fix for Q8_1 correction sum (#31247)
740251a92 cuda : gather batched tensor reads into mapped host memory (PR to master) (#31391)
71efc559a Add nccl support for multi-node tensor parallelism (#28967)
19e8a86fe tools : reject mismatched shards in GGUF split merge (#31579)
259d91709 meta: support GLM-5.3 next sm tensor (#30499)
36ee3caf7 metal : fix cpy kernel for dst non-contiguous in dim 0 (#31581)
fac3a894f vulkan: skip maxStorageBufferRange pre-check for non-compute tensors (#31114)
b74298c10 delta_net_base: refactor conv state (#30878)
37b0f9c36 vulkan: fix out-of-bounds NVFP4 UE4M3 scale lookup (#31079)
ca8daad19 llama : drop the redundant cnv from llm_attn_mask (#31558)
0f663d247 dsv4.1: fix llama-context tests with partial offload (#31292)
00f113ece cuda : prevent premature eviction of graphs about to be used (#30662)
e6192de0a opencl: add initial iq4_xs support (#31339)
4402e6540 chat : allow constraint type after gpt-oss final channel (#31556)
74101b3cd ci : update the HIP VGPR spill ignore list for the kv_rows FA kernel argument (#31550)
713319e28 webgpu: add ARANGE support (#31455)
ee17f293b kv-cache : never return 0 kv_rows for sequences without cells (#31570)
51fe42c5d hexagon: tiled hvx permute (#31446)
2cbca389f dflash: copy hidden features via device copies (#31506)
29c720eaf docs: update s390x build docs (#31546)
d02b4c0d6 mtmd: Pocket tts - support for voices without voice cloning (#31429)
e4b6c8ca6 model: add Clover support (#31306)
1b6935b22 llama : flash_attn_ext_rows - more efficient unified kv for multi-seq (#29510)
3f8af15a7 imatrix : fix --nextn crash (#31522)
cd8427d01 context : simplify setters (#29730)
6b00d5627 readme : fix links in README.md for maintainer PRs (#31487)
458fcfc34 docs: CANN backend supports BF16 on 910B, document GGML_CANN_NO_PINNED (#31249)
6ed812057 ggml-zdnn: share buffers with host (#31481)
ea24b952c ggml : use `vm_allocate` instead of `posix_memalign` on all Apple platforms (#31437)
84d9ce0fa opencl: add topk_mask (#31441)
dcbb09167 vulkan: add tensor-parallel allreduce function (#25051)
07ec7c8af vulkan: improve small-n split-K selection on RDNA3 and RDNA4 (#30146)
cb02250b5 vulkan: avoid redundant scans when zeroing skipped rows (#31266)
2c93f0b6e sycl : fast ggml_sycl_comm_exchange() on Intel Arc Pro B70s  (#30956)
5e18eb021 sycl: dmmv code cleanup (#31325)
5c2ea1ab1 ui: disable model deletion the server would refuse (#31305)
23426d797 ui: align alert dialog styling with other overlay surfaces (#31312)
90080ce09 ui: keep queued steering messages in their own conversation (#31304)
64be95b16 ui: show interrupted state for tool calls that never returned (#31314)
b12b405c1 ui: don't reload a loading model on select, prefer it in pre-selection (#31326)
aac6da801 docs : fix Vulkan example command in build.md (#31530)
00ef13664 tests : merge identical if branches (#31523)
59695669f jinja : implement map('filter') (#24033)
a7a490a49 ggml : fix clang-cl build with AVX512 BF16 (#31276)
f72dc3092 docs: fix Huawei ascend brand (#31463)
fcfe4b59d requirements : minor adjustments for python 3.14 wheels (#31534)
4e910a86e cmake : add explicit thread linkage (#31414)
1c5ed702c webgpu : fix CI by keeping scratch alloc sizes monotonic in batch length (#31422)
785322d17 requirements : fix numpy dependencies (#31508)
dde879bc4 sycl: Try PkgConfig for LevelZero includes / libs (#31076)
060b2fea4 opencl: add initial iq3 support (#31338)
a91eab67d hexagon : fix DMA transfers with strides > 24 bits (#31442)
d5ef408e2 mtmd : fix InternVL CLS token order (#30886)
79bce0c88 tests : enable Gemma 4 in `test-llama-archs` (#31401)
bc428e407 llama : enable tensor split for LFM3 (#31431)
f6312ad75 vendor : update miniaudio to 0.11.26 (#31459)
0138937e3 llama : fix rotation of attention tensors in layers with shared KV (#31406)
ddf48f85c reshaping so mm on 2d instead of 3d tensor for lfm sc (#30831)
f3586e66b server: cap shared decision prefixes at the first output (#30710)
2871678a1 server : fix /v1/responses endpoint to accept extra_params (#30959)
7bd180830 mtmd : resize Gemma 4 images without letterbox padding (#30922)
0ec4027a2 opencl: add fwht (#31434)
1052f7e1d chat : strip the think block in the qwen3-coder with reasoning_format none (#31380)
8956c769e sycl: fix f32 to q2_0/q4_0/q5_0 rounding in CPY (#31120)
5047748f1 rpc : delete fs_path_to_utf8() (#31424)
792fcf4e7 opencl: add initial iq1 support (#31341)
a34de8618 common : delete fs_path_to_utf8() (#31423)
aa588a346 common : drop the Windows argv reconstruction (#31417)
889f2ec96 quant : allow quantization for LFM3-Audio codec decoder (#31386)
1ab23c33b vendor : update cpp-httplib to 0.64.0 (#31400)
27b8464e8 ci : add missing ccache-clear to windows behavior check (#31413)
d63fbfe79 cmake : embed an app manifest in all Windows exes (#31329)
e216f4ec8 ci : extract most apple jobs into daily workflow (#31408)
344846b4f gemma3n, gemma4 : create token_embd before the tied output (#31394)
fb5997274 kv-cache : keep rotation constants on the GPU (#31073)
ab3768cdc memory: refuse rollbacks past the snapshots of the last ubatch (#31368)
e0f142d5d opencl: add initial q2_0 support (#31340)
3c809f443 common : end reasoning budget forcing on an end tag from the prompt (#31374)
36a0e2ffc sycl: FLASH_ATTN_EXT failures (#30761)
418f905a4 ggml : add batched tensor copy API (#30881)
eb4e244be ROCm/HIP: add RDNA4_M family for gfx1170/gfx1171 (#31373)
68d20b884 Quant: OCP FP8 E4M3 support (#27512)
0893ec98f skills: specify rule about ggml_build_forward_expand (#31375)
78feec062 model: mistral le chonk (#31376)
0ac1a7fd3 llama : reuse the tensor staging buffer and skip the direct-io bounce buffer (#31321)
7df8b876b server : restore the spec checkpoint for drafts longer than n_rs_seq (#31350)
8ab29faec ui: keep chats at the bottom until the reader scrolls up (#31311)
f5d4d7541 ui: show submit button when the chat input has content (#31324)
3ed915e30 ui: reveal the collapsed sidebar from its logo and toggle it there (#31307)
f8fcef254 ui: add MCP group checkboxes in tools settings and fix indeterminate checkbox colors (#31303)
b7cde589e ui: request persistent storage on startup (#31299)
3dd0f60bb doc: update ops for opencl (#31347)
78febbad9 HIP/CUDA: enable sparse attn on CDNA (#31259)
abb76ab38 model : Support Limite 1B - Violetto (#29433)
41be0bdc9 common: select A100 cores for SpaceMiT default threads (#30284)
22183e51f opencl: initial support for iq2 (#31267)
6d194531e metal : faster MXFP4 mat-vec, full threadgroups for unary/binary/GLU (#31075)
fade717ed tests : remove duplicate FA test cases added in #31125 (#31357)
c9daee149 ggml-metal : fix unary kernels compile on older Metal toolchains (#31360)
8a199ad31 hexagon: support for UPSCALE op (#31331)
da6c30ade hexagon: improve DDR bw utilization in transposed CONCAT (#31277)
f7c01c522 [SYCL] add DPAS flash attention kernel for quantized KV cache (#31125)
bf48103ad sycl : vectorize reordered-layout dequantization stores (Q4_0, K-quants, IQ3, MXFP4) (#30976)
6d5ac3c8d tests : fix comp_padding CUDA graph reservation (#31344)
7ac5727d6 ggml-openvino: slice view inputs of SCALE (#31334)
2e0d86beb Hexagon: IM2COL improvement - block based HVX parallelization (#31050)
e09a78a25 tests: fix CI flakes in server cancel and sleep tests (#31330)
369dcf309 ggml-cpu: add SVE implementation of ggml_gemv_q8_0_4x8_q8_0 (#30585)
d0ff6317c docs : fix DSpark confidence threshold flag name (--spec-draft-p-min) (#31178)
cf24317be common, mtmd: bound control vector layer indices and M-RoPE position loops (#31336)
74a4fb003 opencl: add tiled q4_k GEMM for adreno (#30412)
522021325 hexagon: add conv2d support (#30995)
c3df4b7e2 Speed up IQ4 quant creation with pre-computed halfway points (#31201)
ac8e1694d ggml-cpu: SVE 256 bit implementation of gemm_q6_K_8x8_q8_K kernel (#27472)
c02b5c641 ggml-cpu: SVE 256-bit Implementation of mxfp4 gemv kernel (#28141)
ff0d396e3 ci(s390x): switch to Ubuntu 26.04 runners (#31317)
838093f19 llama : remove simple batch splitting for DSV4 (#31300)
604cc4302 codeowners : refresh teams and maintainer PRs link (#31316)
39febd2ad sycl: work-group argmax for short TOP_K rows (#31110)
f5222f25c cuda: fuse MoE (MUL_MAT_ID) gate/up and GLU in MMQ (#31188)
28cb47c7c gguf-py: fix np_roundf dropping the sign (#31310)

## 笔记


