"""采集编排：把各个源跑一遍，存档，合并进产品池。

这里不做任何判断 —— 不判断产品好坏，不过滤，不打分。
判断是 Claude Code 读 config/filter.md 之后的事。
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path

import yaml

from .dedupe import ProductIndex, canonical_url
from .models import (
    DEMAND_EARLY_SIGNAL,
    DEMAND_UNKNOWN,
    EVENT_FIRST_DISCOVERED,
    EVENT_MATERIAL_UPDATE,
    SUPPLY_EMERGING,
    DiscoveryEvent,
    Evidence,
    MarketObservation,
    Product,
    RawItem,
    Sighting,
    slugify,
    today,
)
from .sources import Http, get_fetcher, registered_names
from .store import Store


@dataclass(frozen=True)
class SourceResult:
    name: str
    ok: bool
    count: int
    error: str = ""


@dataclass(frozen=True)
class CollectReport:
    day: date
    results: tuple[SourceResult, ...]
    raw_fetched: int
    raw_written: int
    new_products: int
    updated_products: int
    unchanged_products: int
    news_items: int
    dry_run: bool

    @property
    def failed(self) -> tuple[SourceResult, ...]:
        return tuple(r for r in self.results if not r.ok)


def load_config(store: Store) -> dict:
    """读 config/sources.yaml。缺文件或格式错就抛异常 —— 这是配置错误，必须暴露。"""
    path = store.config_dir / "sources.yaml"
    if not path.exists():
        raise FileNotFoundError(f"找不到配置文件 {path}")

    try:
        config = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"{path} 格式有问题：{exc}") from exc

    if not isinstance(config, dict):
        raise ValueError(f"{path} 顶层必须是字典")
    return config


def build_http(config: dict) -> Http:
    http_cfg = config.get("http") or {}
    return Http(
        timeout=float(http_cfg.get("timeout_seconds") or 25),
        user_agent=str(http_cfg.get("user_agent") or "x-octo/0.1"),
        retries=int(http_cfg.get("retries") or 2),
    )


def run_sources(config: dict, http: Http) -> tuple[list[RawItem], list[SourceResult]]:
    """依次跑所有启用的源。

    单个源失败只记录不中断 —— 三个源挂一个，另外两个的数据照样要拿到。
    """
    sources_cfg = config.get("sources") or {}
    items: list[RawItem] = []
    results: list[SourceResult] = []

    for name, cfg in sources_cfg.items():
        cfg = cfg or {}
        if not cfg.get("enabled"):
            continue

        fetcher = get_fetcher(name)
        if fetcher is None:
            results.append(
                SourceResult(
                    name, False, 0, f"没有叫「{name}」的采集器（已注册：{', '.join(registered_names())}）"
                )
            )
            print(f"  ✗ {name}：没有对应的采集器")
            continue

        print(f"  → {name}")
        try:
            fetched = fetcher(cfg, http)
        except Exception as exc:  # 采集器可以抛任何异常，这里必须全接住
            results.append(SourceResult(name, False, 0, f"{type(exc).__name__}: {exc}"))
            print(f"  ✗ {name} 失败：{exc}")
            continue

        items.extend(fetched)
        results.append(SourceResult(name, True, len(fetched)))
        print(f"  ✓ {name}：{len(fetched)} 条")

    return items, results


def _has_material_change(old: Product, new: Product) -> bool:
    """判断这次合并是不是"真的有变化"。

    "我们今天又扫到了它"不算变化 —— Product Hunt 的 feed 就那 50 条，
    一个产品连续一周出现在里面只说明 feed 短，不说明它有新动态。
    所以时间戳的变化一律忽略，只认三件事：
      出现在了新的源 / 热度指标变了 / 补上了原来缺的简介。
    """
    if old.sources != new.sources:
        return True
    if old.summary != new.summary or old.builder != new.builder:
        return True
    if old.priority_review != new.priority_review:
        return True
    old_metrics = {(s.source, s.url): s.metrics for s in old.sightings}
    new_metrics = {(s.source, s.url): s.metrics for s in new.sightings}
    return old_metrics != new_metrics


def _evidence_from_raw(product: Product, item: RawItem) -> Evidence:
    """把一次原始发现留成可追溯证据，但不把内部渠道名写进公开字段。"""
    source_kind = "product"
    if item.source in {"github", "huggingface", "modelscope"}:
        source_kind = "open_source"
    elif any(key in item.metrics for key in ("raw_value", "stars", "points", "mom_percent")):
        source_kind = "adoption"
    tier = str(item.extra.get("evidence_tier") or ("behavioural" if source_kind in {"open_source", "adoption"} else "first_party"))
    evidence_url = str(item.extra.get("evidence_url") or item.url)
    evidence_title = str(item.extra.get("evidence_title") or item.title)
    fingerprint = "|".join((product.slug, evidence_url, item.published_at, item.collected_at, evidence_title))
    evidence_id = "ev-" + hashlib.sha1(fingerprint.encode("utf-8")).hexdigest()[:16]
    return Evidence(
        id=evidence_id,
        project_slug=product.slug,
        url=evidence_url,
        title=evidence_title,
        published_at=item.published_at,
        collected_at=item.collected_at,
        source_kind=source_kind,
        tier=tier,
        # 原始摘要不是编辑结论；先保存为证据原文，后续 `/req` 只能引用而不能扩写。
        fact=item.summary[:1200],
    )


def _event_from_raw(product: Product, item: RawItem, *, event_type: str, evidence_id: str) -> DiscoveryEvent:
    signals = ["release"]
    if item.source in {"github", "huggingface", "modelscope"}:
        signals.append("open_source")
    if any(key in item.metrics for key in ("raw_value", "stars", "points", "mom_percent")):
        signals.append("adoption")
    if event_type == EVENT_MATERIAL_UPDATE:
        signals = ["update", *[signal for signal in signals if signal != "release"]]
    # 首次发现一项目只有一个稳定事件 ID；更新事件按本次事实指纹幂等。
    if event_type == EVENT_FIRST_DISCOVERED:
        event_id = f"first-{product.slug}"
    else:
        payload = json.dumps(item.metrics, ensure_ascii=False, sort_keys=True)
        fingerprint = "|".join((product.slug, event_type, item.url, item.collected_at, payload))
        event_id = "evt-" + hashlib.sha1(fingerprint.encode("utf-8")).hexdigest()[:16]
    return DiscoveryEvent(
        id=event_id,
        project_slug=product.slug,
        event_type=event_type,
        occurred_at=item.published_at or item.collected_at,
        discovered_at=item.collected_at,
        signals=tuple(signals),
        # “发现新的公开信号”只是在说采集器做了什么，并不是读者需要的
        # 产品变化。没有可核实的具体变化时宁可留空，首页会把空间留给
        # 产品定位、机会方向和 /req 判断。
        summary="",
        evidence_ids=(evidence_id,),
    )


def _record_opportunity_event(store: Store, product: Product, item: RawItem, *, event_type: str) -> None:
    """产品池兼容层之外新增事件与证据，不影响既有采集结果。"""
    evidence = _evidence_from_raw(product, item)
    store.append_evidence(evidence)
    store.append_event(_event_from_raw(product, item, event_type=event_type, evidence_id=evidence.id))
    ecosystem = str(item.extra.get("ecosystem") or "")
    market = str(item.extra.get("market") or "")
    # 英文发布与开源社区不是“美国市场”的代理，但它们构成可单独观察的
    # 英文生态。国家级结论只在数据源明确给出国家时才写入。
    if not ecosystem and item.source in {"producthunt", "hackernews", "github", "huggingface"}:
        ecosystem = "en"
        market = "English-language market"
    if ecosystem and market:
        # 这是“在该生态发现了可核验供给”，不是对另一市场的缺席判断。
        # 另一方只有在独立检索写入覆盖范围后，才允许标为未发现。
        coverage = "已覆盖的中文生态公开项目发布与开发者讨论。" if ecosystem == "zh" else "已覆盖的英文生态公开项目发布与开发者讨论。"
        demand = DEMAND_EARLY_SIGNAL if int(item.metrics.get("comments") or 0) > 0 else DEMAND_UNKNOWN
        store.append_market_observation(MarketObservation(
            project_slug=product.slug,
            market=market,
            ecosystem=ecosystem,
            observed_at=item.collected_at,
            supply_status=SUPPLY_EMERGING,
            demand_status=demand,
            coverage=coverage,
            evidence_ids=(evidence.id,),
        ))


def merge_into_pool(
    store: Store, items: list[RawItem], *, dry_run: bool
) -> tuple[int, int, int, int]:
    """把原始记录合并进产品池，返回 (新建数, 实质更新数, 无变化数, 新闻数)。

    标记为 news 的不进产品池 —— 那是报道不是产品。但它仍然留在
    data/raw/ 里，简报的"大厂动作/趋势"那一节要用。
    """
    index = ProductIndex(list(store.iter_products()))
    new_count = 0
    updated_count = 0
    unchanged_count = 0
    news_count = 0

    for item in items:
        if item.extra.get("kind") == "news":
            news_count += 1
            continue

        existing = index.match(item)

        if existing is not None:
            sighting = Sighting(
                source=item.source,
                url=item.url,
                seen_at=item.collected_at,
                metrics=item.metrics,
            )
            updated = existing.with_sighting(sighting)
            # 原本缺的字段，这次源给了就补上（已有的不覆盖）
            if not updated.summary and item.summary:
                updated = replace(updated, summary=item.summary)
            if not updated.builder and item.extra.get("builder"):
                updated = replace(updated, builder=item.extra["builder"])
            # GitHub 每次抓取都会重新合并所有发现通道，因此它对“是否重大”的
            # 当前判定是权威的。这样可清掉旧规则曾把专题插件误升为重大留下的标记；
            # 其他来源不能把 GitHub 的重大项目降级。
            if item.source == "github":
                priority_review = bool(item.extra.get("priority_review"))
                if updated.priority_review != priority_review:
                    updated = replace(updated, priority_review=priority_review)

            if _has_material_change(existing, updated):
                index.add(updated)
                if not dry_run:
                    store.save_product(updated)
                    _record_opportunity_event(store, updated, item, event_type=EVENT_MATERIAL_UPDATE)
                updated_count += 1
            else:
                unchanged_count += 1
            continue

        product = Product.from_raw(item, canonical_url(item.url))
        product = replace(product, slug=index.next_free_slug(slugify(item.title)))
        index.add(product)
        if not dry_run:
            store.save_product(product)
            _record_opportunity_event(store, product, item, event_type=EVENT_FIRST_DISCOVERED)
        new_count += 1

    return new_count, updated_count, unchanged_count, news_count


def prune(store: Store, keep_days: int = 30) -> tuple[int, int]:
    """删掉过老的原始存档，返回 (删除天数, 剩余天数)。

    原始存档要进库（云端自动采集时不提交就永久丢了），但不能无限长 ——
    一天约 1MB，不清理一年就是 300MB+。保留 30 天：足够覆盖任何一次
    解析规则调整后的重建需求，再老的历史重建价值也有限。

    产品档案（pool/）永远不删 —— 那是最终产物，体积也小。
    """
    days = store.raw_days()
    if len(days) <= keep_days:
        return 0, len(days)

    doomed = days[:-keep_days]
    for day in doomed:
        store.raw_path(day).unlink(missing_ok=True)
    return len(doomed), len(days) - len(doomed)


def rebuild(store: Store) -> tuple[int, int]:
    """从 raw 存档重建整个产品池，返回 (处理天数, 产品数)。

    改了标题解析、去重规则之后用它。旧产品池不会被删除，
    而是整个目录改名备份 —— 但 md 正文里手写的笔记不会自动迁移过来，
    重建前请确认那些笔记你还留着。
    """
    store.ensure_dirs()
    days = store.raw_days()
    if not days:
        raise ValueError("data/raw/ 里没有任何存档，没法重建。先跑一次 collect。")

    if any(store.pool_dir.iterdir()):
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        backup = store.pool_dir.parent / f"pool.bak-{stamp}"
        store.pool_dir.rename(backup)
        print(f"  旧产品池已备份到 data/{backup.name}/（没有删，确认无误后你自己删）")
    store.pool_dir.mkdir(parents=True, exist_ok=True)

    for day in days:
        items = store.read_raw(day)
        merge_into_pool(store, items, dry_run=False)
        print(f"  {day.isoformat()}：{len(items)} 条")

    return len(days), len(list(store.iter_products()))


def collect(
    store: Store, *, dry_run: bool = False, day: date | None = None, force: bool = False
) -> CollectReport:
    """跑一次完整采集。幂等：同一天跑多次结果一致。

    force=True 会用本次结果整份重写当天存档，用于改了解析逻辑后重采。
    """
    store.ensure_dirs()
    day = day or today()

    config = load_config(store)
    http = build_http(config)

    mode = "（试跑，不写盘）" if dry_run else "（强制重写当天存档）" if force else ""
    print(f"采集 {day.isoformat()}{mode}")
    items, results = run_sources(config, http)

    if dry_run:
        existing_keys = {i.key for i in store.read_raw(day)}
        written = len([i for i in items if i.key not in existing_keys])
    else:
        written = store.append_raw(items, day, overwrite=force)

    new_count, updated_count, unchanged_count, news_count = merge_into_pool(
        store, items, dry_run=dry_run
    )

    return CollectReport(
        day=day,
        results=tuple(results),
        raw_fetched=len(items),
        raw_written=written,
        new_products=new_count,
        updated_products=updated_count,
        unchanged_products=unchanged_count,
        news_items=news_count,
        dry_run=dry_run,
    )
