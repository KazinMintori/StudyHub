# -*- coding: utf-8 -*-
"""Bộ kiểm định chất lượng và tính đúng đắn độc lập cho Lab 07-regex.

Kiểm tra:
1. Định dạng văn bản và cấu trúc:
   - Đủ 20 thẻ định danh span id: data-lab-07-regex-01 đến data-lab-07-regex-20.
   - Đủ 20 khối ::: exercise và 20 khối ::: solution, đóng mở container cân đối (80 dấu :::).
   - Đúng thứ tự bắt buộc cho từng bài:
     Đề bài -> Full code 1 -> Giải thích 1 -> Output 1 -> Full code 2 -> Giải thích 2 -> Output 2 -> So sánh.
2. Quy chuẩn văn phong tiếng Việt:
   - Không chứa từ ngữ cấm theo quy ước.
   - Không chứa dấu gạch ngang dài (em dash '—' hoặc '--' trong văn xuôi).
   - Không chứa dấu chấm phẩy (';') trong văn xuôi.
   - Viết hoa chữ cái đầu tiên ngay sau dấu hai chấm (':').
3. Kiểm tra tính đầy đủ và ánh xạ trong coverage-07-regex.json:
   - Đúng 102 ô từ course notebook (không có template counterpart).
   - Ánh xạ đầy đủ đến các mã bài tương ứng.
4. Thực thi độc lập toàn bộ 40 khối code Python trong namespace trắng (fresh):
   - Không dùng biến toàn cục ẩn.
   - Kiểm định cả 2 phương pháp (solve và solve_compiled) qua toàn bộ 321 test cases.
   - Kiểm định cả 2 phương pháp qua toàn bộ 20 bài kiểm tra đoạn văn (passage).
"""

from io import StringIO
import json
from pathlib import Path
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
LAB_FILE = ROOT / "raw_materials/xu-ly-du-lieu/labs/lab-07-regex.md"
COVERAGE_FILE = ROOT / "raw_materials/xu-ly-du-lieu/labs/coverage-07-regex.json"

CASES_FILE = ROOT / "docs/public/materials/data-labs/regex-cases.json"

BANNED_WORDS = [
    "hợp đồng",
    "lấy từ giáo trình",
    "lấy từ slide",
    "lấy từ sách",
    "do người soạn thêm",
    "không gán cho tác giả",
    "khoan đã, hãy xem lại",
    "à không, thay vào đó",
    "sinh viên rất hay nhầm",
    "lỗi phổ biến nhất của sinh viên",
    "đa số sinh viên đều mắc",
    "bẫy thi cử",
    "nguyên tác",
    "tiến độ bản dịch",
    "bản dịch của"
]

def check_file_structure(content: str):
    print("--- 1. Kiểm tra cấu trúc file và thẻ định danh bài tập ---")
    required_spans = [f"data-lab-07-regex-{i:02d}" for i in range(1, 21)]
    for span in required_spans:
        assert f'id="{span}"' in content or f"id='{span}'" in content, f"Thiếu thẻ định danh {span}"
    print(f"Đã tìm thấy đủ {len(required_spans)} thẻ định danh span id.")

    exercise_count = content.count("::: exercise")
    solution_count = content.count("::: solution")
    close_count = content.count(":::")
    assert exercise_count == 20, f"Số lượng ::: exercise mong đợi 20, thực tế: {exercise_count}"
    assert solution_count == 20, f"Số lượng ::: solution mong đợi 20, thực tế: {solution_count}"
    assert close_count == exercise_count + solution_count + (20 * 2), f"Đóng mở container không khớp: {close_count}"
    print("Cấu trúc container ::: exercise và ::: solution hoàn toàn cân đối (20 bài x 2 container = 80 dấu :::).")

    # Kiểm tra thứ tự các thành phần trong từng bài
    print("Kiểm tra thứ tự các thành phần bắt buộc cho từng bài tập...")
    sections = content.split('<span id="data-lab-07-regex-')
    for i in range(1, 21):
        sec = sections[i]
        pos_exercise = sec.find("::: exercise")
        pos_code1 = sec.find("#### Cách 1: Người mới bắt đầu")
        pos_exp1 = sec.find("##### Giải thích chi tiết Cách 1:")
        pos_out1 = sec.find("##### Kết quả thực thi Cách 1:")
        pos_code2 = sec.find("#### Cách 2: Ứng dụng thực tế")
        pos_exp2 = sec.find("##### Giải thích chi tiết Cách 2:")
        pos_out2 = sec.find("##### Kết quả thực thi Cách 2:")
        pos_comp = sec.find("#### So sánh hai phương pháp:")

        assert pos_exercise != -1, f"Bài {i} thiếu khối ::: exercise"
        assert pos_code1 != -1, f"Bài {i} thiếu tiêu đề Cách 1"
        assert pos_exp1 != -1, f"Bài {i} thiếu giải thích Cách 1"
        assert pos_out1 != -1, f"Bài {i} thiếu bảng kết quả Cách 1"
        assert pos_code2 != -1, f"Bài {i} thiếu tiêu đề Cách 2"
        assert pos_exp2 != -1, f"Bài {i} thiếu giải thích Cách 2"
        assert pos_out2 != -1, f"Bài {i} thiếu bảng kết quả Cách 2"
        assert pos_comp != -1, f"Bài {i} thiếu phần so sánh hai phương pháp"

        assert pos_exercise < pos_code1 < pos_exp1 < pos_out1 < pos_code2 < pos_exp2 < pos_out2 < pos_comp, (
            f"Bài {i} vi phạm thứ tự bắt buộc: "
            f"Đề bài -> Code1 -> Giải thích1 -> Output1 -> Code2 -> Giải thích2 -> Output2 -> So sánh"
        )
    print("Toàn bộ 20 bài đều tuân thủ chính xác 100% trật tự cấu trúc nội dung bắt buộc.")

def check_prose_rules(content: str):
    print("--- 2. Kiểm tra quy chuẩn văn phong tiếng Việt học thuật ---")
    lines = content.splitlines()
    in_code_block = False

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Kiểm tra từ cấm
        lower_line = line.lower()
        for banned in BANNED_WORDS:
            assert banned not in lower_line, f"Dòng {idx} chứa từ ngữ không phù hợp '{banned}': {line}"

        # Bỏ qua dòng bảng Markdown
        if stripped.startswith("|"):
            continue

        # Bỏ qua dòng kẻ ngang và container VitePress
        if stripped == "---" or stripped.startswith(":::"):
            continue

        # Bỏ qua code span `...` khi kiểm tra gạch ngang dài
        text_without_codespans = re.sub(r"`[^`]*`", "", line)

        # Kiểm tra em dash (— hoặc --)
        assert "—" not in text_without_codespans, f"Dòng {idx} chứa dấu gạch ngang dài (em dash): {line}"
        if not stripped.startswith("- "):
            assert "--" not in text_without_codespans, f"Dòng {idx} chứa ký hiệu '--': {line}"

        # Kiểm tra dấu chấm phẩy trong văn xuôi
        cleaned_line = re.sub(r"&[a-zA-Z0-9#]+;", "", line)
        assert ";" not in cleaned_line, f"Dòng {idx} chứa dấu chấm phẩy trong văn xuôi: {line}"

        # Kiểm tra viết hoa sau dấu hai chấm
        colon_matches = re.finditer(r":\s+([a-zA-Z\u00C0-\u1EF9])", line)
        for m in colon_matches:
            char = m.group(1)
            start_pos = m.start()
            prefix = line[:start_pos]
            if "http" in prefix or "https" in prefix or prefix.count("`") % 2 == 1:
                continue
            assert char.isupper(), f"Dòng {idx} không viết hoa chữ cái sau dấu hai chấm (': {char}'): {line}"

    print("Văn phong tiếng Việt chuẩn mực: Không từ cấm, không em dash, không chấm phẩy, viết hoa sau dấu hai chấm.")

def check_coverage_json():
    print("--- 3. Kiểm tra coverage-07-regex.json ---")
    assert COVERAGE_FILE.exists(), f"Không tìm thấy file {COVERAGE_FILE}"
    with open(COVERAGE_FILE, encoding="utf-8") as f:
        data = json.load(f)

    assert data["lab"] == "07-regex", f"lab không đúng: {data['lab']}"
    assert data["course_source"] == "course/2627-1/notebooks/lab-07-regex.ipynb"
    assert "course_cells" in data
    assert len(data["course_cells"]) == 102, f"Số lượng ô mong đợi 102, thực tế: {len(data['course_cells'])}"

    # Kiểm tra các ô bài tập
    for i in range(1, 21):
        ex_id = f"data-lab-07-regex-{i:02d}"
        ex_cells = [c for c in data["course_cells"] if c.get("exercise_id") == ex_id]
        assert len(ex_cells) == 5, f"Bài {i} mong đợi 5 ô được ánh xạ trong notebook, thực tế có {len(ex_cells)}"

    print("coverage-07-regex.json hoàn toàn hợp lệ và ánh xạ trọn vẹn 102 ô.")

def extract_python_blocks(content: str):
    pattern = r"```python\r?\n(.*?)```"
    return re.findall(pattern, content, re.DOTALL)

def run_code_verifications(content: str):
    print("--- 4. Thực thi độc lập 40 khối code Python trong namespace trắng ---")
    all_blocks = extract_python_blocks(content)
    assert len(all_blocks) == 40, f"Mong đợi đúng 40 khối code (20 bài x 2 cách), tìm thấy {len(all_blocks)}"

    assert CASES_FILE.exists(), f"Không tìm thấy {CASES_FILE}"
    cases_data = json.loads(CASES_FILE.read_text(encoding="utf-8"))

    total_pair_tests = 0
    total_passage_tests = 0

    for i in range(20):
        ex_num = i + 1
        b1 = all_blocks[2 * i]
        b2 = all_blocks[2 * i + 1]

        # 1. Chạy Cách 1 trong namespace trắng
        ns1 = {}
        try:
            exec(b1, ns1)
        except Exception as e:
            raise AssertionError(f"Lỗi thực thi Cách 1 Bài {ex_num}: {e}") from e
        assert "solve" in ns1, f"Không tìm thấy hàm solve trong Cách 1 Bài {ex_num}"
        fn1 = ns1["solve"]

        # 2. Chạy Cách 2 trong namespace trắng
        ns2 = {}
        try:
            exec(b2, ns2)
        except Exception as e:
            raise AssertionError(f"Lỗi thực thi Cách 2 Bài {ex_num}: {e}") from e
        assert "solve_compiled" in ns2, f"Không tìm thấy hàm solve_compiled trong Cách 2 Bài {ex_num}"
        fn2 = ns2["solve_compiled"]

        # 3. Kiểm định qua toàn bộ test cases từ regex-cases.json
        ex_cases = cases_data["exercises"][i]["cases"]
        for case in ex_cases:
            inp = case["input"]
            exp = case["expected"]
            exp_type = case["expectedType"]
            if exp_type == "tuple" and isinstance(exp, list):
                exp = tuple(exp)

            # Kiểm tra Cách 1
            act1 = fn1(inp)
            assert act1 == exp, f"Bài {ex_num} Cách 1 sai giá trị trên {inp!r}: mong đợi {exp!r}, nhận {act1!r}"
            assert type(act1).__name__ == exp_type, (
                f"Bài {ex_num} Cách 1 sai kiểu dữ liệu trên {inp!r}: "
                f"mong đợi {exp_type}, nhận {type(act1).__name__}"
            )

            # Kiểm tra Cách 2
            act2 = fn2(inp)
            assert act2 == exp, f"Bài {ex_num} Cách 2 sai giá trị trên {inp!r}: mong đợi {exp!r}, nhận {act2!r}"
            assert type(act2).__name__ == exp_type, (
                f"Bài {ex_num} Cách 2 sai kiểu dữ liệu trên {inp!r}: "
                f"mong đợi {exp_type}, nhận {type(act2).__name__}"
            )
            total_pair_tests += 1

        # Input and expected output are plain data, without notebook grading code.
        passage_case = cases_data["exercises"][i]
        for function in [fn1, fn2]:
            selected = []
            for item in re.findall(r"«([^»]*)»", passage_case["passage"]):
                value = function(item)
                if value is not None and value is not False:
                    selected.append((item, value))
            assert json.loads(json.dumps(selected)) == passage_case["selected"]
        total_passage_tests += 1

    print(f"Toàn bộ 40 khối code đã chạy độc lập hoàn hảo.")
    print(f"Tổng số ca kiểm thử độc lập đã vượt qua: {total_pair_tests} ca dữ liệu đối chiếu.")
    print(f"Tổng số bài kiểm tra đoạn văn đã vượt qua: {total_passage_tests} đoạn văn.")
    print("Cả hai phương pháp giải (trực tiếp và biên dịch mẫu) đều cho kết quả trùng khớp 100%.")

def main():
    print("=== BẮT ĐẦU BỘ KIỂM ĐỊNH LAB 07-REGEX ===")
    assert LAB_FILE.exists(), f"Không tìm thấy file bài lab: {LAB_FILE}"
    content = LAB_FILE.read_text(encoding="utf-8")

    check_file_structure(content)
    check_prose_rules(content)
    check_coverage_json()
    run_code_verifications(content)

    print("\n=== TỔNG KẾT: TẤT CẢ PHÉP KIỂM ĐỊNH LAB 07-REGEX ĐỀU ĐẠT CHUẨN 100% ===")

if __name__ == "__main__":
    main()
