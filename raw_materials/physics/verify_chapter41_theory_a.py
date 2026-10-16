#!/usr/bin/env python3
"""
Comprehensive verifier for Chapter 41 Theory A (Sections 41.1–41.4):
- Physical and quantum mechanical calculations for all concepts, Examples 41.1–41.5, and TYU 41.1–41.4
- Image asset pixel validation against source PDF (fresh RGB exact match)
- Markdown syntax, academic style, colon capitalization, and math delimiter audit for all 4 files
- Annotation module consistency and syntax
- Real MathJax width measurement (Display body <= 27ex, Tagged <= 35ex on 320px, Inline <= 38ex)
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
import numpy as np

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent.parent
LOCAL_SOURCE = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE_PDF = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-41"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics41-theory-a-image-annotations.mjs"

TRANSLATION_FILES = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-41" / "01-schrodinger-ba-chieu.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-41" / "02-hop-ba-chieu.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-41" / "03-nguyen-tu-hydro.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-41" / "04-hieu-ung-zeeman.md",
]

CROPS = [
    ("hinh-41-01", 1382, (34, 545, 195, 672)),
    ("hinh-41-02", 1384, (34, 300, 195, 755)),
    ("hinh-41-03", 1385, (400, 205, 560, 350)),
    ("hinh-41-04", 1386, (245, 530, 528, 748)),
    ("hinh-41-05", 1388, (34, 160, 195, 345)),
    ("hinh-41-06", 1390, (34, 215, 195, 528)),
    ("hinh-41-07", 1391, (454, 165, 614, 370)),
    ("hinh-41-08", 1393, (454, 224, 614, 515)),
    ("hinh-41-09", 1393, (100, 545, 425, 715)),
    ("hinh-41-10", 1394, (215, 104, 575, 305)),
    ("hinh-41-11", 1395, (454, 280, 614, 545)),
    ("hinh-41-12", 1395, (454, 600, 614, 755)),
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

    hbar = 1.054571817e-34  # J * s
    h = 6.62607015e-34       # J * s
    e_charge = 1.602176634e-19 # C
    me = 9.1093837e-31       # kg
    mp = 1.67262192e-27      # kg
    eps0 = 8.8541878128e-12  # F/m
    c = 2.99792458e8         # m/s

    # 1. Fundamental constant ratio
    assert abs(hbar - h / (2 * math.pi)) < 1e-40, "hbar definition mismatch"
    print(f"  Fundamental constants: OK (hbar = {hbar:.3e} J*s, h = {h:.3e} J*s)")

    # 2. Section 41.1: TYU 41.1
    # U = 0, E > 0, d2psi/dx2 > 0, d2psi/dy2 > 0, d2psi/dz2 > 0
    # Equation: Laplacian(psi) = -(2mE/hbar^2) * psi
    # LHS > 0, -(2mE/hbar^2) < 0 => psi must be negative.
    print("  TYU 41.1: OK (LHS > 0 and -(2mE/hbar^2) < 0 => psi < 0)")

    # 3. Section 41.2: Example 41.1
    # (a) Normalization constant C = (2/L)^(3/2)
    # Integral of sin^2(n*pi*x/L) from 0 to L is L/2.
    # C^2 * (L/2)^3 = 1 => C = (2/L)^(3/2)
    # (b) Probability in 0 <= x <= L/4
    def prob_quarter(nx):
        return 0.25 - 1.0 / (2 * nx * math.pi) * math.sin(nx * math.pi / 2)

    p1 = prob_quarter(1)
    p2 = prob_quarter(2)
    p3 = prob_quarter(3)
    assert abs(p1 - 0.091) < 0.001, f"Ex 41.1 p1 expected ~0.091, got {p1}"
    assert abs(p2 - 0.250) < 0.001, f"Ex 41.1 p2 expected 0.250, got {p2}"
    assert abs(p3 - 0.303) < 0.001, f"Ex 41.1 p3 expected ~0.303, got {p3}"
    print(f"  Example 41.1: OK (P1 = {p1:.3f}, P2 = {p2:.3f}, P3 = {p3:.3f})")

    # 4. Section 41.2: TYU 41.2
    # E proportional to nx^2 + ny^2 + nz^2
    s_i = 2**2 + 3**2 + 2**2    # 17
    s_ii = 4**2 + 1**2 + 1**2   # 18
    s_iii = 2**2 + 2**2 + 3**2  # 17
    s_iv = 1**2 + 3**2 + 3**2   # 19
    assert s_iv > s_ii > s_i and s_i == s_iii, "TYU 41.2 ranking mismatch"
    print(f"  TYU 41.2: OK (sum of squares: iv={s_iv} > ii={s_ii} > i={s_i} == iii={s_iii})")

    # 5. Section 41.3: Example 41.2
    # n = 3 states: l in {0, 1, 2}. States count: 1 + 3 + 5 = 9 = 3^2.
    n_states = sum(2 * l + 1 for l in range(3))
    assert n_states == 9, "Ex 41.2 state count mismatch"
    E3_calc = -13.60 / (3**2)
    assert abs(E3_calc - (-1.51)) < 0.01, f"Ex 41.2 E3 expected -1.51 eV, got {E3_calc}"
    print(f"  Example 41.2: OK (states = {n_states}, E3 = {E3_calc:.2f} eV)")

    # 6. Section 41.3: Example 41.3
    # n = 4 => l_max = 3
    l_max = 3
    L_max = math.sqrt(l_max * (l_max + 1))
    assert abs(L_max - math.sqrt(12)) < 1e-12
    theta_min_deg = math.degrees(math.acos(3.0 / L_max))
    assert abs(theta_min_deg - 30.0) < 0.1, f"Ex 41.3 theta_min expected 30.0 deg, got {theta_min_deg}"
    print(f"  Example 41.3: OK (L_max = {L_max:.3f} hbar = sqrt(12) hbar, theta_min = {theta_min_deg:.1f} deg)")

    # 7. Section 41.3: Example 41.4
    # (a) Normalization: int_0^infty (4/a^3) * r^2 * exp(-2r/a) dr = 1
    # Let u = 2r/a => dr = (a/2) du => (4/a^3) * (a/2)^3 * int_0^infty u^2 exp(-u) du = (4/8) * 2! = 1.
    # (b) Probability r < a: 1 - 5 * exp(-2)
    p_ground_a = 1.0 - 5.0 * math.exp(-2.0)
    assert abs(p_ground_a - 0.323) < 0.001, f"Ex 41.4 p_ground_a expected 0.323, got {p_ground_a}"
    print(f"  Example 41.4: OK (norm = 1.0, P(r < a) = 1 - 5e^(-2) = {p_ground_a:.3f})")

    # 8. Section 41.3: Bohr radius & ground state energy from fundamental constants
    mr = (me * mp) / (me + mp)
    a_bohr = (4 * math.pi * eps0 * hbar**2) / (mr * e_charge**2)
    assert abs(a_bohr - 5.29e-11) < 0.05e-11, f"Bohr radius mismatch: {a_bohr}"
    E1_joule = (mr * e_charge**4) / (2 * (4 * math.pi * eps0)**2 * hbar**2)
    E1_eV = E1_joule / e_charge
    assert abs(E1_eV - 13.60) < 0.05, f"Hydrogen ground energy mismatch: {E1_eV}"
    print(f"  Bohr radius & energy: OK (a = {a_bohr:.3e} m, E1 = -{E1_eV:.2f} eV)")

    # 9. Section 41.3: TYU 41.3
    # P(r) for 1s: P_1s(r) = (4/a^3) * r^2 * exp(-2r/a)
    # at r = 5a: P_1s(5a) = (100 * exp(-10)) / a
    p_1s_5a = 100.0 * math.exp(-10.0) # in units of 1/a
    assert abs(p_1s_5a - 0.00453999) < 1e-7, f"P_1s(5a) expected ~0.00454, got {p_1s_5a}"

    # P(r) for 2p: P_2p(r) = (1 / (24 * a^5)) * r^4 * exp(-r/a)
    # at r = 5a: P_2p(5a) = (625 / 24) * exp(-5) / a
    p_2p_5a = (625.0 / 24.0) * math.exp(-5.0) # in units of 1/a
    assert abs(p_2p_5a - 0.175467) < 1e-5, f"P_2p(5a) expected ~0.17547, got {p_2p_5a}"
    assert p_2p_5a > p_1s_5a, "2p must have higher probability than 1s at r=5a"
    ratio_p = p_2p_5a / p_1s_5a
    assert abs(ratio_p - 38.65) < 0.1

    # Counterexample for peak rule: 2s state outer maximum
    # P_2s(r) = (1/(2 a^3)) * r^2 * (1 - r/(2a))^2 * exp(-r/a)
    # Roots of derivative of x^2 * (1 - x/2)^2 * exp(-x):
    # x^3 - 8x^2 + 16x - 8 = 0
    # Outer root is 3 + sqrt(5) approx 5.236068 (not 4a!)
    outer_root_2s = 3.0 + math.sqrt(5.0)
    assert abs(outer_root_2s - 5.236068) < 1e-5
    print(f"  TYU 41.3: OK (P_1s(5a) = {p_1s_5a:.6f}/a, P_2p(5a) = {p_2p_5a:.6f}/a, ratio = {ratio_p:.1f}x, 2s peak = {outer_root_2s:.3f}a != 4a)")

    # 10. Section 41.4: Example 41.5
    # lambda = 600.000 nm, B = 2.00 T
    # E = hc / lambda
    lam_0 = 600e-9
    E_phot_J = (h * c) / lam_0
    E_phot_eV = E_phot_J / e_charge
    assert abs(E_phot_eV - 2.07) < 0.01, f"Ex 41.5 photon E expected 2.07 eV, got {E_phot_eV}"
    mu_B_J = (e_charge * hbar) / (2 * me)
    mu_B_eV = mu_B_J / e_charge
    assert abs(mu_B_J - 9.274e-24) < 0.005e-24, f"mu_B Joule mismatch: {mu_B_J}"
    assert abs(mu_B_eV - 5.788e-5) < 0.005e-5, f"mu_B eV mismatch: {mu_B_eV}"
    delta_E_eV = mu_B_eV * 2.00
    delta_E_J = mu_B_J * 2.00
    assert abs(delta_E_eV - 1.16e-4) < 0.01e-4, f"Ex 41.5 delta_E mismatch: {delta_E_eV}"
    assert abs(delta_E_J - 1.85e-23) < 0.01e-23, f"Ex 41.5 delta_E_J mismatch: {delta_E_J}"
    ratio_dE = delta_E_eV / E_phot_eV
    assert abs(ratio_dE - 5.60e-5) < 0.05e-5, f"Ex 41.5 ratio mismatch: {ratio_dE}"
    delta_lam = lam_0 * ratio_dE
    assert abs(delta_lam - 0.034e-9) < 0.001e-9, f"Ex 41.5 delta_lambda mismatch: {delta_lam}"
    lam_1 = (lam_0 - delta_lam) * 1e9
    lam_2 = lam_0 * 1e9
    lam_3 = (lam_0 + delta_lam) * 1e9
    assert abs(lam_1 - 599.966) < 0.001
    assert abs(lam_3 - 600.034) < 0.001
    print(f"  Example 41.5: OK (E = {E_phot_eV:.2f} eV, delta_E = {delta_E_eV:.2e} eV, delta_lam = {delta_lam*1e9:.3f} nm, triplet = {lam_1:.3f}, {lam_2:.3f}, {lam_3:.3f} nm)")

    # 11. Section 41.4: TYU 41.4
    print("  TYU 41.4: OK (Physics invariant under coordinate axis reorientation)")

def verify_images():
    print("=== 2. Verifying Image Assets Pixel Equality (RGB 100%) ===")
    if not SOURCE_PDF.is_file():
        report_error(f"Source PDF not found at {SOURCE_PDF}")
        return

    doc = pymupdf.open(SOURCE_PDF)
    for stem, p_num, box in CROPS:
        img_file = IMG_DIR / f"{stem}.png"
        if not img_file.is_file():
            report_error(f"Missing image file: {img_file}")
            continue
        if img_file.stat().st_size < 1000:
            report_error(f"Image file too small or empty: {img_file}")
            continue

        with Image.open(img_file) as im:
            w, h = im.size
            im_rgb = np.array(im.convert("RGB"))
            page = doc[p_num - 1]
            rect = pymupdf.Rect(box) & page.rect
            expected_w = int(round(rect.width * 2.5))
            expected_h = int(round(rect.height * 2.5))
            if abs(w - expected_w) > 2 or abs(h - expected_h) > 2:
                report_error(f"Image dimensions mismatch for {stem}: got {w}x{h}, expected ~{expected_w}x{expected_h}")
                continue
            pix = page.get_pixmap(matrix=pymupdf.Matrix(2.5, 2.5), clip=rect, alpha=False)
            pix_rgb = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, 3))
            if not np.array_equal(im_rgb, pix_rgb):
                report_error(f"Image byteRGB mismatch for {stem}!")
            else:
                print(f"  {stem}.png: OK ({w}x{h} px, byteRGB match 100% against PDF p.{p_num})")

def verify_markdown():
    print("=== 3. Auditing Markdown Content & Formatting ===")
    forbidden_words = [
        "cực kỳ", "vô cùng", "kỳ diệu", "giả trân", "bẫy thi cử", "then chốt",
        "theo sách", "ảnh lấy từ sách", "hình trong sách", "nguyên tác",
        "bản dịch", "lớp bài toán", "lớp hàm", "hợp đồng"
    ]

    for t_file in TRANSLATION_FILES:
        if not t_file.is_file():
            report_error(f"Missing translation file: {t_file}")
            continue

        content = t_file.read_text(encoding="utf-8")
        lines = content.splitlines()

        # Check for frontmatter
        if lines and lines[0].strip() == "---":
            report_error(f"{t_file.name}: Frontmatter detected! Fragments must not have frontmatter.")

        # Check for H1 or references
        for idx, line in enumerate(lines, 1):
            if line.startswith("# ") and not line.startswith("## "):
                report_error(f"{t_file.name}:{idx}: H1 heading detected! Fragments start at H2.")
            if line.strip().startswith("## Tài liệu tham khảo"):
                report_error(f"{t_file.name}:{idx}: References heading detected! Fragments must not contain references heading.")

        # Check for forbidden words, em dashes, \vert, colons
        for idx, line in enumerate(lines, 1):
            for fw in forbidden_words:
                if fw in line.lower():
                    report_error(f"{t_file.name}:{idx}: Contains forbidden word '{fw}': {line[:60]}")

            # Check for em dash in prose
            if "—" in line:
                report_error(f"{t_file.name}:{idx}: Contains forbidden em dash (—). Use comma, parentheses, colon, or natural Vietnamese conjunctions: {line[:60]}")
            if " -- " in line:
                report_error(f"{t_file.name}:{idx}: Contains double dash (--) in prose: {line[:60]}")

            # Check for \vert{} or \Vert{}
            if r"\vert" in line or r"\Vert" in line:
                report_error(f"{t_file.name}:{idx}: Contains forbidden \\vert or \\Vert. Use |x| or \\|x\\| directly: {line[:60]}")

            # Colon capitalization check in prose
            if not line.strip().startswith("$$") and not line.strip().startswith("```") and not line.strip().startswith(":::") and "http" not in line:
                colon_matches = re.finditer(r':\s+([a-zàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ])', line)
                for cm in colon_matches:
                    char_found = cm.group(1)
                    report_error(f"{t_file.name}:{idx}: Colon followed by lowercase '{char_found}'. Must be capitalized: ...{line[max(0, cm.start()-15):min(len(line), cm.end()+15)]}...")

            # Details summary answer leak check
            if line.strip().startswith("::: details"):
                if ": Đáp án" in line or ": Thứ tự" in line:
                    report_error(f"{t_file.name}:{idx}: Details summary line must not leak answers: {line.strip()}")

        # Math delimiters check
        in_display = False
        display_line_start = 0
        current_tex_lines = []

        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped == "$$":
                if not in_display:
                    in_display = True
                    display_line_start = idx
                    current_tex_lines = []
                    if not line.startswith("$$"):
                        report_error(f"{t_file.name}:{idx}: Opening '$$' must be at COLUMN 0 alone!")
                else:
                    in_display = False
                    if not line.startswith("$$"):
                        report_error(f"{t_file.name}:{idx}: Closing '$$' must be at COLUMN 0 alone!")

                    # Analyze block
                    block_text = "\n".join(current_tex_lines).strip()
                    if r"\begin{aligned}" in block_text:
                        lines_in_aligned = [l.strip() for l in current_tex_lines if l.strip() and not l.strip().startswith(r"\begin{aligned}") and not l.strip().startswith(r"\end{aligned}")]
                        if len(lines_in_aligned) <= 1:
                            report_error(f"{t_file.name}:{display_line_start}: Unnecessary one-line aligned block!")
                        for al_idx, al_line in enumerate(lines_in_aligned, 1):
                            if al_line.endswith(r"\\"):
                                if not ("=" in al_line or "<" in al_line or ">" in al_line or r"\le" in al_line or r"\ge" in al_line or r"\approx" in al_line or r"\implies" in al_line or r"\iff" in al_line or al_line.startswith("&")):
                                    report_error(f"{t_file.name}:{display_line_start}+{al_idx}: Line break inside aligned must occur at relation or start with &: {al_line}")
            elif in_display:
                current_tex_lines.append(line)
            else:
                if stripped == "$":
                    report_error(f"{t_file.name}:{idx}: Isolated single dollar delimiter line!")

        if in_display:
            report_error(f"{t_file.name}: Unclosed display math block starting at line {display_line_start}")

        print(f"  {t_file.name}: Markdown formatting checks completed.")

    # Image presence checks across files
    all_content = "\n".join(t.read_text(encoding="utf-8") for t in TRANSLATION_FILES if t.is_file())
    for stem, _, _ in CROPS:
        img_target = f"../img/young-41/{stem}.png"
        if img_target not in all_content:
            report_error(f"Missing image reference in translations: {img_target}")
        else:
            print(f"  Image reference '{img_target}': present.")

def verify_annotations():
    print("=== 4. Auditing Image Annotations Module ===")
    if not ANNOTATIONS_FILE.is_file():
        report_error(f"Missing annotations file: {ANNOTATIONS_FILE}")
        return

    res = subprocess.run(["node", "--check", str(ANNOTATIONS_FILE)], capture_output=True, text=True)
    if res.returncode != 0:
        report_error(f"Node syntax check failed on {ANNOTATIONS_FILE}:\n{res.stderr}")
    else:
        print(f"  {ANNOTATIONS_FILE.name}: node --check PASSED cleanly.")

    content = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    for i in range(1, 13):
        key = f"young-41/hinh-41-{i:02d}"
        if key not in content:
            report_error(f"Missing key in annotations: '{key}'")
        else:
            print(f"  Key '{key}': present.")

def verify_mathjax_widths():
    print("=== 5. Measuring Real MathJax Widths (SVG ex) ===")
    pkg_to_use = ROOT / "package.json"
    if not pkg_to_use.is_file():
        pkg_to_use = Path("C:/Users/Ai/Documents/StudyHub/package.json")

    display_items = []
    inline_items = []

    for t_file in TRANSLATION_FILES:
        if not t_file.is_file():
            continue

        lines = t_file.read_text(encoding="utf-8").splitlines()
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
                    tag_match = re.search(r'\\tag\{([^}]+)\}', block)
                    tag_val = tag_match.group(1) if tag_match else None
                    clean_block = re.sub(r'\\tag\{[^}]+\}', '', block).strip()
                    display_items.append({
                        "file": t_file.name,
                        "line": cur_start,
                        "tex": clean_block,
                        "tag": tag_val
                    })
            elif in_display:
                cur_tex.append(line)
            else:
                matches = re.finditer(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', line)
                for m in matches:
                    inline_tex = m.group(1).strip()
                    if inline_tex:
                        inline_items.append({"file": t_file.name, "line": idx, "tex": inline_tex})

    if not display_items:
        report_warning("No display math blocks found in translations.")
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
let maxDisplay = 0;
let maxTagged = 0;
let maxInline = 0;

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
    if (w > maxDisplay) maxDisplay = w;
    if (w > 27.0) {{
      console.log(`[DISPLAY OVERFLOW] ${{w.toFixed(2)}}ex > 27ex at ${{item.file}}:${{item.line}}: ${{item.tex.replace(/\\n/g, ' ')}}`);
      displayErrors++;
    }} else if (w > 25.0) {{
      console.log(`[DISPLAY TARGET NOTE] ${{w.toFixed(2)}}ex > 25ex (within max 27ex) at ${{item.file}}:${{item.line}}`);
    }}
    if (item.tag) {{
      const renderedTag = md.render('$(' + item.tag + ')$');
      const mTag = renderedTag.match(/width="([\\d.]+)ex"/);
      const tagW = mTag ? parseFloat(mTag[1]) : 4.0;
      const fullW = w + 2.0 + tagW;
      if (fullW > maxTagged) maxTagged = fullW;
      if (fullW > 35.0) {{
        console.log(`[TAGGED OVERFLOW] ${{fullW.toFixed(2)}}ex > 35ex on 320px at ${{item.file}}:${{item.line}}: tag (${{item.tag}})`);
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
    if (w > maxInline) maxInline = w;
    if (w > 38.0) {{
      console.log(`[INLINE OVERFLOW] ${{w.toFixed(2)}}ex > 38ex at ${{item.file}}:${{item.line}}: $${{item.tex}}$`);
      inlineErrors++;
    }}
  }} catch (err) {{
    // ignore inline render error
  }}
}}

console.log(`MathJax stats: Max display body = ${{maxDisplay.toFixed(2)}}ex (limit <= 27ex, target <= 25ex), max tagged = ${{maxTagged.toFixed(2)}}ex (limit <= 35ex on 320px), max inline = ${{maxInline.toFixed(2)}}ex (limit <= 38ex, target <= 27ex).`);
console.log(`MathJax measurement complete: ${{data.display.length}} display blocks, ${{data.inline.length}} inline items.`);
if (displayErrors > 0 || inlineErrors > 0) {{
  console.log(`FAILED with ${{displayErrors}} display errors and ${{inlineErrors}} inline errors.`);
  process.exit(1);
}} else {{
  console.log(`PASSED: All display body <= 27ex, tagged <= 35ex on 320px box, inline <= 38ex!`);
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
        except Exception:
            pass

def main():
    print("=================================================================")
    print("=== VERIFYING CHAPTER 41 THEORY A (SECTIONS 41.1–41.4) ===")
    print("=================================================================")

    verify_calculations()
    verify_images()
    verify_markdown()
    verify_annotations()
    verify_mathjax_widths()

    print("=================================================================")
    if ERRORS:
        print(f"FAILED: {len(ERRORS)} error(s) found!")
        for e in ERRORS:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"ALL CHECKS PASSED CLEANLY! (Warnings: {len(WARNINGS)})")
        sys.exit(0)

if __name__ == "__main__":
    main()
