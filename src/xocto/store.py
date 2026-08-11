"""文件存储层。

不用数据库，理由见 CLAUDE.md：蔡蔡要能直接打开看，要好备份，
要能被 Claude Code 直接 grep 和读取。

布局：
    data/raw/YYYY-MM-DD.jsonl   当日原始抓取，只追加
    data/pool/<slug>.md         产品档案，frontmatter 存结构化数据，正文留给人写
    data/analysis/<slug>.md     分析结果
    data/reports/YYYY-MM-DD.md  每日简报
"""

from __future__ import annotations

import json
import os
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator

import yaml

from .models import Product, RawItem, Sighting

# 正文分隔标记。这一行以下是自由区，机器写入时永不覆盖。
NOTES_MARKER = "## 笔记"


def project_root() -> Path:
    """项目根目录。允许用 XOCTO_HOME 覆盖，方便测试和迁移。"""
    env = os.environ.get("XOCTO_HOME")
    if env:
        return Path(env).expanduser().resolve()
    # store.py -> xocto -> src -> 项目根
    return Path(__file__).resolve().parents[2]


class Store:
    """所有落盘操作的唯一入口。"""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or project_root()
        self.data_dir = self.root / "data"
        self.raw_dir = self.data_dir / "raw"
        self.pool_dir = self.data_dir / "pool"
        self.analysis_dir = self.data_dir / "analysis"
        self.reports_dir = self.data_dir / "reports"
        self.config_dir = self.root / "config"

    def ensure_dirs(self) -> None:
        for d in (self.raw_dir, self.pool_dir, self.analysis_dir, self.reports_dir):
            d.mkdir(parents=True, exist_ok=True)

    # ---------- 原始层 ----------

    def raw_path(self, day: date | None = None) -> Path:
        day = day or datetime.now(timezone.utc).date()
        return self.raw_dir / f"{day.isoformat()}.jsonl"

    def read_raw(self, day: date | None = None) -> list[RawItem]:
        """读某天的原始记录。文件不存在返回空列表，损坏的行跳过不中断。"""
        path = self.raw_path(day)
        if not path.exists():
            return []

        items: list[RawItem] = []
        with path.open("r", encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    items.append(RawItem.from_dict(json.loads(line)))
                except (json.JSONDecodeError, KeyError) as exc:
                    print(f"  ! 跳过损坏的记录 {path.name}:{lineno} — {exc}")
        return items

    def append_raw(
        self, items: Iterable[RawItem], day: date | None = None, *, overwrite: bool = False
    ) -> int:
        """追加原始记录，按 source+external_id 幂等。

        返回实际写入的条数。同一天重复跑，已存在的记录不会重复写入。

        overwrite=True 时整份重写当天存档 —— 只在改了解析逻辑、需要用
        新代码重新解析当天数据时用。这会丢掉当天已存但本次没抓到的记录。
        """
        path = self.raw_path(day)
        path.parent.mkdir(parents=True, exist_ok=True)

        if overwrite:
            rows = list(items)
            body = "".join(
                json.dumps(item.to_dict(), ensure_ascii=False) + "\n" for item in rows
            )
            _atomic_write(path, body)
            return len(rows)

        existing_keys = {item.key for item in self.read_raw(day)}
        new_items = [item for item in items if item.key not in existing_keys]
        if not new_items:
            return 0

        with path.open("a", encoding="utf-8") as fh:
            for item in new_items:
                fh.write(json.dumps(item.to_dict(), ensure_ascii=False) + "\n")
        return len(new_items)

    def raw_days(self) -> list[date]:
        """已有原始数据的日期，升序。"""
        days: list[date] = []
        for path in self.raw_dir.glob("*.jsonl"):
            try:
                days.append(date.fromisoformat(path.stem))
            except ValueError:
                continue
        return sorted(days)

    # ---------- 产品池 ----------

    def product_path(self, slug: str) -> Path:
        return self.pool_dir / f"{slug}.md"

    def load_product(self, slug: str) -> Product | None:
        path = self.product_path(slug)
        if not path.exists():
            return None
        return self._parse_product(path)

    def iter_products(self) -> Iterator[Product]:
        """遍历产品池。单个文件损坏只跳过它，不影响其他。"""
        for path in sorted(self.pool_dir.glob("*.md")):
            product = self._parse_product(path)
            if product is not None:
                yield product

    def save_product(self, product: Product) -> Path:
        """写产品档案。

        正文的「笔记」区如果文件已存在则原样保留 —— 那是人写的东西，
        机器永远不覆盖。
        """
        path = self.product_path(product.slug)
        notes = product.notes
        if path.exists() and not notes:
            existing = self._parse_product(path)
            if existing is not None:
                notes = existing.notes

        front = {
            "slug": product.slug,
            "name": product.name,
            "builder": product.builder,
            "category": product.category,
            "url": product.url,
            "canonical_url": product.canonical_url,
            "summary": product.summary,
            "first_seen": product.first_seen,
            "last_seen": product.last_seen,
            "status": product.status,
            "sources": list(product.sources),
            "sightings": [s.to_dict() for s in product.sightings],
        }
        front_yaml = yaml.safe_dump(front, allow_unicode=True, sort_keys=False, width=100)

        body = (
            f"---\n{front_yaml}---\n\n"
            f"# {product.name}\n\n"
            f"{product.summary or '_（源没给简介）_'}\n\n"
            f"{NOTES_MARKER}\n\n"
            f"{notes}\n"
        )
        _atomic_write(path, body)
        return path

    def _parse_product(self, path: Path) -> Product | None:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"  ! 读不了 {path.name} — {exc}")
            return None

        if not text.startswith("---"):
            print(f"  ! {path.name} 缺少 frontmatter，跳过")
            return None

        parts = text.split("---", 2)
        if len(parts) < 3:
            print(f"  ! {path.name} frontmatter 不完整，跳过")
            return None

        try:
            front = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError as exc:
            print(f"  ! {path.name} frontmatter 解析失败 — {exc}")
            return None

        notes = ""
        if NOTES_MARKER in parts[2]:
            notes = parts[2].split(NOTES_MARKER, 1)[1].strip()

        try:
            return Product(
                slug=front["slug"],
                name=front.get("name", front["slug"]),
                url=front.get("url", ""),
                canonical_url=front.get("canonical_url", ""),
                summary=front.get("summary", ""),
                first_seen=front.get("first_seen", ""),
                last_seen=front.get("last_seen", ""),
                status=front.get("status", "pending_filter"),
                sightings=tuple(
                    Sighting.from_dict(s) for s in (front.get("sightings") or [])
                ),
                builder=front.get("builder") or "",
                category=front.get("category") or "",
                notes=notes,
            )
        except KeyError as exc:
            print(f"  ! {path.name} 缺字段 {exc}，跳过")
            return None

    # ---------- 简报 ----------

    def report_path(self, day: date | None = None) -> Path:
        day = day or datetime.now(timezone.utc).date()
        return self.reports_dir / f"{day.isoformat()}.md"

    def analysis_path(self, slug: str) -> Path:
        return self.analysis_dir / f"{slug}.md"


def _atomic_write(path: Path, content: str) -> None:
    """先写临时文件再 rename，避免写到一半中断导致文件损坏。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(content)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise
