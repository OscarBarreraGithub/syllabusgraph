"""Overlap is a measured subgraph, not a course or an invented consensus."""

from copy import deepcopy

import pytest

from syllabusgraph.backbone import shared_backbone
from syllabusgraph.io import ProjectError


def book(id, group=None):
    return {"project_id": id, "title": id, **({"comparison_group": group} if group else {})}


def graph(memberships, edges=()):
    return {
        "nodes": [
            {"id": id, "origins": [{"project": b, "node": id} for b in books]}
            for id, books in memberships.items()
        ],
        "edges": [
            {"id": f"e{i}", "from": a, "to": b, "relation": rel}
            for i, (a, b, rel) in enumerate(edges)
        ],
    }


def test_grouped_volumes_and_exact_overlap_distribution():
    direct = {
        "all": ["a", "b", "c1", "c2"],
        "three": ["a", "b", "c1"],
        "two": ["a", "c2"],
        "one": ["c1", "c2"],
        "imported": [],
    }
    knowledge = graph(direct, [("all", "three", "prerequisite"), ("three", "two", "evidence")])
    before = deepcopy(knowledge)
    entries = [
        book("a"),
        book("b"),
        book("c1", {"id": "c", "title": "C"}),
        book("c2", {"id": "c", "title": "C"}),
    ]
    result = shared_backbone(knowledge, direct, entries)
    assert result["available"]
    family = result["perspectives"]["textbooks"]
    assert family["distribution"] == [
        {"count": 0, "nodes": 1},
        {"count": 1, "nodes": 1},
        {"count": 2, "nodes": 1},
        {"count": 3, "nodes": 2},
    ]
    assert family["levels"][-1]["nodes"] == ["all", "three"]
    assert family["levels"][-1]["edges"] == ["e0"]
    assert result["perspectives"]["volumes"]["levels"][-1]["nodes"] == ["all"]
    assert knowledge == before


def test_do_not_invent_shortcuts_through_nodes_outside_the_core():
    direct = {"a": ["x", "y", "z"], "bridge": ["x", "y"], "b": ["x", "y", "z"]}
    knowledge = graph(direct, [("a", "bridge", "prerequisite"), ("bridge", "b", "prerequisite")])
    result = shared_backbone(knowledge, direct, [book(id) for id in "xyz"])
    core = result["perspectives"]["textbooks"]["levels"][-1]
    assert core["nodes"] == ["a", "b"]
    assert core["edges"] == []
    assert len(core["components"]) == core["isolated"] == 2
    broader = result["perspectives"]["textbooks"]["levels"][0]
    assert len(broader["components"]) == 1
    assert len(broader["edges"]) == 2


def test_all_relation_types_count_as_connections_but_are_reported_separately():
    direct = {"a": ["x", "y"], "b": ["x", "y"], "c": ["x", "y"]}
    knowledge = graph(direct, [("a", "b", "alternative"), ("b", "a", "evidence")])
    core = shared_backbone(knowledge, direct, [book("x"), book("y")])["perspectives"]["textbooks"][
        "levels"
    ][0]
    assert core["relations"] == {"alternative": 1, "evidence": 1}
    assert [len(c["nodes"]) for c in core["components"]] == [2, 1]
    assert core["isolated"] == 1


def test_missing_exports_do_not_silently_reduce_the_comparison():
    direct = {"a": ["x", "y"]}
    knowledge = graph({"a": ["x", "y", "z"]})
    result = shared_backbone(knowledge, direct, [book("x"), book("y")])
    assert not result["available"]
    assert result["missing_books"] == ["z"]
    assert not shared_backbone(graph({}), {}, [book("x")])["available"]


def test_grouping_is_explicit_and_conflicting_titles_are_rejected():
    direct = {"a": ["book-1", "book-2"]}
    knowledge = graph(direct)
    result = shared_backbone(knowledge, direct, [book("book-1"), book("book-2")])
    assert len(result["perspectives"]["textbooks"]["units"]) == 2
    with pytest.raises(ProjectError, match="titles must agree"):
        shared_backbone(
            knowledge,
            direct,
            [book("book-1", {"id": "x", "title": "X"}), book("book-2", {"id": "x", "title": "Y"})],
        )
