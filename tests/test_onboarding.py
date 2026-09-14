import subprocess

import pytest

from syllabusgraph import cli


@pytest.mark.parametrize("template", ["blank", "sampling"])
def test_every_project_has_guides_and_ignores_all_materials(tmp_path, template):
    project = cli.initialize(tmp_path / "course", template)
    assert (project.root / "README.md").is_file()
    assert (project.root / "materials/README.md").is_file()
    assert (project.root / "COURSE_GUIDANCE.md").is_file()
    agent_guide = (project.root / "AGENTS.md").read_text()
    assert "--provider codex" in agent_guide and "--provider claude" in agent_guide
    assert (project.root / "CLAUDE.md").read_text() == "@AGENTS.md\n"
    files = [
        "materials/handout.txt",
        "materials/chapter.md",
        "materials/book.pdf",
        "materials/nested/data.json",
        ".syllabusgraph/run.json",
        "COURSE_GUIDANCE.md",
        "CLAUDE.local.md",
        ".claude/settings.local.json",
    ]
    for name in files:
        path = project.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("Local input fixture.", encoding="utf-8")
    # Use a separate Git root so the tool repository's own rules cannot mask a gap.
    subprocess.run(["git", "init", "--quiet", "--template="], cwd=project.root, check=True)
    result = subprocess.run(
        ["git", "check-ignore", "--no-index", "-z", "--stdin"],
        input="\0".join(files) + "\0",
        cwd=project.root,
        text=True,
        capture_output=True,
        check=True,
    )
    assert set(result.stdout.rstrip("\0").split("\0")) == set(files)
    public = subprocess.run(
        ["git", "check-ignore", "project.yaml", "knowledge/graph.yaml"],
        cwd=project.root,
        capture_output=True,
        check=False,
    )
    assert public.returncode == 1


def test_guides_preserve_existing_instructions_and_materials(blank):
    guide = blank.root / "README.md"
    guide.write_text("Existing course instructions.\n", encoding="utf-8")
    material = blank.root / "materials/notes.md"
    material.write_text("Existing local source.\n", encoding="utf-8")
    brief = blank.root / "COURSE_GUIDANCE.md"
    brief.write_text("Existing course decisions.\n", encoding="utf-8")
    agent_guide = blank.root / "AGENTS.md"
    agent_guide.write_text("Existing agent instructions.\n", encoding="utf-8")
    ignore = blank.root / ".gitignore"
    ignore.write_text("custom-private/\n", encoding="utf-8")
    cli.create_workspace_guides(blank.root)
    first = ignore.read_text(encoding="utf-8")
    cli.create_workspace_guides(blank.root)
    assert ignore.read_text(encoding="utf-8") == first
    assert "custom-private/\n" in first
    assert "materials/\n" in first
    assert guide.read_text(encoding="utf-8") == "Existing course instructions.\n"
    assert material.read_text(encoding="utf-8") == "Existing local source.\n"
    assert brief.read_text(encoding="utf-8") == "Existing course decisions.\n"
    assert agent_guide.read_text(encoding="utf-8") == "Existing agent instructions.\n"


def test_template_local_material_is_not_copied_into_new_courses(tmp_path, monkeypatch):
    original_bundled = cli.bundled
    templates = tmp_path / "templates"
    cli.initialize(templates / "new-course", "blank")
    private = templates / "new-course/materials/private-notes.md"
    private.write_text("This local source must not become template content.", encoding="utf-8")
    brief = templates / "new-course/COURSE_GUIDANCE.md"
    brief.write_text("Private decisions from an earlier course.", encoding="utf-8")

    def bundled(directory):
        return templates if directory == "templates" else original_bundled(directory)

    monkeypatch.setattr(cli, "bundled", bundled)
    project = cli.initialize(tmp_path / "new-project", "blank")
    assert not (project.root / "materials/private-notes.md").exists()
    assert (project.root / "materials/README.md").is_file()
    assert "Private decisions" not in (project.root / "COURSE_GUIDANCE.md").read_text(
        encoding="utf-8"
    )
    assert project.config["sources"] == []
    assert not project.nodes
