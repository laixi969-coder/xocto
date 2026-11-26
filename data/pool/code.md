---
slug: code
name: Code
builder: moyuman
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
inspiration_en: ''
priority_review: false
project_type: new_application
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: false
url: https://code.claude.com/docs/zh-CN/prompt-caching#which-ttl-each-request-gets
canonical_url: https://code.claude.com/docs/zh-CN/prompt-caching
summary: "Claude Max 订阅用了小半年之后，还是被封了。\r\n\r\n简单挣扎之后未果，又没实力付那么高的溢价，只能选择迁移到其他模型。\r\n\r\n目前尝试过的订阅/模型\r\n\r\
  \n- Deepseek-flash 官方 API\r\n- Gpt：100 刀档\r\n- Gemini：50 刀档\r\n- Qwen Token Plan：首月优惠 19 块\r\n- Grok\
  \ 首月优惠：具体多少钱忘了，首月大概 100RMB 的左右\r\n- 中转站：具体哪个就不说了，我也只是试用了一下而已\r\n\r\n模型上就是用 cc switch、magpie 等等之类的网关，将模型路由到\
  \ claude code\r\n\r\n# 配置相关\r\n\r\n## 降低额度消耗\r\n\r\n1. 关掉 Teammate\r\n    \r\n    GPT 非常喜欢使用 SubAgent，屁大点事都要喊一个\
  \ Agent 帮他来做，所以建议关掉 Teammate 功能，使用更轻量的 Subagent\r\n    \r\n    ```jsx\r\n    {\r\n    \t\"env\": {\r\
  \n    \t\t\"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS\": \"0\"\r\n    \t}\r\n    }\r\n    ```\r\n    \r\n\
  2. 限制 Subagent 可用的模型\r\n    \r\n    我明明没用 Astra，但是用量分析里却有 100 多条 Astra 的请求，怀疑是 Subagent 自动调了，所以还是限制下\r\
  \n    \r\n    ```json\r\n    {\r\n    \t\"env\": {\r\n    \t\t\"CLAUDE_CODE_SUBAGENT_MODEL\": \"轻量模型\"\
  ,\r\n    \t\t\"CLAUDE_CODE_SUBAGENT_MODEL_FORCE\": \"1\"\r\n    \t}\r\n    }\r\n    ```\r\n    \r\n\
  3. 延长缓存时间\r\n    \r\n    官方订阅主会话的 TTL 默认 1 小时，第三方默认 5 分钟\r\n    \r\n    参考：https://code.claude.com/docs/zh-CN/prompt-caching#which-ttl-each-request-gets\r\
  \n    \r\n    ```json\r\n    {\r\n    \t\"promptCacheTtl\": \"1h\"\r\n    }\r\n    ```\r\n    \r\n\r\
  \n## Auto-Compact\r\n\r\nsol 的 context 在 claude code 中似乎变少了，又或者本身就少。\r\n\r\n我这边显示 92% 的 context 用量，但是却触发了\
  \ ：\r\n\r\n```bash\r\n Your input exceeds the context window of this model. Please adjust your input\
  \ and try again.\r\n```\r\n\r\n所以建议还是设置一下 auto compact\r\n\r\n```json\r\n{\r\n\t  \"autoCompactEnabled\"\
  : true,\r\n    \"autoCompactWindow\": \"500k\",  // 具体多少看各位的习惯了\r\n}\r\n```\r\n\r\n## Skill\r\n\r\n\
  关掉之前需要 `/login` 才能使用的 `Skill`\r\n\r\n```json\r\n\"skillOverrides\": {\r\n\t\"claude-api\": \"off\"\r\
  \n}\r\n```\r\n\r\n## Plugin 和 MCP\r\n\r\n无需调整\r\n\r\n## Mod\r\n\r\n1. You-should-know\r\n    \r\n  \
  \  很好用的一个 mod，但是只能订阅状态下用，不过有人逆向出来了 https://github.com/wassname/cc-plugin-you-should-know 可以让 AI 复刻一个自己用就好\r\
  \n    \r\n\r\n## Tool\r\n\r\n1. 开启 Task Tool 的使用权限（这个一定要开！！）\r\n\r\n参考：https://code.claude.com/docs/zh-CN/tools-reference#task-tool-availability\r\
  \n\r\n```jsx\r\n{\r\n  \"env\": {\r\n    \"CLAUDE_CODE_ENABLE_TODO_TOOLS\": \"1\"\r\n  }\r\n}\r\n```\r\
  \n\r\n1. 关掉需要 `/login` 的 `Tool`\r\n\r\n```jsx\r\n{\r\n  \"permissions\": {\r\n    \"deny\": [\"Artifact\"\
  ]\r\n  }\r\n}\r\n```\r\n\r\n1. `Artifact` 替代\r\n\r\nArtifact 也是个很好用的工具，随时随地的看效果，市面上确实有一些开源替代\r\n\r\n\
  - ‣\r\n- ‣\r\n- 等等\r\n\r\n我并没有试过，只是简单调研了下，所以不做推荐了。\r\n\r\n我这边最后选了一个更轻量的方案，就是直接让 agent 在会话中给我看截图或者视频，用的是\
  \ Show-Your-Work Mod\r\n\r\n## StatusLine\r\n\r\n如果你之前习惯在 `statusLine` 中显示额度信息，那么现在让 AI 改从 Codex Cli\
  \ 读取用量信息即可\r\n\r\n如果你用的 magpie 之类的本地网关，也可以从网关取数\r\n\r\n# 模型问题\r\n\r\n## 过于谨慎\r\n\r\n这里点名 GPT，说的就是你。他经常纠结于一个屁大点的问题，无限钻牛角尖。像是一个能力不足的完美主义者。\r\
  \n\r\n改进：\r\n\r\n1. 尝试降低思考强度，我之前习惯开 `xhigh` ，改为 `high` \r\n2. 引入  Ponytail，直接把他核心那段写在你的 CLAUDE.md 中就好，不用装他那一整套东西\r\
  \n\r\n## 听不懂话\r\n\r\n这里也是点名 GPT，怀念 Claude，Claude 真的给我一种“懂我”的感觉。\r\n\r\ndeepseek 在这方面则表现很好，有一种“小 claude”\
  \ 的感觉。\r\n\r\n改进：\r\n\r\n1. 更详细精准的描述，比如用语音输入、比如直接截图标注给他\r\n2. 善用记忆功能，每次遇到类似情况，直接说“记一下，在我说 xxx 的时候，指的是\
  \ xxx”\r\n\r\n## 审美\r\n\r\n这里其实 GPT 就还好，deepseek 则会差一些。对我来讲，和之前写UI的流程没太大差别。可以去 [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-code/skills/artifact-design/SKILL.md)\
  \ 找 Claude 的 Desgin skill，让他更接近 Claude 的感觉\r\n\r\n# 感受\r\n\r\n- 模型本身能力当然重要，但目前这个时间节点，Harness 侧的配置和工作流也十分很重要\r\
  \n- Deepseek Flash 很棒，但在高峰期用官方API还是挺贵的\r\n- 当你把 Harness 调的比较好时，你会发现各个模型之间的差别变得不那么明显了\r\n- 相比更强大的模型，我更想要性价比高的模型（Claude\
  \ 如果能原价订阅那无意是性价比最高的，但可惜现在只能溢价买）\r\n\r\n# 最后\r\n\r\n调完这一大堆后，主力 6.1 Sol 用了一周了，感觉基本可用了。\r\n\r\n未来可能会保持\
  \ GPT 100刀 + Gemini 50刀。对比我之前的 Claude Max 125刀（IOS订阅）成本上差别不大。\r\n\r\n目前 Claude 订阅的溢价对我来讲过高了，说到底是个成本的问题，成本允许的话，我早就找个靠谱中转一把梭了。希望我的项目早日扭亏为盈哈哈哈。\r\
  \n\r\n希望能给同样被封各位一些新思路吧，如果有更好的配置、使用方法也欢迎讨论。"
first_seen: '2026-11-20T03:15:49Z'
last_seen: '2026-11-26T04:11:57Z'
status: pending_filter
sources:
- v2ex
- officialfeeds
- newssearch
- marketfeeds
sightings:
- source: v2ex
  url: https://code.claude.com/docs/zh-CN/prompt-caching#which-ttl-each-request-gets
  seen_at: '2026-11-20T03:15:49Z'
  metrics:
    comments: 4
  kind: product
- source: officialfeeds
  url: https://aws.amazon.com/blogs/machine-learning/use-kimi-code-cli-with-models-on-amazon-bedrock/
  seen_at: '2026-11-20T03:16:25Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMi2gFBVV95cUxPX3o3eldDLTdvWmRmM3FKcFpKckpoZjczMDg2Um9PMktiRkVfMlZYbFVNX1Z0ZXIzVWNTT0xrT09KTGhtRU5oc1N1aHhGd2lXMWlvN1MzQkhKci13dFNXYVNQbEhiRVVBY0g1b05PUHBHSEQwRlUzcERlYThrZzFSeWxLeGVvMnFYaHZFWUZ6SDhsWjgyYTBuMUxxRkFtMXlEalhLVG8wSklMRG55YVRCWS0wOUZ5dDZqdm9oTXh6ZW5ZUkllLUZldmdNODJ1eDExTlV1dmw2T2k1dw?oc=5
  seen_at: '2026-11-22T02:15:21Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/
  seen_at: '2026-11-24T06:03:57Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMiigFBVV95cUxNOUx2T3ZlUUF5UEt5blpwSWN5MmVCUmpiRi1kOXRxLXU4bk9UUHNzbERrNnB0dlF6aFRyWVVqZ2ltd2RqYlozQWtRZWQ5MUZsVGUyTktSYU1vSExNNlJacTRSWjRrY2hOclpqcHNtWG5EOWF4TURsX3lUQjR2NnptY2ZHdVNXTVpMOVE?oc=5
  seen_at: '2026-11-25T04:55:10Z'
  metrics: {}
  kind: news
- source: marketfeeds
  url: https://techcrunch.com/2026/11/25/jensen-huang-broke-nvidias-code-of-conduct-and-his-employees-may-not-forget-it/
  seen_at: '2026-11-26T04:11:00Z'
  metrics: {}
  kind: news
- source: newssearch
  url: https://news.google.com/rss/articles/CBMickFVX3lxTE1iRFpFa010UFU2c3FMQjIwLURiUGJMQXlpb0dxNUczRHZXTkh2STd1VFdmT3habjlGSC1WWkJDNmNxUHVabm5qaU5JV0pMdTRsMDU0NkRUblBOUUdabEoxTlFYa3FqLVN3a2JGTmNCZ0Z0UQ?oc=5
  seen_at: '2026-11-26T04:11:57Z'
  metrics: {}
  kind: news
---

# Code

Claude Max 订阅用了小半年之后，还是被封了。

简单挣扎之后未果，又没实力付那么高的溢价，只能选择迁移到其他模型。

目前尝试过的订阅/模型

- Deepseek-flash 官方 API
- Gpt：100 刀档
- Gemini：50 刀档
- Qwen Token Plan：首月优惠 19 块
- Grok 首月优惠：具体多少钱忘了，首月大概 100RMB 的左右
- 中转站：具体哪个就不说了，我也只是试用了一下而已

模型上就是用 cc switch、magpie 等等之类的网关，将模型路由到 claude code

# 配置相关

## 降低额度消耗

1. 关掉 Teammate
    
    GPT 非常喜欢使用 SubAgent，屁大点事都要喊一个 Agent 帮他来做，所以建议关掉 Teammate 功能，使用更轻量的 Subagent
    
    ```jsx
    {
    	"env": {
    		"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "0"
    	}
    }
    ```
    
2. 限制 Subagent 可用的模型
    
    我明明没用 Astra，但是用量分析里却有 100 多条 Astra 的请求，怀疑是 Subagent 自动调了，所以还是限制下
    
    ```json
    {
    	"env": {
    		"CLAUDE_CODE_SUBAGENT_MODEL": "轻量模型",
    		"CLAUDE_CODE_SUBAGENT_MODEL_FORCE": "1"
    	}
    }
    ```
    
3. 延长缓存时间
    
    官方订阅主会话的 TTL 默认 1 小时，第三方默认 5 分钟
    
    参考：https://code.claude.com/docs/zh-CN/prompt-caching#which-ttl-each-request-gets
    
    ```json
    {
    	"promptCacheTtl": "1h"
    }
    ```
    

## Auto-Compact

sol 的 context 在 claude code 中似乎变少了，又或者本身就少。

我这边显示 92% 的 context 用量，但是却触发了 ：

```bash
 Your input exceeds the context window of this model. Please adjust your input and try again.
```

所以建议还是设置一下 auto compact

```json
{
	  "autoCompactEnabled": true,
    "autoCompactWindow": "500k",  // 具体多少看各位的习惯了
}
```

## Skill

关掉之前需要 `/login` 才能使用的 `Skill`

```json
"skillOverrides": {
	"claude-api": "off"
}
```

## Plugin 和 MCP

无需调整

## Mod

1. You-should-know
    
    很好用的一个 mod，但是只能订阅状态下用，不过有人逆向出来了 https://github.com/wassname/cc-plugin-you-should-know 可以让 AI 复刻一个自己用就好
    

## Tool

1. 开启 Task Tool 的使用权限（这个一定要开！！）

参考：https://code.claude.com/docs/zh-CN/tools-reference#task-tool-availability

```jsx
{
  "env": {
    "CLAUDE_CODE_ENABLE_TODO_TOOLS": "1"
  }
}
```

1. 关掉需要 `/login` 的 `Tool`

```jsx
{
  "permissions": {
    "deny": ["Artifact"]
  }
}
```

1. `Artifact` 替代

Artifact 也是个很好用的工具，随时随地的看效果，市面上确实有一些开源替代

- ‣
- ‣
- 等等

我并没有试过，只是简单调研了下，所以不做推荐了。

我这边最后选了一个更轻量的方案，就是直接让 agent 在会话中给我看截图或者视频，用的是 Show-Your-Work Mod

## StatusLine

如果你之前习惯在 `statusLine` 中显示额度信息，那么现在让 AI 改从 Codex Cli 读取用量信息即可

如果你用的 magpie 之类的本地网关，也可以从网关取数

# 模型问题

## 过于谨慎

这里点名 GPT，说的就是你。他经常纠结于一个屁大点的问题，无限钻牛角尖。像是一个能力不足的完美主义者。

改进：

1. 尝试降低思考强度，我之前习惯开 `xhigh` ，改为 `high` 
2. 引入  Ponytail，直接把他核心那段写在你的 CLAUDE.md 中就好，不用装他那一整套东西

## 听不懂话

这里也是点名 GPT，怀念 Claude，Claude 真的给我一种“懂我”的感觉。

deepseek 在这方面则表现很好，有一种“小 claude” 的感觉。

改进：

1. 更详细精准的描述，比如用语音输入、比如直接截图标注给他
2. 善用记忆功能，每次遇到类似情况，直接说“记一下，在我说 xxx 的时候，指的是 xxx”

## 审美

这里其实 GPT 就还好，deepseek 则会差一些。对我来讲，和之前写UI的流程没太大差别。可以去 [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-code/skills/artifact-design/SKILL.md) 找 Claude 的 Desgin skill，让他更接近 Claude 的感觉

# 感受

- 模型本身能力当然重要，但目前这个时间节点，Harness 侧的配置和工作流也十分很重要
- Deepseek Flash 很棒，但在高峰期用官方API还是挺贵的
- 当你把 Harness 调的比较好时，你会发现各个模型之间的差别变得不那么明显了
- 相比更强大的模型，我更想要性价比高的模型（Claude 如果能原价订阅那无意是性价比最高的，但可惜现在只能溢价买）

# 最后

调完这一大堆后，主力 6.1 Sol 用了一周了，感觉基本可用了。

未来可能会保持 GPT 100刀 + Gemini 50刀。对比我之前的 Claude Max 125刀（IOS订阅）成本上差别不大。

目前 Claude 订阅的溢价对我来讲过高了，说到底是个成本的问题，成本允许的话，我早就找个靠谱中转一把梭了。希望我的项目早日扭亏为盈哈哈哈。

希望能给同样被封各位一些新思路吧，如果有更好的配置、使用方法也欢迎讨论。

## 笔记


