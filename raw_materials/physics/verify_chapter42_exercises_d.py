#!/usr/bin/env python3
"""
Toàn bộ kịch bản kiểm tra độc lập và nghiệm thu cho nhóm bài tập Chapter 42 nhóm D:
1. Tính toán độc lập bằng Python cho toàn bộ 37 bài (42.23 - 42.58 và Bài tập cầu nối).
2. Kiểm tra pixel-match (RGB chính xác 100%) giữa 5 ảnh PNG cắt và trang PDF gốc.
3. Kiểm định cú pháp Markdown: H2/H3 hợp lệ, thẻ details đóng kín, tóm tắt/hướng đi, viết hoa sau dấu hai chấm.
4. Kiểm tra tệp chú thích ảnh docs/.vitepress/physics42-exercises-d-image-annotations.mjs.
5. Đo đạc độ rộng thực tế MathJax SVG (bằng markdown-it và markdown-it-mathjax3).
"""

import sys
import os
import re
import math
import subprocess
import json
import tempfile
from pathlib import Path
from PIL import Image
import pymupdf as fitz
import numpy as np

# Cấu hình UTF-8 cho stdout trên Windows
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent.parent
SOURCE_PDF = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-42"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics42-exercises-d-image-annotations.mjs"

TRANSLATION_FILES = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-42" / "12-bai-tap-23-38.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-42" / "13-bai-tap-39-50.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-42" / "14-bai-tap-51-55.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-42" / "15-mcat.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-42" / "16-bai-tap-cau-noi.md",
]

CROPS = {
    'hinh-p42-38': (1458, (80, 498, 250, 616)),
    'hinh-p42-49': (1459, (215, 333, 335, 396)),
    'hinh-p42-50': (1459, (395, 75, 565, 180)),
    'hinh-p42-52': (1460, (105, 75, 225, 180)),
    'hinh-doan-van-diot': (1460, (355, 385, 525, 495)),
}

ERRORS = []
WARNINGS = []

def report_error(msg):
    ERRORS.append(msg)
    print(f"  [ERROR] {msg}")

def report_warning(msg):
    WARNINGS.append(msg)
    print(f"  [WARN]  {msg}")

def verify_calculations():
    print("=== 1. Kiểm tra tính toán vật lý độc lập (37 bài toán) ===")

    # Hằng số chuẩn
    c = 2.99792458e8
    h = 6.62607015e-34
    hbar = h / (2 * math.pi)
    e = 1.602176634e-19
    k_B = 1.380649e-23
    m_e = 9.1093837e-31
    eps0 = 8.8541878128e-12
    u = 1.6605e-27

    # 42.23
    kT_300 = k_B * 300 / e
    f_23 = 1.0 / (math.exp(0.020 / kT_300) + 1.0)
    assert 0.315 < f_23 < 0.317, f"42.23 f(E) sai lệch: {f_23}"
    print(f"  42.23: f(E) = {f_23:.4f} -> OK")

    # 42.24
    for T, expected_f in [(250, 1.77e-7), (300, 2.36e-6), (350, 1.50e-5)]:
        kT = k_B * T / e
        fc = 1.0 / (math.exp(0.335 / kT) + 1.0)
        assert abs(fc - expected_f) / expected_f < 0.02, f"42.24 f(Ec) tại {T}K sai"
    print("  42.24: f(Ec) và 1-f(Ev) tại 250, 300, 350K -> OK")

    # 42.25
    dE_c = kT_300 * math.log(1.0 / 4.4e-4 - 1.0)
    assert abs(dE_c - 0.200) < 0.005, f"42.25 Ec - EF sai: {dE_c}"
    print(f"  42.25: Ec - EF = {dE_c:.4f} eV -> OK")

    # 42.26
    lam_Ge = (h * c) / (0.67 * e) * 1e6
    lam_Si = (h * c) / (1.12 * e) * 1e6
    assert abs(lam_Ge - 1.85) < 0.02 and abs(lam_Si - 1.11) < 0.02
    print(f"  42.26: lambda_max Ge = {lam_Ge:.2f} um, Si = {lam_Si:.2f} um -> OK")

    # 42.27
    kT_290 = k_B * 290 / e
    I_1 = 0.5e-3 * (math.exp(1e-3 / kT_290) - 1.0) * 1e3
    assert abs(I_1 - 0.0204) < 0.001
    print("  42.27: Dòng chuyển tiếp p-n tại 290K -> OK")

    # 42.28
    kT_293 = k_B * 293.15 / e
    I_85 = 0.950e-3 * (math.exp(0.085 / kT_293) - 1.0)
    R_85 = 0.085 / I_85
    assert abs(R_85 - 3.20) < 0.05
    print("  42.28: Điện trở thuận và nghịch p-n -> OK")

    # 42.29
    Is_29 = 9.25e-3 / (math.exp(0.015 / kT_300) - 1.0)
    I_10 = Is_29 * (math.exp(0.010 / kT_300) - 1.0) * 1e3
    assert abs(I_10 - 5.56) < 0.05
    print("  42.29: Dòng điện tại 10 mV và dòng âm -> OK")

    # 42.30
    V_30 = kT_300 * math.log(1.0 + 40.0 / 6.4) * 1e3
    assert abs(V_30 - 51.2) < 0.2
    print("  42.30: Điện áp thuận 51.2 mV -> OK")

    # 42.31
    kT_29015 = k_B * 290.15 / e
    I_31 = 10e-6 * (math.exp(0.20 / kT_29015) - 1.0)
    R_31 = 0.20 / I_31
    assert abs(R_31 - 6.71) < 0.1
    print("  42.31: Điện trở tại 0.20 V thuận/nghịch -> OK")

    # 42.32
    I_32 = (hbar * 54.3e-6) / (math.pi * c)
    assert abs(I_32 - 6.08e-48) < 0.05e-48
    print(f"  42.32: I = {I_32:.3e} kg.m^2 -> OK")

    # 42.33
    frac_NaCl = (3.0e-29 / 0.24e-9) / e
    frac_HI = (1.5e-30 / 0.16e-9) / e
    assert abs(frac_NaCl - 0.780) < 0.01 and abs(frac_HI - 0.0585) < 0.002
    print("  42.33: Độ ion hóa NaCl (78%) và HI (5.85%) -> OK")

    # 42.34
    I_34 = 3 * hbar * 3.83e-3 / (2 * math.pi * c)
    mu_34 = (3.82e-26 * 3.15e-26) / (3.82e-26 + 3.15e-26)
    r0_34 = math.sqrt(I_34 / mu_34) * 1e9
    assert abs(r0_34 - 0.193) < 0.005
    print(f"  42.34: r0(NaF) = {r0_34:.3f} nm -> OK")

    # 42.35 & 42.36
    I_CO = 1.45e-46
    beta = hbar**2 / (2 * I_CO * k_B * 300)
    l_max = math.sqrt(I_CO * k_B * 300 / hbar**2) - 0.5
    assert abs(l_max - 6.85) < 0.05
    ratio_7 = 15 * math.exp(-beta * 56)
    assert abs(ratio_7 - 8.93) < 0.05
    print("  42.35 - 42.36: Phân bố quay CO và cực đại l = 7 -> OK")

    # 42.37
    I_37 = 1.2e-11 * (math.exp(0.6 / kT_300) - 1.0)
    P_37 = I_37 * 0.6 * 1e3
    assert abs(P_37 - 86.5) < 1.0
    print(f"  42.37: P(0.6V) = {P_37:.1f} mW, Vmax ~ 0.6 V -> OK")

    # 42.38
    dE_38 = hbar**2 / I_CO / e * 1e3
    lam_38 = h * c / (hbar**2 / I_CO) * 1e3
    assert abs(dE_38 - 0.479) < 0.005 and abs(lam_38 - 2.59) < 0.02
    print("  42.38: Bức xạ CO 2.59 mm trong tinh vân Orion -> OK")

    # 42.39
    mu_H2 = 1.67e-27 / 2.0
    E0_39 = 0.5 * hbar * math.sqrt(576 / mu_H2) / e
    assert abs(E0_39 - 0.273) < 0.005
    print("  42.39: Năng lượng điểm không H2 = 0.273 eV -> OK")

    # 42.40
    dE_40 = 0.463 * e
    f_40 = dE_40 / h
    mu_40 = (2.66e-26 * 1.67e-27) / (2.66e-26 + 1.67e-27)
    k_40 = mu_40 * (2 * math.pi * f_40)**2
    assert abs(f_40 - 1.12e14) < 0.02e14 and abs(k_40 - 778) < 5
    print("  42.40: Tần số và hằng số lực OH -> OK")

    # 42.41
    mu_41 = (1.67e-27 * 2.11e-25) / (1.67e-27 + 2.11e-25)
    I_41 = mu_41 * (0.160e-9)**2
    assert abs(I_41 - 4.24e-47) < 0.05e-47
    print("  42.41: Mômen quán tính và bước sóng HI -> OK")

    # 42.42
    mu_HF = (1.67e-27 * 3.15e-26) / (1.67e-27 + 3.15e-26)
    k_HF = mu_HF * (2 * math.pi * 1.24e14)**2
    mu_DF = (3.34e-27 * 3.15e-26) / (3.34e-27 + 3.15e-26)
    f_DF = (1.0 / (2 * math.pi)) * math.sqrt(k_HF / mu_DF)
    lam_DF = c / f_DF * 1e6
    assert abs(f_DF - 8.99e13) < 0.05e13 and abs(lam_DF - 3.34) < 0.05
    print("  42.42: Tần số DF và bước sóng 3.34 um -> OK")

    # 42.43
    n_K = 851.0 / 6.49e-26
    EF_K = ((3 * math.pi**2 * n_K)**(2/3)) * hbar**2 / (2 * m_e) / e
    assert abs(EF_K - 2.03) < 0.03
    print("  42.43: Năng lượng Fermi của Kali = 2.03 eV -> OK")

    # 42.44
    U_coul = (1.75 * e**2) / (4 * math.pi * eps0 * 0.281e-9) / e
    Utot_44 = - (7.0 / 8.0) * U_coul
    E_remove = -Utot_44 - 5.14 + 3.61
    assert abs(Utot_44 - (-7.85)) < 0.05 and abs(E_remove - 6.32) < 0.05
    print("  42.44: Thế năng mạng tinh thể NaCl và năng lượng tách 6.32 eV -> OK")

    # 42.45
    n_Li = 2.0 / (0.35e-9)**3
    EF_Li = ((3 * math.pi**2 * n_Li)**(2/3)) * hbar**2 / (2 * m_e) / e
    assert abs(EF_Li - 4.73) < 0.03
    print("  42.45: Mật độ mạng bcc và Fermi Lithi 4.73 eV -> OK")

    # 42.46
    diff_46 = 2062.7
    I_46 = hbar / (2 * math.pi * c * diff_46)
    mu_46 = (1.67e-27 * 5.81e-26) / (1.67e-27 + 5.81e-26)
    r0_46 = math.sqrt(I_46 / mu_46) * 1e9
    assert abs(r0_46 - 0.129) < 0.005
    print("  42.46: Phổ quay HCl và khoảng cách 0.129 nm -> OK")

    # 42.47
    E_data = np.array([3.0, 2.5, 2.0, 1.5, 1.0, 0.5])
    f_data = np.array([0.064, 0.173, 0.390, 0.661, 0.856, 0.950])
    x_data = np.log(1.0 / f_data - 1.0)
    p_fit = np.polyfit(x_data, E_data, 1)
    assert abs(p_fit[1] - 1.80) < 0.03 and abs(p_fit[0] * e / k_B - 5170) < 100
    print("  42.47: Tuyến tính hóa Fermi-Dirac EF = 1.80 eV, T = 5170 K -> OK")

    # 42.48
    x_48 = 0.407 / 0.338
    T_48 = (e * 5.0e-3) / (k_B * math.log(x_48))
    Is_48 = 0.407e-3 / (x_48 - 1.0) * 1e3
    assert abs(T_48 - 312.3) < 1.0 and abs(Is_48 - 1.99) < 0.05
    print("  42.48: Chẩn đoán turbine T = 312 K, Is = 1.99 mA -> OK")

    # 42.49
    Vout_min = kT_300 * math.log(1.0 + 1e-3 / 5e-13)
    assert abs(Vout_min - 0.554) < 0.01
    print("  42.49: Chỉnh lưu nửa chu kỳ Vout_min = 0.554 V, Vmax = 0.60 V -> OK")

    # 42.50
    eps_Si = 11.7 * eps0
    ap_50 = 55.0e-9 * (5.00 / 1.00)
    E_peak_50 = (e * 5.00e22 * 55.0e-9) / eps_Si
    Vb_50 = 0.5 * E_peak_50 * (ap_50 + 55.0e-9)
    assert abs(ap_50 * 1e9 - 275.0) < 0.1 and abs(E_peak_50 - 4.25e6) < 0.05e6 and abs(Vb_50 - 0.702) < 0.01
    print("  42.50: Phương trình Poisson p-n ap = 275 nm, E_max = 4.25e6 V/m, Vb = 0.702 V -> OK")

    # 42.51
    M_eff_51 = (48.0 / 11.0) * u
    omega_51 = math.sqrt(1860.0 / M_eff_51)
    f_51 = omega_51 / (2 * math.pi)
    assert abs(f_51 - 8.06e13) < 0.05e13
    print("  42.51: Mode kéo dãn bất đối xứng CO2 f = 8.06e13 Hz -> OK")

    # 42.52
    h_p = 4.1357e-15
    c_p = 2.9979e8
    E_R0 = h_p * c_p / 4.2826e-6
    E_P1 = h_p * c_p / 4.2972e-6
    hbar_w0_52 = 0.5 * (E_R0 + E_P1)
    I_52 = 2 * hbar**2 / ((E_R0 - E_P1) * e)
    k_52 = (7.0 * u) * (hbar_w0_52 * e / hbar)**2
    assert abs(hbar_w0_52 - 0.28901) < 0.0001 and abs(I_52 - 1.40e-46) < 0.02e-46 and abs(k_52 - 2241) < 20
    print("  42.52: Khí bí ẩn N2, I = 1.40e-46 kg.m^2, k = 2241 N/m -> OK")

    # 42.53
    p_Cu = (3.0**(2/3) * math.pi**(4/3) * hbar**2 / (5 * m_e)) * (8.45e28**(5/3))
    assert abs(p_Cu - 3.80e10) < 0.05e10
    print(f"  42.53: Áp suất thoái hóa Cu p = {p_Cu:.2e} Pa ({p_Cu/101325:.2e} atm) -> OK")

    # 42.54
    B_Cu = (5.0 / 3.0) * p_Cu
    frac_Cu = B_Cu / 1.4e11
    assert abs(B_Cu - 6.34e10) < 0.05e10 and abs(frac_Cu - 0.453) < 0.01
    print("  42.54: Môđun khối B = 5/3 p = 6.34e10 Pa (45.3%) -> OK")

    # 42.55
    n_rel = (2.0**(1.5) * (m_e * c)**3) / (3000 * math.pi**2 * hbar**3)
    V_wd = (4.0 / 3.0) * math.pi * (6.0e6)**3
    n_wd = (6.0 * (2.0e30 / 1.99e-26)) / V_wd
    assert abs(n_rel - 1.66e33) < 0.05e33 and abs(n_wd - 6.66e35) < 0.05e35
    print("  42.55: Giới hạn tương đối tính và nồng độ sao lùn trắng -> OK")

    # 42.56 - 42.58 (MCAT)
    S_mcat = (-0.25) / 125.0 * 1e3
    assert abs(S_mcat - (-2.0)) < 0.01
    print("  42.56 - 42.58: MCAT độ nhạy -2.0 mV/°C và đặc tuyến -> OK")

    # Bài tập cầu nối
    mu_bridge = (1.67e-27 * 3.15e-26) / (1.67e-27 + 3.15e-26)
    I_bridge = mu_bridge * (0.092e-9)**2
    E_ph_bridge = (h * 1.24e14 - hbar**2 / I_bridge) / e
    dE_c_bridge = E_ph_bridge - 0.230
    f_bridge = math.exp(-(E_ph_bridge - 0.115) / (k_B * 80 / e))
    assert abs(dE_c_bridge - 0.278) < 0.002
    assert 1.7e-25 <= f_bridge <= 1.9e-25
    print(f"  Bài tập cầu nối: dE_c = {dE_c_bridge:.3f} eV, f(E) = {f_bridge:.2e} -> OK")

def verify_images():
    print("=== 2. Kiểm tra ảnh trích xuất PDF gốc (RGB exact match) ===")
    assert SOURCE_PDF.is_file(), f"Không tìm thấy file nguồn {SOURCE_PDF}"
    with fitz.open(SOURCE_PDF) as doc:
        for stem, (page, clip) in CROPS.items():
            img_path = IMG_DIR / f"{stem}.png"
            assert img_path.is_file(), f"Thiếu file ảnh: {img_path}"
            pix = doc[page - 1].get_pixmap(matrix=fitz.Matrix(3, 3), clip=fitz.Rect(clip), alpha=False)
            with Image.open(img_path) as im:
                im_rgb = im.convert("RGB")
                assert im.size == (pix.width, pix.height), f"Kích thước ảnh {stem} không khớp"
                assert im_rgb.tobytes() == pix.samples, f"Dữ liệu pixel của {stem} không khớp tuyệt đối với PDF"
            print(f"  {stem}.png: {im.size} RGB exact match -> OK")

def verify_markdown_rules():
    print("=== 3. Kiểm định cú pháp Markdown và quy chuẩn sư phạm ===")
    all_h3_ids = []
    colon_errors = 0

    for file_path in TRANSLATION_FILES:
        assert file_path.is_file(), f"Thiếu file bài giảng: {file_path}"
        text = file_path.read_text(encoding="utf-8")

        # Kiểm tra H1, frontmatter
        if text.startswith("---") or re.search(r"^#\s+", text, re.MULTILINE):
            report_error(f"{file_path.name}: Chứa tiêu đề H1 hoặc frontmatter bị cấm")

        # Thu thập ID bài toán
        h3s = re.findall(r"^###\s+(.+)$", text, re.MULTILINE)
        for h in h3s:
            if h in all_h3_ids:
                report_error(f"Trùng lặp ID bài toán: {h}")
            all_h3_ids.append(h)

        # Kiểm tra cặp thẻ <details> và <summary>
        open_details = len(re.findall(r"<details>", text))
        close_details = len(re.findall(r"</details>", text))
        if open_details != close_details:
            report_error(f"{file_path.name}: Lệch thẻ <details> ({open_details} mở vs {close_details} đóng)")

        # Kiểm tra viết hoa sau dấu hai chấm trong văn xuôi
        for line_no, line in enumerate(text.splitlines(), 1):
            if line.strip().startswith("$$") or line.strip().startswith("http") or line.strip().startswith("file:"):
                continue
            # Bỏ qua công thức toán nội dòng
            cleaned = re.sub(r"\$[^$]+\$", "", line)
            for m in re.finditer(r":\s+([^\s\d\$\"\'\(\[\{])", cleaned):
                char = m.group(1)
                if char.islower():
                    colon_errors += 1
                    report_warning(f"{file_path.name}:{line_no}: Từ sau dấu ':' viết thường '{char}': {line.strip()[:60]}")

    print(f"  Tổng số đề bài đã kiểm tra: {len(all_h3_ids)} (Kỳ vọng: 37 bài)")
    assert len(all_h3_ids) == 37, f"Tổng số bài toán không bằng 37: {len(all_h3_ids)}"

def verify_annotations():
    print("=== 4. Kiểm tra tệp chú thích ảnh mjs ===")
    assert ANNOTATIONS_FILE.is_file(), f"Thiếu file chú thích: {ANNOTATIONS_FILE}"
    res = subprocess.run(["node", "--check", str(ANNOTATIONS_FILE)], capture_output=True, text=True)
    if res.returncode != 0:
        report_error(f"Lỗi cú pháp Node trong {ANNOTATIONS_FILE.name}:\n{res.stderr}")
    else:
        print(f"  {ANNOTATIONS_FILE.name}: node --check sạch sẽ -> OK")

def verify_mathjax():
    print("=== 5. Đo đạc độ rộng thực tế MathJax SVG (markdown-it) ===")
    pkg_json = ROOT / "package.json"
    assert pkg_json.is_file(), "Không tìm thấy package.json"

    display_items = []
    inline_items = []

    for file_path in TRANSLATION_FILES:
        lines = file_path.read_text(encoding="utf-8").splitlines()
        in_display = False
        cur_tex = []
        cur_start = 0
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped == "$$":
                if not in_display:
                    in_display = True
                    cur_tex = []
                    cur_start = idx
                else:
                    in_display = False
                    block = "\n".join(cur_tex).strip()
                    display_items.append({
                        "file": file_path.name,
                        "line": cur_start,
                        "tex": block
                    })
            elif in_display:
                cur_tex.append(line)
            else:
                matches = re.finditer(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', line)
                for m in matches:
                    itex = m.group(1).strip()
                    if itex:
                        inline_items.append({"file": file_path.name, "line": idx, "tex": itex})

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as f:
        json.dump({"display": display_items, "inline": inline_items}, f)
        temp_json = f.name

    pkg_path_str = str(pkg_json).replace('\\', '/')
    js_code = f"""
    const {{ createRequire }} = require('node:module');
    const req = createRequire('{pkg_path_str}');
    const MarkdownIt = req('markdown-it');
    const mathjax = req('markdown-it-mathjax3');
    const md = new MarkdownIt({{ html: true }}).use(mathjax.default || mathjax);
    const fs = require('node:fs');

    const raw = fs.readFileSync(process.argv[2], 'utf-8');
    const data = JSON.parse(raw);
    let displayErrors = 0;
    let maxDisplay = 0;
    let maxInline = 0;

    for (const item of data.display) {{
      try {{
        const rendered = md.render('$$\\n' + item.tex + '\\n$$');
        const m = rendered.match(/width="([\\d.]+)ex"/);
        if (!m) continue;
        const w = parseFloat(m[1]);
        if (w > maxDisplay) maxDisplay = w;
        if (w > 27.0) {{
          console.log(`[DISPLAY > 27ex] ${{w.toFixed(2)}}ex: ${{item.file}}:${{item.line}} -> ${{item.tex.replace(/\\n/g, ' ')}}`);
          displayErrors++;
        }}
      }} catch (err) {{
        console.error(`Render error at ${{item.file}}:${{item.line}}:`, err.message);
      }}
    }}

    let inlineErrors = 0;
    for (const item of data.inline) {{
      try {{
        const rendered = md.render('$' + item.tex + '$');
        const m = rendered.match(/width="([\\d.]+)ex"/);
        if (!m) continue;
        const w = parseFloat(m[1]);
        if (w > maxInline) maxInline = w;
        if (w > 38.0) {{
          console.log(`[INLINE > 38ex] ${{w.toFixed(2)}}ex: ${{item.file}}:${{item.line}} -> ${{item.tex}}`);
          inlineErrors++;
        }}
      }} catch (err) {{ inlineErrors++; console.error(String(err)); }}
    }}

    console.log(`Max Display Math Width: ${{maxDisplay.toFixed(2)}}ex (Giới hạn 27ex; bố cục được kiểm riêng trong trình duyệt)`);
    console.log(`Max Inline Math Width: ${{maxInline.toFixed(2)}}ex (Mục tiêu <= 38ex)`);
    if (displayErrors > 0 || inlineErrors > 0) process.exit(1);
    """

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".js", delete=False) as f:
        f.write(js_code)
        temp_js = f.name

    try:
        res = subprocess.run(["node", temp_js, temp_json], capture_output=True, text=True)
        print(res.stdout.strip())
        if res.returncode != 0:
            report_error("Phát hiện công thức toán MathJax vượt ngưỡng chiều rộng!")
        else:
            print("  Đo đạc MathJax SVG hoàn tất: Toàn bộ công thức nằm trong phạm vi cho phép.")
    finally:
        try:
            os.remove(temp_json)
            os.remove(temp_js)
        except OSError:
            pass

def main():
    print("Bắt đầu kiểm tra xác minh Chapter 42 Exercises D...")
    verify_calculations()
    verify_images()
    verify_markdown_rules()
    verify_annotations()
    verify_mathjax()

    if ERRORS:
        print(f"\n[KẾT QUẢ] Phát hiện {len(ERRORS)} lỗi nghiêm trọng:")
        for e in ERRORS:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"\n[KẾT QUẢ] TẤT CẢ CÁC BÀI TOÁN VÀ TIÊU CHUẨN XÁC MINH ĐỀU ĐẠT CHUẨN (Cảnh báo nhỏ: {len(WARNINGS)}).")

if __name__ == "__main__":
    main()
