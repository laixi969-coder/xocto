---
slug: commit-rewriter-01
name: commit-rewriter
builder: ''
category: AI + 开发
summary_zh: 开源维护者在准备对外发布仓库时打开它，处理的是编码代理生成、夹杂私有 issue 编号的提交历史；工具接收本地仓库路径，在网页里逐条改写提交信息，提交后先建一个带时间戳的分支以便回退，再从第一条被改的提交重写到最新提交，最终得到一份可公开的提交历史，改写范围仍需人工确认。
inspiration: 趋势是编码代理开始批量产出提交，提交历史本身成了需要清洗的发布物料。切入可放在开源维护者与安全发布流程：把“发布前清理提交信息”做成可回退的批量改写，而不是逐条 amend；也可考虑按仓库或按发布次数收费的托管版本，但公开材料未披露任何定价。
summary_en: An open-source maintainer preparing a public release opens it to deal with a commit history
  written by coding agents and salted with private issue IDs. The tool takes a local repository path,
  lets the user rewrite commit messages in a web page, then creates a timestamped branch for rollback
  and rewrites every commit from the first edited one to the latest, producing a publishable history;
  the rewrite scope still needs human confirmation.
inspiration_en: 'The trend is that coding agents now mass-produce commits, making the commit history itself
  a release artifact that needs cleaning. The opening is the open-source maintainer and security-release
  workflow: make pre-release commit-message cleanup a reversible bulk rewrite instead of one-by-one amends,
  possibly as a hosted version priced per repository or per release, though no pricing is disclosed in
  the public material.'
priority_review: false
project_type: open_source
industries:
- 软件与信息服务
industries_en:
- Software and IT services
jobs:
- 开源维护者
- 软件工程师
jobs_en:
- Open-source maintainer
- Software engineer
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
status: pending_filter
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


