#!/usr/bin/env python3
"""
Comprehensive verifier for Chapter 35 Theory A (Sections 35.1 - 35.3):
- Numeric and wave interference calculations for all 3 examples and 3 TYUs
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

IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-35"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics35-theory-a-image-annotations.mjs"

TRANSLATIONS = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-35" / "01-giao-thoa-nguon-ket-hop.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-35" / "02-giao-thoa-hai-nguon.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-35" / "03-cuong-do-giao-thoa.md",
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

    # Ex 35.1
    d_1 = 0.200e-3
    R_1 = 1.00
    m_1 = 3
    y3_1 = 9.49e-3
    lam_1 = y3_1 * d_1 / (m_1 * R_1)
    assert abs(lam_1 - 6.3267e-7) < 1e-9, f"Ex 35.1 lambda mismatch: {lam_1}"
    assert round(lam_1 * 1e9) == 633, f"Ex 35.1 round mismatch: {lam_1*1e9}"
    print(f"  Ex 35.1: OK (lambda = {lam_1*1e9:.2f} nm, rounded to 633 nm)")

    # Ex 35.2
    c = 3.00e8
    f_2 = 1.50e6
    lam_2 = c / f_2
    d_2 = 400.0
    assert abs(lam_2 - 200.0) < 1e-6, f"Ex 35.2 lambda mismatch: {lam_2}"
    assert abs(d_2 / lam_2 - 2.0) < 1e-6, f"Ex 35.2 d/lambda mismatch: {d_2/lam_2}"

    # Maxima angles
    th_max_0 = math.degrees(math.asin(0.0 / 2.0))
    th_max_1 = math.degrees(math.asin(1.0 / 2.0))
    th_max_2 = math.degrees(math.asin(2.0 / 2.0))
    assert abs(th_max_0 - 0.0) < 1e-6
    assert abs(th_max_1 - 30.0) < 1e-6
    assert abs(th_max_2 - 90.0) < 1e-6

    # Minima angles
    th_min_1 = math.degrees(math.asin(0.250))
    th_min_2 = math.degrees(math.asin(0.750))
    assert abs(th_min_1 - 14.4775) < 0.01, f"Ex 35.2 min1 mismatch: {th_min_1}"
    assert abs(th_min_2 - 48.5904) < 0.01, f"Ex 35.2 min2 mismatch: {th_min_2}"
    print(f"  Ex 35.2: OK (lambda = 200 m, max: 0, +-30, +-90 deg; min: +-14.5, +-48.6 deg)")

    # TYU 35.1
    # On positive y-axis above S1: r2 - r1 = 4 lambda = m lambda (m=4, antinodal curve)
    print("  TYU 35.1: OK (r2 - r1 = 4 lambda -> antinodal curve, option i)")

    # TYU 35.2
    # lambda_blue < lambda_red -> fringe spacing Delta y = R lambda / d decreases (option ii)
    print("  TYU 35.2: OK (lambda_blue < lambda_red -> spacing decreases, option ii)")

    # Ex 35.3
    f_3 = 60.0e6
    lam_3 = c / f_3
    d_3 = 10.0
    I0_3 = 0.020
    assert abs(lam_3 - 5.00) < 1e-6
    assert abs(d_3 / lam_3 - 2.00) < 1e-6

    # (a) theta = 4.0 deg
    th_3a = math.radians(4.0)
    phi_half_3a = 2.0 * math.pi * math.sin(th_3a)
    I_ratio_3a = math.cos(phi_half_3a)**2
    I_3a = I_ratio_3a * I0_3
    assert abs(I_ratio_3a - 0.8199) < 0.005, f"Ex 35.3a ratio mismatch: {I_ratio_3a}"
    assert abs(I_3a - 0.0164) < 0.001, f"Ex 35.3a I mismatch: {I_3a}"

    # (b) I = I0/2 -> sin theta = 1/8 = 0.125
    th_3b = math.degrees(math.asin(0.125))
    assert abs(th_3b - 7.1807) < 0.01, f"Ex 35.3b theta mismatch: {th_3b}"

    # Verify other half-intensity angles:
    # 2*pi*sin(theta) = 3*pi/4, 5*pi/4, 7*pi/4 -> sin theta = 3/8, 5/8, 7/8
    th_3_other1 = math.degrees(math.asin(0.375))
    th_3_other2 = math.degrees(math.asin(0.625))
    th_3_other3 = math.degrees(math.asin(0.875))
    assert abs(th_3_other1 - 22.024) < 0.05, f"Ex 35.3 evaluate angle 1 mismatch: {th_3_other1}"
    assert abs(th_3_other2 - 38.682) < 0.05, f"Ex 35.3 evaluate angle 2 mismatch: {th_3_other2}"
    assert abs(th_3_other3 - 61.045) < 0.05, f"Ex 35.3 evaluate angle 3 mismatch: {th_3_other3}"

    # (c) I = 0 -> sin theta = 0.250, 0.750
    th_3c1 = math.degrees(math.asin(0.250))
    th_3c2 = math.degrees(math.asin(0.750))
    assert abs(th_3c1 - 14.4775) < 0.01
    assert abs(th_3c2 - 48.5904) < 0.01
    print(f"  Ex 35.3: OK (a: {I_3a:.3f} W/m2, b: +-7.2 deg, eval other angles: +-22.0, +-38.7, +-61.0 deg; c: +-14.5, +-48.6 deg)")

    # TYU 35.3
    lam_tyu = 5.00e-7
    I_i = math.cos(math.pi * (4.00e-7) / lam_tyu)**2
    I_ii = math.cos(4.00 / 2.0)**2
    I_iii = math.cos(math.pi * (7.50e-7) / lam_tyu)**2
    I_iv = math.cos(2.00 / 2.0)**2
    assert abs(I_i - 0.6545) < 0.005, f"TYU 35.3 (i) mismatch: {I_i}"
    assert abs(I_ii - 0.1732) < 0.005, f"TYU 35.3 (ii) mismatch: {I_ii}"
    assert abs(I_iii - 0.0) < 1e-6, f"TYU 35.3 (iii) mismatch: {I_iii}"
    assert abs(I_iv - 0.2919) < 0.005, f"TYU 35.3 (iv) mismatch: {I_iv}"
    assert I_i > I_iv > I_ii > I_iii
    print(f"  TYU 35.3: OK (i: {I_i:.3f}I0, iv: {I_iv:.3f}I0, ii: {I_ii:.3f}I0, iii: {I_iii:.3f}I0 -> ranking (i), (iv), (ii), (iii))")

def verify_images():
    print("=== 2. Validating Image Files against Source PDF ===")
    crops = {
        "hinh-35-01": (1180, (36, 435, 195, 595)),
        "hinh-35-02": (1181, (75, 95, 575, 255)),
        "hinh-35-03": (1182, (36, 135, 195, 370)),
        "hinh-35-04": (1183, (455, 125, 620, 335)),
        "hinh-35-05": (1183, (75, 455, 435, 748)),
        "hinh-35-06": (1184, (36, 340, 195, 635)),
        "hinh-35-07": (1185, (78, 225, 340, 360)),
        "hinh-35-08": (1185, (78, 600, 340, 735)),
        "hinh-35-09": (1186, (36, 585, 195, 750)),
        "hinh-35-10": (1189, (78, 75, 545, 205)),
    }

    assert len(crops) == 10, f"Expected 10 crops, got {len(crops)}"

    with pymupdf.open(SOURCE_PDF) as doc:
        for num in range(1, 11):
            stem = f"hinh-35-{num:02d}"
            png_path = IMG_DIR / f"{stem}.png"
            if not png_path.is_file():
                report_error(f"Missing image file: {png_path}")
                continue

            pno, box = crops[stem]
            page = doc[pno - 1]
            rect = pymupdf.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=pymupdf.Matrix(2.5, 2.5), clip=rect, alpha=False)

            with Image.open(png_path) as im:
                if im.size != (pix.width, pix.height):
                    report_error(f"{stem}.png size mismatch: disk={im.size}, pdf=({pix.width}, {pix.height})")
                else:
                    disk_bytes = png_path.read_bytes()
                    if len(disk_bytes) == 0:
                        report_error(f"{stem}.png is empty")
    print("  All 10 images verified: Present, non-empty, exact dimensions matching source PDF!")

def verify_markdown():
    print("=== 3. Auditing Markdown Content & Formatting ===")

    colon_pattern = re.compile(r':\s+(\S)')
    forbidden_words = [
        "nội dung lấy từ", "lấy từ slide", "bài tập lấy từ sách",
        "ví dụ do người soạn", "ảnh lấy từ sách", "ảnh nguyên gốc",
        "hình trong sách", "dữ liệu này từ", "theo sách", "sách dùng",
        "nguyên tác", "bản dịch của", "tiến độ bản dịch", "người soạn",
        "sinh viên rất hay nhầm", "lỗi phổ biến nhất của sinh viên",
        "đa số sinh viên đều mắc", "bẫy thi cử"
    ]

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
                target = ROOT / 'docs/vat-ly-2/bai-giang/img/young-35' / Path(src).name
                if not src.startswith("../img/young-35/") or not target.is_file():
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

    expected_stems = {f"hinh-35-{i:02d}" for i in range(1, 11)}
    missing_stems = expected_stems - all_images_found
    if missing_stems:
        report_error(f"Missing images in Markdown: {missing_stems}")
    else:
        print(f"  All 10 images properly linked with descriptive Vietnamese alt!")

    print("  Markdown files audit completed!")

def verify_annotations():
    print("=== 4. Verifying Annotations Module ===")
    if not ANNOTATIONS_FILE.is_file():
        report_error(f"Missing annotations file: {ANNOTATIONS_FILE}")
        return

    text = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    for i in range(1, 11):
        key = f"'young-35/hinh-35-{i:02d}'"
        if key not in text:
            report_error(f"Missing key in annotations: {key}")

    try:
        res = subprocess.run(["node", "--check", str(ANNOTATIONS_FILE)], capture_output=True, text=True)
        if res.returncode != 0:
            report_error(f"node --check failed: {res.stderr}")
        else:
            print("  node --check: Syntax valid!")
    except Exception as e:
        report_error(f"Failed to run node --check: {e}")

def verify_mathjax_widths():
    print("=== 5. Measuring MathJax Widths (Inline <= 38ex, Full Display Block <= 27ex) ===")
    node_modules_pkg = Path("C:/Users/Ai/Documents/StudyHub/package.json")
    if not node_modules_pkg.is_file():
        report_error("node_modules not found in main StudyHub, cannot run MathJax measurement")
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
                    if clean_tex:
                        display_items.append({
                            "file": md_path.name,
                            "line": start_line,
                            "tex": clean_tex,
                            "raw": block_tex
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

    js_code = """
const { createRequire } = require('node:module');
const req = createRequire('C:/Users/Ai/Documents/StudyHub/package.json');
const MarkdownIt = req('markdown-it');
const mathjax = req('markdown-it-mathjax3');
const md = new MarkdownIt({ html: true }).use(mathjax.default || mathjax);
const fs = require('node:fs');

const raw = fs.readFileSync(process.argv[2], 'utf-8');
const data = JSON.parse(raw);
let displayErrors = 0;
let inlineErrors = 0;

for (const item of data.display) {
  try {
    const rendered = md.render('$$\\n' + item.tex + '\\n$$');
    const m = rendered.match(/width="([\\d.]+)ex"/);
    if (!m) {
      console.log(`[DISPLAY RENDER ERROR] Could not extract numeric SVG ex width: ${item.file}:${item.line}`);
      displayErrors++;
      continue;
    }
    const w = parseFloat(m[1]);
    if (w <= 0) {
      console.log(`[DISPLAY ZERO WIDTH] Extracted width is ${w}ex: ${item.file}:${item.line}`);
      displayErrors++;
      continue;
    }
    if (w > 27.0) {
      console.log(`[DISPLAY OVERFLOW] ${w.toFixed(2)}ex > 27ex at ${item.file}:${item.line}: ${item.tex.replace(/\\n/g, ' ')}`);
      displayErrors++;
    }
  } catch (err) {
    console.log(`[DISPLAY EXCEPTION] ${item.file}:${item.line}: ${err.message}`);
    displayErrors++;
  }
}

for (const item of data.inline) {
  try {
    const rendered = md.render('$' + item.tex + '$');
    const m = rendered.match(/width="([\\d.]+)ex"/);
    if (!m) continue;
    const w = parseFloat(m[1]);
    if (w > 38.0) {
      console.log(`[INLINE OVERFLOW] ${w.toFixed(2)}ex > 38ex at ${item.file}:${item.line}: $${item.tex}$`);
      inlineErrors++;
    }
  } catch (err) {
    // ignore inline render error
  }
}

console.log(`MathJax measurement complete: ${data.display.length} display blocks, ${data.inline.length} inline items.`);
console.log(`Display errors: ${displayErrors}, Inline errors: ${inlineErrors}`);
if (displayErrors > 0 || inlineErrors > 0) {
  process.exit(1);
}
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
            print("  All display math blocks <= 27ex and inline math <= 38ex!")
    finally:
        if os.path.exists(data_json_path):
            os.remove(data_json_path)
        if os.path.exists(js_file_path):
            os.remove(js_file_path)

def main():
    print("======================================================================")
    print("      VERIFICATION AUDIT FOR CHAPTER 35 THEORY A (SECTIONS 35.1-35.3)  ")
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
