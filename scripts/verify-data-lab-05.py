# -*- coding: utf-8 -*-
"""Kịch bản kiểm tra tự động toàn diện bộ bài tập Lab 05.

Các tệp kiểm định:
1. raw_materials/xu-ly-du-lieu/labs/lab-05-pandas.md (data-lab-05-01 đến 03)
2. raw_materials/xu-ly-du-lieu/labs/lab-05-groupby.md (data-lab-05-04 đến 09)
3. raw_materials/xu-ly-du-lieu/labs/lab-05-merge.md (data-lab-05-10)

Mục tiêu kiểm định:
1. Thực thi động tất cả các khối mã nguồn Python trong các file Markdown.
2. So sánh tính tương đương về kết quả giữa Cách 1 (cơ bản) và Cách 2 (thực tế/tối ưu).
3. Kiểm tra độc lập các trường hợp biên: Dữ liệu khuyết (NaN), chỉ số âm, bảng rỗng, trùng khóa tra cứu.
4. Đảm bảo cấu trúc Markdown chuẩn mực: Không chứa H1 ngoài code fence, đủ span ID, không dùng từ cấm.
"""

import ast
import io
import os
import re
import sys
from pathlib import Path
import numpy as np
import pandas as pd

# Thiết lập đầu ra console chuẩn UTF-8
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Dữ liệu chuẩn bị sẵn phục vụ kiểm thử độc lập
DEMO = pd.DataFrame({
    "id": list(range(201, 213)),
    "name": [
        "Depto Central", "Pieza Bellas Artes", "Loft Parque Forestal", "Estudio sin precio",
        "Habitacion Santa Lucia", "Depto Providencia", "Suite Costanera", "Loft Pedro de Valdivia",
        "Habitacion Manuel Montt", "Casa Nunoa", "Loft Plaza Egaña", "Villa Vitacura"
    ],
    "neighbourhood": ["Santiago"] * 5 + ["Providencia"] * 4 + ["Ñuñoa"] * 2 + ["Vitacura"],
    "price": [
        25000.0, 45000.0, 120000.0, np.nan, 60000.0,
        30000.0, 99999.0, 100000.0, 18000.0,
        55000.0, 150000.0, 210000.0
    ],
    "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
    "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
})

s_demo = pd.Series([100, 200, 300], index=[2, 0, 5])
gia_cu = pd.Series({"A": 100.0, "B": 200.0, "C": 50.0})
gia_moi = pd.Series({"B": 220.0, "A": 90.0, "D": 70.0})

phi = pd.DataFrame({
    "phan_khuc": ["re", "trung", "cao"],
    "phi_dich_vu": [0.10, 0.13, 0.15],
})

# ==============================================================================
# 1. Định nghĩa các hàm lời giải Cách 1 và Cách 2 cho 10 bài tập
# ==============================================================================

# Bài 1: loc và iloc
def loc_iloc_c1(s: pd.Series, nhan, vi_tri: int) -> dict:
    gia_tri_nhan = s.loc[nhan]
    gia_tri_vi_tri = s.iloc[vi_tri]
    return {"theo_nhan": gia_tri_nhan, "theo_vi_tri": gia_tri_vi_tri}

def loc_iloc_c2(s: pd.Series, nhan, vi_tri: int) -> dict:
    return {"theo_nhan": s.loc[nhan], "theo_vi_tri": s.iloc[vi_tri]}

# Bài 2: alignment
def align_change_c1(gia_cu: pd.Series, gia_moi: pd.Series) -> dict:
    thay_doi = gia_moi - gia_cu
    so_nan = int(thay_doi.isna().sum())
    return {"thay_doi": thay_doi, "so_nan": so_nan}

def align_change_c2(gia_cu: pd.Series, gia_moi: pd.Series) -> dict:
    thay_doi = gia_moi.sub(gia_cu)
    so_nan = int(thay_doi.isna().sum())
    return {"thay_doi": thay_doi, "so_nan": so_nan}

# Bài 3: phan_khuc
def phan_khuc_c1(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    else:
        return "cao"

def phan_khuc_c2(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    if gia < 100000.0:
        return "trung"
    return "cao"

# Bài 4: segment_stats
def segment_stats_c1(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("phan_khuc", observed=True).agg(
        so_phong=("id", "size"),
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean"),
    )

def segment_stats_c2(df: pd.DataFrame) -> pd.DataFrame:
    df_loc = df.dropna(subset=["phan_khuc"]).copy()
    thu_tu = ["re", "trung", "cao"]
    df_loc["phan_khuc"] = pd.Categorical(df_loc["phan_khuc"], categories=thu_tu, ordered=True)
    return df_loc.groupby("phan_khuc", observed=False).agg(
        so_phong=("id", "size"),
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean"),
    )

# Bài 5: pro_host_summary
def pro_host_summary_c1(df: pd.DataFrame, nguong: int = 5) -> dict:
    chuyen = df["calculated_host_listings_count"] >= nguong
    ty_le_chuyen = float(chuyen.mean())
    so_sanh = df.groupby(chuyen, observed=True).agg(
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean"),
    )
    return {"chuyen": chuyen, "ty_le_chuyen": ty_le_chuyen, "so_sanh": so_sanh}

def pro_host_summary_c2(df: pd.DataFrame, nguong: int = 5) -> dict:
    chuyen = df["calculated_host_listings_count"].ge(nguong)
    chuyen.name = "chuyen"
    ty_le_chuyen = float(chuyen.mean())
    so_sanh = df.groupby(chuyen, observed=False).agg(
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean"),
    )
    return {"chuyen": chuyen, "ty_le_chuyen": ty_le_chuyen, "so_sanh": so_sanh}

# Bài 6: big_districts
def big_districts_c1(df: pd.DataFrame, nguong: int = 300) -> dict:
    n_quan = df.groupby("neighbourhood")["id"].transform("size")
    mask = n_quan >= nguong
    df_dong = df[mask].copy()
    return {"n_quan": n_quan, "df_dong": df_dong}

def big_districts_c2(df: pd.DataFrame, nguong: int = 300) -> dict:
    n_quan = df.groupby("neighbourhood")["neighbourhood"].transform("size")
    df_dong = df.loc[n_quan.ge(nguong)].copy()
    return {"n_quan": n_quan, "df_dong": df_dong}

# Bài 7: segment_host_pivot
def segment_host_pivot_c1(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(
        index="phan_khuc",
        columns="chuyen",
        values="number_of_reviews_ltm",
        aggfunc="mean",
    )

def segment_host_pivot_c2(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["phan_khuc", "chuyen"], observed=False)["number_of_reviews_ltm"]
        .mean()
        .unstack(level="chuyen")
    )

# Bài 8: top_price_by_district
def top_price_by_district_c1(df: pd.DataFrame) -> pd.DataFrame:
    gia_max_quan = df.groupby("neighbourhood")["price"].transform("max")
    mask = df["price"] == gia_max_quan
    return df[mask].copy()

def top_price_by_district_c2(df: pd.DataFrame) -> pd.DataFrame:
    df_hop_le = df.dropna(subset=["price"])
    gia_max = df_hop_le.groupby("neighbourhood")["price"].transform("max")
    return df_hop_le.loc[df_hop_le["price"].eq(gia_max)].copy()

# Bài 9: segment_share_by_district
def segment_share_by_district_c1(df: pd.DataFrame) -> pd.DataFrame:
    bang_ty_trong = pd.crosstab(
        df["neighbourhood"],
        df["phan_khuc"],
        normalize="index",
    )
    for col in ["re", "trung", "cao"]:
        if col not in bang_ty_trong.columns:
            bang_ty_trong[col] = 0.0
    return bang_ty_trong[["re", "trung", "cao"]]

def segment_share_by_district_c2(df: pd.DataFrame) -> pd.DataFrame:
    dem = df.groupby(["neighbourhood", "phan_khuc"], observed=False).size().unstack(fill_value=0)
    tong_hang = dem.sum(axis=1)
    bang_ty_trong = dem.div(tong_hang, axis=0)
    for col in ["re", "trung", "cao"]:
        if col not in bang_ty_trong.columns:
            bang_ty_trong[col] = 0.0
    return bang_ty_trong[["re", "trung", "cao"]]

# Bài 10: merge_fees
def merge_fees_c1(df: pd.DataFrame, phi: pd.DataFrame) -> dict:
    m = pd.merge(df, phi, on="phan_khuc", how="left", validate="m:1")
    return {
        "m": m,
        "so_dong_m": len(m),
        "so_nan_phi": int(m["phi_dich_vu"].isna().sum()),
    }

def merge_fees_c2(df: pd.DataFrame, phi: pd.DataFrame) -> dict:
    m = df.merge(phi, on="phan_khuc", how="left", validate="many_to_one")
    return {
        "m": m,
        "so_dong_m": len(m),
        "so_nan_phi": int(m["phi_dich_vu"].isna().sum()),
    }


# ==============================================================================
# 2. Quy trình kiểm định độc lập và kiểm tra biên
# ==============================================================================

def run_all_tests():
    print("=" * 70)
    print("BẮT ĐẦU KIỂM TRA BỘ LỜI GIẢI LAB 05 (PANDAS, GROUPBY, MERGE)")
    print("=" * 70)

    # --------------------------------------------------------------------------
    # Bài 1: data-lab-05-01
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-05-01] Kiểm tra Bài 1: loc_iloc ---")
    res1_c1 = loc_iloc_c1(s_demo, 2, 2)
    res1_c2 = loc_iloc_c2(s_demo, 2, 2)
    assert res1_c1 == res1_c2 == {"theo_nhan": 100, "theo_vi_tri": 300}

    # Biên: Vị trí 0 và nhãn 0
    res1_zero = loc_iloc_c1(s_demo, 0, 0)
    assert res1_zero == {"theo_nhan": 200, "theo_vi_tri": 100}

    # Biên: Vị trí âm (-1 là phần tử cuối)
    res1_neg = loc_iloc_c1(s_demo, 5, -1)
    assert res1_neg == {"theo_nhan": 300, "theo_vi_tri": 300}
    print("✓ Bài 1 ĐẠT (so sánh 2 cách, kiểm tra nhãn số nguyên và chỉ số âm thành công)")

    # --------------------------------------------------------------------------
    # Bài 2: data-lab-05-02
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-05-02] Kiểm tra Bài 2: align_change ---")
    res2_c1 = align_change_c1(gia_cu, gia_moi)
    res2_c2 = align_change_c2(gia_cu, gia_moi)
    pd.testing.assert_series_equal(res2_c1["thay_doi"], res2_c2["thay_doi"])
    assert res2_c1["so_nan"] == res2_c2["so_nan"] == 2
    assert res2_c1["thay_doi"]["A"] == -10.0
    assert res2_c1["thay_doi"]["B"] == 20.0
    assert np.isnan(res2_c1["thay_doi"]["C"])
    assert np.isnan(res2_c1["thay_doi"]["D"])

    # Biên: Hai Series có index hoàn toàn khớp (0 ô NaN)
    s_khop1 = pd.Series({"X": 10.0, "Y": 20.0})
    s_khop2 = pd.Series({"X": 15.0, "Y": 25.0})
    assert align_change_c1(s_khop1, s_khop2)["so_nan"] == 0

    # Biên: Hai Series rời nhau hoàn toàn (tất cả là NaN)
    s_roi1 = pd.Series({"M": 5.0})
    s_roi2 = pd.Series({"N": 10.0})
    assert align_change_c1(s_roi1, s_roi2)["so_nan"] == 2
    print("✓ Bài 2 ĐẠT (so sánh 2 cách, tự căn chỉnh index và kiểm soát NaN chuẩn xác)")

    # --------------------------------------------------------------------------
    # Bài 3: data-lab-05-03
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-05-03] Kiểm tra Bài 3: phan_khuc ---")
    assert phan_khuc_c1(25000.0) == phan_khuc_c2(25000.0) == "re"
    assert phan_khuc_c1(30000.0) == phan_khuc_c2(30000.0) == "trung"
    assert phan_khuc_c1(99999.0) == phan_khuc_c2(99999.0) == "trung"
    assert phan_khuc_c1(100000.0) == phan_khuc_c2(100000.0) == "cao"
    assert phan_khuc_c1(np.nan) is None
    assert phan_khuc_c1(None) is None
    assert phan_khuc_c2(np.nan) is None
    assert phan_khuc_c2(None) is None

    # Tần suất trên 12 dòng DEMO
    dem_demo = DEMO["price"].map(phan_khuc_c1).value_counts(dropna=False)
    assert dem_demo["trung"] == 5
    assert dem_demo["cao"] == 4
    assert dem_demo["re"] == 2
    assert pd.isna(dem_demo.index[dem_demo.index.isna()][0])
    print("✓ Bài 3 ĐẠT (so sánh 2 cách, kiểm tra các ngưỡng biên số học và ô khuyết)")

    # --------------------------------------------------------------------------
    # Bài 4: data-lab-05-04
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-05-04] Kiểm tra Bài 4: segment_stats ---")
    demo_pkg = DEMO.assign(phan_khuc=DEMO["price"].map(phan_khuc_c1))
    before_demo = demo_pkg.copy()
    res4_c1 = segment_stats_c1(demo_pkg)
    res4_c2 = segment_stats_c2(demo_pkg)

    # Đối chiếu số liệu
    assert list(res4_c1.columns) == ["so_phong", "gia_trung_vi", "review_nam_tb"]
    assert res4_c1.loc["trung", "so_phong"] == res4_c2.loc["trung", "so_phong"] == 5
    assert res4_c1.loc["cao", "gia_trung_vi"] == res4_c2.loc["cao", "gia_trung_vi"] == 135000.0
    assert res4_c1.loc["trung", "review_nam_tb"] == res4_c2.loc["trung", "review_nam_tb"] == 17.0
    pd.testing.assert_frame_equal(demo_pkg, before_demo, obj="DEMO không bị thêm cột")
    print("✓ Bài 4 ĐẠT (so sánh 2 cách, tính đúng Named Aggregation và giữ nguyên bảng gốc)")

    # --------------------------------------------------------------------------
    # Bài 5: data-lab-05-05
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-05-05] Kiểm tra Bài 5: pro_host_summary ---")
    before_demo5 = DEMO.copy()
    res5_c1 = pro_host_summary_c1(DEMO, 5)
    res5_c2 = pro_host_summary_c2(DEMO, 5)

    assert res5_c1["ty_le_chuyen"] == res5_c2["ty_le_chuyen"] == 0.5
    assert res5_c1["so_sanh"].loc[True, "gia_trung_vi"] == 80000.0
    assert res5_c1["so_sanh"].loc[False, "review_nam_tb"] == 5.5
    assert "chuyen" not in DEMO.columns, "Bảng DEMO bị thêm cột chuyen ngoài ý muốn!"
    pd.testing.assert_frame_equal(DEMO, before_demo5)
    print("✓ Bài 5 ĐẠT (so sánh 2 cách, nhóm bằng Series ngoài bảo đảm tính bất biến)")

    # --------------------------------------------------------------------------
    # Bài 6: data-lab-05-06
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-05-06] Kiểm tra Bài 6: big_districts ---")
    res6_c1 = big_districts_c1(DEMO, 4)
    res6_c2 = big_districts_c2(DEMO, 4)

    pd.testing.assert_series_equal(res6_c1["n_quan"], res6_c2["n_quan"], check_names=False)
    pd.testing.assert_frame_equal(res6_c1["df_dong"], res6_c2["df_dong"])
    assert list(res6_c1["n_quan"]) == [5, 5, 5, 5, 5, 4, 4, 4, 4, 2, 2, 1]
    assert len(res6_c1["df_dong"]) == 9
    assert res6_c1["df_dong"]["neighbourhood"].nunique() == 2
    assert "n_quan" not in DEMO.columns and "n_quan" not in res6_c1["df_dong"].columns

    # Biên: Ngưỡng lớn hơn mọi quận -> bảng rỗng
    res6_empty = big_districts_c1(DEMO, 100)
    assert len(res6_empty["df_dong"]) == 0
    print("✓ Bài 6 ĐẠT (so sánh 2 cách, gắn quy mô nhóm qua transform và lọc quận lớn)")

    # --------------------------------------------------------------------------
    # Bài 7: data-lab-05-07
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-05-07] Kiểm tra Bài 7: segment_host_pivot ---")
    demo_pv = demo_pkg.copy()
    demo_pv["chuyen"] = demo_pv["calculated_host_listings_count"] >= 5
    res7_c1 = segment_host_pivot_c1(demo_pv)
    res7_c2 = segment_host_pivot_c2(demo_pv)

    pd.testing.assert_frame_equal(res7_c1, res7_c2)
    assert res7_c1.loc["cao", False] == 1.0
    assert round(res7_c1.loc["trung", True], 2) == 21.67
    assert np.isnan(res7_c1.loc["re", True])
    print("✓ Bài 7 ĐẠT (so sánh 2 cách, xây dựng bảng chéo pivot table chuẩn xác)")

    # --------------------------------------------------------------------------
    # Bài 8: data-lab-05-08 (Extension 1: Phòng đắt nhất từng quận)
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-05-08] Kiểm tra Bài 8: top_price_by_district ---")
    df_quan_lon = res6_c1["df_dong"].copy()
    res8_c1 = top_price_by_district_c1(df_quan_lon)
    res8_c2 = top_price_by_district_c2(df_quan_lon)

    pd.testing.assert_frame_equal(res8_c1, res8_c2)
    assert len(res8_c1) == 2
    assert set(res8_c1["neighbourhood"]) == {"Santiago", "Providencia"}
    assert res8_c1.loc[res8_c1["neighbourhood"] == "Santiago", "price"].values[0] == 120000.0
    assert res8_c1.loc[res8_c1["neighbourhood"] == "Providencia", "price"].values[0] == 100000.0

    # Biên hòa giá (Ties): Hai phòng cùng giá tối đa
    df_hoa = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["A", "B", "C"],
        "neighbourhood": ["Quận 1", "Quận 1", "Quận 1"],
        "price": [100.0, 100.0, 50.0],
    })
    res_hoa = top_price_by_district_c1(df_hoa)
    assert len(res_hoa) == 2, "Trường hợp hòa giá phải giữ lại toàn bộ các phòng cùng đạt giá trần"
    print("✓ Bài 8 ĐẠT (so sánh 2 cách, tìm phòng đắt nhất qua transform max và xử lý hòa giá)")

    # --------------------------------------------------------------------------
    # Bài 9: data-lab-05-09 (Extension 2: Cơ cấu phân khúc theo quận)
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-05-09] Kiểm tra Bài 9: segment_share_by_district ---")
    demo_quan_lon = demo_pkg[demo_pkg["neighbourhood"].isin(["Santiago", "Providencia"])].copy()
    res9_c1 = segment_share_by_district_c1(demo_quan_lon)
    res9_c2 = segment_share_by_district_c2(demo_quan_lon)

    pd.testing.assert_frame_equal(res9_c1, res9_c2)
    assert np.allclose(res9_c1.sum(axis=1), 1.0)
    assert np.isclose(res9_c1.loc["Santiago", "re"], 0.25)
    assert np.isclose(res9_c1.loc["Santiago", "trung"], 0.50)
    assert np.isclose(res9_c1.loc["Santiago", "cao"], 0.25)
    print("✓ Bài 9 ĐẠT (so sánh 2 cách, chuẩn hóa tỷ trọng phân khúc theo quận tổng bằng 1.0)")

    # --------------------------------------------------------------------------
    # Bài 10: data-lab-05-10
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-05-10] Kiểm tra Bài 10: merge_fees ---")
    res10_c1 = merge_fees_c1(demo_pkg, phi)
    res10_c2 = merge_fees_c2(demo_pkg, phi)

    assert res10_c1["so_dong_m"] == res10_c2["so_dong_m"] == 12
    assert res10_c1["so_nan_phi"] == res10_c2["so_nan_phi"] == 1
    m1 = res10_c1["m"]
    m2 = res10_c2["m"]
    pd.testing.assert_frame_equal(m1, m2)

    # Tính trung vị giá gồm phí
    gia_tong = m1["price"] * (1 + m1["phi_dich_vu"])
    tv_gia = gia_tong.groupby(m1["phan_khuc"]).median().round(0)
    assert tv_gia["trung"] == 62150.0

    # Kiểm tra ném ngoại lệ khi bảng tra cứu bị lỗi trùng khóa
    phi_trung = pd.concat([phi, phi.head(1)], ignore_index=True)
    try:
        merge_fees_c1(demo_pkg, phi_trung)
    except pd.errors.MergeError:
        pass
    else:
        raise AssertionError("validate='m:1' phải ném ngoại lệ MergeError khi bảng tra cứu có khóa trùng!")
    print("✓ Bài 10 ĐẠT (so sánh 2 cách, ghép bảng tra cứu, kiểm định quan hệ m:1 thành công)")

    # --------------------------------------------------------------------------
    # 3. Kiểm tra cú pháp Markdown và thực thi toàn bộ các khối mã
    # --------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("KIỂM TRA CẤU TRÚC MARKDOWN VÀ THỰC THI TOÀN BỘ CÁC KHỐI MÃ PYTHON")
    print("=" * 70)

    base_dir = Path(__file__).resolve().parents[1]
    owned_md_files = [
        base_dir / "raw_materials/xu-ly-du-lieu/labs/lab-05-pandas.md",
        base_dir / "raw_materials/xu-ly-du-lieu/labs/lab-05-groupby.md",
        base_dir / "raw_materials/xu-ly-du-lieu/labs/lab-05-merge.md",
    ]

    total_blocks_executed = 0
    forbidden_terms = ["hợp đồng hàm", "hợp đồng file", "hợp đồng dữ liệu"]

    for md_path in owned_md_files:
        assert md_path.exists(), f"Không tìm thấy tệp {md_path.name}"
        content = md_path.read_text(encoding="utf-8")
        assert "::: exercise" in content and "::: solution" in content, f"Thiếu container exercise/solution trong {md_path.name}"
        assert "#### Cách 1:" in content and "#### Cách 2:" in content, f"Thiếu tiêu đề Cách 1 / Cách 2 trong {md_path.name}"

        # Kiểm tra không chứa H1 ngoài code fence
        lines = content.splitlines()
        in_code_fence = False
        for line_idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if not in_code_fence and stripped.startswith("# "):
                raise AssertionError(f"Phát hiện heading H1 ngoài code fence tại dòng {line_idx} trong {md_path.name}: '{line}'")
            if not in_code_fence and "—" in line:
                raise AssertionError(f"Phát hiện dấu em dash ('—') ngoài code fence tại dòng {line_idx} trong {md_path.name}: '{line}'")
            if not in_code_fence and ";" in line:
                raise AssertionError(f"Phát hiện dấu chấm phẩy (';') ngoài code fence tại dòng {line_idx} trong {md_path.name}: '{line}'")

        # Kiểm tra từ cấm
        for term in forbidden_terms:
            assert term not in content.lower(), f"Phát hiện thuật ngữ cấm '{term}' trong {md_path.name}"

        # Trích xuất và chạy thử động các khối mã Python
        blocks = re.findall(r"```python\s*(.*?)\s*```", content, re.DOTALL)
        ns_doc = {}
        for b_idx, block in enumerate(blocks, 1):
            try:
                ast.parse(block, filename=f"{md_path.name}:block_{b_idx}")
            except SyntaxError as syn_err:
                raise AssertionError(f"Lỗi cú pháp AST tại khối {b_idx} của {md_path.name}: {syn_err}")

            try:
                exec(block, ns_doc)
            except Exception as exc:
                raise AssertionError(f"Lỗi thực thi khối {b_idx} của {md_path.name}: {type(exc).__name__}: {exc}")

        total_blocks_executed += len(blocks)
        print(f"✓ {md_path.name}: {len(blocks)} khối mã Python thực thi thành công 100%.")

    # Kiểm tra đầy đủ 10 exercise span IDs
    all_content = "".join([f.read_text(encoding="utf-8") for f in owned_md_files])
    for i in range(1, 11):
        span_id = f"data-lab-05-{i:02d}"
        assert f'id="{span_id}"' in all_content or f"id='{span_id}'" in all_content, f"Thiếu span id {span_id} trong các tệp Markdown"

    print("\n" + "=" * 70)
    print(f"TẤT CẢ 10 BÀI TẬP VÀ {total_blocks_executed} KHỐI MÃ PYTHON ĐÃ VƯỢT QUA 100% CÁC PHÉP KIỂM ĐỊNH!")
    print("=" * 70)

if __name__ == "__main__":
    run_all_tests()
