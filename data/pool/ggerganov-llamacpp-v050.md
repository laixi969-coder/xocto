---
slug: ggerganov-llamacpp-v050
name: 'ggerganov/llama.cpp: v0.5.0'
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
url: https://github.com/ggml-org/llama.cpp/releases/tag/v0.5.0
canonical_url: https://github.com/ggml-org/llama.cpp/releases/tag/v0.5.0
summary: "## Overview\r\n\r\nThis release focuses on backend performance and correctness, broader model\
  \ coverage, and more robust server/router operation. It adds HRM-Text (DFM Mimir 1B) support, MiMo-V2.6\
  \ and HunyuanOCR conversion support, ggml 0.25.0 backend improvements, multi-address HTTP binding, image\
  \ outputs from function calls, and several chat parser/UI fixes.\r\n\r\n### Highlights\r\n\r\n- Accelerate\
  \ CUDA `conv2d` with implicit GEMM ([#29135](https://github.com/ggml-org/llama.cpp/pull/29135))\r\n\
  - Add Metal MoE and SSM_CONV fusion optimizations ([#28948](https://github.com/ggml-org/llama.cpp/pull/28948))\r\
  \n- Allow the server to bind to multiple addresses ([#28690](https://github.com/ggml-org/llama.cpp/pull/28690))\r\
  \n\r\n### API changes\r\n\r\n- Add `llama_adapter_lora_init_from_file_ptr()` for loading LoRA from an\
  \ open FILE ([#28993](https://github.com/ggml-org/llama.cpp/pull/28993))\r\n- Document `llama_model_load_from_file_ptr()`\
  \ as reading from the current position and requiring aligned mmap ([#28993](https://github.com/ggml-org/llama.cpp/pull/28993))\r\
  \n- Add `LLAMA_VOCAB_TYPE_TEST` dummy tokenizer ([#29084](https://github.com/ggml-org/llama.cpp/pull/29084))\r\
  \n- Add `input_image` support to server function-call outputs ([#22575](https://github.com/ggml-org/llama.cpp/pull/22575))\r\
  \n- Allow `--host` to accept comma-separated TCP addresses and UNIX sockets ([#28690](https://github.com/ggml-org/llama.cpp/pull/28690))\r\
  \n\r\n### New models\r\n\r\n- Add HRM-Text / DFM Mimir 1B support ([#27625](https://github.com/ggml-org/llama.cpp/pull/27625))\r\
  \n- Add MiMo-V2.6 conversion support ([#29257](https://github.com/ggml-org/llama.cpp/pull/29257))\r\n\
  - Add DFlash support for HunyuanOCR ([#28890](https://github.com/ggml-org/llama.cpp/pull/28890))\r\n\
  - Extend Nemotron MTP and Nemotron-H model handling ([#29018](https://github.com/ggml-org/llama.cpp/pull/29018),\
  \ [#28989](https://github.com/ggml-org/llama.cpp/pull/28989))\r\n- Add Qwen4Exp hyper-connection ops\
  \ and sparse flash attention ([#28901](https://github.com/ggml-org/llama.cpp/pull/28901), [#28770](https://github.com/ggml-org/llama.cpp/pull/28770))\r\
  \n- Add `--fuse-qkv` support for Muse Glimmer ([#29203](https://github.com/ggml-org/llama.cpp/pull/29203))\r\
  \n\r\n### Core changes\r\n\r\n- Add graph input/input-tensor diagnostics during scheduler reserve ([#26625](https://github.com/ggml-org/llama.cpp/pull/26625))\r\
  \n- Enable CUDA graphs for MTP drafting ([#28549](https://github.com/ggml-org/llama.cpp/pull/28549))\r\
  \n- Fix tensor-parallel split state/granularity for fused QKV models ([#28965](https://github.com/ggml-org/llama.cpp/pull/28965))\r\
  \n- Fix Mamba time-step projection input contiguity ([#28832](https://github.com/ggml-org/llama.cpp/pull/28832))\r\
  \n- Write the SWA pattern in the model saver and round-trip 15 more architectures ([#29042](https://github.com/ggml-org/llama.cpp/pull/29042))\r\
  \n- Add environment variables for temperature, top-p, min-p and penalties ([#27380](https://github.com/ggml-org/llama.cpp/pull/27380))\r\
  \n- Reduce the sampler backend probe size ([#29285](https://github.com/ggml-org/llama.cpp/pull/29285))\r\
  \n- Add Ling 3.0, DeepSeek V3.2/V4, qwen3-coder, Muse Glimmer and Gemma 4 parser fixes ([#28682](https://github.com/ggml-org/llama.cpp/pull/28682),\
  \ [#29008](https://github.com/ggml-org/llama.cpp/pull/29008), [#28869](https://github.com/ggml-org/llama.cpp/pull/28869),\
  \ [#29242](https://github.com/ggml-org/llama.cpp/pull/29242), [#29115](https://github.com/ggml-org/llama.cpp/pull/29115))\r\
  \n- Improve JSON Schema and PEG handling ([#28518](https://github.com/ggml-org/llama.cpp/pull/28518),\
  \ [#29127](https://github.com/ggml-org/llama.cpp/pull/29127), [#29161](https://github.com/ggml-org/llama.cpp/pull/29161))\r\
  \n- Add ufakzeka pre-tokenizer and `llama-bench --version` ([#29033](https://github.com/ggml-org/llama.cpp/pull/29033),\
  \ [#28971](https://github.com/ggml-org/llama.cpp/pull/28971))\r\n\r\n### Multi-modality changes\r\n\r\
  \n- Add sanity checks for mtmd layer indices, SAM layer counts, resize targets and graph allocation\
  \ ([#29276](https://github.com/ggml-org/llama.cpp/pull/29276), [#28149](https://github.com/ggml-org/llama.cpp/pull/28149))\r\
  \n- Fix SigLIP bucket buffer overrun for tall/wide images ([#29276](https://github.com/ggml-org/llama.cpp/pull/29276))\r\
  \n\r\n### Server changes\r\n\r\n- Fix router eviction races and child process lifecycle handling ([#29217](https://github.com/ggml-org/llama.cpp/pull/29217))\r\
  \n- Do not pass log file or API key file to router-spawned children ([#29212](https://github.com/ggml-org/llama.cpp/pull/29212),\
  \ [#28938](https://github.com/ggml-org/llama.cpp/pull/28938))\r\n- Improve startup and model-source\
  \ logging ([#29125](https://github.com/ggml-org/llama.cpp/pull/29125))\r\n- Update vendored cpp-httplib\
  \ to 0.57.1 ([#29239](https://github.com/ggml-org/llama.cpp/pull/29239))\r\n\r\n### UI changes\r\n\r\
  \n- Accept WEBM video files ([#28622](https://github.com/ggml-org/llama.cpp/pull/28622))\r\n- Add close\
  \ button to UI toasts ([#28246](https://github.com/ggml-org/llama.cpp/pull/28246))\r\n- Fix mobile breakpoint\
  \ and content overflow issues, including horizontal table scrolling ([#29108](https://github.com/ggml-org/llama.cpp/pull/29108))\r\
  \n- Restore the reasoning menu in single-model desktop mode ([#27985](https://github.com/ggml-org/llama.cpp/pull/27985))\r\
  \n- Stop re-probing a disabled `/tools` endpoint on every message ([#28646](https://github.com/ggml-org/llama.cpp/pull/28646))\r\
  \n\r\n### ggml changes\r\n\r\n- Updated ggml to v0.25.0 ([release](https://github.com/ggml-org/ggml/releases/tag/v0.25.0))\r\
  \n- The release expands hyper-connection, flash-attention, and fused MoE/SSM support across backends,\
  \ with robustness, quantization, data-layout, and RPC/meta improvements.\r\n- API changes include gated\
  \ `ggml_dsv4_hc_pre_gated()`, optional `ggml_dsv4_hc_post()` comb, and RPC protocol major v7.\r\n\r\n\
  ## Assets\r\n\r\n**Nightly build:** [b11146](https://github.com/ggml-org/llama.cpp/releases/tag/b11146)\r\
  \n\r\n## More info\r\n\r\n- [Releases and versioning of `ggml-org` projects](https://github.com/ggml-org/ggml/discussions/1579)\r\
  \n\r\n## Changelog since [v0.4.1](https://github.com/ggml-org/llama.cpp/releases/tag/v0.4.1)\r\n\r\n\
  7fe450e19 llama.cpp : bump version to 0.5.0 (#29333)\r\n177cd8cc7 sync : ggml\r\ne4e2f6232 ggml : bump\
  \ version to 0.25.1 (ggml/1637)\r\n66fba63af CUDA: add a reserve to avoid spurious warning on older\
  \ GCC builds (#29317)\r\nbddf8263c common : keep HF cache dir as path, expose UTF-8 only for logs (#29320)\r\
  \n957538960 metal: add the missing f32 x bf16 mul_mv variants (#28741)\r\ndc9879cf6 CUDA: enable sparse-fa\
  \ for dsv4 prefill (again) (#29298)\r\n42916d83f server: fix token counting API crash on sleep (#29309)\r\
  \n4e416ee73 jinja : parse unary +/- before variables (#29244)\r\nee3ecce05 metal : key the fa-vec tuned\
  \ table by family instead of SKU (#29075)\r\n057494f93 server: accept OpenAI video_url content type\
  \ and data: video URIs (#27921)\r\nbcbc936a8 server: Dedup the draft HF model via dedup-cache-models\
  \ (#27934)\r\n26758d38f ci : fix build-cmake runner target (#29299)\r\n18f9f7bef model-conversion :\
  \ add causal-compare-logits recipe (#29305)\r\n633733d0a model : support Gemma4 DSpark draft backbone\
  \ (#29226)\r\n86b2daa73 ci : run python (jinja) test (#29302)\r\n183d2a04c make-release : update summary\
  \ prompt\r\n45062d405 sync : ggml\r\n503549c5f ggml : bump version to 0.25.0 (ggml/1635)\r\ne97545d91\
  \ sycl : fix compile warnings\r\nb1ff4ca23 vulkan: add IQ4_XS MMQ/MMV matmul kernels (#28415)\r\n94256114c\
  \ ggml-meta: resolve multi buffer views (#29266)\r\n1a679828f cuda: top-k MoE should always fire (#28432)\r\
  \n384a534ce sycl : support new UT case for mul_mat_hadamard fp16 (#29218)\r\n5e48b3100 sycl: extend\
  \ MMVQ GLU fusion, add rms_norm+scale and ssm_conv+silu fusions (#28931)\r\n4d7d7703f sycl : support\
  \ op get_rows_back, only support fp32/fp16 (#25266)\r\n08b1d2aea vulkan: hide internal symbols to prevent\
  \ duplicate-dlopen state destruction (#29139)\r\n441df11f6 sampler: reduce the size of the probe (#29285)\r\
  \ne6ab7c1a4 hex-dma: introduce direct-mapped DMA cache that is better suited for HVX FA mask handling\
  \ (#29282)\r\nf46bc30cb HIP : optimize IQ2/IQ3 (`__vsub4` `__vcmpne4`) using SWAR (#27962)\r\n709fe755d\
  \ jinja : fix dangling reference warning in for_statement (#29279)\r\nd5f66492e opencl: add bin kernel\
  \ `kernel_gemm_noshuffle_q4_k_q8_1_dp4a_ila_a8_bin` (#29056)\r\n991991118 server: fix router eviction\
  \ races with the existing queue (#29217)\r\nbbf99b1b3 server: do not pass log file to children (#29212)\r\
  \n4098fdc92 server: support input_image in function_call_output (#20663) (#22575)\r\n4ceb17191 vulkan:\
  \ add Intel Xe flash attention optimization kernels (2/3, Xe-LPG Plus/Xe2/Xe3) (#24406)\r\n73c941b11\
  \ mtmd: add various sanity checks (#29276)\r\n0f8a414b7 metal : gate mul_mm_id src1 rescale behind ggml_prec\
  \ (#29029)\r\nf95b0d953 ggml : IQ1_M build prefix sums once per block (#28706)\r\nc350a40bb Performance\
  \ tune for gemma4-26b-a4b flash attention shape. (#28450)\r\n9b421fa94 ui : Accept WEBM video files\
  \ (#28622)\r\n348f853b7 jinja: use const for statement::execute and ::visit (#29271)\r\n217f81c26 server:\
  \ Add support for binding to multiple addresses (#28690)\r\n828fdf282 spec : support DFlash for HunyuanOCR\
  \ (#28890)\r\nbfd73a876 convert: add MiMo-V2.6 support (#29257)\r\na60f9aead cmake : allow repeated\
  \ find_package calls for llama (#29228)\r\n7ab4ee7ba chat : Fix Muse Glimmer tool-call first parser\
  \ error (#29242)\r\n0ee9435b8 ci : publish snapdragon builds in release workflow (#29007)\r\n8cfc315a8\
  \ Add close button to UI toasts (#28246)\r\nec5a12b85 opencl: add A8 Q4_0 non-MoE dp4a binary kernel\
  \ (#29055)\r\nc550d2f60 ci : update Level Zero SDK to v1.33.1 and enable the L0/oneDNN CMake flags in\
  \ the SYCL job (#29230)\r\n58367713a hexagon: new HMX-optimized GATED_DELTA_NET (#29199)\r\nff0dbb975\
  \ vendor : update cpp-httplib to 0.57.1 (#29239)\r\nfb34fc262 metal : fix mask bounds in flash attention\
  \ block pre-pass (#29220)\r\nc641dfa83 test-save-load-state : compare logits with NMSE and feed expected\
  \ tokens (#29238)\r\n965506136 llama-context : report graph inputs and input tensors during sched reserve\
  \ (#26625)\r\nb1c2863e2 cuda: fix sm_70 tile compilation error (#29224)\r\nf4e276a20 ggml-cuda : convert\
  \ contiguous tensors four elements at a time (#29155)\r\ne6cef8152 cuda : accelerate conv2d with implicit\
  \ GEMM (#29135)\r\nc21284cdf ggml : fix dimension and stride truncation in ggml_permute (#29227)\r\n\
  6f41ac59e vendor : update cpp-httplib to 0.57.0 (#29214)\r\nec91ab5ad docker : bump cuda to 13.4.1 (#29207)\r\
  \nbb3c853c3 sycl : support gated DSV4_HC_PRE and optional HC_POST comb matrix (#29132)\r\naf911149c\
  \ sycl : pinned memory use right device context instead of 0 (#28895)\r\n1884824fd CUDA: Follow up of\
  \ #25635, refactoring FA shared smem swizzle (#28536)\r\n161755f29 test-llama-archs : make tensor data\
  \ stdev configurable and improve help (#29133)\r\n1d72b05d3 tests/test-backend-ops : allow regex entries\
  \ in the -o filter (#29204)\r\n542e9202d ci : refactor build-self-hosted into backend-specific workflows\
  \ (#28991)\r\ne0dff5847 args: add env vars for temperature, top-p, min-p and penalties (#27380)\r\n\
  982a3329a server : do not forward --api-key-file to router-spawned child instances (#28938)\r\n711f60bee\
  \ tests : remove stale comment (#29140)\r\n335b21fcb ggml-metal : simplify fusion pattern op list declaration\
  \ (#29206)\r\n26394b4e6 json: Fixed json enum handling (#28518)\r\n1aa2954bd sycl : coalesce MKL-FA\
  \ softmax loads instead of one work-item per row (#28918)\r\n8034c1d1f ggml-cpu: ARM Repack kernels\
  \ for Q1_0 (#23492)\r\n6ad1af560 ci : Upgrade CUDA to 13.4 for Ubuntu CUDA Release Builds (#29202)\r\
  \n0c3626ec0 hexagon: overhaul of buffer and DMA handling to support 64bit mappings + improvements (#29197)\r\
  \n68d9053af cuda : tune MMVQ to MMQ crossover for SM70 (Volta) (#28912)\r\n8aa161b54 metal : fix deprecation\
  \ warnings from macOS 27 SDK (#29136)\r\n932a68e06 webgpu : add fused gdn + cpy (#28976)\r\n62668d6b2\
  \ convert: enable --fuse-qkv for muse-glimmer (#29203)\r\nce8caa6e6 CUDA: tune FA for Gemma 4 on Ampere\
  \ or newer (#29152)\r\na894dae93 metal : support arbitrary hc in dsv4_hc_pre (#29169)\r\n3d82ef62d common/peg\
  \ : handle invalid utf-8 sequences in the AST (#29161)\r\n3cf03257f CUDA: enable sparse fa for qwen4\
  \ (#28770)\r\nb23efaa2e ui: Fix mobile breakpoint + content overflow issues (#29108)\r\n426090367 fix(mamba)\
  \ : make time-step projection input contiguous (#28832)\r\n9a9f939b8 metal: add F16 input to the FWHT\
  \ (#29094)\r\nf072b1037 chat : fix gemma4 required tool grammar (#29115)\r\n59657a613 chat : add dedicated\
  \ Ling 3.0 (Bailing V3) parser (#28682)\r\ne613ef2c8 hexagon: enable I32 GET_ROWS (#29116)\r\n851cb34f2\
  \ hexagon: add support for GEGLU_QUICK (#29114)\r\n7d4b92bb9 hexagon: enable support for TOP_K op (#29113)\r\
  \n1af554f8f server : improve startup log messages (#29125)\r\neb1e1f495 json-schema : accept escaped\
  \ hyphen in regex patterns (#29127)\r\n5b59b83f4 metal : add MoE and SSM_CONV fusion optimizations (#28948)\r\
  \n60b06ab9a metal : fix FA support checks (#29122)\r\nefa28e950 test-llama-archs : generate dummy test\
  \ vocab (#29084)\r\n59fc5a1ca metal : support qwen4exp hc ops (#29000)\r\nb23701f77 cuda : fix CUB argsort\
  \ corruption caused by in-place keys (#28389)\r\n60081bb2b opencl: add support for bin kernel `flash_attn_f32_f16_bin`\
  \ (#29046)\r\n2b1847030 hexagon: add ROLL op support (#29105)\r\n50631b3d2 hexagon: im2col update (#29103)\r\
  \n18a04f09c hexagon: HMX flash-attention head_dim padding (support DK=DV=72) (#26539)\r\nec9281505 opencl:\
  \ add bin kernel `kernel_gemm_noshuffle_q6_k_f32_32b_trans_ila_a8_bin` (#28678)\r\n4fea119de ggml-cpu:\
  \ add F16 input to the FWHT (#27779)\r\n5b335f413 ggml : check for allocation failures to prevent crashes\
  \ (#28149)\r\n542348a35 Model-Saver: Write the SWA pattern, 15 more architectures roundtrip (#29042)\r\
  \nd663dd3f3 ci: change ubuntu-latest to ubuntu-24.04 (#29079)\r\n44be98f05 ggml-webgpu: fix supports_op\
  \ condition for GET_ROWS (#28978)\r\n911f6cdc8 ggml : handle graph buffer reservation failure (#26070)\r\
  \nbbd488c42 vulkan: add IQ3_S  MMQ matmul kernels (#28822)\r\ndc85f89c7 vocab : add ufakzeka pre-tokenizer\
  \ (#29033)\r\n8ed1a55ef cmake : fix build when GGML_CPU=OFF and GGML_CUDA=ON (#29026)\r\nbb11ebb68 gguf-py:\
  \ fix Q8_1 block size in GGML_QUANT_SIZES (2+2+32) (#29036)\r\nf03cf3e9b ci : disable GHA cache for\
  \ copilot (#29068)\r\nbdcbaaf6e ci : bump android-actions/setup-android to 4.0.4 (#29065)\r\n5c53396b8\
  \ vulkan: raise the hoisted row-id limit for mul_mat_id from 256 to 512 experts (#28501)\r\n972d2313b\
  \ ci : add missing evict-old-files (#29041)\r\nc77ae695c rpc : skip ACCEL devices (#29020)\r\nb49650adb\
  \ model : skip gate_up_exps if TENSOR_SKIP is set (#29014)\r\n707618048 model : extend Nemotron MTP\
  \ support (#29018)\r\nebbb18522 openvino : Update OpenVINO to 2026.4;fix clangd,MSVC warnings;  (#29009)\r\
  \n4ff829ec2 ui: fix removed reasoning menu in single model mode on desktop (#27985)\r\nf172be756 vulkan:\
  \ split buffers and debug code into separate files, add shared headers (#28732)\r\n87f9c82f2 ci : add\
  \ API/ABI check to make-release workflow [no ci] (#28947)\r\n7f6f0c2a9 chat : add message delimiters\
  \ to the DeepSeek V3.2/V4 parser (#29008)\r\n81aeaeb74 gguf : align the data section relative to the\
  \ GGUF start, not the file (#28993)\r\nc9a5eeeb3 sycl : fix the B70 mem allocate error when >19.3GB\
  \ (#28953)\r\n7490357f2 vulkan: skip unneeded MoE work in mul_mm coopmat1 path (#25483)\r\n817e5f83e\
  \ sycl: ssm_conv: fuse the SiLU epilogue into the ssm_conv kernel (#28929)\r\nc57da6fd8 opencl: fix\
  \ various warnings (#28984)\r\n79bfc1d43 docs: remove JG as CODEOWNER for test-llama-archs (#29003)\r\
  \n05f2dcfdb  vulkan: fix buffer_reference alignment in im2col shaders (#28996)\r\n35822afe5 vulkan:\
  \ support qwen4exp hc ops (#28988)\r\naa39d7a3e [SYCL] Fix function signature for `ggml_backend_sycl_split_buffer_type`\
  \ (#28981)\r\n4bc272fd7 vulkan: work around NV bug with argsort_large.comp (#28975)\r\nfb27a525d TP:\
  \ fix split state and granularity for fused QKV gemma4, qwen35 (#28965)\r\nc6824a9e4 ci: switch fast\
  \ jobs back to github (#28959)\r\n2f3fd0252 Enable CUDA graph for MTP draft (#28549)\r\n1ec818809 hexagon:\
  \ Support for K-Quants Q4_K and Q6_K (#28994)\r\n82324fc50 hexagon: accept the zeroed rope probe in\
  \ supports_op (#28995)\r\n7ceed8737 models : allow Nemotron-H models to only define layer_norm_epsilon\
  \ (#28989)\r\n7d6f5d02b model : add support for HrmTextForCausalLM (DFM Mimir 1B) (#27625)\r\n83078fec0\
  \ CUDA/HIP: improve access patterns in im2col (#28013)\r\nf266648fa spacemit : fix wrong transpose function\
  \ for int16 data (#25161)\r\n60199339b rpc : invalidate cached compute graph when a referenced buffer\
  \ is freed (#24292)\r\nb04d4e567 Change max context length for auto-fitting with unified KV (#28849)\r\
  \n37b53fd45 qwen4exp: add hc ops (#28901)\r\nfccf7166f HIP: broaden MoE ncols_opt tile heuristic on\
  \ RDNA3.5 architecture (#28935)\r\n0bec16e38 chat : force `\\n</think>` on reasoning budget end for\
  \ qwen3-coder (#28869)\r\nd4365d955 vulkan: make MUL_MAT_ID BN/2 tail unconditional (#28923)\r\n0a8b29a60\
  \ metal: fix NaN in mul_mm_id when activations exceed f16 range (#26223)\r\n583926e3a ci : add self-hosted\
  \ webgpu to hf-jobs (#28712)\r\ne13469a32 llama-bench: support --version to print build info (#28971)\r\
  \n930e2fa59 hexagon: add back missing contiguous fast-path and hvx_copy_uu for each run (#28886)\r\n\
  72b590d65 hex-cpy: use dma if src and dst are contiguous (#28906)\r\n38a5b42d9 HIP: Enable AllReduce\
  \ for ROCm (#27825)\r\n9f31776c3 opencl: choose the MoE expert matmul by batch size for speculative\
  \ decoding/MTP (#27637)\r\nd1d3c3396 ci: build MUSA for only 1 arch (#28944)\r\n6011c34ce docs: Rule\
  \ of thumb for AI review time [no ci] (#28945)\r\n760984655 rpc : hash-cache only weights (#28789)\r\
  \n543158132 cuda: support row-contiguous SUM_ROWS (#26308)\r\n9e7171624 models : move build_arch_graph()\
  \ after graph() template specialization (#28934)\r\nfc82583e6 vulkan: support sparse Flash Attention\
  \ (#28105)\r\n77d554b26 OpenVINO: optimize stateful decode and GPU MoE inference (#28638)\r\n6ec1a7e95\
  \ opencl: add generic ssm_scan (#28881)\r\n1af6c65de ci: bump kleidiai runners from 22.04 to 24.04 (#28885)\r\
  \n1e7bcf3da metal : add FA kernels for HSK=96, HSV=64 (MiniCPM3) (#28599)\r\n0ecb159c9 ci: Bump CUDA\
  \ Windows x64 builds to 13.4.1 (#28930)\r\n987498f45 ci : fix android release (#28936)\r\n4c9233c03\
  \ cuda : enable i16 and i32 for DUP (#28897)\r\n69eb25067 cmake : use PROJECT_SOURCE_DIR instead of\
  \ CMAKE_SOURCE_DIR (#28771)\r\n1bc7a5af0 webui: stop re-probing disabled /tools endpoint on every message\
  \ (#28646)\r\n7cf1c54a9 ci : reuse build tag name when used instead of safe one (#28911)\r\n96ffdc41c\
  \ CI: hip-quality-check: ignore spill added in bfdc32183d57f1e35bacf35c47d6311e2028bbbc (#28909)\r\n\
  bfdc32183 HIP: fattn-mma: use fp32 accumulation on MFMA devices (#28576)\r\n391fac164 ci : add ubuntu-cuda\
  \ builds to release (#28186)\r\n41abbfd59 qwen4exp: enable rms_norm + mul fusion (#28896)\r\nb4fa47d22\
  \ release : added gfx1103 to ubuntu rocm build (#28423)\r\nf3a184b15 cmake : remove precompiled headers\
  \ (#28892)\r\ndfe45163e scripts: Add script to verify API/ABI compatibility (#28579)"
first_seen: '2026-09-23T20:50:06Z'
last_seen: '2026-09-24T00:30:54Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/ggml-org/llama.cpp/releases/tag/v0.5.0
  seen_at: '2026-09-24T00:30:54Z'
  metrics:
    reactions: 6
  kind: news
---

# ggerganov/llama.cpp: v0.5.0

## Overview

This release focuses on backend performance and correctness, broader model coverage, and more robust server/router operation. It adds HRM-Text (DFM Mimir 1B) support, MiMo-V2.6 and HunyuanOCR conversion support, ggml 0.25.0 backend improvements, multi-address HTTP binding, image outputs from function calls, and several chat parser/UI fixes.

### Highlights

- Accelerate CUDA `conv2d` with implicit GEMM ([#29135](https://github.com/ggml-org/llama.cpp/pull/29135))
- Add Metal MoE and SSM_CONV fusion optimizations ([#28948](https://github.com/ggml-org/llama.cpp/pull/28948))
- Allow the server to bind to multiple addresses ([#28690](https://github.com/ggml-org/llama.cpp/pull/28690))

### API changes

- Add `llama_adapter_lora_init_from_file_ptr()` for loading LoRA from an open FILE ([#28993](https://github.com/ggml-org/llama.cpp/pull/28993))
- Document `llama_model_load_from_file_ptr()` as reading from the current position and requiring aligned mmap ([#28993](https://github.com/ggml-org/llama.cpp/pull/28993))
- Add `LLAMA_VOCAB_TYPE_TEST` dummy tokenizer ([#29084](https://github.com/ggml-org/llama.cpp/pull/29084))
- Add `input_image` support to server function-call outputs ([#22575](https://github.com/ggml-org/llama.cpp/pull/22575))
- Allow `--host` to accept comma-separated TCP addresses and UNIX sockets ([#28690](https://github.com/ggml-org/llama.cpp/pull/28690))

### New models

- Add HRM-Text / DFM Mimir 1B support ([#27625](https://github.com/ggml-org/llama.cpp/pull/27625))
- Add MiMo-V2.6 conversion support ([#29257](https://github.com/ggml-org/llama.cpp/pull/29257))
- Add DFlash support for HunyuanOCR ([#28890](https://github.com/ggml-org/llama.cpp/pull/28890))
- Extend Nemotron MTP and Nemotron-H model handling ([#29018](https://github.com/ggml-org/llama.cpp/pull/29018), [#28989](https://github.com/ggml-org/llama.cpp/pull/28989))
- Add Qwen4Exp hyper-connection ops and sparse flash attention ([#28901](https://github.com/ggml-org/llama.cpp/pull/28901), [#28770](https://github.com/ggml-org/llama.cpp/pull/28770))
- Add `--fuse-qkv` support for Muse Glimmer ([#29203](https://github.com/ggml-org/llama.cpp/pull/29203))

### Core changes

- Add graph input/input-tensor diagnostics during scheduler reserve ([#26625](https://github.com/ggml-org/llama.cpp/pull/26625))
- Enable CUDA graphs for MTP drafting ([#28549](https://github.com/ggml-org/llama.cpp/pull/28549))
- Fix tensor-parallel split state/granularity for fused QKV models ([#28965](https://github.com/ggml-org/llama.cpp/pull/28965))
- Fix Mamba time-step projection input contiguity ([#28832](https://github.com/ggml-org/llama.cpp/pull/28832))
- Write the SWA pattern in the model saver and round-trip 15 more architectures ([#29042](https://github.com/ggml-org/llama.cpp/pull/29042))
- Add environment variables for temperature, top-p, min-p and penalties ([#27380](https://github.com/ggml-org/llama.cpp/pull/27380))
- Reduce the sampler backend probe size ([#29285](https://github.com/ggml-org/llama.cpp/pull/29285))
- Add Ling 3.0, DeepSeek V3.2/V4, qwen3-coder, Muse Glimmer and Gemma 4 parser fixes ([#28682](https://github.com/ggml-org/llama.cpp/pull/28682), [#29008](https://github.com/ggml-org/llama.cpp/pull/29008), [#28869](https://github.com/ggml-org/llama.cpp/pull/28869), [#29242](https://github.com/ggml-org/llama.cpp/pull/29242), [#29115](https://github.com/ggml-org/llama.cpp/pull/29115))
- Improve JSON Schema and PEG handling ([#28518](https://github.com/ggml-org/llama.cpp/pull/28518), [#29127](https://github.com/ggml-org/llama.cpp/pull/29127), [#29161](https://github.com/ggml-org/llama.cpp/pull/29161))
- Add ufakzeka pre-tokenizer and `llama-bench --version` ([#29033](https://github.com/ggml-org/llama.cpp/pull/29033), [#28971](https://github.com/ggml-org/llama.cpp/pull/28971))

### Multi-modality changes

- Add sanity checks for mtmd layer indices, SAM layer counts, resize targets and graph allocation ([#29276](https://github.com/ggml-org/llama.cpp/pull/29276), [#28149](https://github.com/ggml-org/llama.cpp/pull/28149))
- Fix SigLIP bucket buffer overrun for tall/wide images ([#29276](https://github.com/ggml-org/llama.cpp/pull/29276))

### Server changes

- Fix router eviction races and child process lifecycle handling ([#29217](https://github.com/ggml-org/llama.cpp/pull/29217))
- Do not pass log file or API key file to router-spawned children ([#29212](https://github.com/ggml-org/llama.cpp/pull/29212), [#28938](https://github.com/ggml-org/llama.cpp/pull/28938))
- Improve startup and model-source logging ([#29125](https://github.com/ggml-org/llama.cpp/pull/29125))
- Update vendored cpp-httplib to 0.57.1 ([#29239](https://github.com/ggml-org/llama.cpp/pull/29239))

### UI changes

- Accept WEBM video files ([#28622](https://github.com/ggml-org/llama.cpp/pull/28622))
- Add close button to UI toasts ([#28246](https://github.com/ggml-org/llama.cpp/pull/28246))
- Fix mobile breakpoint and content overflow issues, including horizontal table scrolling ([#29108](https://github.com/ggml-org/llama.cpp/pull/29108))
- Restore the reasoning menu in single-model desktop mode ([#27985](https://github.com/ggml-org/llama.cpp/pull/27985))
- Stop re-probing a disabled `/tools` endpoint on every message ([#28646](https://github.com/ggml-org/llama.cpp/pull/28646))

### ggml changes

- Updated ggml to v0.25.0 ([release](https://github.com/ggml-org/ggml/releases/tag/v0.25.0))
- The release expands hyper-connection, flash-attention, and fused MoE/SSM support across backends, with robustness, quantization, data-layout, and RPC/meta improvements.
- API changes include gated `ggml_dsv4_hc_pre_gated()`, optional `ggml_dsv4_hc_post()` comb, and RPC protocol major v7.

## Assets

**Nightly build:** [b11146](https://github.com/ggml-org/llama.cpp/releases/tag/b11146)

## More info

- [Releases and versioning of `ggml-org` projects](https://github.com/ggml-org/ggml/discussions/1579)

## Changelog since [v0.4.1](https://github.com/ggml-org/llama.cpp/releases/tag/v0.4.1)

7fe450e19 llama.cpp : bump version to 0.5.0 (#29333)
177cd8cc7 sync : ggml
e4e2f6232 ggml : bump version to 0.25.1 (ggml/1637)
66fba63af CUDA: add a reserve to avoid spurious warning on older GCC builds (#29317)
bddf8263c common : keep HF cache dir as path, expose UTF-8 only for logs (#29320)
957538960 metal: add the missing f32 x bf16 mul_mv variants (#28741)
dc9879cf6 CUDA: enable sparse-fa for dsv4 prefill (again) (#29298)
42916d83f server: fix token counting API crash on sleep (#29309)
4e416ee73 jinja : parse unary +/- before variables (#29244)
ee3ecce05 metal : key the fa-vec tuned table by family instead of SKU (#29075)
057494f93 server: accept OpenAI video_url content type and data: video URIs (#27921)
bcbc936a8 server: Dedup the draft HF model via dedup-cache-models (#27934)
26758d38f ci : fix build-cmake runner target (#29299)
18f9f7bef model-conversion : add causal-compare-logits recipe (#29305)
633733d0a model : support Gemma4 DSpark draft backbone (#29226)
86b2daa73 ci : run python (jinja) test (#29302)
183d2a04c make-release : update summary prompt
45062d405 sync : ggml
503549c5f ggml : bump version to 0.25.0 (ggml/1635)
e97545d91 sycl : fix compile warnings
b1ff4ca23 vulkan: add IQ4_XS MMQ/MMV matmul kernels (#28415)
94256114c ggml-meta: resolve multi buffer views (#29266)
1a679828f cuda: top-k MoE should always fire (#28432)
384a534ce sycl : support new UT case for mul_mat_hadamard fp16 (#29218)
5e48b3100 sycl: extend MMVQ GLU fusion, add rms_norm+scale and ssm_conv+silu fusions (#28931)
4d7d7703f sycl : support op get_rows_back, only support fp32/fp16 (#25266)
08b1d2aea vulkan: hide internal symbols to prevent duplicate-dlopen state destruction (#29139)
441df11f6 sampler: reduce the size of the probe (#29285)
e6ab7c1a4 hex-dma: introduce direct-mapped DMA cache that is better suited for HVX FA mask handling (#29282)
f46bc30cb HIP : optimize IQ2/IQ3 (`__vsub4` `__vcmpne4`) using SWAR (#27962)
709fe755d jinja : fix dangling reference warning in for_statement (#29279)
d5f66492e opencl: add bin kernel `kernel_gemm_noshuffle_q4_k_q8_1_dp4a_ila_a8_bin` (#29056)
991991118 server: fix router eviction races with the existing queue (#29217)
bbf99b1b3 server: do not pass log file to children (#29212)
4098fdc92 server: support input_image in function_call_output (#20663) (#22575)
4ceb17191 vulkan: add Intel Xe flash attention optimization kernels (2/3, Xe-LPG Plus/Xe2/Xe3) (#24406)
73c941b11 mtmd: add various sanity checks (#29276)
0f8a414b7 metal : gate mul_mm_id src1 rescale behind ggml_prec (#29029)
f95b0d953 ggml : IQ1_M build prefix sums once per block (#28706)
c350a40bb Performance tune for gemma4-26b-a4b flash attention shape. (#28450)
9b421fa94 ui : Accept WEBM video files (#28622)
348f853b7 jinja: use const for statement::execute and ::visit (#29271)
217f81c26 server: Add support for binding to multiple addresses (#28690)
828fdf282 spec : support DFlash for HunyuanOCR (#28890)
bfd73a876 convert: add MiMo-V2.6 support (#29257)
a60f9aead cmake : allow repeated find_package calls for llama (#29228)
7ab4ee7ba chat : Fix Muse Glimmer tool-call first parser error (#29242)
0ee9435b8 ci : publish snapdragon builds in release workflow (#29007)
8cfc315a8 Add close button to UI toasts (#28246)
ec5a12b85 opencl: add A8 Q4_0 non-MoE dp4a binary kernel (#29055)
c550d2f60 ci : update Level Zero SDK to v1.33.1 and enable the L0/oneDNN CMake flags in the SYCL job (#29230)
58367713a hexagon: new HMX-optimized GATED_DELTA_NET (#29199)
ff0dbb975 vendor : update cpp-httplib to 0.57.1 (#29239)
fb34fc262 metal : fix mask bounds in flash attention block pre-pass (#29220)
c641dfa83 test-save-load-state : compare logits with NMSE and feed expected tokens (#29238)
965506136 llama-context : report graph inputs and input tensors during sched reserve (#26625)
b1c2863e2 cuda: fix sm_70 tile compilation error (#29224)
f4e276a20 ggml-cuda : convert contiguous tensors four elements at a time (#29155)
e6cef8152 cuda : accelerate conv2d with implicit GEMM (#29135)
c21284cdf ggml : fix dimension and stride truncation in ggml_permute (#29227)
6f41ac59e vendor : update cpp-httplib to 0.57.0 (#29214)
ec91ab5ad docker : bump cuda to 13.4.1 (#29207)
bb3c853c3 sycl : support gated DSV4_HC_PRE and optional HC_POST comb matrix (#29132)
af911149c sycl : pinned memory use right device context instead of 0 (#28895)
1884824fd CUDA: Follow up of #25635, refactoring FA shared smem swizzle (#28536)
161755f29 test-llama-archs : make tensor data stdev configurable and improve help (#29133)
1d72b05d3 tests/test-backend-ops : allow regex entries in the -o filter (#29204)
542e9202d ci : refactor build-self-hosted into backend-specific workflows (#28991)
e0dff5847 args: add env vars for temperature, top-p, min-p and penalties (#27380)
982a3329a server : do not forward --api-key-file to router-spawned child instances (#28938)
711f60bee tests : remove stale comment (#29140)
335b21fcb ggml-metal : simplify fusion pattern op list declaration (#29206)
26394b4e6 json: Fixed json enum handling (#28518)
1aa2954bd sycl : coalesce MKL-FA softmax loads instead of one work-item per row (#28918)
8034c1d1f ggml-cpu: ARM Repack kernels for Q1_0 (#23492)
6ad1af560 ci : Upgrade CUDA to 13.4 for Ubuntu CUDA Release Builds (#29202)
0c3626ec0 hexagon: overhaul of buffer and DMA handling to support 64bit mappings + improvements (#29197)
68d9053af cuda : tune MMVQ to MMQ crossover for SM70 (Volta) (#28912)
8aa161b54 metal : fix deprecation warnings from macOS 27 SDK (#29136)
932a68e06 webgpu : add fused gdn + cpy (#28976)
62668d6b2 convert: enable --fuse-qkv for muse-glimmer (#29203)
ce8caa6e6 CUDA: tune FA for Gemma 4 on Ampere or newer (#29152)
a894dae93 metal : support arbitrary hc in dsv4_hc_pre (#29169)
3d82ef62d common/peg : handle invalid utf-8 sequences in the AST (#29161)
3cf03257f CUDA: enable sparse fa for qwen4 (#28770)
b23efaa2e ui: Fix mobile breakpoint + content overflow issues (#29108)
426090367 fix(mamba) : make time-step projection input contiguous (#28832)
9a9f939b8 metal: add F16 input to the FWHT (#29094)
f072b1037 chat : fix gemma4 required tool grammar (#29115)
59657a613 chat : add dedicated Ling 3.0 (Bailing V3) parser (#28682)
e613ef2c8 hexagon: enable I32 GET_ROWS (#29116)
851cb34f2 hexagon: add support for GEGLU_QUICK (#29114)
7d4b92bb9 hexagon: enable support for TOP_K op (#29113)
1af554f8f server : improve startup log messages (#29125)
eb1e1f495 json-schema : accept escaped hyphen in regex patterns (#29127)
5b59b83f4 metal : add MoE and SSM_CONV fusion optimizations (#28948)
60b06ab9a metal : fix FA support checks (#29122)
efa28e950 test-llama-archs : generate dummy test vocab (#29084)
59fc5a1ca metal : support qwen4exp hc ops (#29000)
b23701f77 cuda : fix CUB argsort corruption caused by in-place keys (#28389)
60081bb2b opencl: add support for bin kernel `flash_attn_f32_f16_bin` (#29046)
2b1847030 hexagon: add ROLL op support (#29105)
50631b3d2 hexagon: im2col update (#29103)
18a04f09c hexagon: HMX flash-attention head_dim padding (support DK=DV=72) (#26539)
ec9281505 opencl: add bin kernel `kernel_gemm_noshuffle_q6_k_f32_32b_trans_ila_a8_bin` (#28678)
4fea119de ggml-cpu: add F16 input to the FWHT (#27779)
5b335f413 ggml : check for allocation failures to prevent crashes (#28149)
542348a35 Model-Saver: Write the SWA pattern, 15 more architectures roundtrip (#29042)
d663dd3f3 ci: change ubuntu-latest to ubuntu-24.04 (#29079)
44be98f05 ggml-webgpu: fix supports_op condition for GET_ROWS (#28978)
911f6cdc8 ggml : handle graph buffer reservation failure (#26070)
bbd488c42 vulkan: add IQ3_S  MMQ matmul kernels (#28822)
dc85f89c7 vocab : add ufakzeka pre-tokenizer (#29033)
8ed1a55ef cmake : fix build when GGML_CPU=OFF and GGML_CUDA=ON (#29026)
bb11ebb68 gguf-py: fix Q8_1 block size in GGML_QUANT_SIZES (2+2+32) (#29036)
f03cf3e9b ci : disable GHA cache for copilot (#29068)
bdcbaaf6e ci : bump android-actions/setup-android to 4.0.4 (#29065)
5c53396b8 vulkan: raise the hoisted row-id limit for mul_mat_id from 256 to 512 experts (#28501)
972d2313b ci : add missing evict-old-files (#29041)
c77ae695c rpc : skip ACCEL devices (#29020)
b49650adb model : skip gate_up_exps if TENSOR_SKIP is set (#29014)
707618048 model : extend Nemotron MTP support (#29018)
ebbb18522 openvino : Update OpenVINO to 2026.4;fix clangd,MSVC warnings;  (#29009)
4ff829ec2 ui: fix removed reasoning menu in single model mode on desktop (#27985)
f172be756 vulkan: split buffers and debug code into separate files, add shared headers (#28732)
87f9c82f2 ci : add API/ABI check to make-release workflow [no ci] (#28947)
7f6f0c2a9 chat : add message delimiters to the DeepSeek V3.2/V4 parser (#29008)
81aeaeb74 gguf : align the data section relative to the GGUF start, not the file (#28993)
c9a5eeeb3 sycl : fix the B70 mem allocate error when >19.3GB (#28953)
7490357f2 vulkan: skip unneeded MoE work in mul_mm coopmat1 path (#25483)
817e5f83e sycl: ssm_conv: fuse the SiLU epilogue into the ssm_conv kernel (#28929)
c57da6fd8 opencl: fix various warnings (#28984)
79bfc1d43 docs: remove JG as CODEOWNER for test-llama-archs (#29003)
05f2dcfdb  vulkan: fix buffer_reference alignment in im2col shaders (#28996)
35822afe5 vulkan: support qwen4exp hc ops (#28988)
aa39d7a3e [SYCL] Fix function signature for `ggml_backend_sycl_split_buffer_type` (#28981)
4bc272fd7 vulkan: work around NV bug with argsort_large.comp (#28975)
fb27a525d TP: fix split state and granularity for fused QKV gemma4, qwen35 (#28965)
c6824a9e4 ci: switch fast jobs back to github (#28959)
2f3fd0252 Enable CUDA graph for MTP draft (#28549)
1ec818809 hexagon: Support for K-Quants Q4_K and Q6_K (#28994)
82324fc50 hexagon: accept the zeroed rope probe in supports_op (#28995)
7ceed8737 models : allow Nemotron-H models to only define layer_norm_epsilon (#28989)
7d6f5d02b model : add support for HrmTextForCausalLM (DFM Mimir 1B) (#27625)
83078fec0 CUDA/HIP: improve access patterns in im2col (#28013)
f266648fa spacemit : fix wrong transpose function for int16 data (#25161)
60199339b rpc : invalidate cached compute graph when a referenced buffer is freed (#24292)
b04d4e567 Change max context length for auto-fitting with unified KV (#28849)
37b53fd45 qwen4exp: add hc ops (#28901)
fccf7166f HIP: broaden MoE ncols_opt tile heuristic on RDNA3.5 architecture (#28935)
0bec16e38 chat : force `\n</think>` on reasoning budget end for qwen3-coder (#28869)
d4365d955 vulkan: make MUL_MAT_ID BN/2 tail unconditional (#28923)
0a8b29a60 metal: fix NaN in mul_mm_id when activations exceed f16 range (#26223)
583926e3a ci : add self-hosted webgpu to hf-jobs (#28712)
e13469a32 llama-bench: support --version to print build info (#28971)
930e2fa59 hexagon: add back missing contiguous fast-path and hvx_copy_uu for each run (#28886)
72b590d65 hex-cpy: use dma if src and dst are contiguous (#28906)
38a5b42d9 HIP: Enable AllReduce for ROCm (#27825)
9f31776c3 opencl: choose the MoE expert matmul by batch size for speculative decoding/MTP (#27637)
d1d3c3396 ci: build MUSA for only 1 arch (#28944)
6011c34ce docs: Rule of thumb for AI review time [no ci] (#28945)
760984655 rpc : hash-cache only weights (#28789)
543158132 cuda: support row-contiguous SUM_ROWS (#26308)
9e7171624 models : move build_arch_graph() after graph() template specialization (#28934)
fc82583e6 vulkan: support sparse Flash Attention (#28105)
77d554b26 OpenVINO: optimize stateful decode and GPU MoE inference (#28638)
6ec1a7e95 opencl: add generic ssm_scan (#28881)
1af6c65de ci: bump kleidiai runners from 22.04 to 24.04 (#28885)
1e7bcf3da metal : add FA kernels for HSK=96, HSV=64 (MiniCPM3) (#28599)
0ecb159c9 ci: Bump CUDA Windows x64 builds to 13.4.1 (#28930)
987498f45 ci : fix android release (#28936)
4c9233c03 cuda : enable i16 and i32 for DUP (#28897)
69eb25067 cmake : use PROJECT_SOURCE_DIR instead of CMAKE_SOURCE_DIR (#28771)
1bc7a5af0 webui: stop re-probing disabled /tools endpoint on every message (#28646)
7cf1c54a9 ci : reuse build tag name when used instead of safe one (#28911)
96ffdc41c CI: hip-quality-check: ignore spill added in bfdc32183d57f1e35bacf35c47d6311e2028bbbc (#28909)
bfdc32183 HIP: fattn-mma: use fp32 accumulation on MFMA devices (#28576)
391fac164 ci : add ubuntu-cuda builds to release (#28186)
41abbfd59 qwen4exp: enable rms_norm + mul fusion (#28896)
b4fa47d22 release : added gfx1103 to ubuntu rocm build (#28423)
f3a184b15 cmake : remove precompiled headers (#28892)
dfe45163e scripts: Add script to verify API/ABI compatibility (#28579)

## 笔记


