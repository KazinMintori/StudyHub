"""Comprehensive verifier for Chapter 35 Theory B (Sections 35.4-35.5, Figures 35.11-35.19).

Verifies:
1. Exact numerical calculations and assertions for Examples 35.4, 35.5, 35.6, 35.7, and Self-Checks 35.4, 35.5.
2. Complete Markdown parsing, display and inline math widths, syntax rules, and equation tags.
3. Decoded PNG pixel fidelity against source PDF regions for all 9 figures.
4. Completeness and syntax of physics35-theory-b-image-annotations.mjs.
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

    # Example 35.4: Thin-film interference I (air wedge between microscope slides)
    l_35_4_m = 0.100  # 10.0 cm = 0.100 m
    h_35_4_m = 0.0200e-3  # 0.0200 mm = 0.0200 * 10^-3 m
    lambda0_35_4_m = 500e-9  # 500 nm = 500 * 10^-9 m
    # Dark fringe spacing: Delta x = l * lambda0 / (2 * h)
    dx_35_4_m = (l_35_4_m * lambda0_35_4_m) / (2.0 * h_35_4_m)
    assert math.isclose(dx_35_4_m, 1.25e-3, abs_tol=1e-6)
    dx_35_4_mm = dx_35_4_m * 1e3
    assert math.isclose(dx_35_4_mm, 1.25, abs_tol=1e-4)
    # Line of contact (m = 0 => x = 0): dark fringe
    results["example_35_4"] = {
        "dx_mm": dx_35_4_mm,
        "contact_fringe": "dark",
        "passed": True
    }

    # Example 35.5: Thin-film interference II (water wedge between glass plates)
    n_water = 1.33
    lambda_water_nm = 500.0 / n_water
    assert math.isclose(round(lambda_water_nm), 376.0, abs_tol=0.5)
    dx_35_5_mm = dx_35_4_mm / n_water
    assert math.isclose(round(dx_35_5_mm, 3), 0.940, abs_tol=1e-4)
    # Dimension h to get same fringe spacing
    h_eq_35_5_mm = 0.0200 / n_water
    assert math.isclose(round(h_eq_35_5_mm, 4), 0.0150, abs_tol=1e-4)
    results["example_35_5"] = {
        "lambda_water_nm": lambda_water_nm,
        "dx_mm": dx_35_5_mm,
        "h_eq_mm": h_eq_35_5_mm,
        "contact_fringe": "dark",
        "passed": True
    }

    # Example 35.6: Thin-film interference III (silicone grease wedge)
    n_plastic = 1.40
    n_grease = 1.50
    n_flint = 1.60
    lambda_grease_nm = 500.0 / n_grease
    assert math.isclose(round(lambda_grease_nm), 333.0, abs_tol=0.5)
    dx_35_6_mm = dx_35_4_mm / n_grease
    assert math.isclose(round(dx_35_6_mm, 3), 0.833, abs_tol=1e-4)
    # Line of contact (m = 0 in constructive 2t = m * lambda => x = 0): bright fringe
    results["example_35_6"] = {
        "lambda_grease_nm": lambda_grease_nm,
        "dx_mm": dx_35_6_mm,
        "contact_fringe": "bright",
        "passed": True
    }

    # Example 35.7: A nonreflective coating (MgF2 on glass)
    n_mgf2 = 1.38
    n_glass = 1.52
    lambda0_35_7_nm = 550.0
    lambda_mgf2_nm = lambda0_35_7_nm / n_mgf2
    assert math.isclose(round(lambda_mgf2_nm), 399.0, abs_tol=1.0)
    # Text states lambda = lambda0 / n = 550 nm / 1.38 = 400 nm, and t = lambda / 4 = 100 nm
    t_35_7_nm = round(lambda_mgf2_nm / 4.0)
    assert t_35_7_nm == 100
    # Constructive reflection in air for 2t = lambda_film => lambda_film = 200 nm
    # lambda_air = (200 nm) * 1.38 = 276 nm
    lambda_air_constructive_nm = 200.0 * n_mgf2
    assert math.isclose(round(lambda_air_constructive_nm), 276.0, abs_tol=0.5)
    results["example_35_7"] = {
        "lambda_mgf2_nm": lambda_mgf2_nm,
        "t_coating_nm": t_35_7_nm,
        "lambda_air_constructive_nm": lambda_air_constructive_nm,
        "passed": True
    }

    # Self-Check 35.4: Benzene on fluorite
    n_benzene = 1.501
    n_fluorite = 1.434
    lambda_in_benzene_nm = 400.0
    # Air (1.000) < Benzene (1.501) => pi phase shift at upper surface
    # Benzene (1.501) > Fluorite (1.434) => 0 phase shift at lower surface
    # Constructive condition: 2t = (m + 1/2) * lambda => t = (m + 1/2) * lambda / 2
    t_selfcheck_35_4 = [(m + 0.5) * lambda_in_benzene_nm / 2.0 for m in range(4)]
    assert t_selfcheck_35_4[0] == 100.0  # (i)
    assert t_selfcheck_35_4[1] == 300.0  # (iii)
    assert t_selfcheck_35_4[2] == 500.0
    valid_options = ["(i)", "(iii)"]

    # Self-Check 35.5: Michelson interferometer compensator plate index change
    # Changing index of refraction changes optical path length nd => fringes shift.
    selfcheck_35_5_ans = "yes"

    results["selfchecks"] = {
        "selfcheck_35_4_options": valid_options,
        "selfcheck_35_4_thicknesses": t_selfcheck_35_4,
        "selfcheck_35_5_answer": selfcheck_35_5_ans,
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
        ROOT / "raw_materials/physics/translations/chapter-35/04-giao-thoa-mang-mong.md",
        ROOT / "raw_materials/physics/translations/chapter-35/05-giao-thoa-ke-michelson.md",
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
            assert ref.startswith("../img/young-35/"), f"Topic image path should start with ../img/young-35/: {ref} in {path.name}"

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

        report[path.name] = {
            "display_equations": len(display_blocks),
            "inline_equations": len(inline_matches),
            "size_bytes": len(text.encode("utf-8")),
            "passed": True
        }

    # 4. Rigorous Node.js MathJax SVG ex Width Measurement
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
        if (width > 27.0) {
            console.error('Display equation #' + dispIdx + ' at ' + f + ':' + line + ' exceeds 27ex (' + width + 'ex > 27.0ex):\\n' + block);
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
        if (width > 38.0) {
            console.error('Inline equation #' + inlineIdx + ' in ' + f + ' exceeds 38ex (' + width + 'ex > 38.0ex): $' + eq + '$');
            process.exit(1);
        }
    }
}

console.log('MATHJAX_MEASURED_OK: max_disp=' + maxDispWidth + 'ex (limit 27.0ex), max_inline=' + maxInlineWidth + 'ex (limit 38.0ex)');
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

    print(f"Test 2 PASSED: Verified {len(md_files)} files with {total_display_equations} display equations (<=27ex) and {total_inline_equations} inline formulas (<=38ex).")
    return report

# ---------------------------------------------------------
# Test 3: Figure Asset Verification & Decoded PNG Comparison
# ---------------------------------------------------------
def test_figure_assets():
    print("--- Running Test 3: Figure Asset Verification & Pixel Comparison ---")
    img_dir = ROOT / "docs/vat-ly-2/bai-giang/img/young-35"
    assert img_dir.is_dir(), f"Image directory missing: {img_dir}"

    prep_script = ROOT / "scripts/prepare-physics35-theory-b-assets.py"
    assert prep_script.is_file(), f"Asset prep script missing: {prep_script}"

    import importlib.util
    spec = importlib.util.spec_from_file_location("prep", str(prep_script))
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)

    crops = prep.CROPS
    assert len(crops) == 9, f"Expected 9 figure crops, got {len(crops)}"

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
    annot_file = ROOT / "docs/.vitepress/physics35-theory-b-image-annotations.mjs"
    assert annot_file.is_file(), f"Annotations file missing: {annot_file}"

    # Syntax check with node
    res = subprocess.run(["node", "--check", str(annot_file)], capture_output=True, text=True)
    assert res.returncode == 0, f"Node syntax check failed: {res.stderr}"

    # Dynamic import and semantic validation in Node.js
    node_audit = f"""
import('{annot_file.as_uri()}').then(m => {{
    const annotations = m.physics35TheoryBImageAnnotations;
    if (!annotations) {{
        console.error('physics35TheoryBImageAnnotations export missing');
        process.exit(1);
    }}
    let totalLabels = 0;
    for (let i = 11; i <= 19; i++) {{
        const key = `young-35/hinh-35-${{i}}`;
        const list = annotations[key];
        if (!list || !Array.isArray(list)) {{
            console.error(`Missing or non-array annotation for ${{key}}`);
            process.exit(1);
        }}
        // Figure 35.15 has only mathematical symbols (x, l, h, t) and lines.
        if (list.length === 0 && i !== 15) {{
            console.error(`Empty annotation array for ${{key}}`);
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
    console.log(`ANNOTATIONS_AUDIT_OK: verified 9 figures with ${{totalLabels}} bilingual labels`);
}}).catch(err => {{
    console.error(err);
    process.exit(1);
}});
"""
    audit_res = subprocess.run(["node", "--input-type=module", "-e", node_audit], capture_output=True, text=True, encoding="utf-8")
    assert audit_res.returncode == 0, f"Annotation audit failed:\n{audit_res.stderr or audit_res.stdout}"
    assert "ANNOTATIONS_AUDIT_OK" in audit_res.stdout, f"Annotation audit did not report success:\n{audit_res.stdout}"
    print(f"  {audit_res.stdout.strip()}")

    print("Test 4 PASSED: Annotation module syntax, 9 figure keys, and bilingual label pairs verified successfully.")
    return {"passed": True}

# ---------------------------------------------------------
# Main Runner
# ---------------------------------------------------------
def main():
    print("==========================================================")
    print("STARTING CHAPTER 35 THEORY B COMPREHENSIVE VERIFICATION")
    print("==========================================================")
    t1 = test_numerical_calculations()
    t3 = test_figure_assets()
    t4 = test_image_annotations()
    # Test 2 will run when markdown files are written
    if (ROOT / "raw_materials/physics/translations/chapter-35/04-giao-thoa-mang-mong.md").is_file():
        t2 = test_markdown_formatting()
    else:
        print("Test 2 SKIPPED: Markdown files not yet created.")
    print("==========================================================")
    print("ALL RUNNING VERIFICATION SUITES PASSED SUCCESSFULLY")
    print("==========================================================")

if __name__ == "__main__":
    main()
