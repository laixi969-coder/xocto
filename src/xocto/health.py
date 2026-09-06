"""采集健康检查 —— 防的是"静默变质"，不是"报错"。

为什么需要这个：采集层刻意做成单源失败不中断（见 CLAUDE.md），
这对当天的产出是对的，但代价是**没有人会被通知**。

真正会出事的形态不是崩溃，是安静地什么都不返回：

  - 源站改了 HTML 结构 → 选择器匹配不到，返回 200 但 0 条
  - 源站开始反爬 → 持续 429，重试耗尽，那个源被跳过
  - 接口换了域名 → 404，4xx 不重试直接跳过

以上三种，站点每天照常更新，看起来一切正常。半年后你可能已经连续
两个月只从一个源拿数据，而这个站的唯一价值就是数据。

判据取自 data/raw/ 的历史条数 —— 那是只追加不修改的存档，是唯一真相。
没有历史时只断言"不为零"；历史攒够了才跟中位数比。

退出码只在"死源"时非零：让 GitHub Actions 变红并发邮件。
骤降只警告不失败 —— 每天的自然波动就会触发，天天变红等于没有告警。

单日 0 条不直接判死：低产源（每天中位数一两条的生态源）本来就会有空窗日，
高产源也可能是采集当刻一次瞬时拉取失败。规则是：昨天还有产出、今天挂零
只警告；连续两天挂零才升级为死源。真正死掉的源只晚一天报警，换来定时
任务不再被单日波动染红。
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass
from datetime import date, timedelta

from .models import today as today_cst
from .store import Store

# 回看窗口。raw 保留 30 天（xocto prune），取 14 天足够形成基线又不至于
# 被一个月前的旧口径拖偏。
LOOKBACK_DAYS = 14

# 低于中位数这个比例算骤降。0.4 是刻意宽松的：
# Product Hunt 周末条数本来就掉一半，阈值太紧会天天误报。
DROP_RATIO = 0.4

# 算中位数至少要几天的历史，否则一两天的样本毫无意义
MIN_HISTORY_DAYS = 3

SEVERITY_DEAD = "dead"
SEVERITY_WARN = "warn"


@dataclass(frozen=True)
class Finding:
    severity: str
    source: str
    message: str


def daily_counts(store: Store, days: int = LOOKBACK_DAYS) -> dict[date, dict[str, int]]:
    """每天每个源各有多少条。只读 raw，不碰产品池。"""
    today = today_cst()
    window = {d for d in store.raw_days() if (today - d).days < days}
    out: dict[date, dict[str, int]] = {}
    for day in sorted(window):
        counts: dict[str, int] = {}
        for item in store.read_raw(day):
            counts[item.source] = counts.get(item.source, 0) + 1
        out[day] = counts
    return out


def enabled_sources(config: dict) -> list[str]:
    """配置里标了 enabled 的源。检查要以"该有什么"为基准，不是"有什么"。"""
    sources = config.get("sources") or {}
    return sorted(
        name for name, cfg in sources.items()
        if isinstance(cfg, dict) and cfg.get("enabled")
    )


def _newssearch_lane_findings(store: Store, config: dict, day: date) -> list[Finding]:
    """逐条检查中美搜索车道，防止一个市场失效却被另一个市场总量掩盖。"""
    source_cfg = ((config.get("sources") or {}).get("newssearch") or {})
    if not isinstance(source_cfg, dict) or not source_cfg.get("enabled"):
        return []
    expected = {
        str(spec.get("name") or "").strip()
        for spec in (source_cfg.get("queries") or [])
        if isinstance(spec, dict) and str(spec.get("name") or "").strip()
    }
    actual = {
        str(item.extra.get("query_lane") or "").strip()
        for item in store.read_raw(day)
        if item.source == "newssearch" and str(item.extra.get("query_lane") or "").strip()
    }
    # 整个 newssearch 为零时，源级检查已经给出更直接的死源结论。
    if not actual:
        return []
    findings = [
        Finding(
            SEVERITY_DEAD,
            f"newssearch:{lane}",
            "同一轮其他新闻搜索有产出，但这条语言/市场车道为 0 —— 查询可能失效或被限流",
        )
        for lane in sorted(expected - actual)
    ]
    findings.extend(
        Finding(
            SEVERITY_WARN,
            f"newssearch:{lane}",
            "原始数据出现未配置的搜索车道 —— 配置和实际不一致",
        )
        for lane in sorted(actual - expected)
    )
    return findings


def check(store: Store, config: dict, today: date | None = None) -> list[Finding]:
    """比对今天和历史，返回发现。空列表 = 健康。"""
    today = today or today_cst()
    counts = daily_counts(store)
    findings: list[Finding] = []

    expected = enabled_sources(config)
    if not expected:
        return [Finding(SEVERITY_WARN, "-", "配置里没有任何 enabled 的源")]

    if today not in counts:
        return [
            Finding(
                SEVERITY_DEAD, "-",
                f"{today} 没有任何原始存档 —— 采集根本没跑，或者一条都没抓到",
            )
        ]

    now = counts[today]
    history = {d: c for d, c in counts.items() if d < today}

    for source in expected:
        got = now.get(source, 0)
        past = [c.get(source, 0) for c in history.values()]
        seen_before = [n for n in past if n > 0]

        if got == 0:
            if seen_before:
                last = max(d for d, c in history.items() if c.get(source, 0) > 0)
                if (today - last).days >= 2:
                    findings.append(Finding(
                        SEVERITY_DEAD, source,
                        f"连续两天 0 条，上次产出还是 {last}（{history[last][source]} 条）—— "
                        f"大概率是源站改版、反爬或换了域名",
                    ))
                else:
                    findings.append(Finding(
                        SEVERITY_WARN, source,
                        f"今天 0 条，但 {last} 还有 {history[last][source]} 条 —— "
                        f"单日空窗可能是波动或瞬时拉取失败，连续两天挂零才算死源",
                    ))
            else:
                findings.append(Finding(
                    SEVERITY_WARN, source,
                    "开着但从来没产出过条目 —— 刚启用可以忽略，否则它一直是坏的",
                ))
            continue

        if len(seen_before) >= MIN_HISTORY_DAYS:
            median = statistics.median(seen_before)
            if got < median * DROP_RATIO:
                findings.append(Finding(
                    SEVERITY_WARN, source,
                    f"今天 {got} 条，近期中位数 {median:.0f} 条 —— "
                    f"掉到 {got / median:.0%}，值得看一眼是不是采集规则失效了",
                ))

    unexpected = sorted(set(now) - set(expected))
    for source in unexpected:
        findings.append(Finding(
            SEVERITY_WARN, source,
            f"数据里有 {now[source]} 条，但配置里没有 enabled —— 配置和实际不一致",
        ))

    findings.extend(_newssearch_lane_findings(store, config, today))

    return findings


def format_report(store: Store, config: dict, findings: list[Finding]) -> str:
    """给人看的一段文字。CI 日志里要一眼看懂发生了什么。"""
    counts = daily_counts(store)
    lines = ["采集健康检查"]

    recent = sorted(counts)[-7:]
    if recent:
        lines.append("")
        lines.append("  近 7 天各源条数：")
        all_sources = sorted({s for d in recent for s in counts[d]})
        for day in recent:
            detail = "  ".join(f"{s}={counts[day].get(s, 0)}" for s in all_sources)
            lines.append(f"    {day}  {detail}")

    lines.append("")
    if not findings:
        lines.append("  ✓ 所有开启的源今天都有产出，且没有异常骤降")
        return "\n".join(lines)

    dead = [f for f in findings if f.severity == SEVERITY_DEAD]
    warn = [f for f in findings if f.severity == SEVERITY_WARN]
    for f in dead:
        lines.append(f"  ✗ 死源 {f.source}：{f.message}")
    for f in warn:
        lines.append(f"  ! 注意 {f.source}：{f.message}")
    if dead:
        lines.append("")
        lines.append("  有源已经不产出数据了。站点还会照常更新，所以不查就不会发现。")
    return "\n".join(lines)


def has_dead(findings: list[Finding]) -> bool:
    return any(f.severity == SEVERITY_DEAD for f in findings)
