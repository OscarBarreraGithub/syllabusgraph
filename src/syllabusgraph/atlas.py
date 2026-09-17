"""Project reviewed record links onto reviewed primary concept memberships.

An atlas link says that specific records are connected. It never turns that
existential claim into a universal concept prerequisite or a course order.
"""

from collections import Counter, defaultdict

from .io import ProjectError


def concept_atlas(inventory, books, entries):
    project_ids = {p["id"] for p in inventory["projects"]}
    by_project = {b["project_id"]: b for b in books}
    if not project_ids <= set(by_project):
        raise ProjectError("The concept inventory needs all of its book graphs in the catalog.")
    works, membership = {}, {}
    for entry in entries:
        project = entry["project_id"]
        if project not in project_ids:
            continue
        group = entry.get("comparison_group", {"id": project, "title": entry["title"]})
        work = works.setdefault(group["id"], {**group, "projects": []})
        work["projects"].append(project)
        membership[project] = group["id"]
    if set(membership) != project_ids:
        raise ProjectError("Every inventory book needs an explicit textbook catalog entry.")
    nodes, owners, internal = [], {}, Counter()
    for concept in inventory["concepts"]:
        treatments = []
        for treatment in concept["treatments"]:
            identity = (treatment["project"], treatment["node"])
            if identity in owners:
                raise ProjectError("A source record cannot have two primary concept homes.")
            owners[identity] = concept["id"]
            original = next(n for n in by_project[identity[0]]["knowledge"]["nodes"] if n["id"] == identity[1])
            treatments.append({**treatment, "label": original["label"]})
        nodes.append({**concept, "treatments": treatments,
                      "works": sorted({membership[p] for p in concept["independent_book_counts"]})})
    links = defaultdict(list)
    for project in sorted(project_ids):
        native = set(inventory["coverage_sources"][project])
        for edge in by_project[project]["knowledge"]["edges"]:
            source, target = owners.get((project, edge["from"])), owners.get((project, edge["to"]))
            if not source or not target:
                raise ProjectError("Every book relationship endpoint needs a primary concept home.")
            if not native & {e["source"] for e in edge["evidence"]}:
                continue
            if source == target:
                internal[source] += 1
                continue
            key = tuple(sorted((source, target)))
            links[key].append({"project": project, "edge": edge["id"],
                               "from": edge["from"], "to": edge["to"],
                               "from_concept": source, "to_concept": target,
                               "relation": edge["relation"], "necessity": edge["necessity"]})
    result_links = []
    for (source, target), records in sorted(links.items()):
        result_links.append({"from": source, "to": target, "records": records,
                             "works": sorted({membership[r["project"]] for r in records})})
    for node in nodes:
        node["internal_relationships"] = internal[node["id"]]
    shared = {n["id"] for n in nodes if len(n["works"]) == len(works)}
    shared_links = [e for e in result_links if {e["from"], e["to"]} <= shared]
    neighbors = {identity: set() for identity in shared}
    for edge in shared_links:
        neighbors[edge["from"]].add(edge["to"])
        neighbors[edge["to"]].add(edge["from"])
    remaining, components = set(shared), 0
    while remaining:
        components += 1
        frontier = [remaining.pop()]
        while frontier:
            for neighbor in neighbors[frontier.pop()] & remaining:
                remaining.remove(neighbor)
                frontier.append(neighbor)
    return {"version": 1, "concepts": nodes, "groups": inventory["groups"],
            "works": list(works.values()), "links": result_links,
            "counts": {"concepts": len(nodes), "records": len(owners),
                       "all_works": sum(len(n["works"]) == len(works) for n in nodes),
                       "two_or_more": sum(len(n["works"]) >= 2 for n in nodes),
                       "shared_connections": len(shared_links), "shared_components": components,
                       "within_concept_relationships": sum(internal.values()),
                       "between_concept_relationships": sum(len(v) for v in links.values())},
            "connection_meaning": "Specific records assigned to these concepts have recorded relationships. "
                                  "Connections do not assert universal concept prerequisites or a course order.",
            "coverage_meaning": "Native-source treatments assigned to each primary concept. "
                                "Missing assignments are not certified absence; volumes are grouped explicitly."}
