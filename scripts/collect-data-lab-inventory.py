"""Record source identity and section locations without publishing raw notebooks."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("source_root", type=Path)
args = parser.parse_args()
entries = []
for source, folder, repo, prefix in [
    ("template", args.source_root / "template", "uet-iai-notebook-labs-2026/notebook-labs-template", ""),
    ("course", args.source_root / "course" / "2627-1" / "notebooks", "uet-iai-course/programming-for-data-processing", "2627-1/notebooks/"),
]:
    git_root = args.source_root / ("template" if source == "template" else "course")
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=git_root, text=True).strip()
    for file in sorted(folder.glob("lab-*.ipynb")):
        raw = file.read_bytes()
        notebook = json.loads(raw)
        sections = []
        for index, cell in enumerate(notebook["cells"]):
            text = "".join(cell.get("source", []))
            if cell["cell_type"] != "markdown":
                continue
            for heading in re.findall(r"^#{2,3}\s+(.+)", text, re.M):
                if re.search(r"Khai báo|Thông tin và nộp|Trước khi nộp|Rubric|Cách làm|Hỗ trợ bài tập lớn|Tóm tắt bài|Hợp đồng hàm|Nguồn học tập|Lộ trình|Mã khởi đầu|Bộ test", heading, re.I):
                    continue
                cleaned = re.sub(r"\s*[—–]\s*(?:\d+ điểm|không cộng|cùng khai báo).*", "", heading)
                cleaned = re.sub(r"\s*✅ mở.*", "", cleaned)
                cleaned = re.sub(r"\s*\(?~?\d+ phút\)?", "", cleaned)
                sections.append({"cell": index, "heading": cleaned})
        entries.append({
            "source": source,
            "notebook": file.name,
            "url": f"https://github.com/{repo}/blob/{commit}/{prefix}{file.name}",
            "commit": commit,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "cells": len(notebook["cells"]),
            "technicalSections": sections,
        })

payload = {
    "schemaVersion": 1,
    "sourcePolicy": "Only technical exercises, input/output requirements and data. Administrative cells and grading infrastructure are excluded.",
    "sources": entries,
}
out = Path("raw_materials/xu-ly-du-lieu/lab-source-inventory.json")
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"notebooks": len(entries), "template": sum(e["source"] == "template" for e in entries), "course": sum(e["source"] == "course" for e in entries)}, ensure_ascii=False))
