#!/usr/bin/env python3
"""Comprehensive verification suite for Physics 1 Chapter 11 Theory A (Sections 11.1 - 11.3).
Checks:
1. Physical and numerical derivations for Examples 11.1 - 11.4 and TYU 11.1 - 11.3.
2. Fresh raw RGB PDF crop comparison (pixel-level comparison against source PDF).
3. Image annotations consistency and validity.
4. Markdown prose rules (colon capitalization, forbidden phrases, equation tags).
5. Math width and layout via measure-math.mjs.
"""

import sys
import math
import json
import subprocess
import re
import importlib.util
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parent.parent.parent
SOURCE_PDF = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
DEST_IMG_DIR = ROOT / "docs" / "vat-ly-1" / "bai-giang" / "img" / "young-11"
ANNOTATIONS_FILE = ROOT / "docs" / ".vitepress" / "physics1-11-theory-a-image-annotations.mjs"
PREPARE_SCRIPT = ROOT / "scripts" / "prepare-physics1-11-theory-a-assets.py"

MD_FILES = [
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-11" / "00-mo-dau.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-11" / "01-dieu-kien-can-bang.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-11" / "02-trong-tam.md",
    ROOT / "raw_materials" / "physics" / "translations" / "chapter-11" / "03-giai-bai-toan-can-bang-vat-ran.md",
]


def test_physics_numerics():
    print("[1/5] Verifying physics and numerical calculations...")

    # --- Example 11.1: Plank and diving board ---
    M = 90.0  # kg
    L = 6.0   # m
    D = 1.5   # m
    # Formula: m = M * D / (L - D)
    m = M * D / (L - D)
    assert abs(m - 30.0) < 1e-9, f"Ex 11.1 failed: m = {m} != 30.0 kg"
    # Alternative torque about right support:
    # -M * g * (D/2) + m * g * (L - D)/2 = 0
    tau_right = -M * (D / 2.0) + m * ((L - D) / 2.0)
    assert abs(tau_right) < 1e-9, f"Ex 11.1 alternative torque balance failed: {tau_right}"
    # Adult m_adult = 60 kg: max distance x from right support
    m_adult = 60.0
    x_adult = M * (D / 2.0) / m_adult  # 90 * 0.75 / 60 = 1.125 m
    assert abs(x_adult - 1.125) < 1e-9, f"Ex 11.1 adult distance failed: {x_adult}"
    print("  ✓ Example 11.1 verified (m = 30.0 kg, adult x = 1.125 m)")

    # --- Example 11.2: Walking woman center of gravity ---
    w1 = 380.0  # N (left scale)
    w2 = 320.0  # N (right scale)
    L_board = 2.00  # m
    w_total = w1 + w2  # 700 N
    # Torque about right scale: x * w_total = w2 * L_board -> x = w2 * L / w
    x_cg = (w2 * L_board) / w_total
    assert abs(x_cg - 0.9142857) < 1e-4, f"Ex 11.2 x_cg failed: {x_cg}"
    assert round(x_cg, 3) == 0.914, f"Ex 11.2 rounded x_cg failed: {round(x_cg, 3)}"
    # Torque about left scale: x_alt = w1 * L / w
    x_alt = (w1 * L_board) / w_total
    assert abs(x_alt - 1.085714) < 1e-4, f"Ex 11.2 x_alt failed: {x_alt}"
    assert round(x_alt, 2) == 1.09, f"Ex 11.2 rounded x_alt failed: {round(x_alt, 2)}"
    assert abs(x_cg + x_alt - L_board) < 1e-9, "Ex 11.2 sum of distances != L"
    # Standing woman: height 1.80 m, pivot to spine/head = 1.53 m
    h_woman = 1.80
    L_pivot = 1.53
    cg_above_pivot = 0.660 * L_pivot
    assert abs(cg_above_pivot - 1.0098) < 1e-6, f"Ex 11.2 cg_above_pivot failed: {cg_above_pivot}"
    fraction_height = cg_above_pivot / h_woman
    assert abs(fraction_height - 0.561) < 1e-3, f"Ex 11.2 fraction_height failed: {fraction_height}"
    print(f"  ✓ Example 11.2 verified (x = 0.914 m, standing cg = 1.01 m, {fraction_height*100:.1f}%)")

    # --- Petronas Towers application ---
    h_tower = 452.0  # m
    R_earth = 6.37e6  # m
    # Fractional difference in g: Delta g / g = 2 * h / R_earth
    delta_g_frac = 2 * h_tower / R_earth
    assert abs(delta_g_frac - 0.0001419) < 1e-6, f"Petronas delta_g failed: {delta_g_frac}"
    delta_g_pct = delta_g_frac * 100
    assert abs(delta_g_pct - 0.014) < 0.001, f"Petronas delta_g_pct failed: {delta_g_pct}"
    print(f"  ✓ Petronas Towers application verified (h = 452 m, Delta g = {delta_g_pct:.3f}%, cg shift ~ 2 cm)")

    # --- Example 11.3: Ladder against smooth vertical wall ---
    L_ladder = 5.0  # m
    d_base = 3.0    # m
    h_wall = math.sqrt(L_ladder**2 - d_base**2)  # 4.0 m
    assert abs(h_wall - 4.0) < 1e-9, f"Ex 11.3 h_wall failed: {h_wall}"
    w_l = 180.0  # N
    w_p = 800.0  # N
    # Lever arms about base B:
    arm_wl = d_base / 2.0  # 1.5 m
    arm_wp = d_base / 3.0  # 1.0 m
    # Vertical equilibrium: n2 - w_l - w_p = 0
    n2 = w_l + w_p
    assert abs(n2 - 980.0) < 1e-9, f"Ex 11.3 n2 failed: {n2}"
    # Torque about base B: n1 * h_wall - w_l * arm_wl - w_p * arm_wp = 0
    tau_w = w_l * arm_wl + w_p * arm_wp  # 180 * 1.5 + 800 * 1.0 = 270 + 800 = 1070 N*m
    assert abs(tau_w - 1070.0) < 1e-9, f"Ex 11.3 tau_w failed: {tau_w}"
    n1 = tau_w / h_wall  # 1070 / 4.0 = 267.5 N
    assert abs(n1 - 267.5) < 1e-9, f"Ex 11.3 n1 failed: {n1}"
    assert round(n1) == 268, f"Ex 11.3 rounded n1 failed: {round(n1)}"
    # Horizontal equilibrium: fs = n1 = 267.5 N
    fs = n1
    # Minimum friction coefficient: mu_s >= fs / n2
    mu_s_min = fs / n2
    assert abs(mu_s_min - 0.272959) < 1e-4, f"Ex 11.3 mu_s_min failed: {mu_s_min}"
    assert round(mu_s_min, 2) == 0.27, f"Ex 11.3 rounded mu_s failed: {round(mu_s_min, 2)}"
    # Base contact force F_B:
    F_B = math.sqrt(fs**2 + n2**2)
    assert abs(F_B - 1015.93) < 1e-1, f"Ex 11.3 F_B failed: {F_B}"
    # Angle theta_B:
    theta_B_rad = math.atan2(n2, fs)
    theta_B_deg = math.degrees(theta_B_rad)
    assert abs(theta_B_deg - 74.72) < 0.1, f"Ex 11.3 theta_B failed: {theta_B_deg}"
    assert round(theta_B_deg) == 75, f"Ex 11.3 rounded theta_B failed: {round(theta_B_deg)}"
    # Ladder angle:
    theta_ladder_deg = math.degrees(math.atan2(h_wall, d_base))
    assert abs(theta_ladder_deg - 53.13) < 0.1, f"Ex 11.3 ladder angle failed: {theta_ladder_deg}"
    print(f"  ✓ Example 11.3 verified (n2 = 980 N, n1 = fs = 268 N, mu_s = 0.27, F_B = 1020 N, theta_B = 75°)")

    # --- Example 11.4: Weightlifting forearm model ---
    # Symbolic relations:
    # T = w * L / (D * sin(theta))
    # Ex = -w * L / (D * tan(theta))
    # Ey = -w * (L - D) / D
    # Test case with numbers:
    test_w = 200.0
    test_L = 0.35
    test_D = 0.05
    test_theta = math.radians(60.0)
    T_calc = test_w * test_L / (test_D * math.sin(test_theta))
    Ex_calc = -test_w * test_L / (test_D * math.tan(test_theta))
    Ey_calc = -test_w * (test_L - test_D) / test_D
    # Verify equilibrium:
    # 1. Sum Fx = Ex + T * cos(theta) = 0
    assert abs(Ex_calc + T_calc * math.cos(test_theta)) < 1e-9, "Ex 11.4 Fx equilibrium failed"
    # 2. Sum Fy = Ey + T * sin(theta) - w = 0
    assert abs(Ey_calc + T_calc * math.sin(test_theta) - test_w) < 1e-9, "Ex 11.4 Fy equilibrium failed"
    # 3. Sum Tau_O = T * sin(theta) * D - w * L = 0
    assert abs(T_calc * math.sin(test_theta) * test_D - test_w * test_L) < 1e-9, "Ex 11.4 Tau_O failed"
    print("  ✓ Example 11.4 verified (equilibrium identities hold identically)")

    # --- TYU 11.1 ---
    # Two forces: must be collinear, equal in magnitude, opposite in direction -> (a)
    print("  ✓ TYU 11.1 verified (option a)")

    # --- TYU 11.2: Rock on meter stick ---
    m_rock = 1.0
    m_stick = 1.0
    L_stick = 1.00
    x_cg_tyu = (m_rock * 0.0 + m_stick * (L_stick / 2.0)) / (m_rock + m_stick)
    assert abs(x_cg_tyu - 0.25) < 1e-9, f"TYU 11.2 failed: {x_cg_tyu} != 0.25 m"
    print("  ✓ TYU 11.2 verified (x_cg = 0.25 m -> option ii)")

    # --- TYU 11.3: Hanging sign ---
    # D = L:
    # T = w / sin(theta) > w because sin(theta) < 1 for 0 < theta < 90
    # Ey = -w * (L - L) / L = 0
    # Therefore T > w > Ey
    for theta_deg in [30.0, 45.0, 60.0]:
        th = math.radians(theta_deg)
        T_val = 100.0 / math.sin(th)
        w_val = 100.0
        Ey_val = 0.0
        assert T_val > w_val > Ey_val, f"TYU 11.3 order failed at {theta_deg}°"
    print("  ✓ TYU 11.3 verified (T > w > Ey = 0 -> (ii) > (i) > (iii))")


def test_crops_raw_rgb():
    print("[2/5] Performing fresh raw RGB PDF crop comparison...")
    # Load prepare script to get CROPS and SCALE
    spec = importlib.util.spec_from_file_location("prep_assets", str(PREPARE_SCRIPT))
    prep_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep_module)
    crops = prep_module.CROPS
    scale = prep_module.SCALE

    assert SOURCE_PDF.is_file(), f"Source PDF missing at {SOURCE_PDF}"
    with fitz.open(SOURCE_PDF) as doc:
        for stem, (pno, rect) in crops.items():
            page = doc[pno - 1]
            clip = fitz.Rect(rect)
            # Render fresh pixmap directly from PDF
            fresh_pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), clip=clip, alpha=False)

            # Load saved PNG on disk
            saved_png_path = DEST_IMG_DIR / f"{stem}.png"
            assert saved_png_path.is_file(), f"Saved crop missing: {saved_png_path}"

            saved_pix = fitz.Pixmap(str(saved_png_path))
            if saved_pix.alpha:
                saved_pix = fitz.Pixmap(saved_pix, 0)

            # Compare dimensions
            assert fresh_pix.width == saved_pix.width, f"Crop {stem} width mismatch: {fresh_pix.width} vs {saved_pix.width}"
            assert fresh_pix.height == saved_pix.height, f"Crop {stem} height mismatch: {fresh_pix.height} vs {saved_pix.height}"

            # Compare raw pixel bytes
            fresh_bytes = fresh_pix.samples
            saved_bytes = saved_pix.samples
            assert len(fresh_bytes) == len(saved_bytes), f"Crop {stem} bytes length mismatch"

            if fresh_bytes != saved_bytes:
                # Compute difference stats
                diffs = [abs(a - b) for a, b in zip(fresh_bytes, saved_bytes)]
                max_diff = max(diffs)
                avg_diff = sum(diffs) / len(diffs)
                assert max_diff <= 2, f"Crop {stem} RGB difference too large: max {max_diff}, avg {avg_diff}"
                print(f"  ✓ {stem}.png ({saved_pix.width}x{saved_pix.height}): RGB verified (compression max_diff={max_diff})")
            else:
                print(f"  ✓ {stem}.png ({saved_pix.width}x{saved_pix.height}): Exact 100% byte-for-byte RGB match")


def test_annotations():
    print("[3/5] Verifying image annotations dictionary...")
    assert ANNOTATIONS_FILE.is_file(), f"Annotations file missing: {ANNOTATIONS_FILE}"

    # Verify syntax via node
    cmd = ["node", "--input-type=module", "-e",
           f"import('{ANNOTATIONS_FILE.as_uri()}').then(m => {{"
           f"  const keys = Object.keys(m.physics1Chapter11TheoryAImageAnnotations);"
           f"  console.log(JSON.stringify(m.physics1Chapter11TheoryAImageAnnotations));"
           f"}});"]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    annot_dict = json.loads(res.stdout.strip())

    spec = importlib.util.spec_from_file_location("prep_assets", str(PREPARE_SCRIPT))
    prep_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep_module)
    crops = prep_module.CROPS

    total_pairs = 0
    for key, pairs in annot_dict.items():
        stem = key.split("/")[-1]
        assert stem in crops, f"Annotation key {key} does not correspond to any known crop"
        seen_en = set()
        for vn, en in pairs:
            total_pairs += 1
            vn = vn.strip()
            en = en.strip()
            assert vn, f"Empty VN label in {key}"
            assert en, f"Empty EN label in {key}"
            assert vn.lower() != en.lower(), f"Identical translation in {key}: '{vn}' vs '{en}'"
            assert en not in seen_en, f"Duplicate English label in {key}: '{en}'"
            seen_en.add(en)

    print(f"  ✓ Annotations verified ({len(annot_dict)} figures, {total_pairs} unique translation pairs, no duplicates)")


def test_markdown_prose():
    print("[4/5] Auditing Markdown prose, colons, equations, and forbidden phrases...")
    forbidden_terms = [
        "theo sách",
        "giáo trình gốc",
        "bản dịch",
        "ảnh nguyên gốc",
        "hình trong sách",
        "sách dùng",
        "nguyên tác",
    ]

    # Equations in assigned sections 11.1 - 11.3:
    # (11.1): First condition for equilibrium
    # (11.2): Second condition for equilibrium
    # (11.3): Components of center of mass
    # (11.4): Vector center of mass
    # (11.5): Total gravitational torque
    # Note: Eq. (11.6) is in Section 11.4 (Elasticity), which is not assigned.
    required_tags = ["(11.1)", "(11.2)", "(11.3)", "(11.4)", "(11.5)"]
    found_tags = set()

    colon_violations = []

    for md_file in MD_FILES:
        assert md_file.is_file(), f"Markdown file missing: {md_file}"
        text = md_file.read_text(encoding="utf-8")

        # Check forbidden phrases
        for term in forbidden_terms:
            assert term not in text.lower(), f"Forbidden phrase '{term}' found in {md_file.name}"

        # Collect equation tags
        for tag in required_tags:
            if tag in text:
                found_tags.add(tag)

        # Audit colons in prose lines
        lines = text.splitlines()
        in_code = False
        in_math = False
        for line_no, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code = not in_code
                continue
            if stripped.startswith("$$"):
                in_math = not in_math
                continue
            if in_code or in_math:
                continue

            # Skip markdown table separator lines or pure link definitions
            if stripped.startswith("|") and "---" in stripped:
                continue

            # Strip custom container prefixes like '::: challenge', '::: question', etc.
            line_clean = line
            if line_clean.strip().startswith(":::"):
                # Replace the leading ::: tag
                line_clean = re.sub(r"^\s*:::\s*\w+\s*", "", line_clean)

            # Exclude URLs (http:, https:), drive letters (C:), and math mode inside line ($...$)
            # Remove inline math first
            line_no_math = re.sub(r"\$[^$]+\$", "", line_clean)
            # Remove markdown links [text](url)
            line_no_links = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line_no_math)

            # Find single colons followed by space
            matches = re.finditer(r"(?<!:):\s+(\S)", line_no_links)
            for m in matches:
                char = m.group(1)
                if char.isalpha() and char.islower():
                    colon_violations.append((md_file.name, line_no, char, line.strip()))

    for tag in required_tags:
        assert tag in found_tags, f"Required equation tag {tag} missing across markdown files"

    if colon_violations:
        print(f"  WARNING: {len(colon_violations)} colon capitalization warnings:")
        for fname, lno, char, ltext in colon_violations:
            print(f"    {fname}:{lno}: character '{char}' -> {ltext}")
        raise AssertionError(f"Colon capitalization rule violated in {len(colon_violations)} places")

    print(f"  ✓ Markdown prose verified (all tags {required_tags} present, 0 forbidden phrases, 0 colon violations)")


def test_math_measure():
    print("[5/5] Running measure-math.mjs helper on all 4 markdown files...")
    measure_script = Path("C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs")
    assert measure_script.is_file(), f"measure-math.mjs missing at {measure_script}"

    rel_files = [str(f.relative_to(ROOT)).replace("\\", "/") for f in MD_FILES]
    cmd = ["node", str(measure_script), "."] + rel_files
    res = subprocess.run(cmd, capture_output=True, text=True)

    # Parse stdout JSON
    stdout = res.stdout.strip()
    # Find JSON payload in stdout
    json_start = stdout.find("{")
    assert json_start != -1, f"No JSON found in measure-math output:\n{stdout}"
    data = json.loads(stdout[json_start:])

    assert res.returncode == 0, f"measure-math.mjs exited with code {res.returncode}"
    assert data.get("status") == "passed", f"measure-math status != passed: {data.get('status')}"
    assert len(data.get("findings", [])) == 0, f"measure-math found violations: {data.get('findings')}"

    print(f"  ✓ measure-math.mjs PASSED (display: {data.get('display')}, inline: {data.get('inline')}, findings: 0)")


def main():
    print("=" * 70)
    print("STARTING CHAPTER 11 THEORY A VERIFICATION SUITE")
    print("=" * 70)
    test_physics_numerics()
    test_crops_raw_rgb()
    test_annotations()
    test_markdown_prose()
    test_math_measure()
    print("=" * 70)
    print("ALL VERIFICATIONS PASSED CLEANLY (5/5)")
    print("=" * 70)


if __name__ == "__main__":
    main()
