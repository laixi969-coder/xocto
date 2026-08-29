"""语言表 —— 整站所有随语种变化的东西，只有这一个来源。

站点出两个语种：中文在 site/，英文在 site/en/。**模板只有一套**，
渲染两次。复制一份英文模板看起来更省事，但两套模板一定会跑偏 ——
改了中文版的间距，英文版就落后一个版本，而且没人会发现。

这里装四类东西：

  1. 界面文案     导航、版块标题、空状态、页脚（模板里写 {{ t.nav.home }}）
  2. 枚举标签     赛道 / 阶段 / 状态 / 评级 / 指标口径
  3. 解析参数     分析要抽哪几个标题、报告的评级词、阅读速度、数量单位
  4. 日期格式     "2026 年 8 月 11 日 · 星期二" / "Tuesday, August 11, 2026"

英文站同样受 CLAUDE.md 那条硬约束管：不出现任何采集源名称。
所以指标口径译成 "Community score / Open-source traction"，
不是 "HN points / GitHub stars"。
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any

# 评级的稳定键。数据文件里两个语种各写各的话（中文写"强烈推荐"，
# 英文写"Strong pick"），但 CSS 类名和排序必须认同一套键 ——
# 否则英文站的评级徽章会全部掉色。
VERDICT_KEYS = ("strong", "notable", "unproven")

# 赛道的规范值存在 data/pool/*.md 里，永远是中文。
# 英文只是展示层的一层翻译，不改数据 —— 改数据就要动 160 个文件，
# 而且分类规则（config/filter.md）也是中文的。
CATEGORY_EN = {
    "AI + 创作": "AI + Creative",
    "AI + 开发": "AI + Dev",
    "AI + 商业": "AI + Business",
    "AI + 效率": "AI + Productivity",
    "AI + 生活": "AI + Life",
    "通用助手": "General assistants",
    "基础层": "Infrastructure",
}

PROJECT_TYPE_ZH = {
    "new_application": "新应用 / 服务",
    "open_source": "开源项目",
    "ai_transformation": "AI 改造",
}
PROJECT_TYPE_EN = {
    "new_application": "New application / service",
    "open_source": "Open-source project",
    "ai_transformation": "AI transformation",
}

# 细分榜名。数据里存的是中文，英文站要翻。
# 这些是品类榜不是平台名，所以不违反"不出现采集源"那条约束。
# 出现没登记的新榜时，英文站会原样露出中文，check_design.py 的
# "中文漏进英文站" 会当场抓住 —— 那正是我们要的报警方式。
BOARD_EN = {
    "国内总榜": "China overall",
    "全球总榜": "Global overall",
    "国内增速榜": "China fastest-growing",
    "全球增速榜": "Global fastest-growing",
    "出海总榜": "Global expansion overall",
    "出海增速榜": "Global expansion fastest-growing",
    "聊天机器人榜": "Chatbots",
    "代码辅助榜": "Coding assistants",
    "AI搜索榜": "AI search",
    "智能体榜": "Agents",
    "角色扮演榜": "Roleplay",
    "全球降速榜": "Global fastest-declining",
}

_EN_MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
)
_EN_WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
)


@dataclass(frozen=True)
class Locale:
    """一个语种的全部配置。frozen —— 构建过程中不允许被改。"""

    key: str  # "zh" / "en"
    lang: str  # <html lang>
    hreflang: str  # <link hreflang>
    og_locale: str
    prefix: str  # 输出与 URL 前缀："" / "en/"
    content_subdir: str  # data/analysis/<这里>/：中文是根目录，英文是 en/

    site_name: str
    site_tagline: str  # 顶栏和页脚那句副标题
    site_desc: str  # 没有专属摘要时的兜底

    # 展示标签
    categories: dict[str, str]
    stages: dict[str, str]  # early / proven
    forms: dict[str, str]  # not_business / charging / scaled / settled
    statuses: dict[str, str]
    verdict_words: tuple[str, str, str]  # 与 VERDICT_KEYS 一一对应
    metrics: dict[str, str]
    boards: dict[str, str]

    # 分析正文里要抽的二级标题（按顺序试，第一个命中的算数）
    heading_excerpt: tuple[str, ...]
    heading_replaces: tuple[str, ...]
    heading_takeaway: tuple[str, ...]
    heading_money: tuple[str, ...]
    heading_call: tuple[str, ...]
    heading_watch_next: tuple[str, ...]

    # 报告解析
    quiet_hints: tuple[str, ...]  # 命中就降权：免责/边界类版块不该和判断抢注意力
    count_units: dict[str, str]  # picks / table / list 各自的数量说法
    cta_default: str  # "→ [完整分析](...)" 没写文字时的兜底
    read_unit: str  # "chars"（中文按字数）/ "words"（英文按词数）
    read_speed: int  # 每分钟

    t: dict[str, Any]  # 界面文案，模板里用 t.xxx.yyy

    def category(self, name: str) -> str:
        return self.categories.get(name, name)

    def project_type(self, key: str) -> str:
        labels = PROJECT_TYPE_EN if self.key == "en" else PROJECT_TYPE_ZH
        return labels.get(key, key)

    def status(self, key: str) -> str:
        return self.statuses.get(key, key)

    def stage(self, key: str) -> str:
        return self.stages.get(key, key)

    def form(self, key: str) -> str:
        return self.forms.get(key, key)

    def board(self, name: str) -> str:
        return self.boards.get(name, name)

    def verdict_key(self, raw: str) -> str:
        """将数据中的评级或公开显示标签映射为稳定键。认不出返回空串。

        用前缀匹配而不是全等：作者会在评级后面加括号补充，
        那是给人看的，不该让徽章失去颜色。
        """
        for word, key in zip(self.verdict_words, VERDICT_KEYS):
            if raw.startswith(word):
                return key
        for key, label in self.t["verdict_labels"].items():
            if raw.startswith(label):
                return key
        return ""

    def verdict_rank(self, raw: str) -> int:
        key = self.verdict_key(raw)
        return VERDICT_KEYS.index(key) if key in VERDICT_KEYS else 9

    def verdict_label(self, raw: str) -> str:
        """评级是编辑结论，不应被读成购买或使用建议。"""
        key = self.verdict_key(raw)
        return self.t["verdict_labels"].get(key, raw)

    def count_label(self, kind: str, n: int) -> str:
        unit = self.count_units.get(kind, "")
        return unit.format(n=n) if unit else ""

    def date_label(self, day: str) -> str:
        """报头上的人话日期。解析不出来就原样返回。"""
        try:
            d = date.fromisoformat(day)
        except ValueError:
            return day
        if self.key == "en":
            return f"{_EN_WEEKDAYS[d.weekday()]}, {_EN_MONTHS[d.month - 1]} {d.day}, {d.year}"
        return f"{d.year} 年 {d.month} 月 {d.day} 日 · 星期{'一二三四五六日'[d.weekday()]}"

    def month_label(self, day: str) -> str:
        """日报归档按月分组时使用的人话标题。"""
        try:
            d = date.fromisoformat(day)
        except ValueError:
            return day[:7]
        if self.key == "en":
            return f"{_EN_MONTHS[d.month - 1]} {d.year}"
        return f"{d.year} 年 {d.month} 月"

    def path(self, rel: str) -> str:
        """站内相对路径加上语种前缀。products.html → en/products.html。"""
        return f"{self.prefix}{rel}"


ZH = Locale(
    key="zh",
    lang="zh-CN",
    hreflang="zh-Hans",
    og_locale="zh_CN",
    prefix="",
    content_subdir="",
    site_name="x-octo",
    site_tagline="AI 应用的生意判断",
    site_desc="给要决定下一步押什么的人：每天一句判断，几个讲得清谁付钱的案例。不给买卖建议。",
    categories={name: name for name in CATEGORY_EN},
    stages={"early": "刚冒头", "proven": "已有使用数据"},
    forms={
        "not_business": "还不是生意",
        "charging": "开始收费",
        "scaled": "已有规模",
        "settled": "格局已定",
    },
    statuses={
        "analyzed": "已分析",
        "watching": "持续观察",
        "market_context": "市场背景",
        "queued": "待分析",
        "pending_filter": "新收录",
        "rejected": "已淘汰",
    },
    verdict_words=("强烈推荐", "值得关注", "有待观察"),
    metrics={
        "points": "社区热度",
        "stars": "开源关注",
        "visits": "月访问",
        "mau": "月活",
        "mom": "环比",
    },
    boards={name: name for name in BOARD_EN},
    heading_excerpt=("一句话定位",),
    heading_replaces=("它在替代什么旧行为", "它在替代什么"),
    heading_takeaway=("可借鉴的做法", "对你的可迁移点", "对我的可迁移点"),
    heading_money=("商业模式",),
    heading_call=("判断", "结论"),
    heading_watch_next=("下一步看什么",),
    quiet_hints=("边界", "局限", "免责", "口径"),
    count_units={"picks": "{n} 个", "table": "{n} 项", "list": "{n} 条"},
    cta_default="完整分析",
    read_unit="chars",
    read_speed=350,
    t={
        "verdict_labels": {
            "strong": "重点研究",
            "notable": "持续观察",
            "unproven": "证据不足",
        },
        "skip": "跳到主要内容",
        "home_aria": "x-octo 首页",
        "nav": {"home": "今日机会", "products": "机会库", "reports": "判断档案", "takeaways": "打法库"},
        "theme": {"aria": "深色模式", "label": "明 / 暗"},
        "totop": "回到顶部",
        "lang": {"aria": "Switch to English", "label": "EN"},
        "footer": {
            "counts": "{total} 个案例 · {analysed} 份生意判断",
            "asof": "数据截至 {day}",
            "methodology": "方法与口径",
            "privacy": "隐私与统计",
        },
        "analytics": {
            "title": "帮助我们改进 x-octo",
            "body": " 允许后，我们会用匿名汇总数据了解哪些页面有用、读者从哪里来以及停留多久。",
            "allow": "允许统计",
            "decline": "不用，谢谢",
        },
        "privacy": {
            "kicker": "Privacy",
            "title": "隐私与统计",
            "lede": "我们只在你同意后才启用访问统计，用它改进内容与体验。",
            "what_title": "会收集什么",
            "what_body": "启用后，我们会统计页面浏览、来源渠道、大致地区、设备类型、停留与滚动情况，以及产品页、每日观察和筛选功能的使用情况。Clarity 还会记录经默认隐私遮蔽处理的页面互动，用于查看点击与阅读体验。",
            "choice_title": "你的选择",
            "choice_body": "统计默认关闭。你可以在访问时选择允许或拒绝；拒绝不会影响阅读网站内容。选择会保存在本机浏览器中，避免每次重复询问。",
            "services_title": "使用的服务",
            "services_body": "网站使用 Google Analytics 了解整体流量与内容表现，并使用 Microsoft Clarity 了解点击、滚动与页面体验。Clarity 默认会遮蔽敏感内容；这些服务各自按其隐私政策处理数据。",
            "no_personal_title": "我们不收集什么",
            "no_personal_body": "请勿在公开页面中提交个人信息。本站不会主动向统计服务发送姓名、邮箱、表单输入或其他直接身份信息。",
        },
        "methodology": {
            "title": "方法与口径",
            "lede": "x-octo 给要决定下一步押什么 AI 生意的人用。每天把值得看的产品翻译成：是不是生意、谁付钱、从哪切。不给买卖建议。",
            "reader_title": "不用先选你是谁",
            "reader_body": "同一份事实可以同时服务多个目的：想找切口就看「进入窗口」和「可以借走什么」；想判断质量就看「商业模式」与「接下来验证什么」；想了解影响就看它替代了什么旧行为。按你眼前的问题读，不给人贴身份标签。",
            "decision_title": "我们怎样把一个工具翻成一门生意",
            "decision_body": "每份案例先给 60 秒判断：真需求结论、商业模式、进入窗口、证据缺口；后面才是替代行为、数据、反例和完整推理。这样先帮助读者决定是否投入注意力，再允许他追查我们为什么这么判断。",
            "cadence_title": "每天自动更新",
            "cadence_body": "每天从全球公开信息里收新出现和已经跑出来的 AI 应用。平台、榜单、独立作者都会看。只把能讲成生意的留下来。不公开从哪抓，那是实现细节。",
            "what_title": "我们记录什么",
            "what_body": "每个案例会标明生意形态：还不是生意、开始收费、已有规模、格局已定。有公开使用数据的会展示规模和环比。增长只用来提出下一步该验证什么，不等于已经找到原因。",
            "editorial_title": "公开标准",
            "editorial_body": "只有能讲清它做什么、并给出一条方向判断的产品才会公开。被淘汰或信息不足的条目不会出现在公开页面和站点地图中。",
            "evidence_title": "如何使用这些信息",
            "evidence_body": "产品介绍来自公开资料，完整分析与每日观察属于编辑判断。引用具体结论时，请链接到对应的产品页或每日观察页，并保留页面显示的更新时间。",
            "takeaway_title": "生意判断是核心交付",
            "takeaway_body": "每个案例先回答：这是什么、是不是生意、谁付钱、从哪切、窗口在哪。能抄的做法按产品逻辑、话术、定价结构放在「方法」。诚实写「还不是生意」或「未披露」，比编一个像样的答案更有价值。",
            "updated": "最近数据更新",
        },
        "takeaways": {
            "title": "方法",
            "lede": "从案例里抽出来的可迁移方法，按产品逻辑、话术、定价结构分桶。给创业者回来偷招，不是再翻一遍产品。",
            "desc": "{total} 条生意方法，按产品逻辑 / 话术 / 定价结构分类",
            "note": "给创业者的方法，不是产品目录",
            "topic_product": "产品逻辑",
            "topic_product_note": "怎么做产品：可迁移的方法论",
            "topic_narrative": "话术",
            "topic_narrative_note": "怎么说话：可偷的文案结构",
            "topic_pricing": "定价结构",
            "topic_pricing_note": "怎么变现：可抄的定价策略",
            "count_suffix": "条",
            "empty": "暂无可借鉴条目",
        },
        "home": {
            "eyebrow": "全球 AI+ 机会 · 每日",
            "lede_title": "全球 AI+ 机会的每日记录",
            "lede_body": "每天自动更新，覆盖中文与英文生态。记录新项目、开源采用、实质性 AI 改造与跨国机会，并以公开证据给出真需求初判，说明已知边界。",
            "stat_total": "已收录",
            "what": "这是什么",
            "why_today": "本期为什么值得点开",
            "keep_asking": "继续追问",
            "dimensions": "机会维度",
            "money": "怎么赚钱",
            "meaning": "从哪切进去",
            "fresh_picks": "今天值得做判断的机会",
            "fresh_picks_note": "最多三个。看清是什么、谁付钱、从哪切。",
            "daily_flow": "全球 AI+ 机会流",
            "flow_title": "最新一期全球 AI+ 新发现",
            "flow_kicker": "本期事件",
            "first_discoveries": "本期值得点开的新发现",
            "first_discoveries_note": "从本期首次发现中挑选，并让不同类别轮流露面；项目次日进入机会库。",
            "first_discoveries_empty": "本期新发现将在采集与初判完成后出现。历史项目保留在机会库，不会被重新包装成新发现。",
            "proven_kicker": "已跑出来的生意",
            "proven_businesses": "已验证生意",
            "proven_businesses_note": "有公开规模或环比的成型产品。看真需求成不成立、窗口还在不在，不是热度榜。",
            "event_proven": "已验证生意",
            "update_kicker": "新增事实",
            "important_updates": "重要更新",
            "important_updates_note": "仅保留新增事实会改变产品、市场或需求判断的项目。",
            "market_kicker": "本期变化",
            "market_summary": "本期市场摘要",
            "market_summary_note": "收录本期产品之外的正式市场背景、行业变化与跨国差异，不以热度代替市场结论。",
            "market_industry": "本期首次发现涉及的行业",
            "market_industry_text": "本期首次发现项目涉及：{industries}。",
            "market_cross": "跨国供给差异",
            "market_cross_text": "已形成带覆盖范围的跨国机会判断：{products}。",
            "update_detail": "此次变化",
            "req_initial": "真需求初判",
            "opportunity_judgment": "机会判断",
            "action_investigate": "值得研究",
            "action_watch": "继续跟踪",
            "action_clue": "仅作方向线索",
            "action_avoid": "暂不投入",
            "evidence_boundary": "证据边界：{reason}",
            "boundary_supported": "公开证据支持{gate}闸门。",
            "boundary_insufficient": "公开证据尚未支持{gate}闸门。",
            "boundary_challenged": "公开反证正在挑战{gate}闸门。",
            "discovered_at": "xOcto 首次发现",
            "published_at": "公开时间",
            "req_pending": "判断待生成",
            "req_pending_note": "等待公开证据完成初步判断。",
            "event_first": "首次发现",
            "event_update": "实质更新",
            "event_market": "市场变化",
            "event_req": "真需求判断变化",
            "exit_k": "接着用",
            "exit_title": "接着用",
            "exit_note": "今天的判断用完了，这三处把能用的东西留在站上。",
            "exit_today": "今天的完整判断",
            "exit_today_note": "钩子后面的来龙去脉、边界和证据，三分钟读完。",
            "exit_cases": "已经在收钱的案例",
            "exit_cases_note": "按生意形态翻：谁付钱、窗口在哪、该不该进。",
            "exit_methods": "能抄走的做法",
            "exit_methods_note": "产品怎么做、话怎么说、钱怎么收。拿走就能用。",
            "more_opportunities": "值得继续挖的机会",
            "more_opportunities_note": "只放还在形成的切口；按旧流程和进入窗口排，不按名气排。",
            "replaces": "它替人省掉了哪一步",
            "takeaway": "可借鉴的做法",
            "direction": "趋势与切入",
            "notables": "还不是生意，但值得盯着",
            "notables_note": "问题清楚，付费证据还不够，先记下",
            "movers": "规模在动",
            "movers_note": "公开使用数据出现异常变化。相关不等于因果，只说明值得追问",
            "today_takeaway_title": "今天能拿走的",
            "today_takeaway_note": "白送一句能用的做法。明天还有。",
            "today_takeaway_from": "来自",
            "col_product": "产品",
            "col_growth": "环比",
            "col_scale": "使用规模",
            "col_function": "这是什么",
            "col_why": "趋势与切入",
            "cats": "按方向找",
            "latest_report": "本期判断",
            "daily_minutes": "一屏先看完",
            "daily_contract": "每日更新；每个完成期次交付一条方向判断、三个证据案例和一个能带走的动作。先扫一屏，需要时再深读。",
            "latest_report_note": "先记住今天这件事在往哪走",
            "latest_report_cta": "读完整判断",
            "fresh_kicker": "本期证据",
            "takeaway_kicker": "今天的动作",
            "past_kicker": "回看与校验",
            "past_reports": "这几天的判断",
            "past_reports_note": "旧判断不下架。回来对照新证据，看它有没有被后来的事推翻。",
            "report_fallback": "当日趋势判断与市场信号",
        },
        "products": {
            "title": "机会库",
            "note": "不是产品目录，而是一张 AI 生意机会地图。先按你要验证的问题找，再进案例看证据与边界。",
            "search_label": "先说你在找什么",
            "search_placeholder": "搜索产品、行业、工作或地区",
            "advanced_filters": "更多筛选：项目类型、细分行业、具体工作、地区与日期",
            "desc": "{total} 个 AI 生意案例：看真需求、付费路径、进入窗口与证据缺口。",
            "count": "当前结果",
            "results_jump": "查看结果 →",
            "f_category": "用户与场景",
            "f_type": "项目类型",
            "f_type_aria": "按项目类型筛选",
            "f_industry": "细分行业",
            "f_industry_aria": "按细分行业筛选",
            "f_job": "具体工作",
            "f_job_aria": "按具体工作筛选",
            "f_region": "地区 / 生态",
            "f_region_aria": "按地区或语言生态筛选",
            "f_evidence": "机会信号",
            "f_evidence_aria": "按开源状态筛选",
            "f_cross_aria": "按跨国机会筛选",
            "f_req": "真需求初判",
            "f_req_aria": "按真需求初判筛选",
            "f_discovered": "首次发现日期",
            "f_discovered_aria": "按 xOcto 首次发现日期筛选",
            "date_from": "自",
            "date_to": "至",
            "open_source": "开源项目",
            "cross_market": "跨国机会",
            "f_form": "生意形态",
            "f_form_aria": "按生意形态筛选",
            "f_stage": "证据成熟度",
            "f_status": "收录状态",
            "f_sort": "排序",
            "f_category_aria": "按方向筛选",
            "f_stage_aria": "按阶段筛选",
            "f_status_aria": "按评级筛选",
            "f_sort_aria": "排序方式",
            "all": "全部",
            "sort_opportunity": "创业切口",
            "sort_weight": "综合信号",
            "sort_growth": "增长",
            "sort_recent": "最近出现",
            "sort_name": "名称",
            "no_summary": "还没有简介，需要深挖才能判断",
            "money": "付费路径",
            "entry": "进入窗口",
            "empty": "这个组合下没有产品。",
            "reset": "清掉筛选，看全部 {total} 个",
            "show_more": "再显示 40 个",
            "showing": "已显示 {shown}/{total}",
            "stage_early_note": "刚收录，公开信号还有限，判断会随新信息更新。",
            "stage_proven_note": "已有公开使用数据，先看规模和变化，再看宣传文案。",
        },
        "product": {
            "story_kicker": "从用户的一天开始",
            "story_title": "它为什么会被需要",
            "story_scene": "工作现场",
            "story_call": "xOcto 的判断",
            "story_adoption": "采用动机",
            "story_adoption_title": "为什么有人会把它留在工作流里",
            "story_tension": "还不能轻易下结论的地方",
            "story_tension_title": "真正值得继续追问的矛盾",
            "story_for_user": "如果你正在做这项工作",
            "story_action_sep": "。",
            "story_evidence": "我们凭什么这样判断",
            "story_known": "公开事实",
            "story_inferred": "工作流推理",
            "story_unknown": "会改变判断的未知",
            "req_kicker": "需求与商业证据",
            "req_title": "它解决什么，以及是否已成为生意",
            "req_note": "先回答用户为什么需要或使用，再单独核验采用、付费、留存与交付。未知不是失败。",
            "req_signal": "需求判断",
            "req_evidence": "需求证据档",
            "req_job": "用户要完成什么",
            "req_pain": "它解决的痛点 / 问题",
            "req_alternative": "用户原来怎么做",
            "req_usage_reason": "为什么有人使用",
            "req_demand_maturity": "需求成熟度",
            "req_business_maturity": "商业证据成熟度",
            "req_basis": "判断依据",
            "basis_facts_only": "仅有公开事实",
            "basis_reasoned": "公开事实 + 工作流推理",
            "basis_behavioral": "公开事实 + 可观察行为",
            "basis_commercial": "公开事实 + 商业验证",
            "req_action": "当前建议",
            "action_investigate": "值得深入研究",
            "action_try": "值得试用",
            "action_dissect": "值得拆解",
            "action_watch": "继续观察",
            "action_clue": "仅作线索",
            "req_working_notes": "研究底稿",
            "demand_maturity_unclear": "用户任务尚未说清",
            "demand_maturity_job": "任务已识别，痛点强度未核验",
            "demand_maturity_evidenced": "痛点与需求有公开依据",
            "demand_maturity_challenged": "问题存在，但刚性受到反证",
            "business_maturity_unverified": "付费、留存与复购尚未核验",
            "business_maturity_pricing": "已看到定价路径，真实付费尚未核验",
            "business_maturity_adoption": "已有采用或关注证据，付费留存尚未核验",
            "business_maturity_paid": "已有付费或采购证据，留存尚未核验",
            "business_maturity_retained": "已有持续使用、留存或复购证据",
            "req_level": "判断层级 / 日期",
            "req_next": "下一步核验",
            "req_initial": "初步判断",
            "req_full": "完整判断",
            "req_pending": "尚未完成真需求初判；公开证据到位后将补充四项核验与下一步核验。",
            "req_reason_pending": "已记录判断，英文说明待补充。",
            "req_next_pending": "待根据公开证据补充英文核验说明。",
            "req_value": "价值",
            "req_consensus": "共识",
            "req_model": "模式",
            "req_truth": "求真",
            "req_supported": "已有支持",
            "req_insufficient": "证据不足",
            "req_challenged": "存在反证",
            "markets_kicker": "市场对照",
            "markets_title": "中英文生态与跨国机会",
            "cross_market": "跨国机会",
            "markets_pending": "尚未完成中英文市场对照。待覆盖范围和可核验证据补齐后再给出结论。",
            "ecosystem_zh": "中文生态",
            "ecosystem_en": "英文生态",
            "local_supply": "本地供给：",
            "demand_evidence": "需求证据：",
            "supply_not_found": "在已覆盖来源中未发现",
            "supply_emerging": "早期出现",
            "supply_established": "已有成熟供给",
            "demand_unknown": "尚未核验",
            "demand_early": "初步成立",
            "demand_validated": "信号明确",
            "market_coverage_pending": "已记录该市场的公开覆盖范围。",
            "evidence_kicker": "证据链",
            "evidence_title": "可核验公开证据",
            "evidence_product": "产品信息",
            "evidence_pricing": "定价信息",
            "evidence_open_source": "开源信息",
            "evidence_adoption": "采用信号",
            "evidence_market": "市场对照",
            "evidence_pain": "用户痛点",
            "evidence_workaround": "现有替代方式",
            "evidence_customer_case": "客户案例",
            "evidence_payment": "付费 / 采购",
            "evidence_retention": "留存 / 复购",
            "evidence_delivery": "交付结果",
            "evidence_link": "公开证据链接",
            "research_kicker": "继续查找",
            "research_title": "从产品名直接追到一手材料",
            "research_note": "产品官网缺失或当前链接只是线索时，从这些检索入口继续核验。",
            "research_official": "官网与文档",
            "research_pricing": "定价与套餐",
            "research_reviews": "用户评价与抱怨",
            "research_cases": "客户案例与结果",
            "research_alternatives": "替代品与对比",
            "lede_proven": "已有公开使用数据。判断要同时看它做什么、规模多大，以及变化是否能延续。",
            "lede_early": "公开信息还有限。下面只保留目前能确认的内容，后续会随新证据更新。",
            "builder": "团队 / 作者",
            "first_seen": "本站首次收录",
            "last_seen": "本站最近更新",
            "link": "产品官网",
            "link_open": "查看官网 ↗",
            "inspiration": "进入窗口",
            "replaces": "它替人省掉了哪一步",
            "money": "商业模式",
            "money_unknown": "收费未披露。公开信息里看不到定价，不编造。",
            "decision_kicker": "60 秒生意判断",
            "decision_title": "先决定它值不值得继续看",
            "decision_note": "先给出判断与下一步，再保留完整证据和反例。",
            "call": "一句判断",
            "watch_next": "接下来验证什么",
            "takeaway_short": "可以借走什么",
            "roles_kicker": "把同一事实拆成三个判断",
            "roles_title": "不选身份，按此刻关心的问题读",
            "for_founder_k": "怎样切入 / 可以借走什么",
            "for_investor_k": "证据与风险",
            "for_public_k": "会改变什么",
            "for_investor": {
                "not_business": "还不是一门生意。可以当信号看，不要当成公司看。",
                "charging": "已经开始收费。下一步看谁在反复付钱，以及这点钱够不够撑住团队。",
                "scaled": "已有公开使用规模。要问的是规模能不能变成留存和付费，还是只被平台导流。",
                "settled": "格局已定。这是观察位不是进入位，看它会不会改行业定价，不看它还能不能被复制。",
            },
            "for_public": {
                "AI + 创作": "会改做图、做视频、写东西的人怎么开工。不靠内容吃饭的人，可以当热闹看。",
                "AI + 开发": "主要改写软件的人怎么干活。除非你靠软件吃饭，否则先不用管。",
                "AI + 商业": "会改公司里成交、客服、招采这些岗位怎么干活。",
                "AI + 效率": "会改办公里重复的那几步：记、整理、交文档。",
                "AI + 生活": "可能碰到学、吃、玩、出行，但多数还只是尝鲜。",
                "通用助手": "聊天、搜索、写东西的默认入口可能换人。你会直接碰到。",
                "基础层": "这是底层零件。你不会直接打开它，但以后很多应用可能长在它上面。",
            },
            "takeaway": "可借鉴的做法",
            "direction": "趋势与切入",
            "boards": "",
            "boards_note": "",
            "none_lead": "完整分析还没写。先看上面的方向判断。",
            "none_sub": "目前公开信息有限，判断会随新证据更新。",
            "none_early": "它刚被收录，尚缺可验证的使用数据。",
            "none_proven": "它已有使用数据，后续更值得看规模和变化能否延续。",
            "none_siblings": "同类产品的完整分析：",
            "sibling_sep": "、",
            "notes": "笔记",
            "onward_aria": "继续浏览",
            "siblings": "同类产品",
            "cat_all": "{category} 共 {total} 个 →",
            "prev": "上一个",
            "next": "下一个",
        },
        "report": {
            "kicker": "今日判断",
            "minutes": "约 {n} 分钟",
            "toc": "本期目录",
            "toc_count": "{n} 个版块",
            "rail_aria": "版块导航",
            "rail_now": "本期",
            "rail_past": "往期",
            "rail_all": "查看全部往期",
            "share": "分享这期",
            "share_copied": "链接已复制",
            "share_manual": "浏览器无法自动复制，请手动复制下面的链接：",
            "archive_title": "全部往期判断",
            "archive_lede": "所有每日生意判断按日期永久归档；首页列表满了，也不会删除更早的内容。",
            "archive_count": "已归档",
            "archive_empty": "还没有可回看的观察。",
        },
    },
)


EN = Locale(
    key="en",
    lang="en",
    hreflang="en",
    og_locale="en_US",
    prefix="en/",
    content_subdir="en",
    site_name="x-octo",
    site_tagline="Business judgment on AI products",
    site_desc="For people deciding what to bet on next: one daily call, a few cases that show who pays. Not investment advice.",
    categories=dict(CATEGORY_EN),
    stages={"early": "Early", "proven": "Has usage data"},
    forms={
        "not_business": "Not a business yet",
        "charging": "Started charging",
        "scaled": "Already at scale",
        "settled": "Category is set",
    },
    statuses={
        "analyzed": "Analyzed",
        "watching": "Under watch",
        "market_context": "Market context",
        "queued": "Queued",
        "pending_filter": "New",
        "rejected": "Rejected",
    },
    verdict_words=("Strong pick", "Worth watching", "Unproven"),
    metrics={
        "points": "Community score",
        "stars": "Open-source traction",
        "visits": "Monthly visits",
        "mau": "MAU",
        "mom": "MoM",
    },
    boards=dict(BOARD_EN),
    heading_excerpt=("What it is in one line",),
    heading_replaces=("What old behavior it replaces",),
    heading_takeaway=("What you can take from it",),
    heading_money=("Business model",),
    heading_call=("The call", "Verdict"),
    heading_watch_next=("What to watch next",),
    quiet_hints=("Limits", "Caveats", "Scope", "Disclaimer"),
    count_units={"picks": "{n} picks", "table": "{n} rows", "list": "{n} items"},
    cta_default="Full analysis",
    # 英文按词数算，不是字数。用字数算会把 5 分钟的文章报成 20 分钟。
    read_unit="words",
    read_speed=230,
    t={
        "verdict_labels": {
            "strong": "Worth studying",
            "notable": "Keep watching",
            "unproven": "Insufficient evidence",
        },
        "skip": "Skip to main content",
        "home_aria": "x-octo home",
        # 导航要短。英文词比中文长，顶栏在 375px 上本来就紧，
        # 完整说法留给页面标题
        "nav": {"home": "Today", "products": "Opportunity map", "reports": "Calls archive", "takeaways": "Playbook"},
        # "Light / Dark" 在 375px 上会把顶栏撑出横向滚动 —— 顶栏现在有三个控件，
        # 英文词又比中文长。按钮本来就只有一个功能，一个词说得清
        "theme": {"aria": "Dark mode", "label": "Theme"},
        "totop": "Back to top",
        "lang": {"aria": "切换到中文版", "label": "中文"},
        "footer": {
            "counts": "{total} cases · {analysed} business reads",
            "asof": "Data through {day}",
            "methodology": "Methodology",
            "privacy": "Privacy & analytics",
        },
        "analytics": {
            "title": "Help improve x-octo",
            "body": " If you allow it, we use aggregated analytics to understand which pages help, where readers come from, and how they engage.",
            "allow": "Allow analytics",
            "decline": "No thanks",
        },
        "privacy": {
            "kicker": "Privacy",
            "title": "Privacy & analytics",
            "lede": "We enable visitor analytics only after you agree, so we can improve the work and the reading experience.",
            "what_title": "What we collect",
            "what_body": "After you enable analytics, we collect page views, traffic sources, approximate regions, device types, time and scroll engagement, and use of product pages, daily observations, and filters. Clarity also records privacy-masked page interactions to help us understand clicks and reading experience.",
            "choice_title": "Your choice",
            "choice_body": "Analytics are off by default. You can allow or decline when you visit; declining does not change your access to the site. Your choice is stored in your browser so we do not repeatedly ask.",
            "services_title": "Services we use",
            "services_body": "We use Google Analytics to understand overall traffic and content performance, and Microsoft Clarity to understand clicks, scrolling, and page experience. Clarity masks sensitive content by default; each service processes data under its own privacy policy.",
            "no_personal_title": "What we do not collect",
            "no_personal_body": "Please do not submit personal information on public pages. We do not intentionally send names, email addresses, form inputs, or other direct identifiers to our analytics services.",
        },
        "methodology": {
            "title": "Methodology",
            "lede": "x-octo is for people deciding what AI business to bet on next. Each day it translates a product into: is it a business, who pays, where to enter. Not investment advice.",
            "reader_title": "You do not have to choose who you are first",
            "reader_body": "One set of facts can serve several purposes: start with the entry window and what to borrow when looking for a wedge; with the business model and what to validate when testing quality; and with the old behavior replaced when assessing impact. Read for the question in front of you, not a label.",
            "decision_title": "How we translate a tool into a business",
            "decision_body": "Every case begins with a 60-second read: the demand call, business model, entry window, and evidence gap. Only then come the old behavior, data, counterevidence, and full reasoning. It lets readers decide whether to spend attention before asking why we made the call.",
            "cadence_title": "Updated every day",
            "cadence_body": "Every day we collect newly launched and already-scaled AI apps from public information worldwide. Platforms, rankings, and independent writers are all in the net. Only what can be told as a business is published. We do not list sources; that is an implementation detail.",
            "what_title": "What we record",
            "what_body": "Each case is labeled by business form: not a business yet, started charging, already at scale, or the category is set. Products with public usage data show scale and month-over-month change. Growth points to what to verify next; it does not prove a cause.",
            "editorial_title": "What becomes public",
            "editorial_body": "A product is published only when we can say what it does and give one directional judgment. Rejected or incomplete entries stay off public pages and the sitemap.",
            "evidence_title": "How to use this work",
            "evidence_body": "Product descriptions draw on public material; full analyses and daily observations are editorial judgments. When citing a conclusion, link to its product or daily-observation page and keep the displayed update date.",
            "takeaway_title": "Business judgment is the core deliverable",
            "takeaway_body": "Every case answers: what it is, whether it is a business, who pays, where to enter, and what the window is. Copyable moves live on Playbook. Honest 'not a business yet' or 'not disclosed' beats a polished guess.",
            "updated": "Latest data update",
        },
        "takeaways": {
            "title": "Playbook",
            "lede": "Transferable methods from the cases, grouped by product logic, narrative, and pricing. For founders who come back to steal a move — not another product list.",
            "desc": "{total} business methods, grouped by product logic / narrative / pricing",
            "note": "A playbook for founders — not a product catalog",
            "topic_product": "Product logic",
            "topic_product_note": "How to build: transferable methodology",
            "topic_narrative": "Narrative",
            "topic_narrative_note": "How to talk: stealable copy structures",
            "topic_pricing": "Pricing structure",
            "topic_pricing_note": "How to monetize: copyable pricing moves",
            "count_suffix": "entries",
            "empty": "No takeaways yet",
        },
        "home": {
            "eyebrow": "GLOBAL AI+ OPPORTUNITIES · DAILY",
            "lede_title": "A daily record of global AI+ opportunities",
            "lede_body": "Updated every day across Chinese and English ecosystems. It records new projects, open-source adoption, material AI transformations, and cross-market opportunities, with public evidence and an initial demand assessment that states what remains open.",
            "stat_total": "Tracked",
            "what": "What it is",
            "why_today": "Why it matters in this edition",
            "keep_asking": "The question to keep asking",
            "dimensions": "Opportunity dimensions",
            "money": "How it makes money",
            "meaning": "Where to enter",
            "fresh_picks": "Opportunities worth judging today",
            "fresh_picks_note": "At most three. What it is, who pays, where to enter.",
            "daily_flow": "GLOBAL AI+ OPPORTUNITY FLOW",
            "flow_title": "The latest global AI+ discoveries",
            "flow_kicker": "This edition",
            "first_discoveries": "New discoveries worth opening",
            "first_discoveries_note": "Selected from this edition's first discoveries, with room for different categories. Entries move to the library the next day.",
            "first_discoveries_empty": "New discoveries appear after this edition's collection and initial assessment finish. Historical projects stay in the library and are not repackaged as new.",
            "proven_kicker": "Businesses already running",
            "proven_businesses": "Proven businesses",
            "proven_businesses_note": "Formed products with public scale or month-on-month change. Read whether demand holds and whether the window is still open — not a heat ranking.",
            "event_proven": "Proven business",
            "update_kicker": "New evidence",
            "important_updates": "Important updates",
            "important_updates_note": "Only changes that alter the product, market, or demand view appear here.",
            "market_kicker": "This edition’s change",
            "market_summary": "Market summary for this edition",
            "market_summary_note": "It includes formal market context beyond this edition’s products, industry shifts, and cross-market differences; popularity is not a market conclusion.",
            "market_industry": "Industries in this edition’s first discoveries",
            "market_industry_text": "This edition’s first discoveries involve: {industries}.",
            "market_cross": "Cross-market supply difference",
            "market_cross_text": "Cross-market opportunities with recorded coverage: {products}.",
            "update_detail": "What changed",
            "req_initial": "Initial demand assessment",
            "opportunity_judgment": "Opportunity call",
            "action_investigate": "Worth investigating",
            "action_watch": "Keep watching",
            "action_clue": "Directional clue only",
            "action_avoid": "Do not enter yet",
            "evidence_boundary": "Evidence boundary: {reason}",
            "boundary_supported": "Public evidence supports the {gate} gate.",
            "boundary_insufficient": "Public evidence does not yet establish the {gate} gate.",
            "boundary_challenged": "Public counterevidence challenges the {gate} gate.",
            "discovered_at": "First discovered by xOcto",
            "published_at": "Published",
            "req_pending": "Review pending",
            "req_pending_note": "The initial read follows when public evidence is available.",
            "event_first": "First discovery",
            "event_update": "Material update",
            "event_market": "Market change",
            "event_req": "Demand assessment change",
            "exit_k": "Keep using it",
            "exit_title": "Keep using it",
            "exit_note": "The daily call is the start. These three keep the usable pieces on the site.",
            "exit_today": "Today's call in full",
            "exit_today_note": "The argument behind the hook, plus limits and evidence. A three-minute read.",
            "exit_cases": "Cases already charging",
            "exit_cases_note": "Browse by business form: who pays, where the window is, whether to enter.",
            "exit_methods": "Moves you can copy",
            "exit_methods_note": "How to build, how to talk, how to charge. Take one and use it.",
            "more_opportunities": "Opportunities worth digging into",
            "more_opportunities_note": "Only forming entries: ordered by workflow and entry window, not fame.",
            "replaces": "The step it removes",
            "takeaway": "What to borrow",
            "direction": "Trend and where to enter",
            "notables": "Not a business yet — keep watching",
            "notables_note": "The problem is clear; paying evidence is not",
            "movers": "Scale is moving",
            "movers_note": "Public usage data moved unusually. Correlation is not causation; it is a reason to ask",
            "today_takeaway_title": "Take this with you",
            "today_takeaway_note": "One usable move, given away. There will be another tomorrow.",
            "today_takeaway_from": "From",
            "col_product": "Product",
            "col_growth": "MoM",
            "col_scale": "Usage scale",
            "col_function": "What it is",
            "col_why": "Trend and where to enter",
            "cats": "Browse by direction",
            "latest_report": "This edition’s call",
            "daily_minutes": "Start with one screen",
            "daily_contract": "Updated daily; each completed edition delivers one directional call, three evidence-backed cases, and one usable move. Scan one screen first, then go deeper when needed.",
            "latest_report_note": "One sentence on where this is heading",
            "latest_report_cta": "Read the full call",
            "fresh_kicker": "Evidence in this edition",
            "takeaway_kicker": "Today's move",
            "past_kicker": "Revisit and test",
            "past_reports": "The last few days",
            "past_reports_note": "Old calls stay up. Return to test whether later evidence held them up or overturned them.",
            "report_fallback": "Trend calls and market signals for the day",
        },
        "products": {
            "title": "Opportunity map",
            "note": "Not a product directory: a map of AI business opportunities. Start with the question you need to test, then open a case for evidence and limits.",
            "search_label": "Start with what you need",
            "search_placeholder": "Search products, industries, work, or markets",
            "advanced_filters": "More filters: project type, industry, work, market, and date",
            "desc": "{total} AI business cases: true demand, payment path, entry window, and the remaining evidence gap.",
            "count": "Showing",
            "results_jump": "View results →",
            "f_category": "User & setting",
            "f_type": "Project type",
            "f_type_aria": "Filter by project type",
            "f_industry": "Industry",
            "f_industry_aria": "Filter by industry",
            "f_job": "Specific work",
            "f_job_aria": "Filter by specific work",
            "f_region": "Market / ecosystem",
            "f_region_aria": "Filter by market or language ecosystem",
            "f_evidence": "Opportunity signal",
            "f_evidence_aria": "Filter by open-source status",
            "f_cross_aria": "Filter by cross-market opportunity",
            "f_req": "Initial demand assessment",
            "f_req_aria": "Filter by initial demand assessment",
            "f_discovered": "First-discovered date",
            "f_discovered_aria": "Filter by xOcto first-discovered date",
            "date_from": "From",
            "date_to": "To",
            "open_source": "Open source",
            "cross_market": "Cross-market opportunity",
            "f_form": "Business form",
            "f_form_aria": "Filter by business form",
            "f_stage": "Evidence maturity",
            "f_status": "Editorial status",
            "f_sort": "Sort",
            "f_category_aria": "Filter by direction",
            "f_stage_aria": "Filter by stage",
            "f_status_aria": "Filter by rating",
            "f_sort_aria": "Sort order",
            "all": "All",
            "sort_opportunity": "Entry potential",
            "sort_weight": "Signal strength",
            "sort_growth": "Growth",
            "sort_recent": "Last seen",
            "sort_name": "Name",
            "no_summary": "No description yet — it takes digging to judge this one",
            "money": "Payment path",
            "entry": "Entry window",
            "empty": "Nothing matches this combination.",
            "reset": "Clear filters, show all {total}",
            "show_more": "Show 40 more",
            "showing": "Showing {shown} of {total}",
            "stage_early_note": "Recently added. Public signals are still limited and the view will update with new evidence.",
            "stage_proven_note": "There is public usage data. Look at scale and change alongside the pitch.",
        },
        "product": {
            "story_kicker": "Start inside the user's day",
            "story_title": "Why this would be needed",
            "story_scene": "The work as it happens",
            "story_call": "xOcto's call",
            "story_adoption": "Adoption motive",
            "story_adoption_title": "Why someone would keep it in the workflow",
            "story_tension": "Where the easy answer breaks down",
            "story_tension_title": "The tension worth following",
            "story_for_user": "If this is your job",
            "story_action_sep": ". ",
            "story_evidence": "What this judgment rests on",
            "story_known": "Public fact",
            "story_inferred": "Workflow reasoning",
            "story_unknown": "The unknown that could change the call",
            "req_kicker": "Demand assessment",
            "req_title": "Demand assessment",
            "req_note": "It checks value, adoption, payment, and delivery against public evidence; limited evidence does not mean demand is absent.",
            "req_signal": "Demand call",
            "req_evidence": "Evidence confidence",
            "req_job": "What users need to get done",
            "req_pain": "Pain or problem addressed",
            "req_alternative": "How users do it today",
            "req_usage_reason": "Why people use it",
            "req_demand_maturity": "Demand maturity",
            "req_business_maturity": "Business evidence maturity",
            "req_basis": "Basis of judgment",
            "basis_facts_only": "Public facts only",
            "basis_reasoned": "Public facts + workflow reasoning",
            "basis_behavioral": "Public facts + observable behavior",
            "basis_commercial": "Public facts + commercial validation",
            "req_action": "Recommended action",
            "action_investigate": "Investigate further",
            "action_try": "Worth trying",
            "action_dissect": "Worth dissecting",
            "action_watch": "Keep watching",
            "action_clue": "Clue only",
            "req_working_notes": "Research notes",
            "demand_maturity_unclear": "The user job is not yet clear",
            "demand_maturity_job": "Job identified; pain intensity not yet verified",
            "demand_maturity_evidenced": "Public evidence supports the pain and demand",
            "demand_maturity_challenged": "The problem exists, but urgency is challenged",
            "business_maturity_unverified": "Payment, retention, and repeat use not yet verified",
            "business_maturity_pricing": "Pricing path visible; actual payment not yet verified",
            "business_maturity_adoption": "Adoption or attention visible; payment and retention unverified",
            "business_maturity_paid": "Payment or procurement visible; retention unverified",
            "business_maturity_retained": "Repeat use, retention, or renewal is evidenced",
            "req_level": "Review level / date",
            "req_next": "Next check",
            "req_initial": "Initial review",
            "req_full": "Full review",
            "req_pending": "The initial demand assessment is pending. Four checks and the next check will appear once public evidence is sufficient.",
            "req_reason_pending": "The assessment is recorded; an English explanation is pending.",
            "req_next_pending": "An English validation note will follow from the public evidence.",
            "req_value": "Value",
            "req_consensus": "Consensus",
            "req_model": "Model",
            "req_truth": "Truth",
            "req_supported": "Supported",
            "req_insufficient": "Insufficient evidence",
            "req_challenged": "Challenged",
            "markets_kicker": "Market comparison",
            "markets_title": "Chinese and English ecosystems",
            "cross_market": "Cross-market opportunity",
            "markets_pending": "The Chinese–English market comparison is not complete yet. A conclusion follows only after its coverage and verifiable evidence are recorded.",
            "ecosystem_zh": "Chinese ecosystem",
            "ecosystem_en": "English ecosystem",
            "local_supply": "Local supply: ",
            "demand_evidence": "Demand evidence: ",
            "supply_not_found": "Not found in covered sources",
            "supply_emerging": "Emerging",
            "supply_established": "Established supply",
            "demand_unknown": "Not yet verified",
            "demand_early": "Early signal",
            "demand_validated": "Clear signal",
            "market_coverage_pending": "Public coverage has been recorded for this market.",
            "evidence_kicker": "Evidence trail",
            "evidence_title": "Verifiable public evidence",
            "evidence_product": "Product information",
            "evidence_pricing": "Pricing information",
            "evidence_open_source": "Open-source signal",
            "evidence_adoption": "Adoption signal",
            "evidence_market": "Market comparison",
            "evidence_pain": "User pain",
            "evidence_workaround": "Current workaround",
            "evidence_customer_case": "Customer case",
            "evidence_payment": "Payment / procurement",
            "evidence_retention": "Retention / renewal",
            "evidence_delivery": "Delivery outcome",
            "evidence_link": "Public evidence link",
            "research_kicker": "Keep researching",
            "research_title": "Go from the product name to primary material",
            "research_note": "Use these searches when the official site is missing or the current link is only a lead.",
            "research_official": "Official site and docs",
            "research_pricing": "Pricing and plans",
            "research_reviews": "User reviews and complaints",
            "research_cases": "Customer cases and outcomes",
            "research_alternatives": "Alternatives and comparisons",
            "lede_proven": "There is public usage data. The useful view is what it does, its scale, and whether the change lasts.",
            "lede_early": "Public information is still limited. This page keeps to what can be confirmed and updates as new evidence appears.",
            "builder": "Team / maker",
            "first_seen": "First tracked here",
            "last_seen": "Last updated here",
            "link": "Product site",
            "link_open": "Visit site ↗",
            "inspiration": "Entry window",
            "replaces": "The step it removes",
            "money": "Business model",
            "money_unknown": "Pricing not disclosed. Public materials don't show a price, so we won't invent one.",
            "decision_kicker": "60-second business read",
            "decision_title": "Decide if this deserves more of your time",
            "decision_note": "The call and next move come first; the full read retains the evidence and counterevidence.",
            "call": "The call",
            "watch_next": "What to validate next",
            "takeaway_short": "What to borrow",
            "roles_kicker": "Three questions, one set of facts",
            "roles_title": "Read for what matters now, not for a fixed identity",
            "for_founder_k": "Entry and what to borrow",
            "for_investor_k": "Evidence and risk",
            "for_public_k": "What it changes",
            "for_investor": {
                "not_business": "Not a business yet. Treat it as a signal, not a company.",
                "charging": "It has started charging. Next: who pays twice, and whether that covers a team.",
                "scaled": "Public usage is real. The question is whether scale becomes retention and revenue, or just inbound traffic.",
                "settled": "The category is set. This is a seat to watch, not a seat to enter. Watch whether it resets industry pricing, not whether it can be copied.",
            },
            "for_public": {
                "AI + 创作": "This changes how people who make images, video, or copy start work. If you don't live off content, treat it as news.",
                "AI + 开发": "This changes how software gets written. Unless you live off software, you can skip it.",
                "AI + 商业": "This changes how sales, support, and procurement get done inside companies.",
                "AI + 效率": "This changes the repetitive office steps: capture, sort, hand in.",
                "AI + 生活": "It may touch learning, food, play, or travel. Most of it is still a taste.",
                "通用助手": "The default door for chat, search, and writing may change. You will feel it.",
                "基础层": "This is plumbing. You won't open it, but later apps may sit on it.",
            },
            "takeaway": "What to borrow",
            "direction": "Trend and where to enter",
            "boards": "",
            "boards_note": "",
            "none_lead": "There is no full analysis yet. Start with the direction above.",
            "none_sub": "Public information is limited; this view will update as more evidence appears.",
            "none_early": "It was recently added and does not yet have verifiable usage data.",
            "none_proven": "It has usage data; the next question is whether its scale and change will hold.",
            "none_siblings": "Full analyses of similar products:",
            "sibling_sep": ", ",
            "notes": "Notes",
            "onward_aria": "Keep browsing",
            "siblings": "Similar products",
            "cat_all": "{total} in {category} →",
            "prev": "Previous",
            "next": "Next",
        },
        "report": {
            "kicker": "Today's call",
            "minutes": "{n} min read",
            "toc": "In this issue",
            "toc_count": "{n} sections",
            "rail_aria": "Section navigation",
            "rail_now": "This issue",
            "rail_past": "Past issues",
            "rail_all": "View all issues",
            "share": "Share this issue",
            "share_copied": "Link copied",
            "share_manual": "Your browser could not copy automatically. Copy this link:",
            "archive_title": "All past calls",
            "archive_lede": "Every daily business call stays archived by date. Older work is not deleted when the home-page list fills up.",
            "archive_count": "Archived",
            "archive_empty": "No observations to revisit yet.",
        },
    },
)


LOCALES = (ZH, EN)


def other(locale: Locale) -> Locale:
    """另一个语种。语言切换按钮和 hreflang 都要用。"""
    return EN if locale.key == "zh" else ZH
