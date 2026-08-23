"""数据结构。

全部 frozen —— 采集到的东西不允许被原地修改，任何"变更"都返回新对象。
理由见 CLAUDE.md：原始数据是唯一真相，下游都可以从它重建。
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field, replace
from datetime import date, datetime, timedelta, timezone
from typing import Any

ISO_FMT = "%Y-%m-%dT%H:%M:%SZ"

# 这是一份中文日更，"今天"必须按北京时间算 —— 存档文件名、简报文件名、
# 页面上的日期都是给中国读者看的。以前采集在北京时间 9 点跑，UTC 日期和
# 北京日期正好同一天，用 UTC 当"今天"没露馅；改到早上 7 点（UTC 前一天 23 点）
# 之后两者就差一天，页脚会在 13 号早上写着"数据截至 12 号"。
# 用固定偏移而不是 zoneinfo：中国没有夏令时，一个偏移永远成立，
# 也不用赌运行环境装了 tz 数据库。
CST = timezone(timedelta(hours=8))


def now_iso() -> str:
    """当前 UTC 时间的 ISO8601 字符串。全系统统一用 UTC，展示时再转。"""
    return datetime.now(timezone.utc).strftime(ISO_FMT)


def today() -> date:
    """北京时间的今天。凡是"哪一天"的判断都走这里，不要各处自己算。"""
    return datetime.now(CST).date()


def local_day(iso: str) -> str:
    """存下来的 UTC 时间戳 → 北京日期（YYYY-MM-DD）。这就是"展示时再转"。

    解析不了就原样截前 10 位：手写过的档案里可能有非标准写法，
    显示得不准也好过整页构建崩掉。
    """
    try:
        stamp = datetime.strptime(iso, ISO_FMT).replace(tzinfo=timezone.utc)
    except (ValueError, TypeError):
        return iso[:10]
    return stamp.astimezone(CST).date().isoformat()


def slugify(text: str, max_len: int = 60) -> str:
    """把产品名转成文件名安全的 slug。

    中文等非 ASCII 字符会被保留（macOS 文件系统支持），只清掉
    路径分隔符和空白。全部转不出东西时回退到哈希，保证永不返回空串。
    """
    normalized = unicodedata.normalize("NFKC", text).strip().lower()
    # 空白与常见分隔符统一成连字符
    slug = re.sub(r"[\s_/\\|]+", "-", normalized)
    # 清掉文件名非法字符与标点
    slug = re.sub(r"[^\w\-一-鿿]", "", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    slug = slug[:max_len].strip("-")
    if not slug:
        import hashlib

        slug = "item-" + hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
    return slug


@dataclass(frozen=True, slots=True)
class RawItem:
    """从某个源抓到的一条原始记录。未经去重，未经任何判断。

    metrics 里放各源的热度指标（点赞数、星数、评论数），字段名各源不同，
    不强行统一 —— 统一会丢失信息，判断阶段需要原始语义。
    """

    source: str  # "producthunt" / "hackernews" / "github"
    external_id: str  # 源内唯一 ID，用于源内去重
    title: str
    url: str  # 产品官网或指向页
    summary: str
    published_at: str  # ISO8601 UTC，源提供的发布时间
    collected_at: str  # ISO8601 UTC，我们抓到的时间
    metrics: dict[str, Any]
    extra: dict[str, Any]
    # 源返回的原始数据，原样保存。
    # 上面那些字段都是解析出来的 —— 解析逻辑以后会改，改了之后
    # 只有靠这份原始数据才能重建历史。不存，历史就永远停在旧解析上。
    payload: dict[str, Any] = field(default_factory=dict)

    @property
    def key(self) -> str:
        """源内唯一键，用于 raw 层幂等去重。"""
        return f"{self.source}:{self.external_id}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "external_id": self.external_id,
            "title": self.title,
            "url": self.url,
            "summary": self.summary,
            "published_at": self.published_at,
            "collected_at": self.collected_at,
            "metrics": self.metrics,
            "extra": self.extra,
            "payload": self.payload,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RawItem:
        return cls(
            source=data["source"],
            external_id=data["external_id"],
            title=data.get("title", ""),
            url=data.get("url", ""),
            summary=data.get("summary", ""),
            published_at=data.get("published_at", ""),
            collected_at=data.get("collected_at", ""),
            metrics=data.get("metrics") or {},
            extra=data.get("extra") or {},
            payload=data.get("payload") or {},
        )


@dataclass(frozen=True, slots=True)
class Sighting:
    """某个产品在某个源上被看到的一次记录。

    同一产品可能在 PH 出现一次、两周后又在 HN 出现一次 —— 那是两条 sighting，
    但只有一个产品档案。第二次出现本身就是信号（说明还活着、在推广）。
    """

    source: str
    url: str
    seen_at: str
    metrics: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "url": self.url,
            "seen_at": self.seen_at,
            "metrics": self.metrics,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Sighting:
        return cls(
            source=data["source"],
            url=data.get("url", ""),
            seen_at=data.get("seen_at", ""),
            metrics=data.get("metrics") or {},
        )


# 产品在流水线里的状态。Python 只负责把状态推到 pending_filter，
# 之后的流转由 Claude Code 在过滤和分析阶段写入。
STATUS_PENDING_FILTER = "pending_filter"  # 刚采集，还没过滤
STATUS_REJECTED = "rejected"  # 过滤掉了
# 已成规模的通用入口仍值得用来解释市场变化，但它们不是创业机会。
# 单列这个状态，避免「没公开」被误读成「被淘汰」，也避免它们挤进机会库。
STATUS_MARKET_CONTEXT = "market_context"
STATUS_QUEUED = "queued"  # 通过过滤，等待分析
STATUS_WATCHING = "watching"  # 第三档：存疑保留，只记录不展开
STATUS_ANALYZED = "analyzed"  # 分析完成

ALL_STATUSES = (
    STATUS_PENDING_FILTER,
    STATUS_REJECTED,
    STATUS_MARKET_CONTEXT,
    STATUS_QUEUED,
    STATUS_WATCHING,
    STATUS_ANALYZED,
)

# 赛道。按用户会问的"什么方向"来分，不按技术形态分 ——
# 用户找的是"有没有做视频的"，不是"有没有用 RAG 的"。
CATEGORIES = (
    "AI + 创作",  # 视频、图像、写作、设计、短剧
    "AI + 开发",  # coding agent、devtools、工程效率
    "AI + 商业",  # CRM、销售、营销、GTM、招聘
    "AI + 效率",  # 笔记、任务、文档、办公
    "AI + 生活",  # 健康、社交、娱乐、游戏、教育
    "通用助手",  # 大模型对话产品：DeepSeek、Kimi、豆包这类，自成一类
    "基础层",  # 给 agent 和模型用的：网关、沙箱、记忆、可观测性、算力
)

# 项目类型与赛道是两条独立轴：开源代码、已有业务的 AI 改造和新应用都可以
# 同时属于同一个行业/具体工作。细分行业、工作和地区以自由标签保存，避免每次
# 出现新领域都要改一套枚举。
PROJECT_NEW_APPLICATION = "new_application"
PROJECT_OPEN_SOURCE = "open_source"
PROJECT_AI_TRANSFORMATION = "ai_transformation"
PROJECT_TYPES = (
    PROJECT_NEW_APPLICATION,
    PROJECT_OPEN_SOURCE,
    PROJECT_AI_TRANSFORMATION,
)

# 阶段。替代"数据来源"这个维度 —— 用户关心的是成熟度，不是我们从哪抓的。
STAGE_EARLY = "刚冒头"  # 还没有可验证的数据，判断只能靠推理需求真伪
STAGE_PROVEN = "已验证"  # 有真实流量/月活，可以看势

# 机会流事件。项目是稳定实体；事件才是“今天发生了什么”。
EVENT_FIRST_DISCOVERED = "first_discovered"
EVENT_MATERIAL_UPDATE = "material_update"
EVENT_MARKET_CHANGE = "market_change"
EVENT_REQ_CHANGE = "req_change"
EVENT_TYPES = (
    EVENT_FIRST_DISCOVERED,
    EVENT_MATERIAL_UPDATE,
    EVENT_MARKET_CHANGE,
    EVENT_REQ_CHANGE,
)

# `/req` 的判断结论与四道闸门。结论与展示用信号等级分开：前者忠于
# 真需求框架，后者让读者一眼知道证据处在什么阶段。
REQ_TRUE_DEMAND = "true_demand"
REQ_PSEUDO_DEMAND = "pseudo_demand"
REQ_NEEDS_VALIDATION = "needs_validation"
REQ_VERDICTS = (REQ_TRUE_DEMAND, REQ_PSEUDO_DEMAND, REQ_NEEDS_VALIDATION)
REQ_GATE_VALUE = "value"
REQ_GATE_CONSENSUS = "consensus"
REQ_GATE_MODEL = "model"
REQ_GATE_TRUTH = "truth"
REQ_GATES = (REQ_GATE_VALUE, REQ_GATE_CONSENSUS, REQ_GATE_MODEL, REQ_GATE_TRUTH)
REQ_GATE_SUPPORTED = "supported"
REQ_GATE_INSUFFICIENT = "insufficient"
REQ_GATE_CHALLENGED = "challenged"
REQ_GATE_STATUSES = (REQ_GATE_SUPPORTED, REQ_GATE_INSUFFICIENT, REQ_GATE_CHALLENGED)

SUPPLY_NOT_FOUND = "not_found_in_covered_sources"
SUPPLY_EMERGING = "emerging"
SUPPLY_ESTABLISHED = "established"
SUPPLY_STATUSES = (SUPPLY_NOT_FOUND, SUPPLY_EMERGING, SUPPLY_ESTABLISHED)
DEMAND_UNKNOWN = "unknown"
DEMAND_EARLY_SIGNAL = "early_signal"
DEMAND_VALIDATED_SIGNAL = "validated_signal"
DEMAND_EVIDENCE_STATUSES = (DEMAND_UNKNOWN, DEMAND_EARLY_SIGNAL, DEMAND_VALIDATED_SIGNAL)


@dataclass(frozen=True, slots=True)
class Evidence:
    """支持公开判断的一条可核验事实。

    `source_kind` 描述证据性质而非内部采集渠道，例如 product、pricing、
    open_source、adoption、market_comparison。这样可对外展示证据，不泄漏抓取策略。
    """

    id: str
    project_slug: str
    url: str
    title: str
    published_at: str
    collected_at: str
    source_kind: str
    tier: str  # first_party / behavioural / independent
    fact: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "project_slug": self.project_slug,
            "url": self.url,
            "title": self.title,
            "published_at": self.published_at,
            "collected_at": self.collected_at,
            "source_kind": self.source_kind,
            "tier": self.tier,
            "fact": self.fact,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Evidence":
        return cls(
            id=str(data["id"]),
            project_slug=str(data["project_slug"]),
            url=str(data.get("url") or ""),
            title=str(data.get("title") or ""),
            published_at=str(data.get("published_at") or ""),
            collected_at=str(data.get("collected_at") or ""),
            source_kind=str(data.get("source_kind") or "product"),
            tier=str(data.get("tier") or "first_party"),
            fact=str(data.get("fact") or ""),
        )


@dataclass(frozen=True, slots=True)
class DiscoveryEvent:
    """一次可在首页出现的新增发现或实质更新。"""

    id: str
    project_slug: str
    event_type: str
    occurred_at: str
    discovered_at: str
    signals: tuple[str, ...] = ()
    summary: str = ""
    evidence_ids: tuple[str, ...] = ()
    homepage: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "project_slug": self.project_slug,
            "event_type": self.event_type,
            "occurred_at": self.occurred_at,
            "discovered_at": self.discovered_at,
            "signals": list(self.signals),
            "summary": self.summary,
            "evidence_ids": list(self.evidence_ids),
            "homepage": self.homepage,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "DiscoveryEvent":
        event_type = str(data["event_type"])
        if event_type not in EVENT_TYPES:
            raise ValueError(f"未知事件类型：{event_type}")
        return cls(
            id=str(data["id"]),
            project_slug=str(data["project_slug"]),
            event_type=event_type,
            occurred_at=str(data.get("occurred_at") or ""),
            discovered_at=str(data.get("discovered_at") or ""),
            signals=tuple(str(value) for value in (data.get("signals") or [])),
            summary=str(data.get("summary") or ""),
            evidence_ids=tuple(str(value) for value in (data.get("evidence_ids") or [])),
            homepage=bool(data.get("homepage", True)),
        )


@dataclass(frozen=True, slots=True)
class MarketObservation:
    """某项目在一个国家/市场中的供给与需求证据快照。"""

    project_slug: str
    market: str
    ecosystem: str  # zh / en
    observed_at: str
    supply_status: str
    demand_status: str
    coverage: str = ""
    evidence_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.supply_status not in SUPPLY_STATUSES:
            raise ValueError(f"未知本地供给状态：{self.supply_status}")
        if self.demand_status not in DEMAND_EVIDENCE_STATUSES:
            raise ValueError(f"未知需求证据状态：{self.demand_status}")

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "market": self.market,
            "ecosystem": self.ecosystem,
            "observed_at": self.observed_at,
            "supply_status": self.supply_status,
            "demand_status": self.demand_status,
            "coverage": self.coverage,
            "evidence_ids": list(self.evidence_ids),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "MarketObservation":
        return cls(
            project_slug=str(data["project_slug"]),
            market=str(data["market"]),
            ecosystem=str(data["ecosystem"]),
            observed_at=str(data["observed_at"]),
            supply_status=str(data["supply_status"]),
            demand_status=str(data["demand_status"]),
            coverage=str(data.get("coverage") or ""),
            evidence_ids=tuple(str(value) for value in (data.get("evidence_ids") or [])),
        )


@dataclass(frozen=True, slots=True)
class ReqGateReview:
    """`/req` 单道闸门的可追溯结论。"""

    gate: str
    status: str
    reason: str
    evidence_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.gate not in REQ_GATES:
            raise ValueError(f"未知 `/req` 闸门：{self.gate}")
        if self.status not in REQ_GATE_STATUSES:
            raise ValueError(f"未知 `/req` 闸门状态：{self.status}")

    def to_dict(self) -> dict[str, Any]:
        return {
            "gate": self.gate,
            "status": self.status,
            "reason": self.reason,
            "evidence_ids": list(self.evidence_ids),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ReqGateReview":
        return cls(
            gate=str(data["gate"]),
            status=str(data["status"]),
            reason=str(data.get("reason") or ""),
            evidence_ids=tuple(str(value) for value in (data.get("evidence_ids") or [])),
        )


@dataclass(frozen=True, slots=True)
class ReqReview:
    """一次完整或初步的 `/req` 判断版本。"""

    id: str
    project_slug: str
    level: str  # initial / full
    reviewed_at: str
    verdict: str
    signal_level: str
    gates: tuple[ReqGateReview, ...]
    next_validation: str = ""
    market: str = ""

    def __post_init__(self) -> None:
        if self.level not in {"initial", "full"}:
            raise ValueError(f"未知 `/req` 判断层级：{self.level}")
        if self.verdict not in REQ_VERDICTS:
            raise ValueError(f"未知 `/req` 结论：{self.verdict}")
        if tuple(gate.gate for gate in self.gates) != REQ_GATES:
            raise ValueError("`/req` 判断必须按价值、共识、模式、求真四道闸门完整记录")

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "project_slug": self.project_slug,
            "level": self.level,
            "reviewed_at": self.reviewed_at,
            "verdict": self.verdict,
            "signal_level": self.signal_level,
            "gates": [gate.to_dict() for gate in self.gates],
            "next_validation": self.next_validation,
            "market": self.market,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ReqReview":
        return cls(
            id=str(data["id"]),
            project_slug=str(data["project_slug"]),
            level=str(data["level"]),
            reviewed_at=str(data["reviewed_at"]),
            verdict=str(data["verdict"]),
            signal_level=str(data.get("signal_level") or "待验证"),
            gates=tuple(ReqGateReview.from_dict(item) for item in (data.get("gates") or [])),
            next_validation=str(data.get("next_validation") or ""),
            market=str(data.get("market") or ""),
        )


@dataclass(frozen=True, slots=True)
class Product:
    """产品池里的一份档案。去重后的唯一真相，一个产品一个文件。"""

    slug: str
    name: str
    url: str  # 展示用的原始 URL
    canonical_url: str  # 去重用的规范化 URL
    summary: str
    first_seen: str
    last_seen: str
    status: str
    sightings: tuple[Sighting, ...]
    # 做这个东西的人。各源都白给这个信息，值得留着 ——
    # 判断早期项目时，"这个人为什么做这件事"往往比产品本身更能说明问题。
    builder: str = ""
    # 赛道。用户找东西是按方向找的，不是按"从哪抓来的"找。
    # 取值见 CATEGORIES。空串表示还没归类。
    category: str = ""
    # 中文一句话：谁、在什么场景、得到什么结果。源给的多半是英文营销话术，
    # 直接摆出来等于没说 —— 读者要在一行里看懂，就必须是中文、是大白话。
    summary_zh: str = ""
    # 趋势 + 切入：这件事说明市场往哪走，创业者从哪切进去。
    # 每个产品都要有 —— 没有方向的产品，收录它就没意义。
    inspiration: str = ""
    # 英文站用的一句话。source 自带的 summary 多半是营销话术，
    # 说不清做什么的时候才写这个覆盖掉，能用就不写。
    summary_en: str = ""
    # 英文站用的灵感。英文页面上缺这句就整块不显示 ——
    # 宁可少一块，也不能在英文页面里混中文。
    inspiration_en: str = ""
    # 来自专题、官方组织或全局突破通道的重大项目。它们必须进入日报复核，
    # 不能因普通候选噪音而被静默淘汰。
    priority_review: bool = False
    project_type: str = ""
    industries: tuple[str, ...] = ()
    industries_en: tuple[str, ...] = ()
    jobs: tuple[str, ...] = ()
    jobs_en: tuple[str, ...] = ()
    regions: tuple[str, ...] = ()
    regions_en: tuple[str, ...] = ()
    open_source: bool = False
    notes: str = ""  # 人或 Claude 写的自由笔记，机器不覆盖

    @property
    def sources(self) -> tuple[str, ...]:
        """出现过的所有来源，去重且保序。"""
        seen: list[str] = []
        for s in self.sightings:
            if s.source not in seen:
                seen.append(s.source)
        return tuple(seen)

    def with_sighting(self, sighting: Sighting) -> Product:
        """记录一次新的出现，返回新对象。

        同源同 URL 的重复出现会更新该条 sighting 的指标而不是堆叠，
        否则每天跑一次就会积累无数条相同记录。
        """
        existing = [
            s for s in self.sightings if s.source == sighting.source and s.url == sighting.url
        ]
        if existing:
            updated = tuple(
                sighting if (s.source == sighting.source and s.url == sighting.url) else s
                for s in self.sightings
            )
        else:
            updated = self.sightings + (sighting,)

        return replace(
            self,
            sightings=updated,
            last_seen=max(self.last_seen, sighting.seen_at) if self.last_seen else sighting.seen_at,
        )

    @classmethod
    def from_raw(cls, item: RawItem, canonical_url: str) -> Product:
        """从一条原始记录新建产品档案。"""
        sighting = Sighting(
            source=item.source,
            url=item.url,
            seen_at=item.collected_at,
            metrics=item.metrics,
        )
        return cls(
            slug=slugify(item.title),
            name=item.title,
            url=item.url,
            canonical_url=canonical_url,
            summary=item.summary,
            first_seen=item.published_at or item.collected_at,
            last_seen=item.collected_at,
            status=STATUS_PENDING_FILTER,
            sightings=(sighting,),
            builder=item.extra.get("builder", ""),
            project_type=(PROJECT_OPEN_SOURCE if item.source in {"github", "huggingface", "modelscope"} else PROJECT_NEW_APPLICATION),
            open_source=item.source in {"github", "huggingface", "modelscope"},
            priority_review=bool(item.extra.get("priority_review")),
        )
