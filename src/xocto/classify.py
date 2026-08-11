"""赛道归类。

用户找东西是按方向找的 —— "有没有做视频的"，不是"有没有用 RAG 的"。
所以分类按用户会问的问题分，不按技术形态分。

这里只做确定性的关键词粗分，给每个产品一个初始赛道。
分错的由 Claude 在分析阶段直接改产品档案里的 category 字段 ——
判断归 Claude，规则归 Python，两者不混。
"""

from __future__ import annotations

import re

from .models import CATEGORIES, Product

# 匹配顺序即优先级：越靠前越具体，先命中先赢。
# 一个产品命中多条时，"基础层"和"创作"这种特征鲜明的要早于"开发""效率"这种宽泛的。
_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        # 最先判这一条：产品是给 agent 用的，还是给人用的。
        # 这一刀比任何品类划分都重要 —— 给 agent 造工具的现在极度拥挤，
        # 给人用的那一端反而被忽视。
        "基础层",
        (
            "for ai agents", "for agents", "for any ai agent", "for coding agents",
            "agent activity", "agentic workflow", "multi-agent", "agent runtime",
            "agent framework", "agent harness", "agents against", "for agents:",
            "explained for agents", "gateway", "router", "routing", "inference",
            "gpu", "cuda", "fpga", "sandbox", "sandboxes", "runtime", "orchestrat",
            "observability", "tracing", "eval", "benchmark", "quantiz",
            "fine-tune", "finetune", "vector", "embedding", "rag pipeline",
            "memory for", "llm memory", "permanent memory", "mcp server",
            "mcp setup", "model context protocol", "serving", "context accelerator",
            "算力", "推理", "网关", "沙箱", "调度", "面向 ai agent", "给 ai agent",
        ),
    ),
    (
        # 大模型对话产品自成一类。它们是巨头的地盘，判断逻辑和小工具完全不同：
        # 看的是市场格局变化，不是"解决了什么痛点"。
        "通用助手",
        (
            "chat with", "chatbot", "conversational ai", "ai chat",
            "智能助手", "对话助手", "智能对话", "ai 助手", "ai助手", "大模型",
            "一站式解决", "超级生产力",
        ),
    ),
    (
        "AI + 创作",
        (
            "video", "image", "photo", "picture", "illustrat", "draw", "paint",
            "story", "drama", "script", "screenplay", "film", "cinema", "canvas",
            "design", "designer", "creative", "music", "audio", "voice clone",
            "slides", "ppt", "presentation", "comfyui", "lora", "diffusion",
            "storyboard", "avatar", "3d", "render",
            "短剧", "影视", "创作", "分镜", "绘本", "配图", "剪辑", "素材",
        ),
    ),
    (
        "AI + 商业",
        (
            "crm", "sales", "gtm", "go-to-market", "marketing", "seo", "ads",
            "advertis", "ecommerce", "e-commerce", "shop", "store", "invoice",
            "billing", "pricing", "revenue", "lead", "outreach", "hiring",
            "recruit", "job", "candidate", "customer", "market", "compliance",
            "legal", "contract", "finance", "trading", "stock", "investor",
            "营销", "销售", "招聘", "股", "金融", "合规", "客户",
        ),
    ),
    (
        "AI + 开发",
        (
            "coding", "code", "codex", "developer", "programming", "debug",
            "refactor", "compiler", "ide", "vscode", "terminal", "cli", "shell",
            "git", "github", "pull request", "code review", "devops", "deploy",
            "api client", "sdk", "harness", "skill", "prompt", "agent framework",
            "编码", "代码", "开发",
        ),
    ),
    (
        "AI + 生活",
        (
            "health", "fitness", "medical", "doctor", "wellness", "sleep",
            "nutrition", "workout", "social", "friend", "companion", "dating",
            "game", "play", "puzzle", "entertain", "travel", "recipe", "cook",
            "education", "learn", "study", "course", "tutor", "kids", "language",
            "健康", "医", "社交", "游戏", "教育", "学习", "旅行", "中医", "婚恋",
        ),
    ),
    (
        "AI + 效率",
        (
            "note", "task", "todo", "document", "wiki", "knowledge base",
            "workflow", "automat", "meeting", "calendar", "schedul",
            "email", "inbox", "summar", "translat", "transcri", "organize",
            "productivity", "storage", "boring work", "step-by-step guide",
            "笔记", "任务", "文档", "知识", "自动化", "会议", "日程", "效率", "整理",
        ),
    ),
)

DEFAULT_CATEGORY = "AI + 效率"

# 榜单源会告诉我们一个产品上了哪些细分榜。这是现成的品类答案，
# 比从名字和描述里猜关键词准得多，所以优先用它。
_BOARD_CATEGORY: tuple[tuple[str, str], ...] = (
    ("视频", "AI + 创作"),
    ("图片", "AI + 创作"),
    ("图像", "AI + 创作"),
    ("音乐", "AI + 创作"),
    ("PPT", "AI + 创作"),
    ("设计", "AI + 创作"),
    ("Coding", "AI + 开发"),
    ("编程", "AI + 开发"),
    ("Agent", "基础层"),
    ("云", "基础层"),
    ("算力", "基础层"),
    ("角色", "AI + 生活"),
    ("陪伴", "AI + 生活"),
    ("搜索", "通用助手"),
    ("聊天机器人", "通用助手"),
    ("会议", "AI + 效率"),
    ("办公", "AI + 效率"),
)


def classify_boards(boards: list[str]) -> str:
    """从细分榜名判赛道。总榜（国内总榜/全球总榜）不带品类信息，跳过。"""
    for board in boards:
        if "总榜" in board:
            continue
        for keyword, category in _BOARD_CATEGORY:
            if keyword.lower() in board.lower():
                return category
    return ""


def classify_text(*chunks: str) -> str:
    """按关键词判赛道。全部落空时返回默认值。"""
    haystack = " ".join(c for c in chunks if c).lower()
    if not haystack.strip():
        return DEFAULT_CATEGORY

    for category, keywords in _RULES:
        for kw in keywords:
            # 英文词按词边界匹配，避免 "code" 命中 "encoded"；
            # 中文没有词边界，直接子串匹配。
            if kw.isascii():
                if re.search(r"(?<![a-z])" + re.escape(kw), haystack):
                    return category
            elif kw in haystack:
                return category

    return DEFAULT_CATEGORY


def classify(product: Product) -> str:
    """给一个产品判赛道。已经归过类的不动 —— 那可能是人工改过的。"""
    if product.category in CATEGORIES:
        return product.category

    # 有细分榜信息就用它，那是现成答案
    boards: list[str] = []
    for sighting in product.sightings:
        boards.extend(sighting.metrics.get("boards") or [])
    if boards:
        from_board = classify_boards(boards)
        if from_board:
            return from_board

    return classify_text(product.name, product.summary)
