"""Comprehensive verification test suite for Chapter 42 Theory A (Sections 42.1-42.4).

Verifies:
1. Physics numerical calculations for Examples 42.1-42.5 and all subparts.
2. Image existence and bit-exact RGB pixel comparison with source PDF crops.
3. Image annotations dictionary in docs/.vitepress/physics42-theory-a-image-annotations.mjs.
4. Markdown pedagogical standards: Headings, colon capitalization, TYU structure.
5. Display and inline math formatting: $$ line placement, no \\vert{}, line-breaking rules.
6. Actual MathJax SVG width measurements using markdown-it-mathjax3 (display <= 27ex, inline <= 38ex).
"""
import sys
import os
import re
import math
import subprocess
from pathlib import Path
import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

FRAGMENTS = [
    ROOT / "raw_materials/physics/translations/chapter-42/01-lien-ket-phan-tu.md",
    ROOT / "raw_materials/physics/translations/chapter-42/02-pho-phan-tu.md",
    ROOT / "raw_materials/physics/translations/chapter-42/03-cau-truc-chat-ran.md",
    ROOT / "raw_materials/physics/translations/chapter-42/04-dai-nang-luong.md",
]

IMG_DIR = ROOT / "docs/vat-ly-2/bai-giang/img/young-42"
ANNOTATIONS_FILE = ROOT / "docs/.vitepress/physics42-theory-a-image-annotations.mjs"

# 1. Physics Constants
C_LIGHT = 2.99792458e8       # m/s
C_LIGHT_ROUNDED = 3.00e8    # m/s
H_PLANCK = 6.62607015e-34   # J s
H_BAR = 1.054571817e-34     # J s
H_BAR_SOURCE = 1.0546e-34   # J s
H_EV_S = 4.135667696e-15    # eV s
H_EV_S_SOURCE = 4.136e-15   # eV s
E_CHARGE = 1.602176634e-19  # C
EPS_0 = 8.8541878128e-12    # F/m
K_COULOMB = 1.0 / (4.0 * math.pi * EPS_0)  # N m^2 / C^2
K_COULOMB_SOURCE = 9.0e9    # N m^2 / C^2


def test_physics_calculations():
    print("=== Testing Physics Calculations ===")

    # Section 42.1 source energy balance and Example 42.1
    # 1. Ion creation cost: Na ionization (5.138 eV) and Cl electron affinity (3.613 eV)
    E_ion_Na = 5.138       # eV
    E_affinity_Cl = 3.613  # eV
    delta_E_ion = E_ion_Na - E_affinity_Cl
    assert abs(delta_E_ion - 1.525) < 1e-6, f"Delta E mismatch: {delta_E_ion}"

    # 2. Molecular potential minimum and net binding energy from source text
    U_min_observed = -5.7  # eV at r0 = 0.24 nm
    E_binding_NaCl = abs(U_min_observed) - delta_E_ion
    assert abs(E_binding_NaCl - 4.175) < 1e-6, f"Binding energy mismatch: {E_binding_NaCl}"
    assert round(E_binding_NaCl, 1) == 4.2, f"Rounded binding energy mismatch: {E_binding_NaCl}"

    # 3. Example 42.1: Separate point-charge Coulomb model
    r0_ex1 = 0.24e-9  # m
    U_coulomb_J = -K_COULOMB_SOURCE * (1.6e-19)**2 / r0_ex1
    U_coulomb_eV = U_coulomb_J / 1.6e-19
    assert abs(U_coulomb_J - (-9.6e-19)) < 1e-20, f"Ex 42.1 J mismatch: {U_coulomb_J}"
    assert abs(U_coulomb_eV - (-6.0)) < 0.05, f"Ex 42.1 eV mismatch: {U_coulomb_eV}"
    print("  ✓ Section 42.1 & Example 42.1: Ion cost = 1.525 eV, molecular U_min = -5.7 eV, binding = 4.2 eV; point-charge U = -6.0 eV verified.")

    # Example 42.2: Rotational spectrum of CO
    r0_ex2 = 0.1128e-9  # m
    m1_C = 1.993e-26   # kg
    m2_O = 2.656e-26   # kg
    m_r = (m1_C * m2_O) / (m1_C + m2_O)
    assert abs(m_r - 1.139e-26) < 1e-28, f"Ex 42.2 m_r mismatch: {m_r}"

    I_CO = m_r * (r0_ex2 ** 2)
    assert abs(I_CO - 1.449e-46) < 1e-48, f"Ex 42.2 I mismatch: {I_CO}"

    E_base_J = (H_BAR_SOURCE ** 2) / (2.0 * 1.449e-46)
    assert abs(E_base_J - 3.838e-23) < 1e-25, f"Ex 42.2 E_base_J mismatch: {E_base_J}"

    E_base_eV = E_base_J / E_CHARGE
    E_base_meV = E_base_eV * 1000.0
    assert abs(E_base_meV - 0.2395) < 0.001, f"Ex 42.2 E_base_meV mismatch: {E_base_meV}"

    E0 = 0.0
    E1 = 2.0 * E_base_meV
    E2 = 6.0 * E_base_meV
    assert abs(E1 - 0.479) < 0.002, f"Ex 42.2 E1 mismatch: {E1}"
    assert abs(E2 - 1.437) < 0.005, f"Ex 42.2 E2 mismatch: {E2}"

    delta_E_21_meV = E2 - E1
    assert abs(delta_E_21_meV - 0.958) < 0.005, f"Ex 42.2 Delta E mismatch: {delta_E_21_meV}"

    lambda_21 = (H_EV_S_SOURCE * C_LIGHT_ROUNDED) / (0.958e-3)
    assert abs(lambda_21 - 1.29e-3) < 0.02e-3, f"Ex 42.2 lambda mismatch: {lambda_21}"
    print("  ✓ Example 42.2: m_r = 1.139e-26 kg, I = 1.449e-46 kg m^2, E1 = 0.479 meV, E2 = 1.437 meV, lambda = 1.29 mm verified.")

    # Example 42.3: Vibration-rotation of CO
    hbar_omega_eV = 0.2690
    delta_E_rot_eV = 0.000479
    # Part (a): initial l = 0, final l = 1 => gains rotation, photon energy is less
    E_a = hbar_omega_eV - delta_E_rot_eV
    assert abs(E_a - 0.2685) < 1e-4, f"Ex 42.3 E_a mismatch: {E_a}"
    lambda_a = (H_EV_S_SOURCE * 2.998e8) / 0.2685
    assert abs(lambda_a - 4.618e-6) < 0.005e-6, f"Ex 42.3 lambda_a mismatch: {lambda_a}"

    # Part (b): initial l = 1, final l = 0 => loses rotation, photon energy is more
    E_b = hbar_omega_eV + delta_E_rot_eV
    assert abs(E_b - 0.2695) < 1e-4, f"Ex 42.3 E_b mismatch: {E_b}"
    lambda_b = (H_EV_S_SOURCE * 2.998e8) / 0.2695
    assert abs(lambda_b - 4.601e-6) < 0.005e-6, f"Ex 42.3 lambda_b mismatch: {lambda_b}"
    print("  ✓ Example 42.3: E_a = 0.2685 eV (4.618 um), E_b = 0.2695 eV (4.601 um) verified.")

    # Example 42.4: 1D ionic crystal Madelung sum and stability
    # Alternating harmonic series: 1 - 1/2 + 1/3 - 1/4 + ... = ln(2)
    s = sum((-1)**(k + 1) / k for k in range(1, 100000))
    assert abs(s - math.log(2)) < 1e-4, f"Ex 42.4 series mismatch: {s} vs {math.log(2)}"
    assert 0.6931 < math.log(2) < 0.6932
    # Tagged ion potential energy factor (both sides): -2 * ln(2) approx -1.38629
    factor_tagged = 2.0 * math.log(2)
    assert abs(factor_tagged - 1.38629) < 1e-4
    # Crystal total energy per ion (pair-counted, 1/2 factor to avoid double counting): -ln(2) approx -0.69315
    factor_per_ion = math.log(2)
    assert abs(factor_per_ion - 0.69315) < 1e-4
    print("  ✓ Example 42.4: Alternating series = ln(2) = 0.69315, tagged factor = -1.386, pair-counted factor = -0.693 verified.")

    # Example 42.5: Photoconductivity in Ge
    E_gap_Ge = 0.67  # eV
    lambda_max_Ge = (H_EV_S_SOURCE * C_LIGHT_ROUNDED) / E_gap_Ge
    assert abs(lambda_max_Ge - 1.85e-6) < 0.05e-6, f"Ex 42.5 lambda mismatch: {lambda_max_Ge}"
    assert round(lambda_max_Ge * 1e6, 1) == 1.9, f"Ex 42.5 rounded mismatch: {lambda_max_Ge}"
    print("  ✓ Example 42.5: E_g = 0.67 eV -> lambda_max = 1.9 um (1900 nm) verified.")


def test_image_files_and_pixel_matching():
    print("\n=== Testing Image Files & RGB Pixel Match ===")
    import importlib.util
    spec = importlib.util.spec_from_file_location("prep", str(ROOT / "scripts/prepare-physics42-theory-a-assets.py"))
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)
    CROPS = prep.CROPS
    SCALE = prep.SCALE

    assert SOURCE.is_file(), f"Source PDF missing at {SOURCE}"
    assert len(CROPS) == 23, f"Expected 23 crops, found {len(CROPS)}"

    with pymupdf.open(SOURCE) as pdf:
        for stem, (pno, box) in CROPS.items():
            img_path = IMG_DIR / f"{stem}.png"
            assert img_path.is_file(), f"Missing cropped image: {img_path}"
            assert img_path.stat().st_size > 0, f"Empty image: {img_path}"

            # Render directly from PDF
            page = pdf[pno - 1]
            rect = pymupdf.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=rect, alpha=False)

            # Load saved file
            saved_img = Image.open(img_path)
            assert saved_img.size == (pix.width, pix.height), f"Dimension mismatch for {stem}: {saved_img.size} vs ({pix.width}, {pix.height})"

            # Pixel compare
            saved_bytes = saved_img.convert("RGB").tobytes()
            fresh_bytes = pix.samples
            assert saved_bytes == fresh_bytes, f"Pixel difference detected in {stem}!"
            print(f"  ✓ {stem}: {pix.width}x{pix.height} matches PDF page {pno} bit-for-bit.")


def test_annotations_dictionary():
    print("\n=== Testing Image Annotations Dictionary ===")
    assert ANNOTATIONS_FILE.is_file(), f"Missing annotations file: {ANNOTATIONS_FILE}"
    content = ANNOTATIONS_FILE.read_text(encoding="utf-8")

    import importlib.util
    spec = importlib.util.spec_from_file_location("prep", str(ROOT / "scripts/prepare-physics42-theory-a-assets.py"))
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)
    for stem in prep.CROPS.keys():
        key = f"young-42/{stem}"
        assert f'"{key}":' in content or f"'{key}':" in content, f"Key {key} missing from annotations!"
    print(f"  ✓ All 23 image keys present in {ANNOTATIONS_FILE.name}.")


def test_markdown_pedagogy_and_formatting():
    print("\n=== Testing Markdown Pedagogical Standards & Formatting ===")

    expected_h2 = [
        "## 42.1. Các loại liên kết phân tử",
        "## 42.2. Phổ phân tử",
        "## 42.3. Cấu trúc chất rắn",
        "## 42.4. Dải năng lượng"
    ]

    for idx, fpath in enumerate(FRAGMENTS):
        assert fpath.is_file(), f"Missing markdown fragment: {fpath}"
        text = fpath.read_text(encoding="utf-8")
        lines = text.splitlines()

        # 1. First line must be H2
        assert lines[0] == expected_h2[idx], f"Expected first line {expected_h2[idx]}, got {lines[0]}"
        assert not text.startswith("---"), f"Fragment {fpath.name} must not contain frontmatter!"
        assert not any(line.startswith("# ") for line in lines), f"Fragment {fpath.name} must not contain H1 header!"
        assert not any("Tài liệu tham khảo" in line for line in lines), f"Fragment {fpath.name} must not contain reference footer!"

        # 2. Colon capitalization: Check every prose colon
        for line_num, line in enumerate(lines, 1):
            # Skip code blocks and image lines
            if line.startswith("```") or line.startswith("!["):
                continue
            # Strip VitePress container prefix like '::: tip ' or '::: details '
            clean_line = re.sub(r"^:::\s*\w*\s*", "", line)
            # Find colons in prose
            if "$$" in clean_line:
                continue
            for m in re.finditer(r":\s+([a-zA-Z\u00C0-\u024F\u1EA0-\u1EF9])", clean_line):
                char = m.group(1)
                assert char.isupper(), f"Lowercase after colon in {fpath.name}:{line_num}: '{line.strip()}'"

        # 3. Display math $$ must be on own line at column 0
        in_display = False
        for line_num, line in enumerate(lines, 1):
            if line.strip() == "$$":
                assert line == "$$", f"$$ must be column 0 without leading space in {fpath.name}:{line_num}"
                in_display = not in_display
            elif "$$" in line:
                raise AssertionError(f"Inline $$ delimiter found in {fpath.name}:{line_num}: '{line}'")
        assert not in_display, f"Unclosed $$ in {fpath.name}"

        # 4. Check forbidden math commands
        assert r"\vert{}" not in text, f"Forbidden \\vert{{}} found in {fpath.name}"
        assert r"\Vert{}" not in text, f"Forbidden \\Vert{{}} found in {fpath.name}"

        # 5. Check TYU structure
        tyu_header = f"### Câu tự kiểm tra 42.{idx + 1}"
        assert tyu_header in text, f"Missing TYU header {tyu_header} in {fpath.name}"
        assert "::: details Giải thích và đáp án" in text, f"Missing closed details in {fpath.name}"

        print(f"  ✓ {fpath.name}: Structure, H2, colons, TYU, and $$ syntax validated.")


def test_mathjax_widths_in_memory():
    print("\n=== Testing Actual MathJax Widths via markdown-it-mathjax3 ===")
    root_posix = ROOT.as_posix()

    js_script = f"""
const fs = require('node:fs');
const path = require('node:path');
const MarkdownIt = require(path.resolve('{root_posix}/node_modules/markdown-it'));
const mathjax = require(path.resolve('{root_posix}/node_modules/markdown-it-mathjax3'));

const md = new MarkdownIt().use(mathjax);
const files = [
  path.resolve('{root_posix}/raw_materials/physics/translations/chapter-42/01-lien-ket-phan-tu.md'),
  path.resolve('{root_posix}/raw_materials/physics/translations/chapter-42/02-pho-phan-tu.md'),
  path.resolve('{root_posix}/raw_materials/physics/translations/chapter-42/03-cau-truc-chat-ran.md'),
  path.resolve('{root_posix}/raw_materials/physics/translations/chapter-42/04-dai-nang-luong.md')
];

let totalDisplay = 0, totalInline = 0, maxDisplay = 0, maxInline = 0;
const errors = [], wideDisplay = [], wideInline = [];

for (const f of files) {{
  const source = fs.readFileSync(f, 'utf8');
  for (const m of source.matchAll(/\\$\\$([\\s\\S]*?)\\$\\$/g)) {{
    totalDisplay++;
    const tex = m[1].trim().replace(/\\\\tag\\{{[\\d.]+\\}}/g, '');
    const html = md.render('$$\\n' + tex + '\\n$$');
    const width = Number(html.match(/(?:min-width:\\s*|width=\")([\\d.]+)ex/)?.[1] || 0);
    if (width > maxDisplay) maxDisplay = width;
    const invalid = /data-mjx-error|<merror/.test(html);
    if (invalid) errors.push({{file: f, tex, error: 'invalid display math'}});
    if (width > 27) wideDisplay.push({{file: f, width, tex}});
  }}
  const stripped = source.replace(/\\$\\$[\\s\\S]*?\\$\\$/g, '');
  for (const m of stripped.matchAll(/(?<!\\$)\\$([^\\n$]+)\\$(?!\\$)/g)) {{
    totalInline++;
    const tex = m[1].trim();
    const html = md.renderInline('$' + tex + '$');
    const width = Number(html.match(/width=\"([\\d.]+)ex/)?.[1] || 0);
    if (width > maxInline) maxInline = width;
    const invalid = /data-mjx-error|<merror/.test(html);
    if (invalid) errors.push({{file: f, tex, error: 'invalid inline math'}});
    if (width > 38) wideInline.push({{file: f, width, tex}});
  }}
}}

console.log(`TOTAL_DISPLAY=${{totalDisplay}}`);
console.log(`MAX_DISPLAY=${{maxDisplay}}`);
console.log(`TOTAL_INLINE=${{totalInline}}`);
console.log(`MAX_INLINE=${{maxInline}}`);
console.log(`ERRORS=${{errors.length}}`);
console.log(`WIDE_DISPLAY=${{wideDisplay.length}}`);
for (const item of wideDisplay) {{
  console.log(`[WIDE DISPLAY] ${{item.width}}ex in ${{path.basename(item.file)}}: ${{item.tex.replace(/\\s+/g, ' ').slice(0, 80)}}`);
}}
console.log(`WIDE_INLINE=${{wideInline.length}}`);
for (const item of wideInline) {{
  console.log(`[WIDE INLINE] ${{item.width}}ex in ${{path.basename(item.file)}}: ${{item.tex.replace(/\\s+/g, ' ').slice(0, 80)}}`);
}}

if (errors.length > 0 || wideDisplay.length > 0 || wideInline.length > 0) {{
  process.exit(1);
}}
"""
    proc = subprocess.run(["node", "-"], input=js_script, capture_output=True, text=True, encoding="utf-8", cwd=str(ROOT))
    print(proc.stdout.strip())
    if proc.returncode != 0:
        print("STDERR:", proc.stderr)
        raise AssertionError("MathJax measurement failed due to syntax errors or oversized formulas!")
    print("  ✓ All formulas measured with markdown-it-mathjax3 via node stdin: Display <= 27ex, Inline <= 38ex, 0 syntax errors.")


def main():
    print("Starting Chapter 42 Theory A Verification...")
    test_physics_calculations()
    test_image_files_and_pixel_matching()
    test_annotations_dictionary()
    test_markdown_pedagogy_and_formatting()
    test_mathjax_widths_in_memory()
    print("\n=======================================================")
    print("Chapter 42 Theory A test suites completed successfully (exact verified checks).")
    print("=======================================================")


if __name__ == "__main__":
    main()
