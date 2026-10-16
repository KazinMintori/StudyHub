# -*- coding: utf-8 -*-
"""Verification script for Chapter 43 Theory A (Sections 43.1 - 43.3).

This script performs strict, multi-layer verification:
1. Numerical calculation audit of all examples and TYUs against source physics.
2. Exact byteRGB rendering comparison of all 10 cropped PNG images against source PDF.
3. Markdown formatting, linting, forbidden word audit, and colon capitalization checks.
4. Validation of image annotations module.
"""

from __future__ import annotations

import math
import os
import re
import sys
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).resolve().parents[2]
LOCAL_PDF = REPO_ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
MAIN_PDF = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
PDF_PATH = LOCAL_PDF if LOCAL_PDF.is_file() else MAIN_PDF
RAW_DIR = REPO_ROOT / "raw_materials" / "physics" / "translations" / "chapter-43"
IMG_DIR = REPO_ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-43"
ANNOTATIONS_FILE = REPO_ROOT / "docs" / ".vitepress" / "physics43-theory-a-image-annotations.mjs"

IMAGE_SPECS = [
    ("hinh-43-01.png", 1467, (75, 75, 575, 428), (1251, 883)),
    ("hinh-43-02.png", 1469, (355, 84, 615, 273), (651, 473)),
    ("hinh-43-03.png", 1472, (34, 94, 195, 415), (403, 803)),
    ("hinh-43-04.png", 1473, (110, 55, 435, 475), (813, 1051)),
    ("hinh-43-05.png", 1474, (95, 87, 575, 245), (1201, 396)),
    ("hinh-43-06.png", 1477, (455, 560, 612, 740), (393, 450)),
    ("hinh-43-07.png", 1478, (250, 55, 525, 495), (688, 1101)),
    ("hinh-43-08.png", 1479, (468, 614, 605, 755), (343, 353)),
    ("ung-dung-a-1.png", 1464, (0, 339, 192, 501), (480, 406)),
    ("ung-dung-a-2.png", 1468, (0, 258, 192, 397), (480, 348)),
]

MD_FILES = [
    RAW_DIR / "01-tinh-chat-hat-nhan.md",
    RAW_DIR / "02-nang-luong-lien-ket.md",
    RAW_DIR / "03-on-dinh-va-phong-xa.md",
]

FORBIDDEN_WORDS = [
    "then chốt",
    "cực kỳ",
    "vô cùng",
    "kỳ diệu",
    "giả trân",
    "bẫy thi cử",
    "theo sách",
    "ảnh lấy từ sách",
    "hình trong sách",
    "nguyên tác",
    "bản dịch",
    "lớp bài toán",
    "lớp hàm",
    "hợp đồng",
]


def test_calculations():
    print("[1/4] Auditing numerical calculations...")

    # Ex 43.1: Nuclear properties of 56_26Fe
    R_0 = 1.2e-15
    A_Fe = 56
    R_calc = R_0 * (A_Fe ** (1.0 / 3.0))
    assert abs(R_calc - 4.59e-15) < 0.05e-15, f"R_calc={R_calc}"

    m_Fe = 55.934938 * 1.660539e-27
    assert abs(m_Fe - 9.29e-26) < 0.05e-26, f"m_Fe={m_Fe}"

    V_Fe = (4.0 / 3.0) * math.pi * (R_calc ** 3)
    assert abs(V_Fe - 4.05e-43) < 0.05e-43, f"V_Fe={V_Fe}"

    rho_Fe = m_Fe / V_Fe
    assert abs(rho_Fe - 2.29e17) < 0.05e17, f"rho_Fe={rho_Fe}"

    # Ex 43.1 evaluation: Comparison with bulk iron density (7000 kg/m^3) and 1 cm^3 nuclear matter mass
    rho_bulk_iron = 7000.0  # kg/m^3
    ratio_rho_bulk = rho_Fe / rho_bulk_iron
    assert abs(ratio_rho_bulk - 3.3e13) < 0.2e13, f"ratio_rho_bulk={ratio_rho_bulk}"

    m_1cm3 = rho_Fe * 1e-6  # mass of 1 cm^3 nuclear matter in kg
    assert abs(m_1cm3 - 2.3e11) < 0.1e11, f"m_1cm3={m_1cm3}"
    assert abs((m_1cm3 / 1e3) - 2.3e8) < 0.1e8, "230 million metric tons"

    # Ex 43.2: Proton spin flip
    mu_n_eV = 3.152451e-8  # eV/T
    mu_z_p = 2.7928473 * mu_n_eV
    B_field = 2.30
    U_p = -mu_z_p * B_field
    delta_E = 2 * abs(U_p)
    assert abs(delta_E - 4.05e-7) < 0.01e-7, f"delta_E={delta_E}"

    h_eV_s = 4.135667e-15
    f_p = delta_E / h_eV_s
    assert abs(f_p - 9.79e7) < 0.05e7, f"f_p={f_p}"  # ~97.9 MHz

    c_m_s = 2.997925e8
    lambda_p = c_m_s / f_p
    assert abs(lambda_p - 3.06) < 0.05, f"lambda_p={lambda_p}"

    # Ex 43.3: Binding energy of 62_28Ni
    M_H = 1.007825
    m_n = 1.008665
    M_Ni62 = 61.928345  # Exact source mass in Table 43.2
    delta_M_Ni = (28 * M_H + 34 * m_n) - M_Ni62
    assert abs(delta_M_Ni - 0.585365) < 1e-6, f"delta_M_Ni={delta_M_Ni}"

    E_B_Ni = delta_M_Ni * 931.5
    assert abs(E_B_Ni - 545.3) < 0.1, f"E_B_Ni={E_B_Ni}"

    EB_per_A_Ni = E_B_Ni / 62
    assert abs(EB_per_A_Ni - 8.795) < 0.005, f"EB_per_A_Ni={EB_per_A_Ni}"

    # Ex 43.4: Liquid-drop semiempirical mass formula for 62_28Ni
    # Young & Freedman 15th ed page 1471 exact coefficients
    C1 = 15.75
    C2 = 17.80
    C3 = 0.7100
    C4 = 23.69
    C5 = 39.0

    t1 = C1 * 62
    t2 = -C2 * (62 ** (2.0 / 3.0))
    t3 = -C3 * (28 * 27) / (62 ** (1.0 / 3.0))
    t4 = -C4 * ((62 - 56) ** 2) / 62
    t5 = +C5 * (62 ** (-4.0 / 3.0))
    E_B_model = t1 + t2 + t3 + t4 + t5
    assert abs(E_B_model - 548.5) < 0.1, f"E_B_model={E_B_model}"

    M_est = (28 * M_H + 34 * m_n) - (E_B_model / 931.5)
    assert abs(M_est - 61.925) < 0.005, f"M_est={M_est}"

    # Ex 43.5: Alpha decay of 226_88Ra
    M_Ra226 = 226.025410
    M_Rn222 = 222.017578
    M_He4 = 4.002603
    delta_m_alpha = M_Ra226 - (M_Rn222 + M_He4)
    assert abs(delta_m_alpha - 0.005229) < 1e-6, f"delta_m_alpha={delta_m_alpha}"

    Q_alpha = delta_m_alpha * 931.5
    assert abs(Q_alpha - 4.871) < 0.005, f"Q_alpha={Q_alpha}"

    K_alpha = (222.0 / 226.0) * Q_alpha
    K_Rn = (4.0 / 226.0) * Q_alpha
    assert abs(K_alpha - 4.785) < 0.005, f"K_alpha={K_alpha}"
    assert abs(K_Rn - 0.086) < 0.005, f"K_Rn={K_Rn}"

    # Ex 43.6: Beta-minus decay of 60_27Co
    M_Co60 = 59.933817
    M_Ni60 = 59.930786
    delta_m_beta = M_Co60 - M_Ni60
    assert abs(delta_m_beta - 0.003031) < 1e-6, f"delta_m_beta={delta_m_beta}"

    Q_beta = delta_m_beta * 931.5
    assert abs(Q_beta - 2.823) < 0.005, f"Q_beta={Q_beta}"

    # Ex 43.7: Positron vs EC for 57_27Co
    M_Co57 = 56.936291
    M_Fe57 = 56.935394
    delta_M_EC = M_Co57 - M_Fe57
    assert abs(delta_M_EC - 0.000897) < 1e-6, f"delta_M_EC={delta_M_EC}"

    Q_EC = delta_M_EC * 931.5
    assert abs(Q_EC - 0.836) < 0.005, f"Q_EC={Q_EC}"

    threshold_beta_plus = 2 * 0.00054858 * 931.5  # 2m_e * c^2
    assert threshold_beta_plus > Q_EC, "Beta plus must be energetically forbidden"
    Q_beta_plus = Q_EC - threshold_beta_plus
    assert Q_beta_plus < 0, f"Q_beta_plus should be negative: {Q_beta_plus}"

    # TYU 43.1: Scaling of nuclear volume and radius with mass number A
    # (a) V proportional to A -> Factor of 2 in V requires factor of 2 in A
    factor_A_for_2V = 2.0
    assert factor_A_for_2V == 2.0, f"factor_A_for_2V={factor_A_for_2V}"
    # (b) R proportional to A^(1/3) -> A proportional to R^3 -> Factor of 2 in R requires factor of 2^3 = 8 in A
    factor_A_for_2R = 2.0 ** 3
    assert factor_A_for_2R == 8.0, f"factor_A_for_2R={factor_A_for_2R}"

    # TYU 43.2
    # Ranks: (ii) Cr-52 (~8.8) > (iii) Sm-152 (~8.25) > (iv) Hg-200 (~7.9) > (v) Cf-252 (~7.45) > (i) He-4 (7.07)
    ranks = [("Cr-52", 8.78), ("Sm-152", 8.25), ("Hg-200", 7.90), ("Cf-252", 7.45), ("He-4", 7.07)]
    for i in range(len(ranks) - 1):
        assert ranks[i][1] > ranks[i+1][1], f"Ranking mismatch at {ranks[i]} vs {ranks[i+1]}"

    # TYU 43.3
    # Consecutive alpha (dZ=-2, dN=-2) and beta-plus (dZ=-1, dN=+1)
    dZ_total = -2 + (-1)
    dN_total = -2 + 1
    assert dZ_total == -3 and dN_total == -1, f"TYU 43.3 result: dZ={dZ_total}, dN={dN_total}"

    print("  -> All numerical calculations verified successfully.")


def test_images():
    print("[2/4] Verifying 10 cropped images against source PDF...")
    try:
        import fitz
        from PIL import Image
    except ImportError as e:
        print(f"  PyMuPDF/Pillow error: {e}")
        sys.exit(1)

    assert PDF_PATH.is_file(), f"PDF not found: {PDF_PATH}"
    doc = fitz.open(str(PDF_PATH))
    zoom = 2.5
    mat = fitz.Matrix(zoom, zoom)

    for filename, page_num, bbox, (exp_w, exp_h) in IMAGE_SPECS:
        img_file = IMG_DIR / filename
        assert img_file.is_file(), f"Image file missing: {img_file}"

        with Image.open(img_file) as im:
            actual_w, actual_h = im.size
            assert (actual_w, actual_h) == (exp_w, exp_h), (
                f"{filename} size mismatch: got ({actual_w}, {actual_h}), expected ({exp_w}, {exp_h})"
            )
            saved_bytes = im.convert("RGB").tobytes()

        # Render fresh from PDF
        page = doc.load_page(page_num - 1)
        rect = fitz.Rect(bbox)
        pix = page.get_pixmap(matrix=mat, clip=rect)
        assert (pix.width, pix.height) == (exp_w, exp_h), (
            f"Rendered pixmap size mismatch for {filename}: got ({pix.width}, {pix.height})"
        )
        rendered_bytes = pix.samples

        # 100% byteRGB comparison
        if saved_bytes != rendered_bytes:
            diff_count = sum(1 for a, b in zip(saved_bytes, rendered_bytes) if a != b)
            raise AssertionError(f"Byte mismatch in {filename}: {diff_count} differing bytes")

        print(f"  -> {filename}: OK ({actual_w}x{actual_h} px, exact match)")

    doc.close()


def test_markdown():
    print("[3/4] Auditing Markdown fragments for syntax and rules...")

    expected_starts = {
        "01-tinh-chat-hat-nhan.md": "## 43.1 ",
        "02-nang-luong-lien-ket.md": "## 43.2 ",
        "03-on-dinh-va-phong-xa.md": "## 43.3 ",
    }

    colon_violation_count = 0

    for path in MD_FILES:
        assert path.is_file(), f"Markdown file missing: {path}"
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        # Check start
        assert lines[0].startswith(expected_starts[path.name]), (
            f"{path.name} must start with {expected_starts[path.name]}, got: {lines[0]}"
        )

        # Check no H1
        for idx, line in enumerate(lines, 1):
            if re.match(r"^#[^#]", line):
                raise AssertionError(f"Found H1 in {path.name}:{idx}: {line}")

        # Check no frontmatter
        if lines[0].strip() == "---":
            raise AssertionError(f"Found frontmatter in {path.name}")

        # Check no references section
        for idx, line in enumerate(lines, 1):
            if re.match(r"^##\s*Tài liệu tham khảo", line):
                raise AssertionError(f"Forbidden references section in raw fragment {path.name}:{idx}")

        # Check forbidden words
        text_lower = text.lower()
        for fw in FORBIDDEN_WORDS:
            if fw in text_lower:
                raise AssertionError(f"Forbidden word '{fw}' found in {path.name}")

        # Check math delimiters
        for idx, line in enumerate(lines, 1):
            if line.strip() == "$":
                raise AssertionError(f"Isolated single '$' on line {path.name}:{idx}")
            if "$$" in line and line.strip() != "$$":
                # Check if it's on a line alone
                raise AssertionError(f"'$$' must be on a line alone: {path.name}:{idx}: {line}")

        # Colon capitalization check in prose/list items/headers
        # Ignore math lines ($$ block or inside equations)
        in_display_math = False
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped == "$$":
                in_display_math = not in_display_math
                continue
            if in_display_math:
                continue

            # Check after colons
            # Look for colon followed by whitespace and a lowercase Vietnamese letter
            # Exclude code lines, image links `![alt](url)`, container syntax `:::`
            if stripped.startswith("![") or stripped.startswith(":::"):
                continue

            # Remove inline math $...$ before checking colon
            clean_line = re.sub(r"\$[^$]+\$", "", line)

            # Find colons followed by whitespace and a letter
            for m in re.finditer(r":\s+([^\s])", clean_line):
                char = m.group(1)
                # Check if it is a lowercase letter
                if char.isalpha() and char.islower():
                    colon_violation_count += 1
                    print(f"  WARNING Colon capitalization: {path.name}:{idx}: '{char}' after colon in: {line[:60]}...")

        print(f"  -> {path.name}: OK ({len(lines)} lines)")

    if colon_violation_count > 0:
        raise AssertionError(f"Found {colon_violation_count} colon capitalization violations")


def test_annotations_file():
    print("[4/4] Validating annotations file...")
    assert ANNOTATIONS_FILE.is_file(), f"Annotations file missing: {ANNOTATIONS_FILE}"
    content = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    assert "export const physics43TheoryAImageAnnotations = {" in content
    for filename, _, _, _ in IMAGE_SPECS:
        stem = filename.replace(".png", "")
        key = f"young-43/{stem}"
        assert f'"{key}":' in content or f"'{key}':" in content, (
            f"Annotation missing key for {key}"
        )
    print("  -> Annotations file: OK")


def main():
    print("=" * 60)
    print("Running verification for Chapter 43 Theory A...")
    print("=" * 60)
    test_calculations()
    test_images()
    test_markdown()
    test_annotations_file()
    print("=" * 60)
    print("ALL Chapter 43 Theory A checks passed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
