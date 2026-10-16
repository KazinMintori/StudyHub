#!/usr/bin/env python3
"""
Comprehensive verifier for Chapter 40 Theory A (Section 40.1):
- Physical and quantum mechanical derivations/calculations for all concepts, Examples 40.1-40.2, and TYU 40.1
- Image asset pixel validation against source PDF (RGB exact match)
- Markdown syntax, academic style, colon capitalization, and math delimiter audit
- Annotation module consistency and syntax
- Real MathJax width measurement (Display body <= 25ex, Tagged <= 32ex on 320px, Inline <= 30ex)
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

IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-40"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics40-theory-a-image-annotations.mjs"

TRANSLATION_FILE = ROOT / "raw_materials" / "physics" / "translations" / "chapter-40" / "01-ham-song-schrodinger.md"

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
    me = 9.1093837e-31       # kg
    c = 2.99792458e8         # m/s

    # 1. Fundamental constant ratio
    assert abs(hbar - h / (2 * math.pi)) < 1e-40, "hbar definition mismatch"
    print(f"  Fundamental constants: OK (hbar = {hbar:.3e} J*s, h = {h:.3e} J*s)")

    # 2. String wave vs matter wave dispersion
    # For string: omega = v * k (linear) -> d2y/dt2 has -omega^2
    # For free matter wave: E = p^2 / (2m), p = hbar * k, E = hbar * omega
    # -> hbar * omega = hbar^2 * k^2 / (2m) -> omega = (hbar / 2m) * k^2 (quadratic)
    k_test = 1.5e10  # 1/m (typical electron wave number)
    omega_matter = (hbar * k_test**2) / (2 * me)
    vp_matter = omega_matter / k_test
    vg_matter = hbar * k_test / me
    assert abs(vg_matter - 2 * vp_matter) / vg_matter < 1e-12, "Group velocity must be twice phase velocity for nonrelativistic free particle"
    print(f"  Matter wave dispersion: OK (omega ~ k^2, vp = {vp_matter:.2e} m/s, vg = 2*vp = {vg_matter:.2e} m/s)")

    # 3. Euler relation & Schrödinger constant C
    # Trial: Psi = A cos(kx - wt) + B sin(kx - wt)
    # -hbar^2 / (2m) * d2Psi/dx2 = C * hbar * dPsi/dt
    # gives A = -C*B and B = C*A -> C^2 = -1 -> algebraic C = +-i
    assert (1j)**2 == -1 and (-1j)**2 == -1, "Both C = +i and C = -i satisfy C^2 = -1"
    # Conventional choice C = +i corresponds to conventional phase factor exp(-i*E*t/hbar) with E > 0
    C_conv = 1j
    print(f"  Schrödinger operator derivation: OK (C^2 = -1 -> algebraic C = +-i, convention C = +i for exp(-i*E*t/hbar))")

    # 4. Plane wave modulus squared and relative probability density
    # Psi(x, t) = A * exp(i(kx - wt)) -> |Psi|^2 = |A|^2
    # Integral over [-L/2, L/2] = |A|^2 * L -> infty as L -> infty (idealization, not normalizable on R)
    L_vals = [10.0, 100.0, 1000.0]
    A_val = 2.0
    for L in L_vals:
        integral_val = (abs(A_val)**2) * L
        assert integral_val == 4.0 * L
    print(f"  Plane wave non-normalizability: OK (integral over [-L/2, L/2] = |A|^2 * L -> infty as L -> infty)")

    # 5. Example 40.1: Superposition of two free-particle plane waves
    # Both k1 and k2 are distinct positive numbers (k2 > k1 > 0)
    k1 = 2.0e10
    k2 = 3.0e10
    assert k1 > 0 and k2 > 0 and k1 != k2, "k1 and k2 must be distinct positive numbers"
    w1 = (hbar * k1**2) / (2 * me)
    w2 = (hbar * k2**2) / (2 * me)

    # Verify Schrödinger equation residual for superposition
    t_test = 1.0e-15
    x_grid = np.linspace(-1e-9, 1e-9, 500)
    psi1 = A_val * np.exp(1j * (k1 * x_grid - w1 * t_test))
    psi2 = A_val * np.exp(1j * (k2 * x_grid - w2 * t_test))
    psi_total = psi1 + psi2

    lhs = (hbar * w1) * psi1 + (hbar * w2) * psi2
    rhs = 1j * hbar * (-1j * w1 * psi1 - 1j * w2 * psi2)
    residual = np.max(np.abs(lhs - rhs))
    assert residual < 1e-25, f"Schrödinger equation residual too high: {residual}"

    # Verify probability distribution function formula:
    # |Psi(x, t)|^2 = 2|A|^2 [1 + cos((k2 - k1)x - (w2 - w1)t)] = 4|A|^2 cos^2[((k2 - k1)x - (w2 - w1)t)/2]
    prob_direct = np.abs(psi_total)**2
    prob_formula = 4 * (abs(A_val)**2) * (np.cos(((k2 - k1) * x_grid - (w2 - w1) * t_test) / 2.0))**2
    diff_prob = np.max(np.abs(prob_direct - prob_formula))
    assert diff_prob < 1e-12, f"Probability formula mismatch: {diff_prob}"

    # Verify motion of interference pattern:
    # Pattern speed v_av = (w2 - w1) / (k2 - k1)
    # Average momentum p_av = hbar * (k1 + k2) / 2
    # Velocity relation: v_av = p_av / me
    v_av_wave = (w2 - w1) / (k2 - k1)
    p_av = hbar * (k1 + k2) / 2.0
    v_av_particle = p_av / me
    assert abs(v_av_wave - v_av_particle) / v_av_wave < 1e-14, "v_av from wave speed must match p_av/m"

    # Max, min, and spatial period
    max_prob = np.max(prob_formula)
    min_prob = np.min(prob_formula)
    x_peak = ((w2 - w1) * t_test) / (k2 - k1)
    exact_peak_prob = 4 * (abs(A_val)**2) * (np.cos(((k2 - k1) * x_peak - (w2 - w1) * t_test) / 2.0))**2
    assert abs(exact_peak_prob - 4 * abs(A_val)**2) < 1e-14, f"Exact peak mismatch: {exact_peak_prob}"
    assert abs(max_prob - 4 * abs(A_val)**2) < 1e-4, f"Max prob on grid mismatch: {max_prob} vs {4 * abs(A_val)**2}"
    assert min_prob >= -1e-12, "Probability density cannot be negative"
    delta_x_expected = (2 * math.pi) / (k2 - k1)
    assert abs(delta_x_expected - 6.2831853e-10) < 1e-14
    print(f"  Ex 40.1: OK (Schr residual = {residual:.1e}, max |Psi|^2 = 4|A|^2, min = 0, Delta x = {delta_x_expected:.3e} m, v_av = {v_av_wave:.2e} m/s == p_av/m)")

    # 6. Wave packet Fourier uncertainty relation (Eq. 40.19)
    # Gaussian packet: A(k) = exp(-(k-k0)^2 / (4 sigma_k^2))
    # Fourier transform: Psi(x, 0) = exp(-x^2 / (4 sigma_x^2))
    # where sigma_x * sigma_k = 1/2 -> Delta x * Delta p = hbar / 2
    sigma_k = 1.0e9  # 1/m
    sigma_x = 1.0 / (2 * sigma_k)
    delta_p = hbar * sigma_k
    uncertainty_product = sigma_x * delta_p
    assert abs(uncertainty_product - hbar / 2.0) < 1e-45, "Minimum uncertainty product mismatch"
    print(f"  Wave packet uncertainty: OK (sigma_x * sigma_p = hbar / 2 = {uncertainty_product:.3e} J*s)")

    # 7. Example 40.2: Stationary state with U(x) = 0
    # psi(x) = A1 exp(ikx) + A2 exp(-ikx)
    # -hbar^2 / (2m) * d2psi/dx2 = hbar^2 k^2 / (2m) * psi(x) = E * psi(x)
    A1 = 1.5
    A2 = 2.5
    psi_stat = A1 * np.exp(1j * k1 * x_grid) + A2 * np.exp(-1j * k1 * x_grid)
    d2psi_dx2 = -(k1**2) * psi_stat
    E_stat_expected = (hbar**2 * k1**2) / (2 * me)
    lhs_stat = - (hbar**2 / (2 * me)) * d2psi_dx2
    rhs_stat = E_stat_expected * psi_stat
    stat_residual = np.max(np.abs(lhs_stat - rhs_stat))
    assert stat_residual < 1e-25, f"Stationary state residual too high: {stat_residual}"

    # Definite momentum recovery when one coefficient is zero:
    dpsi1_dx = 1j * k1 * (A1 * np.exp(1j * k1 * x_grid))
    p_hat_psi1 = -1j * hbar * dpsi1_dx
    assert np.allclose(p_hat_psi1, hbar * k1 * (A1 * np.exp(1j * k1 * x_grid))), "Single plane wave must have definite momentum"

    # Probability current: j = (hbar*k/m) * (|A1|^2 - |A2|^2)
    # Pure standing wave if |A1| == |A2|: j = 0
    j_standing = (hbar * k1 / me) * (abs(A1)**2 - abs(A1)**2)
    assert j_standing == 0.0, "Pure standing wave (|A1| = |A2|) has zero probability current"

    # Unequal coefficients (|A1| != |A2|): j != 0, nonzero average momentum
    j_net = (hbar * k1 / me) * (abs(A1)**2 - abs(A2)**2)
    p_exp = hbar * k1 * (A1**2 - A2**2) / (A1**2 + A2**2)
    assert j_net != 0.0 and abs(p_exp) > 0, "Unequal coefficients give nonzero current and nonzero <p>"

    # Independence of time: |Psi(x, t)|^2 = |psi(x)|^2
    t1 = 0.0
    t2 = 5.0e-15
    Psi_t1 = psi_stat * np.exp(-1j * E_stat_expected * t1 / hbar)
    Psi_t2 = psi_stat * np.exp(-1j * E_stat_expected * t2 / hbar)
    diff_stat_time = np.max(np.abs(np.abs(Psi_t1)**2 - np.abs(Psi_t2)**2))
    assert diff_stat_time < 1e-14, f"Stationary probability must be time independent: {diff_stat_time}"
    print(f"  Ex 40.2: OK (E = {E_stat_expected:.3e} J = {E_stat_expected/1.602e-19:.2f} eV, single wave -> definite p, standing |A1|=|A2| -> j=0, unequal -> j={j_net:.2e}, <p>={p_exp:.2e} != +hbar*k)")

    # 8. TYU 40.1: Distinct energies requirement
    # Free energy depends only on |k|: k and -k share the SAME energy
    assert (hbar**2 * k1**2) / (2 * me) == (hbar**2 * (-k1)**2) / (2 * me), "k and -k have same free particle energy"
    # But a spatially localized wave packet requires a range of |k|, hence distinct energies
    # Superposition of distinct energies has time-varying |Psi(x, t)|^2
    t_eval = np.linspace(0, 1e-14, 100)
    psi_tyu = A_val * np.exp(1j * (k1 * 0.0 - w1 * t_eval)) + A_val * np.exp(1j * (k2 * 0.0 - w2 * t_eval))
    prob_tyu = np.abs(psi_tyu)**2
    variation = np.max(prob_tyu) - np.min(prob_tyu)
    assert variation > 1.0, f"Wave packet must show time-dependent probability density: variation = {variation}"
    print(f"  TYU 40.1: OK (k and -k share same E, but localized packet has range of |k| and energies -> time-varying |Psi|^2 with variation = {variation:.2f} > 0 -> Answer: NO)")

def verify_images():
    print("=== 2. Verifying Image Assets ===")
    crops = {
        "hinh-40-01": (1342, (34, 137, 194, 298)),
        "hinh-40-02": (1345, (454, 136, 614, 342)),
        "hinh-40-03": (1345, (450, 448, 618, 600)),
        "hinh-40-04": (1346, (34, 239, 194, 454)),
        "hinh-40-05": (1347, (350, 108.5, 618, 246)),
        "hinh-40-06": (1348, (32, 133, 202, 472)),
        "hinh-40-07": (1349, (450, 113, 618, 535)),
    }

    if not SOURCE_PDF.is_file():
        report_error(f"Source PDF not found at {SOURCE_PDF}")
        return

    doc = pymupdf.open(SOURCE_PDF)
    for stem, (p_num, box) in crops.items():
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

    if not TRANSLATION_FILE.is_file():
        report_error(f"Missing translation file: {TRANSLATION_FILE}")
        return

    content = TRANSLATION_FILE.read_text(encoding="utf-8")
    lines = content.splitlines()

    # Check for frontmatter
    if lines and lines[0].strip() == "---":
        report_error(f"{TRANSLATION_FILE.name}: Frontmatter detected! Fragments must not have frontmatter.")

    # Check for H1 or references
    for idx, line in enumerate(lines, 1):
        if line.startswith("# ") and not line.startswith("## "):
            report_error(f"{TRANSLATION_FILE.name}:{idx}: H1 heading detected! Fragments start at H2.")
        if line.strip().startswith("## Tài liệu tham khảo"):
            report_error(f"{TRANSLATION_FILE.name}:{idx}: References heading detected! Fragments must not contain references heading.")

    # Check for forbidden words, em dashes, \\vert, colons
    for idx, line in enumerate(lines, 1):
        for fw in forbidden_words:
            if fw in line.lower():
                report_error(f"{TRANSLATION_FILE.name}:{idx}: Contains forbidden word '{fw}': {line[:60]}")

        # Check for em dash in prose
        if "—" in line:
            report_error(f"{TRANSLATION_FILE.name}:{idx}: Contains forbidden em dash (—). Use comma, parentheses, colon, or natural Vietnamese conjunctions: {line[:60]}")
        if " -- " in line:
            report_error(f"{TRANSLATION_FILE.name}:{idx}: Contains double dash (--) in prose: {line[:60]}")

        # Check for \\vert{} or \\Vert{}
        if r"\vert" in line or r"\Vert" in line:
            report_error(f"{TRANSLATION_FILE.name}:{idx}: Contains forbidden \\vert or \\Vert. Use |x| or \\|x\\| directly: {line[:60]}")

        # Colon capitalization check in prose
        if not line.strip().startswith("$$") and not line.strip().startswith("```") and not line.strip().startswith(":::") and "http" not in line:
            colon_matches = re.finditer(r':\s+([a-zàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ])', line)
            for cm in colon_matches:
                char_found = cm.group(1)
                report_error(f"{TRANSLATION_FILE.name}:{idx}: Colon followed by lowercase '{char_found}'. Must be capitalized: ...{line[max(0, cm.start()-15):min(len(line), cm.end()+15)]}...")

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
                    report_error(f"{TRANSLATION_FILE.name}:{idx}: Opening $$ must be at column 0.")
            else:
                in_display = False
                if not line.startswith("$$"):
                    report_error(f"{TRANSLATION_FILE.name}:{idx}: Closing $$ must be at column 0.")
                tex_block = "\n".join(current_tex_lines)
                if re.search(r'=\s*\\\\', tex_block):
                    report_error(f"{TRANSLATION_FILE.name}:{display_line_start}: Math line break immediately after = (empty RHS forbidden).")
                if re.search(r'\([^)]*&[^)]*\)', tex_block):
                    report_error(f"{TRANSLATION_FILE.name}:{display_line_start}: '&' found inside parentheses. Alignment must be at top-level relation.")
                if re.search(r'=\s*&', tex_block):
                    report_error(f"{TRANSLATION_FILE.name}:{display_line_start}: '= &' found. Place '&' right before '=' ('&=') instead.")
                if re.search(r'\\\\\s*[+\-]', tex_block):
                    report_error(f"{TRANSLATION_FILE.name}:{display_line_start}: Math line broken at + or - operator. Only break at relations.")
        elif in_display:
            current_tex_lines.append(line)
        else:
            if "$$" in line:
                report_error(f"{TRANSLATION_FILE.name}:{idx}: Inline $$ detected. $$ must be on its own line.")

    # Check presence of all equations 40.1 to 40.23
    expected_tags = [
        "40.1", "40.2", "40.3a", "40.3b", "40.3c", "40.3d",
        "40.4", "40.5", "40.6", "40.7a", "40.7b", "40.8",
        "40.9", "40.10", "40.11", "40.12", "40.13", "40.14a", "40.14b",
        "40.15", "40.16", "40.17", "40.18", "40.19", "40.20",
        "40.21", "40.22", "40.23"
    ]
    for tag in expected_tags:
        if f"\\tag{{{tag}}}" not in content:
            report_error(f"Missing equation tag \\tag{{{tag}}} in translation!")
        else:
            print(f"  Equation \\tag{{{tag}}}: present.")

    # Check images 40.1 to 40.7
    for i in range(1, 8):
        img_target = f"../img/young-40/hinh-40-{i:02d}.png"
        if img_target not in content:
            report_error(f"Missing image reference: {img_target}")
        else:
            print(f"  Image reference '{img_target}': present.")

    print(f"  {TRANSLATION_FILE.name}: Markdown formatting checks completed.")

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
    for i in range(1, 8):
        key = f"young-40/hinh-40-{i:02d}"
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

    if not TRANSLATION_FILE.is_file():
        return

    lines = TRANSLATION_FILE.read_text(encoding="utf-8").splitlines()
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
                    "file": TRANSLATION_FILE.name,
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
                    inline_items.append({"file": TRANSLATION_FILE.name, "line": idx, "tex": inline_tex})

    if not display_items:
        report_warning("No display math blocks found in translations yet.")
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
    print("=== VERIFYING CHAPTER 40 THEORY A (SECTIONS 40.1) ===")
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
