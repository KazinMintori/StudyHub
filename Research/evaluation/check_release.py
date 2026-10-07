"""Validate the two skill packs and save exact command outcomes for review."""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent / "revised"
VALIDATOR = Path("C:/Users/Ai/.codex/skills/.system/skill-creator/scripts/quick_validate.py")


def run(command, env=None):
    done = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", env=env)
    return {"command": command, "exit_code": done.returncode,
            "stdout": done.stdout, "stderr": done.stderr}


def main():
    env = os.environ.copy()
    # Isolated validation dependency; the distributed skill scripts use only stdlib.
    env["PYTHONPATH"] = str(HERE / ".validation-deps")
    results = [run([sys.executable, "-X", "utf8", str(HERE / "verify_tools.py")])]
    for skill in sorted(ROOT.iterdir()):
        results.append(run([sys.executable, "-X", "utf8", str(VALIDATOR), str(skill)], env))
        result = run([sys.executable, "-X", "utf8", str(skill / "scripts/build_teaching_prompt.py"),
                      str(skill / "references/prompt-input.example.json"), "--output",
                      str(HERE / ("compiled-note-prompt.txt" if skill.name == "textbook-passage-explainer" else "compiled-slide-prompt.txt"))])
        results.append(result)
    slides = ROOT / "textbook-to-course-slides"
    results.append(run([sys.executable, "-X", "utf8", str(slides / "scripts/audit_spec.py"),
                        str(slides / "references/sample-course-spec.json"), "--asset-root", str(slides)]))
    report = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "scope": "Tool execution, packaging references and declared structure; no certification of learning outcomes or visual layout.",
              "results": results}
    (HERE / "tool-validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"commands": len(results), "failed": sum(item["exit_code"] != 0 for item in results)}, indent=2))
    return int(any(item["exit_code"] != 0 for item in results))


if __name__ == "__main__":
    raise SystemExit(main())
