#!/usr/bin/env python3
"""Import the supplied philosophy question banks without rewriting their content.

The Markdown files are data. Only anchored question, answer, and matrix records
are parsed. No instructions or code from a source document are executed.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw_materials/triet-hoc-mac-lenin/exam"
OUTPUT_DIR = ROOT / "src/content/courses/triet-hoc-mac-lenin/exam"
SPECS = (
    {
        "chapter": 1,
        "prefix": "CH",
        "count": 360,
        "questionFile": "01_Ngan_hang_cau_hoi_Chuong_I (1).md",
        "answerFile": "02_Dap_an_giai_thich_va_ma_tran_Chuong_I.md",
        "title": "Chương I. Triết học và vai trò của triết học trong đời sống xã hội",
    },
    {
        "chapter": 2,
        "prefix": "Q",
        "count": 440,
        "questionFile": "01_Cau_hoi_Chuong_II.md",
        "answerFile": "02_Dap_an_Giai_thich_Ma_tran_Chuong_II.md",
        "title": "Chương II. Chủ nghĩa duy vật biện chứng",
    },
)
CHAPTER_ONE_GROUPS = {
    "I.1": ("A", "Khái lược triết học và thế giới quan"),
    "I.2": ("B", "Vấn đề cơ bản và các trường phái"),
    "I.3": ("C", "Biện chứng và siêu hình"),
    "II.1": ("D", "Ra đời và phát triển triết học Mác - Lênin"),
    "II.2": ("E", "Khái niệm, đối tượng và chức năng"),
    "II.3": ("F", "Vai trò của triết học và sự nghiệp đổi mới"),
}


class QuizImportError(ValueError):
    """A source bank is incomplete, ambiguous, or internally inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise QuizImportError(message)


def plain(text: str) -> str:
    """Remove inline Markdown emphasis, preserving wording and line breaks."""
    return text.replace("**", "").replace("__", "").replace("`", "").strip()


def records(text: str, prefix: str, answer: bool = False) -> dict[str, str]:
    # Stop at any next heading, so the final record cannot absorb source reports.
    level = "####" if answer else ("###" if prefix == "CH" else "##")
    heading = re.compile(
        rf"^{level} ({prefix}\d{{3}})(?:[^\n]*)$", re.MULTILINE
    )
    result = {}
    for match in heading.finditer(text):
        question_id = match.group(1)
        require(question_id not in result, f"Duplicate record {question_id}")
        tail = text[match.end():]
        next_heading = re.search(r"^#{1,6} ", tail, re.MULTILINE)
        end = match.end() + next_heading.start() if next_heading else len(text)
        result[question_id] = text[match.start():end].strip()
    return result


def parse_questions(text: str, prefix: str) -> dict[str, dict]:
    result = {}
    for question_id, block in records(text, prefix).items():
        body = plain(block.split("\n", 1)[1])
        option_matches = list(re.finditer(r"^([A-D])\.\s+", body, re.MULTILINE))
        keys = [match.group(1) for match in option_matches]
        require(keys == list("ABCD"), f"{question_id}: Expected four ordered options, got {keys}")
        prompt = body[:option_matches[0].start()].strip()
        require(bool(prompt), f"{question_id}: Empty question")
        options = []
        for index, match in enumerate(option_matches):
            end = option_matches[index + 1].start() if index + 1 < 4 else len(body)
            value = body[match.end():end].strip()
            require(bool(value), f"{question_id}: Empty option {match.group(1)}")
            options.append({"key": match.group(1), "text": value})
        result[question_id] = {"id": question_id, "kind": "quiz", "prompt": prompt, "options": options}
    return result


def parse_quick_answers(text: str, prefix: str) -> dict[str, str]:
    marker = re.search(r"^### Bảng đáp án nhanh\s*$", text, re.MULTILINE)
    require(marker is not None, "Missing independent quick-answer table")
    tail = text[marker.end():]
    end = re.search(r"^#{1,6} ", tail, re.MULTILINE)
    table = tail[:end.start()] if end else tail
    result = {}
    for question_id, key in re.findall(rf"\|\s*({prefix}\d{{3}})\s*\|\s*([A-D])\s*(?=\|)", table):
        require(question_id not in result, f"Duplicate quick-answer entry {question_id}")
        result[question_id] = key
    return result


def field(block: str, label: str, question_id: str) -> str:
    # Fields are line anchored. A stray instruction elsewhere is not a field.
    match = re.search(rf"^(?:- )?{re.escape(label)}:\s*(.+)$", block, re.MULTILINE)
    require(match is not None and bool(match.group(1).strip()), f"{question_id}: Missing {label}")
    return match.group(1).strip()


def parse_answers(text: str, prefix: str) -> dict[str, dict]:
    result = {}
    for question_id, raw_block in records(text, prefix, answer=True).items():
        block = plain(raw_block)
        key_matches = re.findall(r"Đáp án\s*:?\s*([A-D])\b", block)
        require(len(key_matches) == 1, f"{question_id}: Expected exactly one answer key")
        key = key_matches[0]
        metadata = re.search(
            r"^(?:- )?(?:Mã kiến thức|Kiến thức):\s*(.+?)\. Loại:\s*(.+?)\. Mức độ:\s*(.+?)\. Độ khó dự kiến:",
            block,
            re.MULTILINE,
        )
        require(metadata is not None, f"{question_id}: Missing structured metadata")
        knowledge_ids = [item.strip() for item in metadata.group(1).split(",")]
        require(all(knowledge_ids), f"{question_id}: Empty knowledge ID")
        question_type = metadata.group(2)
        require(question_type in ("Lý thuyết", "Vận dụng"), f"{question_id}: Unknown question type")
        if prefix == "CH":
            explanation = field(block, "Vì sao đúng", question_id)
            reference = field(block, "Nguồn đã kiểm tra", question_id)
        else:
            rationale = re.search(r"^(?:Luận điểm/dữ kiện nguồn|Dữ kiện/cách hiểu).*?kết luận:\s*(.+)$", block, re.MULTILINE)
            require(rationale is not None, f"{question_id}: Missing correct rationale")
            explanation = rationale.group(1).strip()
            reference = field(block, "Căn cứ đã đối chiếu", question_id)
        distractors = [
            {"key": match.group(1), "explanation": match.group(2).strip()}
            for match in re.finditer(r"^- ([A-D])(?:\s*[—–-]\s*|\s+)sai:\s*(.+)$", block, re.MULTILINE | re.IGNORECASE)
        ]
        expected = set("ABCD") - {key}
        require(len(distractors) == 3 and {item["key"] for item in distractors} == expected,
                f"{question_id}: Need one explanation for each of the three incorrect options")
        result[question_id] = {
            "correctKey": key,
            "explanation": explanation,
            "distractors": distractors,
            "takeaway": field(block, "Cần nắm", question_id),
            "sourceReference": reference,
            "knowledgeIds": knowledge_ids,
            "level": metadata.group(3),
            "questionType": question_type,
        }
    return result


def parse_matrix(text: str, prefix: str) -> dict[str, dict]:
    start = text.index("### Ma trận đầy đủ")
    tail = text[start:]
    end = re.search(r"^## ", tail, re.MULTILINE)
    matrix = tail[:end.start()] if end else tail
    knowledge = {}
    current_group = None
    for line in matrix.splitlines():
        group_heading = re.match(r"^#### ([A-L]\d*)\. (.+)$", line)
        if group_heading:
            current_group = group_heading.groups()
        if not line.startswith("|"):
            continue
        cells = [plain(cell) for cell in line.strip().strip("|").split("|")]
        if len(cells) != 7 or not re.fullmatch(r"(?:KT\d+[a-z]?|[A-L]\d*(?:[-.][A-Za-z0-9]+)+)", cells[0]):
            continue
        knowledge_id, section = cells[:2]
        require(knowledge_id not in knowledge, f"Duplicate matrix ID {knowledge_id}")
        if prefix == "CH":
            section_match = re.match(r"^(II?\.\d+)\b", section)
            require(section_match is not None and section_match.group(1) in CHAPTER_ONE_GROUPS,
                    f"Cannot group matrix entry {knowledge_id}: {section}")
            group = CHAPTER_ONE_GROUPS[section_match.group(1)]
        else:
            require(current_group is not None, f"Missing group for {knowledge_id}")
            group = current_group
        knowledge[knowledge_id] = {
            "group": group[0], "groupTitle": group[1],
            "questionIds": re.findall(rf"\b{prefix}\d{{3}}\b", cells[6]),
        }
    require(bool(knowledge), "Missing knowledge matrix")
    return knowledge


def build_bank(question_text: str, answer_text: str, spec: dict) -> tuple[dict, dict]:
    prefix, expected_count = spec["prefix"], spec["count"]
    questions = parse_questions(question_text, prefix)
    answers = parse_answers(answer_text, prefix)
    answer_blocks = records(answer_text, prefix, answer=True)
    quick = parse_quick_answers(answer_text, prefix)
    matrix = parse_matrix(answer_text, prefix)
    expected_ids = {f"{prefix}{number:03d}" for number in range(1, expected_count + 1)}
    for name, values in (("questions", questions), ("answers", answers), ("quick answers", quick)):
        require(set(values) == expected_ids,
                f"{name}: Expected IDs do not match. Missing {sorted(expected_ids-set(values))}, extra {sorted(set(values)-expected_ids)}")
    warnings = []
    for question_id in questions:
        answer = answers[question_id]
        require(quick[question_id] == answer["correctKey"], f"{question_id}: Quick table and detailed answer disagree")
        summary_pattern = (r"^- Đáp án:\s*[A-D]\s*[—–-]\s*(.+)$" if prefix == "CH"
                           else r"(?:Vì vậy|Do đó) chọn [A-D]:\s*(.+)$")
        summary = re.search(summary_pattern, plain(answer_blocks[question_id]), re.MULTILINE)
        require(summary is not None, f"{question_id}: Missing selected-option summary")
        selected_option = next(option["text"] for option in questions[question_id]["options"] if option["key"] == answer["correctKey"])
        require(summary.group(1).strip() == selected_option,
                f"{question_id}: Selected option text differs from detailed-answer summary")
        require(all(item in matrix for item in answer["knowledgeIds"]), f"{question_id}: Unknown knowledge ID")
        for knowledge_id in answer["knowledgeIds"]:
            require(question_id in matrix[knowledge_id]["questionIds"], f"{question_id}: Missing matrix link for {knowledge_id}")
        first = matrix[answer["knowledgeIds"][0]]
        questions[question_id].update(answer, group=first["group"], groupTitle=first["groupTitle"])
    for knowledge_id, entry in matrix.items():
        require(bool(entry["questionIds"]), f"{knowledge_id}: Matrix has no question")
        for question_id in entry["questionIds"]:
            require(question_id in questions, f"{knowledge_id}: Matrix links nonexistent {question_id}")
            if knowledge_id not in answers[question_id]["knowledgeIds"]:
                warnings.append({"code": "MATRIX_ONLY_LINK", "questionId": question_id, "knowledgeId": knowledge_id})
    source_files = [f"raw_materials/triet-hoc-mac-lenin/exam/{spec[field]}" for field in ("questionFile", "answerFile")]
    bank = {
        "schemaVersion": 1, "id": f"chuong-{spec['chapter']}", "chapter": spec["chapter"],
        "title": spec["title"],
        "description": "Câu hỏi trắc nghiệm kèm đáp án, giải thích từng phương án và nội dung cần nắm.",
        "sourceFiles": source_files,
        "questions": [questions[question_id] for question_id in sorted(questions)],
    }
    report = {
        "id": bank["id"], "questionCount": len(questions), "quickAnswerCount": len(quick),
        "knowledgeCount": len(matrix), "answerDistribution": dict(sorted(Counter(quick.values()).items())),
        "questionTypes": dict(Counter(item["questionType"] for item in questions.values())),
        "levels": dict(Counter(item["level"] for item in questions.values())),
        "groups": [{"id": group, "title": next(q["groupTitle"] for q in questions.values() if q["group"] == group), "count": count}
                   for group, count in sorted(Counter(q["group"] for q in questions.values()).items())],
        "warnings": warnings,
    }
    return bank, report


def source_notes(answer_text: str, chapter: int) -> list[dict]:
    answer_text = answer_text.replace("\r\n", "\n")
    if chapter == 1:
        notes = []
        for line in answer_text.splitlines():
            if re.match(r"^\| CT\d+ \|", line):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                notes.append({"id": cells[0], "section": cells[1], "detail": cells[2], "pages": cells[3], "sourceCaveat": cells[4]})
        return notes
    # Keep source caveats as attributed source information, not verified facts.
    paragraphs = answer_text.split("\n\n")
    selected = [paragraph for paragraph in paragraphs if paragraph.startswith(("Giữ cách trình bày riêng", "Những dữ kiện gắn thời điểm", "Bản này đi thẳng"))]
    return [{"id": f"SOURCE-{index}", "sourceCaveat": plain(paragraph)} for index, paragraph in enumerate(selected, 1)]


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def run(source_dir: Path, check: bool = False) -> dict:
    banks, chapter_reports, files = [], [], []
    for spec in SPECS:
        source_texts = []
        for field in ("questionFile", "answerFile"):
            path = source_dir / spec[field]
            data = path.read_bytes()
            source_texts.append(data.decode("utf-8-sig"))
            files.append({"path": f"raw_materials/triet-hoc-mac-lenin/exam/{path.name}",
                          "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
        bank, chapter_report = build_bank(*source_texts, spec)
        chapter_report["sourceCaveats"] = source_notes(source_texts[1], spec["chapter"])
        banks.append(bank)
        chapter_reports.append(chapter_report)
    catalog = {
        "schemaVersion": 1, "course": "triet-hoc-mac-lenin", "totalCount": sum(len(bank["questions"]) for bank in banks),
        "banks": [{"id": bank["id"], "chapter": bank["chapter"], "title": bank["title"],
                   "count": len(bank["questions"]), "file": f"{bank['id']}.json", "groups": report["groups"]}
                  for bank, report in zip(banks, chapter_reports)],
    }
    report = {
        "schemaVersion": 1, "totalQuestions": catalog["totalCount"], "files": files,
        "validation": {"idsComplete": True, "fourOptionsPerQuestion": True, "detailedAnswersMatchQuickTable": True,
                       "selectedOptionMatchesDetailedAnswer": True,
                       "threeDistractorExplanations": True, "referencesAndTakeawaysPresent": True, "knowledgeMatrixCrossChecked": True,
                       "wordingRewritten": False, "historicalAndFactualClaimsIndependentlyVerified": False},
        "chapters": chapter_reports,
        "notes": ["Source files are copied byte for byte. Inline Markdown emphasis is removed from display text only.",
                  "Group metadata comes from the matrix. Primary group follows the first knowledge ID in each detailed answer.",
                  "Source caveats and difficulty labels are supplied author metadata, not independent factual or psychometric verification.",
                  "No chapter III bank was supplied or generated."],
    }
    outputs = {OUTPUT_DIR / f"{bank['id']}.json": bank for bank in banks}
    outputs[OUTPUT_DIR / "catalog.json"] = catalog
    outputs[RAW_DIR / "import-report.json"] = report
    if check:
        for path, expected in outputs.items():
            require(path.exists() and json.loads(path.read_text(encoding="utf-8")) == expected, f"Generated output differs: {path}")
    else:
        RAW_DIR.mkdir(parents=True, exist_ok=True)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        for spec in SPECS:
            for field in ("questionFile", "answerFile"):
                path = source_dir / spec[field]
                destination = RAW_DIR / path.name
                if path.resolve() != destination.resolve():
                    shutil.copyfile(path, destination)
        for path, value in outputs.items():
            path.write_text(json_text(value), encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, help="Directory containing the four supplied Markdown files")
    parser.add_argument("--check", action="store_true", help="Validate the preserved sources and generated JSON without writing")
    args = parser.parse_args()
    source_dir = args.source_dir or (RAW_DIR if args.check else Path.home() / "Downloads")
    try:
        report = run(source_dir, args.check)
    except (QuizImportError, OSError, UnicodeError) as error:
        print(f"Import failed: {error}", file=sys.stderr)
        return 1
    print(f"{'Validated' if args.check else 'Imported'} {report['totalQuestions']} questions: " + ", ".join(f"{item['id']}={item['questionCount']}" for item in report["chapters"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
