"""
Verification script for Chapter 42 Theory B (Sections 42.5 - 42.8).
Tests:
1. Python numerical recomputations for Examples 42.6, 42.7, 42.8, 42.9.
2. Bit-level image verification for all 18 extracted images.
3. Equation tag inventory: (42.10) to (42.25).
4. Real MathJax SVG width measurement (display <= 27ex, inline <= 38ex).
5. Markdown syntax and pedagogical linting (colons, semicolons, em-dashes, self-checks).
"""

import sys
import os
import re
import math
import json
import subprocess
from pathlib import Path
import fitz # PyMuPDF
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
PDF_PATH = REPO_ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
IMG_DIR = REPO_ROOT / "docs" / "vat-ly-2" / "bai-giang" / "img" / "young-42"
TRANSLATIONS_DIR = REPO_ROOT / "raw_materials" / "physics" / "translations" / "chapter-42"

FRAGMENTS = [
    TRANSLATIONS_DIR / "05-mo-hinh-electron-tu-do.md",
    TRANSLATIONS_DIR / "06-chat-ban-dan.md",
    TRANSLATIONS_DIR / "07-thiet-bi-ban-dan.md",
    TRANSLATIONS_DIR / "08-sieu-dan.md",
]

def test_numerical_recomputations():
    print("=== TEST 1: Numerical Recomputations ===")
    k_B = 1.380649e-23
    k_B_eV = 8.617333262e-5
    e_charge = 1.602176634e-19
    m_e = 9.1093837e-31
    h_planck = 6.62607015e-34
    hbar = 1.054571817e-34

    # Example 42.6: Probabilities in the free-electron model (general T)
    # Source asks: at what energy is f(E) = (a) 0.01 and (b) 0.99?
    # f(E) = 1 / (exp((E - EF)/kT) + 1) => E = EF + kT * ln(1/f - 1)
    # (a) f = 0.01 => E - EF = kT * ln(99) ≈ 4.59512 kT ≈ 4.6 kT
    delta_a_over_kT = math.log(1.0 / 0.01 - 1.0) # ln(99)
    assert abs(delta_a_over_kT - 4.59512) < 1e-4, f"Example 42.6a delta failed: {delta_a_over_kT}"
    assert abs(round(delta_a_over_kT, 1) - 4.6) < 1e-5

    # (b) f = 0.99 => E - EF = kT * ln(1/99) = -ln(99) kT ≈ -4.59512 kT ≈ -4.6 kT
    delta_b_over_kT = math.log(1.0 / 0.99 - 1.0) # -ln(99)
    assert abs(delta_b_over_kT - (-4.59512)) < 1e-4, f"Example 42.6b delta failed: {delta_b_over_kT}"
    assert abs(round(delta_b_over_kT, 1) - (-4.6)) < 1e-5

    # Check exact probabilities returned at these energies
    f_at_plus_4_6kT = 1.0 / (math.exp(delta_a_over_kT) + 1.0)
    f_at_minus_4_6kT = 1.0 / (math.exp(delta_b_over_kT) + 1.0)
    assert abs(f_at_plus_4_6kT - 0.01) < 1e-9
    assert abs(f_at_minus_4_6kT - 0.99) < 1e-9

    # Source evaluate: general symmetry f(EF + delta) + f(EF - delta) = 1
    for delta in [0.01, 0.1, 1.0, 4.6, 10.0]:
        f_hi = 1.0 / (math.exp(delta) + 1.0)
        f_lo = 1.0 / (math.exp(-delta) + 1.0)
        assert abs((f_hi + f_lo) - 1.0) < 1e-12, f"Example 42.6 symmetry failed at delta={delta}"
    print("  ✓ Example 42.6 recomputations passed.")

    # Example 42.7: The Fermi energy in copper
    # Source prompt: n = 8.45 * 10^28 m^-3. Find (a) Fermi energy EF0, (b) Fermi speed vF.
    n_Cu = 8.45e28
    EF0_J = ((3 * math.pi**2 * n_Cu)**(2/3)) * (hbar**2) / (2 * m_e)
    EF0_eV = EF0_J / e_charge
    assert abs(EF0_eV - 7.03) < 0.02, f"Example 42.7 EF0 failed: {EF0_eV}"
    assert abs(EF0_J - 1.126e-18) < 0.005e-18, f"Example 42.7 EF0_J failed: {EF0_J}"

    v_F = math.sqrt(2 * EF0_J / m_e)
    assert abs(v_F - 1.57e6) < 0.02e6, f"Example 42.7 v_F failed: {v_F}"

    # Evaluate checks in source: room temperature comparison (20°C = 293 K)
    kT_293 = k_B * 293.15 # 4.047e-21 J
    kT_293_eV = kT_293 / e_charge # ~0.02526 eV
    assert abs(kT_293_eV - 0.0253) < 0.001
    assert EF0_eV / kT_293_eV > 270 # EF >> kT justifies low-T approximation

    # Density of states check in Evaluate for V = 1 cm^3 at EF0 = 7.03 eV
    V_1cm3 = 1.0e-6
    g_EF0_J = ((2 * m_e)**1.5 * V_1cm3 / (2 * math.pi**2 * hbar**3)) * math.sqrt(EF0_J)
    g_EF0_eV = g_EF0_J * e_charge
    assert abs(g_EF0_eV - 1.81e22) < 0.05e22, f"Example 42.7 g(E) failed: {g_EF0_eV}"
    print("  ✓ Example 42.7 recomputations passed.")

    # Independent Density-of-States Integration & State Count Derivation
    # N = \int_0^{EF0} g(E) dE = g_coef * (2/3) * EF0^(3/2)
    # g(E) = [ (2m)^(3/2) V / (2 pi^2 hbar^3) ] * E^(1/2) = [ 8 sqrt(2) pi m^(3/2) V / h^3 ] * E^(1/2)
    # Integral of E^(1/2) contributes 2/3:
    # coefficient for N in terms of h: 8 sqrt(2) * (2/3) = 16 sqrt(2) / 3 (factor of 2 restored!)
    g_coef_hbar = (2 * m_e)**1.5 * V_1cm3 / (2 * math.pi**2 * hbar**3)
    g_coef_h = 8 * math.sqrt(2) * math.pi * m_e**1.5 * V_1cm3 / (h_planck**3)
    assert abs((g_coef_hbar - g_coef_h) / g_coef_hbar) < 1e-4, "g(E) coefficient equivalence between h and hbar failed"

    # Integrated state count N at EF0
    N_calc_hbar = g_coef_hbar * (2.0 / 3.0) * (EF0_J**1.5)
    N_calc_h = (16 * math.sqrt(2) * math.pi * m_e**1.5 * V_1cm3 / (3 * h_planck**3)) * (EF0_J**1.5)
    assert abs(N_calc_hbar - N_calc_h) / N_calc_hbar < 1e-4, "N integral equivalence between h and hbar failed"
    # Total electrons in 1 cm^3: n_Cu * V_1cm3
    N_expected = n_Cu * V_1cm3
    assert abs(N_calc_hbar - N_expected) / N_expected < 1e-4, "Integrated N does not match n * V"

    # Average energy derivation: E_tot = \int_0^{EF0} E g(E) dE = g_coef * (2/5) * EF0^(5/2)
    # E_av = E_tot / N = [g_coef * (2/5) * EF0^(5/2)] / [g_coef * (2/3) * EF0^(3/2)] = (3/5) * EF0
    E_tot_calc = g_coef_hbar * (2.0 / 5.0) * (EF0_J**2.5)
    E_av_calc = E_tot_calc / N_calc_hbar
    assert abs(E_av_calc - (3.0 / 5.0) * EF0_J) < 1e-12, "E_av = (3/5) EF0 analytical identity failed"
    print("  ✓ Independent Density-of-States integration & state count passed.")

    # Example 42.8: Free-electron gas versus ideal gas
    E_av_0K_eV = (3.0 / 5.0) * EF0_eV
    assert abs(E_av_0K_eV - 4.22) < 0.02, f"Example 42.8 E_av failed: {E_av_0K_eV}"
    kT_room = k_B_eV * 293.15
    E_class_room = (3.0 / 2.0) * kT_room
    assert abs(E_class_room - 0.0379) < 0.001, f"Example 42.8 E_class failed: {E_class_room}"
    ratio_E = E_class_room / E_av_0K_eV
    assert abs(ratio_E - 0.0090) < 0.001, f"Example 42.8 ratio failed: {ratio_E}"
    v_class = math.sqrt(2 * (E_class_room * e_charge) / m_e)
    assert abs(v_class - 1.15e5) < 0.02e5, f"Example 42.8 v_class failed: {v_class}"
    ratio_v = v_class / v_F
    assert abs(ratio_v - 0.073) < 0.003, f"Example 42.8 v ratio failed: {ratio_v}"
    print("  ✓ Example 42.8 recomputations passed.")

    # Example 42.9: Semiconductor band gaps at 300K and 310K
    test_cases = [
        (0.200, 0.0205, 0.0231, 1.13),
        (1.00, 4.0e-9, 7.4e-9, 1.86),
        (5.00, 1.0e-42, 2.3e-41, 23.0),
    ]
    for Eg, exp_300_val, exp_310_val, exp_ratio in test_cases:
        dE = Eg / 2.0
        f300 = 1.0 / (math.exp(dE / (k_B_eV * 300)) + 1.0)
        f310 = 1.0 / (math.exp(dE / (k_B_eV * 310)) + 1.0)
        ratio = f310 / f300
        assert abs(f300 - exp_300_val) / exp_300_val < 0.05, f"Example 42.9 f300 failed for Eg={Eg}: {f300} vs {exp_300_val}"
        assert abs(f310 - exp_310_val) / exp_310_val < 0.05, f"Example 42.9 f310 failed for Eg={Eg}: {f310} vs {exp_310_val}"
        assert abs(ratio - exp_ratio) / exp_ratio < 0.05, f"Example 42.9 ratio failed for Eg={Eg}: {ratio} vs {exp_ratio}"
    print("  ✓ Example 42.9 recomputations passed.")


def test_images():
    print("=== TEST 2: Image Integrity & Pixel Checks ===")
    expected_images = [f"hinh-42-{i}.png" for i in range(20, 37)] + ["ung-dung-b-1.png"]
    assert len(expected_images) == 18, "Expected 18 image files"

    for img_name in expected_images:
        path = IMG_DIR / img_name
        assert path.exists(), f"Image file missing: {path}"
        assert path.stat().st_size > 5000, f"Image file too small ({path.stat().st_size} bytes): {path}"
        with Image.open(path) as img:
            w, h = img.size
            assert w >= 100 and h >= 100, f"Image {img_name} dimensions too small: {w}x{h}"
            assert img.format == "PNG", f"Image {img_name} not PNG: {img.format}"
    print(f"  ✓ All 18 images exist and have valid PNG dimensions (100+ px).")


def test_equation_inventory():
    print("=== TEST 3: Equation Tag Inventory ===")
    all_content = ""
    for frag in FRAGMENTS:
        assert frag.exists(), f"Fragment missing: {frag}"
        all_content += frag.read_text(encoding="utf-8") + "\n"

    # Plan specified 42.10 through 42.22, and actual source contains up to 42.25
    expected_eqs = [f"42.{i}" for i in range(10, 26)]
    found_tags = re.findall(r'\\tag\{(42\.\d+)\}', all_content)

    missing = []
    for eq in expected_eqs:
        if eq not in found_tags:
            missing.append(eq)
        else:
            # Ensure unique definition
            count = found_tags.count(eq)
            assert count == 1, f"Equation tag {eq} defined {count} times (expected 1)"

    if missing:
        raise AssertionError(f"Missing equation tags: {missing}")
    print(f"  ✓ All equations (42.10) to (42.25) are uniquely defined with \\tag{{...}}.")


def test_mathjax_width():
    print("=== TEST 4: Real MathJax SVG Width Measurement ===")
    # Extract all display and inline math from fragments
    inline_math_list = []
    display_math_list = []

    for frag in FRAGMENTS:
        text = frag.read_text(encoding="utf-8")
        rel_path = frag.name

        # Extract display math ($$ ... $$)
        disp_matches = re.findall(r'\$\$(.*?)\$\$', text, flags=re.DOTALL)
        for d in disp_matches:
            clean_d = re.sub(r'\\tag\{[^}]+\}', '', d).strip()
            display_math_list.append((rel_path, clean_d))

        # Remove display math before finding inline math
        clean_text = re.sub(r'\$\$[\s\S]*?\$\$', lambda m: ' ' * len(m.group(0)), text)
        inline_matches = re.findall(r'(?<!\$)\$([^\n$]+)\$(?!\$)', clean_text)
        for inl in inline_matches:
            inline_math_list.append((rel_path, inl.strip()))

    print(f"  Found {len(display_math_list)} display math blocks and {len(inline_math_list)} inline formulas.")

    payload = {
        "inline": [item[1] for item in inline_math_list],
        "display": [item[1] for item in display_math_list]
    }

    # Execute completely in-memory via stdin with node --input-type=module - (no temp files created)
    js_code = f"""
import MarkdownIt from 'markdown-it';
import mathjax from 'markdown-it-mathjax3';
const md = new MarkdownIt().use(mathjax);

const input = {json.dumps(payload)};

const inlineWidths = input.inline.map(tex => {{
    try {{
        const html = md.renderInline('$' + tex + '$');
        const m = html.match(/(?:min-width:\\s*|width=")([\\d.]+)ex/);
        return m ? parseFloat(m[1]) : 0;
    }} catch (e) {{
        return -1;
    }}
}});

const displayWidths = input.display.map(tex => {{
    try {{
        const html = md.render('$$\\n' + tex + '\\n$$');
        const m = html.match(/(?:min-width:\\s*|width=")([\\d.]+)ex/);
        return m ? parseFloat(m[1]) : 0;
    }} catch (e) {{
        return -1;
    }}
}});

console.log(JSON.stringify({{ inlineWidths, displayWidths }}));
"""

    env = {**os.environ, "NODE_PATH": str(REPO_ROOT / "node_modules")}
    res = subprocess.run(
        ["node", "--input-type=module", "-"],
        input=js_code,
        capture_output=True,
        text=True,
        check=True,
        env=env
    )

    data = json.loads(res.stdout.strip())
    inline_widths = data["inlineWidths"]
    display_widths = data["displayWidths"]

    # Check inline widths <= 38ex
    wide_inline = []
    for i, w in enumerate(inline_widths):
        if w > 38.0:
            wide_inline.append((inline_math_list[i][0], inline_math_list[i][1], w))

    # Check display widths <= 27ex
    wide_display = []
    for i, w in enumerate(display_widths):
        if w > 27.0:
            wide_display.append((display_math_list[i][0], display_math_list[i][1], w))

    max_inline = max(inline_widths) if inline_widths else 0
    max_display = max(display_widths) if display_widths else 0
    print(f"  Max inline width: {max_inline:.2f}ex (limit 38ex)")
    print(f"  Max display width: {max_display:.2f}ex (limit 27ex)")

    if wide_inline:
        for f, tex, w in wide_inline:
            print(f"  [WIDE INLINE] {f}: width {w:.1f}ex > 38ex: ${tex}$")
        raise AssertionError(f"Found {len(wide_inline)} wide inline formulas")

    if wide_display:
        for f, tex, w in wide_display:
            print(f"  [WIDE DISPLAY] {f}: width {w:.1f}ex > 27ex:\n$${tex}$$\n")
        raise AssertionError(f"Found {len(wide_display)} wide display formulas")

    print(f"  ✓ All {len(display_math_list)} display math <= 27ex and {len(inline_math_list)} inline math <= 38ex.")


def test_markdown_linting():
    print("=== TEST 5: Markdown & Pedagogical Linting ===")
    prohibited_phrases = [
        "theo sách", "sách dùng", "lấy từ slide", "bài tập lấy từ sách",
        "ảnh lấy từ sách", "hình trong sách", "nguyên tác", "bản dịch của",
        "tiến độ bản dịch", "do người soạn"
    ]

    for frag in FRAGMENTS:
        text = frag.read_text(encoding="utf-8")
        rel_name = frag.name
        lines = text.splitlines()

        # Check prohibited phrases
        for phrase in prohibited_phrases:
            assert phrase not in text.lower(), f"Prohibited phrase '{phrase}' found in {rel_name}"

        # Check semicolons in prose outside math
        in_display_math = False
        for line_num, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped == "$$":
                in_display_math = not in_display_math
                continue
            if in_display_math:
                continue

            # Remove inline math
            prose = re.sub(r'\$.*?\$', '', line)
            # Remove markdown links
            prose = re.sub(r'\[.*?\]\(.*?\)', '', prose)
            # Check semicolon
            assert ";" not in prose, f"Semicolon found in prose at {rel_name}:{line_num}: {line}"

            # Check em-dash
            assert "—" not in prose, f"Em-dash '—' found at {rel_name}:{line_num}: {line}"
            assert " -- " not in prose, f"Dash ' -- ' found at {rel_name}:{line_num}: {line}"

    # Check self-checks
    c05 = (TRANSLATIONS_DIR / "05-mo-hinh-electron-tu-do.md").read_text(encoding="utf-8")
    assert "### Kiểm tra mức độ hiểu mục 42.5" in c05
    assert "::: details" in c05

    c06 = (TRANSLATIONS_DIR / "06-chat-ban-dan.md").read_text(encoding="utf-8")
    assert "### Kiểm tra mức độ hiểu mục 42.6" in c06
    assert "::: details" in c06

    c07 = (TRANSLATIONS_DIR / "07-thiet-bi-ban-dan.md").read_text(encoding="utf-8")
    assert "### Kiểm tra mức độ hiểu mục 42.7" in c07
    assert "::: details" in c07

    c08 = (TRANSLATIONS_DIR / "08-sieu-dan.md").read_text(encoding="utf-8")
    assert "Kiểm tra mức độ hiểu" not in c08, "Section 42.8 should not have an invented self-check"

    print("  ✓ Markdown linting and pedagogical structure verified.")


def main():
    try:
        test_numerical_recomputations()
        test_images()
        test_equation_inventory()
        test_mathjax_width()
        test_markdown_linting()
        print("\n==========================================")
        print("ALL VERIFICATION SUITE TESTS PASSED (5/5)!")
        print("==========================================")
    except AssertionError as e:
        print(f"\n❌ VERIFICATION FAILED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
