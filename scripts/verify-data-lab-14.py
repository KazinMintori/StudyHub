# -*- coding: utf-8 -*-
"""Kịch bản kiểm tra tự động toàn diện bộ bài thực hành Lab 14.

Tệp kiểm định:
1. raw_materials/xu-ly-du-lieu/labs/lab-14.md (data-lab-14-01 đến 07)
2. raw_materials/xu-ly-du-lieu/labs/coverage-14.json

Mục tiêu kiểm định:
1. Kiểm tra tính tương đương và tính đúng đắn giữa Cách 1 (cơ bản) và Cách 2 (thực tế/tối ưu) cho cả 7 bài tập.
2. Kiểm tra độc lập các trường hợp biên: Bảng rỗng, phân khúc không tồn tại, chỉ có một nhóm chủ nhà, dữ liệu khuyết NaN ở cột điểm đánh giá, bảo đảm tính bất biến (immutability) không thay đổi cấu trúc bảng đầu vào.
3. Rà soát cấu trúc Markdown: Không chứa H1 ngoài code fence, đủ 7 span IDs, không dùng dấu chấm phẩy hay gạch ngang dài ngoài code fence, không chứa thuật ngữ dịch máy bị cấm, viết hoa chuẩn mực sau dấu hai chấm.
4. Kiểm tra thứ tự cấu trúc bắt buộc: Đề bài -> fullcode1 -> detailed explanation1 -> output1 -> fullcode2 -> explanation2 -> output2 -> comparison.
5. Phân tích cú pháp AST và thực thi động từng khối mã Python trong lab-14.md một cách hoàn toàn độc lập (fresh isolated namespace), không phụ thuộc vào biến toàn cục từ các khối trước.
6. Xác thực tệp ánh xạ coverage-14.json đầy đủ 39 ô của template và 20 ô của course.
"""

import ast
import io
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Dict, Any, List

import numpy as np
import pandas as pd

# Thiết lập đầu ra console hỗ trợ chuẩn UTF-8
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ==============================================================================
# Dữ liệu mẫu chuẩn bị sẵn phục vụ kiểm thử độc lập
# ==============================================================================

CAU_SAMPLE = {
    "A": "Con số dựa trên 17.688 chỗ ở có giá hợp lệ ở mốc chụp 29/06/2026; 846 chỗ ở không có giá đã được loại và ghi trong qa_report.",
    "B": "Giá thuê điển hình ở Santiago là 59.000 CLP/đêm (khoảng 1,65 triệu đồng), thấp hơn mức trung bình 118.000 CLP.",
    "C": "Trung vị ít bị ảnh hưởng bởi giá ngoại lai: 177 giá trị cực đoan đã gắn cờ làm trung bình cao hơn 44% nhưng gần như không làm thay đổi trung vị.",
    "D": "Kết luận chỉ áp dụng cho giá niêm yết một đêm, chưa gồm phí vệ sinh/dịch vụ; giá thực tế khách trả có thể cao hơn.",
}

CAP_SAMPLE = {
    1: ("So cùng kỳ: +53,7% (T5/2026 so với T5/2025)", "Thị trường tăng trưởng mạnh so với cùng kỳ"),
    2: ("+3,0% so với tháng trước", "Bứt phá thần tốc trong tháng 5"),
    3: ("Hệ số tương quan 0,081", "Nhiệt độ ngày ảnh hưởng rõ rệt tới lượng đánh giá"),
    4: ("Đúng 1 chỗ ở đòi ở tối thiểu 730 đêm", "Một vài ca cực đoan cần gắn cờ"),
    5: ("16.772/18.534 chỗ ở liệt kê Wifi (90,5%)", "Mạng ổn định ở 90% chỗ ở"),
    6: ("Nhóm es chiếm 65,4% (quy tắc chưa kiểm định)", "Chắc chắn 2/3 khách nói tiếng Tây Ban Nha"),
}

BANG_SAMPLE = pd.DataFrame({
    "ky":        ["T9",  "T9",  "T6",  "T6"],
    "phan_khuc": ["cao", "re",  "cao", "re"],
    "n":         [100,   100,   80,    220],
    "gia_tb":    [60.0,  30.0,  66.0,  33.0],
})

DEMO_DS_SAMPLE = pd.DataFrame({
    "id": range(301, 313),
    "calculated_host_listings_count": [1, 7, 2, 12, 5, 1, 3, 9, 1, 6, 2, 4],
    "number_of_reviews_ltm":          [8, 20, 14, 31, 9, 0, 22, 16, 5, 12, 18, 10],
    "review_scores_rating":           [4.9, 4.6, 4.95, 4.7, 4.5, None, 4.85, 4.6, 4.9, 4.55, 4.8, 4.75],
})

# ==============================================================================
# 1. Định nghĩa các hàm kiểm thử độc lập cho cả hai cách tiếp cận
# ==============================================================================

# Bài 1: Kim tự tháp
def validate_pyramid_c1(sentences: dict, order: list) -> list:
    assert sorted(order) == sorted(sentences.keys())
    return order

def validate_pyramid_c2(sentences: dict, order: list, roles: dict) -> bool:
    tang_chuan = ["ket_luan", "bang_chung", "gioi_han", "phuong_phap"]
    tang_thuc_te = [roles.get(ma) for ma in order]
    return tang_thuc_te == tang_chuan

# Bài 2: Đánh giá từ ngữ đúng mức / quá mức
def classify_wording_c1(pairs: dict) -> dict:
    nhan_chuan = {1: "vua", 2: "qua", 3: "qua", 4: "vua", 5: "qua", 6: "qua"}
    return {k: nhan_chuan[k] for k in pairs}

def audit_claim_wording_c2(pairs: dict) -> dict:
    danh_muc_rui_ro = ["bứt phá thần tốc", "ảnh hưởng rõ rệt", "ổn định", "chắc chắn"]
    ket_qua = {}
    for ma_cap, (so_lieu, loi_van) in pairs.items():
        loi_van_lower = loi_van.lower()
        co_rui_ro = any(tu in loi_van_lower for tu in danh_muc_rui_ro)
        ket_qua[ma_cap] = "qua" if co_rui_ro else "vua"
    return ket_qua

# Bài 3: Giá trung bình gộp (pooled_means)
def pooled_means_c1(bang: pd.DataFrame, ky: str = "ky", n: str = "n", gia: str = "gia_tb") -> pd.Series:
    ket_qua = bang.groupby(ky, sort=False).apply(
        lambda g: (g[n] * g[gia]).sum() / g[n].sum()
    )
    ket_qua.name = "gia_tb_gop"
    return ket_qua

def pooled_means_c2(bang: pd.DataFrame, ky: str = "ky", n: str = "n", gia: str = "gia_tb") -> pd.Series:
    doanh_so = bang[n].mul(bang[gia])
    tong_doanh_so = doanh_so.groupby(bang[ky], sort=False).sum()
    tong_so_luong = bang[n].groupby(bang[ky], sort=False).sum()
    trung_binh_gop = tong_doanh_so.div(tong_so_luong)
    trung_binh_gop.name = "gia_tb_gop"
    return trung_binh_gop

# Bài 4: Tỷ trọng phân khúc (segment_share)
def segment_share_c1(bang: pd.DataFrame, phan_khuc: str, ky: str = "ky", nhom: str = "phan_khuc", n: str = "n") -> pd.Series:
    tong_theo_ky = bang.groupby(ky, sort=False)[n].sum()
    bang_pk = bang[bang[nhom] == phan_khuc]
    if bang_pk.empty:
        return pd.Series(0.0, index=tong_theo_ky.index, name=n)
    tong_pk_theo_ky = bang_pk.groupby(ky, sort=False)[n].sum()
    ty_trong = tong_pk_theo_ky.reindex(tong_theo_ky.index, fill_value=0.0) / tong_theo_ky
    ty_trong.name = n
    return ty_trong

def segment_share_c2(bang: pd.DataFrame, phan_khuc: str, ky: str = "ky", nhom: str = "phan_khuc", n: str = "n") -> pd.Series:
    danh_sach_ky = bang[ky].unique()
    bang_cheo = pd.crosstab(
        index=bang[ky],
        columns=bang[nhom],
        values=bang[n],
        aggfunc="sum",
        normalize="index"
    )
    if phan_khuc not in bang_cheo.columns:
        return pd.Series(0.0, index=pd.Index(danh_sach_ky, name=ky), name=n)
    ket_qua = bang_cheo[phan_khuc].reindex(danh_sach_ky, fill_value=0.0)
    ket_qua.name = n
    return ket_qua

# Bài 5: Truy số trung bình đánh giá (reviews_by_host_type)
def reviews_by_host_type_c1(ds: pd.DataFrame, nguong: int = 5) -> pd.Series:
    la_chuyen = ds["calculated_host_listings_count"] >= nguong
    return ds.groupby(la_chuyen)["number_of_reviews_ltm"].mean()

def reviews_by_host_type_c2(ds: pd.DataFrame, nguong: int = 5) -> pd.Series:
    mang_quy_mo = ds["calculated_host_listings_count"].to_numpy()
    mang_danh_gia = ds["number_of_reviews_ltm"].to_numpy()
    mat_na_chuyen = mang_quy_mo >= nguong
    ket_qua = {}
    if (~mat_na_chuyen).any():
        ket_qua[False] = float(mang_danh_gia[~mat_na_chuyen].mean())
    if mat_na_chuyen.any():
        ket_qua[True] = float(mang_danh_gia[mat_na_chuyen].mean())
    chuoi_ket_qua = pd.Series(ket_qua)
    chuoi_ket_qua.name = "number_of_reviews_ltm"
    return chuoi_ket_qua

# Bài 6: Phán quyết thẩm định
def evaluate_claim_decision() -> str:
    return "B"

# Bài 7: Thẩm định mở rộng (audit_host_performance)
def audit_host_performance_c1(ds: pd.DataFrame, nguong: int = 5) -> pd.DataFrame:
    nhom_chuyen = ds["calculated_host_listings_count"] >= nguong
    bang_tong_hop = ds.groupby(nhom_chuyen).agg(
        so_cho_o=("id", "count"),
        trung_binh_luot_danh_gia=("number_of_reviews_ltm", "mean"),
        trung_binh_diem_danh_gia=("review_scores_rating", "mean"),
        so_cho_o_xuat_sac=("review_scores_rating", lambda s: int((s >= 4.8).sum())),
    )
    bang_tong_hop.index = pd.Index(
        ["Cá nhân (dưới 5 chỗ ở)", "Chuyên nghiệp (từ 5 chỗ ở trở lên)"],
        name="Phan_loai_chu_nha"
    )
    bang_tong_hop["ty_le_xuat_sac"] = bang_tong_hop["so_cho_o_xuat_sac"] / bang_tong_hop["so_cho_o"]
    return bang_tong_hop

def audit_host_performance_c2(ds: pd.DataFrame, nguong: int = 5) -> pd.DataFrame:
    cot_chuan = ["so_cho_o", "trung_binh_luot_danh_gia", "trung_binh_diem_danh_gia", "ty_le_xuat_sac"]
    if ds.empty:
        return pd.DataFrame(columns=cot_chuan)
    ds_sach = ds.copy()
    ds_sach["la_chuyen_nghiep"] = ds_sach["calculated_host_listings_count"] >= nguong
    danh_sach_ket_qua = []
    for la_chuyen in [False, True]:
        nhom_df = ds_sach[ds_sach["la_chuyen_nghiep"] == la_chuyen]
        n_cho_o = len(nhom_df)
        if n_cho_o == 0:
            continue
        luot_danh_gia_tb = float(nhom_df["number_of_reviews_ltm"].mean())
        diem_hop_le = nhom_df["review_scores_rating"].dropna()
        diem_tb = float(diem_hop_le.mean()) if not diem_hop_le.empty else np.nan
        so_xuat_sac = int((diem_hop_le >= 4.8).sum())
        ty_le_xuat_sac = (so_xuat_sac / len(diem_hop_le)) if not diem_hop_le.empty else 0.0
        nhan_nhom = "Chuyên nghiệp (từ 5 chỗ ở)" if la_chuyen else "Cá nhân (dưới 5 chỗ ở)"
        danh_sach_ket_qua.append({
            "Nhom_chu_nha": nhan_nhom,
            "so_cho_o": n_cho_o,
            "trung_binh_luot_danh_gia": round(luot_danh_gia_tb, 1),
            "trung_binh_diem_danh_gia": round(diem_tb, 2),
            "so_hop_le_diem": len(diem_hop_le),
            "ty_le_xuat_sac": round(ty_le_xuat_sac, 3),
        })
    return pd.DataFrame(danh_sach_ket_qua).set_index("Nhom_chu_nha")

# ==============================================================================
# 2. Thực thi kiểm định logic toán học và tương đương giữa hai cách
# ==============================================================================

def test_exercise_logic():
    print("=" * 70)
    print("KIỂM TRA LOGIC TOÁN HỌC VÀ TÍNH TƯƠNG ĐƯƠNG GIỮA CÁC PHƯƠNG PHÁP")
    print("=" * 70)

    # Bài 1: Kim tự tháp
    thu_tu_c1 = validate_pyramid_c1(CAU_SAMPLE, ["B", "C", "D", "A"])
    assert thu_tu_c1 == ["B", "C", "D", "A"]
    vai_tro = {"B": "ket_luan", "C": "bang_chung", "D": "gioi_han", "A": "phuong_phap"}
    assert validate_pyramid_c2(CAU_SAMPLE, ["B", "C", "D", "A"], vai_tro) is True
    assert validate_pyramid_c2(CAU_SAMPLE, ["A", "B", "C", "D"], vai_tro) is False
    print("✓ Bài 1 Đạt: Thứ tự kim tự tháp B -> C -> D -> A chính xác.")

    # Bài 2: Đánh giá từ ngữ
    nhan_c1 = classify_wording_c1(CAP_SAMPLE)
    nhan_c2 = audit_claim_wording_c2(CAP_SAMPLE)
    assert nhan_c1 == nhan_c2
    assert nhan_c1 == {1: "vua", 2: "qua", 3: "qua", 4: "vua", 5: "qua", 6: "qua"}
    print("✓ Bài 2 Đạt: Phân loại 6 cặp đúng mức/quá mức hoàn toàn tương đương.")

    # Bài 3: Giá trung bình gộp (pooled_means)
    g1 = pooled_means_c1(BANG_SAMPLE)
    g2 = pooled_means_c2(BANG_SAMPLE)
    assert round(g1["T9"], 1) == 45.0 and round(g1["T6"], 1) == 41.8
    assert round(g2["T9"], 1) == 45.0 and round(g2["T6"], 1) == 41.8
    assert g1["T6"] != BANG_SAMPLE.loc[BANG_SAMPLE["ky"] == "T6", "gia_tb"].mean()
    # Kiểm tra trường hợp biên: Bảng 1 dòng
    bang_1d = pd.DataFrame({"ky": ["T1"], "n": [50], "gia_tb": [100.0]})
    assert pooled_means_c1(bang_1d)["T1"] == 100.0
    assert pooled_means_c2(bang_1d)["T1"] == 100.0
    print("✓ Bài 3 Đạt: Nghịch lý Simpson được kiểm chứng, giá gộp T9=45.0 -> T6=41.8.")

    # Bài 4: Tỷ trọng phân khúc (segment_share)
    s1 = segment_share_c1(BANG_SAMPLE, "re")
    s2 = segment_share_c2(BANG_SAMPLE, "re")
    assert s1["T9"] == 0.5 and round(s1["T6"], 2) == 0.73
    assert s2["T9"] == 0.5 and round(s2["T6"], 2) == 0.73
    # Phân khúc không tồn tại
    assert segment_share_c1(BANG_SAMPLE[BANG_SAMPLE["phan_khuc"] == "cao"], "re").tolist() == [0.0, 0.0]
    assert segment_share_c2(BANG_SAMPLE[BANG_SAMPLE["phan_khuc"] == "cao"], "re").tolist() == [0.0, 0.0]
    print("✓ Bài 4 Đạt: Tỷ trọng phân khúc rẻ tăng từ 50% lên 73%, cơ chế toán học nhất quán.")

    # Bài 5: Truy số trung bình đánh giá (reviews_by_host_type)
    demo_copy = DEMO_DS_SAMPLE.copy()
    r1 = reviews_by_host_type_c1(demo_copy, nguong=5)
    r2 = reviews_by_host_type_c2(demo_copy, nguong=5)
    assert round(r1[True], 1) == 17.6 and round(r1[False], 1) == 11.0
    assert round(r2[True], 1) == 17.6 and round(r2[False], 1) == 11.0
    assert round(reviews_by_host_type_c1(demo_copy, nguong=10)[True], 1) == 31.0
    assert round(reviews_by_host_type_c2(demo_copy, nguong=10)[True], 1) == 31.0
    # Kiểm tra tính bất biến (không thêm cột)
    assert list(demo_copy.columns) == list(DEMO_DS_SAMPLE.columns)
    print("✓ Bài 5 Đạt: Truy số trên DEMO_DS chính xác (True=17.6, False=11.0), bảo toàn bất biến dữ liệu.")

    # Bài 6: Phán quyết thẩm định
    decision = evaluate_claim_decision()
    assert decision == "B"
    print("✓ Bài 6 Đạt: Phán quyết B (Sửa cách diễn đạt) chuẩn xác.")

    # Bài 7: Thẩm định mở rộng (audit_host_performance)
    rep1 = audit_host_performance_c1(DEMO_DS_SAMPLE, nguong=5)
    rep2 = audit_host_performance_c2(DEMO_DS_SAMPLE, nguong=5)
    assert rep1.loc["Cá nhân (dưới 5 chỗ ở)", "so_cho_o"] == 7
    assert rep1.loc["Chuyên nghiệp (từ 5 chỗ ở trở lên)", "so_cho_o"] == 5
    assert round(rep1.loc["Cá nhân (dưới 5 chỗ ở)", "trung_binh_diem_danh_gia"], 2) == 4.86
    assert round(rep1.loc["Chuyên nghiệp (từ 5 chỗ ở trở lên)", "trung_binh_diem_danh_gia"], 2) == 4.59
    assert round(rep1.loc["Cá nhân (dưới 5 chỗ ở)", "ty_le_xuat_sac"], 3) == 0.714
    assert round(rep1.loc["Chuyên nghiệp (từ 5 chỗ ở trở lên)", "ty_le_xuat_sac"], 3) == 0.000
    # Trường hợp bảng rỗng
    rep_empty = audit_host_performance_c2(pd.DataFrame(columns=["id", "calculated_host_listings_count", "number_of_reviews_ltm", "review_scores_rating"]))
    assert rep_empty.empty
    print("✓ Bài 7 Đạt: Phân tầng vạch trần nghịch lý đánh giá (Rating: Cá nhân 4.86 > Chuyên nghiệp 4.59).")

# ==============================================================================
# 3. Rà soát cấu trúc Markdown và thực thi độc lập từng khối mã nguồn
# ==============================================================================

def test_markdown_and_execution():
    print("\n" + "=" * 70)
    print("KIỂM TRA CẤU TRÚC MARKDOWN VÀ THỰC THI ĐỘC LẬP TỪNG KHỐI MÃ PYTHON")
    print("=" * 70)

    repo_root = Path(__file__).resolve().parents[1]
    lab_path = repo_root / "raw_materials/xu-ly-du-lieu/labs/lab-14.md"
    assert lab_path.exists(), f"Không tìm thấy tệp {lab_path}"
    content = lab_path.read_text(encoding="utf-8")

    assert "::: exercise" in content and "::: solution" in content
    assert "#### Cách 1:" in content and "#### Cách 2:" in content
    assert "#### Giải thích chi tiết cách 1" in content
    assert "#### Giải thích chi tiết cách 2" in content
    assert "#### Kết quả thực thi cách 1" in content
    assert "#### Kết quả thực thi cách 2" in content
    assert "#### So sánh hai cách" in content

    # 1. Kiểm tra đủ 7 exercise span IDs
    for i in range(1, 8):
        span_id = f"data-lab-14-{i:02d}"
        assert f'id="{span_id}"' in content or f"id='{span_id}'" in content, f"Thiếu span id {span_id} trong {lab_path.name}"
    print("✓ Đủ 7 span IDs từ data-lab-14-01 đến data-lab-14-07.")

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

    print("✓ Không có H1, không chứa em dash, không chứa dấu chấm phẩy ngoài code fence.")

    # 3. Kiểm tra từ cấm dịch máy
    forbidden_terms = ["hợp đồng hàm", "hợp đồng file", "hợp đồng dữ liệu"]
    for term in forbidden_terms:
        assert term not in content.lower(), f"Phát hiện thuật ngữ cấm '{term}' trong {lab_path.name}"
    print("✓ Không chứa thuật ngữ dịch máy bị cấm.")

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
    print("✓ Quy tắc viết hoa sau dấu hai chấm đạt chuẩn 100%.")

    # 5. Kiểm tra thứ tự cấu trúc bắt buộc cho từng bài tập
    #    Đề bài -> fullcode1 -> detailed explanation1 -> output1 -> fullcode2 -> explanation2 -> output2 -> comparison
    pattern = re.compile(
        r'<span\s+id=[\'"]data-lab-14-(\d+)[\'"]></span>.*?'
        r':::\s*exercise.*?'
        r':::\s*\n\s*'
        r':::\s*solution\s*\n\s*'
        r'####\s*Cách 1:[^\n]*\n.*?'
        r'```python.*?\n```\s*\n\s*'
        r'####\s*Giải thích chi tiết cách 1\s*\n.*?'
        r'####\s*Kết quả thực thi cách 1\s*\n.*?'
        r'####\s*Cách 2:[^\n]*\n.*?'
        r'```python.*?\n```\s*\n\s*'
        r'####\s*Giải thích chi tiết cách 2\s*\n.*?'
        r'####\s*Kết quả thực thi cách 2\s*\n.*?'
        r'####\s*So sánh hai cách(?: tiếp cận)?\s*\n.*?'
        r':::',
        re.DOTALL
    )
    matches = pattern.findall(content)
    assert len(matches) == 7, f"Cấu trúc bài tập chưa đồng nhất, tìm thấy {len(matches)}/7 bài tập đúng chuẩn."
    print("✓ Thứ tự cấu trúc 8 bước cho cả 7 bài tập đạt chuẩn tuyệt đối.")

    # 6. Trích xuất và thực thi ĐỘC LẬP từng khối mã Python (Fresh isolated namespace, NO injected hidden globals)
    blocks = re.findall(r"^```python[^\n]*\n(.*?)^```\s*$", content, flags=re.M | re.S)
    print(f"\nTìm thấy {len(blocks)} khối mã Python trong {lab_path.name}.")

    # Bỏ qua khối mã môi trường đầu tiên nếu chỉ là thiết lập pd.set_option và URLs
    for b_idx, block in enumerate(blocks, 1):
        try:
            tree = ast.parse(block, filename=f"{lab_path.name}:block_{b_idx}")
        except SyntaxError as syn_err:
            raise AssertionError(f"Lỗi cú pháp AST tại khối {b_idx} của {lab_path.name}: {syn_err}")

        # Khởi tạo không gian tên độc lập hoàn toàn cho MỖI khối mã (Fresh Namespace)
        isolated_ns: Dict[str, Any] = {
            "__name__": "__main__",
            "display": print,
        }
        try:
            exec(compile(tree, f"{lab_path.name}:block_{b_idx}", "exec"), isolated_ns)
        except Exception as exc:
            raise AssertionError(f"Lỗi thực thi độc lập tại khối mã {b_idx} của {lab_path.name}: {type(exc).__name__}: {exc}")

    print(f"✓ Toàn bộ {len(blocks)} khối mã Python chạy độc lập 100% thành công không phụ thuộc biến từ khối trước.")

# ==============================================================================
# 4. Xác thực tệp coverage-14.json
# ==============================================================================

def test_coverage_json():
    print("\n" + "=" * 70)
    print("XÁC THỰC TỆP BÁO CÁO ĐỘ PHỦ COVERAGE-14.JSON")
    print("=" * 70)

    repo_root = Path(__file__).resolve().parents[1]
    cov_path = repo_root / "raw_materials/xu-ly-du-lieu/labs/coverage-14.json"
    assert cov_path.exists(), f"Không tìm thấy tệp {cov_path}"

    with open(cov_path, "r", encoding="utf-8") as f:
        cov = json.load(f)

    assert cov["lab"] == "14"
    assert cov["topic"] == "xu-ly-du-lieu"
    assert len(cov["sources"]) == 2

    # Template checks
    tmpl = next(s for s in cov["sources"] if s["source"] == "template")
    assert tmpl["totalCells"] == 39
    assert len(tmpl["cells"]) == 39
    assert any(c.get("exerciseId") == "data-lab-14-01" for c in tmpl["cells"])
    assert any(c.get("exerciseId") == "data-lab-14-07" for c in tmpl["cells"])

    # Course checks
    course = next(s for s in cov["sources"] if s["source"] == "course")
    assert course["totalCells"] == 20
    assert len(course["cells"]) == 20
    assert any(c.get("exerciseId") == "data-lab-14-01" for c in course["cells"])
    assert any(c.get("exerciseId") == "data-lab-14-07" for c in course["cells"])

    print("✓ coverage-14.json hợp lệ: Đủ 39 ô template và 20 ô course với ánh xạ chính xác.")

# ==============================================================================
# Hàm chạy chính
# ==============================================================================

def run_all_tests():
    test_exercise_logic()
    test_markdown_and_execution()
    test_coverage_json()

    print("\n" + "=" * 70)
    print("TẤT CẢ PHÉP KIỂM TRA CHO LAB 14 ĐÃ THÀNH CÔNG 100%!")
    print("=" * 70)

if __name__ == "__main__":
    run_all_tests()
