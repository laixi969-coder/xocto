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
        """"强烈推荐（但先查域名）" → "strong"。认不出返回空串。

        用前缀匹配而不是全等：作者会在评级后面加括号补充，
        那是给人看的，不该让徽章失去颜色。
        """
        for word, key in zip(self.verdict_words, VERDICT_KEYS):
            if raw.startswith(word):
                return key
        return ""

    def verdict_rank(self, raw: str) -> int:
        key = self.verdict_key(raw)
        return VERDICT_KEYS.index(key) if key in VERDICT_KEYS else 9

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
    site_desc="每天挖全球新冒出来的 AI 应用，砍掉噪音，判断它解决了什么真需求。",
    categories={name: name for name in CATEGORY_EN},
    stages={"early": "刚冒头", "proven": "已验证"},
    statuses={
        "analyzed": "已分析",
        "watching": "观察中",
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
    heading_takeaway=("对你的可迁移点", "对我的可迁移点"),
    quiet_hints=("边界", "局限", "免责", "口径"),
    count_units={"picks": "{n} 个", "table": "{n} 项", "list": "{n} 条"},
    cta_default="完整分析",
    read_unit="chars",
    read_speed=350,
    t={
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
            "lede_pre": "已筛出 ",
            "lede_post": " 个值得看",
            "lede_body": "全球 AI 应用每天新增几百个，绝大多数是套壳。"
            "这里只留下能说清「它替代了什么旧行为」的——答不上来的，一律不推荐。",
            "stat_total": "在库",
            "picks": "精选判断",
            "picks_note": "能抄的产品逻辑，不按写作日期凑数",
            "replaces": "替代了什么",
            "takeaway": "能拿走什么",
            "notables": "值得留意",
            "notables_note": "替代关系清晰，但还没展开分析",
            "movers": "增长信号",
            "movers_note": "环比异常通常不是自然增长，是导流或口径变化",
            "col_product": "产品",
            "col_growth": "环比",
            "col_scale": "规模",
            "col_boards": "所在榜单",
            "cats": "按方向找",
            "latest_report": "最新观察",
            "latest_report_note": "当天最反直觉的那句结论",
            "latest_report_cta": "读完整观察",
            "past_reports": "往期观察",
            "past_reports_note": "回看已发生的信号",
            "report_fallback": "当日趋势判断与市场信号",
        },
        "products": {
            "title": "全部产品",
            "note": "刚冒头的看它做什么，已验证的看它涨多快。两类东西的判断方式本来就不同。",
            "desc": "全部 {total} 个 AI 应用。刚冒头的看它做什么，已验证的看它涨多快。",
            "count": "当前结果",
            "f_category": "方向",
            "f_stage": "阶段",
            "f_status": "评级",
            "f_sort": "排序",
            "f_category_aria": "按方向筛选",
            "f_stage_aria": "按阶段筛选",
            "f_status_aria": "按评级筛选",
            "f_sort_aria": "排序方式",
            "all": "全部",
            "sort_weight": "热度",
            "sort_growth": "增长",
            "sort_recent": "最近出现",
            "sort_name": "名称",
            "no_summary": "还没有简介，需要深挖才能判断",
            "empty": "这个组合下没有产品。",
            "reset": "清掉筛选，看全部 {total} 个",
            "stage_early_note": "还没有数据可验证，判断只能靠推理需求真伪。",
            "stage_proven_note": "已经跑出规模，判断看流量和环比，不看介绍。",
        },
        "product": {
            "lede_proven": "已经跑出规模的产品，判断看数据不看介绍。",
            "lede_early": "还没有简介，需要深挖官网才能判断它到底做什么。",
            "builder": "做这个的人",
            "first_seen": "首次出现",
            "last_seen": "最近出现",
            "link": "链接",
            "link_open": "打开 ↗",
            "inspiration": "这个产品给你的灵感",
            "replaces": "替代了什么旧行为",
            "takeaway": "能拿走什么",
            "boards": "所在榜单",
            "boards_note": "上了哪些细分榜，说明它的品类和地位",
            "none_lead": "这个产品还没有展开分析。",
            "none_sub": "上面那句灵感是目前能给的全部判断。",
            "none_early": "它还太早，没有可验证的数据，再多写就是编。",
            "none_proven": "它已经跑出规模，判断要看流量和环比的变化，不是看一次快照。",
            "none_siblings": "同方向已经分析过的：",
            "sibling_sep": "、",
            "notes": "笔记",
            "onward_aria": "继续浏览",
            "siblings": "同方向的其他",
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
    site_desc="Every day we dig through the AI products the world just shipped, "
    "cut the noise, and judge which ones solve a real problem.",
    categories=dict(CATEGORY_EN),
    stages={"early": "Early", "proven": "Proven"},
    statuses={
        "analyzed": "Analyzed",
        "watching": "Watching",
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
            "lede_post": " products worth your time",
            "lede_body": "Hundreds of AI products ship every day and most are a prompt "
            "in a wrapper. Only the ones that can name the old behavior they replace "
            "make it onto this page. No answer, no recommendation.",
            "stat_total": "Tracked",
            "picks": "Selected calls",
            "picks_note": "Product logic worth borrowing, not a list padded to fill a day.",
            "replaces": "Replaces",
            "takeaway": "Take away",
            "notables": "On the radar",
            "notables_note": "The replacement is clear, the deep dive isn't written yet",
            "movers": "Growth signals",
            "movers_note": "A freak month-over-month jump is rarely organic — "
            "it's a traffic deal or a changed definition",
            "col_product": "Product",
            "col_growth": "MoM",
            "col_scale": "Scale",
            "col_boards": "Ranked in",
            "cats": "Browse by direction",
            "latest_report": "Latest observation",
            "latest_report_note": "The least obvious thing we found that day",
            "latest_report_cta": "Read the full observation",
            "past_reports": "Past observations",
            "past_reports_note": "Signals worth revisiting after the fact",
            "report_fallback": "Trend calls and market signals for the day",
        },
        "products": {
            "title": "All products",
            "note": "For early ones, read what they do. For proven ones, read how fast "
            "they're growing. Two different questions.",
            "desc": "All {total} AI products on the radar. For early ones, read what they "
            "do; for proven ones, how fast they're growing.",
            "count": "Showing",
            "f_category": "Direction",
            "f_stage": "Stage",
            "f_status": "Rating",
            "f_sort": "Sort",
            "f_category_aria": "Filter by direction",
            "f_stage_aria": "Filter by stage",
            "f_status_aria": "Filter by rating",
            "f_sort_aria": "Sort order",
            "all": "All",
            "sort_weight": "Heat",
            "sort_growth": "Growth",
            "sort_recent": "Last seen",
            "sort_name": "Name",
            "no_summary": "No description yet — it takes digging to judge this one",
            "empty": "Nothing matches this combination.",
            "reset": "Clear filters, show all {total}",
            "stage_early_note": "Nothing to verify yet. The only judgment available is "
            "whether the need is real.",
            "stage_proven_note": "Already at scale. Read the traffic and the trend, "
            "not the pitch.",
        },
        "product": {
            "lede_proven": "Already at scale. Judge it on the numbers, not the pitch.",
            "lede_early": "No description yet — judging this one means digging into the site.",
            "builder": "Built by",
            "first_seen": "First seen",
            "last_seen": "Last seen",
            "link": "Link",
            "link_open": "Open ↗",
            "inspiration": "What this one is good for",
            "replaces": "What old behavior it replaces",
            "takeaway": "What you can take from it",
            "boards": "Ranked in",
            "boards_note": "Which sub-rankings it charts in tells you its category and standing",
            "none_lead": "No deep dive on this one yet.",
            "none_sub": "The line above is the whole judgment so far.",
            "none_early": "It's too early — there's nothing to verify, and writing more "
            "would be making things up.",
            "none_proven": "It's already at scale. Judging it means watching traffic and "
            "trend move, not reading one snapshot.",
            "none_siblings": "Already analyzed in the same direction:",
            "sibling_sep": ", ",
            "notes": "Notes",
            "onward_aria": "Keep browsing",
            "siblings": "Others in the same direction",
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
