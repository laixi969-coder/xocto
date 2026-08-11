"""数据结构。

全部 frozen —— 采集到的东西不允许被原地修改，任何"变更"都返回新对象。
理由见 CLAUDE.md：原始数据是唯一真相，下游都可以从它重建。
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from typing import Any

ISO_FMT = "%Y-%m-%dT%H:%M:%SZ"


def now_iso() -> str:
    """当前 UTC 时间的 ISO8601 字符串。全系统统一用 UTC，展示时再转。"""
    return datetime.now(timezone.utc).strftime(ISO_FMT)


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
STATUS_QUEUED = "queued"  # 通过过滤，等待分析
STATUS_WATCHING = "watching"  # 第三档：存疑保留，只记录不展开
STATUS_ANALYZED = "analyzed"  # 分析完成

ALL_STATUSES = (
    STATUS_PENDING_FILTER,
    STATUS_REJECTED,
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

# 阶段。替代"数据来源"这个维度 —— 用户关心的是成熟度，不是我们从哪抓的。
STAGE_EARLY = "刚冒头"  # 还没有可验证的数据，判断只能靠推理需求真伪
STAGE_PROVEN = "已验证"  # 有真实流量/月活，可以看势


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
        )
