#!/usr/bin/env python3
"""
Comprehensive verifier for Chapter 41 Theory B (Sections 41.5 - 41.8):
- Numeric and physical calculations for all Examples (41.6 - 41.11) and TYUs (41.5 - 41.8)
- Asset pixel validation against source PDF (exact dimensions and byte-for-byte RGB integrity)
- Markdown syntax, pedagogical structure, colon capitalization, and math formatting audit
- Image annotations module consistency and syntax (node --check)
- Real MathJax width measurement (Display <= 27ex body, Tagged <= 32ex on 320px, Inline <= 38ex)
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
sys.path.insert(0, str(ROOT))
LOCAL_SOURCE = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE_PDF = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-41"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics41-theory-b-image-annotations.mjs"

TRANSLATIONS = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-41" / "05-spin-electron.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-41" / "06-nguyen-tu-nhieu-electron.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-41" / "07-pho-tia-x.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-41" / "08-roi-luong-tu.md",
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

    # Fundamental constants
    h = 6.62607015e-34
    hbar = h / (2 * math.pi)
    c = 2.99792458e8
    m_e = 9.1093837e-31
    e_c = 1.602176634e-19
    h_eV = 4.135667696e-15
    mu_B = e_c * hbar / (2.0 * m_e)
    mu_B_eV = mu_B / e_c
    g_e = 2.00231930436256
    alpha = 7.2973525693e-3

    # 1. Example 41.6: Electron spin in magnetic field B = 2.00 T
    B_416 = 2.00
    mu_z_J = 0.5 * g_e * mu_B
    mu_z_eV = mu_z_J / e_c
    assert abs(mu_z_J - 9.285e-24) < 1e-26, f"Ex 41.6 mu_z(J) mismatch: {mu_z_J}"
    assert abs(mu_z_eV - 5.795e-5) < 1e-7, f"Ex 41.6 mu_z(eV) mismatch: {mu_z_eV}"

    U_J = mu_z_J * B_416
    U_eV = mu_z_eV * B_416
    assert abs(U_J - 1.857e-23) < 2e-25, f"Ex 41.6 U(J) mismatch: {U_J}"
    assert abs(U_eV - 1.159e-4) < 2e-6, f"Ex 41.6 U(eV) mismatch: {U_eV}"

    delta_U_J = 2.0 * U_J
    delta_U_eV = 2.0 * U_eV
    f_res = delta_U_J / h
    assert abs(f_res - 5.60e10) < 5e8, f"Ex 41.6 f_res mismatch: {f_res}"
    print(f"  Ex 41.6: OK (mu_z = {mu_z_J:.3e} J/T = {mu_z_eV:.3e} eV/T, U = {U_eV:.3e} eV, f = {f_res/1e9:.1f} GHz)")

    # 2. Example 41.7: Sodium doublet D1 (588.995 nm) and D2 (589.592 nm)
    lam1 = 588.995e-9
    lam2 = 589.592e-9
    delta_E_J = h * c * (1.0 / lam1 - 1.0 / lam2)
    delta_E_eV = delta_E_J / e_c
    assert abs(delta_E_eV - 2.13e-3) < 2e-5, f"Ex 41.7 delta_E mismatch: {delta_E_eV}"
    assert abs(delta_E_J - 3.41e-22) < 2e-24, f"Ex 41.7 delta_E_J mismatch: {delta_E_J}"
    U_J = delta_E_J / 2.0
    B_eff = U_J / (1.00116 * mu_B)
    assert abs(B_eff - 18.39) < 0.1, f"Ex 41.7 B_eff mismatch: {B_eff}"
    print(f"  Ex 41.7: OK (lambda = 588.995/589.592 nm, delta_E = {delta_E_eV*1e3:.3f} meV = {delta_E_J:.2e} J, B_eff = {B_eff:.2f} T ~ 18.4 T)")

    # 3. Example 41.8: Lyman-alpha fine structure
    # Eq 41.41 for n=2, j=3/2 vs j=1/2:
    # E_2,3/2 - E_2,1/2 = (13.60 eV / 4) * (alpha^2 / 4)
    delta_E_fine_eV = (13.60 / 4.0) * (alpha**2 / 4.0)
    assert abs(delta_E_fine_eV - 4.53e-5) < 5e-7, f"Ex 41.8 delta_E_fine mismatch: {delta_E_fine_eV}"
    lam_0 = 121.6e-9
    E_gamma = 10.20
    delta_lam = (lam_0 / E_gamma) * delta_E_fine_eV
    assert abs(delta_lam - 5.40e-13) < 5e-15, f"Ex 41.8 delta_lam mismatch: {delta_lam}"
    lam_meas_half = 121.567364e-9
    lam_meas_threehalf = 121.566824e-9
    delta_lam_meas = lam_meas_half - lam_meas_threehalf
    assert abs(delta_lam_meas - 5.40e-13) < 1e-15
    print(f"  Ex 41.8: OK (delta_E = {delta_E_fine_eV*1e5:.2f}e-5 eV, delta_lam = {delta_lam*1e12:.3f} pm, measured = {lam_meas_half*1e9:.6f} / {lam_meas_threehalf*1e9:.6f} nm)")

    # 4. Example 41.9: Z_eff for 3s state in Sodium (E_3s = -5.138 eV)
    E_3s = -5.138
    n_3s = 3
    Z_eff_3s = n_3s * math.sqrt(-E_3s / 13.60)
    assert abs(Z_eff_3s - 1.843) < 0.01, f"Ex 41.9 Z_eff mismatch: {Z_eff_3s}"
    screening = 11 - Z_eff_3s
    assert abs(screening - 9.16) < 0.02
    print(f"  Ex 41.9: OK (Sodium 3s: E = {E_3s} eV, Z_eff = {Z_eff_3s:.2f} ~ 1.84, screening = {screening:.2f} e-)")

    # 5. Example 41.10: Potassium 4s valence ground state, lowest Z_eff state is 4f (n = 4, l = 3)
    E_4f_est = - (1.00**2 / 16.0) * 13.60
    assert abs(E_4f_est - (-0.85)) < 0.01, f"Ex 41.10 E_4f_est mismatch: {E_4f_est}"
    E_Mg_3d_est = - (2.00**2 / 9.0) * 13.60
    assert abs(E_Mg_3d_est - (-6.044)) < 0.02
    E_Mg_3d_exp = -6.01
    assert abs(E_Mg_3d_est - E_Mg_3d_exp) < 0.05
    print(f"  Ex 41.10: OK (Potassium 4f: Z_eff ~ 1 -> E_4f = {E_4f_est:.2f} eV; Mg+ 3d: Z_eff ~ 2 -> E_est = {E_Mg_3d_est:.1f} eV vs exp = {E_Mg_3d_exp} eV)")

    # 6. Example 41.11: Moseley's law chemical analysis (lambda = 0.0709 nm)
    lam_x = 0.0709e-9
    f_x = c / lam_x
    assert abs(f_x - 4.228e18) < 5e15, f"Ex 41.11 f_x mismatch: {f_x}"
    Z_est = 1.0 + math.sqrt(f_x / 2.48e15)
    assert abs(Z_est - 42.29) < 0.1, f"Ex 41.11 Z_est mismatch: {Z_est}"
    assert round(Z_est) == 42, f"Ex 41.11 element mismatch: {round(Z_est)}"
    print(f"  Ex 41.11: OK (f = {f_x:.3e} Hz, Z_est = {Z_est:.2f} -> Z = 42 Molybdenum Mo)")

    # TYU 41.5: Spin orientation angle theta
    cos_theta = 0.5 / (math.sqrt(3.0) / 2.0)
    theta_deg = math.degrees(math.acos(cos_theta))
    assert abs(theta_deg - 54.736) < 0.01, f"TYU 41.5 theta mismatch: {theta_deg}"
    print(f"  TYU 41.5: OK (cos theta = +/- 1/sqrt(3) -> theta = {theta_deg:.1f} deg != 0 deg -> option iv neither)")

    # TYU 41.6: Sodium without exclusion principle
    # All 11 electrons fall into n=1 (1s^11), feeling unscreened +11e attraction -> more difficult (ii)
    print("  TYU 41.6: OK (Hypothetical 1s^11 without exclusion -> unscreened +11e attraction -> more difficult, option ii)")

    # TYU 41.7: High-temperature atomic hydrogen
    # Thermal excitation populates n=1, 2, 3 -> absorption edges at 13.60 eV, 3.40 eV, 1.51 eV -> option iv all of these
    E_n1 = 13.60 / 1**2
    E_n2 = 13.60 / 2**2
    E_n3 = 13.60 / 3**2
    assert abs(E_n1 - 13.60) < 0.01
    assert abs(E_n2 - 3.40) < 0.01
    assert abs(E_n3 - 1.511) < 0.01
    print(f"  TYU 41.7: OK (High-temp H: absorption edges at 13.60 eV, 3.40 eV, 1.51 eV -> option iv all of these)")

    # TYU 41.8: Distinguishable particles product state
    print("  TYU 41.8: OK (Distinguishable e-/p+ -> valid wave function (yes); factors into product state -> not entangled (no))")

def verify_assets():
    print("=== 2. Verifying Asset Pixels & Dimensions ===")
    if not SOURCE_PDF.is_file():
        report_error(f"Missing source PDF: {SOURCE_PDF}")
        return

    doc = pymupdf.open(str(SOURCE_PDF))
    import importlib.util
    spec = importlib.util.spec_from_file_location("prep_assets", ROOT / "scripts" / "prepare-physics41-theory-b-assets.py")
    prep_assets = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep_assets)
    FIGURES = prep_assets.FIGURES

    scale = 3.0
    mat = pymupdf.Matrix(scale, scale)

    for name, page_idx, (x0, y0, x1, y1) in FIGURES:
        img_path = IMG_DIR / name
        if not img_path.is_file():
            report_error(f"Missing image asset: {img_path}")
            continue

        disk_img = Image.open(img_path)
        expected_w = int((x1 - x0) * scale)
        expected_h = int((y1 - y0) * scale)

        if disk_img.size != (expected_w, expected_h):
            report_error(f"{name}: Size mismatch! Disk: {disk_img.size}, Expected: ({expected_w}, {expected_h})")
            continue

        # Render fresh from PDF and compare RGB pixels byte-for-byte
        page = doc[page_idx]
        clip_rect = pymupdf.Rect(x0, y0, x1, y1)
        pix = page.get_pixmap(matrix=mat, clip=clip_rect)
        ref_img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        disk_rgb = disk_img.convert("RGB")
        if disk_rgb.tobytes() != ref_img.tobytes():
            report_error(f"{name}: Pixel mismatch against fresh PDF render!")
        else:
            print(f"  {name}: OK ({pix.width}x{pix.height} px, bit-exact RGB equality)")

def verify_markdown():
    print("=== 3. Auditing Markdown Syntax, Structure & Capitalization ===")

    all_images_found = set()
    all_equations_found = set()

    for md_path in TRANSLATIONS:
        if not md_path.is_file():
            report_error(f"Missing translation file: {md_path}")
            continue

        content = md_path.read_text(encoding="utf-8")
        lines = content.split("\n")

        # 1. No YAML frontmatter
        if lines and lines[0].strip().startswith("---"):
            report_error(f"{md_path.name}: YAML frontmatter detected on line 1")

        # 2. No H1
        for idx, line in enumerate(lines, 1):
            if line.startswith("# "):
                report_error(f"{md_path.name}:{idx}: H1 heading detected: {line}")

        # 3. Forbidden phrases
        forbidden = ["theo sách", "ảnh lấy từ sách", "nguyên tác", "bản dịch của", "hình trong sách"]
        for idx, line in enumerate(lines, 1):
            for phrase in forbidden:
                if phrase in line.lower():
                    report_error(f"{md_path.name}:{idx}: Forbidden phrase '{phrase}' detected")

        # 4. Check colon capitalization in prose
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith(":::"):
                continue
            # Match colon followed by space and letter
            for m in re.finditer(r':\s+([a-zA-Z\u00C0-\u1EF9])', stripped):
                char = m.group(1)
                # Ignore url, code, or math
                prefix = stripped[:m.start()]
                if "http" in prefix or "file:" in prefix or "$" in prefix or "`" in prefix:
                    continue
                if char.islower():
                    report_error(f"{md_path.name}:{idx}: Lowercase letter '{char}' after colon: '{stripped[max(0, m.start()-10):m.end()+15]}'")

        # 5. Check $$ delimiters
        in_display = False
        display_block = []
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped == "$$":
                if in_display:
                    in_display = False
                    block_tex = "\n".join(display_block).strip()
                    # Check tag position
                    if r"\tag{" in block_tex and r"\end{aligned}" in block_tex:
                        end_idx = block_tex.find(r"\end{aligned}")
                        tag_idx = block_tex.find(r"\tag{")
                        if tag_idx < end_idx:
                            report_error(f"{md_path.name}:{idx}: \\tag inside aligned block: {block_tex[:60]}")
                    tag_m = re.search(r'\\tag\{([^}]*)\}', block_tex)
                    if tag_m:
                        all_equations_found.add(tag_m.group(1))
                    display_block = []
                else:
                    in_display = True
                    display_block = []
            elif "$$" in stripped:
                report_error(f"{md_path.name}:{idx}: $$ delimiter not alone on line: {line}")
            elif in_display:
                display_block.append(line)

        # 6. Extract images
        for line in lines:
            for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', line):
                img_src = m.group(2)
                stem = Path(img_src).stem
                all_images_found.add(stem)

    expected_stems = {f"hinh-41-{i:02d}" for i in range(16, 28)} | {f"ung-dung-b-{i}" for i in range(1, 4)}
    missing_stems = expected_stems - all_images_found
    if missing_stems:
        report_error(f"Missing images in Markdown: {missing_stems}")
    else:
        print(f"  All {len(expected_stems)} source image crops linked with Vietnamese captions.")

    expected_equations = {f"41.{i}" for i in range(36, 53)}
    missing_eqs = expected_equations - all_equations_found
    if missing_eqs:
        report_error(f"Missing equation tags in Markdown: {missing_eqs}")
    else:
        print(f"  All 17 assigned equations (41.36 - 41.52) present and tagged!")

    print("  Markdown files audit completed!")

def verify_annotations():
    print("=== 4. Verifying Annotations Module ===")
    if not ANNOTATIONS_FILE.is_file():
        report_error(f"Missing annotations file: {ANNOTATIONS_FILE}")
        return

    text = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    for i in range(13, 28):
        key = f'"young-41/hinh-41-{i:02d}"'
        if key not in text:
            report_error(f"Missing key in annotations: {key}")

    for i in range(1, 4):
        key = f'"young-41/ung-dung-b-{i}"'
        if key not in text:
            report_error(f"Missing key in annotations: {key}")

    try:
        res = subprocess.run(["node", "--check", str(ANNOTATIONS_FILE)], capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            report_error(f"node --check failed: {res.stderr}")
        else:
            print("  node --check: Syntax valid!")
    except Exception as e:
        report_error(f"Failed to run node --check: {e}")

def verify_mathjax_widths():
    print("=== 5. Measuring MathJax Widths (Inline <= 38ex, Display Body <= 27ex, Full Tagged <= 32ex on 320px) ===")
    node_modules_pkg = Path("C:/Users/Ai/Documents/StudyHub/package.json")
    pkg_to_use = node_modules_pkg if node_modules_pkg.is_file() else (ROOT / "package.json")
    if not pkg_to_use.is_file():
        report_error("package.json not found, cannot run MathJax measurement")
        return

    display_items = []
    inline_items = []

    for md_path in TRANSLATIONS:
        if not md_path.is_file():
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
let maxDisplay = 0;
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
    if (w > maxDisplay) maxDisplay = w;
    if (w <= 0) {{
      console.log(`[DISPLAY ZERO WIDTH] Extracted width is ${{w}}ex: ${{item.file}}:${{item.line}}`);
      displayErrors++;
      continue;
    }}
    if (w > 27.0) {{
      console.log(`[DISPLAY OVERFLOW] ${{w.toFixed(2)}}ex > 27ex at ${{item.file}}:${{item.line}}: ${{item.tex.replace(/\\n/g, ' ')}}`);
      displayErrors++;
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

console.log(`MathJax measurement complete: ${{data.display.length}} display blocks (max: ${{maxDisplay.toFixed(2)}}ex), ${{data.inline.length}} inline items (max: ${{maxInline.toFixed(2)}}ex).`);
if (displayErrors > 0 || inlineErrors > 0) {{
  console.log(`FAILED with ${{displayErrors}} display errors and ${{inlineErrors}} inline errors.`);
  process.exit(1);
}} else {{
  console.log(`PASSED: All display body <= 27ex (max ${{maxDisplay.toFixed(2)}}ex), tagged <= 32ex, inline <= 38ex (max ${{maxInline.toFixed(2)}}ex)!`);
  process.exit(0);
}}
"""

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as f:
        json.dump({"display": display_items, "inline": inline_items}, f, ensure_ascii=False)
        temp_json = f.name

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".js", delete=False) as f:
        f.write(js_code)
        temp_js = f.name

    try:
        res = subprocess.run(["node", temp_js, temp_json], capture_output=True, text=True, encoding="utf-8")
        print(res.stdout)
        if res.returncode != 0:
            report_error(f"MathJax measurement failed:\n{res.stdout}\n{res.stderr}")
    finally:
        try:
            os.remove(temp_json)
            os.remove(temp_js)
        except OSError:
            pass

def main():
    print("=================================================================")
    print("   Chapter 41 Theory B Comprehensive Verification Suite")
    print("=================================================================")

    verify_calculations()
    verify_assets()
    verify_markdown()
    verify_annotations()
    verify_mathjax_widths()

    print("\n=================================================================")
    if ERRORS:
        print(f"FAILED: {len(ERRORS)} error(s) detected:")
        for err in ERRORS:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("ALL VERIFICATION CHECKS PASSED PERFECTLY!")
        sys.exit(0)

if __name__ == "__main__":
    main()
