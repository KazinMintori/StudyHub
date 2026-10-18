"""Check Antigravity ownership, then optionally copy one verified lab to main."""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import re
import shutil
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("worktree", choices=list("abc"))
parser.add_argument("labs", nargs="+")
parser.add_argument("--allow-prior", nargs="*", default=[])
parser.add_argument("--copy", action="store_true")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
worktree = Path(f"C:/Users/Ai/.codex/worktrees/data-course-20261018-{args.worktree}")
baseline = json.loads((root / f"qa/data-labs/agy-baseline-{args.worktree}.json").read_text(encoding="utf-8"))
for name, record in baseline.items():
    file = worktree / name
    actual = hashlib.sha256(file.read_bytes()).hexdigest() if file.is_file() else None
    assert actual == record["sha256"], f"Baseline file changed: {name}"

allowed_labs = set(args.labs + args.allow_prior)
status = subprocess.check_output(["git", "status", "--porcelain=v1", "--untracked-files=all", "-z"], cwd=worktree).decode()
for entry in filter(None, status.split("\0")):
    path = entry[3:]
    if path in baseline:
        continue
    assert any(
        re.fullmatch(rf"raw_materials/xu-ly-du-lieu/labs/(?:lab-{lab}[^/]*\.md|coverage-{lab}\.json)", path)
        or path == f"scripts/verify-data-lab-{lab}.py"
        or path.startswith(f"docs/xu-ly-du-lieu/bai-giang/img/labs/lab-{lab}/")
        for lab in allowed_labs
    ), f"Outside ownership: {path}"

records = []
for lab in args.labs:
    files = sorted(worktree.glob(f"raw_materials/xu-ly-du-lieu/labs/lab-{lab}*.md"))
    assert files, f"Missing Markdown: {lab}"
    for file in files:
        text = file.read_text(encoding="utf-8")
        assert not re.search(r"public_check|check_public|PUBLIC_RESULTS|LTXLDL|Khai báo (?:sử dụng )?AI|Hạn nộp|grader", text, re.I), file
        exercises = len(re.findall(r"^::: exercise(?: |$)", text, re.M))
        solutions = len(re.findall(r"^::: solution(?: |$)", text, re.M))
        assert exercises == solutions and exercises > 0, (file, exercises, solutions)
        for way in [1, 2]:
            assert len(re.findall(rf"^#{{3,5}}\s+Cách {way}\b", text, re.M)) >= exercises, (file, way)
        blocks = re.findall(r"^```python[^\n]*\n(.*?)^```\s*$", text, re.M | re.S)
        for index, code in enumerate(blocks):
            ast.parse(code, filename=f"{file.name} block {index + 1}")
        records.append({"file": file.relative_to(worktree).as_posix(), "exercises": exercises, "pythonBlocks": len(blocks)})
    coverage = worktree / f"raw_materials/xu-ly-du-lieu/labs/coverage-{lab}.json"
    json.loads(coverage.read_text(encoding="utf-8"))
    verifier = worktree / f"scripts/verify-data-lab-{lab}.py"
    assert verifier.is_file(), verifier

if args.copy:
    for lab in args.labs:
        files = list(worktree.glob(f"raw_materials/xu-ly-du-lieu/labs/lab-{lab}*.md"))
        files += [worktree / f"raw_materials/xu-ly-du-lieu/labs/coverage-{lab}.json", worktree / f"scripts/verify-data-lab-{lab}.py"]
        files += [p for p in worktree.glob(f"docs/xu-ly-du-lieu/bai-giang/img/labs/lab-{lab}/**/*") if p.is_file()]
        for source in files:
            target = root / source.relative_to(worktree)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
print(json.dumps({"worktree": args.worktree, "copied": args.copy, "records": records}, ensure_ascii=False, indent=2))
