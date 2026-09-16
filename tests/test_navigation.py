"""Presentation metadata must not invent source order or lose graph records."""

from copy import deepcopy

from syllabusgraph.navigation import chapter_index, reading_views


def payload(id, nodes, groups=None, sources=None):
    return {
        "project_id": id,
        "title": id,
        "sources": sources if sources is not None else [{"id": id}],
        "knowledge": {"nodes": nodes, "groups": groups or [], "edges": []},
    }


def node(id, source, pages, **extra):
    return {"id": id, "label": id, "evidence": [{"source": source, "pages": pages}], **extra}


def test_chapter_coordinates_only_are_published():
    assert chapter_index(
        {
            "sections": [
                {
                    "section": "3",
                    "kind": "chapter",
                    "first": 10,
                    "last": 20,
                    "private_note": "omitted",
                },
                {"section": "3.1", "kind": "subsection", "first": 11, "last": 12},
                {"section": "4", "kind": "chapter", "first": "unknown", "last": 30},
            ]
        }
    ) == [{"id": "3", "label": "Chapter 3", "first": 10, "last": 20}]


def test_exact_origins_determine_shared_reading_order_not_shared_page_numbers():
    book = payload(
        "book",
        [node("early", "book", [2], group="g"), node("late", "book", [12])],
        [{"id": "g", "title": "An existing topic"}],
    )
    shared = payload(
        "shared",
        [
            node("a", "different", [2], origins=[{"project": "book", "node": "late"}]),
            node("b", "different", [12], origins=[{"project": "book", "node": "early"}]),
            node("c", "different", [4]),  # Globally searchable, no invented book attribution.
        ],
    )
    saved = deepcopy(shared)
    chapters = {
        "book": [
            {"id": "1", "label": "Chapter 1", "first": 1, "last": 5},
            {"id": "2", "label": "Chapter 2", "first": 6, "last": 15},
        ]
    }
    view = reading_views(shared, [book], chapters)[0]
    assert [c["nodes"] for c in view["chapters"]] == [["b"], ["a"]]
    assert view["chapters"][0]["topics"] == ["An existing topic"]
    assert view["node_count"] == 2
    assert shared == saved


def test_imported_and_companion_pagination_cannot_create_false_chapter_membership():
    book = payload(
        "book",
        [
            node("local", "book", [4, 12]),
            node("imported", "different", [4], origins=[{"project": "different", "node": "x"}]),
            node("notation", "roman-pages", [4]),
            node("unmapped", "book", [50]),
        ],
        sources=[{"id": "book"}, {"id": "roman-pages"}],
    )
    chapters = {
        "book": [
            {"id": "1", "label": "Chapter 1", "first": 1, "last": 5},
            {"id": "2", "label": "Chapter 2", "first": 6, "last": 15},
        ]
    }
    view = reading_views(book, [book], chapters)[0]
    assert view["chapters"][0]["nodes"] == ["local"]
    assert view["chapters"][1]["nodes"] == ["local"]
    assert set(view["chapters"][2]["nodes"]) == {"imported", "notation", "unmapped"}
    assert view["node_count"] == 4  # A multi-chapter citation is counted once.


def test_generic_and_empty_graphs_need_no_inventory():
    graph = payload(
        "example",
        [node("a", "primer", [1], group="g"), node("b", "primer", [2])],
        [{"id": "g", "title": "First topic"}],
        [{"id": "primer"}],
    )
    for available in ([graph], []):
        view = reading_views(graph, available, {})[0]
        assert {n for c in view["chapters"] for n in c["nodes"]} == {"a", "b"}
        assert view["chapters"][0]["label"] == "First topic"
    empty = payload("blank", [])
    assert reading_views(empty, [empty], {})[0]["chapters"] == []


def test_inventory_can_name_a_source_different_from_the_project_id():
    book = payload(
        "custom-project",
        [node("a", "primary", [4]), node("b", "companion", [4])],
        sources=[{"id": "primary"}, {"id": "companion"}],
    )
    chapters = chapter_index(
        {
            "source": "primary",
            "sections": [{"section": "1", "kind": "chapter", "first": 1, "last": 10}],
        }
    )
    view = reading_views(book, [book], {"custom-project": chapters})[0]
    assert view["chapters"][0]["nodes"] == ["a"]
    assert view["chapters"][1]["nodes"] == ["b"]
