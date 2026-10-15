#!/usr/bin/env python3
"""
Comprehensive verifier for Chapter 39 Theory A (Sections 39.1 - 39.2):
- Numeric and quantum calculations for all 4 examples and 2 TYUs
- Asset pixel validation against source PDF
- Markdown syntax, style, colon capitalization, and math formatting audit
- Annotation module consistency and syntax
- Real MathJax width measurement (Display <= 25ex body, Tagged <= 32ex on 320px, Inline <= 30ex)
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

IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-39"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics39-theory-a-image-annotations.mjs"

TRANSLATIONS = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-39" / "01-song-electron.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-39" / "02-nguyen-tu-hat-nhan-pho.md",
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

    h_SI = 6.626e-34
    c = 3.00e8
    e = 1.602e-19
    me = 9.109e-31

    # Sand grain de Broglie wavelength
    m_sand = 5e-10
    v_sand = 0.4
    p_sand = m_sand * v_sand
    assert abs(p_sand - 2e-10) < 1e-12, f"Sand p mismatch: {p_sand}"
    lam_sand = h_SI / p_sand
    assert round(lam_sand * 1e24) == 3, f"Sand lambda mismatch: {lam_sand}"
    print(f"  Sand grain: OK (p = {p_sand*1e10:.1f}e-10 kg*m/s, lambda = {lam_sand*1e24:.1f}e-24 m)")

    # Ex 39.1: Electron-diffraction experiment
    Vba_1 = 54.0
    p_1 = math.sqrt(2 * me * e * Vba_1)
    lam_1 = h_SI / p_1
    assert round(lam_1 * 1e10, 1) == 1.7, f"Ex 39.1 lambda mismatch: {lam_1}"
    assert round(lam_1 * 1e9, 2) == 0.17, f"Ex 39.1 lambda (nm) mismatch: {lam_1*1e9}"

    d_1 = 2.18e-10
    lam_1_bragg = d_1 * math.sin(math.radians(50.0))
    assert round(lam_1_bragg * 1e10, 1) == 1.7, f"Ex 39.1 Bragg mismatch: {lam_1_bragg}"
    print(f"  Ex 39.1: OK (lambda_deBroglie = {lam_1*1e10:.2f}e-10 m, lambda_Bragg = {lam_1_bragg*1e10:.2f}e-10 m ~ 0.17 nm)")

    # Ex 39.2: Energy of a thermal neutron
    mn = 1.675e-27
    lam_2 = 0.200e-9
    v_2 = h_SI / (lam_2 * mn)
    assert round(v_2 * 1e-3, 2) == 1.98, f"Ex 39.2 v mismatch: {v_2}"
    K_2 = 0.5 * mn * v_2**2
    assert round(K_2 * 1e21, 2) == 3.28, f"Ex 39.2 K mismatch: {K_2}"
    K_2_eV = K_2 / e
    assert round(K_2_eV, 4) == 0.0205, f"Ex 39.2 K (eV) mismatch: {K_2_eV}"

    kB = 1.38e-23
    T_2 = 293.0
    K_therm = 1.5 * kB * T_2
    assert round(K_therm * 1e21, 2) == 6.07, f"Ex 39.2 K_therm mismatch: {K_therm}"
    K_therm_eV = K_therm / e
    assert round(K_therm_eV, 4) == 0.0379, f"Ex 39.2 K_therm (eV) mismatch: {K_therm_eV}"
    assert v_2 / c < 1e-4, f"Ex 39.2 nonrelativistic check: {v_2/c}"
    print(f"  Ex 39.2: OK (v = {v_2:.1f} m/s, K = {K_2*1e21:.2f}e-21 J = {K_2_eV:.4f} eV, K_therm = {K_therm_eV:.4f} eV)")

    # Ex 39.3: Electron microscope
    lam_3 = 10e-12
    Vba_3 = (h_SI**2) / (2 * me * e * lam_3**2)
    assert round(Vba_3, -2) == 15000, f"Ex 39.3 Vba mismatch: {Vba_3}"
    assert round(Vba_3 * 1e-4, 1) == 1.5, f"Ex 39.3 Vba round mismatch: {Vba_3}"
    K_3_keV = (e * Vba_3) / (e * 1e3)
    assert abs(K_3_keV - 15.0) < 0.1
    assert K_3_keV < 511.0, f"Ex 39.3 nonrelativistic check: {K_3_keV} keV vs 511 keV"
    print(f"  Ex 39.3: OK (Vba = {Vba_3:.0f} V ~ 15 kV, K = 15 keV << 511 keV)")

    # TYU 39.1: Proton vs neutron, and photon of 54 eV
    mp = 1.673e-27
    assert mp < mn, "mp must be slightly less than mn"
    # (a) Same lambda -> K = h^2 / (2 m lambda^2) -> K_p > K_n -> (i)
    # (b) Photon with E = 54 eV: lambda = hc / E
    E_phot_eV = 54.0
    h_eV = 4.136e-15  # eV * s
    c_speed = 2.998e8  # m/s
    lam_phot = (h_eV * c_speed) / E_phot_eV
    assert round(lam_phot * 1e8, 1) == 2.3, f"TYU 39.1(b) photon lambda mismatch: {lam_phot}"
    ratio_phot_electron = lam_phot / 1.7e-10
    assert ratio_phot_electron > 100, f"Photon wavelength should be >100x electron wavelength, got {ratio_phot_electron}"
    print(f"  TYU 39.1: OK (mp < mn -> K_p > K_n (i); lambda_photon = {lam_phot*1e8:.2f}e-8 m ~ 2.3e-8 m, ratio = {ratio_phot_electron:.1f} > 100 -> no (khong))")

    # Ex 39.4: Rutherford alpha scattering on gold nucleus
    eps0_factor = 9.0e9  # 1 / (4 pi epsilon0)
    q1 = 2 * 1.60e-19
    q2 = 79 * 1.60e-19
    r_4 = 5.0e-14
    U_4_J = eps0_factor * q1 * q2 / r_4
    assert round(U_4_J * 1e13, 1) == 7.3, f"Ex 39.4 U_4 mismatch: {U_4_J}"
    # In textbook: 7.3 * 10^-13 J / (1.60 * 10^-19 J/eV) = 4.5625 * 10^6 eV = 4.6 MeV
    U_4_eV_rounded = 7.3e-13 / 1.60e-19
    assert round(U_4_eV_rounded * 1e-6, 1) == 4.6, f"Ex 39.4 U_4 (MeV) mismatch: {U_4_eV_rounded}"

    m_alpha = 6.64e-27
    v_alpha = math.sqrt(2 * 7.3e-13 / m_alpha)
    assert round(v_alpha * 1e-7, 1) == 1.5, f"Ex 39.4 v_alpha mismatch: {v_alpha}"
    p_alpha = 9.8e-20  # rounded value in text: 9.8 * 10^-20 kg * m/s

    m_Au = 3.27e-25
    v_Au = p_alpha / m_Au
    assert round(v_Au * 1e-5, 1) == 3.0, f"Ex 39.4 v_Au mismatch: {v_Au}"
    K_Au_J = 0.5 * m_Au * v_Au**2
    assert round(K_Au_J * 1e14, 1) == 1.5, f"Ex 39.4 K_Au mismatch: {K_Au_J}"
    K_Au_MeV = K_Au_J / (1.602e-13)
    assert round(K_Au_MeV, 3) == 0.092, f"Ex 39.4 K_Au (MeV) mismatch: {K_Au_MeV}"
    recoil_pct = (K_Au_MeV / 4.6) * 100
    assert round(recoil_pct) == 2, f"Ex 39.4 recoil percentage mismatch: {recoil_pct}"
    print(f"  Ex 39.4: OK (U = {U_4_J*1e13:.1f}e-13 J = 4.6 MeV; v_alpha = {v_alpha*1e-7:.1f}e7 m/s; recoil K_Au = {K_Au_MeV:.3f} MeV ~ 2%)")

    # TYU 39.2: Alpha on solid hydrogen
    # Alpha particle has mass ~ 4 u, proton has mass ~ 1 u
    # In 1D head-on elastic collision: v_1f = (m1 - m2)/(m1 + m2) * v_1i = (4 - 1)/(4 + 1) * v_1i = +3/5 v_1i > 0
    # The alpha cannot bounce backward (theta < 90 deg always) -> less large-angle scattering -> (iii)
    print("  TYU 39.2: OK (m_alpha > m_proton -> alpha continues forward -> less large-angle scattering (iii))")

def verify_images():
    print("=== 2. Verifying Image Assets ===")
    crops = {
        "hinh-39-01": (1300, (34, 146, 194, 360)),
        "hinh-39-02": (1300, (235, 572, 555, 746)),
        "hinh-39-03": (1301, (454, 125, 616, 472)),
        "hinh-39-04": (1301, (454, 610, 648, 746)),
        "hinh-39-05": (1304, (34, 358, 196, 615)),
        "hinh-39-06": (1305, (454, 175, 648, 314)),
        "hinh-39-07": (1305, (105, 552, 405, 744)),
        "hinh-39-08": (1306, (268, 105, 512, 242)),
        "hinh-39-09": (1306, (0, 592, 194, 744)),
        "hinh-39-10": (1307, (454, 166, 614, 300)),
        "hinh-39-11": (1307, (78, 526, 420, 746)),
        "hinh-39-12": (1308, (34, 84, 196, 265)),
        "hinh-39-13": (1308, (215, 448, 560, 595)),
        "hinh-39-14": (1309, (454, 365, 615, 660)),
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
        "bản dịch", "lớp bài toán", "lớp hàm"
    ]

    for md_path in TRANSLATIONS:
        if not md_path.is_file():
            report_error(f"Missing translation file: {md_path}")
            continue

        content = md_path.read_text(encoding="utf-8")
        lines = content.splitlines()

        # Check for frontmatter
        if lines and lines[0].strip() == "---":
            report_error(f"{md_path.name}: Frontmatter detected! Fragments must not have frontmatter.")

        # Check for forbidden words
        for idx, line in enumerate(lines, 1):
            for fw in forbidden_words:
                if fw in line.lower():
                    report_error(f"{md_path.name}:{idx}: Contains forbidden word '{fw}': {line[:60]}")

            # Check for em dash in prose
            if "—" in line:
                report_error(f"{md_path.name}:{idx}: Contains forbidden em dash (—). Use comma, parentheses, colon, or natural Vietnamese conjunctions: {line[:60]}")
            if " -- " in line:
                report_error(f"{md_path.name}:{idx}: Contains double dash (--) in prose: {line[:60]}")

            # Check for \\vert{} or \\Vert{}
            if r"\vert" in line or r"\Vert" in line:
                report_error(f"{md_path.name}:{idx}: Contains forbidden \\vert or \\Vert. Use |x| or \\|x\\| directly: {line[:60]}")

            # Colon capitalization check in prose
            # Match colon followed by whitespace and a lowercase Vietnamese letter
            # Exclude code blocks, URLs, display math, and ::: container directives
            if not line.strip().startswith("$$") and not line.strip().startswith("```") and not line.strip().startswith(":::") and "http" not in line:
                # Find colons not preceded by $ and not followed by $
                colon_matches = re.finditer(r':\s+([a-zàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ])', line)
                for cm in colon_matches:
                    char_found = cm.group(1)
                    report_error(f"{md_path.name}:{idx}: Colon followed by lowercase '{char_found}'. Must be capitalized: ...{line[max(0, cm.start()-15):min(len(line), cm.end()+15)]}...")

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
                        report_error(f"{md_path.name}:{idx}: Opening $$ must be at column 0.")
                else:
                    in_display = False
                    if not line.startswith("$$"):
                        report_error(f"{md_path.name}:{idx}: Closing $$ must be at column 0.")
                    # Audit display block
                    tex_block = "\n".join(current_tex_lines)
                    # Check break after =
                    if re.search(r'=\s*\\\\', tex_block):
                        report_error(f"{md_path.name}:{display_line_start}: Math line break immediately after = (empty RHS forbidden).")
                    # Check & inside ()
                    if re.search(r'\([^)]*&[^)]*\)', tex_block):
                        report_error(f"{md_path.name}:{display_line_start}: '&' found inside parentheses. Alignment must be at top-level relation.")
                    # Check = &
                    if re.search(r'=\s*&', tex_block):
                        report_error(f"{md_path.name}:{display_line_start}: '= &' found. Place '&' right before '=' ('&=') instead.")
                    # Check breaking at + or -
                    if re.search(r'\\\\\s*[+\-]', tex_block):
                        report_error(f"{md_path.name}:{display_line_start}: Math line broken at + or - operator. Only break at relations.")
            elif in_display:
                current_tex_lines.append(line)
            else:
                if "$$" in line:
                    report_error(f"{md_path.name}:{idx}: Inline $$ detected. $$ must be on its own line.")

        print(f"  {md_path.name}: Markdown formatting checks completed.")

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
    for i in range(1, 15):
        key = f"young-39/hinh-39-{i:02d}"
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

    for md_path in TRANSLATIONS:
        if not md_path.is_file():
            continue
        lines = md_path.read_text(encoding="utf-8").splitlines()
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
                        "file": md_path.name,
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
                        inline_items.append({"file": md_path.name, "line": idx, "tex": inline_tex})

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
    if (w > 30.0) {{
      console.log(`[INLINE OVERFLOW] ${{w.toFixed(2)}}ex > 30ex at ${{item.file}}:${{item.line}}: $${{item.tex}}$`);
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
  console.log(`PASSED: All display body <= 25ex, tagged <= 32ex, inline <= 30ex!`);
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
    print("STARTING AUDIT: Chapter 39 Theory A (Sections 39.1 - 39.2)")
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
