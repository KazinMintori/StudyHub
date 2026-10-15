"""Comprehensive verifier for Chapter 36 Theory B (Sections 36.5-36.8, Figures 36.16-36.30).

Verifies:
1. Exact numerical calculations and assertions for Examples 36.4, 36.5, 36.6, and Self-Checks 36.5, 36.6, 36.7.
2. Complete Markdown parsing, display and inline math widths, syntax rules, and equation tags.
3. Decoded PNG pixel fidelity against source PDF regions for all 15 figures.
4. Completeness and syntax of physics36-theory-b-image-annotations.mjs.
"""
import math
import re
import subprocess
import sys
from pathlib import Path
import numpy as np
from PIL import Image
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[2]

# ---------------------------------------------------------
# Test 1: Numerical Calculations & Assertions
# ---------------------------------------------------------
def test_numerical_calculations():
    print("--- Running Test 1: Numerical Calculations & Assertions ---")
    results = {}

    # Example 36.4: Width of a grating spectrum
    # 600 slits per millimeter
    d_36_4_m = 1.0 / (600.0 * 1e3)  # 1.6667e-6 m
    assert math.isclose(round(d_36_4_m * 1e6, 2), 1.67, abs_tol=1e-3)
    d_used = 1.67e-6

    # (a) First-order (m = 1) limits: 380 nm (violet) to 750 nm (red)
    sin_theta_v1 = (1 * 380e-9) / d_used
    theta_v1_deg = math.degrees(math.asin(sin_theta_v1))
    assert math.isclose(round(theta_v1_deg, 1), 13.2, abs_tol=0.1)

    sin_theta_r1 = (1 * 750e-9) / d_used
    theta_r1_deg = math.degrees(math.asin(sin_theta_r1))
    assert math.isclose(round(theta_r1_deg, 1), 26.7, abs_tol=0.1)

    # (b) Second-order (m = 2) and third-order (m = 3)
    sin_theta_v2 = (2 * 380e-9) / d_used
    theta_v2_deg = math.degrees(math.asin(sin_theta_v2))
    assert math.isclose(round(theta_v2_deg, 1), 27.1, abs_tol=0.1)

    sin_theta_r2 = (2 * 750e-9) / d_used
    theta_r2_deg = math.degrees(math.asin(sin_theta_r2))
    assert math.isclose(round(theta_r2_deg, 1), 63.9, abs_tol=0.1)

    sin_theta_v3 = (3 * 380e-9) / d_used
    theta_v3_deg = math.degrees(math.asin(sin_theta_v3))
    assert math.isclose(round(theta_v3_deg, 1), 43.0, abs_tol=0.1)

    sin_theta_r3 = (3 * 750e-9) / d_used
    assert sin_theta_r3 > 1.0  # undefined, reaches 90 deg earlier

    # Cutoff wavelength for m = 3 at theta = 90 deg: lambda = d / 3
    lambda_cutoff_3 = (d_used / 3.0) * 1e9
    assert math.isclose(round(lambda_cutoff_3), 557.0, abs_tol=1.0)

    # Overlap assertions
    assert theta_r1_deg < theta_v2_deg  # 26.7 < 27.1 => no overlap of 1st and 2nd
    assert theta_v3_deg < theta_r2_deg  # 43.0 < 63.9 => overlap of 2nd and 3rd

    # Evaluate question: eye sensitive to 380 nm - 900 nm
    sin_theta_r1_900 = 900e-9 / d_used
    assert sin_theta_r1_900 > sin_theta_v2  # 900 > 760 => orders 1 and 2 overlap!

    results["example_36_4"] = {
        "d_m": d_used,
        "theta_v1": theta_v1_deg,
        "theta_r1": theta_r1_deg,
        "theta_v2": theta_v2_deg,
        "theta_r2": theta_r2_deg,
        "theta_v3": theta_v3_deg,
        "lambda_cutoff_3_nm": lambda_cutoff_3,
        "passed": True
    }

    # Example 36.5: X-ray diffraction
    lambda_36_5_nm = 0.154
    theta_1_deg = 34.5
    # (a) Bragg condition: 2 d sin(theta) = m * lambda (m = 1)
    d_36_5_nm = (1.0 * lambda_36_5_nm) / (2.0 * math.sin(math.radians(theta_1_deg)))
    assert math.isclose(round(d_36_5_nm, 3), 0.136, abs_tol=1e-4)

    # (b) For m = 2: sin(theta) = 2 * (0.154) / (2 * 0.136) = 0.154 / 0.136 = 1.132 > 1
    sin_theta_m2 = (2.0 * lambda_36_5_nm) / (2.0 * 0.136)
    assert sin_theta_m2 > 1.0  # Impossible

    # Evaluate: for 3 maxima (m = 3 possible): lambda < 2d / 3
    lambda_max_for_3_maxima = (2.0 * 0.136) / 3.0
    assert math.isclose(round(lambda_max_for_3_maxima, 4), 0.0907, abs_tol=1e-4)

    results["example_36_5"] = {
        "d_nm": d_36_5_nm,
        "sin_theta_m2": sin_theta_m2,
        "lambda_max_for_3_maxima": lambda_max_for_3_maxima,
        "passed": True
    }

    # Example 36.6: Resolving power of a camera lens
    f_len_mm = 50.0
    s_obj_m = 9.0
    lambda_36_6_m = 500e-9

    # (a) f/2 => D = f / 2 = 25 mm
    D_a_m = (f_len_mm / 2.0) * 1e-3
    theta_a_rad = 1.22 * (lambda_36_6_m / D_a_m)
    assert math.isclose(round(theta_a_rad * 1e5, 1), 2.4, abs_tol=0.1)
    theta_used = 2.4e-5

    y_a_m = s_obj_m * theta_used
    y_a_mm = y_a_m * 1e3
    assert math.isclose(round(y_a_mm, 2), 0.22, abs_tol=0.01)

    y_prime_a_mm = f_len_mm * theta_used
    assert math.isclose(round(y_prime_a_mm, 4), 0.0012, abs_tol=1e-4)

    # (b) stopped down to f/16 => D_b = D_a / 8 => theta_b = 8 * theta_a
    y_b_mm = 8.0 * 0.22
    assert math.isclose(round(y_b_mm, 1), 1.8, abs_tol=0.1)
    y_prime_b_mm = 8.0 * y_prime_a_mm
    assert math.isclose(round(y_prime_b_mm, 4), 0.0096, abs_tol=1e-4)

    results["example_36_6"] = {
        "theta_a_rad": theta_a_rad,
        "y_a_mm": y_a_mm,
        "y_prime_a_mm": y_prime_a_mm,
        "y_b_mm": y_b_mm,
        "y_prime_b_mm": y_prime_b_mm,
        "passed": True
    }

    # Self-Check 36.5: Sodium doublet in 4th order
    # Doublet: 589.00 nm and 589.59 nm => Delta lambda = 0.59 nm
    # R = lambda / Delta lambda = 589.00 / 0.59 = 1000
    # In fourth order (m = 4): N = R / m = 1000 / 4 = 250 slits
    N_slits_36_5 = 1000 / 4
    assert N_slits_36_5 == 250

    # Self-Check 36.6: Highest-order maximum in x-ray diffraction
    # d = 0.200 nm, lambda = 0.0900 nm
    # m = 2 d sin(theta) / lambda <= 2 * 0.200 / 0.0900 = 4.44 => m = 4
    m_max_36_6 = (2.0 * 0.200) / 0.0900
    assert math.floor(m_max_36_6) == 4

    # Self-Check 36.7: Telescope resolution ranking lambda / D
    # (i) radio: D = 100 m, lambda = 0.21 m => 2.1e-3
    ratio_i = 0.21 / 100.0
    # (ii) optical: D = 2.0 m, lambda = 500e-9 m => 2.5e-7
    ratio_ii = 500e-9 / 2.0
    # (iii) UV: D = 1.0 m, lambda = 100e-9 m => 1.0e-7
    ratio_iii = 100e-9 / 1.0
    # (iv) IR: D = 2.0 m, lambda = 10e-6 m => 5.0e-6
    ratio_iv = 10e-6 / 2.0

    assert ratio_iii < ratio_ii < ratio_iv < ratio_i
    rank_order = ["(iii)", "(ii)", "(iv)", "(i)"]

    results["selfchecks"] = {
        "selfcheck_36_5": 250,
        "selfcheck_36_6": 4,
        "selfcheck_36_7": rank_order,
        "passed": True
    }

    print("Test 1 PASSED: All numerical computations and self-checks verified successfully.")
    return results

# ---------------------------------------------------------
# Test 2: Source Markdown Files Equation & Formatting Audit
# ---------------------------------------------------------
def test_markdown_formatting():
    print("--- Running Test 2: Markdown Equations and Formatting Audit ---")
    md_files = [
        ROOT / "raw_materials/physics/translations/chapter-36/05-cach-tu-nhieu-xa.md",
        ROOT / "raw_materials/physics/translations/chapter-36/06-nhieu-xa-tia-x.md",
        ROOT / "raw_materials/physics/translations/chapter-36/07-khau-do-tron-phan-giai.md",
        ROOT / "raw_materials/physics/translations/chapter-36/08-anh-toan-ky.md",
    ]
    report = {}
    total_display_equations = 0
    total_inline_equations = 0

    forbidden_phrases = [
        "lấy từ giáo trình",
        "lấy từ slide",
        "bài tập lấy từ",
        "ảnh lấy từ",
        "ảnh nguyên gốc sách",
        "hình trong sách",
        "dữ liệu này từ",
        "theo sách",
        "sách dùng",
        "nguyên tác",
        "bản dịch của",
        "tiến độ bản dịch",
        "tại thời điểm biên soạn giáo trình",
        "do người soạn",
    ]

    for path in md_files:
        assert path.is_file(), f"Missing required file: {path}"
        text = path.read_text(encoding="utf-8")
        assert len(text) > 1000, f"File unexpectedly short: {path}"

        # Check forbidden phrases
        for phrase in forbidden_phrases:
            assert phrase.lower() not in text.lower(), f"Forbidden narrative phrase '{phrase}' found in {path.name}"

        # Check image path convention
        img_refs = re.findall(r"!\[.*?\]\((.*?)\)", text)
        for ref in img_refs:
            assert ref.startswith("../img/young-36/"), f"Topic image path should start with ../img/young-36/: {ref} in {path.name}"

        # 1. Check display math blocks syntax and tags
        display_blocks = []
        pos = 0
        while True:
            start = text.find("$$", pos)
            if start == -1:
                break
            end = text.find("$$", start + 2)
            assert end != -1, f"Unclosed $$ in {path.name} starting at character {start}"
            display_blocks.append((start, end + 2, text[start + 2:end]))
            pos = end + 2

        total_display_equations += len(display_blocks)

        for s, e, block in display_blocks:
            before_start = text.rfind("\n", 0, s)
            after_start = text.find("\n", s)
            line_opening = text[before_start + 1:after_start].strip()
            assert line_opening == "$$", f"Opening $$ must be on its own line in {path.name}: {line_opening!r}"

            assert r"\vert{" not in block, f"Forbidden \\vert{{}} syntax found in {path.name}"
            assert r"\Vert{" not in block, f"Forbidden \\Vert{{}} syntax found in {path.name}"

            tag_match = re.search(r"\\tag\{([^}]+)\}", block)
            if tag_match:
                tag_str = tag_match.group(1)
                assert r"\end{aligned}" in block, f"Block with tag {tag_str} must contain \\end{{aligned}} in {path.name}"
                aligned_pos = block.find(r"\end{aligned}")
                tag_pos = block.find(r"\tag{")
                assert tag_pos > aligned_pos, f"Tag {tag_str} must be AFTER \\end{{aligned}} in {path.name}"

        # 2. Check inline math syntax
        inline_matches = re.findall(r"(?<!\$)\$([^$\n]+)\$(?!\$)", text)
        total_inline_equations += len(inline_matches)
        for inline_eq in inline_matches:
            assert r"\vert{" not in inline_eq, f"Forbidden \\vert{{}} in inline eq: {inline_eq}"
            assert r"\Vert{" not in inline_eq, f"Forbidden \\Vert{{}} in inline eq: {inline_eq}"

        # 3. Check capitalization after colon in prose
        for line_idx, line in enumerate(text.splitlines(), start=1):
            if line.strip().startswith(":::"):
                continue
            matches = re.finditer(r"(?<!:):\s+(\S)", line)
            for m in matches:
                if "$" in line or "`" in line or "http" in line or "\\\\" in line:
                    continue
                char = m.group(1)
                if char.islower():
                    assert False, f"Lowercase '{char}' after colon in {path.name}:{line_idx}: {line}"

        # 4. Check H1 absence and H2/H3 structure
        h1s = [line for line in text.splitlines() if line.startswith("# ")]
        assert len(h1s) == 0, f"Forbidden H1 (# ...) found in {path.name}: {h1s}"
        h2s = [line.strip() for line in text.splitlines() if line.startswith("## ")]
        assert len(h2s) == 1, f"Expected exactly 1 H2 (## 36.n ...) in {path.name}, got {len(h2s)}: {h2s}"
        assert re.match(r"^## 36\.[5-8]\s+", h2s[0]), f"H2 must match ## 36.n in {path.name}: {h2s[0]}"

        # 5. Check canonical alt text prefix Hình 36.xx:
        for alt, ref in re.findall(r"!\[(.*?)\]\((.*?)\)", text):
            assert re.match(r"^Hình 36\.\d{2}:", alt), f"Image alt must start with canonical 'Hình 36.xx:': {alt[:30]} in {path.name}"

        report[path.name] = {
            "display_equations": len(display_blocks),
            "inline_equations": len(inline_matches),
            "size_bytes": len(text.encode("utf-8")),
            "passed": True
        }

    # 6. Rigorous Node.js MathJax SVG ex Width Measurement
    node_code = """
const fs = require('fs');
const md = require('./node_modules/markdown-it')();
const mathjax = require('./node_modules/markdown-it-mathjax3');
md.use(mathjax);

const files = process.argv.slice(1);
console.log('NODE ARGS:', files);
let maxDispWidth = 0;
let maxInlineWidth = 0;

for (const f of files) {
    console.log('START FILE: ' + f);
    const content = fs.readFileSync(f, 'utf8');
    let pos = 0;
    let dispIdx = 0;
    while (true) {
        const s = content.indexOf('$$', pos);
        if (s === -1) break;
        const e = content.indexOf('$$', s + 2);
        if (e === -1) {
            console.error('Unclosed $$ in ' + f);
            process.exit(1);
        }
        dispIdx++;
        let block = content.substring(s + 2, e).trim();
        block = block.replace(/\\\\tag\\{[^}]+\\}/g, '').trim();
        const rendered = md.render('$$\\n' + block + '\\n$$');
        const m = rendered.match(/(?:min-width:\\s*|width=")([\\d.]+)ex/);
        if (!m) {
            console.error('Failed to parse SVG width for display block #' + dispIdx + ' in ' + f + ':\\n' + block);
            process.exit(1);
        }
        const width = parseFloat(m[1]);
        if (isNaN(width) || width <= 0) {
            console.error('Invalid SVG width ' + width + ' for display block #' + dispIdx + ' in ' + f);
            process.exit(1);
        }
        const line = content.substring(0, s).split('\\n').length;
        if (width > maxDispWidth) maxDispWidth = width;
        if (width > 25.0) {
            console.error('Display equation #' + dispIdx + ' at ' + f + ':' + line + ' exceeds 25ex (' + width + 'ex > 25.0ex):\\n' + block);
            process.exit(1);
        }
        pos = e + 2;
    }

    const inlineRe = /(?<!\\$)\\$([^$\\n]+)\\$(?!\\$)/g;
    let inlineIdx = 0;
    let match;
    while ((match = inlineRe.exec(content)) !== null) {
        inlineIdx++;
        const eq = match[1];
        const rendered = md.render('$' + eq + '$');
        const m = /width="([0-9.]+)ex"/.exec(rendered);
        if (!m) {
            console.error('Failed to parse SVG width for inline eq #' + inlineIdx + ' in ' + f + ': $' + eq + '$');
            process.exit(1);
        }
        const width = parseFloat(m[1]);
        if (isNaN(width) || width <= 0) {
            console.error('Invalid SVG width ' + width + ' for inline eq #' + inlineIdx + ' in ' + f + ': $' + eq + '$');
            process.exit(1);
        }
        if (width > maxInlineWidth) maxInlineWidth = width;
        if (width > 30.0) {
            console.error('Inline equation #' + inlineIdx + ' in ' + f + ' exceeds 30ex (' + width + 'ex > 30.0ex): $' + eq + '$');
            process.exit(1);
        }
    }
}

console.log('MATHJAX_MEASURED_OK: max_disp=' + maxDispWidth + 'ex (limit 25.0ex), max_inline=' + maxInlineWidth + 'ex (limit 30.0ex)');
"""

    node_res = subprocess.run(
        ["node", "-e", node_code] + [str(p) for p in md_files],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    assert node_res.returncode == 0, f"MathJax measurement failed:\n{node_res.stderr or node_res.stdout}"
    assert "MATHJAX_MEASURED_OK" in node_res.stdout, f"MathJax measurement did not report success:\n{node_res.stdout}"
    print(f"  {node_res.stdout.strip()}")

    print(f"Test 2 PASSED: Verified {len(md_files)} files with {total_display_equations} display equations (<=25ex) and {total_inline_equations} inline formulas (<=30ex).")
    return report

# ---------------------------------------------------------
# Test 3: Figure Asset Verification & Decoded PNG Comparison
# ---------------------------------------------------------
def test_figure_assets():
    print("--- Running Test 3: Figure Asset Verification & Pixel Comparison ---")
    img_dir = ROOT / "docs/vat-ly-2/bai-giang/img/young-36"
    assert img_dir.is_dir(), f"Image directory missing: {img_dir}"

    prep_script = ROOT / "scripts/prepare-physics36-theory-b-assets.py"
    assert prep_script.is_file(), f"Asset prep script missing: {prep_script}"

    import importlib.util
    spec = importlib.util.spec_from_file_location("prep", str(prep_script))
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)

    crops = prep.CROPS
    assert len(crops) == 15, f"Expected 15 figure crops, got {len(crops)}"

    source_pdf = prep.SOURCE
    assert source_pdf.is_file(), f"Source PDF missing: {source_pdf}"

    results = {}
    with fitz.open(source_pdf) as doc:
        for stem, (page_num, box) in crops.items():
            img_file = img_dir / f"{stem}.png"
            assert img_file.is_file(), f"Target image missing: {img_file}"

            page = doc[page_num - 1]
            rect = fitz.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=fitz.Matrix(prep.SCALE, prep.SCALE), clip=rect, alpha=False)

            with Image.open(img_file) as on_disk:
                on_disk_rgb = on_disk.convert("RGB")
                assert on_disk_rgb.size == (pix.width, pix.height), (
                    f"Dimension mismatch for {stem}: disk {on_disk_rgb.size} vs pdf {pix.width}x{pix.height}"
                )
                pdf_im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                diff = np.abs(np.array(on_disk_rgb, dtype=np.int16) - np.array(pdf_im, dtype=np.int16))
                max_diff = int(diff.max())
                assert max_diff == 0, f"Pixel difference detected in {stem}: max diff = {max_diff}"

            results[stem] = {
                "page": page_num,
                "box": box,
                "size": (pix.width, pix.height),
                "max_diff": max_diff,
                "passed": True
            }

    print(f"Test 3 PASSED: Verified all {len(results)} figure assets with bit-exact pixel matching (max_diff=0).")
    return results

# ---------------------------------------------------------
# Test 4: Image Annotations Module Audit
# ---------------------------------------------------------
def test_image_annotations():
    print("--- Running Test 4: Image Annotations Module Audit ---")
    annot_file = ROOT / "docs/.vitepress/physics36-theory-b-image-annotations.mjs"
    assert annot_file.is_file(), f"Annotations file missing: {annot_file}"

    # Syntax check with node
    res = subprocess.run(["node", "--check", str(annot_file)], capture_output=True, text=True)
    assert res.returncode == 0, f"Node syntax check failed: {res.stderr}"

    # Dynamic import and semantic validation in Node.js
    node_audit = f"""
import('{annot_file.as_uri()}').then(m => {{
    const annotations = m.physics36TheoryBImageAnnotations;
    if (!annotations) {{
        console.error('physics36TheoryBImageAnnotations export missing');
        process.exit(1);
    }}
    let totalLabels = 0;
    for (let i = 16; i <= 30; i++) {{
        const key = `young-36/hinh-36-${{i}}`;
        const list = annotations[key];
        if (!list || !Array.isArray(list)) {{
            console.error(`Missing or non-array annotation for ${{key}}`);
            process.exit(1);
        }}
        const seenEn = new Set();
        for (const [vi, en] of list) {{
            if (!vi || !en) {{
                console.error(`Invalid pair in ${{key}}: [${{vi}}, ${{en}}]`);
                process.exit(1);
            }}
            if (seenEn.has(en)) {{
                console.error(`Duplicate English label in ${{key}}: ${{en}}`);
                process.exit(1);
            }}
            seenEn.add(en);
            totalLabels++;
        }}
    }}
    console.log(`ANNOTATIONS_AUDIT_OK: verified 15 figures with ${{totalLabels}} bilingual labels`);
}}).catch(err => {{
    console.error(err);
    process.exit(1);
}});
"""
    audit_res = subprocess.run(["node", "--input-type=module", "-e", node_audit], capture_output=True, text=True, encoding="utf-8")
    assert audit_res.returncode == 0, f"Annotation audit failed:\n{audit_res.stderr or audit_res.stdout}"
    assert "ANNOTATIONS_AUDIT_OK" in audit_res.stdout, f"Annotation audit did not report success:\n{audit_res.stdout}"
    print(f"  {audit_res.stdout.strip()}")

    print("Test 4 PASSED: Annotation module syntax, 15 figure keys, and bilingual label pairs verified successfully.")
    return {"passed": True}

# ---------------------------------------------------------
# Main Runner
# ---------------------------------------------------------
def main():
    print("==========================================================")
    print("STARTING CHAPTER 36 THEORY B COMPREHENSIVE VERIFICATION")
    print("==========================================================")
    t1 = test_numerical_calculations()
    t3 = test_figure_assets()
    t4 = test_image_annotations()
    # Test 2 will run when markdown files are written
    if (ROOT / "raw_materials/physics/translations/chapter-36/05-cach-tu-nhieu-xa.md").is_file():
        t2 = test_markdown_formatting()
    else:
        print("Test 2 SKIPPED: Markdown files not yet created.")
    print("==========================================================")
    print("ALL RUNNING VERIFICATION SUITES PASSED SUCCESSFULLY")
    print("==========================================================")

if __name__ == "__main__":
    main()
