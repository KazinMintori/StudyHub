#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification suite for Physics Chapter 43 Exercises Group D
Ensures 46 complete closed solutions, substantive physical recomputations,
MathJax syntax compliance, and image annotations integrity.
"""

import math
import os
import re
import sys
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
TRANSLATIONS_DIR = BASE_DIR / "raw_materials" / "physics" / "translations" / "chapter-43"
IMG_DIR = BASE_DIR / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-43"
ANNOTATIONS_FILE = BASE_DIR / "docs" / ".vitepress" / "physics43-exercises-d-image-annotations.mjs"

FILE_12 = TRANSLATIONS_DIR / "12-bai-tap-33-48.md"
FILE_13 = TRANSLATIONS_DIR / "13-bai-tap-49-64.md"
FILE_14 = TRANSLATIONS_DIR / "14-bai-tap-65-72.md"
FILE_15 = TRANSLATIONS_DIR / "15-mcat.md"
FILE_16 = TRANSLATIONS_DIR / "16-bai-tap-cau-noi.md"

ALL_TRANSLATION_FILES = [FILE_12, FILE_13, FILE_14, FILE_15, FILE_16]


def test_files_exist():
    print("[1/6] Checking file existence...")
    for f in ALL_TRANSLATION_FILES:
        assert f.is_file(), f"Missing translation file: {f}"
    assert ANNOTATIONS_FILE.is_file(), f"Missing annotations file: {ANNOTATIONS_FILE}"

    for i in range(1, 9):
        svg = IMG_DIR / f"loi-giai-d-{i:02d}.svg"
        assert svg.is_file(), f"Missing SVG asset: {svg}"
        content = svg.read_text(encoding="utf-8")
        assert "<svg" in content and "</svg>" in content, f"Invalid SVG file: {svg}"
    print("      All required files and SVG assets exist.")


def test_problem_count_and_structure():
    print("[2/6] Verifying problem counts, IDs, and structure...")
    expected_ids = {
        FILE_12: [f"### 43.{n}" for n in range(33, 49)],
        FILE_13: [f"### 43.{n}" for n in range(49, 65)],
        FILE_14: [f"### 43.{n}" for n in range(65, 73)],
        FILE_15: [f"### 43.{n}" for n in range(73, 78)],
        FILE_16: ["### Bài tập cầu nối"],
    }

    total_problems = 0
    all_found_ids = []

    for f, ids in expected_ids.items():
        text = f.read_text(encoding="utf-8")
        for pid in ids:
            assert pid in text, f"Missing problem ID {pid} in {f.name}"
            # Check single occurrence
            count = text.count(pid)
            assert count == 1, f"Problem ID {pid} appears {count} times in {f.name} (must be exactly 1)"
            all_found_ids.append(pid)
            total_problems += 1

        # Check details block count
        open_details = text.count("<details>")
        close_details = text.count("</details>")
        assert open_details == len(ids), f"File {f.name} has {open_details} <details> tags, expected {len(ids)}"
        assert close_details == open_details, f"File {f.name} has mismatched details tags"

        # Check required pedagogical headers
        assert text.count("<summary>Xem lời giải chi tiết</summary>") == len(ids)
        assert text.count("**Tóm tắt đề bài:**") == len(ids)
        assert text.count("**Hướng đi:**") == len(ids)

    assert total_problems == 46, f"Expected exactly 46 problems, found {total_problems}"
    print(f"      Verified exactly {total_problems} problems across 5 files with complete structure.")


def test_formatting_and_math_rules():
    print("[3/6] Checking MathJax delimiters and style guidelines...")
    for f in ALL_TRANSLATION_FILES:
        lines = f.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines, 1):
            # Check $$ alone on column 0 lines
            if "$$" in line:
                assert line.strip() == "$$", f"{f.name}:{idx} Display delimiter '$$' not alone on its own line: {line}"
            # No isolated single dollar on line
            assert not re.match(r"^\s*\$\s*$", line), f"{f.name}:{idx} Isolated single dollar on line"
            # No machine local links
            assert not re.search(r"file://|[A-Z]:[\\/](Users|My Drive)", line), f"{f.name}:{idx} Local machine link found"

    print("      MathJax formatting rules verified.")


def test_colon_capitalization():
    print("[4/6] Verifying capitalization after colons in prose...")
    colon_violations = []
    for f in ALL_TRANSLATION_FILES:
        lines = f.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines, 1):
            # Skip code blocks, math display lines, URLs, image paths
            if line.startswith("$$") or line.startswith("```") or line.startswith("!"):
                continue
            # Find colon followed by space and a character
            matches = re.finditer(r":\s+(\S)", line)
            for m in matches:
                char = m.group(1)
                prefix = line[:m.start()]
                if prefix.endswith("http") or prefix.endswith("https"):
                    continue
                dollar_count = prefix.count("$")
                if dollar_count % 2 == 1:
                    # Inside inline math
                    continue
                if char.isalpha() and char.islower():
                    colon_violations.append((f.name, idx, line.strip()))

    if colon_violations:
        print(f"      Warning: Found {len(colon_violations)} lowercase letters after colons:")
        for fn, ln, txt in colon_violations[:5]:
            print(f"        {fn}:{ln} -> {txt[:60]}")
    assert len(colon_violations) == 0, f"Found {len(colon_violations)} colon capitalization violations"
    print("      All colons in prose follow proper capitalization.")


def test_numerical_recomputations():
    import runpy
    runpy.run_path(str(BASE_DIR/'raw_materials/physics/verify_chapter43_end_parent.py'),run_name='__main__')


def test_image_annotations():
    print("[6/6] Checking image annotations module...")
    content = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    assert "export const physics43ExercisesDImageAnnotations" in content
    for i in range(1, 9):
        key = f"young-43/loi-giai-d-{i:02d}"
        assert key in content, f"Missing annotation key for {key}"
    print("      Image annotations module verified.")


def main():
    print("=" * 60)
    print("VERIFYING STUDYHUB CHAPTER 43 EXERCISES GROUP D")
    print("=" * 60)
    test_files_exist()
    test_problem_count_and_structure()
    test_formatting_and_math_rules()
    test_colon_capitalization()
    test_numerical_recomputations()
    test_image_annotations()
    print("=" * 60)
    print("ALL Chapter 43 Group D Verification Assertions Passed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
