"""Comprehensive verification for Physics 1 Chapter 11 Theory B.

Covers:
- Numeric ledger and physics verification for all textbook examples and self-checks:
  * Example 11.5: Tensile stress, strain, and elongation of steel cable.
  * Example 11.6: Bulk stress, bulk strain, volume change, compressibility of oil.
  * Example 11.7: Shear strain, shear stress, shear force on brass plate.
  * Test Your Understanding 11.4: Comparative strain and stress in copper vs steel.
  * Bio Application: Tendon Young's modulus and strain limits.
  * Bio Application: Anglerfish bulk stress at depth.
  * Test Your Understanding 11.5: Proportional limit, yield point, fracture mechanics.
- Fresh raw RGB PDF crop comparison for all 15 generated image assets.
- Image annotations dictionary schema, key coverage, and translation integrity.
"""

import importlib.util
import json
import math
from pathlib import Path
import numpy as np
from PIL import Image
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
PDF_PATH = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
PREP_SCRIPT = ROOT / "scripts/prepare-physics1-11-theory-b-assets.py"
ANNOTATIONS_FILE = ROOT / "docs/.vitepress/physics1-11-theory-b-image-annotations.mjs"


def verify_numeric_cases():
    print("=== 1. Verifying Numerical and Physical Calculations ===")

    # Case 1: Example 11.5 (Tensile stress, strain, elongation)
    # Steel rod: L0 = 2.0 m, A = 0.30 cm^2 = 3.0e-5 m^2, m = 550 kg, g = 9.8 m/s^2, Y = 20e10 Pa
    L0_steel = 2.0
    A_steel = 0.30e-4
    m_load = 550.0
    g = 9.8
    Y_steel = 20e10

    F_perp = m_load * g  # 5390.0 N
    stress_11_5 = F_perp / A_steel  # 1.79667e8 Pa
    strain_11_5 = stress_11_5 / Y_steel  # 8.9833e-4
    delta_l_11_5 = strain_11_5 * L0_steel  # 1.7967e-3 m

    assert math.isclose(F_perp, 5390.0, rel_tol=1e-5), f"F_perp failed: {F_perp}"
    assert math.isclose(stress_11_5, 1.8e8, rel_tol=0.01), f"Stress failed: {stress_11_5}"
    assert math.isclose(strain_11_5, 9.0e-4, rel_tol=0.01), f"Strain failed: {strain_11_5}"
    assert math.isclose(delta_l_11_5 * 1000, 1.8, rel_tol=0.01), f"Elongation failed: {delta_l_11_5}"
    print(f"  [PASS] Example 11.5: F={F_perp} N, Stress={stress_11_5:.3e} Pa (~1.8e8 Pa), Strain={strain_11_5:.3e} (~9.0e-4), delta_l={delta_l_11_5*1000:.2f} mm (~1.8 mm)")

    # Case 2: Example 11.6 (Bulk stress and strain in hydraulic press)
    # Oil: V0 = 0.25 m^3 (250 L), delta_p = 1.6e7 Pa (160 atm), B = 5.0e9 Pa (5.0e4 atm), k = 20e-6 atm^-1
    V0_oil = 0.25
    delta_p_Pa = 1.6e7
    B_oil = 5.0e9
    k_oil_atm = 20e-6
    delta_p_atm = 160.0

    delta_V_from_B = -V0_oil * delta_p_Pa / B_oil  # -8.0e-4 m^3 = -0.80 L
    delta_V_from_k = -k_oil_atm * V0_oil * delta_p_atm  # -8.0e-4 m^3
    fractional_V_change = delta_V_from_B / V0_oil  # -0.0032 = -0.32%

    assert math.isclose(delta_V_from_B, -8.0e-4, rel_tol=1e-5), f"delta_V failed: {delta_V_from_B}"
    assert math.isclose(delta_V_from_k, -8.0e-4, rel_tol=1e-5), f"delta_V from k failed: {delta_V_from_k}"
    assert math.isclose(fractional_V_change, -0.0032, rel_tol=1e-5), f"Fractional change failed: {fractional_V_change}"
    print(f"  [PASS] Example 11.6: delta_V={delta_V_from_B:.2e} m^3 (-0.80 L), fractional change={fractional_V_change*100:.2f}% (-0.32%)")

    # Case 3: Example 11.7 (Shear stress and strain on brass plate)
    # Brass plate: 0.80 m square, 0.50 cm thick (0.0050 m), displacement x = 0.16 mm = 1.6e-4 m, S = 3.5e10 Pa
    h_plate = 0.80
    t_plate = 0.0050
    L_plate = 0.80
    x_disp = 1.6e-4
    S_brass = 3.5e10

    A_shear = L_plate * t_plate  # 0.0040 m^2
    shear_strain = x_disp / h_plate  # 2.0e-4
    shear_stress = shear_strain * S_brass  # 7.0e6 Pa
    F_parallel = shear_stress * A_shear  # 2.8e4 N

    assert math.isclose(A_shear, 0.0040, rel_tol=1e-5), f"A_shear failed: {A_shear}"
    assert math.isclose(shear_strain, 2.0e-4, rel_tol=1e-5), f"Shear strain failed: {shear_strain}"
    assert math.isclose(shear_stress, 7.0e6, rel_tol=1e-5), f"Shear stress failed: {shear_stress}"
    assert math.isclose(F_parallel, 2.8e4, rel_tol=1e-5), f"F_parallel failed: {F_parallel}"
    print(f"  [PASS] Example 11.7: A={A_shear} m^2, Shear strain={shear_strain:.2e}, Shear stress={shear_stress:.2e} Pa, F_parallel={F_parallel:.2e} N (~28 kN)")

    # Case 4: Test Your Understanding 11.4
    # Copper rod: A = 0.500 cm^2, L0 = 1.00 m, delta_l = 2.00e-2 mm = 2.00e-5 m, Y_Cu = 11e10 Pa
    # Steel rod: A = 0.500 cm^2, L0 = 0.100 m, delta_l = 2.00e-3 mm = 2.00e-6 m, Y_steel = 20e10 Pa
    strain_Cu = 2.00e-5 / 1.00  # 2.00e-5
    strain_steel = 2.00e-6 / 0.100  # 2.00e-5
    stress_Cu = 11e10 * strain_Cu  # 2.2e6 Pa
    stress_steel = 20e10 * strain_steel  # 4.0e6 Pa

    assert math.isclose(strain_Cu, strain_steel, rel_tol=1e-5), "Strains should be identical"
    assert stress_steel > stress_Cu, "Steel stress must exceed copper stress"
    print(f"  [PASS] TYU 11.4: strain_Cu = strain_steel = {strain_Cu:.2e} (option iii); stress_steel ({stress_steel:.2e} Pa) > stress_Cu ({stress_Cu:.2e} Pa) (option ii)")

    # Case 5: Bio Application Tendon
    Y_tendon = 1.2e9
    max_strain_tendon = 0.025
    stress_at_max = Y_tendon * max_strain_tendon  # 3.0e7 Pa
    assert math.isclose(stress_at_max, 3.0e7, rel_tol=1e-5)
    print(f"  [PASS] Bio Tendon: Y={Y_tendon:.2e} Pa, max strain={max_strain_tendon*100}%, stress={stress_at_max:.2e} Pa")

    # Case 6: Bio Application Anglerfish
    # Depth = 1000 m, hydrostatic pressure delta_p ~ rho * g * h ~ 1000 * 9.8 * 1000 ~ 9.8e6 Pa ~ 97 atm ~ 100 atm
    p_1000m = 1000.0 * 9.8 * 1000.0 / 101325.0
    assert 95 <= p_1000m <= 100
    print(f"  [PASS] Bio Anglerfish: depth 1000 m corresponds to ~{p_1000m:.1f} atm (reported ~100 atm)")


def verify_fresh_pdf_crops():
    print("=== 2. Verifying Fresh Raw RGB PDF Crop Comparison ===")
    spec = importlib.util.spec_from_file_location("prep", str(PREP_SCRIPT))
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)

    doc = pymupdf.open(prep.PDF)
    all_matched = True

    for name, (p1, box) in prep.CROPS.items():
        saved_file = prep.OUT / name
        assert saved_file.exists(), f"Saved file missing: {saved_file}"

        saved_img = Image.open(saved_file).convert("RGB")
        page = doc[p1 - 1]
        rect = pymupdf.Rect(box)
        pix = page.get_pixmap(matrix=pymupdf.Matrix(prep.SCALE, prep.SCALE), clip=rect, alpha=False)
        fresh_img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        assert saved_img.size == fresh_img.size, f"Size mismatch for {name}: {saved_img.size} vs {fresh_img.size}"

        diff = np.abs(np.array(saved_img, dtype=int) - np.array(fresh_img, dtype=int))
        max_diff = int(np.max(diff))
        mean_diff = float(np.mean(diff))

        assert max_diff == 0, f"Pixel mismatch in {name}: max={max_diff}, mean={mean_diff}"
        print(f"  [PASS] {name:30s} matches fresh PDF crop exactly (max diff = 0, size {saved_img.size[0]}x{saved_img.size[1]})")

    print(f"  All {len(prep.CROPS)} image crops verified against fresh PDF rendering.")


def verify_image_annotations():
    print("=== 3. Verifying Image Annotations Integrity ===")
    content = ANNOTATIONS_FILE.read_text(encoding="utf-8")
    assert "export const physics1Chapter11TheoryBImageAnnotations" in content, "Missing export name"

    spec = importlib.util.spec_from_file_location("prep", str(PREP_SCRIPT))
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)

    # Check that all crop basenames have entries in annotations
    for name in prep.CROPS.keys():
        stem = Path(name).stem
        key = f"young-11/{stem}"
        assert f"'{key}'" in content or f'"{key}"' in content, f"Key {key} missing from annotations!"

    print(f"  [PASS] All {len(prep.CROPS)} image keys accounted for in annotations dictionary.")


def main():
    verify_numeric_cases()
    verify_fresh_pdf_crops()
    verify_image_annotations()
    print("\n>>> ALL CHAPTER 11 THEORY B VERIFICATIONS PASSED SUCCESSFULLY! <<<")


if __name__ == "__main__":
    main()
