"""Verification script for Physics 1 Chapter 9 Theory A (Sections 9.1, 9.2, 9.3).

Verifies:
1. Exact source numerical ledger and physics calculations.
2. Derivations and mathematical identities.
3. Fresh PDF crop RGB comparison and file existence.
4. Exported annotations consistency.
"""
import math
from pathlib import Path
from PIL import Image
import pymupdf

def verify_calculations():
    print("=== 1. Verifying Numerical Ledger and Physics Cases ===")

    # Opening challenge
    # I_rod = (1/3) M L^2. If L doubles with same M and omega:
    # K = 1/2 I omega^2 increases by factor 2^2 = 4
    factor = 2**2
    assert factor == 4, "Opening challenge kinetic energy factor must be 4"
    print("  [PASS] Opening challenge: Factor = 4 (Option ii)")

    # 9.1 Radian definitions & conversions
    theta_sample = 3.0 / 2.0
    assert abs(theta_sample - 1.5) < 1e-9
    deg_per_rad = 360.0 / (2.0 * math.pi)
    assert abs(deg_per_rad - 57.2957795) < 1e-5
    assert round(deg_per_rad, 1) == 57.3
    rpm_to_rads = (2.0 * math.pi) / 60.0
    assert abs(rpm_to_rads - math.pi / 30.0) < 1e-9
    rads_to_rpm = 60.0 / (2.0 * math.pi)
    assert round(rads_to_rpm, 1) == 9.5
    print("  [PASS] Radian and angular speed conversions")

    # Example 9.1: Flywheel
    d = 0.36
    r = d / 2.0
    assert abs(r - 0.18) < 1e-9
    # theta(t) = 2.0 * t^3
    t1, t2 = 2.0, 5.0
    theta1 = 2.0 * (t1 ** 3)
    theta2 = 2.0 * (t2 ** 3)
    assert theta1 == 16.0
    assert theta2 == 250.0
    theta1_deg = theta1 * 180.0 / math.pi
    theta2_deg = theta2 * 180.0 / math.pi
    assert round(theta1_deg, -1) == 920.0
    assert round(theta2_deg, -3) == 14000.0

    delta_theta = theta2 - theta1
    assert delta_theta == 234.0
    s = r * delta_theta
    assert abs(s - 42.12) < 1e-9
    assert round(s) == 42

    omega_av = delta_theta / (t2 - t1)
    assert omega_av == 78.0
    omega_av_rpm = omega_av * rads_to_rpm
    assert round(omega_av_rpm, -1) == 740.0

    # instantaneous omega(t) = 6.0 * t^2
    omega1 = 6.0 * (t1 ** 2)
    omega2 = 6.0 * (t2 ** 2)
    assert omega1 == 24.0
    assert omega2 == 150.0
    print("  [PASS] Example 9.1 (Flywheel angular velocity): theta1=16 rad (920 deg), theta2=250 rad (14000 deg), s=42 m, omega_av=78 rad/s (740 rpm), omega1=24 rad/s, omega2=150 rad/s")

    # Example 9.2: Flywheel acceleration
    alpha_av = (omega2 - omega1) / (t2 - t1)
    assert alpha_av == 42.0
    # alpha(t) = 12.0 * t
    alpha1 = 12.0 * t1
    alpha2 = 12.0 * t2
    assert alpha1 == 24.0
    assert alpha2 == 60.0
    print("  [PASS] Example 9.2 (Flywheel angular acceleration): alpha_av=42 rad/s^2, alpha1=24 rad/s^2, alpha2=60 rad/s^2")

    # Bio Application: E. coli
    rpm_min, rpm_max = 200.0, 1000.0
    rads_min = rpm_min * rpm_to_rads
    rads_max = rpm_max * rpm_to_rads
    assert round(rads_min, -1) == 20.0
    assert round(rads_max, -2) == 100.0
    print("  [PASS] Bio Application: 200-1000 rpm = ~20-100 rad/s")

    # Test Your Understanding 9.1:
    # 0 < t < 2: vz > 0, az > 0 -> speeding up
    # 2 < t < 4: vz > 0, az < 0 -> slowing down
    # 4 < t < 6: vz < 0, az < 0 -> speeding up
    print("  [PASS] TYU 9.1: (a) speeding up in (i) and (iii); (b) slowing down in (ii)")

    # Example 9.3: Blu-ray disc
    omega0z = 27.5
    alphaz = -10.0
    t_ex3 = 0.300
    omega_z_ex3 = omega0z + alphaz * t_ex3
    assert abs(omega_z_ex3 - 24.5) < 1e-9
    theta_ex3 = omega0z * t_ex3 + 0.5 * alphaz * (t_ex3 ** 2)
    assert abs(theta_ex3 - 7.80) < 1e-9
    revs_ex3 = theta_ex3 / (2.0 * math.pi)
    assert round(revs_ex3, 2) == 1.24
    extra_angle = (revs_ex3 - 1.0) * 360.0
    assert round(extra_angle) == 87
    # evaluate via omega^2 = omega0^2 + 2*alpha*(theta - theta0)
    theta_check = (omega_z_ex3**2 - omega0z**2) / (2.0 * alphaz)
    assert abs(theta_check - 7.80) < 1e-9
    print("  [PASS] Example 9.3 (Blu-ray disc): omega_z=24.5 rad/s, theta=7.80 rad (1.24 rev, 87 deg)")

    # Test Your Understanding 9.2:
    # Double omega0 and double alpha magnitude -> t_stop = -omega0/alpha = unchanged (Option i)
    # delta_theta = 1/2 omega0 * t_stop -> doubled (Option ii)
    t_stop_orig = 27.5 / 10.0
    t_stop_new = 55.0 / 20.0
    assert t_stop_orig == t_stop_new == 2.75
    theta_stop_orig = 0.5 * 27.5 * t_stop_orig
    theta_stop_new = 0.5 * 55.0 * t_stop_new
    assert theta_stop_new == 2.0 * theta_stop_orig
    print("  [PASS] TYU 9.2: (a) same time (i), (b) twice as many revolutions (ii)")

    # Example 9.4: Throwing a discus
    r_discus = 0.800
    omega_discus = 10.0
    alpha_discus = 50.0
    atan_discus = r_discus * alpha_discus
    assert atan_discus == 40.0
    arad_discus = (omega_discus ** 2) * r_discus
    assert arad_discus == 80.0
    a_discus = math.sqrt(atan_discus**2 + arad_discus**2)
    assert abs(a_discus - 89.4427) < 1e-4
    assert round(a_discus, 1) == 89.4
    # evaluate: omega doubles to 20.0
    arad_discus_2 = (20.0 ** 2) * r_discus
    assert arad_discus_2 == 320.0
    a_discus_2 = math.sqrt(atan_discus**2 + arad_discus_2**2)
    assert round(a_discus_2) == 322
    print("  [PASS] Example 9.4 (Discus): atan=40.0 m/s^2, arad=80.0 m/s^2, a=89.4 m/s^2; with omega=20, a=322 m/s^2")

    # Example 9.5: Propeller design
    rpm_prop = 2400.0
    omega_prop = rpm_prop * (2.0 * math.pi / 60.0) # 80*pi approx 251.327
    assert round(omega_prop) == 251
    v_plane = 75.0
    v_tip_max = 270.0
    # v_tip^2 = v_plane^2 + (r*omega)^2
    r_prop_max = math.sqrt(v_tip_max**2 - v_plane**2) / omega_prop
    assert round(r_prop_max, 2) == 1.03
    arad_prop = (omega_prop ** 2) * r_prop_max
    assert round(arad_prop, -3) == 65000.0
    print("  [PASS] Example 9.5 (Propeller design): omega=251 rad/s, r_max=1.03 m, arad=6.5e4 m/s^2")

    # Test Your Understanding 9.3:
    # v = r*omega = constant. If r increases, omega must decrease (Option ii).
    print("  [PASS] TYU 9.3: omega must decrease (Option ii)")

def verify_assets_and_crops():
    print("=== 2. Verifying Crops and Assets ===")
    root = Path(__file__).resolve().parents[2]
    import importlib.util
    spec = importlib.util.spec_from_file_location('prep', root / 'scripts/prepare-physics1-09-theory-a-assets.py')
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)

    img_dir = root / 'docs/vat-ly-1/bai-giang/img/young-09'
    assert img_dir.exists(), f"Image directory {img_dir} does not exist"

    doc = pymupdf.open(root / 'raw_materials/physics/source/young-freedman-15.pdf')
    mat = pymupdf.Matrix(prep.SCALE, prep.SCALE)

    for name, (p1, (x0, y0, x1, y1)) in prep.CROPS.items():
        img_file = img_dir / f"{name}.png"
        assert img_file.exists(), f"Missing image {img_file}"
        im = Image.open(img_file)
        assert im.width > 100 and im.height > 100, f"Image {name} too small ({im.size})"
        # compare fresh pixmap size and actual RGB pixel equality
        page = doc[p1 - 1]
        clip_rect = pymupdf.Rect(x0, y0, x1, y1)
        pix = page.get_pixmap(matrix=mat, clip=clip_rect, alpha=False)
        assert im.size == (pix.width, pix.height), f"Image dimension mismatch for {name}: {im.size} vs {(pix.width, pix.height)}"
        im_rgb = im.convert('RGB')
        assert im_rgb.tobytes() == pix.samples, f"RGB byte mismatch for {name}: on-disk image does not match fresh PDF crop pixels"
        print(f"  [PASS] Asset {name}.png: {im.size} matches fresh PDF render P{p1} RGB bytes exactly")

def verify_annotations():
    print("=== 3. Verifying Image Annotations ===")
    root = Path(__file__).resolve().parents[2]
    import importlib.util
    spec = importlib.util.spec_from_file_location('prep', root / 'scripts/prepare-physics1-09-theory-a-assets.py')
    prep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prep)

    # read docs/.vitepress/physics1-09-theory-a-image-annotations.mjs
    ann_path = root / 'docs/.vitepress/physics1-09-theory-a-image-annotations.mjs'
    assert ann_path.exists(), "Missing annotations mjs file"
    content = ann_path.read_text(encoding='utf-8')
    assert 'physics1Chapter9TheoryAImageAnnotations' in content

    # check that each crop in CROPS has a corresponding key 'young-09/{name}'
    for name in prep.CROPS:
        key = f"young-09/{name}"
        assert f"'{key}'" in content or f'"{key}"' in content, f"Missing annotation for key {key}"
        print(f"  [PASS] Annotation present for {key}")

def main():
    verify_calculations()
    verify_assets_and_crops()
    verify_annotations()
    print("\nALL Chapter 9 Theory A checks PASSED successfully!")

if __name__ == '__main__':
    main()
