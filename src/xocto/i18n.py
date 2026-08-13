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
    statuses: dict[str, str]
    verdict_words: tuple[str, str, str]  # 与 VERDICT_KEYS 一一对应
    metrics: dict[str, str]
    boards: dict[str, str]

    # 分析正文里要抽的二级标题（按顺序试，第一个命中的算数）
    heading_excerpt: tuple[str, ...]
    heading_replaces: tuple[str, ...]
    heading_takeaway: tuple[str, ...]

    # 报告解析
    quiet_hints: tuple[str, ...]  # 命中就降权：免责/边界类版块不该和判断抢注意力
    count_units: dict[str, str]  # picks / table / list 各自的数量说法
    cta_default: str  # "→ [完整分析](...)" 没写文字时的兜底
    read_unit: str  # "chars"（中文按字数）/ "words"（英文按词数）
    read_speed: int  # 每分钟

    t: dict[str, Any]  # 界面文案，模板里用 t.xxx.yyy

    def category(self, name: str) -> str:
        return self.categories.get(name, name)

    def status(self, key: str) -> str:
        return self.statuses.get(key, key)

    def stage(self, key: str) -> str:
        return self.stages.get(key, key)

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
    site_tagline="全球 AI 应用雷达",
    site_desc="每天追踪新出现与已跑出规模的 AI 应用，讲清它替人省去了哪一步、又有哪些真实信号。",
    categories={name: name for name in CATEGORY_EN},
    stages={"early": "刚冒头", "proven": "已有使用数据"},
    statuses={
        "analyzed": "已分析",
        "watching": "持续观察",
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
        "nav": {"home": "首页", "products": "全部产品", "reports": "每日观察"},
        "theme": {"aria": "深色模式", "label": "明 / 暗"},
        "totop": "回到顶部",
        "lang": {"aria": "Switch to English", "label": "EN"},
        "footer": {
            "counts": "{total} 个产品 · {analysed} 份深度分析",
            "asof": "数据截至 {day}",
        },
        "home": {
            "lede_pre": "已收录 ",
            "lede_post": " 个值得研究的产品",
            "lede_body": "每天都有新的 AI 应用出现。这里优先留下能说清它替人完成哪一步、又有哪些真实信号的产品。",
            "stat_total": "已收录",
            "picks": "编辑精选",
            "picks_note": "从产品中提炼出的可借鉴做法",
            "replaces": "它替人省掉了哪一步",
            "takeaway": "可借鉴的做法",
            "notables": "值得留意",
            "notables_note": "已经看清它解决的问题，仍在等待更多证据",
            "movers": "增长信号",
            "movers_note": "这里记录可能解释增长的产品、需求或分发因素；相关不等于因果",
            "col_product": "产品",
            "col_growth": "环比",
            "col_scale": "使用规模",
            "col_function": "核心功能",
            "col_why": "增长看点",
            "cats": "按方向找",
            "latest_report": "最新观察",
            "latest_report_note": "先记住一条值得回看的变化",
            "latest_report_cta": "读完整观察",
            "past_reports": "往期观察",
            "past_reports_note": "回看后来被验证或推翻的判断",
            "report_fallback": "当日趋势判断与市场信号",
        },
        "products": {
            "title": "全部产品",
            "note": "这里同时收录刚发布的产品和已有使用数据的应用：前者看它解决什么问题，后者看它的规模和变化。",
            "desc": "全部 {total} 个 AI 应用：看它替人完成哪一步，以及已有的使用信号。",
            "count": "当前结果",
            "f_category": "方向",
            "f_stage": "发展阶段",
            "f_status": "收录状态",
            "f_sort": "排序",
            "f_category_aria": "按方向筛选",
            "f_stage_aria": "按阶段筛选",
            "f_status_aria": "按评级筛选",
            "f_sort_aria": "排序方式",
            "all": "全部",
            "sort_weight": "综合信号",
            "sort_growth": "增长",
            "sort_recent": "最近出现",
            "sort_name": "名称",
            "no_summary": "还没有简介，需要深挖才能判断",
            "empty": "这个组合下没有产品。",
            "reset": "清掉筛选，看全部 {total} 个",
            "stage_early_note": "刚收录，公开信号还有限，判断会随新信息更新。",
            "stage_proven_note": "已有公开使用数据，先看规模和变化，再看宣传文案。",
        },
        "product": {
            "lede_proven": "已有公开使用数据。判断要同时看它做什么、规模多大，以及变化是否能延续。",
            "lede_early": "公开信息还有限。下面只保留目前能确认的内容，后续会随新证据更新。",
            "builder": "团队 / 作者",
            "first_seen": "本站首次收录",
            "last_seen": "本站最近更新",
            "link": "产品官网",
            "link_open": "查看官网 ↗",
            "inspiration": "值得借鉴的一点",
            "replaces": "它替人省掉了哪一步",
            "takeaway": "可借鉴的做法",
            "boards": "",
            "boards_note": "",
            "none_lead": "这款产品尚未形成完整分析。",
            "none_sub": "目前公开信息有限，以下判断会随新证据持续更新。",
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
            "kicker": "每日观察",
            "minutes": "约 {n} 分钟",
            "toc": "本期目录",
            "toc_count": "{n} 个版块",
            "rail_aria": "版块导航",
            "rail_now": "本期",
            "rail_past": "往期",
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
    site_tagline="Global AI product radar",
    site_desc="A daily radar for new and proven AI products: what they help people do, "
    "and which public signals are worth tracking.",
    categories=dict(CATEGORY_EN),
    stages={"early": "Early", "proven": "Has usage data"},
    statuses={
        "analyzed": "Analyzed",
        "watching": "Under watch",
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
        "nav": {"home": "Home", "products": "Products", "reports": "Daily"},
        # "Light / Dark" 在 375px 上会把顶栏撑出横向滚动 —— 顶栏现在有三个控件，
        # 英文词又比中文长。按钮本来就只有一个功能，一个词说得清
        "theme": {"aria": "Dark mode", "label": "Theme"},
        "totop": "Back to top",
        "lang": {"aria": "切换到中文版", "label": "中文"},
        "footer": {
            "counts": "{total} products · {analysed} deep dives",
            "asof": "Data through {day}",
        },
        "home": {
            # 数字必须打头（它是整屏唯一的高亮件），后面得跟上名词 ——
            # 只写 "worth your time today" 会变成"0 个什么？"
            "lede_pre": "",
            "lede_post": " products worth researching",
            "lede_body": "New AI products appear every day. We prioritize the ones that make clear "
            "what step they help people complete, and what public signals support the case.",
            "stat_total": "Tracked",
            "picks": "Editor’s picks",
            "picks_note": "Practical ideas drawn from the products themselves",
            "replaces": "The step it removes",
            "takeaway": "What to borrow",
            "notables": "On the radar",
            "notables_note": "The problem is clear; we are still waiting for more evidence",
            "movers": "Growth signals",
            "movers_note": "These are possible product, demand, or distribution explanations for growth; correlation is not causation",
            "col_product": "Product",
            "col_growth": "MoM",
            "col_scale": "Usage scale",
            "col_function": "Core function",
            "col_why": "Growth angle",
            "cats": "Browse by direction",
            "latest_report": "Latest observation",
            "latest_report_note": "One change from today worth keeping in view",
            "latest_report_cta": "Read the full observation",
            "past_reports": "Past observations",
            "past_reports_note": "Calls to revisit as evidence accumulates",
            "report_fallback": "Trend calls and market signals for the day",
        },
        "products": {
            "title": "All products",
            "note": "This list covers newly released products and apps with public usage data: "
            "first see what they help people do, then see whether the signal is holding.",
            "desc": "All {total} AI products on the radar: what they help people do and the public signals behind them.",
            "count": "Showing",
            "f_category": "Direction",
            "f_stage": "Maturity",
            "f_status": "Editorial status",
            "f_sort": "Sort",
            "f_category_aria": "Filter by direction",
            "f_stage_aria": "Filter by stage",
            "f_status_aria": "Filter by rating",
            "f_sort_aria": "Sort order",
            "all": "All",
            "sort_weight": "Signal strength",
            "sort_growth": "Growth",
            "sort_recent": "Last seen",
            "sort_name": "Name",
            "no_summary": "No description yet — it takes digging to judge this one",
            "empty": "Nothing matches this combination.",
            "reset": "Clear filters, show all {total}",
            "stage_early_note": "Recently added. Public signals are still limited and the view will update with new evidence.",
            "stage_proven_note": "There is public usage data. Look at scale and change alongside the pitch.",
        },
        "product": {
            "lede_proven": "There is public usage data. The useful view is what it does, its scale, and whether the change lasts.",
            "lede_early": "Public information is still limited. This page keeps to what can be confirmed and updates as new evidence appears.",
            "builder": "Team / maker",
            "first_seen": "First tracked here",
            "last_seen": "Last updated here",
            "link": "Product site",
            "link_open": "Visit site ↗",
            "inspiration": "A useful idea here",
            "replaces": "The step it removes",
            "takeaway": "What to borrow",
            "boards": "",
            "boards_note": "",
            "none_lead": "There is no full analysis of this product yet.",
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
            "kicker": "Daily read",
            "minutes": "{n} min read",
            "toc": "In this issue",
            "toc_count": "{n} sections",
            "rail_aria": "Section navigation",
            "rail_now": "This issue",
            "rail_past": "Past issues",
        },
    },
)


LOCALES = (ZH, EN)


def other(locale: Locale) -> Locale:
    """另一个语种。语言切换按钮和 hreflang 都要用。"""
    return EN if locale.key == "zh" else ZH
