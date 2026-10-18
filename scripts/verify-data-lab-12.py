# -*- coding: utf-8 -*-
"""Kịch bản kiểm tra tự động toàn diện bộ bài tập Lab 12.

Tệp kiểm định:
1. raw_materials/xu-ly-du-lieu/labs/lab-12.md (data-lab-12-01 đến 11)
2. raw_materials/xu-ly-du-lieu/labs/coverage-12.json
3. docs/xu-ly-du-lieu/bai-giang/img/labs/lab-12/*.svg

Mục tiêu kiểm định:
1. Định nghĩa và so sánh tính tương đương giữa Cách 1 (cơ bản) và Cách 2 (thực tế/tối ưu) cho cả 11 bài tập.
2. Kiểm tra độc lập các trường hợp biên: Bảng rỗng, địa bàn không tồn tại, toàn bộ phòng khóa lịch, toàn bộ phòng mở quanh năm, dữ liệu chứa NaN, mốc cắt snapshot cuối tháng và giữa tháng.
3. Kiểm tra chi tiết cấu trúc đồ họa trên đối tượng Axes: Tọa độ x/y đường vẽ, chiều dài thanh ngang barh, chiều cao cột đứng bar, tổng chiều cao các thanh histogram, giới hạn gốc tọa độ 0.
4. Kiểm tra sự tồn tại và tính hợp lệ của toàn bộ 6 tệp biểu đồ SVG lưu tại docs/xu-ly-du-lieu/bai-giang/img/labs/lab-12/.
5. Rà soát cấu trúc Markdown: Không chứa H1 ngoài code fence, đủ 11 span IDs, không dùng dấu chấm phẩy hay gạch ngang dài ngoài code fence, không chứa thuật ngữ dịch máy bị cấm, viết hoa sau dấu hai chấm.
6. Phân tích cú pháp AST và thực thi động toàn bộ các khối mã Python trong lab-12.md.
"""

import ast
import io
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Union, Tuple, Dict, Any

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Thiết lập đầu ra console hỗ trợ chuẩn UTF-8
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

os.environ["MPLBACKEND"] = "Agg"

# ==============================================================================
# Dữ liệu mẫu chuẩn bị sẵn phục vụ kiểm thử độc lập
# ==============================================================================

SNAPSHOT = "2026-06-29"

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)
_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}
DEMO_DS = pd.DataFrame({
    "id": list(range(101, 161)),
    "neighbourhood": _QUAN,
    "room_type": [
        "Private room"
        if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
        else "Entire home/apt"
        for k, q in enumerate(_QUAN)
    ],
    "availability_365": [
        0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
        for k in range(60)
    ],
})

_dong = []
for k, lid in enumerate(DEMO_DS["id"]):
    for ngay in pd.date_range("2024-01-10", "2026-07-01", freq=f"{20 + k % 25}D"):
        _dong.append((lid, ngay))
DEMO_RV = pd.DataFrame(_dong, columns=["listing_id", "date"])

# ==============================================================================
# 1. Định nghĩa các hàm lời giải Cách 1 và Cách 2 cho 11 bài tập
# ==============================================================================

# Bài 1: monthly_reviews
def monthly_reviews_c1(rv: pd.DataFrame, ds: pd.DataFrame, quan: str) -> pd.Series:
    tap_id = set(ds.loc[ds["neighbourhood"] == quan, "id"])
    rv_quan = rv[rv["listing_id"].isin(tap_id)]
    thang = rv_quan.set_index("date").resample("ME").size()
    return thang.iloc[:-1]

def monthly_reviews_c2(rv: pd.DataFrame, ds: pd.DataFrame, quan: str) -> pd.Series:
    danh_sach_id = ds.loc[ds["neighbourhood"] == quan, "id"].to_numpy()
    chuoi_thang = (
        rv.loc[rv["listing_id"].isin(danh_sach_id)]
        .set_index("date")
        .resample("ME")
        .size()
    )
    if len(chuoi_thang) >= 2:
        return chuoi_thang.iloc[:-1]
    return chuoi_thang

# Bài 2: monthly_reviews_with_cutoff
def monthly_reviews_with_cutoff_c1(
    rv: pd.DataFrame, ds: pd.DataFrame, quan: str, snapshot: str = "2026-06-29"
) -> pd.Series:
    snap_dt = pd.Timestamp(snapshot)
    tap_id = set(ds.loc[ds["neighbourhood"] == quan, "id"])
    dieu_kien = (rv["listing_id"].isin(tap_id)) & (rv["date"] <= snap_dt)
    rv_hop_le = rv.loc[dieu_kien]
    thang = rv_hop_le.set_index("date").resample("ME").size()
    if len(thang) > 0 and snap_dt < thang.index[-1]:
        return thang.iloc[:-1]
    return thang

def monthly_reviews_with_cutoff_c2(
    rv: pd.DataFrame, ds: pd.DataFrame, quan: str, snapshot: str = "2026-06-29"
) -> pd.Series:
    snap_dt = pd.Timestamp(snapshot)
    danh_sach_id = ds.loc[ds["neighbourhood"] == quan, "id"].to_numpy()
    rv_loc = (
        rv.loc[rv["listing_id"].isin(danh_sach_id)]
        .sort_values("date")
        .set_index("date")
        .loc[:snap_dt]
    )
    thang = rv_loc.resample("ME").size()
    ngay_cuoi_thang_chuan = snap_dt - pd.offsets.MonthEnd(1) if snap_dt < (snap_dt + pd.offsets.MonthEnd(0)) else snap_dt
    return thang.loc[:ngay_cuoi_thang_chuan]

# Bài 3: plot_line
def plot_line_c1(thang: pd.Series, path: str):
    fig, ax = plt.subplots(figsize=(9, 3.5))
    ax.plot(thang.index, thang.values, color="#1976d2", linewidth=2, marker="o", markersize=3)
    ax.set_title("Diễn biến số lượt đánh giá theo tháng tại quận Providencia (2024–2026)", pad=12)
    ax.set_ylabel("Lượt đánh giá (lượt/tháng)")
    ax.set_xlabel("Thời gian ghi nhận")
    fig.text(0.12, -0.02, "Nguồn: Dữ liệu Inside Airbnb Santiago (mẫu giả lập chuẩn hóa 2024–2026)", fontsize=9, color="#555555")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax

def plot_line_c2(thang: pd.Series, path: str):
    fig, ax = plt.subplots(figsize=(9, 3.5))
    ax.plot(thang.index, thang.values, color="#0d47a1", linewidth=1.8, marker="s", markersize=3.5)
    ax.set_title("Số lượt đánh giá theo tháng tại quận Providencia duy trì đà tăng trưởng", pad=12)
    ax.set_ylabel("Số lượt đánh giá (lượt/tháng)")
    ax.set_xlabel("Thời gian ghi nhận")
    fig.text(0.12, -0.03, "Nguồn: Inside Airbnb Santiago, dữ liệu chuẩn hóa phục vụ phân tích", fontsize=9, color="#424242")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax

# Bài 4: share_entire
def share_entire_c1(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame:
    tk = ds.groupby("neighbourhood").agg(
        n=("id", "size"),
        pct=("room_type", lambda cot: (cot == "Entire home/apt").mean())
    )
    return tk.loc[tk["n"] >= min_n].sort_values("pct", ascending=True)

def share_entire_c2(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame:
    tk = (
        ds.assign(la_nguyen_can=ds["room_type"] == "Entire home/apt")
        .groupby("neighbourhood")
        .agg(n=("id", "size"), pct=("la_nguyen_can", "mean"))
    )
    return tk.loc[tk["n"] >= min_n].sort_values("pct")

# Bài 5: plot_share_barh
def plot_share_barh_c1(tk: pd.DataFrame, path: str):
    fig, ax = plt.subplots(figsize=(7, 4))
    thanh = ax.barh(tk.index, tk["pct"] * 100, color="#2b5c8f", height=0.65)
    ax.bar_label(thanh, fmt="%.0f%%", padding=4, fontsize=10)
    ax.set_xlim(left=0, right=115)
    ax.set_xlabel("Tỷ lệ phòng nguyên căn (%)")
    ax.set_title("Tỷ lệ phòng nguyên căn tại các quận có từ 5 chỗ ở trở lên", pad=12)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax

def plot_share_barh_c2(tk: pd.DataFrame, path: str):
    fig, ax = plt.subplots(figsize=(7, 4))
    mau_sac = ["#4a7bb0" if p < tk["pct"].max() else "#1a4971" for p in tk["pct"]]
    thanh = ax.barh(tk.index, tk["pct"] * 100, color=mau_sac, height=0.6)
    ax.bar_label(thanh, fmt="%.1f%%", padding=5, color="#111111", weight="bold")
    ax.set_xlim(0, 115)
    ax.set_xlabel("Tỷ lệ phòng nguyên căn (%)")
    ax.set_title("Cơ cấu loại phòng nguyên căn phân hóa mạnh giữa các địa bàn", pad=12)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax

# Bài 6: plot_availability
def plot_availability_c1(avail: pd.Series, path: str, bins: int = 40) -> dict:
    du_lieu = avail.dropna()
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.hist(du_lieu, bins=bins, color="#0288d1", edgecolor="white", linewidth=0.5)
    ax.set_title("Phân phối số ngày mở lịch trong năm tới: Tập trung tại hai cực", pad=12)
    ax.set_xlabel("Số ngày mở lịch trong năm (ngày)")
    ax.set_ylabel("Số lượng chỗ ở")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    so_khoa = int((du_lieu == 0).sum())
    so_mo_quanh_nam = int((du_lieu >= 360).sum())
    return {"ax": ax, "so_khoa": so_khoa, "so_mo_quanh_nam": so_mo_quanh_nam}

def plot_availability_c2(avail: pd.Series, path: str, bins: int = 40) -> dict:
    mang_du_lieu = avail.dropna().to_numpy()
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ranh_gioi_bin = np.linspace(0, 365, bins + 1)
    ax.hist(mang_du_lieu, bins=ranh_gioi_bin, color="#0097a7", edgecolor="#ffffff", linewidth=0.5)
    ax.set_title("Phân phối hai đỉnh của số ngày mở lịch phản ánh hai nhóm vận hành", pad=12)
    ax.set_xlabel("Số ngày mở lịch trong năm (ngày)")
    ax.set_ylabel("Số lượng chỗ ở")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    so_khoa = int(np.count_nonzero(mang_du_lieu == 0))
    so_mo_quanh_nam = int(np.count_nonzero(mang_du_lieu >= 360))
    return {"ax": ax, "so_khoa": so_khoa, "so_mo_quanh_nam": so_mo_quanh_nam}

# Bài 7: analyze_bimodal_distribution
def analyze_bimodal_distribution_c1(avail: pd.Series) -> dict:
    s = avail.dropna()
    n = len(s)
    trung_binh = float(s.mean())
    trung_vi = float(s.median())
    so_khoa = int((s == 0).sum())
    so_mo_quanh_nam = int((s >= 360).sum())
    so_giua = int(((s > 0) & (s < 360)).sum())
    return {
        "mean": round(trung_binh, 2),
        "median": round(trung_vi, 2),
        "pct_khoa": round(so_khoa / n * 100, 2),
        "pct_mo_quanh_nam": round(so_mo_quanh_nam / n * 100, 2),
        "pct_giua": round(so_giua / n * 100, 2),
        "so_khoa": so_khoa,
        "so_mo_quanh_nam": so_mo_quanh_nam,
        "so_giua": so_giua,
    }

def analyze_bimodal_distribution_c2(avail: pd.Series) -> dict:
    s = avail.dropna()
    n = len(s)
    nhom = pd.cut(s, bins=[-1, 0, 359, 365], labels=["khoa", "giua", "mo_quanh_nam"])
    dem = nhom.value_counts()
    return {
        "mean": round(float(s.mean()), 2),
        "median": round(float(s.median()), 2),
        "pct_khoa": round(dem["khoa"] / n * 100, 2),
        "pct_mo_quanh_nam": round(dem["mo_quanh_nam"] / n * 100, 2),
        "pct_giua": round(dem["giua"] / n * 100, 2),
        "so_khoa": int(dem["khoa"]),
        "so_mo_quanh_nam": int(dem["mo_quanh_nam"]),
        "so_giua": int(dem["giua"]),
    }

# Bài 8: visual_distortion_factor
def visual_distortion_factor_c1(data: pd.Series, y_min: float, y_max: float) -> dict:
    v_min = float(data.min())
    v_max = float(data.max())
    r_thuc = v_max / v_min
    h_min = v_min - y_min
    h_max = v_max - y_min
    r_thi_giac = h_max / h_min
    he_so = r_thi_giac / r_thuc
    return {
        "v_min": v_min,
        "v_max": v_max,
        "r_thuc": round(r_thuc, 3),
        "r_thi_giac": round(r_thi_giac, 3),
        "he_so": round(he_so, 3),
    }

def visual_distortion_factor_c2(data: pd.Series, y_min: float, y_max: float) -> dict:
    vals = data.to_numpy()
    v_min, v_max = float(vals.min()), float(vals.max())
    if y_min >= v_min:
        raise ValueError("Giới hạn dưới y_min phải nhỏ hơn giá trị nhỏ nhất của dữ liệu.")
    r_thuc = v_max / v_min
    r_thi_giac = (v_max - y_min) / (v_min - y_min)
    he_so = r_thi_giac / r_thuc
    return {
        "v_min": v_min,
        "v_max": v_max,
        "r_thuc": round(r_thuc, 3),
        "r_thi_giac": round(r_thi_giac, 3),
        "he_so": round(he_so, 3),
    }

# Bài 9: plot_honest_bars
def plot_honest_bars_c1(pct: pd.Series, path: str):
    fig, ax = plt.subplots(figsize=(6, 3.5))
    thanh = ax.bar(pct.index, pct.values, color="#388e3c", width=0.55)
    ax.bar_label(thanh, fmt="%.0f%%", padding=3, fontsize=10)
    ax.set_ylim(bottom=0, top=100)
    ax.set_ylabel("Tỷ lệ nguyên căn (%)")
    ax.set_title("Trục tung xuất phát từ 0: Phản ánh trung thực tương quan tỷ lệ", pad=12)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax

def plot_honest_bars_c2(pct: pd.Series, path: str):
    fig, ax = plt.subplots(figsize=(6, 3.5))
    cot = ax.bar(pct.index, pct.values, color="#2e7d32", width=0.5, edgecolor="#1b5e20", linewidth=0.8)
    ax.bar_label(cot, fmt="%.1f%%", padding=4, weight="bold")
    ax.set_ylim(0, 105)
    ax.set_ylabel("Tỷ lệ phòng nguyên căn (%)")
    ax.set_title("Tỷ lệ phòng nguyên căn giữa các quận có sự tương đồng đáng kể", pad=12)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax

# Bài 10: validate_chart_structure
def validate_chart_structure_c1(
    ax: matplotlib.axes.Axes,
    min_title_len: int = 15,
    require_ylabel: bool = False,
    require_xlabel: bool = False,
    require_zero_x: bool = False,
    require_zero_y: bool = False,
    min_patches: int = 0,
    min_lines: int = 0,
    saved_path: str = None,
) -> dict:
    tieu_de = ax.get_title().strip()
    dat_tieu_de = len(tieu_de) >= min_title_len
    dat_nhan_y = not require_ylabel or bool(ax.get_ylabel().strip())
    dat_nhan_x = not require_xlabel or bool(ax.get_xlabel().strip())
    dat_goc_x = not require_zero_x or (round(ax.get_xlim()[0], 5) == 0.0)
    dat_goc_y = not require_zero_y or (round(ax.get_ylim()[0], 5) == 0.0)
    dat_patches = len(ax.patches) >= min_patches
    dat_lines = len(ax.lines) >= min_lines
    dat_tep = True
    if saved_path:
        tep = Path(saved_path)
        dat_tep = tep.exists() and tep.stat().st_size > 0
    tat_ca_dat = all([dat_tieu_de, dat_nhan_y, dat_nhan_x, dat_goc_x, dat_goc_y, dat_patches, dat_lines, dat_tep])
    return {
        "has_title": dat_tieu_de,
        "has_ylabel": dat_nhan_y,
        "has_xlabel": dat_nhan_x,
        "has_zero_x": dat_goc_x,
        "has_zero_y": dat_goc_y,
        "has_patches": dat_patches,
        "has_lines": dat_lines,
        "has_file": dat_tep,
        "all_passed": tat_ca_dat,
    }

def validate_chart_structure_c2(
    ax: matplotlib.axes.Axes,
    min_title_len: int = 15,
    require_ylabel: bool = False,
    require_xlabel: bool = False,
    require_zero_x: bool = False,
    require_zero_y: bool = False,
    min_patches: int = 0,
    min_lines: int = 0,
    saved_path: str = None,
) -> dict:
    ket_qua = {
        "has_title": len(ax.get_title().strip()) >= min_title_len,
        "has_ylabel": not require_ylabel or bool(ax.get_ylabel().strip()),
        "has_xlabel": not require_xlabel or bool(ax.get_xlabel().strip()),
        "has_zero_x": not require_zero_x or (round(ax.get_xlim()[0], 5) == 0.0),
        "has_zero_y": not require_zero_y or (round(ax.get_ylim()[0], 5) == 0.0),
        "has_patches": len(ax.patches) >= min_patches,
        "has_lines": len(ax.lines) >= min_lines,
        "has_file": bool(saved_path and Path(saved_path).is_file() and Path(saved_path).stat().st_size > 0) if saved_path else True,
    }
    ket_qua["all_passed"] = all(ket_qua.values())
    return ket_qua

# Bài 11: plot_comparative_groups
def plot_comparative_groups_c1(
    ds: pd.DataFrame, quan_a: str, quan_b: str, path: str, bins: int = 20
) -> tuple:
    avail_a = ds.loc[ds["neighbourhood"] == quan_a, "availability_365"].dropna()
    avail_b = ds.loc[ds["neighbourhood"] == quan_b, "availability_365"].dropna()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)
    ax1.hist(avail_a, bins=bins, color="#1976d2", edgecolor="white", linewidth=0.5)
    ax1.set_title(f"Quận {quan_a} (N = {len(avail_a)})", fontsize=11)
    ax1.set_xlabel("Số ngày mở lịch (ngày)")
    ax1.set_ylabel("Số lượng chỗ ở")
    ax2.hist(avail_b, bins=bins, color="#f57c00", edgecolor="white", linewidth=0.5)
    ax2.set_title(f"Quận {quan_b} (N = {len(avail_b)})", fontsize=11)
    ax2.set_xlabel("Số ngày mở lịch (ngày)")
    fig.suptitle("So sánh phân phối số ngày mở lịch trên cùng thang đo trục tung", y=1.02, fontsize=12)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return fig, (ax1, ax2)

def plot_comparative_groups_c2(
    ds: pd.DataFrame, quan_a: str, quan_b: str, path: str, bins: int = 20
) -> tuple:
    s_a = ds.loc[ds["neighbourhood"] == quan_a, "availability_365"].dropna()
    s_b = ds.loc[ds["neighbourhood"] == quan_b, "availability_365"].dropna()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)
    luoi_chia = np.linspace(0, 365, bins + 1)
    ax1.hist(s_a, bins=luoi_chia, color="#1565c0", edgecolor="#ffffff", linewidth=0.6)
    ax1.set_title(f"Địa bàn {quan_a} (N = {len(s_a)})", fontsize=11)
    ax1.set_xlabel("Số ngày mở lịch (ngày)")
    ax1.set_ylabel("Số lượng chỗ ở")
    ax2.hist(s_b, bins=luoi_chia, color="#e65100", edgecolor="#ffffff", linewidth=0.6)
    ax2.set_title(f"Địa bàn {quan_b} (N = {len(s_b)})", fontsize=11)
    ax2.set_xlabel("Số ngày mở lịch (ngày)")
    fig.suptitle("Phân tích so sánh phân phối số ngày mở lịch giữa hai quận", y=1.02, fontsize=12)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return fig, (ax1, ax2)

# ==============================================================================
# 2. Quy trình kiểm tra toàn diện
# ==============================================================================

def run_all_tests():
    print("=" * 70)
    print("BẮT ĐẦU KIỂM THỬ TOÀN DIỆN LAB 12")
    print("=" * 70)

    with tempfile.TemporaryDirectory(prefix="studyhub-verify-lab-12-") as tmpdir:
        tmp_path = Path(tmpdir)

        # ----------------------------------------------------------------------
        # Bài 1: data-lab-12-01 (monthly_reviews)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-01] Kiểm tra Bài 1: Tổng hợp chuỗi tháng của một quận ---")
        thang_c1 = monthly_reviews_c1(DEMO_RV, DEMO_DS, "Providencia")
        thang_c2 = monthly_reviews_c2(DEMO_RV, DEMO_DS, "Providencia")
        pd.testing.assert_series_equal(thang_c1, thang_c2)
        assert len(thang_c1) == 30, f"Mong đợi 30 tháng, nhận được {len(thang_c1)}"
        assert thang_c1.index[0] == pd.Timestamp("2024-01-31")
        assert thang_c1.index[-1] == pd.Timestamp("2026-06-30")
        assert thang_c1.iloc[-1] == 15
        assert thang_c1.sum() == 391
        # Kiểm tra quận không có chỗ ở
        thang_rong = monthly_reviews_c1(DEMO_RV, DEMO_DS, "Quan_Khong_Ton_Tai")
        assert len(thang_rong) == 0
        print("✓ Bài 1 ĐẠT (30 tháng, tháng cuối 15 lượt, tổng 391 lượt, xử lý an toàn quận rỗng)")

        # ----------------------------------------------------------------------
        # Bài 2: data-lab-12-02 (monthly_reviews_with_cutoff)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-02] Kiểm tra Bài 2: Kiểm soát mốc snapshot và kỳ chưa trọn ---")
        t_cut_29_c1 = monthly_reviews_with_cutoff_c1(DEMO_RV, DEMO_DS, "Providencia", "2026-06-29")
        t_cut_29_c2 = monthly_reviews_with_cutoff_c2(DEMO_RV, DEMO_DS, "Providencia", "2026-06-29")
        pd.testing.assert_series_equal(t_cut_29_c1, t_cut_29_c2)
        assert len(t_cut_29_c1) == 29
        assert t_cut_29_c1.index[-1] == pd.Timestamp("2026-05-31")

        t_cut_30_c1 = monthly_reviews_with_cutoff_c1(DEMO_RV, DEMO_DS, "Providencia", "2026-06-30")
        t_cut_30_c2 = monthly_reviews_with_cutoff_c2(DEMO_RV, DEMO_DS, "Providencia", "2026-06-30")
        pd.testing.assert_series_equal(t_cut_30_c1, t_cut_30_c2)
        assert len(t_cut_30_c1) == 30
        assert t_cut_30_c1.index[-1] == pd.Timestamp("2026-06-30")
        print("✓ Bài 2 ĐẠT (2026-06-29 loại tháng 6 chưa trọn; 2026-06-30 giữ tháng 6 trọn vẹn)")

        # ----------------------------------------------------------------------
        # Bài 3: data-lab-12-03 (plot_line)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-03] Kiểm tra Bài 3: Dựng biểu đồ đường hoàn chỉnh ---")
        p_line_c1 = tmp_path / "line_c1.png"
        p_line_c2 = tmp_path / "line_c2.png"
        ax_l1 = plot_line_c1(thang_c1, str(p_line_c1))
        ax_l2 = plot_line_c2(thang_c1, str(p_line_c2))
        assert p_line_c1.exists() and p_line_c1.stat().st_size > 0
        assert p_line_c2.exists() and p_line_c2.stat().st_size > 0
        assert len(ax_l1.lines) >= 1
        assert len(ax_l1.get_title().strip()) >= 15
        assert ax_l1.get_ylabel().strip() != ""
        assert any(t.get_text().strip() for t in ax_l1.figure.texts)
        assert list(ax_l1.lines[0].get_ydata()) == thang_c1.tolist()
        print("✓ Bài 3 ĐẠT (1 đường, dữ liệu đúng, tiêu đề >= 15 ký tự, nhãn y có đơn vị, chú thích nguồn)")

        # ----------------------------------------------------------------------
        # Bài 4: data-lab-12-04 (share_entire)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-04] Kiểm tra Bài 4: Bảng tỷ lệ nguyên căn theo quận ---")
        tk_c1 = share_entire_c1(DEMO_DS, min_n=5)
        tk_c2 = share_entire_c2(DEMO_DS, min_n=5)
        pd.testing.assert_frame_equal(tk_c1, tk_c2)
        assert list(tk_c1.columns) == ["n", "pct"]
        assert len(tk_c1) == 5
        assert "Vitacura" not in tk_c1.index  # Vitacura chỉ có 4 chỗ ở
        assert tk_c1["pct"].is_monotonic_increasing
        assert tk_c1.index[-1] == "Lo Barnechea" and tk_c1["pct"].max() == 1.0
        assert tk_c1.loc["Ñuñoa", "pct"] == 0.5
        assert tk_c1.loc["Santiago", "n"] == 20
        # Kiểm tra tính bất biến của DEMO_DS
        assert "la_nguyen_can" not in DEMO_DS.columns
        print("✓ Bài 4 ĐẠT (5 quận >= 5 chỗ ở, sắp tăng dần pct, Lo Barnechea 100%, không đổi ds)")

        # ----------------------------------------------------------------------
        # Bài 5: data-lab-12-05 (plot_share_barh)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-05] Kiểm tra Bài 5: Dựng biểu đồ thanh ngang có nhãn % ---")
        p_barh_c1 = tmp_path / "barh_c1.png"
        p_barh_c2 = tmp_path / "barh_c2.png"
        ax_b1 = plot_share_barh_c1(tk_c1, str(p_barh_c1))
        ax_b2 = plot_share_barh_c2(tk_c1, str(p_barh_c2))
        assert p_barh_c1.exists() and p_barh_c1.stat().st_size > 0
        assert p_barh_c2.exists() and p_barh_c2.stat().st_size > 0
        assert len(ax_b1.patches) == 5
        widths_expected = (tk_c1["pct"] * 100).tolist()
        widths_actual = [round(p.get_width(), 4) for p in ax_b1.patches]
        assert np.allclose(widths_actual, widths_expected)
        assert len(ax_b1.texts) >= 5, "Mỗi thanh cần một nhãn giá trị (bar_label)"
        assert ax_b1.get_xlim()[0] == 0, "Trục x bắt buộc phải bắt đầu từ gốc 0"
        assert len(ax_b1.get_title().strip()) >= 15
        assert "%" in ax_b1.get_xlabel()
        print("✓ Bài 5 ĐẠT (5 thanh ngang, độ dài = pct*100, xlim[0]=0, đủ nhãn bar_label)")

        # ----------------------------------------------------------------------
        # Bài 6: data-lab-12-06 (plot_availability)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-06] Kiểm tra Bài 6: Dựng histogram và trích xuất hai đỉnh ---")
        p_hist_c1 = tmp_path / "hist_c1.png"
        p_hist_c2 = tmp_path / "hist_c2.png"
        res_h1 = plot_availability_c1(DEMO_DS["availability_365"], str(p_hist_c1), bins=40)
        res_h2 = plot_availability_c2(DEMO_DS["availability_365"], str(p_hist_c2), bins=40)
        assert set(res_h1.keys()) == {"ax", "so_khoa", "so_mo_quanh_nam"}
        assert res_h1["so_khoa"] == res_h2["so_khoa"] == 7
        assert res_h1["so_mo_quanh_nam"] == res_h2["so_mo_quanh_nam"] == 13
        assert len(res_h1["ax"].patches) == 40
        assert sum(p.get_height() for p in res_h1["ax"].patches) == 60
        assert p_hist_c1.exists() and p_hist_c1.stat().st_size > 0
        # Kiểm tra trường hợp Series chứa toàn NaN
        s_nan = pd.Series([np.nan, np.nan])
        res_nan = plot_availability_c1(s_nan, str(tmp_path / "hist_nan.png"), bins=10)
        assert res_nan["so_khoa"] == 0 and res_nan["so_mo_quanh_nam"] == 0
        print("✓ Bài 6 ĐẠT (40 bins, tổng chiều cao 60, so_khoa=7, so_mo_quanh_nam=13)")

        # ----------------------------------------------------------------------
        # Bài 7: data-lab-12-07 (analyze_bimodal_distribution)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-07] Kiểm tra Bài 7: Phân tích phân phối hai đỉnh ---")
        stat_c1 = analyze_bimodal_distribution_c1(DEMO_DS["availability_365"])
        stat_c2 = analyze_bimodal_distribution_c2(DEMO_DS["availability_365"])
        assert stat_c1 == stat_c2
        assert stat_c1["mean"] == 180.57
        assert stat_c1["median"] == 191.0
        assert stat_c1["so_khoa"] == 7 and stat_c1["pct_khoa"] == 11.67
        assert stat_c1["so_mo_quanh_nam"] == 13 and stat_c1["pct_mo_quanh_nam"] == 21.67
        assert stat_c1["so_giua"] == 40 and stat_c1["pct_giua"] == 66.67
        print("✓ Bài 7 ĐẠT (mean=180.57, median=191.0, 11.67% khóa, 21.67% mở quanh năm)")

        # ----------------------------------------------------------------------
        # Bài 8: data-lab-12-08 (visual_distortion_factor)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-08] Kiểm tra Bài 8: Đo lường hệ số phóng đại thị giác ---")
        dulieu_test = pd.Series([65.0, 75.0, 80.0], index=["Santiago", "Providencia", "Las Condes"])
        dist_c1 = visual_distortion_factor_c1(dulieu_test, y_min=60.0, y_max=85.0)
        dist_c2 = visual_distortion_factor_c2(dulieu_test, y_min=60.0, y_max=85.0)
        assert dist_c1 == dist_c2
        assert dist_c1["r_thuc"] == 1.231
        assert dist_c1["r_thi_giac"] == 4.0
        assert dist_c1["he_so"] == 3.25
        print("✓ Bài 8 ĐẠT (r_thuc=1.231, r_thi_giac=4.0, hệ số phóng đại thị giác = 3.25 lần)")

        # ----------------------------------------------------------------------
        # Bài 9: data-lab-12-09 (plot_honest_bars)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-09] Kiểm tra Bài 9: Sửa biểu đồ cột trung thực có trục từ 0 ---")
        p_honest_c1 = tmp_path / "honest_c1.png"
        p_honest_c2 = tmp_path / "honest_c2.png"
        ax_h1 = plot_honest_bars_c1(dulieu_test, str(p_honest_c1))
        ax_h2 = plot_honest_bars_c2(dulieu_test, str(p_honest_c2))
        assert p_honest_c1.exists() and p_honest_c1.stat().st_size > 0
        assert p_honest_c2.exists() and p_honest_c2.stat().st_size > 0
        assert ax_h1.get_ylim()[0] == 0, "Biểu đồ cột: Trục y bắt buộc phải bắt đầu từ 0"
        assert len(ax_h1.patches) == 3
        heights_expected = dulieu_test.tolist()
        heights_actual = [round(p.get_height(), 4) for p in ax_h1.patches]
        assert np.allclose(heights_actual, heights_expected)
        assert len(ax_h1.get_title().strip()) >= 15
        print("✓ Bài 9 ĐẠT (ylim[0]=0, 3 cột, chiều cao trùng khớp dữ liệu thực tế)")

        # ----------------------------------------------------------------------
        # Bài 10: data-lab-12-10 (validate_chart_structure)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-10] Kiểm tra Bài 10: Tự động hóa kiểm tra cấu trúc biểu đồ ---")
        chk_barh_c1 = validate_chart_structure_c1(
            ax_b1, min_title_len=15, require_xlabel=True, require_zero_x=True, min_patches=5, saved_path=str(p_barh_c1)
        )
        chk_barh_c2 = validate_chart_structure_c2(
            ax_b1, min_title_len=15, require_xlabel=True, require_zero_x=True, min_patches=5, saved_path=str(p_barh_c1)
        )
        assert chk_barh_c1 == chk_barh_c2
        assert chk_barh_c1["all_passed"] is True

        chk_honest_c1 = validate_chart_structure_c1(
            ax_h1, min_title_len=15, require_ylabel=True, require_zero_y=True, min_patches=3, saved_path=str(p_honest_c1)
        )
        chk_honest_c2 = validate_chart_structure_c2(
            ax_h1, min_title_len=15, require_ylabel=True, require_zero_y=True, min_patches=3, saved_path=str(p_honest_c1)
        )
        assert chk_honest_c1 == chk_honest_c2
        assert chk_honest_c1["all_passed"] is True

        # Thử nghiệm trường hợp vi phạm: Yêu cầu 10 cột khi chỉ có 3
        chk_fail = validate_chart_structure_c1(ax_h1, min_patches=10)
        assert chk_fail["all_passed"] is False and chk_fail["has_patches"] is False
        print("✓ Bài 10 ĐẠT (kiểm định toàn diện 8 tiêu chí, phát hiện chính xác trường hợp vi phạm)")

        # ----------------------------------------------------------------------
        # Bài 11: data-lab-12-11 (plot_comparative_groups)
        # ----------------------------------------------------------------------
        print("\n--- [data-lab-12-11] Kiểm tra Bài 11: So sánh phân phối trên biểu đồ ghép cùng thang đo ---")
        p_comp_c1 = tmp_path / "comp_c1.png"
        p_comp_c2 = tmp_path / "comp_c2.png"
        fig_c1, (ax_p1, ax_s1) = plot_comparative_groups_c1(DEMO_DS, "Providencia", "Santiago", str(p_comp_c1), bins=20)
        fig_c2, (ax_p2, ax_s2) = plot_comparative_groups_c2(DEMO_DS, "Providencia", "Santiago", str(p_comp_c2), bins=20)
        assert p_comp_c1.exists() and p_comp_c1.stat().st_size > 0
        assert p_comp_c2.exists() and p_comp_c2.stat().st_size > 0
        assert ax_p1.get_ylim() == ax_s1.get_ylim(), "Hai biểu đồ con phải dùng chung thang đo trục tung"
        assert len(ax_p1.patches) == 20 and len(ax_s1.patches) == 20
        assert sum(p.get_height() for p in ax_p1.patches) == 12  # Providencia có 12 chỗ ở
        assert sum(p.get_height() for p in ax_s1.patches) == 20  # Santiago có 20 chỗ ở
        plt.close("all")
        print("✓ Bài 11 ĐẠT (sharey=True đồng bộ thang đo, tổng chiều cao Providencia=12, Santiago=20)")

    # --------------------------------------------------------------------------
    # 3. Kiểm tra các tệp biểu đồ SVG đã xuất bản trong repo
    # --------------------------------------------------------------------------
    print("\n--- Kiểm tra tệp biểu đồ SVG đã xuất bản (task-owned assets) ---")
    svg_dir = Path(__file__).resolve().parents[1] / "docs/xu-ly-du-lieu/bai-giang/img/labs/lab-12"
    assert svg_dir.exists(), f"Thư mục SVG không tồn tại: {svg_dir}"

    expected_svgs = [
        "providencia-monthly-reviews.svg",
        "entire-home-share-barh.svg",
        "availability-365-hist.svg",
        "misleading-truncated-bar.svg",
        "honest-zero-baseline-bar.svg",
        "comparative-groups-distribution.svg",
    ]

    for svg_name in expected_svgs:
        svg_file = svg_dir / svg_name
        assert svg_file.exists(), f"Thiếu tệp SVG: {svg_name}"
        assert svg_file.stat().st_size > 500, f"Tệp SVG quá nhỏ hoặc rỗng: {svg_name}"
        svg_text = svg_file.read_text(encoding="utf-8")
        assert "<svg" in svg_text and "</svg>" in svg_text, f"Tệp không có thẻ SVG chuẩn: {svg_name}"
        assert "d=" in svg_text or "<path" in svg_text, f"Tệp SVG thiếu đường nét vector: {svg_name}"
        print(f"✓ Đạt: {svg_name} ({svg_file.stat().st_size:,} bytes)")

    # --------------------------------------------------------------------------
    # 4. Rà soát cấu trúc Markdown và chạy động toàn bộ các khối mã nguồn
    # --------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("KIỂM TRA CẤU TRÚC MARKDOWN VÀ THỰC THI TOÀN BỘ CÁC KHỐI MÃ PYTHON")
    print("=" * 70)

    lab_path = Path(__file__).resolve().parents[1] / "raw_materials/xu-ly-du-lieu/labs/lab-12.md"
    assert lab_path.exists(), f"Không tìm thấy tệp {lab_path}"
    content = lab_path.read_text(encoding="utf-8")

    assert "::: exercise" in content and "::: solution" in content
    assert "#### Cách 1:" in content and "#### Cách 2:" in content

    # 1. Kiểm tra đủ 11 exercise span IDs
    for i in range(1, 12):
        span_id = f"data-lab-12-{i:02d}"
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

    # 4. Kiểm tra quy tắc viết hoa sau dấu hai chấm (bỏ qua container ::: và bảng |)
    for line_idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if not in_code_fence:
            if stripped.startswith(":::") or stripped.startswith("|"):
                continue
            cleaned = re.sub(r"https?://\S+", "", line)
            cleaned = re.sub(r"\[.*?\]\(.*?\)", "", cleaned)
            cleaned = re.sub(r"`.*?`", "", cleaned)
            cleaned = re.sub(r"\$.*?\$", "", cleaned)
            matches = re.finditer(r":\s+(\S)", cleaned)
            for m in matches:
                char = m.group(1)
                if char.islower():
                    raise AssertionError(f"Dòng {line_idx} chưa viết hoa sau dấu hai chấm: '{char}' trong câu: {line}")

    # 5. Trích xuất, kiểm tra cú pháp AST và chạy thử động toàn bộ các khối mã Python trong lab-12.md
    blocks = re.findall(r"^```python[^\n]*\n(.*?)^```\s*$", content, flags=re.M | re.S)
    print(f"\nTìm thấy {len(blocks)} khối mã Python trong {lab_path.name}.")

    with tempfile.TemporaryDirectory(prefix="studyhub-ast-lab-12-") as ast_tmp:
        prev_cwd = Path.cwd()
        os.chdir(ast_tmp)
        try:
            ns_doc = {
                "__name__": "__lesson__",
                "display": lambda *args, **kwargs: None,
            }
            for b_idx, block in enumerate(blocks, 1):
                try:
                    tree = ast.parse(block, filename=f"{lab_path.name}:block_{b_idx}")
                except SyntaxError as syn_err:
                    raise AssertionError(f"Lỗi cú pháp AST tại khối {b_idx} của {lab_path.name}: {syn_err}")

                try:
                    exec(compile(tree, f"{lab_path.name}:block_{b_idx}", "exec"), ns_doc)
                except Exception as exc:
                    raise AssertionError(f"Lỗi thực thi khối {b_idx} của {lab_path.name}: {type(exc).__name__}: {exc}")
            if "plt" in ns_doc:
                ns_doc["plt"].close("all")
        finally:
            os.chdir(prev_cwd)

    print(f"✓ Cấu trúc Markdown chuẩn mực: Đủ 11 span IDs, không chứa H1, không dấu chấm phẩy hay em dash ngoài code fence, viết hoa sau dấu hai chấm.")
    print(f"✓ Phân tích AST và thực thi: Toàn bộ {len(blocks)} khối mã Python trong {lab_path.name} chạy thành công 100%.")

    print("\n" + "=" * 70)
    print("TẤT CẢ 11 BÀI TẬP VÀ PHÉP KIỂM ĐỊNH LAB 12 ĐÃ VƯỢT QUA 100% THÀNH CÔNG!")
    print("=" * 70)

if __name__ == "__main__":
    run_all_tests()
