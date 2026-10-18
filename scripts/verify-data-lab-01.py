"""Bộ kiểm định chất lượng và tính đúng đắn cho Lab 01.

Kiểm tra:
1. Định dạng văn bản: span id, ::: exercise, ::: solution, bảng Markdown.
2. Quy chuẩn văn phong: không em dash, không dấu chấm phẩy văn xuôi, viết hoa sau dấu hai chấm.
3. Không dùng từ cấm: 'hợp đồng', 'lấy từ giáo trình', 'lấy từ slide', 'phòng thủ'.
4. Thực thi tuần tự toàn bộ code blocks từ Markdown trên môi trường thực tế, kiểm tra đầu ra và các ca biên.
"""

from io import StringIO
from pathlib import Path
import re
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
LAB_FILE = ROOT / "raw_materials/xu-ly-du-lieu/labs/lab-01.md"
COVERAGE_FILE = ROOT / "raw_materials/xu-ly-du-lieu/labs/coverage-01.json"

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
    print("--- 1. Kiểm tra cấu trúc file và thẻ bài tập ---")
    required_spans = [f"data-lab-01-{i:02d}" for i in range(1, 8)]
    for span in required_spans:
        assert f'id="{span}"' in content or f"id='{span}'" in content, f"Thiếu thẻ định danh {span}"
    print(f"Đã tìm thấy đủ {len(required_spans)} thẻ định danh span id.")

    exercise_count = content.count("::: exercise")
    solution_count = content.count("::: solution")
    close_count = content.count(":::")
    assert exercise_count == 7, f"Số lượng ::: exercise mong đợi 7, thực tế: {exercise_count}"
    assert solution_count == 7, f"Số lượng ::: solution mong đợi 7, thực tế: {solution_count}"
    assert close_count == exercise_count + solution_count + (7 * 2), f"Đóng mở container không khớp: {close_count}"
    print("Cấu trúc container ::: exercise và ::: solution hoàn toàn cân đối.")

def check_prose_rules(content: str):
    print("--- 2. Kiểm tra quy tắc văn phong tiếng Việt ---")
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

        # Bỏ qua dòng kẻ ngang Markdown và container VitePress
        if stripped == "---" or stripped.startswith(":::"):
            continue

        # Kiểm tra em dash (— hoặc --)
        assert "—" not in line, f"Dòng {idx} chứa dấu gạch ngang dài (em dash): {line}"
        if not stripped.startswith("- "):
            assert "--" not in line, f"Dòng {idx} chứa ký hiệu '--': {line}"

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

    print("Văn phong tiếng Việt chuẩn mực: Không em dash, không dấu chấm phẩy, viết hoa sau dấu hai chấm.")

def extract_python_blocks(content: str):
    pattern = r"```python\r?\n(.*?)```"
    return re.findall(pattern, content, re.DOTALL)

def run_code_verifications(content: str):
    print("--- 3. Thực thi tuần tự toàn bộ code blocks Markdown ---")
    all_blocks = extract_python_blocks(content)
    print(f"Tổng số khối code Python tìm thấy: {len(all_blocks)}")
    assert len(all_blocks) == 15, f"Mong đợi đúng 15 khối code (1 DEMO_CSV + 7 bài x 2 cách), tìm thấy {len(all_blocks)}"

    # Chạy tuần tự từ trên xuống dưới trong cùng một namespace như người đọc
    namespace = {"__name__": "__main__", "plt": plt}
    for idx, block in enumerate(all_blocks, start=1):
        try:
            exec(block, namespace)
        except Exception as exc:
            raise AssertionError(f"Lỗi thực thi khối code {idx}: {exc}") from exc

    # Kiểm tra biến và hàm sau khi chạy tuần tự
    assert "DEMO_CSV" in namespace
    assert namespace.get("so_phong_gia_dinh") == 4
    assert "safe_access_variable" in namespace
    assert namespace["safe_access_variable"]("so_phong_chua_co", {}) is None
    assert namespace["safe_access_variable"]("so_phong_gia_dinh", {"so_phong_gia_dinh": 4}) == 4

    assert namespace.get("du_doan_3_lan") == 3
    assert namespace.get("du_doan_run_all") == 1
    assert "simulate_counter" in namespace
    assert namespace["simulate_counter"](3) == 3
    assert namespace["simulate_counter"](1) == 1

    assert namespace.get("so_dong") == 6
    assert namespace.get("loai_nhieu_nhat") == "Entire home/apt"
    assert "get_table_profile" in namespace
    sample_df = namespace["ds"]
    profile = namespace["get_table_profile"](sample_df, "room_type")
    assert profile["total_rows"] == 6
    assert profile["top_category"] == "Entire home/apt"
    empty_profile = namespace["get_table_profile"](sample_df.iloc[:0], "room_type")
    assert empty_profile["total_rows"] == 0
    assert empty_profile["top_category"] is None

    ty_le = namespace.get("ty_le")
    assert isinstance(ty_le, pd.Series)
    assert ty_le["Entire home/apt"] == 66.7
    assert ty_le["Private room"] == 33.3
    assert "calculate_percentages" in namespace
    ty_le_chuan = namespace["calculate_percentages"](namespace["dem_loai"])
    pd.testing.assert_series_equal(ty_le, ty_le_chuan)

    # Bài 6 (E1): analyze_question
    assert "analyze_question" in namespace
    res = namespace["analyze_question"](sample_df)
    assert isinstance(res, dict) and set(res) == {"question", "table", "unit"}
    assert isinstance(res["table"], pd.DataFrame)
    assert len(res["table"].columns) >= 1
    assert res["table"].columns.is_unique
    # Kiểm tra không thay đổi bảng gốc
    sample_copy = sample_df.copy(deep=True)
    namespace["analyze_question"](sample_df)
    pd.testing.assert_frame_equal(sample_df, sample_copy)
    # Kiểm tra ca biên rỗng
    empty_res = namespace["analyze_question"](sample_df.iloc[:0])
    assert empty_res["table"].empty
    assert list(empty_res["table"].columns) == list(res["table"].columns)

    # Bài 7: kiem_tra_hoat_dong
    assert "df_so_sanh" in namespace
    assert "kiem_tra_hoat_dong" in namespace
    qa_res = namespace["kiem_tra_hoat_dong"](sample_df)
    assert qa_res["tong_phong"] == 6
    assert qa_res["so_phong_chua_danh_gia"] == 2
    assert qa_res["ty_le_chua_danh_gia"] == 33.3
    assert namespace["kiem_tra_hoat_dong"](sample_df.iloc[:0]) == {"tong_phong": 0, "ty_le_chua_danh_gia": 0.0}

    plt.close("all")
    print("Tất cả 15 khối code đều thực thi chính xác và đạt 100% assertions!")

def check_coverage_json():
    print("--- 4. Kiểm tra file coverage-01.json ---")
    assert COVERAGE_FILE.exists(), f"Không tìm thấy file {COVERAGE_FILE}"
    import json
    data = json.loads(COVERAGE_FILE.read_text(encoding="utf-8"))
    assert "template_cells" in data, "Thiếu trường template_cells"
    assert "course_cells" in data, "Thiếu trường course_cells"
    assert len(data["template_cells"]) == 42, f"Template có 42 cell (0-41), ghi nhận: {len(data['template_cells'])}"
    assert len(data["course_cells"]) == 30, f"Course có 30 cell (0-29), ghi nhận: {len(data['course_cells'])}"
    print(f"Coverage JSON đầy đủ: {len(data['template_cells'])} template cells và {len(data['course_cells'])} course cells.")

def main():
    print(f"=== BẮT ĐẦU KIỂM ĐỊNH LAB 01 ({LAB_FILE.name}) ===")
    assert LAB_FILE.exists(), f"Không tìm thấy file {LAB_FILE}"
    content = LAB_FILE.read_text(encoding="utf-8")
    check_file_structure(content)
    check_prose_rules(content)
    run_code_verifications(content)
    check_coverage_json()
    print("=== TOÀN BỘ KIỂM ĐỊNH LAB 01 ĐẠT 100% ===")

if __name__ == "__main__":
    main()
