"""Loopback-only course design UI; private source files are never served."""

from __future__ import annotations

from copy import deepcopy
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import secrets
import tempfile
from urllib.parse import parse_qs, urlparse

from .export import render
from .io import ProjectError, write_yaml
from .planner import build_plan
from .project import load_project, validate_shape
from .sources import MAX_SOURCE_BYTES, public_status, register
from .workflow import prepare, project_lock, status

ASSETS = Path(__file__).parent / "assets"
STATIC = {
    "/app.js": ("app.js", "text/javascript; charset=utf-8"),
    "/style.css": ("style.css", "text/css; charset=utf-8"),
    "/icon.svg": ("icon.svg", "image/svg+xml"),
}


class CourseServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, project_path: Path, port: int = 8766):
        self.project_path = project_path.resolve()
        load_project(self.project_path)
        self.token = secrets.token_urlsafe(32)
        super().__init__(("127.0.0.1", port), Handler)


class Handler(BaseHTTPRequestHandler):
    server: CourseServer

    def log_message(self, format, *args):
        # Avoid logging user-supplied topic searches or private request paths.
        return

    def respond(
        self, value, code=200, content_type="application/json; charset=utf-8", filename=None
    ):
        data = (
            json.dumps(value, ensure_ascii=False).encode()
            if isinstance(value, (dict, list))
            else value
        )
        if isinstance(data, str):
            data = data.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'",
        )
        if filename:
            self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
        self.end_headers()
        self.wfile.write(data)

    def _host_ok(self):
        host = self.headers.get("Host", "")
        return host in {
            f"127.0.0.1:{self.server.server_port}",
            f"localhost:{self.server.server_port}",
        }

    def do_GET(self):
        if not self._host_ok():
            return self.respond({"error": "Use the local address printed by the server."}, 403)
        url = urlparse(self.path)
        if url.path == "/":
            html = (
                (ASSETS / "index.html")
                .read_text(encoding="utf-8")
                .replace("__SESSION_TOKEN__", self.server.token)
            )
            return self.respond(html, content_type="text/html; charset=utf-8")
        if url.path in STATIC:
            filename, content_type = STATIC[url.path]
            return self.respond((ASSETS / filename).read_bytes(), content_type=content_type)
        if not url.path.startswith("/api/"):
            return self.respond({"error": "Not found."}, 404)
        try:
            project = load_project(self.server.project_path)
            query = parse_qs(url.query)
            if url.path == "/api/project":
                return self.respond(
                    {
                        "config": project.config,
                        "knowledge": project.knowledge,
                        "plans": project.plans,
                        "digest": project.content_digest,
                        "sources": public_status(project),
                        "workflow": status(project),
                    }
                )
            if url.path in {"/api/plan", "/api/export"}:
                plan_id = query.get("id", [next(iter(project.plans), "")])[0]
                result = build_plan(project, plan_id)
                if url.path == "/api/plan":
                    return self.respond(result)
                format = query.get("format", ["syllabus"])[0]
                if format not in {"syllabus", "notes", "json", "mermaid"}:
                    raise ProjectError("Unknown export format.")
                extension = {"json": "json", "mermaid": "mmd"}.get(format, "md")
                return self.respond(
                    render(project, result, format),
                    content_type="text/plain; charset=utf-8",
                    filename=f"{plan_id}-{format}.{extension}",
                )
            return self.respond({"error": "Not found."}, 404)
        except ProjectError as exc:
            self.respond({"error": str(exc)}, 400)
        except Exception:
            self.respond(
                {"error": "The project could not be read. Run syllabusgraph validate for details."},
                500,
            )

    def _authorized(self):
        origin = self.headers.get("Origin")
        allowed = {
            f"http://127.0.0.1:{self.server.server_port}",
            f"http://localhost:{self.server.server_port}",
        }
        return (
            self._host_ok()
            and self.headers.get("X-SyllabusGraph-Token") == self.server.token
            and (origin is None or origin in allowed)
        )

    def do_POST(self):
        if not self._authorized():
            return self.respond({"error": "Reload the local app before saving changes."}, 403)
        path = urlparse(self.path).path
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > MAX_SOURCE_BYTES:
                return self.respond({"error": "Request is empty or exceeds the import limit."}, 413)
            project = load_project(self.server.project_path)
            if path.startswith("/api/upload/"):
                source_id = path.removeprefix("/api/upload/")
                if source_id not in project.sources:
                    raise ProjectError("Choose a registered reference before uploading material.")
                suffix = Path(self.headers.get("X-Filename", "")).suffix.lower()
                if suffix not in {".pdf", ".txt", ".md"}:
                    raise ProjectError("Upload a PDF, TXT, or Markdown file.")
                offset = int(self.headers.get("X-Page-Offset", "0"))
                project.local.mkdir(parents=True, exist_ok=True)
                with tempfile.TemporaryDirectory(dir=project.local) as temporary:
                    target = Path(temporary) / ("upload" + suffix)
                    remaining = length
                    with target.open("wb") as out:
                        while remaining:
                            chunk = self.rfile.read(min(1024 * 1024, remaining))
                            if not chunk:
                                raise ProjectError("Upload ended before the declared length.")
                            out.write(chunk)
                            remaining -= len(chunk)
                    with project_lock(project):
                        entry = register(project, source_id, target, offset=offset)
                return self.respond(
                    {"source": source_id, "pages": entry["page_count"], "sha256": entry["sha256"]}
                )
            if length > 2_000_000:
                return self.respond({"error": "Course request exceeds 2 MB."}, 413)
            data = json.loads(self.rfile.read(length))
            if not isinstance(data, dict):
                raise ProjectError("Expected a JSON object.")
            if path == "/api/prepare":
                packet = prepare(
                    project,
                    data["unit"],
                    data["source"],
                    int(data["first"]),
                    int(data["last"]),
                    scope=data["scope"],
                    page_budget=data.get("page_budget", 80),
                )
                return self.respond(
                    {"unit": packet["unit"], "packet_digest": packet["packet_digest"]}
                )
            if path in {"/api/preview", "/api/save", "/api/export"}:
                plan = data.get("plan")
                if not isinstance(plan, dict):
                    raise ProjectError("Choose a course plan first.")
                modified = project.with_plan(plan)
                result = build_plan(modified, plan)
                if path == "/api/preview":
                    return self.respond(result)
                if path == "/api/export":
                    format = data.get("format", "syllabus")
                    if format not in {"syllabus", "notes", "json", "mermaid"}:
                        raise ProjectError("Unknown export format.")
                    return self.respond(
                        render(modified, result, format), content_type="text/plain; charset=utf-8"
                    )
                with project_lock(project):
                    current = load_project(project.root)
                    if data.get("expected_digest") != current.content_digest:
                        return self.respond(
                            {
                                "error": "Project changed elsewhere. Reload before saving this course."
                            },
                            409,
                        )
                    if plan["id"] not in current.plan_paths:
                        raise ProjectError(
                            "Create additional course plan files before editing them here."
                        )
                    write_yaml(current.plan_paths[plan["id"]], plan)
                return self.respond(
                    {"digest": load_project(project.root).content_digest, "result": result}
                )
            if path == "/api/source":
                source = data.get("source")
                validate_shape(source, "source")
                with project_lock(project):
                    current = load_project(project.root)
                    if source["id"] in current.sources:
                        raise ProjectError("This reference ID already exists.")
                    config = deepcopy(current.config)
                    config["sources"].append(source)
                    validate_shape(config, "project")
                    write_yaml(project.root / "project.yaml", config)
                return self.respond({"source": source["id"]})
            return self.respond({"error": "Not found."}, 404)
        except (ProjectError, ValueError, KeyError) as exc:
            self.respond({"error": str(exc)}, 400)
        except Exception:
            self.respond(
                {"error": "The change could not be saved. Check the local project files."}, 500
            )


def serve(project_path: Path, port: int = 8766, *, open_browser: bool = False):
    import webbrowser

    server = CourseServer(project_path, port)
    url = f"http://127.0.0.1:{server.server_port}"
    print(f"SyllabusGraph is ready at {url}", flush=True)
    print(
        "Your project and source material stay on this computer. Press Ctrl-C to stop.", flush=True
    )
    if open_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
