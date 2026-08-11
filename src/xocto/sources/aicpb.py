"""AICPB（AI 产品榜）—— 中文世界唯一拿得到真实数据的源。

和另外三个源性质完全不同，用之前先搞清楚：

- PH / HN / GitHub 抓的是**刚冒出来的东西**，没数据，靠判断。
- AICPB 抓的是**已经跑出规模的东西**，有真实的访问量和月活，而且有环比。

所以它不是"发现新产品"用的，是回答两个问题用的：
  1. 中国市场上什么在真涨（增长率榜上环比 +3479% 这种异常值就是信号）
  2. 手上这个产品到底有没有人用（拿它当核实层）

榜单是月度更新的，每天抓没意义，但抓一次成本极低，就交给去重层兜着。
"""

from __future__ import annotations

import re
import time

from ..models import RawItem, now_iso
from .base import Http, HttpError, register

BASE = "https://www.aicpb.com"
RANKING_PATH = "/ai-rankings/products/{name}"

DEFAULT_RANKINGS = ("china-ai-growth-rate-ranking",)

# 榜单表格的一行：产品链接 → 数值 → 环比
# 结构来自实测，页面是服务端渲染的，不需要跑 JS。
_ROW = re.compile(
    r'<a href="(?P<path>/product/[^"]+)" class="decoration-none[^"]*"[^>]*>(?P<name>[^<]+)</a>'
    r'.{0,400}?<div class="flex items-center justify-center">(?P<value>[^<]{1,20})</div>'
    r'.{0,200}?<span class="z-9">(?P<mom>[^<]{1,20})</span>',
    re.S,
)

# 榜单标题，用来标注这批数据是哪个榜的什么口径
_HEADING = re.compile(r"AICPB[^<]{0,80}Rankings[^<]{0,40}", re.S)

_UNITS = {"K": 1_000, "M": 1_000_000, "B": 1_000_000_000}

# 榜单页里产品描述那个标签是空的（客户端才填），所以描述只能去详情页拿。
_META_DESC = re.compile(r'<meta name="description" content="([^"]*)"')
# 详情页会列出这个产品上了哪些细分榜。这比描述更有用 ——
# "聊天机器人榜第 4" 直接说明了它是什么品类、什么地位。
_BOARD = re.compile(r"AI产品榜\s*·\s*([^第<\n]{2,20}?)\s*第\s*(\d+)\s*名")
DETAIL_DELAY = 0.35  # 秒。48 个产品逐个抓，别把人家站点打疼了


@register("aicpb")
def fetch(cfg: dict, http: Http) -> list[RawItem]:
    rankings = cfg.get("rankings") or list(DEFAULT_RANKINGS)
    collected = now_iso()
    by_id: dict[str, RawItem] = {}

    for name in rankings:
        url = BASE + RANKING_PATH.format(name=name)
        try:
            page = http.get_text(url)
        except HttpError as exc:
            print(f"    ! 榜单「{name}」抓取失败：{exc}")
            continue

        rows = list(_ROW.finditer(page))
        print(f"    [{name}] {len(rows)} 条")

        for row in rows:
            item = _parse_row(row, name, url, collected)
            if item is None:
                continue
            # 同一产品上多个榜时只留一条，但把榜名累积起来 ——
            # "同时在增长率榜和总榜上"本身就是信息
            existing = by_id.get(item.external_id)
            if existing is None:
                by_id[item.external_id] = item
            else:
                merged_boards = list(existing.extra["rankings"])
                if name not in merged_boards:
                    merged_boards.append(name)
                    by_id[item.external_id] = _with_rankings(existing, merged_boards)

    items = list(by_id.values())

    # 榜单只给名字和数字。没有一句话说明它是什么，产品卡片就是废的 ——
    # 所以逐个进详情页补描述和它上过的细分榜。
    if cfg.get("fetch_details", True) and items:
        items = _enrich(items, http)

    return items


def _enrich(items: list[RawItem], http: Http) -> list[RawItem]:
    """逐个抓详情页补描述与细分榜。单个失败不影响其他。"""
    from dataclasses import replace

    print(f"    补充详情（{len(items)} 个）", end="", flush=True)
    out: list[RawItem] = []
    failed = 0

    for i, item in enumerate(items):
        if i:
            time.sleep(DETAIL_DELAY)
        try:
            page = http.get_text(BASE + "/zh" + item.payload["path"])
        except HttpError:
            failed += 1
            out.append(item)
            continue

        desc = ""
        match = _META_DESC.search(page)
        if match:
            desc = match.group(1).strip()

        boards = [
            {"board": b.strip(), "rank": int(r)} for b, r in _BOARD.findall(page)
        ]

        out.append(
            replace(
                item,
                summary=desc or item.summary,
                extra={**item.extra, "boards": boards},
                # 也放进 metrics，这样合并进产品档案后分类器还拿得到 ——
                # "聊天机器人榜第 4" 比任何关键词猜测都准
                metrics={**item.metrics, "boards": [b["board"] for b in boards]},
            )
        )
        if i % 10 == 9:
            print(".", end="", flush=True)

    got = sum(1 for x in out if x.summary)
    print(f" 拿到描述 {got}/{len(items)}" + (f"，{failed} 个失败" if failed else ""))
    return out


def _parse_row(row: re.Match, ranking: str, ranking_url: str, collected: str) -> RawItem | None:
    path = row.group("path")
    name = row.group("name").strip()
    if not path or not name:
        return None

    # 路径尾段形如 webid1D6F34EC9 / appid1D6F37A51，前缀就区分了平台
    external_id = path.rstrip("/").split("/")[-1]
    if not external_id:
        return None

    platform = "app" if external_id.startswith("appid") else "web"
    raw_value = row.group("value").strip()
    raw_mom = row.group("mom").strip()

    return RawItem(
        source="aicpb",
        external_id=external_id,
        title=name,
        # 这是榜单页不是产品官网 —— aicpb.com 已列入聚合站，
        # 不会因为域名相同而被误判成同一个产品
        url=BASE + path,
        summary="",
        published_at="",  # 月度榜，没有发布时间这个概念
        collected_at=collected,
        metrics={
            # 原始字符串和解析值都留着：解析可能出错，原文永远不会
            "raw_value": raw_value,
            "value": _to_number(raw_value),
            "metric": "mau" if platform == "app" else "visits",
            "mom_raw": raw_mom,
            "mom_percent": _to_percent(raw_mom),
        },
        extra={
            "builder": "",  # 榜单不提供创始人
            "platform": platform,
            "rankings": [ranking],
            "ranking_url": ranking_url,
        },
        payload={"path": path, "value": raw_value, "mom": raw_mom, "ranking": ranking},
    )


def _with_rankings(item: RawItem, rankings: list[str]) -> RawItem:
    """返回榜单列表更新后的新对象（RawItem 是 frozen 的）。"""
    from dataclasses import replace

    return replace(item, extra={**item.extra, "rankings": rankings})


def _to_number(text: str) -> float | None:
    """把 "3.70M" 变成 3700000.0。解析不了返回 None，不猜。"""
    match = re.match(r"^([\d.]+)\s*([KMB])?$", text.strip(), re.I)
    if not match:
        return None
    try:
        value = float(match.group(1))
    except ValueError:
        return None
    unit = (match.group(2) or "").upper()
    return value * _UNITS.get(unit, 1)


def _to_percent(text: str) -> float | None:
    """把 "3479.98%" 变成 3479.98。解析不了返回 None。"""
    match = re.match(r"^([+-]?[\d.]+)\s*%$", text.strip())
    if not match:
        return None
    try:
        return float(match.group(1))
    except ValueError:
        return None
