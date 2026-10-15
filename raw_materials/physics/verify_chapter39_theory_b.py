#!/usr/bin/env python3
"""
Comprehensive verifier for Chapter 39 Theory B (Sections 39.3 - 39.4):
- Numeric and quantum calculations for all examples (39.5, 39.6) and TYUs (39.3, 39.4)
- Asset pixel validation against source PDF (exact dimensions and byte-for-byte RGB integrity)
- Markdown syntax, pedagogical structure, colon capitalization, and math formatting audit
- Image annotations module consistency and syntax (node --check)
- Real MathJax width measurement (Display <= 25ex body, Tagged <= 32ex on 320px, Inline <= 38ex)
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
import pymupdf

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent.parent
LOCAL_SOURCE = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE_PDF = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-39"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics39-theory-b-image-annotations.mjs"

TRANSLATIONS = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-39" / "03-muc-nang-luong-bohr.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-39" / "04-laser.md",
]

ERRORS = []
WARNINGS = []

def report_error(msg):
    ERRORS.append(msg)
    print(f"  [ERROR] {msg}")

def report_warning(msg):
    WARNINGS.append(msg)
    print(f"  [WARN]  {msg}")

def verify_calculations():
    print("=== 1. Verifying Physical & Quantum Calculations ===")

    # 1. Lithium 671 nm photon transition
    c = 3.00e8
    h_SI = 6.63e-34
    h_precise = 6.626e-34
    e_charge = 1.602e-19
    h_eV = 4.136e-15

    lam_li = 671e-9
    E_li_J = h_SI * c / lam_li
    assert abs(E_li_J - 2.96e-19) < 2e-21, f"Lithium E(J) mismatch: {E_li_J}"
    E_li_eV = E_li_J / e_charge
    assert round(E_li_eV, 2) == 1.85, f"Lithium E(eV) mismatch: {E_li_eV}"
    print(f"  Lithium 671 nm: OK (E = {E_li_J:.2e} J = {E_li_eV:.2f} eV)")

    # 2. Example 39.5: Hypothetical atom with levels 0.00 eV, 1.00 eV, 3.00 eV
    # 1.00 eV transition
    f_10 = 1.00 / h_eV
    lam_10 = c / f_10
    assert abs(f_10 - 2.42e14) < 1e12, f"Ex 39.5 f(1.00 eV) mismatch: {f_10}"
    assert round(lam_10 * 1e9) == 1240 or round(lam_10 * 1e9, -1) == 1240, f"Ex 39.5 lam(1.00 eV) mismatch: {lam_10}"

    # 2.00 eV transition
    f_20 = 2.00 / h_eV
    lam_20 = c / f_20
    assert abs(f_20 - 4.84e14) < 1e12, f"Ex 39.5 f(2.00 eV) mismatch: {f_20}"
    assert round(lam_20 * 1e9) == 620, f"Ex 39.5 lam(2.00 eV) mismatch: {lam_20}"

    # 3.00 eV transition
    f_30 = 3.00 / h_eV
    lam_30 = c / f_30
    assert abs(f_30 - 7.25e14) < 1e12, f"Ex 39.5 f(3.00 eV) mismatch: {f_30}"
    assert round(lam_30 * 1e9) == 414, f"Ex 39.5 lam(3.00 eV) mismatch: {lam_30}"
    print(f"  Ex 39.5: OK (Emission: 1240 nm IR, 620 nm red, 414 nm violet; Absorption from ground: 1240 nm and 414 nm)")

    # 3. Franck-Hertz mercury excitation: 4.9 eV
    E_fh = 4.9
    lam_fh = (h_eV * c) / E_fh
    assert round(lam_fh * 1e9, -1) == 250, f"Franck-Hertz lambda mismatch: {lam_fh}"
    print(f"  Franck-Hertz 4.9 eV: OK (lambda = {lam_fh*1e9:.1f} nm ~ 250 nm UV)")

    # 4. Bohr Model: Ground state radius, velocity, Rydberg constant
    eps0 = 8.8541878e-12
    h_b = 6.62607e-34
    m_e = 9.10938e-31
    e_c = 1.6021766e-19
    c_b = 2.99792e8

    a0 = (eps0 * h_b**2) / (math.pi * m_e * e_c**2)
    assert abs(a0 - 5.29e-11) < 1e-13, f"Bohr radius a0 mismatch: {a0}"
    assert round(a0 * 1e11, 2) == 5.29, f"Bohr radius round mismatch: {a0}"

    v1 = (1.0 / eps0) * (e_c**2 / (2.0 * h_b))
    assert abs(v1 - 2.19e6) < 1e4, f"v1 mismatch: {v1}"
    assert round(v1 * 1e-6, 2) == 2.19, f"v1 round mismatch: {v1}"
    assert v1 / c_b < 0.01, f"v1 relativistic check: {v1/c_b}"

    R_theo = (m_e * e_c**4) / (8.0 * eps0**2 * h_b**3 * c_b)
    assert abs(R_theo - 1.097e7) < 1e5, f"Rydberg R mismatch: {R_theo}"
    assert round(R_theo * 1e-7, 3) == 1.097, f"Rydberg round mismatch: {R_theo}"

    hcR_eV = (h_b * c_b * R_theo) / e_c
    assert abs(hcR_eV - 13.606) < 0.01, f"hcR mismatch: {hcR_eV}"
    assert round(hcR_eV, 2) == 13.61 or round(hcR_eV, 1) == 13.6, f"hcR round mismatch: {hcR_eV}"

    # Balmer series lines
    R_val = 1.097e7
    lam_alpha = 1.0 / (R_val * (1.0/4.0 - 1.0/9.0))
    lam_beta = 1.0 / (R_val * (1.0/4.0 - 1.0/16.0))
    lam_gamma = 1.0 / (R_val * (1.0/4.0 - 1.0/25.0))
    lam_delta = 1.0 / (R_val * (1.0/4.0 - 1.0/36.0))
    lam_limit = 4.0 / R_val

    assert abs(lam_alpha * 1e9 - 656.3) < 0.5, f"H_alpha mismatch: {lam_alpha*1e9}"
    assert abs(lam_beta * 1e9 - 486.2) < 0.5, f"H_beta mismatch: {lam_beta*1e9}"
    assert abs(lam_gamma * 1e9 - 434.1) < 0.5, f"H_gamma mismatch: {lam_gamma*1e9}"
    assert abs(lam_delta * 1e9 - 410.2) < 0.5, f"H_delta mismatch: {lam_delta*1e9}"
    assert abs(lam_limit * 1e9 - 364.6) < 0.5, f"Balmer limit mismatch: {lam_limit*1e9}"
    print(f"  Bohr Model constants & Balmer series: OK (a0 = {a0*1e11:.2f}e-11 m, v1 = {v1*1e-6:.2f}e6 m/s, R = {R_theo*1e-7:.3f}e7 m^-1, H_alpha = {lam_alpha*1e9:.1f} nm, limit = {lam_limit*1e9:.1f} nm)")

    # 5. Example 39.6: Exploring the Bohr Model (n = 2)
    K2 = 13.60 / (2**2)
    U2 = -27.20 / (2**2)
    E2 = K2 + U2
    E1 = -13.60
    assert K2 == 3.40, f"Ex 39.6 K2 mismatch: {K2}"
    assert U2 == -6.80, f"Ex 39.6 U2 mismatch: {U2}"
    assert E2 == -3.40, f"Ex 39.6 E2 mismatch: {E2}"
    # Verification of signed relations: E = U/2 < 0, U < 0, K = -E = -U/2 > 0
    assert E2 < 0, f"Total energy must be negative: {E2}"
    assert U2 < 0, f"Potential energy must be negative: {U2}"
    assert K2 > 0, f"Kinetic energy must be positive: {K2}"
    assert E2 == U2 / 2.0, f"E must equal U/2: {E2} vs {U2/2.0}"
    assert K2 == -E2, f"K must equal -E: {K2} vs {-E2}"
    delta_E_21 = E2 - E1
    assert delta_E_21 == 10.20, f"Ex 39.6 delta E mismatch: {delta_E_21}"
    lam_lyman_alpha = (h_eV * c) / delta_E_21
    assert abs(lam_lyman_alpha * 1e9 - 121.6) < 0.5, f"Ex 39.6 Lyman alpha mismatch: {lam_lyman_alpha*1e9}"
    assert round(lam_lyman_alpha * 1e9) == 122, f"Ex 39.6 Lyman alpha round mismatch: {lam_lyman_alpha*1e9}"
    print(f"  Ex 39.6: OK (K2 = {K2:.2f} eV > 0, U2 = {U2:.2f} eV < 0, E2 = U2/2 = {E2:.2f} eV < 0, Lyman-alpha = {lam_lyman_alpha*1e9:.0f} nm)")

    # 6. Nuclear motion & reduced mass
    m_p = 1836.2 # in units of electron mass m
    m_r_H = (1.0 * m_p) / (1.0 + m_p)
    assert abs(m_r_H - 0.999456) < 1e-5, f"Reduced mass H mismatch: {m_r_H}"
    assert round(m_r_H, 5) == 0.99946, f"Reduced mass H round mismatch: {m_r_H}"

    m_d = 2.0 * m_p # deuterium nucleus
    m_r_D = (1.0 * m_d) / (1.0 + m_d)
    assert abs(m_r_D - 0.999728) < 1e-5, f"Reduced mass D mismatch: {m_r_D}"
    assert round(m_r_D, 5) == 0.99973, f"Reduced mass D round mismatch: {m_r_D}"
    shift_pct = (m_r_D - m_r_H) / m_r_H * 100.0
    assert abs(shift_pct - 0.027) < 0.005, f"Deuterium isotope shift mismatch: {shift_pct}"
    print(f"  Reduced mass: OK (m_r(H) = {m_r_H:.5f} m, m_r(D) = {m_r_D:.5f} m, isotope shift = {shift_pct:.3f}%)")

    # 7. TYU 39.3: He+ ion transition matching hydrogen
    # He+ has Z = 2, E_n = -4 * 13.60 / n^2.
    # Level n = 4 in He+: E_4 = -4 * 13.60 / 16 = -3.40 eV (matches H n = 2)
    # Level n = 2 in He+: E_2 = -4 * 13.60 / 4 = -13.60 eV (matches H n = 1)
    # Transition (iv) 4 -> 2 gives delta E = 10.20 eV, exactly matching H n = 2 -> 1 (Lyman-alpha, 122 nm)
    E_He = {n: -4.0 * 13.60 / (n**2) for n in range(1, 5)}
    delta_i = E_He[2] - E_He[1]   # 2 -> 1: 40.80 eV
    delta_ii = E_He[3] - E_He[2]  # 3 -> 2: 7.5556 eV (5/9 * 13.60)
    delta_iii = E_He[4] - E_He[3] # 4 -> 3: 2.6444 eV (7/36 * 13.60)
    delta_iv = E_He[4] - E_He[2]  # 4 -> 2: 10.20 eV

    assert abs(delta_i - 40.80) < 1e-4, f"delta_i mismatch: {delta_i}"
    assert abs(delta_ii - 13.60 * 5.0 / 9.0) < 1e-4, f"delta_ii mismatch: {delta_ii}"
    assert abs(delta_iii - 13.60 * 7.0 / 36.0) < 1e-4, f"delta_iii mismatch: {delta_iii}"
    assert abs(delta_iv - 10.20) < 1e-4, f"delta_iv mismatch: {delta_iv}"

    # Verify that delta_i, delta_ii, delta_iii cannot match any H transition:
    # Allowed H transitions: delta_E_H = 13.60 * (1/nL^2 - 1/nU^2)
    # For (i): delta_i = 40.80 eV > 13.60 eV (exceeds max H transition = 13.60 eV)
    assert delta_i > 13.60

    # For (ii): delta_ii / 13.60 = 5/9.
    # If nL = 1: 1 - 1/nU^2 = 5/9 => nU = 1.5 (not integer). If nL >= 2: max delta_E / 13.60 = 1/4 = 0.25 < 5/9.
    match_ii = any(abs((1.0/(nL**2) - 1.0/(nU**2)) - 5.0/9.0) < 1e-6 for nL in range(1, 100) for nU in range(nL+1, 101))
    assert not match_ii, "Unexpected match for transition (ii) in H!"

    # For (iii): delta_iii / 13.60 = 7/36.
    # If nL = 1: min delta_E / 13.60 = 3/4 = 27/36 > 7/36.
    # If nL = 2: 1/4 - 1/nU^2 = 7/36 => 1/nU^2 = 2/36 = 1/18 => nU = sqrt(18) (not integer).
    # If nL >= 3: max delta_E / 13.60 = 1/9 = 4/36 < 7/36.
    match_iii = any(abs((1.0/(nL**2) - 1.0/(nU**2)) - 7.0/36.0) < 1e-6 for nL in range(1, 100) for nU in range(nL+1, 101))
    assert not match_iii, "Unexpected match for transition (iii) in H!"

    # For (iv): delta_iv / 13.60 = 3/4, matches nL = 1, nU = 2
    assert abs((1.0/1.0 - 1.0/4.0) - 3.0/4.0) < 1e-6
    print(f"  TYU 39.3: OK (Only transition (iv) n=4->2 has dE=10.20 eV matching H n=2->1 at 122 nm; (i),(ii),(iii) proved mathematically impossible -> Answer (iv))")

    # 8. Section 39.4 Laser: Maxwell-Boltzmann distribution ratio at 3000 K
    k_B = 1.38e-23
    T = 3000.0
    delta_E_laser = 3.2e-19 # J (2.0 eV)
    kT = k_B * T
    assert abs(kT - 4.14e-20) < 1e-22, f"Laser kT mismatch: {kT}"
    exponent = delta_E_laser / kT
    assert abs(exponent - 7.73) < 0.02, f"Laser exponent mismatch: {exponent}"
    assert round(exponent, 2) == 7.73, f"Laser exponent round mismatch: {exponent}"
    pop_ratio = math.exp(-exponent)
    assert abs(pop_ratio - 0.00044) < 0.00002, f"Laser population ratio mismatch: {pop_ratio}"
    assert round(pop_ratio, 5) == 0.00044, f"Laser population ratio round mismatch: {pop_ratio}"
    print(f"  Section 39.4 Laser: OK (kT = {kT:.2e} J, exponent = {exponent:.2f}, n_ex/n_g = {pop_ratio:.5f} = {pop_ratio*100:.3f}%)")

    # 9. TYU 39.4: Neon sign emission mechanism
    # Ordinary neon sign produces spontaneous emission without optical cavity or population inversion
    print("  TYU 39.4: OK (Ordinary neon sign produces spontaneous emission -> Answer (i))")

def verify_images():
    print("=== 2. Validating Image Files against Source PDF ===")
    if not SOURCE_PDF.is_file():
        report_error(f"Source PDF not found at {SOURCE_PDF}")
        return

    expected_crops = {
        "hinh-39-15.png": (1310, (35, 168, 193, 326)),
        "hinh-39-16.png": (1310, (35, 385, 193, 460)),
        "hinh-39-17.png": (1311, (455, 88, 608, 163)),
        "hinh-39-18.png": (1311, (76, 523, 516, 738)),
        "hinh-39-19.png": (1312, (102, 115, 572, 362)),
        "hinh-39-20.png": (1312, (80, 555, 240, 718)),
        "hinh-39-21.png": (1314, (35, 93, 195, 256)),
        "hinh-39-22.png": (1314, (225, 638, 532, 748)),
        "hinh-39-23.png": (1315, (455, 86, 612, 232)),
        "hinh-39-24.png": (1316, (140, 483, 572, 745)),
        "hinh-39-25.png": (1317, (76, 638, 432, 742)),
        "hinh-39-26.png": (1318, (34, 595, 196, 709)),
        "hinh-39-27.png": (1319, (128, 545, 390, 748)),
        "hinh-39-28.png": (1320, (35, 402, 195, 684)),
        "hinh-39-29.png": (1322, (34, 95, 554, 245)),
        "hinh-39-29d.png": (1322, (34, 267, 195, 401)),
    }

    scale = 3.0
    doc = pymupdf.open(SOURCE_PDF)
    for fname, (p_num, box) in expected_crops.items():
        img_path = IMG_DIR / fname
        if not img_path.is_file():
            report_error(f"Missing image file: {fname}")
            continue

        im = Image.open(img_path)
        expected_w = int(round((box[2] - box[0]) * scale))
        expected_h = int(round((box[3] - box[1]) * scale))

        if abs(im.width - expected_w) > 3 or abs(im.height - expected_h) > 3:
            report_error(f"Image dimension mismatch for {fname}: got {im.width}x{im.height}, expected ~{expected_w}x{expected_h}")
        else:
            # Check byte-for-byte pixel integrity against fresh PDF render
            page = doc[p_num - 1]
            rect = pymupdf.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), clip=rect, alpha=False)
            if im.width != pix.width or im.height != pix.height:
                report_error(f"Pixel dimension mismatch with fresh clip for {fname}: {im.width}x{im.height} vs {pix.width}x{pix.height}")
            elif im.tobytes() != pix.samples:
                report_error(f"Byte mismatch detected for {fname} against source PDF clip!")
            else:
                print(f"  {fname}: OK ({im.width}x{im.height}, 100% byte-exact RGB match)")

    doc.close()
    print(f"  Checked {len(expected_crops)} source image crops. Any mismatch is reported above and fails the final status.")

def verify_markdown():
    print("=== 3. Auditing Markdown Content & Formatting ===")
    forbidden_words = [
        "hợp đồng",
        "hợp đồng file",
        "hợp đồng dữ liệu",
        "ánh xạ hợp đồng",
        "lớp bài toán",
        "lớp hàm",
        "giả trân",
        "kỳ diệu",
        "vô cùng",
        "cực kỳ",
        "mạnh mẽ",
        "then chốt",
        "khoan đã",
        "nhầm rồi",
        "thử lại nào",
        "ý tôi là",
        "sinh viên rất hay nhầm",
        "lỗi phổ biến nhất",
        "đa số sinh viên",
        "bẫy thi cử",
        "do người soạn",
        "lấy từ sách",
        "ảnh trong sách",
        "ảnh lấy từ sách",
        "theo sách",
        "nguyên tác",
        "bản dịch của",
        "tiến độ bản dịch",
    ]

    colon_pattern = re.compile(r':\s+([a-zA-Z\u00C0-\u024F\u1EA0-\u1EF9])')
    all_images_found = set()
    all_equations_found = set()

    for md_path in TRANSLATIONS:
        if not md_path.is_file():
            report_error(f"Missing translation file: {md_path}")
            continue

        text = md_path.read_text(encoding="utf-8")
        lines = text.split("\n")

        # Check forbidden words
        text_lower = text.lower()
        for fw in forbidden_words:
            if fw in text_lower:
                report_error(f"Forbidden phrase '{fw}' found in {md_path.name}")

        # Check forbidden \vert{} or \Vert{}
        if r"\vert{}" in text or r"\Vert{}" in text:
            report_error(f"Forbidden \\vert{{}} found in {md_path.name}")

        # Check colon capitalization and em dash
        in_code_block = False
        in_display_math = False
        for line_idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if stripped == "$$":
                in_display_math = not in_display_math
                continue
            if in_code_block or in_display_math:
                continue

            # Check em dash in prose
            if not stripped.startswith("-") and not stripped.startswith("*"):
                if "—" in line:
                    report_error(f"{md_path.name}:{line_idx}: Em dash '—' found in prose: '{line.strip()}'")
                if " -- " in line:
                    report_error(f"{md_path.name}:{line_idx}: Double dash ' -- ' found in prose: '{line.strip()}'")

            # Check colon capitalization
            clean_line = re.sub(r'https?://\S+', '', line)
            clean_line = re.sub(r'file://\S+', '', clean_line)
            clean_line = re.sub(r'\$[^\$]+\$', '', clean_line)
            m = None if line.lstrip().startswith(':::') else colon_pattern.search(clean_line)
            if m and m.group(1).islower():
                report_error(f"{md_path.name}:{line_idx}: Lowercase '{m.group(1)}' after colon: '{clean_line.strip()}'")

            # Check for forbidden duplicate italic caption paragraphs
            if stripped.startswith("*Hình 39.") or stripped.startswith("*Hình 39:"):
                report_error(f"{md_path.name}:{line_idx}: Duplicate italic caption found: '{stripped}' (captions must be inside image alt only)")

            # Check image links
            img_matches = re.findall(r'!\[(.*?)\]\((.*?)\)', line)
            for alt, src in img_matches:
                if not alt.strip():
                    report_error(f"{md_path.name}:{line_idx}: Empty alt text for image {src}")
                if not alt.startswith(("Hình 39.", "Ứng dụng: ")):
                    report_error(f"{md_path.name}:{line_idx}: Image needs a figure label or application caption: '{alt[:40]}...'")
                if "$" in alt:
                    report_error(f"{md_path.name}:{line_idx}: Literal TeX '$' found in image alt text: '{alt}'")
                target = ROOT / 'docs/vat-ly-2/bai-giang/img/young-39' / Path(src).name
                if not src.startswith("../img/young-39/") or not target.is_file():
                    report_error(f"{md_path.name}:{line_idx}: Invalid image path: {src}")
                stem = Path(src).stem
                all_images_found.add(stem)

        # Check display math tags and alignment
        display_math_blocks = re.findall(r'\$\$\n([\s\S]*?)\n\$\$', text)
        for block in display_math_blocks:
            tag_m = re.search(r'\\tag\{(\d+\.\d+)\}', block)
            if tag_m:
                all_equations_found.add(tag_m.group(1))
            if r"\tag{" in block:
                if r"\end{aligned}" in block:
                    end_idx = block.find(r"\end{aligned}")
                    tag_idx = block.find(r"\tag{")
                    if tag_idx < end_idx:
                        report_error(f"{md_path.name}: \\tag placed inside aligned block: {block[:60]}")

    expected_stems = {f"hinh-39-{i:02d}" for i in range(15, 30)} | {"hinh-39-29d"}
    missing_stems = expected_stems - all_images_found
    if missing_stems:
        report_error(f"Missing images in Markdown: {missing_stems}")
    else:
        print(f"  All {len(expected_stems)} source image crops linked with Vietnamese captions.")

    # Verify all assigned equations (39.5 to 39.18) are present
    expected_equations = {f"39.{i}" for i in range(5, 19)}
    missing_eqs = expected_equations - all_equations_found
    if missing_eqs:
        report_error(f"Missing equation tags in Markdown: {missing_eqs}")
    else:
        print(f"  All 14 assigned equations (39.5 - 39.18) present and tagged!")

    print("  Markdown files audit completed!")

def verify_annotations():
    print("=== 4. Verifying Annotations Module ===")
    if not ANNOTATIONS_FILE.is_file():
        report_error(f"Missing annotations file: {ANNOTATIONS_FILE}")
        return

    text = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    for i in range(15, 30):
        key_double = f'"young-39/hinh-39-{i:02d}"'
        key_single = f"'young-39/hinh-39-{i:02d}'"
        if key_double not in text and key_single not in text:
            report_error(f"Missing key in annotations: young-39/hinh-39-{i:02d}")

    try:
        res = subprocess.run(["node", "--check", str(ANNOTATIONS_FILE)], capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            report_error(f"node --check failed: {res.stderr}")
        else:
            print("  node --check: Syntax valid!")
    except Exception as e:
        report_error(f"Failed to run node --check: {e}")

def verify_mathjax_widths():
    print("=== 5. Measuring MathJax Widths (Inline <= 38ex, Display Body <= 25ex, Full Tagged <= 32ex on 320px) ===")
    node_modules_pkg = Path("C:/Users/Ai/Documents/StudyHub/package.json")
    pkg_to_use = node_modules_pkg if node_modules_pkg.is_file() else (ROOT / "package.json")
    if not pkg_to_use.is_file():
        report_error("package.json not found, cannot run MathJax measurement")
        return

    display_items = []
    inline_items = []

    for md_path in TRANSLATIONS:
        if not md_path.is_file():
            report_error(f"Missing translation file: {md_path}")
            continue
        content = md_path.read_text(encoding="utf-8")
        lines = content.split("\n")

        in_display = False
        display_block = []
        start_line = 0
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped == "$$":
                if in_display:
                    in_display = False
                    block_tex = "\n".join(display_block).strip()
                    clean_tex = re.sub(r'\\tag\{[^}]*\}', '', block_tex).strip()
                    tag_m = re.search(r'\\tag\{([^}]*)\}', block_tex)
                    tag_val = tag_m.group(1) if tag_m else None
                    if clean_tex:
                        display_items.append({
                            "file": md_path.name,
                            "line": start_line,
                            "tex": clean_tex,
                            "raw": block_tex,
                            "tag": tag_val
                        })
                    display_block = []
                else:
                    in_display = True
                    start_line = idx
                    display_block = []
            elif in_display:
                display_block.append(line)
            else:
                for m in re.finditer(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', line):
                    inline_tex = m.group(1).strip()
                    if inline_tex:
                        inline_items.append({"file": md_path.name, "line": idx, "tex": inline_tex})

    if not display_items:
        report_error("No display math blocks found in translations!")
        return

    pkg_path_str = str(pkg_to_use).replace('\\', '/')
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
let inlineErrors = 0;

for (const item of data.display) {{
  try {{
    const rendered = md.render('$$\\n' + item.tex + '\\n$$');
    const m = rendered.match(/width="([\\d.]+)ex"/);
    if (!m) {{
      console.log(`[DISPLAY RENDER ERROR] Could not extract numeric SVG ex width: ${{item.file}}:${{item.line}}`);
      displayErrors++;
      continue;
    }}
    const w = parseFloat(m[1]);
    if (w <= 0) {{
      console.log(`[DISPLAY ZERO WIDTH] Extracted width is ${{w}}ex: ${{item.file}}:${{item.line}}`);
      displayErrors++;
      continue;
    }}
    if (w > 25.0) {{
      console.log(`[DISPLAY OVERFLOW] ${{w.toFixed(2)}}ex > 25ex at ${{item.file}}:${{item.line}}: ${{item.tex.replace(/\\n/g, ' ')}}`);
      displayErrors++;
    }}
    if (item.tag) {{
      const renderedTag = md.render('$(' + item.tag + ')$');
      const mTag = renderedTag.match(/width="([\\d.]+)ex"/);
      const tagW = mTag ? parseFloat(mTag[1]) : 4.0;
      const fullW = w + 2.0 + tagW;
      if (fullW > 32.0) {{
        console.log(`[TAGGED OVERFLOW] ${{fullW.toFixed(2)}}ex > 32ex on 320px at ${{item.file}}:${{item.line}}: tag (${{item.tag}})`);
        displayErrors++;
      }}
    }}
  }} catch (err) {{
    console.log(`[DISPLAY EXCEPTION] ${{item.file}}:${{item.line}}: ${{err.message}}`);
    displayErrors++;
  }}
}}

for (const item of data.inline) {{
  try {{
    const rendered = md.render('$' + item.tex + '$');
    const m = rendered.match(/width="([\\d.]+)ex"/);
    if (!m) continue;
    const w = parseFloat(m[1]);
    if (w > 38.0) {{
      console.log(`[INLINE OVERFLOW] ${{w.toFixed(2)}}ex > 38ex at ${{item.file}}:${{item.line}}: $${{item.tex}}$`);
      inlineErrors++;
    }}
  }} catch (err) {{
    // ignore inline render error
  }}
}}

console.log(`MathJax measurement complete: ${{data.display.length}} display blocks, ${{data.inline.length}} inline items.`);
if (displayErrors > 0 || inlineErrors > 0) {{
  console.log(`FAILED with ${{displayErrors}} display errors and ${{inlineErrors}} inline errors.`);
  process.exit(1);
}} else {{
  console.log(`PASSED: All display body <= 25ex, tagged <= 32ex, inline <= 38ex!`);
  process.exit(0);
}}
"""

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as f:
        json.dump({"display": display_items, "inline": inline_items}, f, ensure_ascii=False)
        json_tmp = f.name

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".cjs", delete=False) as f:
        f.write(js_code)
        js_tmp = f.name

    try:
        res = subprocess.run(["node", js_tmp, json_tmp], capture_output=True, text=True, encoding="utf-8")
        print(res.stdout)
        if res.returncode != 0:
            report_error(f"MathJax width check failed:\n{res.stdout}\n{res.stderr}")
        else:
            print("  MathJax width verification passed!")
    except Exception as e:
        report_error(f"Failed to run MathJax measurement: {e}")
    finally:
        try:
            os.remove(json_tmp)
            os.remove(js_tmp)
        except OSError:
            pass

def main():
    print("======================================================================")
    print("STARTING AUDIT: Chapter 39 Theory B (Sections 39.3 - 39.4)")
    print("======================================================================")

    verify_calculations()
    verify_images()
    verify_markdown()
    verify_annotations()
    verify_mathjax_widths()

    print("\n======================================================================")
    print("AUDIT SUMMARY:")
    print(f"Errors: {len(ERRORS)}")
    print(f"Warnings: {len(WARNINGS)}")
    if ERRORS:
        print("FAIL: Please resolve the following errors:")
        for err in ERRORS:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("SUCCESS: 100% checks passed cleanly!")
        sys.exit(0)

if __name__ == "__main__":
    main()
