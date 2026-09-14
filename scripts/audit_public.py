"""Screen public files, Git objects, and distributions without printing matched secrets."""

import argparse
from pathlib import Path
import re
import subprocess
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {
    ".git",
    ".venv",
    ".syllabusgraph",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "node_modules",
    "dist",
    "build",
}
FORBIDDEN = {".syllabusgraph", "materials", ".env", ".claude", ".wrangler", "__pycache__", ".venv"}
BINARY_SOURCE = {".pdf", ".epub", ".docx", ".pptx", ".pem", ".key"}
RULES = [
    ("private absolute path", re.compile(r"/(?:Users|home)/[A-Za-z][A-Za-z0-9_.-]+/")),
    ("access token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|sk-[A-Za-z0-9_-]{32,})\b")),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
]
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--deny-pattern", action="append", default=[])
    parser.add_argument("--fresh-history", action="store_true")
    args = parser.parse_args()
    rules = RULES + [
        (f"custom rule {i + 1}", re.compile(p, re.I)) for i, p in enumerate(args.deny_pattern)
    ]
    findings, checked = [], 0

    def scan(name, raw, check_path=True):
        nonlocal checked
        checked += 1
        if check_path:
            path = Path(name)
            if FORBIDDEN & set(path.parts) or path.suffix.lower() in BINARY_SOURCE:
                findings.append((name, "private/runtime file or source binary"))
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            return
        for label, pattern in rules:
            if pattern.search(text):
                findings.append((name, label))
        for address in EMAIL.findall(text):
            if not address.endswith("@users.noreply.github.com") and not address.endswith(
                "@example.com"
            ):
                findings.append((name, "non-public contact identifier"))

    if (ROOT / ".git").exists():
        names = git("ls-files", "-z").decode().split("\0")
        if args.fresh_history:
            roots = git("rev-list", "--max-parents=0", "--all").decode().splitlines()
            if len(roots) != 1:
                findings.append(("Git history", "expected exactly one independent root commit"))
        objects = (
            git("cat-file", "--batch-all-objects", "--batch-check=%(objectname) %(objecttype)")
            .decode()
            .splitlines()
        )
        for row in objects:
            oid, kind = row.split()
            if kind in {"blob", "commit", "tag"}:
                scan("Git object " + oid[:12], git("cat-file", kind, oid), check_path=False)
    else:
        names = []
    if not any(names):
        names = [
            str(p.relative_to(ROOT))
            for p in ROOT.rglob("*")
            if p.is_file() and not (set(p.relative_to(ROOT).parts) & IGNORED)
        ]
    for name in filter(None, names):
        scan(name, (ROOT / name).read_bytes())
    for archive in (ROOT / "dist").glob("*"):
        if archive.suffix == ".whl":
            with zipfile.ZipFile(archive) as handle:
                for name in handle.namelist():
                    if not name.endswith("/"):
                        scan(archive.name + ":" + name, handle.read(name))
        elif archive.name.endswith(".tar.gz"):
            with tarfile.open(archive) as handle:
                for member in handle.getmembers():
                    if member.issym() or member.islnk():
                        findings.append(
                            (archive.name + ":" + member.name, "archive link needs review")
                        )
                    elif member.isfile():
                        scan(archive.name + ":" + member.name, handle.extractfile(member).read())
    for name, reason in findings:
        print(f"FAIL {name}: {reason}")
    print(f"Inspected {checked} files/objects/archive entries; {len(findings)} findings.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
