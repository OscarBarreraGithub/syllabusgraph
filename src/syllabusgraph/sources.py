"""Local source registration and page-addressable text extraction."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import shutil

from pypdf import PdfReader

from .io import ProjectError, digest, file_digest, within, write_json
from .project import Project

MAX_SOURCE_BYTES = 200 * 1024 * 1024


def bindings(project: Project) -> dict:
    path = project.local / "sources" / "index.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ProjectError("Cannot read local source registrations.") from exc


def extract_pages(path: Path) -> list[str]:
    if path.stat().st_size > MAX_SOURCE_BYTES:
        raise ProjectError("Source exceeds the 200 MB local import limit.")
    if path.suffix.lower() == ".pdf":
        try:
            reader = PdfReader(path)
            if reader.is_encrypted:
                raise ProjectError("Supply an unlocked PDF you can read locally.")
            pages = []
            for page in reader.pages:
                contents = page.get_contents()
                if contents and len(contents.get_data()) > 20_000_000:
                    raise ProjectError("A PDF page exceeds the extraction size limit.")
                pages.append(page.extract_text() or "")
            return pages
        except ProjectError:
            raise
        except Exception as exc:
            raise ProjectError(
                "PDF text extraction failed; try a text export of the source."
            ) from exc
    if path.suffix.lower() in {".txt", ".md"}:
        return path.read_text(encoding="utf-8").split("\f")
    raise ProjectError("Supported source files are PDF, UTF-8 TXT, and Markdown.")


def register(
    project: Project, source_id: str, path: Path, *, offset: int = 0, replace: bool = False
) -> dict:
    if source_id not in project.sources:
        raise ProjectError(f"Add source {source_id!r} to project.yaml before attaching a file.")
    path = path.resolve()
    if not path.is_file():
        raise ProjectError("The source file does not exist.")
    original_digest = file_digest(path)
    current = bindings(project)
    if source_id in current and not replace:
        if (
            current[source_id]["sha256"] == original_digest
            and current[source_id]["page_offset"] == offset
        ):
            return current[source_id]
        raise ProjectError(
            "This source already has a different local file or page mapping; use --replace explicitly."
        )
    pages = extract_pages(path)
    if not pages or not any(p.strip() for p in pages):
        raise ProjectError(
            "No extractable text. Apply OCR locally before importing a scanned source."
        )
    directory = project.local / "sources" / source_id
    directory.mkdir(parents=True, exist_ok=True)
    # Content-addressed files preserve old runs when a source is deliberately replaced.
    stem = original_digest.removeprefix("sha256:")
    destination = directory / (stem + path.suffix.lower())
    if path != destination:
        shutil.copyfile(path, destination)
    if file_digest(destination) != original_digest:
        raise ProjectError("The source changed during import. Retry with a stable file.")
    text_path = directory / (stem + ".pages.json")
    write_json(text_path, pages)
    entry = {
        "sha256": original_digest,
        "text_digest": digest(pages),
        "file": str(destination.relative_to(project.root)),
        "text": str(text_path.relative_to(project.root)),
        "page_count": len(pages),
        "page_offset": offset,
        "empty_pages": [i + 1 for i, p in enumerate(pages) if not p.strip()],
    }
    current[source_id] = entry
    write_json(project.local / "sources" / "index.json", current)
    return entry


def source_pages(project: Project, source_id: str) -> tuple[dict, list[str]]:
    entries = bindings(project)
    if source_id not in entries:
        source = project.sources.get(source_id, {})
        public_file = source.get("public_file")
        if public_file:
            register(project, source_id, within(project.root, public_file))
            entries = bindings(project)
        else:
            raise ProjectError(f"Source {source_id} has no local material yet.")
    entry = entries[source_id]
    original = within(project.root, entry["file"])
    if not original.is_file() or file_digest(original) != entry["sha256"]:
        raise ProjectError(
            f"Source {source_id} changed or is missing. Register its current file again."
        )
    pages = json.loads(within(project.root, entry["text"]).read_text(encoding="utf-8"))
    if digest(pages) != entry["text_digest"]:
        raise ProjectError(
            "Cached source text changed. Re-register the source with --replace to rebuild it."
        )
    return entry, pages


def public_status(project: Project) -> list[dict]:
    entries = bindings(project)
    result = []
    for source in project.config["sources"]:
        row = deepcopy(source)
        row.pop("public_file", None)
        local = entries.get(source["id"])
        row["local_status"] = (
            "registered"
            if local
            else "included"
            if source.get("public_file")
            else "awaiting_upload"
        )
        if local:
            row.update(
                {
                    "page_count": local["page_count"],
                    "sha256": local["sha256"],
                    "empty_page_count": len(local["empty_pages"]),
                }
            )
        result.append(row)
    return result
