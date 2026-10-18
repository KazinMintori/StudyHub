"""Export exercise input/output examples as data, without grading machinery."""
from pathlib import Path
import ast
import json

root = Path(__file__).resolve().parents[1]
tree = ast.parse((root / "scripts/verify-data-practice-regex.py").read_text(encoding="utf-8"))
records = []
for node in tree.body:
    if not isinstance(node, ast.With):
        continue
    assignment = next((item for item in node.body if isinstance(item, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "CASES" for t in item.targets)), None)
    if assignment is None:
        continue
    cases = ast.literal_eval(assignment.value)
    passage = next(item for item in node.body if isinstance(item, ast.Assign)
                   and any(isinstance(t, ast.Name) and t.id == "PASSAGE" for t in item.targets))
    selected = next(item for item in node.body if isinstance(item, ast.Assert)
                    and isinstance(item.test, ast.Compare)
                    and isinstance(item.test.left, ast.Name) and item.test.left.id == "selected")
    records.append({"exercise": len(records) + 1, "cases": [{"input": source, "expected": expected, "expectedType": type(expected).__name__} for source, expected in cases],
                    "passage": ast.literal_eval(passage.value),
                    "selected": ast.literal_eval(selected.test.comparators[0])})
assert len(records) == 20
payload = {
    "description": "Dữ liệu đầu vào và đầu ra để đối chiếu 20 bài regex. Không chứa lời giải mẫu hoặc công cụ chấm bài.",
    "source": "https://github.com/uet-iai-course/programming-for-data-processing/blob/main/2627-1/notebooks/lab-07-regex.ipynb",
    "license": "CC BY-NC-SA 4.0",
    "exercises": records,
}
target = root / "docs/public/materials/data-labs/regex-cases.json"
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Exported {len(records)} exercises and {sum(len(x['cases']) for x in records)} input/output pairs.")
