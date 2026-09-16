"""Export only public graph records into a portable, read-only website."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import re
import shutil
import webbrowser

from .io import ProjectError, read_yaml, write_json
from .project import load_project
from .navigation import reading_views, chapter_index
from .backbone import shared_backbone

ASSETS = Path(__file__).parent / "explorer"


def build_site(projects, destination: Path):
    """Explicit project allowlist; never copy project directories or local storage."""
    destination = destination.resolve()
    manifest = {"version": 1, "graphs": []}
    payloads = []
    chapter_indexes = {}
    for entry in projects:
        project = load_project(Path(entry["path"]))
        slug = entry.get("id", project.config["id"])
        if not re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_-]*", slug):
            raise ProjectError("Site graph IDs must be simple URL-safe identifiers.")
        if any(row["id"] == slug for row in manifest["graphs"]):
            raise ProjectError("Duplicate site graph ID.")
        if destination == project.root or project.root.is_relative_to(destination):
            raise ProjectError("Site output must not contain an input project.")
        review_path = project.root / "review.yaml"
        review = read_yaml(review_path) if review_path.exists() else {}
        review = {key: review[key] for key in ("status", "human_audit") if key in review}
        # Deliberately omit local workflow, paths, source status, packets and project description.
        payload = {
            "id": slug,
            "project_id": project.config["id"],
            "title": entry.get("title", project.config["title"]),
            "digest": project.content_digest,
            "knowledge": project.knowledge,
            "sources": [
                {k: s[k] for k in ("id", "title", "authors", "edition", "volume") if k in s}
                for s in project.config["sources"]
            ],
            "review": review,
        }
        coverage_path = project.root / "coverage.yaml"
        if coverage_path.exists():
            chapter_indexes[project.config["id"]] = chapter_index(read_yaml(coverage_path))
        comparison_group = entry.get("comparison_group")
        if comparison_group is not None:
            if not isinstance(comparison_group, dict) or any(
                not isinstance(comparison_group.get(key), str) or not comparison_group[key].strip()
                for key in ("id", "title")
            ):
                raise ProjectError("A comparison_group needs nonempty id and title strings.")
            comparison_group = {key: comparison_group[key] for key in ("id", "title")}
        payloads.append((slug, payload))
        manifest["graphs"].append(
            {
                "id": slug,
                "project_id": payload["project_id"],
                "title": payload["title"],
                "kind": entry.get("kind", "graph"),
                **({"comparison_group": comparison_group} if comparison_group else {}),
                "nodes": len(project.nodes),
                "edges": len(project.knowledge["edges"]),
                "review": review,
                "file": f"data/{slug}.json",
            }
        )
    # Imported textbook nodes are dependencies, not an independent treatment.
    # Match the graph-bank overlap definition without changing scientific records.
    projects_by_id = {payload["project_id"]: payload for _, payload in payloads}
    kinds = {e["id"]: e["kind"] for e in manifest["graphs"]}
    textbook_payloads = [p for slug, p in payloads if kinds[slug] == "textbook"]
    for slug, payload in payloads:
        direct = {}
        for node in payload["knowledge"]["nodes"]:
            books = set()
            for origin in node.get("origins", []):
                target = projects_by_id.get(origin["project"])
                if target:
                    original = next(
                        (n for n in target["knowledge"]["nodes"] if n["id"] == origin["node"]), None
                    )
                    if original and not original.get("origins"):
                        books.add(origin["project"])
            direct[node["id"]] = sorted(books)
        payload["direct_books"] = direct
        if kinds[slug] == "shared":
            payload["backbone"] = shared_backbone(
                payload["knowledge"],
                direct,
                [e for e in manifest["graphs"] if e["kind"] == "textbook"],
            )
        payload["reading_views"] = reading_views(
            payload, textbook_payloads if kinds[slug] == "shared" else [payload], chapter_indexes
        )
    if not payloads:
        raise ProjectError("Choose at least one graph for the site.")
    # A reused output directory must contain only our generated allowlist. Fail closed
    # instead of accidentally uploading unrelated files or deleting someone's work.
    expected = {"catalog.json", "data", *[p.name for p in ASSETS.iterdir() if p.is_file()]}
    if destination.exists():
        unexpected = [p.name for p in destination.iterdir() if p.name not in expected]
        data_dir = destination / "data"
        if data_dir.exists():
            unexpected += [
                str(p)
                for p in data_dir.iterdir()
                if not p.is_file() or p.suffix != ".json" or p.is_symlink()
            ]
        if unexpected or any(p.is_symlink() for p in destination.iterdir()):
            raise ProjectError("Site output contains unexpected files; choose a fresh directory.")
        if data_dir.exists():
            shutil.rmtree(data_dir)
    destination.mkdir(parents=True, exist_ok=True)
    for asset in ASSETS.iterdir():
        if asset.is_file():
            shutil.copyfile(asset, destination / asset.name)
    for slug, payload in payloads:
        # Compact JSON reduces download size; citations remain intact.
        (destination / "data").mkdir(exist_ok=True)
        (destination / "data" / f"{slug}.json").write_text(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
        )
    write_json(destination / "catalog.json", manifest)
    return manifest


def build_catalog(catalog: Path, destination: Path):
    entries = json.loads(catalog.read_text(encoding="utf-8"))["graphs"]
    return build_site([{**e, "path": catalog.parent / e["path"]} for e in entries], destination)


class SiteHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        # Only generated assets and graph JSON are served; no directory listings.
        name = self.path.split("?", 1)[0].lstrip("/") or "index.html"
        allowed = {p.name for p in ASSETS.iterdir() if p.is_file()} | {"catalog.json"}
        if name not in allowed and not re.fullmatch(r"data/[a-zA-Z][a-zA-Z0-9_-]*\.json", name):
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        self.send_error(405)

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        # Local rebuilds can happen within HTTP Last-Modified’s one-second resolution.
        self.send_header("Cache-Control", "no-store")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'",
        )
        super().end_headers()


def serve_site(directory: Path, port=8767, *, open_browser=False):
    server = ThreadingHTTPServer(("127.0.0.1", port), partial(SiteHandler, directory=directory))
    url = f"http://127.0.0.1:{server.server_port}"
    print(f"SyllabusGraph explorer: {url}", flush=True)
    if open_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
