# -*- coding: utf-8 -*-
"""Kịch bản kiểm tra tự động trọn bộ lời giải Bài thực hành 04 (Lab 04).

Thư mục: raw_materials/xu-ly-du-lieu/labs/lab-04.md
Mục tiêu kiểm định:
1. Chạy độc lập mọi khối mã nguồn Python trong lab-04.md với dữ liệu mẫu (DEMO).
2. So sánh tính tương đương về kết quả giữa Cách 1 (cơ bản) và Cách 2 (thực tế/tối ưu).
3. Kiểm tra các trường hợp biên: bảng rỗng, dữ liệu khuyết (NaN), quận không tồn tại, tính bất biến không làm thay đổi bảng dữ liệu gốc.
4. Đảm bảo toàn bộ chuẩn mực in ra chuẩn UTF-8, không lỗi mã hóa ký tự tiếng Việt.
"""

import sys
import io
import math
import tempfile
from pathlib import Path
import numpy as np
import pandas as pd

# Thiết lập đầu ra console hỗ trợ chuẩn UTF-8
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Dữ liệu giả lập 12 dòng từ fixture chuẩn của đề bài
DEMO = pd.DataFrame({
    "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    "name": [
        "Depto Plaza Ñuñoa", "Pieza cerca metro", "Loft Irarrázaval", "Depto sin precio",
        "Dormitorio simple", "Casa familiar", "Studio Providencia", "Pieza Providencia",
        "Depto Centro", "Hostal Centro", "Pieza Centro", "Hotel boutique"
    ],
    "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
    "room_type": [
        "Entire home/apt", "Private room", "Entire home/apt", "Entire home/apt",
        "Private room", "Entire home/apt", "Entire home/apt", "Private room",
        "Entire home/apt", "Shared room", "Private room", "Hotel room"
    ],
    "price": [
        45000.0, 18000.0, 72000.0, np.nan, 2500.0, 60000.0,
        80000.0, 30000.0, 40000.0, 12000.0, np.nan, 95000.0
    ],
    "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
})


# ==============================================================================
# 1. Định nghĩa các hàm lời giải Cách 1 và Cách 2 cho 12 bài tập
# ==============================================================================

# Bài 1: Chọn cột, chọn hàng và tỷ lệ
def select_basics_c1(df: pd.DataFrame) -> dict:
    cot_gia = df["price"]
    bang_con = df[["name", "price"]]
    ty_le_private = float((df["room_type"] == "Private room").mean())
    mask = df["room_type"] == "Entire home/apt"
    nguyen_can = df[mask]
    gia_nguyen_can = df.loc[mask, "price"]
    return {
        "cot_gia": cot_gia,
        "bang_con": bang_con,
        "ty_le_private": ty_le_private,
        "nguyen_can": nguyen_can,
        "gia_nguyen_can": gia_nguyen_can,
    }

def select_basics_c2(df: pd.DataFrame) -> dict:
    cot_gia = df.loc[:, "price"]
    bang_con = df.filter(items=["name", "price"])
    ty_le_private = float(df["room_type"].eq("Private room").mean())
    mask = df["room_type"].eq("Entire home/apt")
    nguyen_can = df.loc[mask]
    gia_nguyen_can = df.loc[mask, "price"]
    return {
        "cot_gia": cot_gia,
        "bang_con": bang_con,
        "ty_le_private": ty_le_private,
        "nguyen_can": nguyen_can,
        "gia_nguyen_can": gia_nguyen_can,
    }


# Bài 2: Thói quen 5 bước
def extract_5step_metrics_c1(df: pd.DataFrame) -> dict:
    so_dong = len(df)
    so_cot = df.shape[1]
    so_thieu_price = int(df["price"].isna().sum())
    so_loai_phong = len(df["room_type"].value_counts())
    return {
        "so_dong": so_dong,
        "so_cot": so_cot,
        "so_thieu_price": so_thieu_price,
        "so_loai_phong": so_loai_phong,
    }

def extract_5step_metrics_c2(df: pd.DataFrame) -> dict:
    n_rows, n_cols = df.shape
    missing_price = int(df["price"].isnull().sum())
    n_room_types = int(df["room_type"].nunique())
    return {
        "so_dong": n_rows,
        "so_cot": n_cols,
        "so_thieu_price": missing_price,
        "so_loai_phong": n_room_types,
    }


# Bài 3: Cắt riêng một quận
def filter_district_c1(df: pd.DataFrame, ten_quan: str) -> dict:
    bang = df[df["neighbourhood"] == ten_quan]
    ty_trong = float(len(bang) / len(df)) if len(df) > 0 else 0.0
    return {"bang": bang, "ty_trong": ty_trong}

def filter_district_c2(df: pd.DataFrame, ten_quan: str) -> dict:
    mask = df["neighbourhood"].eq(ten_quan)
    bang = df.loc[mask]
    ty_trong = float(mask.mean()) if len(df) > 0 else 0.0
    return {"bang": bang, "ty_trong": ty_trong}


# Bài 4: Lọc kết hợp trong quận
def count_segment_c1(listings: pd.DataFrame, room_type: str = "Entire home/apt", gia_toi_da: float = 60000.0) -> int:
    mask = (listings["room_type"] == room_type) & (listings["price"] <= gia_toi_da)
    return int(mask.sum())

def count_segment_c2(listings: pd.DataFrame, room_type: str = "Entire home/apt", gia_toi_da: float = 60000.0) -> int:
    mask = listings["room_type"].eq(room_type) & listings["price"].le(gia_toi_da)
    return int(mask.sum())


# Bài 5: Chỗ ở rẻ nhất quận
def cheapest_c1(listings: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    return listings.nsmallest(n, "price")[["name", "price"]]

def cheapest_c2(listings: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    return listings.dropna(subset=["price"]).sort_values("price", kind="stable").head(n).loc[:, ["name", "price"]]


# Bài 6: Sửa bảng bằng .loc và tính lại cột phụ thuộc
def discount_quote_c1(listings: pd.DataFrame, room_type: str = "Entire home/apt", giam: float = 0.10) -> pd.DataFrame:
    df_quote = listings[["id", "room_type", "price"]].copy()
    mask = df_quote["room_type"] == room_type
    df_quote.loc[mask, "price"] = df_quote.loc[mask, "price"] * (1.0 - giam)
    df_quote["tien_3_dem"] = df_quote["price"] * 3
    return df_quote

def discount_quote_c2(listings: pd.DataFrame, room_type: str = "Entire home/apt", giam: float = 0.10) -> pd.DataFrame:
    df_quote = listings[["id", "room_type", "price"]].copy()
    mask = df_quote["room_type"].eq(room_type)
    df_quote.loc[mask, "price"] *= (1.0 - giam)
    return df_quote.assign(tien_3_dem=lambda x: x["price"] * 3)


# Bài 7: So sánh với thành phố và ảnh hưởng của NaN
def share_below_c1(prices: pd.Series, nguong: float) -> dict:
    ty_le_tho = float((prices < nguong).mean())
    gia_sach = prices.dropna()
    ty_le_sach = float((gia_sach < nguong).mean()) if len(gia_sach) > 0 else 0.0
    so_thieu = int(prices.isna().sum())
    return {"ty_le_tho": ty_le_tho, "ty_le_sach": ty_le_sach, "so_thieu": so_thieu}

def share_below_c2(prices: pd.Series, nguong: float) -> dict:
    so_thieu = int(prices.isnull().sum())
    mask_below = prices.lt(nguong)
    ty_le_tho = float(mask_below.mean())
    valid_count = int(prices.notna().sum())
    ty_le_sach = float(mask_below.sum() / valid_count) if valid_count > 0 else 0.0
    return {"ty_le_tho": ty_le_tho, "ty_le_sach": ty_le_sach, "so_thieu": so_thieu}


# Bài 8: Cơ cấu loại phòng và tỷ lệ thiếu
def room_mix_c1(listings: pd.DataFrame) -> dict:
    co_cau = listings["room_type"].value_counts(normalize=True)
    thieu_pct = round(float(listings["price"].isna().mean() * 100), 2)
    return {"co_cau": co_cau, "thieu_pct": thieu_pct}

def room_mix_c2(listings: pd.DataFrame) -> dict:
    total = len(listings)
    if total == 0:
        return {"co_cau": pd.Series(dtype=float), "thieu_pct": 0.0}
    co_cau = listings.groupby("room_type", observed=False).size() / total
    co_cau = co_cau.sort_values(ascending=False)
    thieu_pct = round(float(listings["price"].isnull().sum() / total * 100), 2)
    return {"co_cau": co_cau, "thieu_pct": thieu_pct}


# Bài 9: Xuất hồ sơ ra file và đọc lại
def export_profile_c1(listings: pd.DataFrame, ten_quan: str, path) -> pd.DataFrame:
    ty_le_nc = round(float((listings["room_type"] == "Entire home/apt").mean()), 3)
    thieu_pct = round(float(listings["price"].isna().mean() * 100), 2)
    ho_so = pd.DataFrame([{
        "quan": ten_quan,
        "so_cho_o": len(listings),
        "gia_trung_vi": float(listings["price"].median()),
        "ty_le_nguyen_can": ty_le_nc,
        "ty_le_thieu_gia_pct": thieu_pct,
    }])
    ho_so.to_csv(path, index=False, encoding="utf-8")
    return pd.read_csv(path)

def export_profile_c2(listings: pd.DataFrame, ten_quan: str, path) -> pd.DataFrame:
    ty_le_nc = round(float(listings["room_type"].eq("Entire home/apt").mean()), 3)
    thieu_pct = round(float(listings["price"].isnull().sum() / len(listings) * 100), 2)
    ho_so = pd.DataFrame({
        "quan": [ten_quan],
        "so_cho_o": [int(len(listings))],
        "gia_trung_vi": [float(listings["price"].median())],
        "ty_le_nguyen_can": [ty_le_nc],
        "ty_le_thieu_gia_pct": [thieu_pct],
    })
    ho_so.to_csv(path, index=False, encoding="utf-8")
    return pd.read_csv(path, dtype={"quan": str, "so_cho_o": int, "gia_trung_vi": float,
                                    "ty_le_nguyen_can": float, "ty_le_thieu_gia_pct": float})


# Bài 10 (Mở rộng 1): Tự động hóa hồ sơ quận qua tham số cấu hình
def profile_district_pipeline_c1(df: pd.DataFrame, ten_quan: str) -> dict:
    sub = df[df["neighbourhood"] == ten_quan]
    if len(sub) == 0:
        return {"quan": ten_quan, "so_cho_o": 0, "ty_trong": 0.0, "gia_trung_vi": np.nan, "ty_le_nguyen_can": 0.0}
    return {
        "quan": ten_quan,
        "so_cho_o": len(sub),
        "ty_trong": round(float(len(sub) / len(df)), 3),
        "gia_trung_vi": float(sub["price"].median()),
        "ty_le_nguyen_can": round(float((sub["room_type"] == "Entire home/apt").mean()), 3),
    }

def profile_district_pipeline_c2(df: pd.DataFrame, ten_quan: str) -> dict:
    mask = df["neighbourhood"].eq(ten_quan)
    sub = df.loc[mask]
    n_sub = len(sub)
    if n_sub == 0:
        return {"quan": ten_quan, "so_cho_o": 0, "ty_trong": 0.0, "gia_trung_vi": np.nan, "ty_le_nguyen_can": 0.0}
    return {
        "quan": ten_quan,
        "so_cho_o": n_sub,
        "ty_trong": round(float(mask.mean()), 3),
        "gia_trung_vi": float(sub["price"].median()),
        "ty_le_nguyen_can": round(float(sub["room_type"].eq("Entire home/apt").mean()), 3),
    }


# Bài 11 (Mở rộng 2): Tìm quận có giá trung vị thấp nhất bằng groupby
def find_affordable_popular_district_c1(df: pd.DataFrame, min_listings: int = 3) -> tuple:
    summary = df.groupby("neighbourhood")["price"].agg(["median", "size"])
    filtered = summary[summary["size"] >= min_listings]
    cheapest_row = filtered.nsmallest(1, "median").iloc[0]
    return cheapest_row.name, float(cheapest_row["median"]), int(cheapest_row["size"])

def find_affordable_popular_district_c2(df: pd.DataFrame, min_listings: int = 3) -> tuple:
    grouped = (
        df.groupby("neighbourhood")
        .agg(gia_trung_vi=("price", "median"), so_cho_o=("price", "size"))
        .query("so_cho_o >= @min_listings")
        .sort_values("gia_trung_vi", ascending=True)
    )
    first = grouped.iloc[0]
    return first.name, float(first["gia_trung_vi"]), int(first["so_cho_o"])


# Bài 12 (Mở rộng 3): Khắc phục lỗi Chained Assignment
def safe_apply_discount_c1(df: pd.DataFrame, room_type: str, giam: float) -> pd.DataFrame:
    out = df.copy()
    mask = out["room_type"] == room_type
    out.loc[mask, "price"] = out.loc[mask, "price"] * (1.0 - giam)
    return out

def safe_apply_discount_c2(df: pd.DataFrame, room_type: str, giam: float) -> pd.DataFrame:
    out = df.copy()
    mask = out["room_type"].eq(room_type)
    new_price = np.where(mask, out["price"] * (1.0 - giam), out["price"])
    out["price"] = new_price
    return out


# ==============================================================================
# 2. Bộ kiểm thử toàn diện
# ==============================================================================

def run_all_tests():
    print("=" * 70)
    print("BẮT ĐẦU CHẠY KIỂM ĐỊNH TOÀN DIỆN CHO LAB 04")
    print("=" * 70)

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 1: data-lab-04-01
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-01] Kiểm tra Bài 1: Chọn cột, chọn hàng và tỷ lệ ---")
    before_demo = DEMO.copy()
    res1_c1 = select_basics_c1(DEMO)
    res1_c2 = select_basics_c2(DEMO)

    # Đối chiếu 2 cách
    assert res1_c1["cot_gia"].equals(res1_c2["cot_gia"]), "Bài 1: Cột giá không khớp giữa 2 cách"
    pd.testing.assert_frame_equal(res1_c1["bang_con"], res1_c2["bang_con"])
    assert math.isclose(res1_c1["ty_le_private"], res1_c2["ty_le_private"], abs_tol=1e-9)
    pd.testing.assert_frame_equal(res1_c1["nguyen_can"], res1_c2["nguyen_can"])
    assert res1_c1["gia_nguyen_can"].equals(res1_c2["gia_nguyen_can"])

    # Xác minh chỉ số bài giảng
    assert round(res1_c1["ty_le_private"], 3) == 0.333
    assert len(res1_c1["nguyen_can"]) == 6
    assert list(res1_c1["gia_nguyen_can"].index) == [0, 2, 3, 5, 6, 8]
    assert res1_c1["gia_nguyen_can"].median() == 60000.0
    pd.testing.assert_frame_equal(DEMO, before_demo, obj="DEMO không bị sửa")

    # Kiểm tra biên: bảng 1 dòng
    one_row = DEMO.iloc[[1]].copy()
    res_one = select_basics_c1(one_row)
    assert res_one["ty_le_private"] == 1.0
    assert len(res_one["nguyen_can"]) == 0
    print("✓ Bài 1 ĐẠT (so khớp 2 cách, kiểm tra index, kiểu trả về và bất biến)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 2: data-lab-04-02
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-02] Kiểm tra Bài 2: Thói quen 5 bước ---")
    res2_c1 = extract_5step_metrics_c1(DEMO)
    res2_c2 = extract_5step_metrics_c2(DEMO)
    assert res2_c1 == res2_c2, "Bài 2: Hai cách cho kết quả chỉ số khác nhau"
    assert res2_c1 == {"so_dong": 12, "so_cot": 6, "so_thieu_price": 2, "so_loai_phong": 4}
    print("✓ Bài 2 ĐẠT (12 dòng, 6 cột, 2 giá thiếu, 4 loại phòng)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 3: data-lab-04-03
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-03] Kiểm tra Bài 3: Cắt riêng một quận ---")
    res3_c1 = filter_district_c1(DEMO, "Ñuñoa")
    res3_c2 = filter_district_c2(DEMO, "Ñuñoa")
    pd.testing.assert_frame_equal(res3_c1["bang"], res3_c2["bang"])
    assert res3_c1["ty_trong"] == res3_c2["ty_trong"] == 0.5
    assert len(res3_c1["bang"]) == 6

    # Kiểm tra trường hợp biên: quận không tồn tại
    empty_dist = filter_district_c1(DEMO, "Las Condes")
    assert len(empty_dist["bang"]) == 0 and empty_dist["ty_trong"] == 0.0
    print("✓ Bài 3 ĐẠT (Ñuñoa có 6 căn = 50%, quận lạ trả bảng rỗng và tỷ trọng 0)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 4: data-lab-04-04
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-04] Kiểm tra Bài 4: Lọc kết hợp trong quận ---")
    nu_demo = res3_c1["bang"]
    res4_c1 = count_segment_c1(nu_demo)
    res4_c2 = count_segment_c2(nu_demo)
    assert res4_c1 == res4_c2 == 2, "Bài 4: Kết quả lọc kết hợp không khớp"

    # Kiểm tra trường hợp biên: giá đúng bằng ngưỡng (<= 60000)
    assert count_segment_c1(nu_demo, "Entire home/apt", 45000) == 1
    assert count_segment_c1(nu_demo, "Private room", 10000) == 1
    assert count_segment_c1(pd.DataFrame(columns=["room_type", "price"])) == 0
    print("✓ Bài 4 ĐẠT (tìm được 2 căn nguyên căn giá <= 60000, kiểm tra biên rỗng và NaN)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 5: data-lab-04-05
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-05] Kiểm tra Bài 5: Chỗ ở rẻ nhất quận ---")
    res5_c1 = cheapest_c1(nu_demo, 3)
    res5_c2 = cheapest_c2(nu_demo, 3)
    pd.testing.assert_frame_equal(res5_c1, res5_c2)
    assert list(res5_c1.index) == [4, 1, 0]
    assert list(res5_c1["price"]) == [2500.0, 18000.0, 45000.0]

    # Kiểm tra n=5 không chứa NaN
    res5_5 = cheapest_c1(nu_demo, 5)
    assert len(res5_5) == 5 and res5_5["price"].notna().all()
    print("✓ Bài 5 ĐẠT (nsmallest bảo toàn index, bỏ qua NaN, khớp kết quả sắp xếp)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 6: data-lab-04-06
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-06] Kiểm tra Bài 6: Sửa bảng bằng .loc và tính lại cột ---")
    before_nu = nu_demo.copy()
    res6_c1 = discount_quote_c1(nu_demo)
    res6_c2 = discount_quote_c2(nu_demo)
    pd.testing.assert_frame_equal(res6_c1, res6_c2)
    np.testing.assert_allclose(res6_c1["price"], [40500, 18000, 64800, np.nan, 2500, 54000])
    np.testing.assert_allclose(res6_c1["tien_3_dem"], [121500, 54000, 194400, np.nan, 7500, 162000])
    pd.testing.assert_frame_equal(nu_demo, before_nu, obj="nu_demo không bị sửa đổi")
    print("✓ Bài 6 ĐẠT (giảm 10% cho Entire home/apt, tính lại tien_3_dem, giữ nguyên bảng gốc)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 7: data-lab-04-07
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-07] Kiểm tra Bài 7: So sánh với thành phố và ảnh hưởng của NaN ---")
    med_demo = DEMO["price"].median()
    assert med_demo == 42500.0
    res7_c1 = share_below_c1(nu_demo["price"], med_demo)
    res7_c2 = share_below_c2(nu_demo["price"], med_demo)
    assert res7_c1 == res7_c2
    assert round(res7_c1["ty_le_tho"], 3) == 0.333
    assert res7_c1["ty_le_sach"] == 0.4
    assert res7_c1["so_thieu"] == 1
    print("✓ Bài 7 ĐẠT (mẫu số thô: 6, mẫu số sạch: 5, tỷ lệ lệch nhau đúng 6.7 điểm %)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 8: data-lab-04-08
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-08] Kiểm tra Bài 8: Cơ cấu loại phòng và mức thiếu ---")
    res8_c1 = room_mix_c1(nu_demo)
    res8_c2 = room_mix_c2(nu_demo)
    pd.testing.assert_series_equal(res8_c1["co_cau"].sort_index(), res8_c2["co_cau"].sort_index(), check_names=False)
    assert res8_c1["thieu_pct"] == res8_c2["thieu_pct"] == 16.67
    assert round(res8_c1["co_cau"]["Entire home/apt"], 3) == 0.667
    print("✓ Bài 8 ĐẠT (cơ cấu phòng chuẩn hóa, tỷ lệ thiếu 16.67%)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 9: data-lab-04-09
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-09] Kiểm tra Bài 9: Xuất hồ sơ ra file và đọc lại ---")
    with tempfile.TemporaryDirectory() as td:
        p1 = Path(td) / "ho_so_1.csv"
        p2 = Path(td) / "ho_so_2.csv"
        doc1 = export_profile_c1(nu_demo, "Ñuñoa", p1)
        doc2 = export_profile_c2(nu_demo, "Ñuñoa", p2)
        pd.testing.assert_frame_equal(doc1, doc2)
        header = p1.read_text(encoding="utf-8").splitlines()[0]
        assert header == "quan,so_cho_o,gia_trung_vi,ty_le_nguyen_can,ty_le_thieu_gia_pct"
        assert doc1.shape == (1, 5)
        assert doc1.loc[0, "quan"] == "Ñuñoa"
        assert doc1.loc[0, "so_cho_o"] == 6
        assert doc1.loc[0, "gia_trung_vi"] == 45000.0
        assert doc1.loc[0, "ty_le_nguyen_can"] == 0.667
        assert doc1.loc[0, "ty_le_thieu_gia_pct"] == 16.67
    print("✓ Bài 9 ĐẠT (xuất file CSV UTF-8 không lưu index, đọc lại đúng các bất biến)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 10 (Mở rộng 1): data-lab-04-10
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-10] Kiểm tra Mở rộng 1: Hồ sơ quận thứ hai ---")
    pipe1_nu = profile_district_pipeline_c1(DEMO, "Ñuñoa")
    pipe2_nu = profile_district_pipeline_c2(DEMO, "Ñuñoa")
    assert pipe1_nu == pipe2_nu
    pipe1_pro = profile_district_pipeline_c1(DEMO, "Providencia")
    pipe2_pro = profile_district_pipeline_c2(DEMO, "Providencia")
    assert pipe1_pro == pipe2_pro
    assert pipe1_pro["so_cho_o"] == 2 and pipe1_pro["gia_trung_vi"] == 55000.0
    print("✓ Bài 10 ĐẠT (pipeline chạy linh hoạt trên các quận khác nhau)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 11 (Mở rộng 2): data-lab-04-11
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-11] Kiểm tra Mở rộng 2: Tìm quận có giá thấp nhất bằng groupby ---")
    res11_c1 = find_affordable_popular_district_c1(DEMO, min_listings=3)
    res11_c2 = find_affordable_popular_district_c2(DEMO, min_listings=3)
    assert res11_c1 == res11_c2
    # Với ngưỡng size >= 3: Ñuñoa (size 6, median 45000), Santiago (size 4, median 40000).
    # Quận có giá thấp nhất là Santiago với trung vị 40.000 CLP.
    assert res11_c1 == ("Santiago", 40000.0, 4)
    print("✓ Bài 11 ĐẠT (tìm được Santiago có median 40.000 CLP với size >= 3)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 12 (Mở rộng 3): data-lab-04-12
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-04-12] Kiểm tra Mở rộng 3: Khắc phục lỗi Chained Assignment ---")
    res12_c1 = safe_apply_discount_c1(nu_demo, "Entire home/apt", 0.10)
    res12_c2 = safe_apply_discount_c2(nu_demo, "Entire home/apt", 0.10)
    pd.testing.assert_frame_equal(res12_c1, res12_c2)
    assert res12_c1.loc[0, "price"] == 40500.0
    print("✓ Bài 12 ĐẠT (cập nhật giá an toàn qua .loc và np.where, triệt tiêu lỗi gán chuỗi)")

    # --------------------------------------------------------------------------
    # Kiểm tra cú pháp Markdown và thực thi động toàn bộ các khối mã nguồn trong lab-04.md
    # --------------------------------------------------------------------------
    lab_path = Path(__file__).resolve().parents[1] / "raw_materials/xu-ly-du-lieu/labs/lab-04.md"
    if lab_path.exists():
        content = lab_path.read_text(encoding="utf-8")
        assert "::: exercise" in content and "::: solution" in content
        for i in range(1, 13):
            span_id = f"data-lab-04-{i:02d}"
            assert f'id="{span_id}"' in content or f"id='{span_id}'" in content, f"Thiếu span id {span_id} trong {lab_path.name}"

        # 1. Kiểm tra không chứa heading H1 ngoài code fence
        lines = content.splitlines()
        in_code_fence = False
        for line_idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if not in_code_fence and stripped.startswith("# "):
                raise AssertionError(f"Phát hiện heading H1 ngoài code fence tại dòng {line_idx} trong {lab_path.name}: '{line}'")

        # 2. Kiểm tra không chứa thuật ngữ dịch máy bị cấm theo nguyên tắc StudyHub
        forbidden_terms = ["hợp đồng hàm", "hợp đồng file", "hợp đồng dữ liệu"]
        for term in forbidden_terms:
            assert term not in content.lower(), f"Phát hiện thuật ngữ dịch máy bị cấm: '{term}'"

        # 3. Trích xuất, kiểm tra cú pháp AST và chạy thử động toàn bộ các khối mã Python trong lab-04.md
        import ast
        import re
        blocks = re.findall(r"```python\s*(.*?)\s*```", content, re.DOTALL)
        for idx, block in enumerate(blocks):
            try:
                ast.parse(block, filename=f"block_{idx}.py")
            except SyntaxError as syn_err:
                raise AssertionError(f"Lỗi cú pháp AST tại khối mã Python thứ {idx} trong {lab_path.name}: {syn_err}")

        from contextlib import redirect_stdout, redirect_stderr
        from io import StringIO
        import os
        from tempfile import TemporaryDirectory
        ns_doc = {}
        previous_directory = Path.cwd()
        with TemporaryDirectory(prefix="studyhub-lab04-") as temporary:
            try:
                os.chdir(temporary)
                for idx, block in enumerate(blocks):
                    try:
                        with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                            exec(block, ns_doc)
                    except Exception as exc:
                        raise AssertionError(f"Lỗi khi thực thi khối mã Python thứ {idx} trong {lab_path.name}: {type(exc).__name__}: {exc}")
            finally:
                os.chdir(previous_directory)
        print(f"\n✓ Kiểm tra cấu trúc Markdown: Không chứa heading H1 ngoài code fence, đủ 12 exercise span IDs, container ::: exercise và ::: solution chuẩn mực, danh mục từ cấm cơ bản không vi phạm.")
        print(f"✓ Kiểm tra AST và Thực thi: Toàn bộ {len(blocks)} khối mã nguồn Python trong {lab_path.name} đã được phân tích AST và chạy thành công!")

    print("\n" + "=" * 70)
    print("TẤT CẢ 12 BÀI TẬP VÀ PHÉP KIỂM ĐỊNH ĐÃ VƯỢT QUA 100% THÀNH CÔNG!")
    print("=" * 70)

if __name__ == "__main__":
    run_all_tests()
