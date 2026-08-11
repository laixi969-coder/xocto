"""采集编排：把各个源跑一遍，存档，合并进产品池。

这里不做任何判断 —— 不判断产品好坏，不过滤，不打分。
判断是 Claude Code 读 config/filter.md 之后的事。
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

from .dedupe import ProductIndex, canonical_url
from .models import Product, RawItem, Sighting, slugify
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
    old_metrics = {(s.source, s.url): s.metrics for s in old.sightings}
    new_metrics = {(s.source, s.url): s.metrics for s in new.sightings}
    return old_metrics != new_metrics


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

            if _has_material_change(existing, updated):
                index.add(updated)
                if not dry_run:
                    store.save_product(updated)
                updated_count += 1
            else:
                unchanged_count += 1
            continue

        product = Product.from_raw(item, canonical_url(item.url))
        product = replace(product, slug=index.next_free_slug(slugify(item.title)))
        index.add(product)
        if not dry_run:
            store.save_product(product)
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
    day = day or datetime.now(timezone.utc).date()

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
