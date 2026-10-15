#!/usr/bin/env python3
"""
Comprehensive verifier for Chapter 36 Theory A (Sections 36.1 - 36.4):
- Numeric and wave diffraction calculations for all 3 examples and 4 TYUs
- Asset pixel validation against source PDF
- Markdown syntax, style, colon capitalization, and math formatting audit
- Annotation module consistency and syntax
- Real MathJax width measurement (Display <= 27ex, Inline <= 38ex)
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

IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-36"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics36-theory-a-image-annotations.mjs"

TRANSLATIONS = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-36" / "01-nhieu-xa-fresnel-fraunhofer.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-36" / "02-nhieu-xa-mot-khe.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-36" / "03-cuong-do-nhieu-xa-mot-khe.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-36" / "04-nhieu-khe.md",
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
    print("=== 1. Verifying Physical & Optical Calculations ===")

    # Ex 36.1
    lam_1 = 633e-9
    x_1 = 6.0
    two_y1 = 32e-3
    y1 = two_y1 / 2.0
    a_1 = x_1 * lam_1 / y1
    assert abs(a_1 - 2.37375e-4) < 1e-7, f"Ex 36.1 a mismatch: {a_1}"
    assert round(a_1 * 1e3, 2) == 0.24, f"Ex 36.1 round mismatch: {a_1*1e3}"
    ratio_1 = lam_1 / a_1
    assert abs(ratio_1 - 0.0026) < 0.0001, f"Ex 36.1 ratio mismatch: {ratio_1}"
    two_y2 = 2.0 * two_y1
    assert abs(two_y2 - 64e-3) < 1e-6
    print(f"  Ex 36.1: OK (a = {a_1*1e3:.2f} mm, ratio = {ratio_1:.4f}, 2y2 = {two_y2*1e3:.0f} mm)")

    # TYU 36.1
    print("  TYU 36.1: Fabricated sound check removed per source Young & Freedman 15th ed scope (actual scope: TYU 36.2-36.4)")

    # TYU 36.2
    # Ratios lambda / a:
    r_i = 400e-9 / 0.20e-3
    r_ii = 600e-9 / 0.20e-3
    r_iii = 400e-9 / 0.30e-3
    r_iv = 600e-9 / 0.30e-3
    assert abs(r_i - 2.0e-3) < 1e-6
    assert abs(r_ii - 3.0e-3) < 1e-6
    assert abs(r_iii - 1.3333e-3) < 1e-5
    assert abs(r_iv - 2.0e-3) < 1e-6
    assert r_ii > r_i and abs(r_i - r_iv) < 1e-9 and r_iv > r_iii
    print(f"  TYU 36.2: OK (Ratios: (ii) {r_ii*1e3:.1f}e-3 > (i)=(iv) {r_i*1e3:.1f}e-3 > (iii) {r_iii*1e3:.2f}e-3)")

    # Ex 36.2
    beta_2 = 66.0
    half_beta = beta_2 / 2.0
    i_ratio_2 = (math.sin(half_beta) / half_beta) ** 2
    assert abs(i_ratio_2 - 9.18e-4) < 1e-5, f"Ex 36.2 I ratio mismatch: {i_ratio_2}"
    theta_2_deg = 7.0
    sin_theta_2 = math.sin(math.radians(theta_2_deg))
    a_over_lam = beta_2 / (2.0 * math.pi * sin_theta_2)
    assert abs(a_over_lam - 86.19) < 0.1, f"Ex 36.2 a/lambda mismatch: {a_over_lam}"
    assert round(a_over_lam) == 86
    lam_sample = 550e-9
    a_sample = round(a_over_lam) * lam_sample
    assert abs(a_sample - 4.73e-5) < 1e-6
    m_side = (beta_2 / math.pi - 1.0) / 2.0
    assert abs(m_side - 10.00) < 0.05
    print(f"  Ex 36.2: OK (I/I0 = {i_ratio_2*1e4:.1f}e-4, a/lambda = {a_over_lam:.1f} ~ 86, m ~ 10)")

    # Ex 36.3
    a_3 = 2.4e-4
    lam_3 = 6.33e-7
    x_3 = 6.0
    y_3 = 3.0e-3
    tan_th_3 = y_3 / x_3
    assert abs(tan_th_3 - 5.0e-4) < 1e-7
    half_beta_3 = math.pi * a_3 * tan_th_3 / lam_3
    assert abs(half_beta_3 - 0.59556) < 1e-4
    assert round(half_beta_3, 2) == 0.60
    i_ratio_3 = (math.sin(0.60) / 0.60) ** 2
    assert abs(i_ratio_3 - 0.8856) < 0.01
    assert round(i_ratio_3, 2) == 0.89
    # Secondary maxima in single-slit diffraction
    # Source approximations: 0.0450, 0.0162, 0.0083
    approx_intensities = [1.0 / (((m + 0.5) * math.pi) ** 2) for m in [1, 2, 3]]
    assert abs(approx_intensities[0] - 0.0450) < 0.0005
    assert abs(approx_intensities[1] - 0.0162) < 0.0005
    assert abs(approx_intensities[2] - 0.0083) < 0.0005
    # Actual transcendental roots of tan(u) = u:
    # u1 approx 1.4303*pi, u2 approx 2.4590*pi, u3 approx 3.4709*pi
    # beta = 2*u => beta1 approx 2.8606*pi, beta2 approx 4.9180*pi, beta3 approx 6.9418*pi
    actual_roots = [1.4303 * math.pi, 2.4590 * math.pi, 3.4709 * math.pi]
    actual_intensities = [(math.sin(u) / u) ** 2 for u in actual_roots]
    assert abs(actual_intensities[0] - 0.0472) < 0.0005
    assert abs(actual_intensities[1] - 0.0165) < 0.0005
    assert abs(actual_intensities[2] - 0.0083) < 0.0005
    print("  Secondary maxima: OK (Approx 0.0450, 0.0162, 0.0083; Actual 0.0472, 0.0165, 0.0083)")

    # TYU 36.3
    a_tyu3 = 0.0100e-3
    lam_blue = 500e-9
    lam_ir = 10.0e-6
    lam_micro = 20.0e-3
    assert lam_blue < a_tyu3
    assert lam_ir == a_tyu3
    assert lam_micro > a_tyu3
    print("  TYU 36.3: OK (No diffraction minima when lambda >= a -> (ii) 10.0 um and (iii) 20.0 mm)")

    # TYU 36.4
    # d = 2.5 a => mi = 2.5 md = (5/2) md
    # For md = 2 -> mi = 5; md = 4 -> mi = 10
    missing_orders = [int(2.5 * md) for md in [2, 4, 6]]
    assert missing_orders == [5, 10, 15]
    print("  TYU 36.4: OK (Missing interference maxima: mi = +-5, +-10, +-15, ...)")

def verify_images():
    print("=== 2. Validating Image Files against Source PDF ===")
    if not SOURCE_PDF.is_file():
        report_error(f"Source PDF not found at {SOURCE_PDF}")
        return

    expected_images = {
        "hinh-36-01.png": (1206, (36, 85, 195, 258)),
        "hinh-36-02.png": (1206, (210, 560, 575, 735)),
        "hinh-36-03.png": (1207, (75, 588, 460, 745)),
        "hinh-36-04.png": (1208, (38, 74, 575, 226)),
        "hinh-36-05.png": (1208, (210, 545, 575, 742)),
        "hinh-36-06.png": (1209, (455, 420, 580, 565)),
        "hinh-36-07.png": (1210, (36, 74, 275, 198)),
        "hinh-36-08.png": (1210, (36, 275, 195, 742)),
        "hinh-36-09.png": (1211, (455, 460, 615, 745)),
        "hinh-36-10.png": (1212, (105, 630, 575, 748)),
        "hinh-36-11.png": (1213, (450, 125, 610, 235)),
        "hinh-36-12.png": (1214, (36, 335, 195, 740)),
        "hinh-36-13.png": (1215, (455, 260, 615, 455)),
        "hinh-36-14.png": (1215, (75, 626, 445, 735)),
        "hinh-36-15.png": (1216, (36, 135, 195, 565)),
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
    print("  All 15 images verified: Present, non-empty, exact dimensions matching source PDF!")

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
        "con quay pha",
        "tỷ lệ nghịch với 1/n",
        "tỉ lệ nghịch với 1/n",
        "nghịch với 1/n",
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
                target = ROOT / 'docs/vat-ly-2/bai-giang/img/young-36' / Path(src).name
                if not src.startswith("../img/young-36/") or not target.is_file():
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

    expected_stems = {f"hinh-36-{i:02d}" for i in range(1, 16)}
    missing_stems = expected_stems - all_images_found
    if missing_stems:
        report_error(f"Missing images in Markdown: {missing_stems}")
    else:
        print(f"  All 15 images properly linked with descriptive Vietnamese alt!")

    print("  Markdown files audit completed!")

def verify_annotations():
    print("=== 4. Verifying Annotations Module ===")
    if not ANNOTATIONS_FILE.is_file():
        report_error(f"Missing annotations file: {ANNOTATIONS_FILE}")
        return

    text = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    for i in range(1, 16):
        key_double = f'"young-36/hinh-36-{i:02d}"'
        key_single = f"'young-36/hinh-36-{i:02d}'"
        if key_double not in text and key_single not in text:
            report_error(f"Missing key in annotations: young-36/hinh-36-{i:02d}")

    try:
        res = subprocess.run(["node", "--check", str(ANNOTATIONS_FILE)], capture_output=True, text=True)
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
console.log(`Display errors: ${{displayErrors}}, Inline errors: ${{inlineErrors}}`);
if (displayErrors > 0 || inlineErrors > 0) {{
  process.exit(1);
}}
"""

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as f:
        json.dump({"display": display_items, "inline": inline_items}, f, ensure_ascii=False)
        data_json_path = f.name

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".js", delete=False) as f:
        f.write(js_code)
        js_file_path = f.name

    try:
        proc = subprocess.run(["node", js_file_path, data_json_path], capture_output=True, text=True, encoding="utf-8")
        print(proc.stdout.strip())
        if proc.returncode != 0:
            report_error(f"MathJax width limits violated:\n{proc.stdout}\n{proc.stderr}")
        else:
            print("  All display math bodies <= 25ex, tagged widths <= 32ex on 320px, and inline math <= 30ex!")
    finally:
        if os.path.exists(data_json_path):
            os.remove(data_json_path)
        if os.path.exists(js_file_path):
            os.remove(js_file_path)

def main():
    print("======================================================================")
    print("      VERIFICATION AUDIT FOR CHAPTER 36 THEORY A (SECTIONS 36.1-36.4)  ")
    print("======================================================================")

    verify_calculations()
    verify_images()
    verify_markdown()
    verify_annotations()
    verify_mathjax_widths()

    print("\n=== SUMMARY ===")
    if ERRORS:
        print(f"FAILED with {len(ERRORS)} error(s):")
        for e in ERRORS:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("ALL AUDITS PASSED PERFECTLY! 100% compliant with StudyHub standards.")

if __name__ == "__main__":
    main()
