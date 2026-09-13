"""Deterministic graph operations independent of course subject or storage."""

from __future__ import annotations

from collections import defaultdict
import heapq
from typing import Callable, Iterable

from .io import ProjectError


def topological(
    nodes: Iterable[str], edges: Iterable[tuple[str, str]], key: Callable | None = None
) -> list[str]:
    ids = set(nodes)
    adjacency = {n: set() for n in ids}
    indegree = dict.fromkeys(ids, 0)
    for source, target in edges:
        if source not in ids or target not in ids:
            raise ProjectError("An ordering edge names a missing vertex.")
        if target not in adjacency[source]:
            adjacency[source].add(target)
            indegree[target] += 1
    key = key or (lambda n: n)
    ready = [(key(n), n) for n in ids if indegree[n] == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        _, node = heapq.heappop(ready)
        order.append(node)
        for child in sorted(adjacency[node]):
            indegree[child] -= 1
            if indegree[child] == 0:
                heapq.heappush(ready, (key(child), child))
    if len(order) != len(ids):
        pending = sorted(n for n in ids if indegree[n])
        raise ProjectError("Ordering cycle; inspect prerequisites among: " + ", ".join(pending))
    return order


def reduction(nodes: Iterable[str], edges: Iterable[tuple[str, str]]) -> list[tuple[str, str]]:
    pairs = set(edges)
    order = topological(nodes, pairs)
    adjacency = defaultdict(set)
    descendants = {n: set() for n in order}
    for source, target in pairs:
        adjacency[source].add(target)
    for source in reversed(order):
        for target in adjacency[source]:
            descendants[source].add(target)
            descendants[source].update(descendants[target])
    return sorted(
        (a, b)
        for a, b in pairs
        if not any(b in descendants[other] for other in adjacency[a] if other != b)
    )


def layout(nodes: Iterable[str], edges: Iterable[tuple[str, str]]) -> dict:
    pairs = set(edges)
    order = topological(nodes, pairs)
    parents = defaultdict(list)
    for source, target in sorted(pairs):
        parents[target].append(source)
    layers, rows = {}, defaultdict(int)
    positions = []
    for node in order:
        depth = max((layers[p] + 1 for p in parents[node]), default=0)
        layers[node] = depth
        positions.append({"id": node, "x": 40 + depth * 260, "y": 40 + rows[depth] * 90})
        rows[depth] += 1
    return {
        "nodes": positions,
        "edges": reduction(order, pairs),
        "width": 280 + max(layers.values(), default=0) * 260,
        "height": 110 + max(rows.values(), default=0) * 90,
    }
