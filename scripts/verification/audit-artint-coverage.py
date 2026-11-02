"""Produce an independent source-to-translation coverage audit.

Size, numbered examples and formula counts are review signals, not proof of a
correct translation. Missing source mappings are hard failures. This script
never labels content semantically verified.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


def body(text: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.S)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--source", type=Path)
    parser.add_argument("--part", choices=["a", "b", "c"])
    parser.add_argument("--chapter", type=int, action="append")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    source = (args.source or root / "raw_materials/ai-nen-tang-tac-tu/source").resolve()
    manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8"))
    pages = list((root / "docs/ai-nen-tang-tac-tu/bai-giang").rglob("*.md"))
    texts = {p: body(p.read_text(encoding="utf-8")) for p in pages}
    records = []
    for chapter in manifest["chapters"]:
        if args.part and chapter["part"] != args.part:
            continue
        if args.chapter and chapter["number"] not in args.chapter:
            continue
        for page in chapter["pages"]:
            targets = [p for p, text in texts.items() if page["source"] in text]
            target_text = "\n\n".join(texts[p] for p in targets)
            original = (source / "text" / page["filename"].replace(".html", ".md")).read_text(encoding="utf-8")
            source_words = len(original.split())
            target_words = len(target_text.split())
            source_examples = sorted(set(re.findall(r"^#{1,6}\s+Example\s+(\d+\.\d+)", original, re.M)))
            target_examples = sorted(set(re.findall(
                r"^(?:#{1,6}\s+|:::\s+example\s+)(?:Ví dụ\s+)?(\d+\.\d+)", target_text, re.M | re.I)))
            missing_examples = [n for n in source_examples if n not in target_examples]
            flags = []
            if not targets:
                flags.append("MISSING_SOURCE_MAPPING")
            if targets and source_words > 150 and target_words < source_words * 0.6:
                flags.append("SHORT_TRANSLATION_REVIEW_REQUIRED")
            if missing_examples:
                flags.append("NUMBERED_EXAMPLES_REVIEW_REQUIRED")
            records.append(dict(chapter=chapter["number"], source=page["source"],
                                targets=[str(p.relative_to(root)).replace("\\", "/") for p in targets],
                                source_words=source_words, target_words=target_words,
                                source_examples=source_examples, missing_examples=missing_examples,
                                source_math_delimiters=original.count("$"),
                                target_math_delimiters=target_text.count("$"), flags=flags))
    report = dict(pages=len(records), mapped=sum(bool(r["targets"]) for r in records),
                  missing=sum("MISSING_SOURCE_MAPPING" in r["flags"] for r in records),
                  review_flags=sum(bool(r["flags"]) for r in records),
                  semantic_verification="Not assessed by this script", records=records)
    output = args.output or root / "qa/artint3e/source-coverage.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "records"}, ensure_ascii=False))
    print(output)
    raise SystemExit(1 if report["missing"] else 0)


if __name__ == "__main__":
    main()
