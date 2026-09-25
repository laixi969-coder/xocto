---
slug: commit-rewriter-01
name: commit-rewriter
builder: ''
category: AI + 开发
summary_zh: 开源维护者在准备对外发布补丁时，本地仓库里常混着编码代理留下的杂乱提交信息和私有仓库的 issue 编号，直接公开会泄露内部信息。commit-rewriter 让维护者在本机仓库上逐条改写这些提交信息，提交后自动生成一个带时间戳的分支保存当前状态，最终得到一份可以公开的提交历史，人工仍需逐条确认改写内容。
inspiration: 趋势是编码代理开始批量产生提交，仓库历史本身成了需要清洗的发布物料。切入可以从开源维护者、安全响应团队这类必须公开补丁记录的人群做起，围绕“发布前把内部痕迹从历史里摘干净”这一步做工具或服务，而不是做通用
  Git 客户端。
summary_en: When open-source maintainers prepare a public patch release, their local repository often
  contains messy commit messages left by coding agents and issue IDs from private repositories, which
  would leak internal information if published. commit-rewriter lets maintainers rewrite those commit
  messages on their local repository, and on submit it creates a timestamped branch of the current repo
  state, producing a publishable commit history; a human still has to confirm each edit.
inspiration_en: 'The trend is that coding agents now generate commits in bulk, making repository history
  itself a release artifact that needs cleaning. The entry point is open-source maintainers and security
  response teams who must publish patch records: build a tool or service around the step of stripping
  internal traces from history before release, rather than a general Git client.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 开源维护者在发布安全补丁前清理提交历史
jobs_en:
- Open-source maintainers cleaning commit history before a security release
regions: []
regions_en: []
open_source: true
url: https://simonwillison.net/2026/Sep/14/commit-rewriter/
canonical_url: https://simonwillison.net/2026/Sep/14/commit-rewriter
summary: "Release:   commit-rewriter 0.1  \n         I built this little web app the other day to help\
  \ edit the commit messages for the  Datasette security releases . The initial commits were full of coding\
  \ agent cruft and references to issue IDs from our private repository, so they weren't fit for publication.\
  \ \n If you want to edit the commit messages for a repository you can run it like this: \n  uvx commit-rewriter\
  \ path/to/repo\n  \n Omit the path if you are already in the directory for that repo. \n   \n When you\
  \ submit your edits the tool creates a timestamped branch of your current repo state - to allow you\
  \ to revert if you need to - and then rewrites every commit from the first one you edited to the most\
  \ recent. \n    \n    \n         Tags:  git ,  projects ,  python ,  ai-assisted-programming"
first_seen: '2026-09-14T00:28:10Z'
last_seen: '2026-09-25T00:34:10Z'
status: watching
sources:
- marketfeeds
sightings:
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/14/commit-rewriter/
  seen_at: '2026-09-15T00:39:09Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://simonwillison.net/2026/Sep/24/commit-rewriter/
  seen_at: '2026-09-25T00:34:10Z'
  metrics: {}
  kind: news
---

# commit-rewriter

Release:   commit-rewriter 0.1  
         I built this little web app the other day to help edit the commit messages for the  Datasette security releases . The initial commits were full of coding agent cruft and references to issue IDs from our private repository, so they weren't fit for publication. 
 If you want to edit the commit messages for a repository you can run it like this: 
  uvx commit-rewriter path/to/repo
  
 Omit the path if you are already in the directory for that repo. 
   
 When you submit your edits the tool creates a timestamped branch of your current repo state - to allow you to revert if you need to - and then rewrites every commit from the first one you edited to the most recent. 
    
    
         Tags:  git ,  projects ,  python ,  ai-assisted-programming

## 笔记


