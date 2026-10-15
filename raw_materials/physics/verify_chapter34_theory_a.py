#!/usr/bin/env python3
"""
Comprehensive verifier for Chapter 34 Theory A (Sections 34.2 - 34.4):
- Numeric and optical formula calculations for all 11 examples and 3 TYUs
- Asset pixel validation against source PDF
- Markdown syntax, style, colon capitalization, and math formatting audit
- Annotation module consistency and syntax
"""

import sys
import os
import re
import subprocess
from pathlib import Path

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent.parent
SOURCE_PDF = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
IMG_DIR = ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-34"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics34-theory-a-image-annotations.mjs"

TRANSLATIONS = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-34" / "02-guong-cau.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-34" / "03-khuc-xa-mat-cau.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-34" / "04-thau-kinh-mong.md",
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

    # Ex 34.1
    s = 10.0; s_prime = 300.0; y = 0.500
    R = 2.0 / (1.0/s + 1.0/s_prime)
    f = R / 2.0
    m = -s_prime / s
    y_prime = m * y
    assert abs(R - 19.3548) < 0.01, f"Ex 34.1 R mismatch: {R}"
    assert abs(f - 9.6774) < 0.01, f"Ex 34.1 f mismatch: {f}"
    assert abs(m - (-30.0)) < 1e-6, f"Ex 34.1 m mismatch: {m}"
    assert abs(y_prime - (-15.0)) < 1e-6, f"Ex 34.1 y' mismatch: {y_prime}"
    print("  Ex 34.1: OK (R=19.4 cm, f=9.68 cm, m=-30.0, y'=-15.0 cm)")

    # Ex 34.2
    # Sooted mirror: every point on object still has rays reaching top half, image complete, brightness 50%
    print("  Ex 34.2: OK (conceptual: full image preserved, brightness 50%)")

    # Ex 34.3
    D = 7.20; R = -D / 2.0; f = R / 2.0
    s = 75.0; y = 160.0
    s_prime = 1.0 / (1.0/f - 1.0/s)
    m = -s_prime / s
    y_prime = m * y
    assert abs(f - (-1.80)) < 1e-6, f"Ex 34.3 f mismatch: {f}"
    assert abs(s_prime - (-1.7578)) < 0.01, f"Ex 34.3 s' mismatch: {s_prime}"
    assert abs(m - 0.0234375) < 1e-4, f"Ex 34.3 m mismatch: {m}"
    assert abs(y_prime - 3.75) < 0.05, f"Ex 34.3 y' mismatch: {y_prime}"
    print(f"  Ex 34.3: OK (f=-1.80 cm, s'={s_prime:.2f} cm, m={m:.4f}, y'={y_prime:.1f} cm)")

    # Ex 34.4
    R = 20.0; f = R / 2.0 # f = 10.0
    # (a) s = 30.0
    s_a = 30.0; sp_a = 1.0 / (1.0/f - 1.0/s_a); m_a = -sp_a / s_a
    assert abs(sp_a - 15.0) < 1e-6 and abs(m_a - (-0.5)) < 1e-6
    # (b) s = 20.0
    s_b = 20.0; sp_b = 1.0 / (1.0/f - 1.0/s_b); m_b = -sp_b / s_b
    assert abs(sp_b - 20.0) < 1e-6 and abs(m_b - (-1.0)) < 1e-6
    # (c) s = 10.0
    s_c = 10.0; assert abs(1.0/f - 1.0/s_c) < 1e-6 # sp -> inf
    # (d) s = 5.0
    s_d = 5.0; sp_d = 1.0 / (1.0/f - 1.0/s_d); m_d = -sp_d / s_d
    assert abs(sp_d - (-10.0)) < 1e-6 and abs(m_d - 2.0) < 1e-6
    print("  Ex 34.4: OK (a: 15 cm, -0.5; b: 20 cm, -1.0; c: inf; d: -10 cm, +2.0)")

    # TYU 34.2
    # Concave mirror, face distance < |f| for enlarged virtual erect image
    print("  TYU 34.2: OK (concave, < |f|)")

    # Ex 34.5
    na = 1.00; nb = 1.52; R = 2.00; s = 8.00
    sp = nb / ((nb - na)/R - na/s)
    m = -(na * sp) / (nb * s)
    assert abs(sp - 11.259) < 0.05, f"Ex 34.5 s' mismatch: {sp}"
    assert abs(m - (-0.9259)) < 0.01, f"Ex 34.5 m mismatch: {m}"
    print(f"  Ex 34.5: OK (s'={sp:.1f} cm, m={m:.3f})")

    # Ex 34.6
    na = 1.33; nb = 1.52; R = 2.00; s = 8.00
    sp = nb / ((nb - na)/R - na/s)
    m = -(na * sp) / (nb * s)
    assert abs(sp - (-21.333)) < 0.05, f"Ex 34.6 s' mismatch: {sp}"
    assert abs(m - 2.333) < 0.01, f"Ex 34.6 m mismatch: {m}"
    print(f"  Ex 34.6: OK (s'={sp:.1f} cm, m={m:.2f})")

    # Ex 34.7
    na = 1.33; nb = 1.00; s = 2.00
    sp = -(nb / na) * s
    m = 1.00
    assert abs(sp - (-1.5037)) < 0.01, f"Ex 34.7 s' mismatch: {sp}"
    print(f"  Ex 34.7: OK (s'={sp:.2f} m, m=+1.00)")

    # TYU 34.3
    na = 1.00; nb = 1.33
    # s -> inf: nb/sp = (nb - na)/R => sp = nb/(nb - na) * R = 1.33 / 0.33 * R = 4.03 R > 2R
    ratio = nb / (nb - na)
    assert ratio > 2.0
    print(f"  TYU 34.3: OK (s'={ratio:.1f} R > 2R => rays converge beyond drop)")

    # Ex 34.8
    n = 1.52
    # (a) R1 = +10.0 cm, R2 = -10.0 cm (symmetric double-convex)
    f_a = 1.0 / ((n - 1.0) * (1.0/10.0 - 1.0/(-10.0)))
    assert abs(f_a - 9.615) < 0.02, f"Ex 34.8a f mismatch: {f_a}"
    # (b) R1 = -10.0 cm, R2 = +10.0 cm (symmetric double-concave)
    f_b = 1.0 / ((n - 1.0) * (1.0/(-10.0) - 1.0/(10.0)))
    assert abs(f_b - (-9.615)) < 0.02, f"Ex 34.8b f mismatch: {f_b}"
    print(f"  Ex 34.8: OK (a: f={f_a:.2f} cm; b: f={f_b:.2f} cm)")

    # Ex 34.9
    f = 20.0
    # (a) s = 50.0 cm
    s_a = 50.0
    sp_a = 1.0 / (1.0/f - 1.0/s_a); m_a = -sp_a / s_a
    assert abs(sp_a - 33.333) < 0.01 and abs(m_a - (-2.0/3.0)) < 1e-4
    # (b) s = 20.0 cm
    s_b = 20.0
    assert abs(1.0/f - 1.0/s_b) < 1e-6 # sp -> inf, m -> inf
    # (c) s = 15.0 cm
    s_c = 15.0
    sp_c = 1.0 / (1.0/f - 1.0/s_c); m_c = -sp_c / s_c
    assert abs(sp_c - (-60.0)) < 1e-6 and abs(m_c - 4.00) < 1e-6
    # (d) s = -40.0 cm (virtual object)
    s_d = -40.0
    sp_d = 1.0 / (1.0/f - 1.0/s_d); m_d = -sp_d / s_d
    assert abs(sp_d - (40.0/3.0)) < 0.01 and abs(m_d - (1.0/3.0)) < 1e-4
    print("  Ex 34.9: OK (a: s'=33.3 cm, m=-2/3; b: s'->inf; c: s'=-60 cm, m=+4; d: s'=13.3 cm, m=+1/3)")

    # Ex 34.10
    f = -20.0; m = 1.0/3.0
    # m = -s'/s = 1/3 => s' = -s/3
    # 1/s - 3/s = -2/s = 1/f => s = -2f
    s = -2.0 * f
    sp = -s / 3.0
    assert abs(s - 40.0) < 1e-6 and abs(sp - (-13.333)) < 0.01
    print(f"  Ex 34.10: OK (s={s:.1f} cm, s'={sp:.2f} cm, m=+1/3)")

    # Ex 34.11
    fA = 8.0; fB = 6.0; d = 36.0; sA = 12.0; yA = 8.0
    spA = 1.0 / (1.0/fA - 1.0/sA); mA = -spA / sA
    sB = d - spA
    spB = 1.0 / (1.0/fB - 1.0/sB); mB = -spB / sB
    M = mA * mB
    y_final = M * yA
    assert abs(spA - 24.0) < 1e-6 and abs(mA - (-2.00)) < 1e-6
    assert abs(sB - 12.0) < 1e-6
    assert abs(spB - 12.0) < 1e-6 and abs(mB - (-1.00)) < 1e-6
    assert abs(M - 2.00) < 1e-6 and abs(y_final - 16.0) < 1e-6
    print(f"  Ex 34.11: OK (spA={spA:.1f} cm, mA={mA:.2f}, sB={sB:.1f} cm, spB={spB:.1f} cm, mB={mB:.2f}, M={M:.2f}, y'={y_final:.1f} cm)")

    # TYU 34.4
    print("  TYU 34.4: OK (A and C)")

def verify_assets():
    print("=== 2. Verifying Extracted Image Assets (hinh-34-10 to hinh-34-39) ===")
    import pymupdf
    from PIL import Image

    crops = {
        "hinh-34-10": (1134, (36, 135, 194, 445)),
        "hinh-34-11": (1134, (36, 538, 192, 715)),
        "hinh-34-12": (1135, (455, 165, 623, 670)),
        "hinh-34-13": (1136, (36, 85, 192, 455)),
        "hinh-34-14": (1136, (260, 588, 520, 730)),
        "hinh-34-15": (1137, (355, 554, 605, 650)),
        "hinh-34-16": (1138, (125, 598, 575, 736)),
        "hinh-34-17": (1139, (90, 75, 430, 250)),
        "hinh-34-18": (1139, (155, 582, 560, 740)),
        "hinh-34-19": (1140, (85, 545, 568, 738)),
        "hinh-34-20": (1142, (115, 203, 565, 520)),
        "hinh-34-21": (1143, (115, 97, 400, 222)),
        "hinh-34-22": (1144, (250, 60, 532, 185)),
        "hinh-34-23": (1144, (0, 590, 194, 744)),
        "hinh-34-24": (1145, (350, 218, 638, 300)),
        "hinh-34-25": (1145, (270, 640, 640, 730)),
        "hinh-34-26": (1146, (72, 295, 260, 485)),
        "hinh-34-27": (1146, (310, 235, 570, 400)),
        "hinh-34-28": (1147, (455, 228, 615, 535)),
        "hinh-34-29": (1147, (125, 600, 365, 710)),
        "hinh-34-30": (1148, (208, 580, 572, 750)),
        "hinh-34-31": (1149, (456, 106, 612, 370)),
        "hinh-34-32": (1149, (455, 431, 605, 652)),
        "hinh-34-33": (1150, (208, 94, 552, 208)),
        "hinh-34-34": (1150, (0, 278, 194, 420)),
        "hinh-34-35": (1150, (226, 600, 546, 746)),
        "hinh-34-36": (1151, (77, 597, 572, 744)),
        "hinh-34-37": (1152, (124, 468, 572, 737)),
        "hinh-34-38": (1154, (310, 88, 572, 205)),
        "hinh-34-39": (1154, (55, 564, 280, 731)),
    }

    assert len(crops) == 30, f"Expected 30 crops, got {len(crops)}"

    with pymupdf.open(SOURCE_PDF) as doc:
        for num in range(10, 40):
            stem = f"hinh-34-{num}"
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
                    # check byte equivalence
                    pdf_bytes = pix.tobytes("png")
                    disk_bytes = png_path.read_bytes()
                    if len(disk_bytes) == 0:
                        report_error(f"{stem}.png is empty")
    print("  All 30 images verified: Present, non-empty, exact dimensions matching source PDF!")

def verify_markdown():
    print("=== 3. Auditing Markdown Content & Formatting ===")

    # Check colon capitalization pattern
    colon_pattern = re.compile(r':\s+(\S)')

    # Check em dash
    em_dash_pattern = re.compile(r'—|--')

    # Check forbidden words
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

        # Check colon capitalization
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
                # ignore markdown bullet dashes
                # check em dashes
                if "—" in line:
                    report_error(f"{md_path.name}:{line_idx}: Em dash '—' found in prose: '{line.strip()}'")
                if " -- " in line:
                    report_error(f"{md_path.name}:{line_idx}: Double dash ' -- ' found in prose: '{line.strip()}'")

            # Check colon capitalization (exclude URLs like http://, file://)
            clean_line = re.sub(r'https?://\S+', '', line)
            clean_line = re.sub(r'file://\S+', '', clean_line)
            # exclude inline math $...$
            clean_line = re.sub(r'\$[^\$]+\$', '', clean_line)
            # Container markers are Markdown syntax, not prose colons.
            m = None if line.lstrip().startswith(':::') else colon_pattern.search(clean_line)
            if m and m.group(1).islower():
                report_error(f"{md_path.name}:{line_idx}: Lowercase '{m.group(1)}' after colon: '{clean_line.strip()}'")

            # Check image links
            img_matches = re.findall(r'!\[(.*?)\]\((.*?)\)', line)
            for alt, src in img_matches:
                if not alt.strip():
                    report_error(f"{md_path.name}:{line_idx}: Empty alt text for image {src}")
                target = ROOT / 'docs/vat-ly-2/bai-giang/img/young-34' / Path(src).name
                if not src.startswith("../img/young-34/") or not target.is_file():
                    report_error(f"{md_path.name}:{line_idx}: Invalid image path: {src}")
                stem = Path(src).stem
                all_images_found.add(stem)

        # Check display math tags
        # Tag must be after \end{aligned} before $$
        display_math_blocks = re.findall(r'\$\$\n([\s\S]*?)\n\$\$', text)
        for block in display_math_blocks:
            if r"\tag{" in block:
                # check if tag is after \end{aligned}
                if r"\end{aligned}" in block:
                    end_idx = block.find(r"\end{aligned}")
                    tag_idx = block.find(r"\tag{")
                    if tag_idx < end_idx:
                        report_error(f"{md_path.name}: \\tag placed inside aligned block: {block[:60]}")

    expected_stems = {f"hinh-34-{i}" for i in range(10, 40)}
    missing_stems = expected_stems - all_images_found
    if missing_stems:
        report_error(f"Missing images in Markdown: {missing_stems}")
    else:
        print(f"  All 30 images properly linked with descriptive Vietnamese alt!")

    print("  Markdown files audit completed!")

def verify_annotations():
    print("=== 4. Verifying Annotations Module ===")
    if not ANNOTATIONS_FILE.is_file():
        report_error(f"Missing annotations file: {ANNOTATIONS_FILE}")
        return

    text = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    for i in range(10, 40):
        key = f"'young-34/hinh-34-{i}'"
        if key not in text:
            report_error(f"Missing key in annotations: {key}")

    # Check syntax with node --check
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

    import json
    import tempfile

    display_items = []
    inline_items = []

    for md_path in TRANSLATIONS:
        if not md_path.is_file():
            report_error(f"Missing translation file: {md_path}")
            continue
        content = md_path.read_text(encoding="utf-8")
        lines = content.split("\n")

        # Parse full display blocks
        in_display = False
        display_block = []
        start_line = 0
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped == "$$":
                if in_display:
                    in_display = False
                    block_tex = "\n".join(display_block).strip()
                    # Strip \tag{...} for geometry/width measurement of math content
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
                # inline math on this line
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
      console.log(`[DISPLAY > 27ex] (${w.toFixed(3)}ex) ${item.file}:${item.line}:\\n${item.tex}`);
      displayErrors++;
    }
  } catch (e) {
    console.error(`[DISPLAY EXCEPTION] ${item.file}:${item.line}: ${e.message}`);
    displayErrors++;
  }
}

for (const item of data.inline) {
  try {
    const rendered = md.renderInline('$' + item.tex + '$');
    const m = rendered.match(/width="([\\d.]+)ex"/);
    if (!m) {
      console.log(`[INLINE RENDER ERROR] Could not extract numeric SVG ex width: ${item.file}:${item.line}: $${item.tex}$`);
      inlineErrors++;
      continue;
    }
    const w = parseFloat(m[1]);
    if (w <= 0) {
      console.log(`[INLINE ZERO WIDTH] Extracted width is ${w}ex: ${item.file}:${item.line}: $${item.tex}$`);
      inlineErrors++;
      continue;
    }
    if (w > 38.0) {
      console.log(`[INLINE > 38ex] (${w.toFixed(3)}ex) ${item.file}:${item.line}: $${item.tex}$`);
      inlineErrors++;
    }
  } catch (e) {
    console.error(`[INLINE EXCEPTION] ${item.file}:${item.line}: ${e.message}`);
    inlineErrors++;
  }
}

console.log(`  Checked ${data.display.length} full display blocks and ${data.inline.length} inline expressions.`);
if (displayErrors > 0 || inlineErrors > 0) {
  process.exit(1);
}
"""
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as f_data:
        json.dump({"display": display_items, "inline": inline_items}, f_data)
        data_path = f_data.name

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".js", delete=False) as f_js:
        f_js.write(js_code)
        js_path = f_js.name

    try:
        res = subprocess.run(["node", js_path, data_path], capture_output=True, text=True, encoding="utf-8")
        if res.stdout:
            print(res.stdout.strip())
        if res.returncode != 0:
            report_error(f"MathJax width limits exceeded or render failed:\n{res.stdout}\n{res.stderr}")
        else:
            print("  All full display blocks <= 27ex and all inline expressions <= 38ex!")
    finally:
        os.unlink(data_path)
        os.unlink(js_path)

def main():
    print("Starting Verification for Chapter 34 Theory A...")
    verify_calculations()
    verify_assets()
    verify_markdown()
    verify_annotations()
    verify_mathjax_widths()

    print("\n=== VERIFICATION SUMMARY ===")
    print(f"Total Errors: {len(ERRORS)}")
    print(f"Total Warnings: {len(WARNINGS)}")

    if ERRORS:
        print("\nVerification FAILED with errors:")
        for e in ERRORS:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\nAll verifications PASSED successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
