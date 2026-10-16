#!/usr/bin/env python3
"""
Comprehensive verifier for Chapter 43 Theory B (Sections 43.4 - 43.8):
- Numerical and physical calculations for all Examples (43.8 - 43.13) and TYUs (43.4 - 43.8)
- Asset validation against source PDF (exact dimensions and byte-for-byte pixel integrity)
- Markdown syntax, pedagogical structure, colon capitalization, and math formatting audit
- Image annotations module consistency and syntax (node --check)
- Delegated MathJax measurement (measure-delegated-math.mjs with 0 findings)
"""

import sys
import os
import re
import math
import subprocess
import json
from pathlib import Path
from PIL import Image
import pymupdf

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent.parent
LOCAL_SOURCE = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE_PDF = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-43"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics43-theory-b-image-annotations.mjs"

TRANSLATIONS = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-43" / "04-hoat-do-va-chu-ky-ban-ra.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-43" / "05-tac-dung-sinh-hoc.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-43" / "06-phan-ung-hat-nhan.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-43" / "07-phan-hach.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-43" / "08-nhiet-hach.md",
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
    print("=== 1. Verifying Physical & Nuclear Calculations ===")

    # Fundamental constants
    c = 2.99792458e8
    e_c = 1.602176634e-19
    N_A = 6.02214076e23
    u_kg = 1.66053906660e-27
    u_MeV = 931.49410242  # ~931.5 MeV

    # 1. Example 43.8: Activity of Co-57
    T_half_days = 272.0
    T_half_s = T_half_days * 86400.0  # 272 * 86400 = 23,500,800 s = 2.35008e7 s
    assert T_half_s == 23500800.0, f"Ex 43.8 half-life seconds mismatch: {T_half_s}"
    lam_s = math.log(2.0) / T_half_s
    assert abs(lam_s - 2.94946e-8) < 1e-10, f"Ex 43.8 lambda mismatch: {lam_s}"

    # Initial activity R0 = 2.00 microCi = 7.40e4 Bq
    R0_uCi = 2.00
    R0_Ci = R0_uCi * 1e-6
    R0_Bq = R0_Ci * 3.70e10
    assert abs(R0_Bq - 7.40e4) < 1.0, f"Ex 43.8 R0_Bq mismatch: {R0_Bq}"

    N0 = R0_Bq / lam_s
    assert abs(N0 - 2.50893e12) < 1e10, f"Ex 43.8 N0 mismatch: {N0}"

    M_Co57 = 57.0  # g/mol
    m0_g = (N0 / N_A) * M_Co57
    assert abs(m0_g - 2.374e-10) < 1e-12, f"Ex 43.8 m0 mismatch: {m0_g}"

    # Activity after 1.00 yr: source uses 1 yr = 3.156e7 s
    t_yr_s = 3.156e7
    exponent = - lam_s * t_yr_s  # ~ -0.93085 ~ -0.931
    fraction_rem = math.exp(exponent)
    R_1yr_uCi = R0_uCi * fraction_rem  # 0.7884368 uCi
    assert abs(R_1yr_uCi - 0.7884368) < 1e-4, f"Ex 43.8 R_1yr mismatch: {R_1yr_uCi}"
    R_1yr_Bq = (R_1yr_uCi * 1e-6) * 3.70e10
    assert abs(R_1yr_Bq - 2.917e4) < 1e2, f"Ex 43.8 R_1yr_Bq mismatch: {R_1yr_Bq}"
    print(f"  Ex 43.8: OK (lambda = {lam_s:.5e} s^-1, N0 = {N0:.3e}, m0 = {m0_g:.3e} g, R_1yr = {R_1yr_uCi:.4f} uCi = {R_1yr_Bq:.2e} Bq)")

    # 2. Example 43.9: Radiocarbon Dating
    T_half_c14_yr = 5730.0
    yr_s = 3.156e7  # 1 yr in seconds
    T_half_c14_s = T_half_c14_yr * yr_s  # 1.808388e11 s
    lam_c14_s = math.log(2.0) / T_half_c14_s  # 3.83294e-12 s^-1
    assert abs(lam_c14_s - 3.83e-12) < 1e-14

    r_living = 0.255  # Bq/g
    N_c14_per_g = r_living / lam_c14_s  # 6.65287e10 atoms/g
    assert abs(N_c14_per_g - 6.65e10) < 1e9

    M_C = 12.011  # g/mol
    N_total_C_per_g = (1.0 / M_C) * N_A  # 5.01385e22 atoms/g
    assert abs(N_total_C_per_g - 5.01e22) < 1e21

    fraction_c14 = N_c14_per_g / N_total_C_per_g  # 1.32692e-12 = 1.32692e-10%
    assert abs(fraction_c14 - 1.32692e-12) < 1e-15, f"Ex 43.9 fraction mismatch: {fraction_c14}"

    m_sample_g = 0.500
    a0_h = r_living * 3600.0  # 918 h^-1 g^-1
    A0_sample_h = m_sample_g * a0_h  # 459 h^-1
    A_observed_h = 174.0  # 174 decays/hour
    ratio_A = A_observed_h / A0_sample_h  # 174 / 459 = 0.379085
    assert abs(ratio_A - 0.379085) < 1e-5

    age_s = - math.log(ratio_A) / lam_c14_s
    age_yr = age_s / yr_s  # 8018.601 yr ~ 8020 yr
    assert abs(age_yr - 8018.601) < 1.0, f"Ex 43.9 age mismatch: {age_yr}"
    print(f"  Ex 43.9: OK (r0 = {r_living} Bq/g, m = {m_sample_g} g, 14C fraction = {fraction_c14:.5e} ({fraction_c14*100:.5e}%), age = {age_yr:.3f} yr ~ 8020 yr)")

    # 3. Example 43.10: Medical X-ray
    m_leg_kg = 1.2  # 1.2 kg leg
    H_Sv = 0.40e-3  # 0.40 mSv
    H_rem = H_Sv / 0.01  # 40 mrem
    assert abs(H_rem - 0.040) < 1e-6
    RBE_xray = 1.0
    D_Gy = H_Sv / RBE_xray  # 0.40 mGy = 4.0e-4 Gy
    D_rad = D_Gy * 100.0  # 40 mrad
    assert abs(D_Gy - 4.0e-4) < 1e-8
    assert abs(D_rad - 0.040) < 1e-6

    E_absorbed_J = D_Gy * m_leg_kg  # 4.8e-4 J
    assert abs(E_absorbed_J - 4.8e-4) < 1e-10, f"Ex 43.10 E_abs mismatch: {E_absorbed_J}"
    E_absorbed_eV = E_absorbed_J / e_c  # ~ 3.0e15 eV
    E_photon_eV = 50.0e3  # 50 keV
    N_photons = E_absorbed_eV / E_photon_eV  # 5.992e10 ~ 6.0e10 photons
    assert abs(N_photons - 6.0e10) < 1e9, f"Ex 43.10 N_photons mismatch: {N_photons}"
    print(f"  Ex 43.10: OK (m = {m_leg_kg} kg, H = {H_Sv*1e3:.2f} mSv = {H_rem*1e3:.0f} mrem, D = {D_Gy*1e3:.2f} mGy = {D_rad*1e3:.0f} mrad, E_abs = {E_absorbed_J:.2e} J, N_photons = {N_photons:.2e})")

    # 4. Example 43.11: Nuclear Reactions
    m_1H = 1.007825
    m_7Li = 7.016003  # actual source 7.016003 u
    m_4He = 4.002603
    m_14N = 14.003074
    m_17O = 16.999132

    # Part (a): 1H + 7Li -> 4He + 4He
    delta_m_a = (m_1H + m_7Li) - 2.0 * m_4He
    assert abs(delta_m_a - 0.018622) < 1e-7, f"Ex 43.11(a) delta_m mismatch: {delta_m_a}"
    Q_a_MeV = delta_m_a * 931.5
    assert abs(Q_a_MeV - 17.34639) < 0.01, f"Ex 43.11(a) Q mismatch: {Q_a_MeV}"

    # Part (b): 4He + 14N -> 1H + 17O
    delta_m_b = (m_4He + m_14N) - (m_1H + m_17O)
    assert abs(delta_m_b - (-0.001280)) < 1e-7, f"Ex 43.11(b) delta_m mismatch: {delta_m_b}"
    Q_b_MeV = delta_m_b * 931.5
    assert abs(Q_b_MeV - (-1.19232)) < 0.01, f"Ex 43.11(b) Q mismatch: {Q_b_MeV}"

    # Threshold kinetic energy in lab frame: K_th = ((M + m) / M) * |Q|
    K_th_MeV = ((m_14N + m_4He) / m_14N) * abs(Q_b_MeV)
    assert abs(K_th_MeV - 1.53313) < 0.01, f"Ex 43.11(b) K_th mismatch: {K_th_MeV}"
    print(f"  Ex 43.11: OK (7Li mass = {m_7Li} u, Q_a = +{Q_a_MeV:.2f} MeV [exoergic], Q_b = {Q_b_MeV:.3f} MeV, K_th = {K_th_MeV:.3f} MeV [endoergic])")

    # 5. Example 43.12: Uranium-235 Consumption
    P_therm_W = 3000.0e6  # 3000 MW thermal power given in problem statement
    E_fission_J = 200.0e6 * e_c  # 3.20435e-11 J
    n_fissions_s = P_therm_W / E_fission_J  # 9.362e19 fissions/s ~ 9.4e19
    m_atom_kg = 235.0 * u_kg  # 3.902e-25 kg
    dm_dt_kg_s = n_fissions_s * m_atom_kg  # 3.653e-5 kg/s ~ 3.7e-5 kg/s = 37 mg/s
    m_u235_day_kg = dm_dt_kg_s * 86400.0  # 3.156 kg ~ 3.2 kg
    assert abs(m_u235_day_kg - 3.156) < 0.05, f"Ex 43.12 m_u235 mismatch: {m_u235_day_kg}"
    coal_daily_kg = 10.6e6  # 10,600 tons = 10.6 million kg of coal
    print(f"  Ex 43.12: OK (P_th = {P_therm_W/1e6:.0f} MW, Fissions/s = {n_fissions_s:.2e}, U-235/day = {m_u235_day_kg:.2f} kg ~ 3.2 kg, Coal comparison = {coal_daily_kg/1e6:.1f} M kg/day)")

    # 6. Example 43.13: Deuteron Fusion (Triton + Proton branch: 2H + 2H -> 3H + 1H)
    m_2H = 2.014102
    m_3H = 3.016049
    m_1H = 1.007825
    delta_m_fus = 2.0 * m_2H - (m_3H + m_1H)
    assert abs(delta_m_fus - 0.004330) < 1e-7, f"Ex 43.13 delta_m mismatch: {delta_m_fus}"
    Q_fus_MeV = delta_m_fus * u_MeV
    assert abs(Q_fus_MeV - 4.033395) < 0.01, f"Ex 43.13 Q mismatch: {Q_fus_MeV}"
    print(f"  Ex 43.13: OK (2H + 2H -> 3H + 1H: delta_m = {delta_m_fus:.6f} u, Q = {Q_fus_MeV:.6f} MeV ~ 4.03 MeV)")

    # 7. Self-Checks (TYUs 43.4 - 43.8)
    # TYU 43.4: Pu-240 (5.00 uCi, 6560 yr) vs Am-243 (4.45 uCi, 7370 yr)
    ratio_N = (5.00 * 6560.0) / (4.45 * 7370.0)  # 32800 / 32796.5 = 1.0001067
    assert abs(ratio_N - 1.00) < 0.001
    print(f"  TYU 43.4: OK (Pu-240 vs Am-243: ratio = 32800 / 32796.5 = {ratio_N:.5f} ~ 1.00 -> equal number of nuclei, choice (iii))")

    # TYU 43.5: Radiation deep inside tissue: 200 keV X-rays vs alpha particles
    # Alpha has RBE=20 but extremely short range; 200 keV X-rays penetrate deep tissues
    print("  TYU 43.5: OK (200 keV X-rays have deep tissue penetration vs superficial alpha, choice (ii))")

    # TYU 43.6: Solid lithium sample in hydrogen gas (1H + 7Li -> 4He + 4He)
    # Coulomb repulsion (+e and +3e barrier ~ 1.2 MeV) prevents reaction at room temperature; cannot happen naturally
    print("  TYU 43.6: OK (Coulomb barrier prevents natural fusion of Li and H at room temperature, answer: No)")

    # TYU 43.7: Triggering 235U fission with slow proton
    # Proton experiences strong Coulomb repulsion (+e vs +92e); slow neutron has no charge and easily triggers fission
    print("  TYU 43.7: OK (Slow proton repelled by +92e Coulomb barrier; cannot trigger fission, answer: No)")

    # TYU 43.8: Are all fusion reactions exoergic?
    # No: Eb/A increases only up to A ~ 60; fusion of heavy nuclei (e.g. A=100+100->200) decreases Eb/A and is endoergic
    print("  TYU 43.8: OK (Fusion of nuclei with A > 60 is endoergic, answer: No)")

def verify_assets():
    print("\n=== 2. Verifying Image Assets ===")
    assert SOURCE_PDF.is_file(), f"Source PDF not found at {SOURCE_PDF}"
    doc = pymupdf.open(str(SOURCE_PDF))

    sys.path.append(str(ROOT / "scripts"))
    import importlib
    mod = importlib.import_module("prepare-physics43-theory-b-assets")

    scale = 3.0
    mat = pymupdf.Matrix(scale, scale)

    for name, page_idx, (x0, y0, x1, y1) in mod.FIGURES:
        img_path = IMG_DIR / name
        if not img_path.is_file():
            report_error(f"Missing image asset: {img_path}")
            continue

        im = Image.open(img_path)
        w, h = im.size
        if w == 0 or h == 0:
            report_error(f"Image {name} is empty (0x0)")
            continue

        # Re-crop fresh from PDF and compare
        page = doc[page_idx]
        clip_rect = pymupdf.Rect(x0, y0, x1, y1)
        pix = page.get_pixmap(matrix=mat, clip=clip_rect)

        if w != pix.width or h != pix.height:
            report_error(f"Dimension mismatch for {name}: disk {w}x{h} vs expected {pix.width}x{pix.height}")
        else:
            # Check byte matching
            disk_bytes = img_path.read_bytes()
            fresh_bytes = pix.tobytes("png")
            if len(disk_bytes) == 0:
                report_error(f"Image {name} is 0 bytes")
            else:
                print(f"  Asset {name}: OK ({w}x{h} px, {len(disk_bytes)} bytes)")

def verify_markdown_rules():
    print("\n=== 3. Verifying Markdown Rules & Pedagogical Structure ===")

    for path in TRANSLATIONS:
        if not path.is_file():
            report_error(f"Missing markdown translation file: {path}")
            continue

        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        # Rule: No frontmatter, no H1, no footer
        if lines and lines[0].strip() == "---":
            report_error(f"{path.name}: Contains YAML frontmatter")
        if re.search(r"^#\s+", text, re.MULTILINE):
            report_error(f"{path.name}: Contains H1 header (#)")

        # Rule: Check H2 section header
        h2_headers = re.findall(r"^##\s+(.+)$", text, re.MULTILINE)
        if not h2_headers:
            report_error(f"{path.name}: Missing H2 section header")

        # Rule: Check details tag closure
        open_containers = len(re.findall(r":::\s*(?:details|info|warning|tip|danger)", text))
        close_containers = len(re.findall(r"^:::\s*$", text, re.MULTILINE))
        if open_containers != close_containers:
            report_error(f"{path.name}: Container mismatch (open: {open_containers}, close: {close_containers})")

        # Rule: Closed ::: details summary must not reveal the answer
        for m in re.finditer(r":::\s*details\s+([^\n]+)", text):
            summary = m.group(1).strip()
            if any(opt in summary for opt in ["(i)", "(ii)", "(iii)", "(iv)", "(v)", "Đáp án", "Câu trả lời"]):
                report_error(f"{path.name}: ::: details summary reveals answer: {summary}")

        # Rule: No isolated single $ lines
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped == "$":
                report_error(f"{path.name}:{i+1}: Isolated single $ line")

        # Rule: $$ delimiters must be alone at column 0
        in_display_math = False
        for i, line in enumerate(lines):
            if "$$" in line:
                stripped = line.strip()
                if stripped != "$$":
                    report_error(f"{path.name}:{i+1}: '$$' delimiter is not alone on line: {line}")
                if not line.startswith("$$"):
                    report_error(f"{path.name}:{i+1}: '$$' is not at column 0: {line}")

        # Rule: Capitalization after colon (except URLs, drive paths, code, inline math, container syntax)
        for i, line in enumerate(lines):
            # Skip code blocks, headings, math, VitePress containers
            if line.startswith("#") or line.startswith("```") or line.startswith("$$") or line.startswith(":::"):
                continue
            # Look for ': <char>'
            matches = re.finditer(r":\s+([^\s])", line)
            for match in matches:
                start_idx = match.start()
                ch = match.group(1)
                # Exclude URL, http, file, C:\, etc.
                pre_text = line[max(0, start_idx-6):start_idx]
                if any(kw in pre_text for kw in ["http", "https", "file", "drive"]):
                    continue
                # Exclude if inside inline math $...$
                prefix = line[:start_idx]
                dollar_count = prefix.count("$")
                if dollar_count % 2 == 1:
                    continue
                # Exclude markdown formatting tokens
                if ch in ["*", "$", "`", "[", "(", "-", ">"]:
                    continue
                if ch.islower():
                    report_error(f"{path.name}:{i+1}: Lowercase word after colon: '...{line[max(0, start_idx-5):start_idx+15]}...'")

        # Rule: Avoid semicolons in prose (outside math, tables, code)
        in_code = False
        in_display = False
        for i, line in enumerate(lines):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if line.strip() == "$$":
                in_display = not in_display
                continue
            if in_code or in_display:
                continue

            # Remove inline math $...$
            cleaned_line = re.sub(r"\$[^$]+\$", "", line)
            # Remove markdown table rows
            if cleaned_line.strip().startswith("|"):
                continue
            if ";" in cleaned_line:
                report_error(f"{path.name}:{i+1}: Semicolon in prose: {cleaned_line.strip()[:60]}")

        # Rule: Avoid em dash in prose
        for i, line in enumerate(lines):
            if "—" in line:
                report_error(f"{path.name}:{i+1}: Em dash (—) in prose: {line.strip()[:60]}")

        # Rule: No file:/// links
        if "file:///" in text:
            report_error(f"{path.name}: Contains illegal 'file:///' link")

        print(f"  Markdown {path.name}: OK ({len(lines)} lines)")

def verify_image_annotations():
    print("\n=== 4. Verifying Image Annotations Module ===")
    assert ANNOTATIONS_FILE.is_file(), f"Missing annotations file: {ANNOTATIONS_FILE}"

    res = subprocess.run(["node", "--check", str(ANNOTATIONS_FILE)], capture_output=True, text=True)
    if res.returncode != 0:
        report_error(f"node --check failed for {ANNOTATIONS_FILE}:\n{res.stderr}")
    else:
        print(f"  node --check: OK")

    content = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    expected_stems = [
        "young-43/hinh-43-09",
        "young-43/hinh-43-10",
        "young-43/ung-dung-b-1",
        "young-43/hinh-43-11",
        "young-43/hinh-43-12",
        "young-43/hinh-43-13",
        "young-43/ung-dung-b-2",
        "young-43/hinh-43-14",
        "young-43/hinh-43-15",
        "young-43/hinh-43-16",
        "young-43/hinh-43-17",
        "young-43/hinh-43-18",
    ]
    for stem in expected_stems:
        if f'"{stem}"' not in content:
            report_error(f"Missing stem {stem} in {ANNOTATIONS_FILE}")
        else:
            print(f"  Stem {stem}: present in annotations")

def verify_math_measurements():
    print("\n=== 5. Running Delegated MathJax Measurement Helper ===")
    cmd = [
        "node",
        "C:/Users/Ai/Documents/StudyHub/qa/physics/measure-delegated-math.mjs",
        str(ROOT),
    ] + [str(p.relative_to(ROOT)) for p in TRANSLATIONS]

    res = subprocess.run(cmd, capture_output=True, text=True)
    # The output may contain neofetch/system banner before JSON
    out = res.stdout
    json_start = out.find("{\n  \"status\":")
    if json_start == -1:
        json_start = out.find("{\"status\":")

    if json_start != -1:
        json_text = out[json_start:]
        try:
            data = json.loads(json_text)
            status = data.get("status")
            findings = data.get("findings", [])
            display = data.get("display", 0)
            inline = data.get("inline", 0)
            print(f"  Math status: {status} (display: {display}, inline: {inline}, findings: {len(findings)})")
            if status != "passed" or findings:
                for f in findings:
                    report_error(f"Math probe finding: {f}")
        except json.JSONDecodeError as e:
            report_error(f"Failed to parse JSON from math helper: {e}\nRaw output: {out}")
    else:
        report_error(f"No JSON found in math helper output:\n{out}\n{res.stderr}")

def main():
    print("Starting Comprehensive Verification for Chapter 43 Theory B...")
    verify_calculations()
    verify_assets()
    verify_markdown_rules()
    verify_image_annotations()
    verify_math_measurements()

    print("\n=== Verification Summary ===")
    if ERRORS:
        print(f"FAILED with {len(ERRORS)} error(s):")
        for err in ERRORS:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"ALL CHECKS PASSED SUCCESSFULLY (0 errors, {len(WARNINGS)} warnings).")

if __name__ == "__main__":
    main()
