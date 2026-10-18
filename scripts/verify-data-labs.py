"""Validate authored lab coverage/markup and run every numerical verifier."""
from pathlib import Path
import argparse
import ast
import builtins
import json
import os
import re
import subprocess
import sys
import symtable
import unicodedata


def normalized_label(text):
    text = unicodedata.normalize("NFD", text.casefold()).replace("đ", "d")
    return re.sub(r"[*_`]+", "", "".join(c for c in text if unicodedata.category(c) != "Mn")).strip()


def method_number(label):
    """Recognize the role of a heading, not one mandatory heading string."""
    label = normalized_label(label)
    label = re.sub(r"^\d+[.)]\s*", "", label)
    match = re.match(r"(?:cach(?: giai)?|phuong phap|huong(?: giai)?|method)\s+(?:thu\s+)?(1|2|mot|hai|nhat|nhi|first|second)\b", label)
    if match:
        return 1 if match.group(1) in {"1", "mot", "nhat", "first"} else 2
    return None


def unresolved_globals(code):
    table = symtable.symtable(code, "<method>", "exec")
    def references(scope):
        result = {symbol.get_name() for symbol in scope.get_symbols()
                  if symbol.is_global() and symbol.is_referenced()}
        for child in scope.get_children():
            result.update(references(child))
        return result
    defined = {symbol.get_name() for symbol in table.get_symbols()
               if symbol.is_assigned() or symbol.is_imported() or symbol.is_namespace()}
    return references(table) - defined - set(dir(builtins)) - {"__name__", "__file__"}


def markdown_events(text):
    """Small fence-aware reader. Code cannot masquerade as headings/containers."""
    lines = text.splitlines()
    events = []
    index = 0
    while index < len(lines):
        line = lines[index]
        opening = re.match(r"^\s{0,3}(`{3,}|~{3,})([^\r\n]*)$", line)
        if opening:
            delimiter, language = opening.groups()
            start = index
            index += 1
            content = []
            while index < len(lines):
                if re.match(r"^\s{0,3}" + re.escape(delimiter[0]) + "{" + str(len(delimiter)) + r",}\s*$", lines[index]):
                    break
                content.append(lines[index])
                index += 1
            events.append({"kind": "fence", "line": start + 1, "end": index + 1,
                           "language": language.strip().split()[0] if language.strip() else "",
                           "text": "\n".join(content), "closed": index < len(lines)})
            index += 1
            continue
        span = re.search(r'<span\s+id=[\"\'](data-lab-[^\"\']+)[\"\']', line)
        if span:
            events.append({"kind": "span", "line": index + 1, "text": span.group(1)})
        container = re.match(r"^\s*(:{3,})(?:\s+([\w-]+)(?:\s+.*)?)?\s*$", line)
        heading = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if container:
            events.append({"kind": "open" if container.group(2) else "close", "line": index + 1, "text": container.group(2) or ""})
        elif heading:
            events.append({"kind": "heading", "line": index + 1, "text": heading.group(1)})
        elif line.strip():
            events.append({"kind": "text", "line": index + 1, "text": line})
        index += 1
    return events


def output_marker(event):
    if event["kind"] not in {"heading", "text"}:
        return False
    label = normalized_label(event["text"])
    label = re.sub(r"^\s*[-*>]+\s*", "", label)
    # Labels may be headings, bold labels, or a short introductory sentence.
    return bool(re.match(r"(?:ket qua|dau ra|output|stdout|ban in|hinh ket qua)\b", label))


def output_payload(events):
    """Require actual material: A populated table, text block, image or scalar."""
    for index, event in enumerate(events):
        if event["kind"] == "fence" and event["language"].casefold() not in {"python", "py"} and event["text"].strip():
            return True
        if event["kind"] != "text":
            continue
        value = event["text"].strip()
        if re.search(r"!\[[^\]]*\]\([^\n]+\)|<img\b|<figure\b|<svg\b", value, re.I):
            return True
        if "|" in value and index + 2 < len(events):
            separator = events[index + 1]
            row = events[index + 2]
            if (separator["kind"] == "text" and row["kind"] == "text"
                    and re.match(r"^\s*\|?\s*:?-{3,}", separator["text"])
                    and "|" in row["text"] and re.search(r"[\w`$]", row["text"])):
                return True
        # Plain scalar results can be a stand-alone number/boolean or a sentence
        # with an explicit result label; prose mentioning a number is insufficient.
        label = normalized_label(value)
        bare = re.sub(r"^[>*\s]+|[.*\s]+$", "", value).strip("`")
        if re.fullmatch(r"(?:[-+]?\d[\d.,% eE+-]*|True|False|None|NaN|NaT|null)", bare):
            return True
        if (output_marker(event) or re.match(r"^(?:in ra|tra ve|nhan duoc|thu duoc)\b", label)) and re.search(r"`[^`]+`|\b\d+(?:[.,]\d+)?\b|\b(?:True|False|None|NaN|NaT)\b", value):
            # Ignore an output label that merely says "Cách 1" or "Cách 2".
            meaningful = re.sub(r"\b(?:cach|method)\s+[12]\b", "", label)
            if re.search(r"`[^`]+`|\b\d+(?:[.,]\d+)?\b|\b(?:true|false|none|nan|nat)\b", meaningful):
                return True
    return False


def explanation_present(events):
    prose = []
    for event in events:
        if event["kind"] != "text":
            continue
        line = event["text"].strip()
        if line.startswith(("<!--", "|", "![", "<img", "---")):
            continue
        prose.append(re.sub(r"`[^`]*`|https?://\S+", " ", line))
    # This establishes that explanation text exists, not its pedagogical quality.
    return len(re.findall(r"[^\W\d_]+", " ".join(prose), re.UNICODE)) >= 12


def check_structure(text, file="<markdown>"):
    events = markdown_events(text)
    failures, stack, exercises, solutions = [], [], [], []
    active_id = None
    def error(line, identifier, message):
        failures.append({"file": str(file), "line": line, "exercise": identifier, "message": message})
    for event in events:
        kind = event["kind"]
        if kind == "span":
            active_id = event["text"]
        if kind == "open":
            stack.append({"name": event["text"], "line": event["line"], "id": active_id, "events": []})
            continue
        if kind == "close":
            if not stack:
                error(event["line"], active_id, "Container đóng nhưng không có container mở")
                continue
            opened = stack.pop()
            opened["end"] = event["line"]
            if opened["name"] == "exercise":
                exercises.append(opened)
            elif opened["name"] == "solution":
                solutions.append(opened)
            continue
        for opened in stack:
            opened["events"].append(event)
        if kind == "fence" and not event["closed"]:
            error(event["line"], active_id, "Code fence chưa đóng")
    for opened in stack:
        error(opened["line"], opened["id"], f"Container {opened['name']} chưa đóng")
    paired = set()
    for solution in solutions:
        preceding = [index for index, exercise in enumerate(exercises)
                     if exercise["end"] < solution["line"]]
        if not preceding:
            error(solution["line"], solution["id"], "Lời giải cần có đề trong ::: exercise ở phía trước")
        else:
            nearest = preceding[-1]
            problem = exercises[nearest]
            if nearest in paired or (problem["id"] and solution["id"] != problem["id"]):
                error(solution["line"], solution["id"], "Lời giải không ghép được với một đề riêng đứng ngay trước nó")
            else:
                paired.add(nearest)
                if not any(event["kind"] == "text" and re.search(r"\w", event["text"]) for event in problem["events"]):
                    error(problem["line"], problem["id"], "Container đề bài không có nội dung")
        content = solution["events"]
        methods = [(index, method_number(event["text"])) for index, event in enumerate(content)
                   if event["kind"] == "heading" and method_number(event["text"]) is not None]
        if [number for _, number in methods] != [1, 2]:
            error(solution["line"], solution["id"], f"Cần đúng hai cách giải theo thứ tự 1, 2; tìm thấy {[n for _, n in methods]}")
            continue
        for ordinal, (start, number) in enumerate(methods):
            end = methods[ordinal + 1][0] if ordinal + 1 < len(methods) else len(content)
            segment = content[start + 1:end]
            # A shared comparison section cannot satisfy method 2's missing parts.
            shared = next((index for index, event in enumerate(segment)
                           if event["kind"] == "heading" and re.match(r"^(?:so sanh|doi chieu hai|nhan xet chung|tong ket)\b", normalized_label(event["text"]))), len(segment))
            segment = segment[:shared]
            programs = [(index, event) for index, event in enumerate(segment)
                        if event["kind"] == "fence" and event["language"].casefold() in {"python", "py"}]
            line = content[start]["line"]
            label = f"Cách {number}"
            if not programs:
                error(line, solution["id"], f"{label}: Thiếu chương trình Python đầy đủ")
                continue
            first, program = programs[0]
            try:
                parsed = ast.parse(program["text"])
                if not parsed.body:
                    error(program["line"], solution["id"], f"{label}: Fence Python rỗng")
                missing = sorted(unresolved_globals(program["text"]))
                if missing:
                    error(program["line"], solution["id"], f"{label}: Chương trình phụ thuộc tên bên ngoài fence {missing}")
            except SyntaxError as exc:
                error(program["line"] + (exc.lineno or 1), solution["id"], f"{label}: Python không hợp lệ: {exc.msg}")
            after = segment[first + 1:]
            markers = [index for index, event in enumerate(after) if output_marker(event)]
            # Unlabelled output tables/text/images are valid as long as explanation
            # precedes them. Prefer explicit semantic labels when they are present.
            if markers:
                boundary = markers[0]
            else:
                boundary = next((index for index, event in enumerate(after)
                                 if event["kind"] == "fence" or (event["kind"] == "text" and
                                    ("|" in event["text"] or output_payload([event])))), len(after))
            if not explanation_present(after[:boundary]):
                error(line, solution["id"], f"{label}: Thiếu phần giải thích riêng sau mã và trước output")
            if boundary == len(after) or not output_payload(after[boundary:]):
                error(line, solution["id"], f"{label}: Thiếu output riêng có nội dung trước cách tiếp theo hoặc hết lời giải")
            if len(programs) > 1:
                error(line, solution["id"], f"{label}: Có {len(programs)} fence Python; cần gom thành một chương trình đầy đủ trước phần giải thích")
    for index, problem in enumerate(exercises):
        if index not in paired:
            error(problem["line"], problem["id"], "Đề bài chưa có lời giải riêng sau nó")
    if not exercises:
        error(1, None, "Không tìm thấy bài tập trong ::: exercise")
    return {"file": str(file), "exercises": len(exercises), "methods": sum(
        event["kind"] == "heading" and method_number(event["text"]) is not None
        for solution in solutions for event in solution["events"]), "errors": failures}


def structure_only(files):
    records = [check_structure(file.read_text(encoding="utf-8"), file) for file in files]
    errors = [error for record in records for error in record["errors"]]
    for error in errors:
        print(f"{error['file']}:{error['line']}: {error['exercise'] or '-'}: {error['message']}")
    print(json.dumps({"passed": not errors, "files": len(records),
                      "exercises": sum(record["exercises"] for record in records),
                      "methods": sum(record["methods"] for record in records), "errors": errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--structure-only", action="store_true", help="Check current Markdown without numerical verifiers or coverage prerequisites")
    parser.add_argument("files", nargs="*", type=Path, help="Optional files for --structure-only")
    options = parser.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if options.structure_only:
        files = options.files or sorted((Path(__file__).resolve().parents[1] / "raw_materials/xu-ly-du-lieu/labs").glob("lab-*.md"))
        raise SystemExit(structure_only(files))
    if options.files:
        parser.error("Explicit files require --structure-only")

root = Path(__file__).resolve().parents[1]
expected = ["01", "02", "03", "04", "05", "06", "07", "07-regex", "08", "10", "11", "12", "13", "14"]
inventory = json.loads((root / "raw_materials/xu-ly-du-lieu/lab-source-inventory.json").read_text(encoding="utf-8"))
assert len(inventory["sources"]) == 27
placement = json.loads((root / "raw_materials/xu-ly-du-lieu/lab-placement.json").read_text(encoding="utf-8"))
placed = [name for item in placement for name in item["files"]]
assert len(placed) == len(set(placed)), "One lab fragment must have one canonical chapter"
records = []
env = os.environ.copy()
env.update(PYTHONIOENCODING="utf-8", MPLBACKEND="Agg")
for lab in expected:
    files = sorted((root / "raw_materials/xu-ly-du-lieu/labs").glob(f"lab-{lab}.md"))
    if lab == "05":
        files = sorted((root / "raw_materials/xu-ly-du-lieu/labs").glob("lab-05-*.md"))
    assert files, f"Missing lab {lab}"
    assert (root / f"raw_materials/xu-ly-du-lieu/labs/coverage-{lab}.json").is_file()
    for file in files:
        assert file.name in placed, f"Not integrated: {file.name}"
        text = file.read_text(encoding="utf-8")
        assert not re.search(r"public_check|check_public|PUBLIC_RESULTS|LTXLDL|Khai báo (?:sử dụng )?AI|Hạn nộp|grader", text, re.I), file
        prose = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
        assert not re.search(r"^#\s", prose, re.M), f"No H1 in fragment: {file}"
        assert not re.search(r"C:[/\\]Users[/\\]Ai|\.codex[/\\]worktrees", text), f"Local machine path in lesson: {file}"
        exercises = len(re.findall(r"^::: exercise(?: |$)", text, re.M))
        solutions = len(re.findall(r"^::: solution(?: |$)", text, re.M))
        assert exercises == solutions and exercises > 0, (file, exercises, solutions)
        structure = check_structure(text, file)
        assert not structure["errors"], json.dumps(structure["errors"], ensure_ascii=False, indent=2)
        blocks = re.findall(r"^```python[^\n]*\n(.*?)^```\s*$", text, re.M | re.S)
        for index, code in enumerate(blocks):
            ast.parse(code, filename=f"{file.name} block {index + 1}")
        records.append({"lab": lab, "file": file.name, "exercises": exercises, "pythonBlocks": len(blocks)})
    verifier = root / f"scripts/verify-data-lab-{lab}.py"
    assert verifier.is_file(), verifier
    result = subprocess.run([sys.executable, str(verifier)], cwd=root, env=env, check=False)
    assert result.returncode == 0, verifier
    visible = subprocess.run([sys.executable, str(root / "scripts/verify-data-lab-markdown.py"), "--require-calls", *map(str, files)], cwd=root, env=env, check=False)
    assert visible.returncode == 0, f"Published Markdown does not run: {lab}"
print(json.dumps({"notebooks": 27, "labs": len(expected), "exercises": sum(r["exercises"] for r in records), "pythonBlocks": sum(r["pythonBlocks"] for r in records), "records": records}, ensure_ascii=False, indent=2))
