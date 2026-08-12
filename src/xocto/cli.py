"""命令行入口。

输出面向不看代码的人：说人话，报清楚哪里成了哪里没成。
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from datetime import date, datetime, timezone

from .collect import CollectReport, collect, load_config, prune, rebuild
from .health import check as health_check, format_report as health_report, has_dead
from .models import (
    STATUS_ANALYZED,
    STATUS_PENDING_FILTER,
    STATUS_QUEUED,
    STATUS_WATCHING,
)
from .store import Store

STATUS_LABELS = {
    STATUS_PENDING_FILTER: "待过滤",
    "rejected": "已淘汰",
    STATUS_QUEUED: "待分析",
    STATUS_WATCHING: "观察中",
    STATUS_ANALYZED: "已分析",
}


def _parse_day(text: str | None) -> date | None:
    if not text:
        return None
    try:
        return date.fromisoformat(text)
    except ValueError:
        raise SystemExit(f"日期格式不对：{text}，应该是 YYYY-MM-DD")


def cmd_collect(args: argparse.Namespace) -> int:
    store = Store()
    try:
        report = collect(
            store, dry_run=args.dry_run, day=_parse_day(args.date), force=args.force
        )
    except (FileNotFoundError, ValueError) as exc:
        print(f"\n配置有问题，没能开始采集：\n  {exc}", file=sys.stderr)
        return 2

    _print_report(report)
    # 所有源都失败才算失败退出；部分失败只提示
    return 1 if report.results and len(report.failed) == len(report.results) else 0


def _print_report(report: CollectReport) -> None:
    print()
    print("─" * 46)
    if report.dry_run:
        print("试跑结果（没有写盘）")
    else:
        print("采集完成")
    print("─" * 46)
    print(f"  抓到          {report.raw_fetched} 条")
    print(f"  新存档        {report.raw_written} 条（重复的自动跳过）")
    print(f"  新增产品      {report.new_products} 个")
    print(f"  有新动态      {report.updated_products} 个（热度变了或多了一个源）")
    print(f"  没变化        {report.unchanged_products} 个")
    if report.news_items:
        print(f"  新闻报道      {report.news_items} 条（不进产品池，留给趋势那一节）")

    if report.failed:
        print()
        print(f"  以下 {len(report.failed)} 个源没跑成功：")
        for result in report.failed:
            print(f"    ✗ {result.name}：{result.error}")

    print()
    if report.dry_run:
        print("  去掉 --dry-run 才会真正写入。")
    elif report.new_products:
        print(f"  下一步：让 Claude 读 config/filter.md，把这 {report.new_products} 个新产品过一遍。")


def cmd_prune(args: argparse.Namespace) -> int:
    store = Store()
    store.ensure_dirs()
    removed, left = prune(store, keep_days=args.keep_days)
    if removed:
        print(f"\n  清掉 {removed} 天的旧存档，还剩 {left} 天\n")
    else:
        print(f"\n  存档只有 {left} 天，没到 {args.keep_days} 天的保留上限，不用清\n")
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    from .site import build

    store = Store()
    store.ensure_dirs()
    print("\n生成静态站")
    try:
        out = build(store)
    except FileNotFoundError as exc:
        print(f"\n{exc}", file=sys.stderr)
        return 2
    print(f"\n  直接打开看：open {out}/index.html\n")
    return 0


def cmd_rebuild(args: argparse.Namespace) -> int:
    store = Store()
    print("\n从原始存档重建产品池")
    try:
        days, count = rebuild(store)
    except ValueError as exc:
        print(f"\n{exc}", file=sys.stderr)
        return 2
    print(f"\n  完成：{days} 天的存档，重建出 {count} 个产品\n")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    store = Store()
    store.ensure_dirs()

    days = store.raw_days()
    products = list(store.iter_products())
    counts = Counter(p.status for p in products)

    print()
    print("─" * 46)
    print("x-octo 现状")
    print("─" * 46)

    if days:
        print(f"  原始存档      {len(days)} 天（{days[0]} → {days[-1]}）")
        today_items = store.read_raw(datetime.now(timezone.utc).date())
        print(f"  今天已抓      {len(today_items)} 条")
    else:
        print("  原始存档      还没有数据，先跑 collect")

    print(f"  产品池        {len(products)} 个")
    for status, label in STATUS_LABELS.items():
        if counts.get(status):
            print(f"    {label:<8} {counts[status]}")

    reports = sorted(store.reports_dir.glob("*.md"))
    print(f"  已出简报      {len(reports)} 份" + (f"（最新 {reports[-1].stem}）" if reports else ""))
    print()
    return 0


def cmd_health(args: argparse.Namespace) -> int:
    """采集是否在静默变质。挂在每日流程的最后一步，源死了就让 CI 变红。"""
    store = Store()
    try:
        config = load_config(store)
    except (FileNotFoundError, ValueError) as exc:
        print(f"配置有问题，没法检查：\n  {exc}", file=sys.stderr)
        return 2

    findings = health_check(store, config, today=_parse_day(args.date))
    print(health_report(store, config, findings))
    # 只有死源才非零退出。骤降天天都可能发生，天天变红等于没有告警。
    return 1 if has_dead(findings) else 0


def cmd_pool(args: argparse.Namespace) -> int:
    store = Store()
    store.ensure_dirs()

    products = list(store.iter_products())
    if args.new:
        products = [p for p in products if p.status == STATUS_PENDING_FILTER]
    elif args.status:
        products = [p for p in products if p.status == args.status]

    products.sort(key=lambda p: p.last_seen, reverse=True)
    if args.limit:
        products = products[: args.limit]

    if not products:
        print("\n（没有符合条件的产品）\n")
        return 0

    print()
    for product in products:
        label = STATUS_LABELS.get(product.status, product.status)
        sources = "+".join(product.sources)
        print(f"  {product.name}")
        print(f"    {product.summary[:90] or '（无简介）'}")
        print(f"    {label} · {sources} · {product.url}")
        print()
    print(f"  共 {len(products)} 个\n")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="xocto", description="全球 AI 应用雷达 —— 采集层"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_collect = sub.add_parser("collect", help="跑一次采集")
    p_collect.add_argument("--dry-run", action="store_true", help="只看会抓到什么，不写盘")
    p_collect.add_argument("--date", help="指定归档日期 YYYY-MM-DD，默认今天")
    p_collect.add_argument(
        "--force",
        action="store_true",
        help="用本次结果整份重写当天存档（改了解析规则后重采时用）",
    )
    p_collect.set_defaults(func=cmd_collect)

    p_build = sub.add_parser("build", help="把 data/ 生成成静态网站")
    p_build.set_defaults(func=cmd_build)

    p_prune = sub.add_parser("prune", help="清掉过老的原始存档，控制仓库体积")
    p_prune.add_argument("--keep-days", type=int, default=30, help="保留最近几天，默认 30")
    p_prune.set_defaults(func=cmd_prune)

    p_rebuild = sub.add_parser(
        "rebuild", help="从原始存档重建产品池（改了解析规则之后用；旧的会备份不会删）"
    )
    p_rebuild.set_defaults(func=cmd_rebuild)

    p_status = sub.add_parser("status", help="看数据现状")
    p_status.set_defaults(func=cmd_status)

    p_health = sub.add_parser(
        "health", help="检查有没有源在静默变质（该有产出却 0 条）"
    )
    p_health.add_argument("--date", help="检查哪天，默认今天")
    p_health.set_defaults(func=cmd_health)

    p_pool = sub.add_parser("pool", help="列出产品池")
    p_pool.add_argument("--new", action="store_true", help="只看还没过滤的")
    p_pool.add_argument("--status", help=f"按状态筛选：{', '.join(STATUS_LABELS)}")
    p_pool.add_argument("--limit", type=int, default=30, help="最多显示几个，默认 30")
    p_pool.set_defaults(func=cmd_pool)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\n中断了。已经写入的数据不受影响。", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
