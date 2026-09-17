"""Prepare a compact record index and verify a reviewed concept inventory.

This is an organizational pass over existing graphs, not a textbook reread or
an equivalence/dependency inference. Compact evidence sections identify index
records as JSON: {"records": [1, 2]}. Public exports resolve them to graph IDs.
"""

import argparse
import json
from pathlib import Path

from syllabusgraph.io import write_json
from syllabusgraph.project import load_project

from syllabusgraph.inventory import (
    record_index, inventory, resolve_coverage, verify_inventory,
)

__all__ = ["record_index", "inventory", "resolve_coverage", "verify_inventory"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    make = sub.add_parser("index")
    make.add_argument("output", type=Path)
    make.add_argument("projects", type=Path, nargs="+")
    check = sub.add_parser("check")
    check.add_argument("manifest", type=Path)
    check.add_argument("proposal", type=Path)
    verify = sub.add_parser("verify")
    verify.add_argument("manifest", type=Path)
    verify.add_argument("inventory", type=Path)
    verify.add_argument("projects", type=Path, nargs="+")
    args = parser.parse_args()
    if args.command == "index":
        manifest, text = record_index([load_project(p) for p in args.projects])
        args.output.mkdir(parents=True, exist_ok=True)
        write_json(args.output / "index.json", manifest)
        (args.output / "records.txt").write_text(text, encoding="utf-8")
        print(f"Indexed {len(manifest['records'])} records on {len(text.split(chr(12)))} pages.")
    elif args.command == "check":
        result = inventory(json.loads(args.proposal.read_text()), json.loads(args.manifest.read_text()))
        print(f"Complete partition: {len(result['concepts'])} concepts.")
    else:
        result = verify_inventory(json.loads(args.inventory.read_text()),
                                  json.loads(args.manifest.read_text()),
                                  [load_project(p) for p in args.projects])
        print(json.dumps(result))


if __name__ == "__main__":
    main()
