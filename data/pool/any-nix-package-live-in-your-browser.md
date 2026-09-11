---
slug: any-nix-package-live-in-your-browser
name: trynix
builder: ''
category: AI + 开发
summary_zh: 后端工程师或开源维护者在评审一个改动依赖或运行环境的 PR 时，原本要本地装 Nix、拉取依赖、复现旧版本环境才能验证；trynix 把 Nix 包放进浏览器内的 WebAssembly
  虚拟机，点开链接即可得到可交互 shell，trynix-preview 还会在 PR 下自动评论该链接。最终交付是一个可复现的浏览器内运行环境，是否与真实 CI 结果一致仍需人工确认。
inspiration: 趋势：把“环境复现”从本地安装搬到浏览器，评审和排障的入口正在从文档转向可点击的运行实例。切入：可从开源项目维护者、依赖升级频繁的团队切入，把“每个 PR 一个可启动环境”做成评审环节的默认动作；也可面向需要长期维护旧版本软件的企业，按可复现环境次数收费，但公开材料未披露定价。
summary_en: When a backend engineer or open source maintainer reviews a PR that changes dependencies or
  runtime, they normally install Nix locally, fetch dependencies and rebuild the old environment to verify
  it; trynix puts Nix packages into a WebAssembly VM in the browser so a link yields an interactive shell,
  and trynix-preview auto-comments that link on the PR. The deliverable is a reproducible in-browser runtime;
  whether it matches real CI results still needs human confirmation.
inspiration_en: 'Trend: environment reproduction is moving from local installs into the browser, so review
  and debugging entry points shift from docs to clickable running instances. Entry: start with open source
  maintainers and teams that upgrade dependencies often, making one bootable environment per PR the default
  review step; long-term legacy maintainers are another buyer, priced per reproducible environment, though
  no pricing is disclosed.'
priority_review: false
project_type: open_source
industries:
- 软件开发
- 信息技术服务
industries_en:
- Software Development
- IT Services
jobs:
- 后端工程师
- 开源维护者
jobs_en:
- Backend Engineer
- Open Source Maintainer
regions:
- 全球
regions_en:
- Global
open_source: true
url: https://simonwillison.net/2026/Sep/10/trynix/
canonical_url: https://simonwillison.net/2026/Sep/10/trynix
summary: "Any Nix package, live in your browser   \nFarid Zakaria calls this his \" magnum opus  of Nix\
  \ work\", and I can see why. \n  trynix.dev  provides a  qemu-wasm  powered x86_64 Linux virtual machine\
  \ running entirely in your browser through WebAssembly. That VM can then be booted with  any Nix package\
  \  from the past 13 years. They are URL addressable, so you can navigate to this page: \n  https://trynix.dev/?pkg=python3%403.6.2\
  \  \n Then click \"Load\" and get an interactive shell against a virtual machine running Python 3.6.2\
  \ from 2017. \n Farid is building all sorts of neat things on top of this. One recent example:  Review\
  \ a pull request by booting it  introduces  trynix-preview , described like this: \n \n GitHub action\
  \ that comments a link on a pull request which lets you boot the PR’s build in the browser using  https://trynix.dev\
  \ . No servers, just browsers. \n \n\n       Via  Lobste.rs   \n\n\n     Tags:  code-review ,  linux\
  \ ,  webassembly ,  github-actions"
first_seen: '2026-09-10T23:44:15Z'
last_seen: '2026-09-11T00:10:53Z'
status: watching
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/10/trynix/
  seen_at: '2026-09-11T00:10:53Z'
  metrics: {}
  kind: news
---

# trynix

Any Nix package, live in your browser   
Farid Zakaria calls this his " magnum opus  of Nix work", and I can see why. 
  trynix.dev  provides a  qemu-wasm  powered x86_64 Linux virtual machine running entirely in your browser through WebAssembly. That VM can then be booted with  any Nix package  from the past 13 years. They are URL addressable, so you can navigate to this page: 
  https://trynix.dev/?pkg=python3%403.6.2  
 Then click "Load" and get an interactive shell against a virtual machine running Python 3.6.2 from 2017. 
 Farid is building all sorts of neat things on top of this. One recent example:  Review a pull request by booting it  introduces  trynix-preview , described like this: 
 
 GitHub action that comments a link on a pull request which lets you boot the PR’s build in the browser using  https://trynix.dev . No servers, just browsers. 
 

       Via  Lobste.rs   


     Tags:  code-review ,  linux ,  webassembly ,  github-actions

## 笔记


