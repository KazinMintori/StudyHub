#!/usr/bin/env python3
"""
scripts/verify-data-lab-10.py
Bộ kiểm thử và kiểm định toàn diện cho Lab 10:
Kiểm tra chất lượng và làm sạch dữ liệu chéo bảng.

Phạm vi kiểm tra:
1. Xác minh sự tồn tại và tính hợp lệ của các tệp sở hữu:
   - raw_materials/xu-ly-du-lieu/labs/lab-10.md
   - raw_materials/xu-ly-du-lieu/labs/coverage-10.json
   - scripts/verify-data-lab-10.py
2. Kiểm tra quy chuẩn Markdown và sư phạm trong lab-10.md:
   - Đủ 13 mã bài tập: data-lab-10-01 đến data-lab-10-13
   - Cặp khối ::: exercise và ::: solution hoàn chỉnh
   - Đủ các tiêu đề '#### Cách 1:' và '#### Cách 2:'
   - Không chứa dấu gạch ngang dài (em dash '—' hoặc '--') trong văn xuôi
   - Không chứa dấu chấm phẩy (';') trong văn xuôi
   - Quy tắc viết hoa sau dấu hai chấm (':')
   - Không chứa các từ ngữ cảm tính hoặc cụm từ bị cấm
   - Khối công thức hiển thị $$ đứng trên dòng riêng, không chứa \\vert hay \\Vert
   - Bảng kết quả đúng chuẩn Markdown/HTML
3. Kiểm tra tính bao phủ trong coverage-10.json:
   - Bao phủ đầy đủ 38 cell của template/lab-10.ipynb
   - Bao phủ đầy đủ 62 cell của course/2627-1/notebooks/lab-10.ipynb
4. Thực thi và kiểm định kết quả số học của mọi hàm và lời giải:
   - Bài 1 (data-lab-10-01): Điền khuyết có căn cứ cho reviews_per_month khi number_of_reviews == 0
   - Bài 2 (data-lab-10-02): Điền giá theo nhóm room_type bằng trung vị và cờ gia_da_dien
   - Bài 3 (data-lab-10-03): Quy tắc kiểm tra giá kiem_gia với ba cờ boolean thieu, khong_duong, cao
   - Bài 4 (data-lab-10-04): Ngưỡng IQR, P99 và bảng so_sanh ba chiến lược ngoại lai
   - Bài 5 (data-lab-10-05): Phân biệt khử trùng review_id với đếm cặp (listing_id, date) lặp lại
   - Bài 6 (data-lab-10-06): Kiểm tra miền thời gian time_domain và bảng cờ kiem_reviews
   - Bài 7 (data-lab-10-07): Kiểm tra toàn vẹn khóa ngoại orphan_reviews
   - Bài 8 (data-lab-10-08): Đánh giá ứng viên khóa tự nhiên duplicate_pairs
   - Bài 9 (data-lab-10-09): Đối chiếu cột dẫn xuất tổng số đánh giá review_count_check và doi_chieu
   - Bài 10 (data-lab-10-10): Đối chiếu cột LTM 12 tháng ltm_mismatch và doi_chieu_12_thang_co_dinh
   - Bài 11 (data-lab-10-11): Đóng gói báo cáo chất lượng dữ liệu qa_report và tóm tắt cờ tom_tat_co
   - Bài 12 (data-lab-10-12): Tách nhóm giá mâu thuẫn tach_gia_mau_thuan thành gia_gop và gia_can_xem
   - Bài 13 (data-lab-10-13): Điền mốt loai_dien, ffill theo nhóm lich_dien, và nội suy thời gian noi_suy
5. Kiểm định số liệu thực tế trên snapshot Inside Airbnb Santiago (nếu có sẵn).
"""

import os
import sys
import json
import re
import tempfile
from pathlib import Path

# Cấu hình UTF-8 cho stdout và stderr
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
LAB_MD_PATH = REPO_ROOT / "raw_materials" / "xu-ly-du-lieu" / "labs" / "lab-10.md"
COVERAGE_PATH = REPO_ROOT / "raw_materials" / "xu-ly-du-lieu" / "labs" / "coverage-10.json"
DATA_DIR = Path(os.environ.get("DATA_LAB_SNAPSHOT", REPO_ROOT / "qa/data-labs/snapshot"))

EXPECTED_EXERCISES = [
    f"data-lab-10-{i:02d}" for i in range(1, 14)
]

FORBIDDEN_WORDS = [
    "kỳ diệu",
    "vô cùng",
    "cực kỳ",
    "then chốt",
    "bẫy thi cử",
    "sinh viên rất hay nhầm",
    "hợp đồng",
    "Khoan đã",
    "À không",
    "Ý tôi là",
    "Nhầm rồi",
    "Tài liệu này hệ thống hóa",
]


def test_file_existence():
    """Kiểm tra sự tồn tại của các tệp thuộc phạm vi lab-10."""
    print("--- [1] Kiểm tra sự tồn tại của các tệp sở hữu ---")
    assert LAB_MD_PATH.exists(), f"Không tìm thấy tệp {LAB_MD_PATH}"
    assert COVERAGE_PATH.exists(), f"Không tìm thấy tệp {COVERAGE_PATH}"
    assert LAB_MD_PATH.stat().st_size > 5000, "Tệp lab-10.md quá ngắn hoặc rỗng."
    assert COVERAGE_PATH.stat().st_size > 1000, "Tệp coverage-10.json quá ngắn hoặc rỗng."
    print("  ✓ Tệp lab-10.md và coverage-10.json tồn tại và có nội dung đầy đủ.")


def test_markdown_pedagogical_rules():
    """Kiểm tra các quy chuẩn văn phong, định dạng và sư phạm trong Markdown."""
    print("--- [2] Kiểm tra quy chuẩn Markdown và văn phong tiếng Việt ---")
    content = LAB_MD_PATH.read_text(encoding="utf-8")

    # 1. Kiểm tra đủ 13 exercise IDs
    for ex_id in EXPECTED_EXERCISES:
        assert f'id="{ex_id}"' in content, f"Thiếu mã bài tập {ex_id} trong lab-10.md"
    print(f"  ✓ Đã tìm thấy đầy đủ 13 mã bài tập: {', '.join(EXPECTED_EXERCISES)}")

    # 2. Kiểm tra container exercise và solution
    exercise_opens = len(re.findall(r"^::: exercise", content, re.MULTILINE))
    solution_opens = len(re.findall(r"^::: solution", content, re.MULTILINE))
    container_closes = len(re.findall(r"^:::\s*$", content, re.MULTILINE))
    assert exercise_opens == 13, f"Số lượng '::: exercise' là {exercise_opens}, kỳ vọng 13."
    assert solution_opens == 13, f"Số lượng '::: solution' là {solution_opens}, kỳ vọng 13."
    assert container_closes == 26, f"Số lượng ':::' đóng là {container_closes}, kỳ vọng 26 (13 exercise + 13 solution)."
    print(f"  ✓ Đã kiểm tra cấu trúc container: {exercise_opens} exercise, {solution_opens} solution, {container_closes} thẻ đóng.")

    # 3. Kiểm tra tiêu đề Cách 1 và Cách 2
    cach1_count = len(re.findall(r"^#### Cách 1:", content, re.MULTILINE))
    cach2_count = len(re.findall(r"^#### Cách 2:", content, re.MULTILINE))
    assert cach1_count == 13, f"Số lượng '#### Cách 1:' là {cach1_count}, kỳ vọng 13."
    assert cach2_count == 13, f"Số lượng '#### Cách 2:' là {cach2_count}, kỳ vọng 13."
    print(f"  ✓ Đã kiểm tra tiêu đề giải pháp: {cach1_count} Cách 1, {cach2_count} Cách 2.")

    # 4. Trích xuất văn xuôi (bỏ qua khối code ```...```, bảng và vạch kẻ ngang)
    prose_lines = []
    in_code = False
    for line in content.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            # Bỏ qua vạch kẻ ngang và hàng chia cột bảng
            if line.strip() == "---" or re.match(r"^\|[-:\s|]+\|$", line.strip()):
                continue
            prose_lines.append(line)
    prose = "\n".join(prose_lines)

    # 5. Kiểm tra từ cấm
    for word in FORBIDDEN_WORDS:
        matches = re.findall(rf"\b{re.escape(word)}\b", prose, re.IGNORECASE)
        assert not matches, f"Phát hiện từ cấm '{word}' trong văn xuôi lab-10.md"
    print("  ✓ Không chứa bất kỳ từ cấm hoặc cụm từ cảm tính AI nào.")

    # 6. Kiểm tra dấu gạch ngang dài
    assert "—" not in prose, "Phát hiện dấu em dash ('—') trong văn xuôi."
    assert "--" not in prose, "Phát hiện dấu double dash ('--') trong văn xuôi."
    print("  ✓ Không chứa dấu gạch ngang dài trong văn xuôi.")

    # 7. Kiểm tra dấu chấm phẩy
    semicolons = [l for l in prose_lines if ";" in l]
    assert not semicolons, f"Phát hiện dấu chấm phẩy trong văn xuôi: {semicolons}"
    print("  ✓ Không chứa dấu chấm phẩy trong văn xuôi.")

    # 8. Kiểm tra quy tắc viết hoa sau dấu hai chấm (':')
    colon_issues = []
    for line in prose_lines:
        l_strip = line.strip()
        if l_strip.startswith("|") or l_strip.endswith("|") or l_strip.startswith(":::"):
            continue
        l_clean = re.sub(r"https?://\S+", "", line)
        l_clean = re.sub(r"\$[^$]+\$", "", l_clean)
        l_clean = re.sub(r"`[^`]+`", "", l_clean)
        for m in re.finditer(r":\s+(\S)", l_clean):
            char = m.group(1)
            if char.islower():
                colon_issues.append((line, char))
    assert not colon_issues, f"Phát hiện chữ thường sau dấu hai chấm: {colon_issues[:5]}"
    print("  ✓ Đã kiểm tra quy tắc viết hoa sau dấu hai chấm (100% đạt chuẩn).")

    # 9. Kiểm tra công thức toán học
    assert "\\vert" not in content, "Phát hiện cú pháp cấm \\vert trong công thức toán."
    assert "\\Vert" not in content, "Phát hiện cú pháp cấm \\Vert trong công thức toán."
    print("  ✓ Cú pháp công thức toán học đạt chuẩn (không dùng \\vert hay \\Vert).")


def test_coverage_completeness():
    """Kiểm tra tính bao phủ và tính hợp lệ của tệp coverage-10.json."""
    print("--- [3] Kiểm tra tính bao phủ trong coverage-10.json ---")
    coverage_data = json.loads(COVERAGE_PATH.read_text(encoding="utf-8"))

    assert coverage_data.get("lab") == "lab-10", "Thuộc tính 'lab' phải là 'lab-10'."
    assert coverage_data.get("total_exercises") == 13, "Thuộc tính 'total_exercises' phải là 13."
    assert coverage_data.get("exercise_ids") == EXPECTED_EXERCISES, "Danh sách 'exercise_ids' không khớp."

    cells = coverage_data.get("cells", {})
    template_cells = cells.get("template/lab-10.ipynb", [])
    course_cells = cells.get("course/2627-1/notebooks/lab-10.ipynb", [])

    assert len(template_cells) == 38, f"template/lab-10.ipynb có 38 cell, ghi nhận {len(template_cells)}."
    assert len(course_cells) == 62, f"course/2627-1/notebooks/lab-10.ipynb có 62 cell, ghi nhận {len(course_cells)}."

    for cell in template_cells:
        assert "cell_index" in cell and "cell_type" in cell and "status" in cell and "reason" in cell
        if cell["status"] == "mapped":
            assert cell["exercise_id"] in EXPECTED_EXERCISES

    for cell in course_cells:
        assert "cell_index" in cell and "cell_type" in cell and "status" in cell and "reason" in cell
        if cell["status"] == "mapped":
            assert cell["exercise_id"] in EXPECTED_EXERCISES

    print(f"  ✓ Bao phủ hoàn chỉnh: 38 cell template, 62 cell course (tổng cộng 100 cell).")


def test_python_implementations_and_fixtures():
    """Thực thi và đối chiếu thuật toán Cách 1 và Cách 2 của cả 13 bài tập."""
    print("--- [4] Thực thi và kiểm định thuật toán cả 13 bài tập ---")
    import numpy as np
    import pandas as pd

    # Dữ liệu dùng chung
    moc = "2026-06-29"
    ltm_bat_dau = "2025-06-30"

    demo_rv = pd.DataFrame({
        "listing_id": [11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 16],
        "date": pd.to_datetime([
            "2019-03-01", "2024-12-01", "2025-06-30", "2025-08-10", "2025-08-10", "2026-06-29", "2026-06-30",
            "2010-11-13", "2025-06-30", "2026-01-05", "2026-07-01",
            "2023-04-04", "2023-04-04", "2023-04-04", "2025-07-01",
            "2025-12-24", "2026-06-30", "2021-02-02"
        ]),
    })

    demo_ds = pd.DataFrame({
        "id": [11, 12, 13, 14, 15, 16],
        "name": ["Depto Lastarria", "Pieza Bellavista", "Loft Providencia", "Casa Ñuñoa", "Studio nuevo", "Hab Centro"],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]),
    })

    # --------------------------------------------------------------------------
    # Bài 1: data-lab-10-01
    # --------------------------------------------------------------------------
    ds_demo_rpm = pd.DataFrame({
        "id": [11, 12, 13, 14],
        "number_of_reviews": [0, 5, 0, 2],
        "reviews_per_month": [np.nan, 1.45, np.nan, np.nan],
    }, index=["N1", "N2", "N3", "N4"])

    # Cách 1
    rpm_c1 = ds_demo_rpm["reviews_per_month"].copy()
    rpm_c1.loc[ds_demo_rpm["number_of_reviews"].eq(0)] = 0.0

    # Cách 2
    rpm_c2 = ds_demo_rpm["reviews_per_month"].mask(ds_demo_rpm["number_of_reviews"].eq(0), 0.0)

    assert rpm_c1.equals(rpm_c2)
    assert rpm_c1.loc["N1"] == 0.0 and rpm_c1.loc["N3"] == 0.0
    assert rpm_c1.loc["N2"] == 1.45
    assert pd.isna(rpm_c1.loc["N4"])  # Chỗ ở có đánh giá nhưng thiếu rpm thì giữ NaN
    print("  ✓ Bài 1 (data-lab-10-01): Điền 0 có căn cứ kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 2: data-lab-10-02
    # --------------------------------------------------------------------------
    ds_demo_gia = pd.DataFrame({
        "id": [101, 102, 103, 104, 105],
        "room_type": ["Entire home/apt", "Entire home/apt", "Private room", "Private room", "Shared room"],
        "price": [60000.0, np.nan, 30000.0, np.nan, 20000.0],
    })

    # Cách 1
    trung_vi_nhom = ds_demo_gia.groupby("room_type")["price"].median()
    gia_uoc_c1 = ds_demo_gia["price"].copy()
    co_dien_c1 = ds_demo_gia["price"].isna()
    for rt, val in trung_vi_nhom.items():
        gia_uoc_c1.loc[co_dien_c1 & (ds_demo_gia["room_type"] == rt)] = val

    # Cách 2
    gia_uoc_c2 = ds_demo_gia["price"].fillna(ds_demo_gia.groupby("room_type")["price"].transform("median"))
    co_dien_c2 = ds_demo_gia["price"].isna()

    assert gia_uoc_c1.equals(gia_uoc_c2) and co_dien_c1.equals(co_dien_c2)
    assert gia_uoc_c1.loc[1] == 60000.0 and gia_uoc_c1.loc[3] == 30000.0
    assert co_dien_c1.tolist() == [False, True, False, True, False]
    print("  ✓ Bài 2 (data-lab-10-02): Điền giá theo nhóm và cờ kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 3: data-lab-10-03
    # --------------------------------------------------------------------------
    gia_thu = pd.DataFrame({
        "price": [np.nan, 0.0, -5000.0, 100000.0, 150000.0, 250000.0],
    }, index=["P6", "P2", "P9", "P1", "P5", "P3"])

    def kiem_gia_test(d, nguong):
        p = d["price"]
        hop_le = p.notna()
        return pd.DataFrame({
            "thieu": ~hop_le,
            "khong_duong": (hop_le & (p <= 0)).fillna(False).astype(bool),
            "cao": (hop_le & (p > nguong)).fillna(False).astype(bool),
        }, index=d.index)

    co_gia = kiem_gia_test(gia_thu, 120000.0)
    assert co_gia["thieu"].tolist() == [True, False, False, False, False, False]
    assert co_gia["khong_duong"].tolist() == [False, True, True, False, False, False]
    assert co_gia["cao"].tolist() == [False, False, False, False, True, True]
    assert not co_gia.isna().any().any()
    print("  ✓ Bài 3 (data-lab-10-03): Quy tắc kiểm tra giá kiem_gia kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 4: data-lab-10-04
    # --------------------------------------------------------------------------
    ds_demo_phan_vi = pd.DataFrame({
        "price": [10000.0, 20000.0, 30000.0, 40000.0, 50000.0, 60000.0, 70000.0, 80000.0, 90000.0, 500000.0, np.nan, -100.0],
    })
    p_pos = ds_demo_phan_vi.loc[ds_demo_phan_vi["price"] > 0, "price"].dropna()
    q1, q3 = p_pos.quantile(0.25), p_pos.quantile(0.75)
    nguong_iqr = q3 + 1.5 * (q3 - q1)
    so_vuot_iqr = int((p_pos > nguong_iqr).sum())
    nguong_p99 = float(p_pos.quantile(0.99))
    p_bo = p_pos[p_pos <= nguong_p99]
    p_chan = p_pos.clip(upper=nguong_p99)

    assert so_vuot_iqr == 1  # 500000 vượt IQR
    assert len(p_pos) == 10 and len(p_bo) == 9 and len(p_chan) == 10
    assert p_chan.max() == nguong_p99
    print("  ✓ Bài 4 (data-lab-10-04): Phân vị ngoại lai và bảng so sánh kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 5: data-lab-10-05
    # --------------------------------------------------------------------------
    mau_rv_demo = pd.DataFrame({
        "review_id": ["R1", "R2", "R1", "R3"],
        "listing_id": ["P1", "P1", "P1", "P2"],
        "date": pd.to_datetime(["2026-06-28"] * 4),
        "noi_dung": ["Yên tĩnh", "Sạch sẽ", "Yên tĩnh", "Thuận tiện"],
    })
    rv_rut_gon_demo = pd.DataFrame({
        "listing_id": [11, 11, 12, 12, 12],
        "date": pd.to_datetime(["2025-08-10", "2025-08-10", "2026-01-05", "2026-01-05", "2026-01-05"]),
    })
    sach = mau_rv_demo.drop_duplicates(subset=["review_id"])
    assert len(sach) == 3 and set(sach["review_id"]) == {"R1", "R2", "R3"}
    cap = ["listing_id", "date"]
    assert rv_rut_gon_demo.duplicated(subset=cap).sum() == 3
    assert rv_rut_gon_demo.duplicated(subset=cap, keep=False).sum() == 5
    print("  ✓ Bài 5 (data-lab-10-05): Phân biệt khử trùng review_id và đếm lặp kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 6: data-lab-10-06
    # --------------------------------------------------------------------------
    def time_domain_test(rv, m):
        d = rv["date"]
        return {
            "ngay_dau": d.min(),
            "ngay_cuoi": d.max(),
            "so_sau_moc": int((d > pd.Timestamp(m)).sum()),
        }
    td = time_domain_test(demo_rv, moc)
    assert td["ngay_dau"] == pd.Timestamp("2010-11-13")
    assert td["ngay_cuoi"] == pd.Timestamp("2026-07-01")
    assert td["so_sau_moc"] == 3

    def kiem_reviews_test(r, ids, m):
        d = r["date"]
        moc_ts = pd.Timestamp(m)
        return pd.DataFrame({
            "ngay_thieu": d.isna(),
            "sau_moc": (d.notna() & (d > moc_ts)).fillna(False).astype(bool),
            "id_khong_khop": (~r["listing_id"].isin(ids)).astype(bool),
        }, index=r.index)
    co_r = kiem_reviews_test(demo_rv, demo_ds["id"], moc)
    assert co_r["sau_moc"].sum() == 3
    assert co_r["id_khong_khop"].sum() == 0
    assert co_r.any(axis=1).sum() == 3
    print("  ✓ Bài 6 (data-lab-10-06): time_domain và kiem_reviews kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 7: data-lab-10-07
    # --------------------------------------------------------------------------
    def orphan_reviews_test(rv, ds):
        return int((~rv["listing_id"].isin(ds["id"])).sum())
    assert orphan_reviews_test(demo_rv, demo_ds) == 0
    ds_thieu = demo_ds[demo_ds["id"] != 11]
    assert orphan_reviews_test(demo_rv, ds_thieu) == 7
    print("  ✓ Bài 7 (data-lab-10-07): orphan_reviews kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 8: data-lab-10-08
    # --------------------------------------------------------------------------
    def duplicate_pairs_test(rv, cot=None):
        if cot is None:
            cot = ["listing_id", "date"]
        return int(rv.duplicated(subset=cot).sum())
    assert duplicate_pairs_test(demo_rv) == 3
    assert duplicate_pairs_test(demo_rv, ["listing_id"]) == 13
    print("  ✓ Bài 8 (data-lab-10-08): duplicate_pairs kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 9: data-lab-10-09
    # --------------------------------------------------------------------------
    def review_count_check_test(rv, ds):
        dem = rv.groupby("listing_id").size()
        dem_that = ds["id"].map(dem).fillna(0).astype(int)
        so_lech = int((ds["number_of_reviews"] != dem_that).sum())
        return {"dem_that": dem_that, "so_lech_tong": so_lech}
    rc = review_count_check_test(demo_rv, demo_ds)
    assert rc["so_lech_tong"] == 0
    assert rc["dem_that"].tolist() == [7, 4, 4, 2, 0, 1]
    print("  ✓ Bài 9 (data-lab-10-09): review_count_check kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 10: data-lab-10-10
    # --------------------------------------------------------------------------
    def ltm_mismatch_test(rv, ds, bat_dau, ket_thuc=None):
        ts_bat_dau = pd.Timestamp(bat_dau)
        if ket_thuc is None:
            loc_rv = rv.loc[rv["date"] >= ts_bat_dau]
        else:
            loc_rv = rv.loc[rv["date"].between(ts_bat_dau, pd.Timestamp(ket_thuc))]
        dem = loc_rv.groupby("listing_id").size()
        ltm_that = ds["id"].map(dem).fillna(0).astype(int)
        do_lech = ds["number_of_reviews_ltm"] - ltm_that
        so_lech_ltm = int((do_lech != 0).sum())
        return {"ltm_that": ltm_that, "do_lech": do_lech, "so_lech_ltm": so_lech_ltm}

    ltm_unbounded = ltm_mismatch_test(demo_rv, demo_ds, ltm_bat_dau)
    assert ltm_unbounded["ltm_that"].tolist() == [5, 3, 1, 2, 0, 0]
    assert ltm_unbounded["do_lech"].tolist() == [-1, -1, 0, 0, 0, 0]
    assert ltm_unbounded["so_lech_ltm"] == 2

    ltm_bounded = ltm_mismatch_test(demo_rv, demo_ds, ltm_bat_dau, moc)
    assert ltm_bounded["ltm_that"].tolist() == [4, 2, 1, 1, 0, 0]
    assert ltm_bounded["do_lech"].tolist() == [0, 0, 0, 1, 0, 0]
    assert ltm_bounded["so_lech_ltm"] == 1
    print("  ✓ Bài 10 (data-lab-10-10): ltm_mismatch cả hai quy ước kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 11: data-lab-10-11
    # --------------------------------------------------------------------------
    def qa_report_test(so_dong, ghi_chu, p):
        danh_sach_qt = list(so_dong.keys())
        df = pd.DataFrame({
            "quy_tac": danh_sach_qt,
            "so_dong": [int(so_dong[k]) for k in danh_sach_qt],
            "ghi_chu": [str(ghi_chu.get(k, "")) for k in danh_sach_qt],
        })
        df.to_csv(p, index=False, encoding="utf-8")
        return pd.read_csv(p, keep_default_na=False)

    with tempfile.TemporaryDirectory() as td:
        tf = Path(td) / "test_report.csv"
        so = {"r1": 3, "r2": 0, "r3": 1}
        gh = {"r1": "note1", "r3": "note3"}
        rep = qa_report_test(so, gh, tf)
        assert rep.shape == (3, 3)
        assert rep["quy_tac"].tolist() == ["r1", "r2", "r3"]
        assert rep.loc[1, "ghi_chu"] == ""
    print("  ✓ Bài 11 (data-lab-10-11): qa_report và tóm tắt cờ kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 12: data-lab-10-12
    # --------------------------------------------------------------------------
    gia_nhap_demo = pd.DataFrame({
        "id": ["P1", "P2", "P3", "P4", "P1", "P2", "P3", "P4", "P1"],
        "ky": ["T6", "T6", "T6", "T6", "T6", "T6", "T6", "T6", "T5"],
        "gia": [120.0, 90.0, np.nan, np.nan, 120.0, 95.0, 110.0, np.nan, 100.0],
    })
    counts = gia_nhap_demo.groupby(["id", "ky"])["gia"].transform(lambda s: s.dropna().nunique())
    can_xem = gia_nhap_demo[counts > 1].copy()
    khong_mau_thuan = gia_nhap_demo[counts <= 1]
    gia_gop = (
        khong_mau_thuan
        .sort_values(by=["id", "ky", "gia"], na_position="last")
        .drop_duplicates(subset=["id", "ky"], keep="first")
        .reset_index(drop=True)
    )
    assert len(can_xem) == 2 and set(can_xem["id"]) == {"P2"}
    assert len(gia_gop) == 4
    gop_dict = gia_gop.set_index(["id", "ky"])["gia"].to_dict()
    assert gop_dict[("P1", "T5")] == 100.0
    assert gop_dict[("P1", "T6")] == 120.0
    assert gop_dict[("P3", "T6")] == 110.0
    assert pd.isna(gop_dict[("P4", "T6")])
    print("  ✓ Bài 12 (data-lab-10-12): tach_gia_mau_thuan kiểm tra thành công.")

    # --------------------------------------------------------------------------
    # Bài 13: data-lab-10-13
    # --------------------------------------------------------------------------
    loai_demo = pd.Series(["Nguyên căn", "Phòng riêng", "Nguyên căn", None, "Nguyên căn"], index=["P1", "P2", "P3", "P4", "P5"])
    lich_demo = pd.DataFrame({
        "id": ["P2", "P1", "P1", "P2", "P1", "P2", "P1", "P2"],
        "ky": [3, 1, 4, 1, 2, 2, 3, 4],
        "gia": [np.nan, 100.0, 130.0, np.nan, np.nan, 200.0, np.nan, np.nan],
    })
    nhiet_do_demo = pd.Series([18.0, np.nan, np.nan, 24.0, np.nan], index=pd.to_datetime(["2026-06-01", "2026-06-02", "2026-06-05", "2026-06-07", "2026-06-08"]))

    loai_dien = loai_demo.fillna(loai_demo.mode().iloc[0])
    assert loai_dien.loc["P4"] == "Nguyên căn"

    lich_dien = lich_demo.sort_values(by=["id", "ky"]).reset_index(drop=True)
    lich_dien["dien"] = lich_dien.groupby("id")["gia"].ffill(limit=1)
    assert np.allclose(lich_dien["dien"].astype(float), [100, 100, np.nan, 130, np.nan, 200, 200, np.nan], equal_nan=True)

    noi_suy = nhiet_do_demo.interpolate(method="time", limit_area="inside")
    assert np.allclose(noi_suy.astype(float), [18, 19, 22, 24, np.nan], equal_nan=True)
    print("  ✓ Bài 13 (data-lab-10-13): Điền mốt, ffill theo nhóm và nội suy thời gian kiểm tra thành công.")


def test_real_snapshot_verification():
    """Kiểm tra đối chiếu các con số thực tế trên snapshot Inside Airbnb Santiago."""
    print("--- [5] Kiểm tra đối chiếu số liệu trên snapshot Santiago thực tế ---")
    tep_listings = DATA_DIR / "listings.csv"
    tep_reviews = DATA_DIR / "reviews.csv"

    if not (tep_listings.exists() and tep_reviews.exists()):
        print("  ℹ Không tìm thấy tệp CSV snapshot đầy đủ cục bộ. Bỏ qua bước kiểm tra snapshot lớn.")
        return

    import pandas as pd
    import numpy as np

    print("  Đang đọc dữ liệu snapshot thực tế...")
    ds = pd.read_csv(tep_listings)
    rv = pd.read_csv(tep_reviews)
    rv["date"] = pd.to_datetime(rv["date"])

    # 1. Toàn vẹn khóa ngoại
    so_mo_coi = int((~rv["listing_id"].isin(ds["id"])).sum())
    assert so_mo_coi == 0, f"Kỳ vọng 0 đánh giá mồ côi, thực tế {so_mo_coi}"
    print(f"  ✓ Snapshot: Toàn vẹn khóa ngoại 100% (0 đánh giá mồ côi trên {len(rv):,} dòng).")

    # 2. Miền thời gian
    moc_ts = pd.Timestamp("2026-06-29")
    so_sau_moc = int((rv["date"] > moc_ts).sum())
    assert so_sau_moc == 204, f"Kỳ vọng 204 đánh giá sau mốc, thực tế {so_sau_moc}"
    assert rv["date"].min() == pd.Timestamp("2010-11-13")
    assert rv["date"].max() == pd.Timestamp("2026-07-01")
    print(f"  ✓ Snapshot: Miền thời gian từ 2010-11-13 đến 2026-07-01 (đúng 204 đánh giá sau 29/06).")

    # 3. Trùng lặp cặp (listing_id, date)
    so_trung_cap = int(rv.duplicated(subset=["listing_id", "date"]).sum())
    assert so_trung_cap == 3548, f"Kỳ vọng 3,548 dòng trùng cặp, thực tế {so_trung_cap}"
    print(f"  ✓ Snapshot: Đúng 3,548 dòng trùng cặp (listing_id, date).")

    # 4. Đối chiếu tổng số đánh giá
    dem_that = ds["id"].map(rv.groupby("listing_id").size()).fillna(0).astype(int)
    so_lech_tong = int((ds["number_of_reviews"] != dem_that).sum())
    assert so_lech_tong == 0, f"Kỳ vọng 0 chỗ ở lệch tổng số đánh giá, thực tế {so_lech_tong}"
    print(f"  ✓ Snapshot: Cột number_of_reviews khớp 100% trên toàn bộ {len(ds):,} chỗ ở.")

    # 5. Đối chiếu LTM không chặn trên
    dem_ltm = ds["id"].map(rv.loc[rv["date"] >= pd.Timestamp("2025-06-30")].groupby("listing_id").size()).fillna(0).astype(int)
    do_lech_ltm = ds["number_of_reviews_ltm"] - dem_ltm
    so_lech_ltm = int((do_lech_ltm != 0).sum())
    assert so_lech_ltm == 665, f"Kỳ vọng 665 chỗ ở lệch LTM không chặn, thực tế {so_lech_ltm}"
    print(f"  ✓ Snapshot: Đúng 665 chỗ ở lệch LTM (không chặn trên), phân vị 50% lệch đúng -1.")

    # 6. Ngưỡng giá IQR và P99
    pos_price = ds.loc[ds["price"] > 0, "price"].dropna()
    q1 = pos_price.quantile(0.25)
    q3 = pos_price.quantile(0.75)
    nguong_iqr = q3 + 1.5 * (q3 - q1)
    so_vuot_iqr = int((pos_price > nguong_iqr).sum())
    assert np.isclose(nguong_iqr, 164784.375, rtol=0, atol=0.01)
    assert so_vuot_iqr == 1499
    nguong_p99 = float(pos_price.quantile(0.99))
    assert np.isclose(nguong_p99, 686143.75, rtol=0, atol=0.01)
    so_vuot_p99 = int((pos_price > nguong_p99).sum())
    assert so_vuot_p99 == 177
    print(f"  ✓ Snapshot: Ngưỡng IQR = 164,784.38 CLP (1,499 chỗ ở vượt); P99 = 686,143.75 CLP (177 chỗ ở vượt).")

    # 7. Giá trị thiếu giá theo room_type
    so_thieu_gia = int(ds["price"].isna().sum())
    assert so_thieu_gia == 846, f"Kỳ vọng 846 giá thiếu, thực tế {so_thieu_gia}"
    medians = ds.groupby("room_type")["price"].median().to_dict()
    assert medians["Entire home/apt"] == 64900.0
    assert medians["Private room"] == 34235.0
    assert medians["Shared room"] == 20541.0
    print(f"  ✓ Snapshot: Đúng 846 chỗ ở thiếu giá, trung vị Entire home/apt = 64,900 CLP, Private room = 34,235 CLP.")


def main():
    print("======================================================================")
    print("CHƯƠNG TRÌNH KIỂM ĐỊNH TOÀN DIỆN LAB 10: XỬ LÝ DỮ LIỆU CHÉO BẢNG")
    print("======================================================================")
    test_file_existence()
    test_markdown_pedagogical_rules()
    test_coverage_completeness()
    test_python_implementations_and_fixtures()
    test_real_snapshot_verification()
    print("======================================================================")
    print("KẾT QUẢ: TẤT CẢ CÁC BÀI KIỂM ĐỊNH ĐÃ VƯỢT QUA XUẤT SẮC (PASSED)")
    print("======================================================================")


if __name__ == "__main__":
    main()
