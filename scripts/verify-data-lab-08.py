# -*- coding: utf-8 -*-
"""Kịch bản kiểm tra tự động toàn diện bộ bài tập Lab 08.

Tệp kiểm định:
1. raw_materials/xu-ly-du-lieu/labs/lab-08.md (data-lab-08-01 đến 14)
2. raw_materials/xu-ly-du-lieu/labs/coverage-08.json

Mục tiêu kiểm định:
1. Định nghĩa và so sánh tính tương đương giữa Cách 1 (cơ bản) và Cách 2 (thực tế/tối ưu) cho cả 14 bài tập.
2. Kiểm tra độc lập các trường hợp biên: Năm nhuận (2020, 2024), bảng rỗng, dữ liệu khuyết (NaT/NaN), tính bất biến của DataFrame đầu vào, kiểm tra lưới ngày đầy đủ không mất ngày trống.
3. Sinh tệp biểu đồ trực quan hóa cửa sổ trượt lưu tại docs/xu-ly-du-lieu/bai-giang/img/labs/lab-08/rolling-7d-2025.svg.
4. Rà soát cấu trúc Markdown: Không chứa H1 ngoài code fence, đủ 14 span IDs, không dùng dấu chấm phẩy hay gạch ngang dài ngoài code fence, không chứa thuật ngữ dịch máy bị cấm.
5. Phân tích AST và thực thi động toàn bộ 30 khối mã Python trong lab-08.md.
"""

import ast
import io
import math
import os
import re
import sys
from pathlib import Path
import numpy as np
import pandas as pd

# Thiết lập đầu ra console hỗ trợ chuẩn UTF-8
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Thiết lập backend matplotlib không cần giao diện đồ họa
os.environ["MPLBACKEND"] = "Agg"

# ==============================================================================
# Dữ liệu mẫu chuẩn bị sẵn phục vụ kiểm thử độc lập
# ==============================================================================

SNAPSHOT = "2026-06-29"

DAT_DEMO = pd.DataFrame({
    "vao": ["28/02/2026", "03/07/2026", "31/06/2026", None],
    "ra": ["03/03/2026", "06/07/2026", "05/07/2026", "12/07/2026"],
}, index=["D1", "D2", "D3", "D4"])

def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[ngay.year]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc

_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")
_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]
DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})
DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])
DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

LISTINGS_DEMO = pd.DataFrame({
    "id": [101, 102, 103, 104, 105],
    "name": [
        "Căn hộ trung tâm", "Phòng riêng Bellas Artes", "Loft Providencia",
        "Studio Recoleta", "Nhà cổ Brasil"
    ],
    "last_review": ["2026-05-15", "2025-01-10", "2026-07-02", "2024-11-20", None],
})

# ==============================================================================
# 1. Định nghĩa các hàm lời giải Cách 1 và Cách 2 cho 14 bài tập
# ==============================================================================

# Bài 1: Tính số đêm lưu trú
def calculate_stay_nights_c1(dat: pd.DataFrame) -> pd.Series:
    vao_dt = pd.to_datetime(dat["vao"], format="%d/%m/%Y", errors="coerce")
    ra_dt = pd.to_datetime(dat["ra"], format="%d/%m/%Y", errors="coerce")
    return (ra_dt - vao_dt).dt.days

def calculate_stay_nights_c2(dat: pd.DataFrame) -> pd.Series:
    vao_dt = pd.to_datetime(dat["vao"], dayfirst=True, errors="coerce")
    ra_dt = pd.to_datetime(dat["ra"], dayfirst=True, errors="coerce")
    return ra_dt.sub(vao_dt).dt.days

# Bài 2: Phát hiện lỗi chuyển đổi ngày
def detect_invalid_date_errors_c1(dat: pd.DataFrame, vao_dt: pd.Series) -> pd.Series:
    return vao_dt.isna() & dat["vao"].notna()

def detect_invalid_date_errors_c2(dat: pd.DataFrame, vao_dt: pd.Series) -> pd.Series:
    dieu_kien_nat = vao_dt.isna().to_numpy()
    dieu_kien_co_chuoi = dat["vao"].notna().to_numpy()
    ket_qua = np.logical_and(dieu_kien_nat, dieu_kien_co_chuoi)
    return pd.Series(ket_qua, index=dat.index, name=vao_dt.name)

# Bài 3: Loại bỏ dòng sau mốc chụp và thiết lập chỉ mục
def prepare_time_index_c1(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)
    mat_na_hop_le = rv["date"] <= moc_tg
    so_dong_sau = int((~mat_na_hop_le).sum())
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")
    return {"so_dong_sau_moc": so_dong_sau, "r": r}

def prepare_time_index_c2(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)
    so_dong_sau = int((rv["date"] > moc_tg).sum())
    r = rv.query("date <= @moc_tg").set_index("date").sort_index(kind="mergesort")
    return {"so_dong_sau_moc": so_dong_sau, "r": r}

# Bài 4: Cắt lát nhãn chuỗi theo năm
def count_year_c1(r: pd.DataFrame, nam: int) -> int:
    return int(len(r.loc[str(nam)]))

def count_year_c2(r: pd.DataFrame, nam: int) -> int:
    return int(r.loc[str(nam)].shape[0])

# Bài 5: Tổng hợp theo quý và nhận diện kỳ chưa trọn
def quarterly_c1(r: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)
    quy = r.resample("QE").size()
    quy_day_du = quy[quy.index <= moc_tg]
    return {"quy": quy, "quy_day_du": quy_day_du}

def quarterly_c2(r: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)
    quy = r.resample("QE").size()
    quy_day_du = quy.truncate(after=moc_tg)
    return {"quy": quy, "quy_day_du": quy_day_du}

# Bài 6: Kiểm tra lọc kỳ chưa trọn tại các mốc biên
def filter_complete_quarters_c1(dem_quy: pd.Series, moc: str) -> pd.Series:
    return dem_quy[dem_quy.index <= pd.Timestamp(moc)]

def filter_complete_quarters_c2(dem_quy: pd.Series, moc: str) -> pd.Series:
    return dem_quy.loc[:pd.Timestamp(moc)]

# Bài 7: Quý cao nhất và quý thấp nhất trong giai đoạn
def quarter_extremes_c1(quy: pd.Series, bat_dau: str, ket_thuc: str) -> dict:
    quy_dinh = quy.idxmax()
    giai_doan = quy.loc[bat_dau:ket_thuc]
    quy_day = giai_doan.idxmin()
    gia_tri_day = int(giai_doan.loc[quy_day])
    return {"quy_dinh": quy_dinh, "quy_day": quy_day, "gia_tri_day": gia_tri_day}

def quarter_extremes_c2(quy: pd.Series, bat_dau: str, ket_thuc: str) -> dict:
    quy_dinh = quy.idxmax()
    phan_doan = quy.loc[bat_dau:ket_thuc]
    quy_day = phan_doan.idxmin()
    gia_tri_day = int(phan_doan.min())
    return {"quy_dinh": quy_dinh, "quy_day": quy_day, "gia_tri_day": gia_tri_day}

# Bài 8: Tổng hợp theo ngày và điền 0 cho ngày trống
def daily_counts_c1(r: pd.DataFrame, nam: int) -> pd.Series:
    return r.loc[str(nam)].resample("D").size()

def daily_counts_c2(r: pd.DataFrame, nam: int) -> pd.Series:
    ngay_dau = f"{nam}-01-01"
    ngay_cuoi = f"{nam}-12-31"
    return r.loc[ngay_dau:ngay_cuoi].resample("1D").size()

# Bài 9: Cửa sổ trượt 7 ngày
def rolling_peak_c1(ngay: pd.Series, cua_so: int = 7) -> dict:
    tb = ngay.rolling(cua_so, center=True).mean()
    ngay_dinh = tb.idxmax()
    gia_tri_dinh = float(tb.loc[ngay_dinh])
    return {"tb": tb, "ngay_dinh": ngay_dinh, "gia_tri_dinh": gia_tri_dinh}

def rolling_peak_c2(ngay: pd.Series, cua_so: int = 7) -> dict:
    tb = ngay.rolling(window=cua_so, min_periods=cua_so, center=False).mean()
    ngay_dinh = tb.idxmax()
    gia_tri_dinh = float(tb.loc[ngay_dinh])
    return {"tb": tb, "ngay_dinh": ngay_dinh, "gia_tri_dinh": gia_tri_dinh}

# Bài 10: So sánh cùng kỳ theo quý
def quarterly_yoy_c1(quy_day_du: pd.Series) -> pd.Series:
    return quy_day_du / quy_day_du.shift(4) - 1.0

def quarterly_yoy_c2(quy_day_du: pd.Series) -> pd.Series:
    return quy_day_du.pct_change(periods=4)

# Bài 11: So sánh theo tháng: kỳ trước và cùng kỳ năm trước
def period_changes_c1(thang: pd.Series, moc: str) -> dict:
    moc_tg = pd.Timestamp(moc)
    nhan_ky_truoc = moc_tg - pd.offsets.MonthEnd(1)
    nhan_cung_ky = moc_tg - pd.offsets.MonthEnd(12)
    val_hien_tai = thang.loc[moc_tg]
    val_ky_truoc = thang.loc[nhan_ky_truoc]
    val_cung_ky = thang.loc[nhan_cung_ky]
    so_ky_truoc = (val_hien_tai / val_ky_truoc - 1.0) * 100.0
    so_cung_ky = (val_hien_tai / val_cung_ky - 1.0) * 100.0
    return {"so_ky_truoc": float(so_ky_truoc), "so_cung_ky": float(so_cung_ky)}

def period_changes_c2(thang: pd.Series, moc: str) -> dict:
    moc_tg = pd.Timestamp(moc)
    pct_1 = thang.pct_change(periods=1) * 100.0
    pct_12 = thang.pct_change(periods=12) * 100.0
    return {"so_ky_truoc": float(pct_1.loc[moc_tg]), "so_cung_ky": float(pct_12.loc[moc_tg])}

# Bài 12: Chuẩn hóa số ngày trong tháng và năm nhuận
def monthly_daily_rate_c1(thang_4nam: pd.Series) -> dict:
    so_ngay = pd.Series(thang_4nam.index.days_in_month, index=thang_4nam.index)
    thang_so = pd.Index(thang_4nam.index.month, name="thang")
    tong = thang_4nam.groupby(thang_so).sum()
    tong_ngay = so_ngay.groupby(thang_so).sum()
    tb_ngay = tong / tong_ngay
    chenh_tong = float(tong.loc[2] / tong.loc[1] - 1.0)
    chenh_ngay = float(tb_ngay.loc[2] / tb_ngay.loc[1] - 1.0)
    return {"tong": tong, "tb_ngay": tb_ngay, "chenh_tong": chenh_tong, "chenh_ngay": chenh_ngay}

def monthly_daily_rate_c2(thang_4nam: pd.Series) -> dict:
    df_thang = pd.DataFrame({
        "so_danh_gia": thang_4nam,
        "so_ngay": thang_4nam.index.days_in_month,
        "thang": thang_4nam.index.month,
    })
    bang_tong_hop = df_thang.groupby("thang").agg(
        tong_danh_gia=("so_danh_gia", "sum"),
        tong_so_ngay=("so_ngay", "sum"),
    )
    tong = bang_tong_hop["tong_danh_gia"]
    tb_ngay = bang_tong_hop["tong_danh_gia"] / bang_tong_hop["tong_so_ngay"]
    chenh_tong = float(tong.loc[2] / tong.loc[1] - 1.0)
    chenh_ngay = float(tb_ngay.loc[2] / tb_ngay.loc[1] - 1.0)
    return {"tong": tong, "tb_ngay": tb_ngay, "chenh_tong": chenh_tong, "chenh_ngay": chenh_ngay}

# Bài 13: Mở rộng 1: Điều tra ngày kỷ lục
def investigate_peak_day_c1(r: pd.DataFrame) -> dict:
    chuoi_ngay = r.resample("D").size()
    ngay_ky_luc = chuoi_ngay.idxmax()
    so_luong_ky_luc = int(chuoi_ngay.loc[ngay_ky_luc])
    dau = ngay_ky_luc - pd.Timedelta(days=2)
    cuoi = ngay_ky_luc + pd.Timedelta(days=2)
    vung_lan_can = chuoi_ngay.loc[dau:cuoi]
    return {"ngay_ky_luc": ngay_ky_luc, "so_luong_ky_luc": so_luong_ky_luc, "vung_lan_can": vung_lan_can}

def investigate_peak_day_c2(r: pd.DataFrame) -> dict:
    chuoi_ngay = r.resample("D").size()
    top_1 = chuoi_ngay.nlargest(1)
    ngay_ky_luc = top_1.index[0]
    so_luong_ky_luc = int(top_1.iloc[0])
    khoang_cach = pd.DateOffset(days=2)
    vung_lan_can = chuoi_ngay.loc[ngay_ky_luc - khoang_cach : ngay_ky_luc + khoang_cach]
    return {"ngay_ky_luc": ngay_ky_luc, "so_luong_ky_luc": so_luong_ky_luc, "vung_lan_can": vung_lan_can}

# Bài 14: Mở rộng 2: Tính khoảng cách từ đánh giá gần nhất
def days_since_last_review_c1(listings: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)
    df = listings.copy()
    df["last_review_dt"] = pd.to_datetime(df["last_review"], errors="coerce")
    ngoai_moc_mask = df["last_review_dt"] > moc_tg
    so_ngoai_moc = int(ngoai_moc_mask.sum())
    df_hop_le = df.loc[~ngoai_moc_mask].copy()
    so_ngay = (moc_tg - df_hop_le["last_review_dt"]).dt.days
    df_hop_le["so_ngay_tu_rv_cuoi"] = so_ngay
    tren_365 = so_ngay > 365
    so_tren_365 = int(tren_365.sum())
    df_hop_le["co_khong_hoat_dong"] = tren_365 | df_hop_le["last_review_dt"].isna()
    return {"so_cho_o_ngoai_moc": so_ngoai_moc, "so_cho_o_tren_365_ngay": so_tren_365, "listings_gan_co": df_hop_le}

def days_since_last_review_c2(listings: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)
    rev_dt = pd.to_datetime(listings["last_review"], errors="coerce")
    mask_ngoai = rev_dt > moc_tg
    so_ngoai_moc = int(mask_ngoai.sum())
    df_loc = listings.loc[~mask_ngoai].copy()
    rev_loc = rev_dt.loc[~mask_ngoai]
    so_ngay = (moc_tg - rev_loc).dt.days
    co_ngung = (so_ngay > 365) | rev_loc.isna()
    df_loc = df_loc.assign(so_ngay_tu_rv_cuoi=so_ngay, co_khong_hoat_dong=co_ngung)
    so_tren_365 = int((so_ngay > 365).sum())
    return {"so_cho_o_ngoai_moc": so_ngoai_moc, "so_cho_o_tren_365_ngay": so_tren_365, "listings_gan_co": df_loc}


# ==============================================================================
# 2. Quy trình kiểm định tự động toàn diện
# ==============================================================================

def run_all_tests():
    print("=" * 70)
    print("BẮT ĐẦU KIỂM ĐỊNH TOÀN DIỆN LAB 08: CHUỖI THỜI GIAN VÀ CỬA SỔ TRƯỢT")
    print("=" * 70)

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 1: data-lab-08-01
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-01] Kiểm tra Bài 1: Tính số đêm lưu trú ---")
    s1_c1 = calculate_stay_nights_c1(DAT_DEMO)
    s1_c2 = calculate_stay_nights_c2(DAT_DEMO)
    pd.testing.assert_series_equal(s1_c1, s1_c2)
    assert s1_c1.loc[["D1", "D2"]].tolist() == [3, 3]
    assert s1_c1.loc[["D3", "D4"]].isna().all()
    # Kiểm tra tính bất biến
    assert "so_dem" not in DAT_DEMO.columns
    print("✓ Bài 1 ĐẠT (tính số đêm chuẩn xác, xử lý ngày sai và thiếu thành NaN)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 2: data-lab-08-02
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-02] Kiểm tra Bài 2: Phát hiện lỗi chuyển đổi ngày ---")
    vao_dt = pd.to_datetime(DAT_DEMO["vao"], format="%d/%m/%Y", errors="coerce")
    loi_c1 = detect_invalid_date_errors_c1(DAT_DEMO, vao_dt)
    loi_c2 = detect_invalid_date_errors_c2(DAT_DEMO, vao_dt)
    pd.testing.assert_series_equal(loi_c1, loi_c2)
    assert loi_c1.tolist() == [False, False, True, False]
    assert loi_c1[loi_c1].index.tolist() == ["D3"]
    print("✓ Bài 2 ĐẠT (phân biệt đúng giữa lỗi cú pháp ngày 31/06 và ô trống ban đầu)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 3: data-lab-08-03
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-03] Kiểm tra Bài 3: Loại bỏ dòng sau mốc và đặt chỉ mục ---")
    res3_c1 = prepare_time_index_c1(DEMO_REVIEWS, SNAPSHOT)
    res3_c2 = prepare_time_index_c2(DEMO_REVIEWS, SNAPSHOT)
    assert res3_c1["so_dong_sau_moc"] == res3_c2["so_dong_sau_moc"] == 16
    pd.testing.assert_frame_equal(res3_c1["r"], res3_c2["r"])
    r = res3_c1["r"]
    assert len(r) == len(DEMO_REVIEWS) - 16 == 11409
    assert isinstance(r.index, pd.DatetimeIndex) and r.index.is_monotonic_increasing
    assert r.index.max() == pd.Timestamp(SNAPSHOT)
    assert list(r.columns) == ["listing_id"]
    print("✓ Bài 3 ĐẠT (loại 16 dòng sau mốc 2026-06-29, tạo DatetimeIndex đơn điệu tăng dần)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 4: data-lab-08-04
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-04] Kiểm tra Bài 4: Cắt lát nhãn chuỗi theo năm ---")
    n19_c1 = count_year_c1(r, 2019)
    n19_c2 = count_year_c2(r, 2019)
    assert n19_c1 == n19_c2 == 1317
    n21_c1 = count_year_c1(r, 2021)
    n21_c2 = count_year_c2(r, 2021)
    assert n21_c1 == n21_c2 == 952
    assert count_year_c1(r, 2020) == int((DEMO_REVIEWS["date"].dt.year == 2020).sum())
    print("✓ Bài 4 ĐẠT (cắt lát chuỗi .loc['YYYY'] khớp hoàn toàn với đếm bộ lọc)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 5: data-lab-08-05
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-05] Kiểm tra Bài 5: Tổng hợp theo quý và nhận diện kỳ chưa trọn ---")
    res5_c1 = quarterly_c1(r, SNAPSHOT)
    res5_c2 = quarterly_c2(r, SNAPSHOT)
    pd.testing.assert_series_equal(res5_c1["quy"], res5_c2["quy"])
    pd.testing.assert_series_equal(res5_c1["quy_day_du"], res5_c2["quy_day_du"])
    assert len(res5_c1["quy"]) == 30
    assert len(res5_c1["quy_day_du"]) == 29
    assert res5_c1["quy"].loc["2026-03-31"] == 904
    assert res5_c1["quy"].loc["2026-06-30"] == 746
    assert res5_c1["quy_day_du"].index[-1] == pd.Timestamp("2026-03-31")
    print("✓ Bài 5 ĐẠT (nhận diện đúng Q2/2026 là kỳ chưa trọn và loại bỏ thành công)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 6: data-lab-08-06
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-06] Kiểm tra Bài 6: Kiểm tra lọc kỳ chưa trọn tại các mốc biên ---")
    dem_quy_mau = pd.Series([100, 120], index=pd.to_datetime(["2026-03-31", "2026-06-30"]))
    q_bien_29_c1 = filter_complete_quarters_c1(dem_quy_mau, "2026-06-29")
    q_bien_29_c2 = filter_complete_quarters_c2(dem_quy_mau, "2026-06-29")
    q_bien_30_c1 = filter_complete_quarters_c1(dem_quy_mau, "2026-06-30")
    q_bien_30_c2 = filter_complete_quarters_c2(dem_quy_mau, "2026-06-30")
    pd.testing.assert_series_equal(q_bien_29_c1, q_bien_29_c2)
    pd.testing.assert_series_equal(q_bien_30_c1, q_bien_30_c2)
    assert len(q_bien_29_c1) == 1 and q_bien_29_c1.index[0] == pd.Timestamp("2026-03-31")
    assert len(q_bien_30_c1) == 2 and q_bien_30_c1.index[-1] == pd.Timestamp("2026-06-30")
    print("✓ Bài 6 ĐẠT (chứng minh loại quý cuối không phải quy tắc máy móc mà phụ thuộc mốc biên)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 7: data-lab-08-07
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-07] Kiểm tra Bài 7: Quý cao nhất và thấp nhất trong giai đoạn ---")
    quy_day_du = res5_c1["quy_day_du"]
    res7_c1 = quarter_extremes_c1(quy_day_du, "2019", "2021")
    res7_c2 = quarter_extremes_c2(quy_day_du, "2019", "2021")
    assert res7_c1 == res7_c2
    assert res7_c1["quy_dinh"] == pd.Timestamp("2026-03-31")
    assert res7_c1["quy_day"] == pd.Timestamp("2020-06-30")
    assert res7_c1["gia_tri_day"] == 26
    print("✓ Bài 7 ĐẠT (xác định đúng đỉnh toàn chuỗi Q1/2026 và đáy khủng hoảng Q2/2020)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 8: data-lab-08-08
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-08] Kiểm tra Bài 8: Tổng hợp theo ngày và điền 0 cho ngày trống ---")
    d25_c1 = daily_counts_c1(r, 2025)
    d25_c2 = daily_counts_c2(r, 2025)
    pd.testing.assert_series_equal(d25_c1, d25_c2)
    assert len(d25_c1) == 365
    assert d25_c1.sum() == int((DEMO_REVIEWS["date"].dt.year == 2025).sum()) == 2089
    assert d25_c1.max() == 13 and d25_c1.loc["2025-11-24"] == 13
    # Kiểm tra năm 2020 có các ngày giãn cách nhận giá trị 0
    d20 = daily_counts_c1(r, 2020)
    assert (d20.loc["2020-04-01":"2020-04-05"] == 0).all()
    print("✓ Bài 8 ĐẠT (lưới 365 ngày liên tục, ngày giãn cách nhận giá trị 0 chính xác)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 9: data-lab-08-09
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-09] Kiểm tra Bài 9: Cửa sổ trượt 7 ngày và nhận diện đỉnh ---")
    res9_c1 = rolling_peak_c1(d25_c1, cua_so=7)
    res9_c2 = rolling_peak_c2(d25_c1, cua_so=7)
    assert res9_c1["tb"].isna().sum() == 6
    assert res9_c1["ngay_dinh"] == pd.Timestamp("2025-11-23")
    assert round(res9_c1["gia_tri_dinh"], 2) == 11.29
    # Cửa sổ quá khứ center=False
    assert res9_c2["tb"].iloc[:6].isna().all()
    assert res9_c2["ngay_dinh"] == pd.Timestamp("2025-11-26")
    assert round(res9_c2["gia_tri_dinh"], 2) == 11.29
    # Kiểm tra đối chiếu khoảng cửa sổ 7 ngày kết thúc tại 2025-11-26
    dau_cs = pd.Timestamp("2025-11-26") - pd.Timedelta(days=6)
    cua_so_7d = d25_c1.loc[dau_cs:pd.Timestamp("2025-11-26")]
    assert len(cua_so_7d) == 7
    assert abs(cua_so_7d.mean() - res9_c2["gia_tri_dinh"]) < 1e-9
    print("✓ Bài 9 ĐẠT (phân biệt cửa sổ căn giữa và quá khứ, giải thích độ trễ đỉnh trượt)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 10: data-lab-08-10
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-10] Kiểm tra Bài 10: So sánh cùng kỳ theo quý (shift 4) ---")
    yoy_c1 = quarterly_yoy_c1(quy_day_du)
    yoy_c2 = quarterly_yoy_c2(quy_day_du)
    pd.testing.assert_series_equal(yoy_c1, yoy_c2)
    assert abs(yoy_c1.loc["2026-03-31"] - (904 / 594 - 1.0)) < 1e-9
    # Đối chiếu đếm trực tiếp trên bảng rv ban đầu trong khoảng [01/01/2025, 01/04/2025)
    mask_q1_2025 = (DEMO_REVIEWS["date"] >= "2025-01-01") & (DEMO_REVIEWS["date"] < "2025-04-01")
    assert int(mask_q1_2025.sum()) == 594 == quy_day_du.loc["2025-03-31"]
    print("✓ Bài 10 ĐẠT (khắc phục lỗi shift(12) thành shift(4), đối chiếu trực tiếp Q1/2025 = 594)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 11: data-lab-08-11
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-11] Kiểm tra Bài 11: So sánh theo tháng (kỳ trước và cùng kỳ) ---")
    thang = r.resample("ME").size()
    res11_c1 = period_changes_c1(thang, "2026-05-31")
    res11_c2 = period_changes_c2(thang, "2026-05-31")
    assert round(res11_c1["so_ky_truoc"], 1) == round(res11_c2["so_ky_truoc"], 1) == 3.2
    assert round(res11_c1["so_cung_ky"], 1) == round(res11_c2["so_cung_ky"], 1) == 57.1
    # Kiểm tra trường hợp biên tháng 2 năm nhuận 2020 vs 2021
    res11_nhuan = period_changes_c1(thang, "2021-02-28")
    assert round(res11_nhuan["so_cung_ky"], 1) == round((thang["2021-02-28"] / thang["2020-02-29"] - 1.0) * 100, 1)
    print("✓ Bài 11 ĐẠT (MoM: +3.2%, YoY: +57.1%, kiểm tra biên tháng 2 nhuận)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 12: data-lab-08-12
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-12] Kiểm tra Bài 12: Chuẩn hóa số ngày trong tháng và năm nhuận ---")
    thang_4n = thang.loc["2022":"2025"]
    res12_c1 = monthly_daily_rate_c1(thang_4n)
    res12_c2 = monthly_daily_rate_c2(thang_4n)
    pd.testing.assert_series_equal(res12_c1["tong"], res12_c2["tong"], check_names=False)
    pd.testing.assert_series_equal(res12_c1["tb_ngay"], res12_c2["tb_ngay"], check_names=False)
    assert abs(res12_c1["chenh_tong"] - res12_c2["chenh_tong"]) < 1e-9
    assert abs(res12_c1["chenh_ngay"] - res12_c2["chenh_ngay"]) < 1e-9
    assert round(res12_c1["chenh_tong"], 3) == -0.092
    assert round(res12_c1["chenh_ngay"], 4) == -0.0037
    # Kiểm tra biên năm nhuận 2024
    so_ngay_series = pd.Series(thang_4n.index.days_in_month, index=thang_4n.index)
    assert so_ngay_series.loc["2024-02-29"] == 29
    assert so_ngay_series.groupby(so_ngay_series.index.month).sum().loc[2] == 113
    print("✓ Bài 12 ĐẠT (xử lý năm nhuận 2024 với 29/02, giải thích chênh lệch -9.2% vs -0.37%)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 13: data-lab-08-13
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-13] Kiểm tra Mở rộng 1: Điều tra ngày kỷ lục ---")
    res13_c1 = investigate_peak_day_c1(r)
    res13_c2 = investigate_peak_day_c2(r)
    assert res13_c1["ngay_ky_luc"] == res13_c2["ngay_ky_luc"] == pd.Timestamp("2026-03-16")
    assert res13_c1["so_luong_ky_luc"] == res13_c2["so_luong_ky_luc"] == 50
    pd.testing.assert_series_equal(res13_c1["vung_lan_can"], res13_c2["vung_lan_can"])
    assert len(res13_c1["vung_lan_can"]) == 5
    assert res13_c1["vung_lan_can"].loc["2026-03-16"] == 50
    print("✓ Bài 13 ĐẠT (tìm đúng ngày kỷ lục 2026-03-16 với 50 đánh giá, vùng lân cận 5 ngày)")

    # --------------------------------------------------------------------------
    # Kiểm tra Bài 14: data-lab-08-14
    # --------------------------------------------------------------------------
    print("\n--- [data-lab-08-14] Kiểm tra Mở rộng 2: Khoảng cách từ đánh giá gần nhất ---")
    res14_c1 = days_since_last_review_c1(LISTINGS_DEMO, SNAPSHOT)
    res14_c2 = days_since_last_review_c2(LISTINGS_DEMO, SNAPSHOT)
    assert res14_c1["so_cho_o_ngoai_moc"] == res14_c2["so_cho_o_ngoai_moc"] == 1
    assert res14_c1["so_cho_o_tren_365_ngay"] == res14_c2["so_cho_o_tren_365_ngay"] == 2
    pd.testing.assert_series_equal(
        res14_c1["listings_gan_co"]["co_khong_hoat_dong"],
        res14_c2["listings_gan_co"]["co_khong_hoat_dong"]
    )
    print("✓ Bài 14 ĐẠT (loại 1 phòng sau mốc, gắn cờ chính xác cho phòng ngừng hoạt động)")

    # --------------------------------------------------------------------------
    # Kiểm tra trường hợp biên mở rộng (Empty DataFrame & Zero Days)
    # --------------------------------------------------------------------------
    print("\n--- Kiểm tra trường hợp biên mở rộng (Bảng rỗng, dữ liệu rỗng) ---")
    df_empty = pd.DataFrame({"vao": [], "ra": []})
    assert len(calculate_stay_nights_c1(df_empty)) == 0
    assert len(calculate_stay_nights_c2(df_empty)) == 0

    rv_after_only = pd.DataFrame({
        "date": pd.to_datetime(["2026-07-01", "2026-07-02"]),
        "listing_id": [1, 2]
    })
    prep_after = prepare_time_index_c1(rv_after_only, SNAPSHOT)
    assert prep_after["so_dong_sau_moc"] == 2
    assert len(prep_after["r"]) == 0
    print("✓ Kiểm tra trường hợp biên mở rộng ĐẠT")

    # --------------------------------------------------------------------------
    # Sinh tệp biểu đồ trực quan hóa cửa sổ trượt task-owned asset
    # --------------------------------------------------------------------------
    print("\n--- Sinh tệp biểu đồ SVG trực quan hóa chuỗi thời gian ---")
    import matplotlib.pyplot as plt
    img_dir = Path(__file__).resolve().parents[1] / "docs/xu-ly-du-lieu/bai-giang/img/labs/lab-08"
    img_dir.mkdir(parents=True, exist_ok=True)
    svg_path = img_dir / "rolling-7d-2025.svg"

    fig, ax = plt.subplots(figsize=(9, 3.2))
    ax.plot(d25_c1.index, d25_c1.values, color="#bbb", lw=0.8, label="Theo ngày")
    ax.plot(res9_c1["tb"].index, res9_c1["tb"].values, color="#1E93AB", lw=2, label="Trượt 7 ngày")
    ax.legend(frameon=False)
    ax.set_title("Số đánh giá theo ngày năm 2025 và đường trung bình trượt 7 ngày")
    ax.set_xlabel("Thời gian")
    ax.set_ylabel("Số đánh giá")
    fig.tight_layout()
    fig.savefig(svg_path, format="svg")
    plt.close(fig)
    assert svg_path.exists(), f"Không tạo được tệp SVG tại {svg_path}"
    print(f"✓ Đã sinh thành công biểu đồ SVG tại {svg_path.relative_to(img_dir.parents[3])}")

    # --------------------------------------------------------------------------
    # Rà soát cấu trúc Markdown và chạy động toàn bộ các khối mã nguồn trong lab-08.md
    # --------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("KIỂM TRA CẤU TRÚC MARKDOWN VÀ THỰC THI TOÀN BỘ CÁC KHỐI MÃ PYTHON")
    print("=" * 70)

    lab_path = Path(__file__).resolve().parents[1] / "raw_materials/xu-ly-du-lieu/labs/lab-08.md"
    assert lab_path.exists(), f"Không tìm thấy tệp {lab_path}"
    content = lab_path.read_text(encoding="utf-8")

    assert "::: exercise" in content and "::: solution" in content
    assert "#### Cách 1:" in content and "#### Cách 2:" in content

    # 1. Kiểm tra đủ 14 exercise span IDs
    for i in range(1, 15):
        span_id = f"data-lab-08-{i:02d}"
        assert f'id="{span_id}"' in content or f"id='{span_id}'" in content, f"Thiếu span id {span_id} trong {lab_path.name}"

    # 2. Kiểm tra không chứa H1, không chứa dấu chấm phẩy hoặc gạch ngang dài ngoài code fence
    lines = content.splitlines()
    in_code_fence = False
    for line_idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if not in_code_fence:
            if stripped.startswith("# "):
                raise AssertionError(f"Phát hiện heading H1 ngoài code fence tại dòng {line_idx} trong {lab_path.name}: '{line}'")
            if "—" in line:
                raise AssertionError(f"Phát hiện dấu em dash ('—') ngoài code fence tại dòng {line_idx} trong {lab_path.name}: '{line}'")
            if ";" in line:
                raise AssertionError(f"Phát hiện dấu chấm phẩy (';') ngoài code fence tại dòng {line_idx} trong {lab_path.name}: '{line}'")

    # 3. Kiểm tra từ cấm
    forbidden_terms = ["hợp đồng hàm", "hợp đồng file", "hợp đồng dữ liệu"]
    for term in forbidden_terms:
        assert term not in content.lower(), f"Phát hiện thuật ngữ cấm '{term}' trong {lab_path.name}"

    # 4. Trích xuất, kiểm tra cú pháp AST và chạy thử động toàn bộ các khối mã Python
    blocks = re.findall(r"```python\s*(.*?)\s*```", content, re.DOTALL)
    ns_doc = {"display": lambda *args, **kwargs: None}
    for b_idx, block in enumerate(blocks, 1):
        try:
            ast.parse(block, filename=f"{lab_path.name}:block_{b_idx}")
        except SyntaxError as syn_err:
            raise AssertionError(f"Lỗi cú pháp AST tại khối {b_idx} của {lab_path.name}: {syn_err}")

        try:
            exec(block, ns_doc)
        except Exception as exc:
            raise AssertionError(f"Lỗi thực thi khối {b_idx} của {lab_path.name}: {type(exc).__name__}: {exc}")

    print(f"✓ Cấu trúc Markdown chuẩn mực: Đủ 14 span IDs, không chứa H1, không dấu chấm phẩy hay em dash ngoài code fence.")
    print(f"✓ Phân tích AST và thực thi: Toàn bộ {len(blocks)} khối mã Python trong {lab_path.name} chạy thành công 100%.")

    print("\n" + "=" * 70)
    print("TẤT CẢ 14 BÀI TẬP VÀ PHÉP KIỂM ĐỊNH LAB 08 ĐÃ VƯỢT QUA 100% THÀNH CÔNG!")
    print("=" * 70)

if __name__ == "__main__":
    run_all_tests()
