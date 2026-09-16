// Prefer the Python environment prepared by SETUP.md, on Windows or Unix.
import { existsSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import path from "node:path";
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const local = path.join(
  root,
  ".venv",
  process.platform === "win32" ? "Scripts/python.exe" : "bin/python",
);
const python = existsSync(local)
  ? local
  : process.platform === "win32"
    ? "python"
    : "python3";
const result = spawnSync(python, ["-m", "syllabusgraph", "site", "build"], {
  cwd: root,
  stdio: "inherit",
});
if (result.error)
  console.error("Run the agent setup in SETUP.md to prepare Python first.");
process.exit(result.status ?? 1);
