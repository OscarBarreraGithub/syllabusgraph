from copy import deepcopy
import json

import pytest

from syllabusgraph.export import markdown, mermaid
from syllabusgraph.graph import reduction, topological
from syllabusgraph.io import ProjectError, read_yaml, write_yaml
from syllabusgraph.planner import build_plan, compare_plans
from syllabusgraph.project import load_project, validate_knowledge


def minimal_plan(sample, target, level):
    plan = deepcopy(sample.plans["foundations"])
    plan.update(
        outcomes=[
            {"node": target, "level": level, "assessment": "Demonstrate the stated operation."}
        ],
        background={},
        include={},
        prior_plans=[],
        treatments={},
    )
    return plan


def test_source_and_course_data_are_separate(sample):
    first = build_plan(sample, "foundations")
    second = build_plan(sample, "simulation-lab")
    assert "sampling.confidence_interval" in first["order"]
    assert "sampling.confidence_interval" not in second["order"]
    assert second["background"]["sampling.confidence_interval"]["origin"] == "foundations"
    # Assumed outcomes cut their ancestry: only background actually used is reported.
    assert "sampling.standard_error" not in second["background"]


@pytest.mark.parametrize("level,needed", [("recognize", False), ("use", True), ("derive", True)])
def test_dependency_activates_at_target_mastery(sample, level, needed):
    result = build_plan(sample, minimal_plan(sample, "sampling.probability", level))
    assert ("sampling.fractions" in result["order"]) == needed


def test_insufficient_background_is_upgraded(sample):
    plan = minimal_plan(sample, "sampling.probability", "use")
    plan["background"] = {"sampling.fractions": "recognize"}
    result = build_plan(sample, plan)
    assert result["levels"]["sampling.fractions"] == "use"
    plan["background"]["sampling.fractions"] = "use"
    result = build_plan(sample, plan)
    assert "sampling.fractions" not in result["order"]
    assert result["background"]["sampling.fractions"]["required"] == "use"


def test_outcome_remains_taught_when_also_assumed(sample):
    plan = minimal_plan(sample, "sampling.probability", "use")
    plan["background"] = {"sampling.probability": "derive"}
    assert "sampling.probability" in build_plan(sample, plan)["order"]


def test_mastery_upgrade_walks_additional_edges(sample):
    plan = minimal_plan(sample, "sampling.standard_error", "use")
    assert "sampling.expectation" not in build_plan(sample, plan)["order"]
    plan["outcomes"][0]["level"] = "derive"
    assert "sampling.expectation" in build_plan(sample, plan)["order"]


def test_exclusion_is_visible_and_not_silently_readded(sample):
    plan = minimal_plan(sample, "sampling.probability", "use")
    plan["omit"] = ["sampling.fractions"]
    result = build_plan(sample, plan)
    assert "sampling.fractions" not in result["order"]
    assert any(
        i["code"] == "omitted_requirement" and i["severity"] == "error" for i in result["issues"]
    )


def test_downgrading_treatment_cannot_silently_lower_outcome(sample):
    plan = minimal_plan(sample, "sampling.probability", "derive")
    plan["treatments"] = {"sampling.probability": "recognize"}
    result = build_plan(sample, plan)
    assert result["levels"]["sampling.probability"] == "derive"
    assert any(i["code"] == "outcome_depth" for i in result["issues"])


def test_alternative_reverse_edge_is_not_a_cycle(sample):
    graph = deepcopy(sample.knowledge)
    edge = deepcopy(graph["edges"][0])
    edge.update(
        id="alternative-route", relation="alternative", **{"from": edge["to"], "to": edge["from"]}
    )
    graph["edges"].append(edge)
    validate_knowledge(sample.config, graph)
    sample.knowledge = graph
    assert build_plan(sample, "foundations")["order"]
    edge["relation"] = "prerequisite"
    with pytest.raises(ProjectError, match="cycle"):
        validate_knowledge(sample.config, graph)


def test_closure_and_order_invariants_for_every_target(sample):
    for target in sample.nodes:
        for level in sample.levels:
            result = build_plan(sample, minimal_plan(sample, target, level))
            taught = set(result["order"])
            positions = {n: i for i, n in enumerate(result["order"])}
            for edge in sample.knowledge["edges"]:
                if edge["relation"] != "prerequisite" or edge["to"] not in taught:
                    continue
                if (
                    sample.levels[result["levels"][edge["to"]]]
                    < sample.levels[edge["target_level"]]
                ):
                    continue
                assert edge["from"] in taught or edge["from"] in result["background"]
                if edge["from"] in taught:
                    assert positions[edge["from"]] < positions[edge["to"]]
                    assert (
                        sample.levels[result["levels"][edge["from"]]]
                        >= sample.levels[edge["source_level"]]
                    )


def test_sessions_partition_plan_without_duplicates(sample):
    for count in [1, 3, 7, 30]:
        plan = deepcopy(sample.plans["foundations"])
        plan["sessions"] = count
        result = build_plan(sample, plan)
        assert [n for s in result["sessions"] for n in s["nodes"]] == result["order"]
        assert len(result["order"]) == len(set(result["order"]))
        assert result["stats"]["unused_sessions"] + len(result["sessions"]) == count


def test_missing_timing_is_never_presented_as_fitting(sample):
    for node in sample.knowledge["nodes"]:
        node.pop("estimates", None)
    result = build_plan(sample, "foundations")
    assert result["stats"]["unestimated"] == len(result["order"])
    assert all(s["timing"] == "unestimated" for s in result["sessions"])


def test_overload_reported(sample):
    plan = deepcopy(sample.plans["foundations"])
    plan.update(sessions=1, minutes_per_session=5)
    assert any(i["code"] == "overloaded" for i in build_plan(sample, plan)["issues"])


def test_empty_project_and_plan_are_valid(blank):
    result = build_plan(blank, "course")
    assert result["order"] == []
    assert result["layout"]["nodes"] == []
    assert result["stats"]["unused_sessions"] == 12


def test_inherited_mastery_can_be_explicitly_downgraded(sample):
    plan = deepcopy(sample.plans["simulation-lab"])
    plan["background"]["sampling.confidence_interval"] = "recognize"
    result = build_plan(sample, plan)
    assert result["levels"]["sampling.confidence_interval"] == "use"


def test_unready_prior_course_is_a_visible_error(sample):
    sample.plans["foundations"]["status"] = "draft"
    result = build_plan(sample, "simulation-lab")
    assert any(i["code"] == "prior_plan" for i in result["issues"])


def test_unknown_background_removes_inherited_assumption(sample):
    plan = deepcopy(sample.plans["simulation-lab"])
    plan["unknown"] = ["sampling.confidence_interval"]
    result = build_plan(sample, plan)
    assert "sampling.confidence_interval" in result["order"]
    assert "sampling.confidence_interval" not in result["background"]


def test_lower_treatment_of_supporting_requirement_is_reported(sample):
    plan = minimal_plan(sample, "sampling.probability", "use")
    plan["treatments"] = {"sampling.fractions": "recognize"}
    result = build_plan(sample, plan)
    assert result["levels"]["sampling.fractions"] == "use"
    assert any(i["code"] == "required_depth" for i in result["issues"])


def test_prior_course_cycle_fails_before_planning(sample):
    plan = deepcopy(sample.plans["foundations"])
    plan["prior_plans"] = ["simulation-lab"]
    with pytest.raises(ProjectError, match="cycle"):
        sample.with_plan(plan)


def test_rebuild_is_path_and_clock_independent(sample, tmp_path):
    import shutil

    first = build_plan(sample, "foundations")
    copy = tmp_path / "another-location"
    shutil.copytree(sample.root, copy)
    second = build_plan(load_project(copy), "foundations")
    assert first == second
    assert markdown(sample, first) == markdown(load_project(copy), second)
    assert "compiled_at" not in json.dumps(first)


def test_reduction_preserves_reachability():
    edges = [("a", "b"), ("b", "c"), ("a", "c"), ("a", "d")]
    assert reduction("abcd", edges) == [("a", "b"), ("a", "d"), ("b", "c")]
    assert topological([], []) == []


def test_exports_include_evidence_and_no_private_paths(sample):
    result = build_plan(sample, "foundations")
    text = markdown(sample, result, notes=True)
    assert (
        "Reading:" in text and "Assessment" not in text
    )  # actual assessment wording is under outcomes
    assert str(sample.root) not in text
    assert "sampling-notes" not in text.split("Reading:")[1].split("\n")[0]
    assert mermaid(sample, result).startswith("flowchart LR")


def test_comparison_is_symmetric_in_shared_material(sample):
    a, b = build_plan(sample, "foundations"), build_plan(sample, "simulation-lab")
    assert compare_plans(a, b)["shared"] == compare_plans(b, a)["shared"]


def test_unknown_sources_and_duplicate_yaml_fail(sample):
    graph = deepcopy(sample.knowledge)
    graph["nodes"][0]["evidence"][0]["source"] = "missing"
    with pytest.raises(ProjectError, match="Unknown evidence"):
        validate_knowledge(sample.config, graph)
    path = sample.root / "bad.yaml"
    path.write_text("id: first\nid: second\n")
    with pytest.raises(ProjectError, match="Duplicate"):
        read_yaml(path)


def test_project_cannot_escape_root(sample):
    config = deepcopy(sample.config)
    config["knowledge"] = "../outside.yaml"
    write_yaml(sample.root / "project.yaml", config)
    with pytest.raises(ProjectError, match="inside"):
        load_project(sample.root)
