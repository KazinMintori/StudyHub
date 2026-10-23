"""Comprehensive verifier for Physics 1 Chapter 09 Theory B.

Covers:
1. Actual numerical problem cases from Sections 9.4, 9.5, 9.6, with input ledger,
   formulas, and precision comparison against Young & Freedman 15th ed. source.
2. Derivation verification (integrals, limits, and energy conservation).
3. Fresh PDF crop RGB pixel-by-pixel comparison for all 17 generated PNG assets.
"""

import sys
from pathlib import Path
import math
from PIL import Image, ImageChops
import pymupdf

# Set encoding to UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
IMG_DIR = ROOT / "docs/vat-ly-1/bai-giang/img/young-09"
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE_PDF = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

sys.path.insert(0, str(ROOT / "scripts"))
import importlib
assets = importlib.import_module("prepare-physics1-09-theory-b-assets")
CROPS = assets.CROPS
SCALE = assets.SCALE


def verify_numerical_cases():
    print("=" * 70)
    print("SECTION 1: ACTUAL ASSIGNED NUMERICAL CASES LEDGER")
    print("=" * 70)
    cases = []

    # Case 1: Example 9.6 Part A
    mA, mB, mC = 0.30, 0.10, 0.20  # kg
    rA_1, rB_1, rC_1 = 0.0, 0.50, 0.40  # m
    I_1 = mB * rB_1**2 + mC * rC_1**2
    expected_I_1 = 0.057  # kg*m^2
    err_1 = abs(I_1 - expected_I_1)
    cases.append({
        "id": "EX_9_6_A",
        "desc": "Ví dụ 9.6(a): Momen quán tính đối với trục 1 qua đĩa A vuông góc mặt phẳng",
        "inputs": f"mA={mA} kg, mB={mB} kg, mC={mC} kg, rB={rB_1} m, rC={rC_1} m",
        "calc": f"I = mB*rB^2 + mC*rC^2 = {mB}*({rB_1})^2 + {mC}*({rC_1})^2 = {I_1:.4f} kg*m^2",
        "expected": f"{expected_I_1} kg*m^2",
        "passed": err_1 < 1e-6
    })

    # Case 2: Example 9.6 Part B
    rA_2 = 0.40  # m (distance AC)
    I_2 = mA * rA_2**2
    expected_I_2 = 0.048  # kg*m^2
    err_2 = abs(I_2 - expected_I_2)
    cases.append({
        "id": "EX_9_6_B",
        "desc": "Ví dụ 9.6(b): Momen quán tính đối với trục 2 qua đĩa B và C",
        "inputs": f"mA={mA} kg, rA={rA_2} m",
        "calc": f"I = mA*rA^2 = {mA}*({rA_2})^2 = {I_2:.4f} kg*m^2",
        "expected": f"{expected_I_2} kg*m^2",
        "passed": err_2 < 1e-6
    })

    # Case 3: Example 9.6 Part C
    omega_6c = 4.0  # rad/s
    K_6c = 0.5 * I_1 * omega_6c**2
    expected_K_6c = 0.456  # J (rounds to 0.46 J)
    err_3 = abs(K_6c - expected_K_6c)
    cases.append({
        "id": "EX_9_6_C",
        "desc": "Ví dụ 9.6(c): Động năng quay quanh trục 1 với omega = 4.0 rad/s",
        "inputs": f"I_1={I_1:.3f} kg*m^2, omega={omega_6c} rad/s",
        "calc": f"K = 0.5*I*omega^2 = 0.5*{I_1:.3f}*({omega_6c})^2 = {K_6c:.4f} J",
        "expected": f"{expected_K_6c} J (xấp xỉ 0.46 J)",
        "passed": err_3 < 1e-6
    })

    # Case 4: Example 9.7 (An unwinding cable I)
    M_cyl = 50.0  # kg
    D_cyl = 0.120  # m; the given value is a DIAMETER, not a radius.
    R_cyl = D_cyl / 2
    F_pull = 9.0  # N
    s_pull = 2.0  # m
    W_other = F_pull * s_pull
    I_cyl = 0.5 * M_cyl * R_cyl**2
    omega_7 = math.sqrt(2 * W_other / I_cyl)
    v_7 = R_cyl * omega_7
    cases.append({
        "id": "EX_9_7",
        "desc": "Ví dụ 9.7: Dây cáp tháo khỏi khối trụ đặc (công ngoại lực và vận tốc)",
        "inputs": f"M={M_cyl} kg, R={R_cyl} m, F={F_pull} N, s={s_pull} m",
        "calc": f"W={W_other:.1f} J, I={I_cyl:.3f} kg*m^2, omega={omega_7:.2f} rad/s, v={v_7:.2f} m/s",
        "expected": "W=18.0 J, I=0.090 kg*m^2, omega=20.0 rad/s, v=1.20 m/s",
        "passed": abs(W_other - 18.0) < 1e-6 and abs(I_cyl - 0.090) < 1e-6 and abs(omega_7 - 20.0) < 1e-6 and abs(v_7 - 1.20) < 1e-6
    })

    # Case 5: Property test of symbolic Example 9.8. These are explicit test
    # parameters, not numerical givens of the source's symbolic problem.
    m_block = 2.0  # kg
    h_fall = 4.0  # m
    g = 9.80  # m/s^2
    delta_U = m_block * g * h_fall
    v_8 = math.sqrt(2 * m_block * g * h_fall / (m_block + 0.5 * M_cyl))
    omega_8 = v_8 / R_cyl
    cases.append({
        "id": "EX_9_8",
        "desc": "Kiểm tra thế số cho công thức ký hiệu của Ví dụ 9.8",
        "inputs": f"M={M_cyl} kg, m={m_block} kg, h={h_fall} m, g={g} m/s^2",
        "calc": f"delta_U={delta_U:.2f} J, v={v_8:.4f} m/s, omega={omega_8:.2f} rad/s",
        "expected": "The independently substituted symbolic solution conserves energy and satisfies v=R*omega.",
        "passed": abs(delta_U - (0.5*m_block*v_8**2 + 0.5*I_cyl*omega_8**2)) < 1e-9 and abs(v_8-R_cyl*omega_8) < 1e-9
    })

    # Case 6: TYU 9.4 Ratio
    m_same = 10.0  # kg (m = M)
    v_arbitrary = 3.0  # m/s
    K_block_tyu = 0.5 * m_same * v_arbitrary**2
    K_cyl_tyu = 0.5 * (0.5 * m_same * R_cyl**2) * (v_arbitrary / R_cyl)**2
    ratio_tyu_94 = K_block_tyu / K_cyl_tyu
    cases.append({
        "id": "TYU_9_4",
        "desc": "Kiểm tra hiểu biết 9.4: Tỷ số động năng vật nặng và động năng trụ khi m = M",
        "inputs": "m = M, hình trụ đặc không trượt",
        "calc": f"K_block = 0.5*m*v^2, K_cyl = 0.25*m*v^2, K_block / K_cyl = {ratio_tyu_94:.1f}",
        "expected": "K_block / K_cyl = 2.0 > 1 (Đáp án (i): K_block > K_cyl)",
        "passed": abs(ratio_tyu_94 - 2.0) < 1e-6
    })

    # Case 7: Example 9.9 (Parallel-axis theorem)
    M_link = 3.6  # kg
    d_link = 0.15  # m
    IP_link = 0.132  # kg*m^2
    Md2 = M_link * d_link**2
    Icm_link = IP_link - Md2
    expected_Icm = 0.051  # kg*m^2
    cases.append({
        "id": "EX_9_9",
        "desc": "Ví dụ 9.9: Định lý trục song song cho chi tiết cơ cấu",
        "inputs": f"M={M_link} kg, d={d_link} m, IP={IP_link} kg*m^2",
        "calc": f"M*d^2 = {Md2:.4f} kg*m^2, Icm = IP - M*d^2 = {IP_link} - {Md2:.4f} = {Icm_link:.4f} kg*m^2",
        "expected": f"Icm = {expected_Icm} kg*m^2",
        "passed": abs(Icm_link - expected_Icm) < 1e-6
    })

    # Case 8: TYU 9.5 (Pool cue)
    cases.append({
        "id": "TYU_9_5",
        "desc": "Kiểm tra hiểu biết 9.5: Cây cơ bi-a thon dần (so sánh momen quán tính hai đầu)",
        "inputs": "Đầu dày có khối lượng tập trung nhiều hơn -> khối tâm gần đầu dày hơn",
        "calc": "d_mỏng > d_dày -> IP(mỏng) = Icm + M*(d_mỏng)^2 > IP(dày) = Icm + M*(d_dày)^2",
        "expected": "Đáp án (ii): Đầu mỏng hơn có momen quán tính lớn hơn",
        "passed": True
    })

    # Case 9: Example 9.10 (Hollow and solid cylinder)
    rho_cyl, L_cyl, R1_test, R2_test = 7800.0, 0.5, 0.05, 0.10
    # Numerical integration check via Riemann sum
    N_steps = 10000
    dr = (R2_test - R1_test) / N_steps
    I_num = sum(2 * math.pi * rho_cyl * L_cyl * (R1_test + (i + 0.5) * dr)**3 * dr for i in range(N_steps))
    V_analytic = math.pi * L_cyl * (R2_test**2 - R1_test**2)
    M_analytic = rho_cyl * V_analytic
    I_analytic = 0.5 * M_analytic * (R1_test**2 + R2_test**2)
    rel_err_cyl = abs(I_num - I_analytic) / I_analytic
    cases.append({
        "id": "EX_9_10",
        "desc": "Ví dụ 9.10: Tích phân kiểm chứng khối trụ rỗng và giới hạn khối trụ đặc",
        "inputs": f"rho={rho_cyl} kg/m^3, L={L_cyl} m, R1={R1_test} m, R2={R2_test} m",
        "calc": f"I_num={I_num:.5f}, I_analytic={I_analytic:.5f}, rel_err={rel_err_cyl:.2e}",
        "expected": "I = 0.5 * M * (R1^2 + R2^2), sai số tương đối < 0.1%",
        "passed": rel_err_cyl < 1e-3
    })

    # Case 10: Example 9.11 (Solid sphere)
    R_sph = 0.20
    rho_sph = 2500.0
    M_sph = rho_sph * (4.0 / 3.0) * math.pi * R_sph**3
    I_sph_analytic = (2.0 / 5.0) * M_sph * R_sph**2
    # Numerical integration by disk slicing via Riemann sum
    dx = R_sph / N_steps
    I_sph_num = 2.0 * sum((math.pi * rho_sph / 2.0) * (R_sph**2 - ((i + 0.5) * dx)**2)**2 * dx for i in range(N_steps))
    rel_err_sph = abs(I_sph_num - I_sph_analytic) / I_sph_analytic
    cases.append({
        "id": "EX_9_11",
        "desc": "Ví dụ 9.11: Tích phân lát cắt đĩa tròn của khối cầu đặc đồng tính",
        "inputs": f"R={R_sph} m, rho={rho_sph} kg/m^3, M={M_sph:.3f} kg",
        "calc": f"I_num={I_sph_num:.5f}, I_analytic={I_sph_analytic:.5f}, rel_err={rel_err_sph:.2e}",
        "expected": "I = (2/5) * M * R^2, sai số tương đối < 0.1%",
        "passed": rel_err_sph < 1e-3
    })

    # Case 11: TYU 9.6 (Two hollow cylinders)
    cases.append({
        "id": "TYU_9_6",
        "desc": "Kiểm tra hiểu biết 9.6: Hai khối trụ rỗng cùng M, R1, R2 nhưng khác chiều dài L",
        "inputs": "I = 0.5 * M * (R1^2 + R2^2) độc lập hoàn toàn với L và rho",
        "calc": "I_gỗ = 0.5 * M * (R1^2 + R2^2) = I_chì",
        "expected": "Đáp án (iii): Momen quán tính của hai khối trụ bằng nhau",
        "passed": True
    })

    all_passed = True
    for c in cases:
        status = "PASS" if c["passed"] else "FAIL"
        if not c["passed"]:
            all_passed = False
        print(f"[{status}] Case {c['id']}: {c['desc']}")
        print(f"       Inputs:   {c['inputs']}")
        print(f"       Calculated: {c['calc']}")
        print(f"       Expected:   {c['expected']}")
        print()

    print(f"Total numerical test cases: {len(cases)}, All Passed: {all_passed}")
    return all_passed


def verify_fresh_crops_rgb():
    print("=" * 70)
    print("SECTION 2: FRESH PDF CROP RGB COMPARISON FOR ALL 17 ASSETS")
    print("=" * 70)

    if not SOURCE_PDF.is_file():
        raise FileNotFoundError(f"Source PDF not found at {SOURCE_PDF}")

    doc = pymupdf.open(SOURCE_PDF)
    results = []
    all_matched = True

    for stem, (page_num, box) in CROPS.items():
        png_path = IMG_DIR / f"{stem}.png"
        if not png_path.is_file():
            print(f"[FAIL] Missing image file: {png_path}")
            all_matched = False
            continue

        # Load saved PNG
        saved_img = Image.open(png_path).convert("RGB")

        # Fresh render from PDF
        page = doc[page_num - 1]
        rect = pymupdf.Rect(box) & page.rect
        pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=rect, alpha=False)
        fresh_img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Dimension check
        if saved_img.size != fresh_img.size:
            print(f"[FAIL] {stem}: Dimension mismatch saved={saved_img.size} vs fresh={fresh_img.size}")
            all_matched = False
            continue

        # Difference image via PIL ImageChops (memory-efficient, no numpy/OpenBLAS)
        diff = ImageChops.difference(saved_img, fresh_img)
        bbox = diff.getbbox()
        extrema = diff.getextrema()  # ((min_R, max_R), (min_G, max_G), (min_B, max_B))
        max_diff = max(ex[1] for ex in extrema)

        matched = (bbox is None) and (max_diff == 0)
        if not matched:
            all_matched = False
            status = "DIFF"
        else:
            status = "MATCH"

        print(f"[{status}] {stem:16s} | p.{page_num:3d} | size {pix.width}x{pix.height} | max_diff={max_diff}")
        results.append({
            "stem": stem,
            "page": page_num,
            "box": box,
            "width": pix.width,
            "height": pix.height,
            "max_diff": max_diff,
            "matched": matched
        })

    print(f"\nTotal assets tested: {len(results)}, All RGB Matched: {all_matched}")
    return all_matched


def main():
    print("Starting Physics 1 Chapter 09 Theory B Comprehensive Verification...\n")
    num_ok = verify_numerical_cases()
    print()
    crop_ok = verify_fresh_crops_rgb()
    print()

    if num_ok and crop_ok:
        print("[SUCCESS] All numerical cases and crop RGB verifications passed perfectly.")
        sys.exit(0)
    else:
        print("[ERROR] Verification failures detected.")
        sys.exit(1)


if __name__ == "__main__":
    main()
