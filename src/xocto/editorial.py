"""Deterministic rejection of known non-editorial placeholder copy.

Relevance and significance remain decisions for the editorial model.
"""


def has_context_copy(text: str) -> bool:
    text = " ".join(text.split()).casefold()
    placeholders = (
        "公开材料尚不足", "内容未提供具体细节", "标题暗示",
        "非独立产品", "具体功能和影响待核验",
        "具体产品形态和流程待核验",
        "public evidence is not yet sufficient to confirm its workflow value",
        "public materials are not yet enough to confirm a concrete workflow",
    )
    return bool(text) and not any(marker in text for marker in placeholders)
