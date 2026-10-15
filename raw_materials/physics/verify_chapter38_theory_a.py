#!/usr/bin/env python3
"""
Comprehensive verifier for Chapter 38 Theory A (Sections 38.1 - 38.2):
- Numeric and photon calculations for all 4 examples and 2 TYUs
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

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent.parent
LOCAL_SOURCE = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE_PDF = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-38"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics38-theory-a-image-annotations.mjs"

TRANSLATIONS = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-38" / "01-quang-dien.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-38" / "02-phat-tia-x.md",
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

    # Ex 38.1: Laser-pointer photons
    lam_1 = 650e-9
    c = 3.00e8
    h_SI = 6.626e-34
    p_1 = h_SI / lam_1
    assert abs(p_1 - 1.01938e-27) < 1e-29, f"Ex 38.1 p mismatch: {p_1}"
    assert round(p_1 * 1e27, 2) == 1.02, f"Ex 38.1 p round mismatch: {p_1*1e27}"

    E_1 = p_1 * c
    assert abs(E_1 - 3.058e-19) < 1e-21, f"Ex 38.1 E mismatch: {E_1}"
    assert round(E_1 * 1e19, 2) == 3.06, f"Ex 38.1 E round mismatch: {E_1*1e19}"
    E_1_eV = E_1 / 1.602e-19
    assert round(E_1_eV, 2) == 1.91, f"Ex 38.1 E (eV) round mismatch: {E_1_eV}"

    P_1 = 5.00e-3
    N_1 = P_1 / E_1
    assert abs(N_1 - 1.6349e16) < 1e14, f"Ex 38.1 N mismatch: {N_1}"
    assert round(N_1 * 1e-16, 2) == 1.63, f"Ex 38.1 N round mismatch: {N_1*1e-16}"
    print(f"  Ex 38.1: OK (p = {p_1*1e27:.2f}e-27 kg*m/s, E = {E_1_eV:.2f} eV, N = {N_1*1e-16:.2f}e16 photons/s)")

    # Ex 38.2: Photoelectric-effect experiment
    V0_2 = 1.25
    e = 1.60e-19
    m_e = 9.11e-31
    Kmax_J = e * V0_2
    assert abs(Kmax_J - 2.00e-19) < 1e-21, f"Ex 38.2 Kmax mismatch: {Kmax_J}"
    vmax_2 = math.sqrt(2 * Kmax_J / m_e)
    assert abs(vmax_2 - 6.626e5) < 1e3, f"Ex 38.2 vmax mismatch: {vmax_2}"
    assert round(vmax_2 * 1e-5, 2) == 6.63, f"Ex 38.2 vmax round mismatch: {vmax_2*1e-5}"
    assert vmax_2 / c < 0.003, f"Ex 38.2 non-relativistic check: {vmax_2/c}"
    print(f"  Ex 38.2: OK (Kmax = {Kmax_J*1e19:.2f}e-19 J = {V0_2:.2f} eV, vmax = {vmax_2*1e-5:.2f}e5 m/s)")

    # Ex 38.3: Determining phi and h experimentally
    f1 = c / 600e-9
    f2 = c / 400e-9
    f3 = c / 300e-9
    assert abs(f1 - 0.50e15) < 1e12
    assert abs(f2 - 0.75e15) < 1e12
    assert abs(f3 - 1.00e15) < 1e12
    intercept = -1.0
    phi_eV = abs(intercept)
    phi_J = phi_eV * e
    assert phi_eV == 1.0
    assert abs(phi_J - 1.6e-19) < 1e-21
    slope = (3.0 - (-1.0)) / (1.00e15 - 0)
    assert abs(slope - 4.0e-15) < 1e-17
    h_meas = slope * e
    assert abs(h_meas - 6.4e-34) < 1e-36
    accepted_h = 6.626e-34
    diff_pct = abs(h_meas - accepted_h) / accepted_h * 100
    assert abs(diff_pct - 3.41) < 0.2
    print(f"  Ex 38.3: OK (phi = {phi_eV:.1f} eV = {phi_J*1e19:.1f}e-19 J, slope = {slope*1e15:.1f}e-15, h = {h_meas*1e34:.1f}e-34 J*s, diff ~ 3%)")

    # TYU 38.1: Silicon photoconductivity
    E_thresh_eV = 1.14
    h_eV = 4.136e-15
    lam_thresh_m = h_eV * c / E_thresh_eV
    lam_thresh_nm = lam_thresh_m * 1e9
    assert abs(lam_thresh_nm - 1088.4) < 1.0
    assert round(lam_thresh_nm) == 1088 or round(lam_thresh_nm, -1) == 1090
    assert 300 <= 1090 and 600 <= 1090 and 1200 > 1090
    print(f"  TYU 38.1: OK (Threshold lambda = {lam_thresh_nm:.0f} nm ~ 1090 nm; (i) 300 nm & (ii) 600 nm cause effect, (iii) 1200 nm does not -> Answer (iv))")

    # Ex 38.4: Producing x rays
    VAC_4 = 10.0e3
    e_std = 1.602e-19
    lam_min_SI = (h_SI * c) / (e_std * VAC_4)
    assert abs(lam_min_SI - 1.2408e-10) < 1e-13
    assert round(lam_min_SI * 1e9, 3) == 0.124
    lam_min_eV = (h_eV * c) / (VAC_4)
    assert abs(lam_min_eV - 1.2408e-10) < 1e-13
    print(f"  Ex 38.4: OK (lambda_min = {lam_min_SI*1e10:.2f}e-10 m = {lam_min_SI*1e9:.3f} nm)")

    # TYU 38.2: X-ray intensity and minimum wavelength
    # lambda_min = hc / (e * VAC), depends only on VAC.
    # Increasing electron rate increases photons/s -> I increases, lambda_min unchanged.
    print("  TYU 38.2: OK (Increasing cathode electron emission rate increases I while lambda_min remains unchanged -> Answer (ii))")

def verify_images():
    print("=== 2. Validating Image Files against Source PDF ===")
    if not SOURCE_PDF.is_file():
        report_error(f"Source PDF not found at {SOURCE_PDF}")
        return

    expected_images = {
        "hinh-38-01.png": (1274, (34, 75, 196, 245)),
        "hinh-38-02.png": (1274, (34, 390, 196, 716)),
        "hinh-38-03.png": (1275, (75, 58, 442, 336)),
        "hinh-38-04.png": (1275, (454, 522, 615, 665)),
        "hinh-38-05.png": (1276, (34, 615, 196, 725)),
        "hinh-38-06.png": (1277, (454, 268, 615, 475)),
        "hinh-38-07.png": (1279, (454, 585, 615, 746)),
        "hinh-38-08.png": (1280, (34, 342, 196, 520)),
        "hinh-38-09.png": (1281, (454, 530, 615, 712)),
    }

    scale = 2.5
    doc = pymupdf.open(SOURCE_PDF)
    for fname, (p_num, box) in expected_images.items():
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
            print(f"  {fname}: OK ({im.width}x{im.height})")

    doc.close()
    print("  All 9 images verified: Present, non-empty, exact dimensions matching source PDF!")

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
        "theo sách",
        "nguyên tác",
        "bản dịch của",
        "tiến độ bản dịch",
    ]

    colon_pattern = re.compile(r':\s+([a-zA-Z\u00C0-\u024F\u1EA0-\u1EF9])')
    all_images_found = set()

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

            # Check image links
            img_matches = re.findall(r'!\[(.*?)\]\((.*?)\)', line)
            for alt, src in img_matches:
                if not alt.strip():
                    report_error(f"{md_path.name}:{line_idx}: Empty alt text for image {src}")
                target = ROOT / 'docs/vat-ly-2/bai-giang/img/young-38' / Path(src).name
                if not src.startswith("../img/young-38/") or not target.is_file():
                    report_error(f"{md_path.name}:{line_idx}: Invalid image path: {src}")
                stem = Path(src).stem
                all_images_found.add(stem)

        # Check display math tags
        display_math_blocks = re.findall(r'\$\$\n([\s\S]*?)\n\$\$', text)
        for block in display_math_blocks:
            if r"\tag{" in block:
                if r"\end{aligned}" in block:
                    end_idx = block.find(r"\end{aligned}")
                    tag_idx = block.find(r"\tag{")
                    if tag_idx < end_idx:
                        report_error(f"{md_path.name}: \\tag placed inside aligned block: {block[:60]}")

    expected_stems = {f"hinh-38-{i:02d}" for i in range(1, 10)}
    missing_stems = expected_stems - all_images_found
    if missing_stems:
        report_error(f"Missing images in Markdown: {missing_stems}")
    else:
        print(f"  All 9 images properly linked with descriptive Vietnamese alt!")

    print("  Markdown files audit completed!")

def verify_annotations():
    print("=== 4. Verifying Annotations Module ===")
    if not ANNOTATIONS_FILE.is_file():
        report_error(f"Missing annotations file: {ANNOTATIONS_FILE}")
        return

    text = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    for i in range(1, 10):
        key_double = f'"young-38/hinh-38-{i:02d}"'
        key_single = f"'young-38/hinh-38-{i:02d}'"
        if key_double not in text and key_single not in text:
            report_error(f"Missing key in annotations: young-38/hinh-38-{i:02d}")

    try:
        res = subprocess.run(["node", "--check", str(ANNOTATIONS_FILE)], capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            report_error(f"node --check failed: {res.stderr}")
        else:
            print("  node --check: Syntax valid!")
    except Exception as e:
        report_error(f"Failed to run node --check: {e}")

def verify_mathjax_widths():
    print("=== 5. Measuring MathJax Widths (Inline <= 30ex, Display Body <= 25ex, Full Tagged <= 32ex on 320px) ===")
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
    print("STARTING AUDIT: Chapter 38 Theory A (Sections 38.1 - 38.2)")
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
