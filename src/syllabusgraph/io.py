"""Strict input loading, stable identities, and atomic project writes."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import tempfile
from typing import Any

import yaml


class ProjectError(ValueError):
    """A user-actionable project or workflow error."""


class UniqueLoader(yaml.SafeLoader):
    pass


def _mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ProjectError("Mapping keys must be strings.")
        if key in result:
            raise ProjectError(f"Duplicate mapping key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def read_yaml(path: Path) -> Any:
    try:
        if path.stat().st_size > 20_000_000:
            raise ProjectError(f"Input exceeds the 20 MB project-data limit: {path.name}")
        result = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueLoader)
        # Reject cyclic YAML aliases and values that cannot be serialized as JSON.
        json.dumps(result, allow_nan=False)
        return result
    except (OSError, yaml.YAMLError, TypeError, ValueError, RecursionError) as exc:
        raise ProjectError(f"Cannot read {path.name}: {exc}") from exc


def canonical(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")


def digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical(value)).hexdigest()


def file_digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def within(root: Path, relative: str) -> Path:
    candidate = Path(relative)
    if candidate.is_absolute():
        raise ProjectError("Project paths must be relative.")
    resolved = (root / candidate).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ProjectError("Project paths must stay inside the project directory.")
    return resolved


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".write-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_json(path: Path, value: Any) -> None:
    write_text(path, json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n")


def write_yaml(path: Path, value: Any) -> None:
    write_text(path, yaml.safe_dump(value, sort_keys=False, allow_unicode=True))


def bundled(directory: str) -> Path:
    installed = Path(__file__).parent / directory
    if installed.is_dir():
        return installed
    checkout = Path(__file__).resolve().parents[2] / directory
    if checkout.is_dir():
        return checkout
    raise ProjectError(f"Missing installed resource directory: {directory}")
