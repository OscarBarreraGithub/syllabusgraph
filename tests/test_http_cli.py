from contextlib import contextmanager
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import threading
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest

from syllabusgraph.project import load_project
from syllabusgraph.server import CourseServer


@contextmanager
def serving(project):
    server = CourseServer(project.root, 0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server, f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def request(base, path, data=None, headers=None):
    req = Request(
        base + path,
        data=json.dumps(data).encode() if data is not None else None,
        headers={"Content-Type": "application/json", **(headers or {})},
    )
    try:
        return urlopen(req, timeout=5)
    except HTTPError as error:
        error.close()
        raise


def test_api_roundtrip_draft_export_and_stale_write(sample):
    with serving(sample) as (server, base):
        with request(base, "/api/project") as response:
            payload = json.load(response)
        plan = deepcopy(payload["plans"]["foundations"])
        plan["sessions"] = 2
        headers = {"X-SyllabusGraph-Token": server.token, "Origin": base}
        with request(base, "/api/preview", {"plan": plan}, headers) as response:
            preview = json.load(response)
        assert len(preview["sessions"]) == 2
        with request(
            base, "/api/export", {"plan": plan, "format": "syllabus"}, headers
        ) as response:
            text = response.read().decode()
        assert "Schedule: 2 sessions" in text
        assert load_project(sample.root).plans["foundations"]["sessions"] == 4
        with request(
            base, "/api/save", {"plan": plan, "expected_digest": payload["digest"]}, headers
        ) as response:
            saved = json.load(response)
        assert saved["digest"] != payload["digest"]
        assert load_project(sample.root).plans["foundations"]["sessions"] == 2
        with pytest.raises(HTTPError) as exc:
            request(
                base, "/api/save", {"plan": plan, "expected_digest": payload["digest"]}, headers
            )
        assert exc.value.code == 409


@pytest.mark.parametrize(
    "path",
    [
        "/project.yaml",
        "/sources/primer.txt",
        "/.syllabusgraph/sources/index.json",
        "/../project.yaml",
        "/.git/config",
    ],
)
def test_arbitrary_files_are_not_served(sample, path):
    with serving(sample) as (_, base):
        with pytest.raises(HTTPError) as exc:
            request(base, path)
        assert exc.value.code == 404


def test_write_token_origin_and_host_are_enforced(sample):
    with serving(sample) as (server, base):
        body = {"plan": sample.plans["foundations"]}
        for headers in [
            {},
            {"X-SyllabusGraph-Token": server.token, "Origin": "https://example.invalid"},
            {"X-SyllabusGraph-Token": server.token, "Host": "example.invalid"},
        ]:
            with pytest.raises(HTTPError) as exc:
                request(base, "/api/preview", body, headers)
            assert exc.value.code == 403


def test_index_has_local_assets_and_no_remote_requests(sample):
    with serving(sample) as (server, base):
        with request(base, "/") as response:
            html = response.read().decode()
            assert server.token in html
            assert "frame-ancestors 'none'" in response.headers["Content-Security-Policy"]
        for path in ["/app.js", "/style.css", "/icon.svg"]:
            with request(base, path) as response:
                assert response.status == 200
        assert '<script src="http' not in html


def test_cli_blank_init_and_sample_rebuild(tmp_path):
    def cli(*args):
        return subprocess.run(
            [sys.executable, "-m", "syllabusgraph", *map(str, args)],
            text=True,
            capture_output=True,
            check=False,
        )

    sample = tmp_path / "sample"
    assert cli("init", sample, "--template", "sampling").returncode == 0
    assert cli("validate", "-p", sample).returncode == 0
    assert cli("build", "-p", sample, "--strict").returncode == 0
    output = sample / ".syllabusgraph/build"
    first = {p.name: p.read_bytes() for p in output.iterdir()}
    assert cli("build", "-p", sample, "--strict").returncode == 0
    assert first == {p.name: p.read_bytes() for p in output.iterdir()}
    blank = tmp_path / "empty"
    assert cli("init", blank, "--title", "A different subject").returncode == 0
    assert cli("build", "-p", blank).returncode == 0
    assert cli("init", blank).returncode == 2
    from syllabusgraph.io import write_yaml

    next_plan = deepcopy(load_project(blank).plans["course"])
    next_plan.update(id="next-course", title="Next course", prior_plans=["course"])
    write_yaml(blank / "plans/next-course.yaml", next_plan)
    assert cli("validate", "-p", blank).returncode == 0
    assert cli("plan", "-p", blank, "--plan", "next-course", "--strict").returncode == 2


def test_notation_and_non_json_input_rejected(sample):
    from syllabusgraph.io import ProjectError, read_yaml

    target = Path(sample.root / "invalid.yaml")
    target.write_text("number: .nan\n")
    with pytest.raises(ProjectError):
        read_yaml(target)
