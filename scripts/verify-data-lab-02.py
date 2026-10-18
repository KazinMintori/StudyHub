"""Bộ kiểm định chất lượng và tính đúng đắn cho Lab 02.

Kiểm tra:
1. Định dạng văn bản: span id, ::: exercise, ::: solution, bảng Markdown.
2. Quy chuẩn văn phong: không em dash, không dấu chấm phẩy văn xuôi, viết hoa sau dấu hai chấm.
3. Không dùng từ cấm: 'hợp đồng', 'lấy từ giáo trình', 'lấy từ slide', 'phòng thủ'.
4. RÀNG BUỘC TUYỆT ĐỐI PYTHON THUẦN: không import pandas, không import numpy trong toàn bộ mã nguồn.
5. Thực thi tuần tự toàn bộ code blocks Markdown từ trên xuống dưới, kiểm tra tính đầy đủ của biến và các ca biên.
"""

import csv
from io import StringIO
import json
from pathlib import Path
import re
import sys
import tempfile

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
LAB_FILE = ROOT / "raw_materials/xu-ly-du-lieu/labs/lab-02.md"
COVERAGE_FILE = ROOT / "raw_materials/xu-ly-du-lieu/labs/coverage-02.json"

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
    required_spans = [f"data-lab-02-{i:02d}" for i in range(1, 16)]
    for span in required_spans:
        assert f'id="{span}"' in content or f"id='{span}'" in content, f"Thiếu thẻ định danh {span}"
    print(f"Đã tìm thấy đủ {len(required_spans)} thẻ định danh span id.")

    exercise_count = content.count("::: exercise")
    solution_count = content.count("::: solution")
    close_count = content.count(":::")
    assert exercise_count == 15, f"Số lượng ::: exercise mong đợi 15, thực tế: {exercise_count}"
    assert solution_count == 15, f"Số lượng ::: solution mong đợi 15, thực tế: {solution_count}"
    assert close_count == exercise_count + solution_count + (15 * 2), f"Đóng mở container không khớp: {close_count}"
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

        # Bỏ qua dòng bảng Markdown, dòng kẻ ngang Markdown và container VitePress
        if stripped.startswith("|") or stripped == "---" or stripped.startswith(":::"):
            continue

        # Kiểm tra từ cấm
        lower_line = line.lower()
        for banned in BANNED_WORDS:
            assert banned not in lower_line, f"Dòng {idx} chứa từ ngữ không phù hợp '{banned}': {line}"

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

def check_pure_python_constraint(blocks: list[str]):
    print("--- 3. Kiểm tra ràng buộc Python thuần (Pure Python Constraint) ---")
    for idx, block in enumerate(blocks, start=1):
        assert "import pandas" not in block and "pd." not in block, f"Khối code {idx} vi phạm ràng buộc: dùng pandas"
        assert "import numpy" not in block and "np." not in block, f"Khối code {idx} vi phạm ràng buộc: dùng numpy"
    print(f"Đạt chuẩn tuyệt đối: Tất cả {len(blocks)} khối code đều chỉ sử dụng thư viện chuẩn Python!")

def run_code_verifications(content: str):
    print("--- 4. Thực thi tuần tự toàn bộ 31 code blocks Markdown trên môi trường tạm ---")
    all_blocks = extract_python_blocks(content)
    print(f"Tổng số khối code Python tìm thấy: {len(all_blocks)}")
    assert len(all_blocks) == 31, f"Mong đợi đúng 31 khối code (1 DEMO_CSV + 15 bài x 2 cách), tìm thấy {len(all_blocks)}"

    check_pure_python_constraint(all_blocks)

    previous_dir = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="studyhub-test-lab02-") as tmp_dir:
        import os
        os.chdir(tmp_dir)
        try:
            namespace = {"__name__": "__main__"}
            for idx, block in enumerate(all_blocks, start=1):
                try:
                    exec(block, namespace)
                except Exception as exc:
                    raise AssertionError(f"Lỗi thực thi khối code {idx}: {type(exc).__name__}: {exc}") from exc

            # Kiểm tra các biến và kết quả chạy tuần tự
            assert "DEMO_CSV" in namespace
            assert namespace["ket_qua"] == "Giá TB: 118,200 CLP"
            assert namespace["ty_le_chu"] == "17.8%"
            assert namespace["gia_co"] == [52000, 78000, 0]
            assert round(namespace["tb"], 1) == 43333.3
            assert namespace["bien_mat"] == {101, 103}
            assert namespace["moi_them"] == {105}

            # Kiểm tra rows được nạp đầy đủ từ Bài 4
            assert "rows" in namespace, "Biến 'rows' phải được định nghĩa sau Bài 4"
            assert len(namespace["rows"]) == 6
            assert namespace["rows"][0]["name"] == "Phong A"

            # Kiểm tra to_float và làm sạch cột giá
            assert namespace["so_thieu"] == 1
            assert len(namespace["gia_hop_le"]) == 5
            assert namespace["gia_hop_le"] == [100.0, 50.0, 150.0, 0.0, 300.0]

            # Kiểm tra summarize_prices
            tom_tat = namespace["tom_tat_gia_c1"]
            assert tom_tat == {"n_valid": 5, "n_missing": 1, "mean": 120.0, "median": 100.0}

            # Kiểm tra most_expensive
            assert namespace["id_dat_nhat_c1"] == "6"
            assert namespace["id_dat_nhat_c2"] == "6"

            # Kiểm tra count_by_area
            assert namespace["dem_khu_vuc_c1"] == {"Centro": 2, "Norte": 2, "Sur": 2}

            # Kiểm tra median_by_area
            trung_vi_khu = namespace["trung_vi_khu_c1"]
            assert trung_vi_khu["Centro"] == 75.0
            assert trung_vi_khu["Norte"] == 150.0
            assert trung_vi_khu["Sur"] == 150.0

            # Kiểm tra review_qa
            qa = namespace["ket_qua_qa_c1"]
            assert qa == {"n_zero": 2, "n_inconsistent": 0}

            # Kiểm tra JSON save/load round-trip
            assert Path("report_santiago.json").exists()
            assert Path("report_santiago_p.json").exists()
            assert namespace["bao_cao_doc_lai_c1"]["thanh_pho"] == "Santiago"
            assert namespace["bao_cao_doc_lai_c2"]["so_phong"] == 6

            # Kiểm tra rank_areas
            ranks = namespace["xep_hang_c1"]
            assert len(ranks) == 2
            assert ranks[0]["neighbourhood"] == "Sur" and ranks[0]["median_price"] == 150.0
            assert ranks[1]["neighbourhood"] == "Centro" and ranks[1]["median_price"] == 75.0

            # Kiểm tra review_counts_by_year
            years = namespace["nam_danh_gia_c1"]
            assert years == {"2025": 1, "2026": 2}

            # Kiểm tra đánh giá thời gian
            assert namespace["ket_qua_danh_gia"]["ket_luan_hop_le"] is False

            # --- KIỂM ĐỊNH MỞ RỘNG CÁC CA BIÊN ĐỘC LẬP ---
            f_clean = namespace["clean_price_column"]
            clean_res = f_clean(namespace["rows"])
            assert clean_res["n_missing"] == 1
            assert len(clean_res["valid_prices"]) == 5

            # Kiểm tra most_expensive hòa điểm ổn định (lấy phần tử đầu tiên)
            tie_records = [{"id": "x", "price": 50.0}, {"id": "y", "price": 50.0}]
            assert namespace["most_expensive"](tie_records) == "x"
            assert namespace["most_expensive"]([]) is None
            assert namespace["most_expensive"]([{"id": "z", "price": None}]) is None

            # Kiểm tra rank_areas hòa điểm sắp xếp theo bảng chữ cái A-Z
            tie_rank = [
                {"neighbourhood": "Khu B", "price": 20.0},
                {"neighbourhood": "Khu B", "price": 20.0},
                {"neighbourhood": "Khu A", "price": 20.0},
                {"neighbourhood": "Khu A", "price": 20.0}
            ]
            r_tie = namespace["rank_areas"](tie_rank, min_valid=2)
            assert [x["neighbourhood"] for x in r_tie] == ["Khu A", "Khu B"]
            assert namespace["rank_areas"]([], min_valid=1) == []

            # Kiểm tra header-only CSV
            with open("header_only.csv", "w", encoding="utf-8") as f:
                f.write("id,name,price\n")
            assert namespace["read_listings"]("header_only.csv") == []

        finally:
            os.chdir(previous_dir)

    print("Toàn bộ 31 khối code Python thuần đều chạy trơn tru và đạt 100% assertions!")

def check_coverage_json():
    print("--- 5. Kiểm tra file coverage-02.json ---")
    assert COVERAGE_FILE.exists(), f"Không tìm thấy file {COVERAGE_FILE}"
    data = json.loads(COVERAGE_FILE.read_text(encoding="utf-8"))
    assert "template_cells" in data, "Thiếu trường template_cells"
    assert "course_cells" in data, "Thiếu trường course_cells"
    assert len(data["template_cells"]) == 53, f"Template có 53 cell (0-52), ghi nhận: {len(data['template_cells'])}"
    assert len(data["course_cells"]) == 40, f"Course có 40 cell (0-39), ghi nhận: {len(data['course_cells'])}"
    print(f"Coverage JSON đầy đủ: {len(data['template_cells'])} template cells và {len(data['course_cells'])} course cells.")

def main():
    print(f"=== BẮT ĐẦU KIỂM ĐỊNH LAB 02 ({LAB_FILE.name}) ===")
    assert LAB_FILE.exists(), f"Không tìm thấy file {LAB_FILE}"
    content = LAB_FILE.read_text(encoding="utf-8")
    check_file_structure(content)
    check_prose_rules(content)
    run_code_verifications(content)
    check_coverage_json()
    print("=== TOÀN BỘ KIỂM ĐỊNH LAB 02 ĐẠT 100% ===")

if __name__ == "__main__":
    main()
