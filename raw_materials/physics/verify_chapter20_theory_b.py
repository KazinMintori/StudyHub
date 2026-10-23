#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification suite for Physics 1 Chapter 20 Theory B.
Verifies all numerical examples, self-checks, derivations, and image assets.
"""

from pathlib import Path
import math
import os
import sys
import subprocess
import json
import fitz
from PIL import Image, ImageChops

PDF_PATH = "raw_materials/physics/source/young-freedman-15.pdf"
IMG_DIR = "docs/vat-ly-1/bai-giang/img/young-20"


def check(condition, message):
    if not condition:
        print(f"FAIL: {message}")
        return False
    print(f"PASS: {message}")
    return True


def verify_math_measurements():
    print("\n--- Verifying Math Formatting & Width via measure-math.mjs ---")
    files = [
        "raw_materials/physics/translations/chapter-20/05-nguyen-ly-thu-hai.md",
        "raw_materials/physics/translations/chapter-20/06-chu-trinh-carnot.md",
        "raw_materials/physics/translations/chapter-20/07-entropy.md",
        "raw_materials/physics/translations/chapter-20/08-giai-thich-vi-mo-entropy.md",
        "raw_materials/physics/translations/chapter-20/17-tom-tat.md",
    ]
    script = str(Path(__file__).resolve().parents[2] / "scripts/verification/measure-physics-math.mjs")
    cmd = ["node", script, "."] + files
    res = subprocess.run(cmd, cwd=Path(__file__).resolve().parents[2], capture_output=True, text=True, encoding="utf-8")
    out = res.stdout
    start = out.find("{")
    end = out.rfind("}")
    if start == -1 or end == -1:
        print("FAIL: could not parse measure-math.mjs output")
        print(out)
        return False
    data = json.loads(out[start : end + 1])
    findings = data.get("findings", [])
    if not findings:
        disp = data.get("display", 0)
        inl = data.get("inline", 0)
        print(f"PASS: measure-math.mjs passed with 0 findings across {len(files)} files (display: {disp}, inline: {inl})")
        return True
    print(f"FAIL: measure-math.mjs reported {len(findings)} findings:")
    for f in findings:
        f_file = os.path.basename(f.get("file", ""))
        f_line = f.get("line", "")
        f_kind = f.get("kind", "")
        f_width = f.get("width", "")
        f_tex = f.get("tex", "")[:50]
        print(f"  {f_file}:{f_line} [{f_kind}] width={f_width} tex={f_tex}")
    return False


def verify_example_20_2():
    print("\n--- Verifying Example 20.2 (Carnot engine I) ---")
    QH = 2000.0  # J
    TH = 500.0   # K
    TC = 350.0   # K

    QC = -QH * (TC / TH)
    W = QH + QC
    e_calc = 1.0 - (TC / TH)
    e_def = W / QH

    ok = True
    ok &= check(math.isclose(QC, -1400.0, rel_tol=1e-5), f"QC = {QC} J (expected -1400 J)")
    ok &= check(math.isclose(W, 600.0, rel_tol=1e-5), f"W = {W} J (expected 600 J)")
    ok &= check(math.isclose(e_calc, 0.30, rel_tol=1e-5), f"e_calc = {e_calc*100:.1f}% (expected 30%)")
    ok &= check(math.isclose(e_def, 0.30, rel_tol=1e-5), f"e_def = {e_def*100:.1f}% (expected 30%)")
    return ok


def verify_example_20_3():
    print("\n--- Verifying Example 20.3 (Carnot engine II) ---")
    n = 0.200       # mol
    gamma = 1.40
    CV = 20.8       # J/(mol*K)
    R = 8.314       # J/(mol*K)
    TH = 500.0      # K (227 C)
    TC = 300.0      # K (27 C)
    pa = 10.0e5     # Pa

    # Point a
    Va = (n * R * TH) / pa  # 8.314e-4 m3
    # Point b (isothermal expansion, volume doubles)
    Vb = 2.0 * Va          # 16.628e-4 m3
    pb = (pa * Va) / Vb    # 5.0e5 Pa

    # Point c (adiabatic expansion: TH * Vb^(gamma-1) = TC * Vc^(gamma-1))
    exp_factor = 1.0 / (gamma - 1.0)  # 2.5
    Vc = Vb * ((TH / TC) ** exp_factor)
    pc = (n * R * TC) / Vc

    # Point d (adiabatic compression: TC * Vd^(gamma-1) = TH * Va^(gamma-1))
    Vd = Va * ((TH / TC) ** exp_factor)
    pd = (n * R * TC) / Vd

    ok = True
    ok &= check(math.isclose(Va, 8.314e-4, rel_tol=1e-3), f"Va = {Va*1e4:.2f}e-4 m3 (textbook: 8.31e-4 m3)")
    ok &= check(math.isclose(Vb, 16.628e-4, rel_tol=1e-3), f"Vb = {Vb*1e4:.2f}e-4 m3 (textbook: 16.6e-4 m3)")
    ok &= check(math.isclose(pb, 5.0e5, rel_tol=1e-5), f"pb = {pb*1e-5:.2f}e5 Pa (textbook: 5.00e5 Pa)")
    ok &= check(math.isclose(Vc, 59.6e-4, rel_tol=1e-2), f"Vc = {Vc*1e4:.1f}e-4 m3 (textbook: 59.6e-4 m3)")
    ok &= check(math.isclose(pc, 0.837e5, rel_tol=1e-2), f"pc = {pc*1e-5:.3f}e5 Pa (textbook: 0.837e5 Pa)")
    ok &= check(math.isclose(Vd, 29.8e-4, rel_tol=1e-2), f"Vd = {Vd*1e4:.1f}e-4 m3 (textbook: 29.8e-4 m3)")
    ok &= check(math.isclose(pd, 1.67e5, rel_tol=1e-2), f"pd = {pd*1e-5:.2f}e5 Pa (textbook: 1.67e5 Pa)")

    # Energy calculations
    Wab = n * R * TH * math.log(Vb / Va)  # 576.28 J
    Qab = Wab
    dUab = 0.0

    Qbc = 0.0
    Wbc = n * CV * (TH - TC)              # 832.0 J
    dUbc = -Wbc

    Wcd = n * R * TC * math.log(Vd / Vc)  # -345.77 J
    Qcd = Wcd
    dUcd = 0.0

    Qda = 0.0
    Wda = n * CV * (TC - TH)              # -832.0 J
    dUda = -Wda

    W_net = Wab + Wbc + Wcd + Wda
    Q_net = Qab + Qbc + Qcd + Qda
    dU_net = dUab + dUbc + dUcd + dUda

    ok &= check(math.isclose(Wab, 576.0, abs_tol=1.0), f"Wab = {Wab:.1f} J (textbook: 576 J)")
    ok &= check(math.isclose(Wbc, 832.0, rel_tol=1e-5), f"Wbc = {Wbc:.1f} J (textbook: 832 J)")
    ok &= check(math.isclose(Wcd, -346.0, abs_tol=1.0), f"Wcd = {Wcd:.1f} J (textbook: -346 J)")
    ok &= check(math.isclose(Wda, -832.0, rel_tol=1e-5), f"Wda = {Wda:.1f} J (textbook: -832 J)")
    ok &= check(math.isclose(W_net, 230.0, abs_tol=1.0), f"W_net = {W_net:.1f} J (textbook: 230 J)")
    ok &= check(math.isclose(Q_net, 230.0, abs_tol=1.0), f"Q_net = {Q_net:.1f} J (textbook: 230 J)")
    ok &= check(math.isclose(dU_net, 0.0, abs_tol=1e-5), f"dU_net = {dU_net:.1f} J (expected 0 J)")

    # Efficiency
    e_net = W_net / Qab
    e_carnot = (TH - TC) / TH
    ok &= check(math.isclose(e_net, 0.40, abs_tol=0.01), f"e_net = {e_net*100:.1f}% (textbook: 40%)")
    ok &= check(math.isclose(e_carnot, 0.40, rel_tol=1e-5), f"e_carnot = {e_carnot*100:.1f}% (textbook: 40%)")
    return ok


def verify_example_20_4():
    print("\n--- Verifying Example 20.4 (Carnot refrigerator) ---")
    QC = 346.0  # J
    W = 230.0   # J
    TH = 500.0  # K
    TC = 300.0  # K

    K_def = QC / W
    K_carnot = TC / (TH - TC)

    ok = True
    ok &= check(math.isclose(K_def, 1.50, abs_tol=0.01), f"K_def = {K_def:.2f} (textbook: 1.50)")
    ok &= check(math.isclose(K_carnot, 1.50, rel_tol=1e-5), f"K_carnot = {K_carnot:.2f} (textbook: 1.50)")
    return ok


def verify_tyu_20_6():
    print("\n--- Verifying TYU 20.6 (Copper engine efficiency) ---")
    TC = 300.0   # K
    TH = 1356.0  # K (copper melting point)
    e_max = 1.0 - (TC / TH)

    ok = check(math.isclose(e_max, 0.7788, rel_tol=1e-3), f"e_max = {e_max*100:.1f}% < 85% (cannot attain 85%)")
    return ok


def verify_example_20_5():
    print("\n--- Verifying Example 20.5 (Entropy of melting ice) ---")
    m = 1.00       # kg
    Lf = 3.34e5    # J/kg
    T = 273.0      # K
    Q = m * Lf
    dS = Q / T

    ok = check(math.isclose(dS, 1.22e3, rel_tol=5e-3), f"dS = {dS:.2f} J/K (textbook: 1.22e3 J/K)")
    return ok


def verify_example_20_6():
    print("\n--- Verifying Example 20.6 (Entropy in heating water) ---")
    m = 1.00       # kg
    c = 4190.0     # J/(kg*K)
    T1 = 273.0     # K
    T2 = 373.0     # K
    dS = m * c * math.log(T2 / T1)

    ok = check(math.isclose(dS, 1.31e3, rel_tol=5e-3), f"dS = {dS:.1f} J/K (textbook: 1.31e3 J/K)")
    return ok


def verify_example_20_9():
    print("\n--- Verifying Example 20.9 (Entropy in Carnot cycle) ---")
    QH = 2000.0  # J
    TH = 500.0   # K
    QC = -1400.0 # J
    TC = 350.0   # K

    dSH = QH / TH
    dSC = QC / TC
    dStot = dSH + dSC

    ok = True
    ok &= check(math.isclose(dSH, 4.0, rel_tol=1e-5), f"dSH = {dSH} J/K (expected +4.0 J/K)")
    ok &= check(math.isclose(dSC, -4.0, rel_tol=1e-5), f"dSC = {dSC} J/K (expected -4.0 J/K)")
    ok &= check(math.isclose(dStot, 0.0, abs_tol=1e-5), f"dStot = {dStot} J/K (expected 0.0 J/K)")
    return ok


def verify_example_20_10():
    print("\n--- Verifying Example 20.10 (Entropy in irreversible mixing) ---")
    m = 1.00       # kg
    c = 4190.0     # J/(kg*K)
    T_hot = 373.0  # K
    T_cold = 273.0 # K
    T_final = 323.0# K

    dSH = m * c * math.log(T_final / T_hot)
    dSC = m * c * math.log(T_final / T_cold)
    dStot = dSH + dSC

    ok = True
    ok &= check(math.isclose(dSH, -603.0, abs_tol=1.0), f"dSH = {dSH:.1f} J/K (textbook: -603 J/K)")
    ok &= check(math.isclose(dSC, 705.0, abs_tol=1.0), f"dSC = {dSC:.1f} J/K (textbook: +705 J/K)")
    ok &= check(math.isclose(dStot, 102.0, abs_tol=1.0), f"dStot = {dStot:.1f} J/K (textbook: +102 J/K)")
    return ok


def verify_section_20_8_microscopic():
    print("\n--- Verifying Microscopic States and Probabilities (Section 20.8) ---")
    # 4 coins: N=4
    # w = C(4, k)
    w_values = [math.comb(4, k) for k in range(5)]
    expected_w = [1, 4, 6, 4, 1]
    ok = check(w_values == expected_w, f"w for 4 coins: {w_values} (expected {expected_w})")
    total_w = sum(w_values)
    ok &= check(total_w == 16, f"Total microstates: {total_w} (expected 16 = 2^4)")

    # Example 20.11: free expansion doubling volume
    # dS = k * ln(2^N) = N * k * ln(2) = n * R * ln(2)
    # Check that symbolic equivalence holds
    R = 8.314462618
    NA = 6.02214076e23
    kB = 1.380649e-23
    ok &= check(math.isclose(R, NA * kB, rel_tol=1e-5), f"R = NA * kB ({R:.5f} vs {NA*kB:.5f})")
    return ok


def verify_image_crops_fresh_rgb():
    print("\n--- Verifying Image Crops against Fresh PDF Renders ---")
    import importlib.util
    spec = importlib.util.spec_from_file_location("prep", "scripts/prepare-physics1-20-theory-b-assets.py")
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)

    doc = fitz.open(PDF_PATH)
    all_ok = True

    for name, (pno, bbox) in prep.CROPS.items():
        png_path = os.path.join(IMG_DIR, f"{name}.png")
        if not os.path.exists(png_path):
            print(f"FAIL: File does not exist: {png_path}")
            all_ok = False
            continue

        disk_img = Image.open(png_path).convert("RGB")
        fresh_img = prep.render_crop(doc, pno, bbox, prep.SCALE)

        if disk_img.size != fresh_img.size:
            print(f"FAIL: Dimension mismatch for {name}: disk {disk_img.size} vs fresh {fresh_img.size}")
            all_ok = False
            continue

        diff = ImageChops.difference(disk_img, fresh_img)
        bbox_diff = diff.getbbox()
        if bbox_diff is not None:
            # calculate max pixel difference
            stat = diff.getextrema()
            max_diff = max(s[1] for s in stat)
            if max_diff > 1:
                print(f"FAIL: RGB pixel difference in {name}: max diff {max_diff}")
                all_ok = False
                continue

        print(f"PASS: {name}.png ({disk_img.width}x{disk_img.height}) identical to fresh PDF render")

    doc.close()
    return all_ok


def main():
    print("=" * 60)
    print("PHYSICS 1 CHAPTER 20 THEORY B VERIFICATION SUITE")
    print("=" * 60)

    results = [
        verify_example_20_2(),
        verify_example_20_3(),
        verify_example_20_4(),
        verify_tyu_20_6(),
        verify_example_20_5(),
        verify_example_20_6(),
        verify_example_20_9(),
        verify_example_20_10(),
        verify_section_20_8_microscopic(),
        verify_image_crops_fresh_rgb(),
        verify_math_measurements(),
    ]

    print("\n" + "=" * 60)
    if all(results):
        print("ALL VERIFICATION CHECKS PASSED SUCCESSFULLY!")
        print("=" * 60)
        sys.exit(0)
    else:
        print("SOME VERIFICATION CHECKS FAILED.")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()
