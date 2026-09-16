"""Reading views derived from public citations; these do not define a course."""

from collections import Counter
import re


def reading_views(payload, book_payloads, chapter_indexes):
    """A shared node appears wherever its exact book origins are encountered.

    Unmapped records remain in a named bucket, and all records remain globally
    searchable. The graph itself is not rewritten or pedagogically sequenced.
    """
    views = []
    for book in book_payloads:
        source = book["project_id"]
        groups = {g["id"]: g.get("title", g["id"]) for g in book["knowledge"]["groups"]}
        originals = {n["id"]: n for n in book["knowledge"]["nodes"]}
        chapters = [dict(c, nodes=[], topics=[]) for c in chapter_indexes.get(source, [])]
        if not chapters:
            # Independent examples need no extra inventory or QFT-specific config.
            chapters = [
                dict(id=g["id"], label=g.get("title", g["id"]), nodes=[], topics=[])
                for g in book["knowledge"]["groups"]
            ]
        miscellaneous = {"id": "other", "label": "Other concepts", "nodes": [], "topics": []}
        page_order, group_titles = {}, {}
        bibliography = {s["id"] for s in book["sources"]}
        primary_source = next((c["source"] for c in chapters if c.get("source")), source)
        if primary_source not in bibliography and len(bibliography) == 1:
            primary_source = next(iter(bibliography))
        for node in payload["knowledge"]["nodes"]:
            originals_here = (
                [node]
                if payload["project_id"] == source
                else [
                    originals[o["node"]]
                    for o in node.get("origins", [])
                    if o["project"] == source and o["node"] in originals
                ]
            )
            if not originals_here:
                continue
            assigned = False
            for original in originals_here:
                refs = [e for e in original.get("evidence", []) if e["source"] == primary_source]
                page_order[node["id"]] = min(
                    page_order.get(node["id"], 10**9),
                    min((p for e in refs for p in e.get("pages", [])), default=10**9),
                )
                for chapter in chapters:
                    if "first" in chapter:
                        belongs = any(
                            chapter["first"] <= p <= chapter["last"]
                            for e in refs
                            for p in e.get("pages", [])
                        )
                    else:
                        belongs = original.get("group") == chapter["id"]
                    if belongs:
                        if node["id"] not in chapter["nodes"]:
                            chapter["nodes"].append(node["id"])
                        group = groups.get(original.get("group"))
                        if group:
                            group_titles.setdefault(chapter["id"], []).append(group)
                        assigned = True
            if not assigned:
                miscellaneous["nodes"].append(node["id"])
        if miscellaneous["nodes"]:
            chapters.append(miscellaneous)
        chapters = [c for c in chapters if c["nodes"]]
        if not chapters:
            continue
        for chapter in chapters:
            chapter["nodes"].sort(key=lambda id: (page_order.get(id, 10**9), id))
            chapter["topics"] = [
                t for t, _ in Counter(group_titles.get(chapter["id"], [])).most_common(3)
            ]
        views.append(
            {
                "id": source,
                "title": book["title"],
                "chapters": chapters,
                "node_count": len({n for c in chapters for n in c["nodes"]}),
            }
        )
    if not views:
        groups = payload["knowledge"]["groups"]
        chapters = [
            {
                "id": g["id"],
                "label": g.get("title", g["id"]),
                "topics": [],
                "nodes": [
                    n["id"] for n in payload["knowledge"]["nodes"] if n.get("group") == g["id"]
                ],
            }
            for g in groups
        ]
        assigned = {n for c in chapters for n in c["nodes"]}
        rest = [n["id"] for n in payload["knowledge"]["nodes"] if n["id"] not in assigned]
        if rest:
            chapters.append({"id": "other", "label": "Concepts", "nodes": rest, "topics": []})
        views = [
            {
                "id": payload["project_id"],
                "title": payload["title"],
                "chapters": [c for c in chapters if c["nodes"]],
                "node_count": len(payload["knowledge"]["nodes"]),
            }
        ]
    return views


def chapter_index(coverage):
    """Publish just chapter coordinates from an existing public inventory."""
    return [
        {
            "id": str(c["section"]),
            "label": f"Chapter {c['section']}",
            "first": c["first"],
            "last": c["last"],
            **({"source": coverage["source"]} if coverage.get("source") else {}),
        }
        for c in coverage.get("sections", [])
        if c.get("kind") == "chapter"
        and re.fullmatch(r"\d+", str(c.get("section", "")))
        and isinstance(c.get("first"), int)
        and isinstance(c.get("last"), int)
    ]
