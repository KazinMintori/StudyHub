"""Bộ kiểm định chất lượng và tính đúng đắn cho Lab 07.

Kiểm tra:
1. Định dạng văn bản: span id, ::: exercise, ::: solution, bảng Markdown.
2. Quy chuẩn văn phong: không em dash, không dấu chấm phẩy văn xuôi, viết hoa sau dấu hai chấm.
3. Không dùng từ cấm: 'hợp đồng', 'lấy từ giáo trình', 'lấy từ slide', 'phòng thủ', v.v.
4. Thực thi tuần tự toàn bộ 31 code blocks từ Markdown trên môi trường thực tế, kiểm tra đầu ra và các ca biên.
5. Kiểm tra tính đầy đủ và ánh xạ chính xác trong coverage-07.json.
"""

from io import StringIO
import json
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
LAB_FILE = ROOT / "raw_materials/xu-ly-du-lieu/labs/lab-07.md"
COVERAGE_FILE = ROOT / "raw_materials/xu-ly-du-lieu/labs/coverage-07.json"

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
    required_spans = [f"data-lab-07-{i:02d}" for i in range(1, 16)]
    for span in required_spans:
        assert f'id="{span}"' in content or f"id='{span}'" in content, f"Thiếu thẻ định danh {span}"
    print(f"Đã tìm thấy đủ {len(required_spans)} thẻ định danh span id.")

    exercise_count = content.count("::: exercise")
    solution_count = content.count("::: solution")
    close_count = content.count(":::")
    assert exercise_count == 15, f"Số lượng ::: exercise mong đợi 15, thực tế: {exercise_count}"
    assert solution_count == 15, f"Số lượng ::: solution mong đợi 15, thực tế: {solution_count}"
    assert close_count == exercise_count + solution_count + (15 * 2), f"Đóng mở container không khớp: {close_count}"
    print("Cấu trúc container ::: exercise và ::: solution hoàn toàn cân đối (15 bài x 2 container = 30 cặp đóng mở).")

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
    assert len(all_blocks) == 31, f"Mong đợi đúng 31 khối code (1 fixture + 15 bài x 2 cách), tìm thấy {len(all_blocks)}"

    # Chạy tuần tự từ trên xuống dưới trong cùng một namespace như người đọc
    namespace = {"__name__": "__main__", "display": lambda *objects, **kwargs: None}
    for idx, block in enumerate(all_blocks, start=1):
        try:
            exec(block, namespace)
        except Exception as exc:
            raise AssertionError(f"Lỗi thực thi khối code {idx}: {exc}") from exc

    # 1. Kiểm tra Bài 1: normalize
    assert "normalize" in namespace
    fn_norm = namespace["normalize"]
    s_test = pd.Series(["  Wifi ", "wifi", "WIFI!", "wi-fi"])
    res1 = fn_norm(s_test)
    assert list(res1) == ["wifi", "wifi", "wifi!", "wi-fi"]
    assert (res1 == "wifi").sum() == 2
    assert fn_norm(pd.Series([" A ", None])).isna().tolist() == [False, True]
    assert list(s_test) == ["  Wifi ", "wifi", "WIFI!", "wi-fi"], "Không thay đổi Series gốc"

    # 2. Kiểm tra Bài 2: count_contains
    assert "count_contains" in namespace
    fn_count_contains = namespace["count_contains"]
    t_test = pd.Series(["depto centro", None, "casa con vista"])
    assert fn_count_contains(t_test, "centro") == 1
    assert fn_count_contains(t_test, "Centro") == 0
    assert fn_count_contains(pd.Series(["giá 50.000", "giá 50,000"]), "50.000") == 1

    # 3. Kiểm tra Bài 3: parse_price
    assert "parse_price" in namespace
    fn_price = namespace["parse_price"]
    df_p = fn_price(namespace["DEMO_PRICES"])
    assert isinstance(df_p, pd.DataFrame)
    assert set(df_p.columns) == {"gia", "gia_so", "loi_doc"}
    assert df_p["gia_so"].iloc[:2].tolist() == [1200.0, 850.0]
    assert df_p["gia_so"].iloc[2:].isna().all()
    assert df_p["loi_doc"].tolist() == [False, False, False, True, True]

    # 4. Kiểm tra Bài 4: validate_price_fullmatch
    assert "validate_price_fullmatch" in namespace
    fn_val_price = namespace["validate_price_fullmatch"]
    res_val = fn_val_price(namespace["DEMO_PRICES_TEST"])
    assert res_val.tolist() == [True, True, False, False, False, False]

    # 5. Kiểm tra Bài 5: text_overview
    assert "text_overview" in namespace
    fn_overview = namespace["text_overview"]
    res_ov = fn_overview(namespace["DEMO_COMMENTS"], 20)
    assert res_ov == {"so_nan": 1, "so_con": 15, "do_dai_tv": 39.0, "so_ngan": 3}
    assert fn_overview(namespace["DEMO_COMMENTS"], 40)["so_ngan"] == 8

    # 6. Kiểm tra Bài 6: clean_br
    assert "clean_br" in namespace
    fn_clean_br = namespace["clean_br"]
    res_br = fn_clean_br(namespace["DEMO_COMMENTS"])
    assert res_br["so_br"] == 3
    assert int(res_br["c_sach"].str.contains("<br/>", regex=False, na=False).sum()) == 0
    assert res_br["c_sach"].iloc[6] == "Nice host. Near Movistar Arena! Recommended."
    assert res_br["c_sach"].isna().sum() == 1

    # 7. Kiểm tra Bài 7: language_flag
    assert "language_flag" in namespace
    fn_lang = namespace["language_flag"]
    c_sach_demo = namespace["DEMO_COMMENTS"].dropna().str.replace("<br/>", " ", regex=False)
    res_lang = fn_lang(c_sach_demo)
    assert isinstance(res_lang["la_es"], pd.Series)
    assert res_lang["la_es"].sum() == 7
    assert round(res_lang["ty_le_es"], 3) == 0.467

    # 8. Kiểm tra Bài 8: median_length_by_flag
    assert "median_length_by_flag" in namespace
    fn_med_len = namespace["median_length_by_flag"]
    res_med = fn_med_len(c_sach_demo, res_lang["la_es"])
    assert res_med == {"len_es": 47.0, "len_khac": 34.5}

    # 9. Kiểm tra Bài 9: extract_near
    assert "extract_near" in namespace
    fn_extract = namespace["extract_near"]
    c_sach_full = namespace["DEMO_COMMENTS"].str.replace("<br/>", " ", regex=False)
    res_extr = fn_extract(c_sach_full)
    assert res_extr["so_trich"] == 9
    assert res_extr["gan"].iloc[0] == "metro"
    assert res_extr["gan"].iloc[5] == "todo"
    assert res_extr["gan"].iloc[15] == "Movistar"

    # 10. Kiểm tra Bài 10: top_places
    assert "top_places" in namespace
    fn_top_places = namespace["top_places"]
    gan_demo = pd.Series(["metro", "Metro", None, "todo", "estación", "metro", "Movistar", "muchos", "movistar"])
    res_top = fn_top_places(gan_demo, n=2, bo_qua=("todo", "muchos"))
    assert dict(res_top) == {"metro": 3, "movistar": 2}

    # 11. Kiểm tra Bài 11: parse_amenities_explode
    assert "parse_amenities_explode" in namespace
    fn_parse_amenities = namespace["parse_amenities_explode"]
    ds_res, muc_res = fn_parse_amenities(namespace["DEMO_LISTINGS"])
    assert len(ds_res) == 5
    assert ds_res.map(type).eq(list).all()
    assert muc_res.str.contains(",", regex=False).any()
    assert muc_res.eq("Wifi").sum() == 1

    # 12. Kiểm tra Bài 12: calculate_amenity_rate
    assert "calculate_amenity_rate" in namespace
    fn_calc_amenity = namespace["calculate_amenity_rate"]
    res_amenity_rate = fn_calc_amenity(namespace["DEMO_LISTINGS"], "Wifi")
    assert res_amenity_rate["so_cho_o_co"] == 1
    assert res_amenity_rate["tong_cho_o"] == 5
    assert abs(res_amenity_rate["ty_le"] - 0.2) < 1e-12

    # 13. Kiểm tra Bài 13: analyze_amenity_completeness
    assert "analyze_amenity_completeness" in namespace
    fn_comp = namespace["analyze_amenity_completeness"]
    res_comp = fn_comp(namespace["DEMO_DS_NHO"], "Wifi")
    assert res_comp["so_da_biet"] == 4
    assert res_comp["so_khuyet"] == 1
    assert abs(res_comp["ty_le_da_biet"] - 0.5) < 1e-12

    # 14. Kiểm tra Bài 14: multilingual_keyword_signals
    assert "multilingual_keyword_signals" in namespace
    fn_signals = namespace["multilingual_keyword_signals"]
    df_sig_res = fn_signals(c_sach_demo, res_lang["la_es"])
    assert isinstance(df_sig_res, pd.DataFrame)
    assert len(df_sig_res) == 2
    assert set(df_sig_res.columns) == {"tin_hieu", "ty_le_nhom_es", "ty_le_nhom_khac"}

    # 15. Kiểm tra Bài 15: extract_area
    assert "extract_area" in namespace
    fn_area = namespace["extract_area"]
    mau_phong_test = pd.Series([
        "Căn hộ 45 m2 thoáng mát",
        "Phòng 30m² trung tâm",
        "Studio 45.5 m2 sạch sẽ",
        "Chỗ ở 45,5 m² đẹp",
        "Mã phòng 30m2x không nhận",
        "Không ghi diện tích"
    ])
    res_area = fn_area(mau_phong_test)
    assert res_area.iloc[:4].tolist() == [45.0, 30.0, 45.5, 45.5]
    assert res_area.iloc[4:].isna().all()

    print("Tất cả 31 khối code đều thực thi chính xác và đạt 100% assertions độc lập!")

def check_coverage_json():
    print("--- 4. Kiểm tra file coverage-07.json ---")
    assert COVERAGE_FILE.exists(), f"Không tìm thấy file {COVERAGE_FILE}"
    data = json.loads(COVERAGE_FILE.read_text(encoding="utf-8"))
    assert "template_cells" in data, "Thiếu trường template_cells"
    assert "course_cells" in data, "Thiếu trường course_cells"
    assert len(data["template_cells"]) == 43, f"Template có 43 cell (0-42), ghi nhận: {len(data['template_cells'])}"
    assert len(data["course_cells"]) == 41, f"Course có 41 cell (0-40), ghi nhận: {len(data['course_cells'])}"

    # Kiểm tra mỗi cell đều có status và reason hợp lệ
    for cell in data["template_cells"]:
        assert cell["status"] in {"included", "excluded"}
        assert len(cell["reason"].strip()) > 0
    for cell in data["course_cells"]:
        assert cell["status"] in {"included", "excluded"}
        assert len(cell["reason"].strip()) > 0

    print(f"Coverage JSON đầy đủ: {len(data['template_cells'])} template cells và {len(data['course_cells'])} course cells.")

def main():
    print(f"=== BẮT ĐẦU KIỂM ĐỊNH LAB 07 ({LAB_FILE.name}) ===")
    assert LAB_FILE.exists(), f"Không tìm thấy file {LAB_FILE}"
    content = LAB_FILE.read_text(encoding="utf-8")
    check_file_structure(content)
    check_prose_rules(content)
    run_code_verifications(content)
    check_coverage_json()
    print("=== TOÀN BỘ KIỂM ĐỊNH LAB 07 ĐẠT 100% ===")

if __name__ == "__main__":
    main()
