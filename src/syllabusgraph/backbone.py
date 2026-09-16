"""Describe recorded textbook overlap without changing the knowledge graph."""

from collections import Counter, defaultdict

from .io import ProjectError


def _level(knowledge, memberships, minimum):
    ids = {id for id, units in memberships.items() if len(units) >= minimum}
    edges = [e for e in knowledge["edges"] if e["from"] in ids and e["to"] in ids]
    adjacent = defaultdict(set)
    for e in edges:
        adjacent[e["from"]].add(e["to"])
        adjacent[e["to"]].add(e["from"])
    components, seen = [], set()
    for id in sorted(ids):
        if id in seen:
            continue
        seen.add(id)
        queue, component = [id], {id}
        while queue:
            for neighbor in sorted(adjacent[queue.pop()] - seen):
                seen.add(neighbor)
                component.add(neighbor)
                queue.append(neighbor)
        components.append(
            {
                "nodes": sorted(component),
                "edges": [e["id"] for e in edges if e["from"] in component],
            }
        )
    components.sort(key=lambda c: (-len(c["nodes"]), c["nodes"][0]))
    return {
        "minimum": minimum,
        "nodes": sorted(ids),
        "edges": [e["id"] for e in edges],
        "relations": dict(sorted(Counter(e["relation"] for e in edges).items())),
        "components": components,
        "isolated": sum(not adjacent[id] for id in ids),
    }


def shared_backbone(knowledge, direct_books, book_entries):
    """Units are explicit catalog groups, never inferred from author/name strings.

    Membership requires an independently treated book origin. Edges are the
    induced shared-graph relations, NOT claims of agreement by every book.
    Missing book exports are reported; they cannot silently lower the denominator.
    """
    referenced = {o["project"] for n in knowledge["nodes"] for o in n.get("origins", [])}
    books = [b for b in book_entries if b["project_id"] in referenced]
    missing = sorted(referenced - {b["project_id"] for b in books})
    if not books:
        return {"available": False, "missing_books": missing, "perspectives": {}}
    grouped, volumes = {}, []
    for book in books:
        project = book["project_id"]
        volumes.append({"id": project, "title": book["title"], "projects": [project]})
        group = book.get("comparison_group", {"id": project, "title": book["title"]})
        if group["id"] in grouped and grouped[group["id"]]["title"] != group["title"]:
            raise ProjectError("Comparison group titles must agree for a shared group ID.")
        unit = grouped.setdefault(group["id"], {**group, "projects": []})
        unit["projects"].append(project)
    perspectives = {}
    for name, units in (("textbooks", list(grouped.values())), ("volumes", volumes)):
        mapping = {project: u["id"] for u in units for project in u["projects"]}
        memberships = {
            n["id"]: sorted({mapping[b] for b in direct_books.get(n["id"], []) if b in mapping})
            for n in knowledge["nodes"]
        }
        distribution = Counter(map(len, memberships.values()))
        perspectives[name] = {
            "units": units,
            "memberships": memberships,
            "distribution": [{"count": i, "nodes": distribution[i]} for i in range(len(units) + 1)],
            "levels": [_level(knowledge, memberships, i) for i in range(2, len(units) + 1)],
        }
    return {
        "available": not missing and len(books) >= 2,
        "missing_books": missing,
        "perspectives": perspectives,
    }
