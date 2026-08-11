# x-octo

每天挖掘全球新出现的 AI 应用，过滤掉噪音，对留下的做商业分析（解决什么问题 / 痛点真伪 / 商业模式 / 可迁移点），产出中文简报。

## 核心分工（不要打破）

系统分两半，**跑腿的归 Python，动脑的归 Claude Code**：

- **Python 只做确定性工作**：抓取、去重、存档、渲染简报。不调用任何 LLM，不做任何判断。
- **判断类工作全部由 Claude Code 执行**：读 `config/filter.md` 做过滤，读 `config/template.md` 做分析，把结果写回 `data/`。

这样做的原因：用户的 Claude 走中转，独立 API 密钥既不稳也碰红线。不要为了"自动化"而在 Python 里引入 LLM SDK。

## 目录

```
config/     可编辑的规则层（品味所在，改这里不改代码）
  sources.yaml    采集源开关与参数
  filter.md       过滤规则 —— 什么值得看，什么是套壳
  template.md     分析模板 —— 输出哪些字段
src/xocto/  Python 采集层
data/
  raw/YYYY-MM-DD.jsonl    当日原始抓取，只追加不修改
  pool/<slug>.md          产品档案，一个产品一个文件，去重后的唯一真相
  analysis/<slug>.md      深度分析结果
  reports/YYYY-MM-DD.md   每日中文简报
```

## 数据规矩

- `data/raw/` 是原始存档，**只追加不删改**。所有下游都可以从它重建。
- `pool/` 里一个产品一个 md 文件，文件名 = slug。重复出现的产品更新同一个文件，不新建。
- 所有脚本必须**幂等**：同一天跑十次，结果和跑一次一样。
- 采集失败不能中断整体：单个源挂了要记录并继续，最后汇总报告哪个源失败了。

## 开发纪律

- 不引入重依赖。当前依赖只有 `httpx` + `pyyaml`，加任何新依赖前先说明为什么标准库不够。
- 每个文件 200-400 行，超 500 行拆分。
- 数据结构用不可变的 dataclass（`frozen=True`），不做原地修改。
- 改完必须实跑验证：`uv run xocto collect --dry-run`，不许只改不验。

## 常用命令

```bash
uv run xocto collect              # 采集今天
uv run xocto collect --dry-run    # 采集但不写盘
uv run xocto status               # 看数据现状
uv run xocto pool --new           # 列出尚未分析的新产品
```
