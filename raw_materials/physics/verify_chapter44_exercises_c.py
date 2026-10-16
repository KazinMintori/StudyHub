"""
verify_chapter44_exercises_c.py
Comprehensive physics recalculation and strict pedagogical quality verification
for Chapter 44 exercises c (StudyHub UET).
Scope: Exactly 55 closed problems:
  - 12 Guided Practice (VP44.1.1-4, VP44.3.1-4, VP44.9.1-4) in 09-luyen-tap-huong-dan.md
  - 13 Discussion Questions (Q44.1-13) in 10-cau-hoi-thao-luan.md
  - 30 Exercises (44.1-30) in 11-bai-tap-01-30.md
"""

import sys
import re
from pathlib import Path

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
CH44_DIR = ROOT_DIR / "raw_materials" / "physics" / "translations" / "chapter-44"

FILE_09 = CH44_DIR / "09-luyen-tap-huong-dan.md"
FILE_10 = CH44_DIR / "10-cau-hoi-thao-luan.md"
FILE_11 = CH44_DIR / "11-bai-tap-01-30.md"
ANNOTATIONS_FILE = ROOT_DIR / "docs" / ".vitepress" / "physics44-exercises-c-image-annotations.mjs"
IMG_DIR = ROOT_DIR / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-44"

# Fundamental Physical Constants
C = 2.99792458e8         # m/s
H = 6.62607015e-34       # J*s
HBAR = H / (2 * 3.141592653589793) # J*s
E_CHARGE = 1.602176634e-19 # C
U_TO_KG = 1.66053906660e-27 # kg
U_TO_MEV = 931.49410242  # MeV
M_E_KG = 9.1093837e-31   # kg
M_E_MEV = 0.51099895     # MeV
M_P_KG = 1.67262192e-27  # kg
M_P_MEV = 938.272088     # MeV
M_N_KG = 1.6749275e-27   # kg
M_N_MEV = 939.565420     # MeV
PC_TO_M = 3.085677581e16 # m
LY_TO_M = 9.460730472e15 # m
MPC_TO_KM = 3.085677581e19 # km


def test_file_existence():
    print("--- [1] Checking File Existence ---")
    assert FILE_09.exists(), f"Missing {FILE_09}"
    assert FILE_10.exists(), f"Missing {FILE_10}"
    assert FILE_11.exists(), f"Missing {FILE_11}"
    assert ANNOTATIONS_FILE.exists(), f"Missing {ANNOTATIONS_FILE}"
    assert IMG_DIR.exists(), f"Missing {IMG_DIR}"
    print("OK: All primary content and metadata files exist.")


def test_asset_files():
    print("--- [2] Checking Generated Pedagogical SVGs ---")
    expected_svgs = [f"loi-giai-c-0{i}.svg" for i in range(1, 9)]
    for svg_name in expected_svgs:
        svg_path = IMG_DIR / svg_name
        assert svg_path.exists(), f"Missing SVG {svg_name}"
        assert svg_path.stat().st_size > 500, f"SVG {svg_name} too small ({svg_path.stat().st_size} bytes)"
    print(f"OK: All {len(expected_svgs)} pedagogical SVGs exist and are valid.")


def test_image_annotations():
    print("--- [3] Checking Image Annotations Registry ---")
    content = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    for i in range(1, 9):
        key = f"young-44/loi-giai-c-0{i}"
        assert key in content, f"Missing annotation key: {key}"
    print("OK: All 8 annotation keys present in physics44-exercises-c-image-annotations.mjs.")


def test_problem_counts_and_structure():
    print("--- [4] Checking Problem Counts & Structural Tags ---")

    # 09-luyen-tap-huong-dan.md
    c09 = FILE_09.read_text(encoding="utf-8")
    vp_headers = re.findall(r"^### (VP44\.\d+\.\d+)", c09, re.MULTILINE)
    assert len(vp_headers) == 12, f"Expected 12 Guided Practice exercises, found {len(vp_headers)}: {vp_headers}"

    # 10-cau-hoi-thao-luan.md
    c10 = FILE_10.read_text(encoding="utf-8")
    q_headers = re.findall(r"^### Q44\.(\d+)", c10, re.MULTILINE)
    assert len(q_headers) == 13, f"Expected 13 Discussion questions, found {len(q_headers)}"

    # 11-bai-tap-01-30.md
    c11 = FILE_11.read_text(encoding="utf-8")
    ex_headers = re.findall(r"^### 44\.(\d+)", c11, re.MULTILINE)
    assert len(ex_headers) == 30, f"Expected 30 exercises, found {len(ex_headers)}: {ex_headers}"

    total_problems = len(vp_headers) + len(q_headers) + len(ex_headers)
    assert total_problems == 55, f"Expected exactly 55 problems, got {total_problems}"
    print(f"OK: Exactly 55 closed problems found (12 VP, 13 Q, 30 Exercises).")

    # Check details and required sections
    all_files = [(FILE_09, c09), (FILE_10, c10), (FILE_11, c11)]
    for path, content in all_files:
        details_open = content.count("<details>")
        details_close = content.count("</details>")
        assert details_open == details_close, f"Unbalanced details in {path.name}: {details_open} vs {details_close}"

        summaries = content.count("<summary>Xem lời giải chi tiết</summary>")
        assert summaries == details_open, f"Mismatched summary tags in {path.name}"

        tom_tat = content.count("**Tóm tắt đề bài:**")
        huong_di = content.count("**Hướng đi:**")
        loi_giai = content.count("**Lời giải chi tiết:**")
        assert tom_tat == details_open, f"Missing Tóm tắt in {path.name}: {tom_tat} vs {details_open}"
        assert huong_di == details_open, f"Missing Hướng đi in {path.name}: {huong_di} vs {details_open}"
        assert loi_giai == details_open, f"Missing Lời giải in {path.name}: {loi_giai} vs {details_open}"

    print("OK: All 55 problems possess mandatory sections and balanced HTML details tags.")


def test_pedagogical_language_rules():
    print("--- [5] Checking Vietnamese Pedagogical Voice & Prohibited Patterns ---")
    prohibited_phrases = [
        "lấy từ sách",
        "theo sách",
        "sách dùng",
        "giáo trình nêu",
        "nguyên tác",
        "bản dịch của",
        "do người soạn",
        "hình trong sách",
        "ảnh nguyên gốc",
        "Khoan đã",
        "À không",
        "Ý tôi là",
        "Thử lại nào",
        "Nhầm rồi",
        "Sinh viên rất hay nhầm",
        "Lỗi phổ biến nhất",
        "Đa số sinh viên",
        "Bẫy thi cử cực kỳ phổ biến",
        "hợp đồng file",
        "hợp đồng dữ liệu",
    ]

    vn_letters = "a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
    boundary = rf"(?:^|[^{vn_letters}\d])"
    boundary_end = rf"(?:$|[^{vn_letters}\d])"

    all_files = [FILE_09, FILE_10, FILE_11]
    for path in all_files:
        content = path.read_text(encoding="utf-8").lower()
        for phrase in prohibited_phrases:
            pattern = re.compile(boundary + re.escape(phrase.lower()) + boundary_end)
            m = pattern.search(content)
            assert not m, f"Prohibited phrase '{phrase}' found in {path.name}"

        # Check em-dash
        assert "—" not in content, f"Em-dash ('—') found in {path.name}. Replace with commas, parentheses or colons."
        assert " -- " not in content, f"Double dash (' -- ') found in {path.name}."

    print("OK: Zero prohibited phrases, zero translationese, zero em-dashes.")


def test_colon_capitalization():
    print("--- [6] Checking Capitalization After Colons ---")
    all_files = [FILE_09, FILE_10, FILE_11]

    # In Vietnamese prose, after ": ", the next character must be uppercase if it's a letter,
    # except when followed by a math expression ($), a code block, a URL, or digits.
    # Regex: find ': [a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]'
    vn_lower = "a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
    colon_pattern = re.compile(rf": ([{vn_lower}])")

    violations = []
    for path in all_files:
        lines = path.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines, start=1):
            # Skip code blocks or image paths
            if line.strip().startswith("```") or line.strip().startswith("!") or line.strip().startswith("<img"):
                continue
            # Also skip URLs or math equations that start with $$
            if "$$" in line or "http://" in line or "https://" in line:
                continue
            m = colon_pattern.search(line)
            if m:
                violations.append((path.name, idx, m.group(0), line.strip()))

    assert len(violations) == 0, f"Found {len(violations)} colon capitalization violations: {violations[:5]}"
    print("OK: Full compliance with Colon Capitalization Rule across all prose lines.")


def test_physics_calculations():
    import runpy
    runpy.run_path(str(ROOT_DIR/'raw_materials/physics/verify_chapter44_end_parent.py'),run_name='__main__')


def main():
    print("==================================================")
    print(" RUNNING CHAPTER 44 EXERCISES C VERIFICATION SUITE")
    print("==================================================")
    test_file_existence()
    test_asset_files()
    test_image_annotations()
    test_problem_counts_and_structure()
    test_pedagogical_language_rules()
    test_colon_capitalization()
    test_physics_calculations()
    print("==================================================")
    print(" ALL VERIFICATION CHECKS PASSED PERFECTLY!")
    print("==================================================")


if __name__ == "__main__":
    main()
