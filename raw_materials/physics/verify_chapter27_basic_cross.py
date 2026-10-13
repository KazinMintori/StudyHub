"""Independent selected checks for Chapter 27 exercises 27.1–27.60."""
from __future__ import annotations

import math
import re
from pathlib import Path

import fitz
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
TRANS = ROOT / "raw_materials/physics/translations/chapter-27"
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
E = 1.602176634e-19
ME = 9.1093837139e-31
MP = 1.67262192595e-27
G = 9.80
KE = 8.9875517923e9


def close(actual: float, expected: float, *, rel: float = 0.01) -> None:
    assert math.isclose(actual, expected, rel_tol=rel, abs_tol=1e-14), (actual, expected)


def coverage() -> None:
    first = (TRANS / "13-bai-tap-01-30.md").read_text(encoding="utf-8-sig")
    second = (TRANS / "14-bai-tap-31-60.md").read_text(encoding="utf-8-sig")
    ids_a = [int(n) for n in re.findall(r"::: exercise (?:Bài )?27\.(\d+)", first)]
    ids_b = [int(n) for n in re.findall(r"::: exercise (?:Bài )?27\.(\d+)", second)]
    assert ids_a == list(range(1, 31)), ids_a
    assert ids_b == list(range(31, 61)), ids_b
    assert len(re.findall(r"::: solution", first)) == 30
    assert len(re.findall(r"::: solution", second)) == 30

    pdf = fitz.open(PDF)
    # Printed pages 909–914 are PDF pages 929–934.
    source = "\n".join(pdf[i].get_text() for i in range(928, 934))
    for n in range(1, 61):
        assert re.search(rf"(?<!\d)27\.{n}(?!\d)", source), f"source problem 27.{n} missing"


def particle_and_field_checks() -> None:
    # 27.1: Compute both force vectors from q(v × B).
    q1 = -1.24e-8
    v1 = np.array([4.19e4, -3.85e4, 0.0])
    b1a = np.array([1.40, 0.0, 0.0])
    b1b = np.array([0.0, 0.0, 1.40])
    f1a, f1b = q1 * np.cross(v1, b1a), q1 * np.cross(v1, b1b)
    np.testing.assert_allclose(f1a, [0, 0, -6.68e-4], rtol=.01, atol=1e-12)
    np.testing.assert_allclose(f1b[:2], [6.68e-4, 7.27e-4], rtol=.01, atol=1e-12)

    # 27.2: Minimum field has no component parallel to the northward velocity.
    bmin2 = (0.195e-3 * G) / (2.50e-8 * 4.00e4)
    close(bmin2, 1.91)

    # 27.3–27.4: Sign and force/acceleration follow the full cross product.
    np.testing.assert_allclose(np.cross([0, 1, 0], [0, 0, 1]), [1, 0, 0])
    f4z = 1.22e-8 * np.cross([0, 3.00e4, 0], [1.63, .980, 0])[2]
    close(f4z / 1.81e-3, -0.330)

    # 27.5: The measured -y force on an electron requires vx < 0.
    vx5 = -5.50e-18 / (E * .200)
    close(vx5, -1.72e2)

    # 27.6: The stated fraction fixes sin(phi), giving supplementary angles.
    phi6 = math.degrees(math.asin(.25))
    close(phi6, 14.48)
    close(180 - phi6, 165.52)

    # 27.7: Treat each stated force direction as a full-vector observation.
    # Proton +x gives By=0 from its zero z-force; the two measured y-forces
    # determine Bz and Bx independently.
    bz7 = -2.25e-16 / (E * 1.50e3)
    bx7 = 8.50e-16 / (E * 4.75e3)
    by7 = 0.0
    bmag7 = float(np.linalg.norm([bx7, by7, bz7]))
    close(bx7, 1.117)
    close(bz7, -0.936)
    close(bmag7, 1.46)
    np.testing.assert_allclose(1.50e3 * np.cross([1, 0, 0], [bx7, by7, bz7]) * E,
                               [0, 2.25e-16, 0], rtol=.01, atol=1e-25)
    np.testing.assert_allclose(-E * 4.75e3 * np.cross([0, 0, -1], [bx7, by7, bz7]),
                               [0, 8.50e-16, 0], rtol=.01, atol=1e-25)
    f7c = -E * 3.20e3 * np.cross([0, -1, 0], [bx7, 0, bz7])
    close(float(np.linalg.norm(f7c)), 7.48e-16)

    # 27.8: vx and vy are fixed, vz is free; magnetic force is perpendicular.
    q8, bz8 = -5.60e-9, -1.25
    vx8 = -7.40e-7 / (q8 * bz8)
    vy8 = -3.40e-7 / (q8 * bz8)
    close(vx8, -1.06e2)
    close(vy8, -48.6)
    f8 = q8 * np.cross([vx8, vy8, 0], [0, 0, bz8])
    close(float(np.dot([vx8, vy8, 0], f8)), 0.0)

    # 27.9–27.12: Flux only uses the component normal to each surface.
    area9 = math.pi * .065**2
    close(.230 * area9, 3.05e-3)
    close(.230 * area9 * math.cos(math.radians(53.1)), 1.83e-3)
    close(.500 * .034**2, 5.78e-4)
    close(3.10e-4 / (.028 * .032 * math.cos(math.radians(60))), .692)

    # 27.13: Opposite projected areas cancel, as required for a closed prism.
    flux_side = .128 * .30 * .30
    close(flux_side, 1.152e-2)
    close(-flux_side + flux_side, 0.0)

    # 27.14–27.16, 27.20–27.22: Circular motion and nonrelativistic values.
    b14e = ME * 1.41e6 / (E * .050)
    t14 = math.pi * .050 / 1.41e6
    close(b14e, 1.60e-4)
    close(t14, 1.11e-7)
    close(MP * 1.41e6 / (E * .050), .294)
    close((6.64e-27 * 3.56e4 / (2 * E * 1.80)) * 2, 8.19e-4)
    v18 = math.sqrt(2 * 5.0e6 * E / MP)
    close(v18 / 299_792_458, .103)
    close(MP * v18 / (E * 1.9), .170)
    close(3.34e-27 * 8.34e5 / (E * 6.96e-3), 2.50)
    close(1.18e-2 * 2 / math.pi, 7.51e-3)

    # 27.23–27.28: Crossed fields, selector and mass-spectrometer checks.
    close(5.85e3 * 1.35, 7.90e3)
    close(1.56e4 / 4.62e-3, 3.38e6)
    close(ME * (1.56e4 / 4.62e-3) / (E * 4.62e-3), 4.16e-3)
    close(150 / 8.20e-3 / math.sqrt(2 * 2 * E * 1.75e3 / 6.64e-27), 4.45e-2)
    close(155 / .0315, 4.92e3)
    close(E * .0175 * .175 / (155 / .0315), 9.97e-26)
    r12 = .125
    r14 = r12 * 2.32e-26 / 1.99e-26
    r15 = r12 * 2.49e-26 / 1.99e-26
    close(2 * (r15 - r14), 2.14e-2)


def conductor_and_device_checks() -> None:
    # 27.29–27.30: The diagram’s current path gives the signed force direction.
    np.testing.assert_allclose(4.50 * np.cross([.30, .60, 0], [0, 0, .240]),
                               [.648, -.324, 0], rtol=.01, atol=1e-12)
    f30 = 1.5 * 2.5 * 5.5e-5
    close(f30, 2.06e-4)

    # 27.31: At lift-off, ILB=mg; shorting R raises I and upward net force.
    i31 = .750 * G / (.500 * .450)
    v31 = i31 * 25.0
    a31 = ((v31 / 2.0) * .500 * .450 - .750 * G) / .750
    close(i31, 32.7)
    close(v31, 817)
    close(a31, 113)
    close(10.8 * .0500 * .550, .297)

    # 27.33–27.34: Current/field cross products and vector components.
    close((175 / 5.0) * .600 * 1.50 / G, 3.21)
    np.testing.assert_allclose(np.cross([0, 0, -1], [1, 0, 0]), [0, -1, 0])
    np.testing.assert_allclose(np.cross([0, 0, -1], [0, -1, 0]), [-1, 0, 0])
    f34 = 2.60 * .0100 * .588
    close(f34, 1.53e-2)

    # 27.35–27.39: Loop torque, motor geometry, and inertia.
    close(.194 / (8.80 * 4.0e-4), 55.1)
    close(6.2 * .050 * .080 * .19, 4.71e-3)
    close((.260**2 / (4 * math.pi)) * 6.2 * .19, 6.34e-3)
    close(5 * 1.20 * .200 * .350, .420)
    m39, perimeter39 = .212, 2 * (1.0 + .5)
    lam39 = m39 / perimeter39
    i39 = 2 * lam39 * 1.0 * .25**2 + 2 * lam39 * .5**3 / 12
    alpha39 = (2 * .5 * 3.0) / i39
    close(i39, 1.03e-2)
    close(alpha39, 2.91e2)

    # 27.43–27.46: Motor branch currents and Hall signs/magnitudes.
    field_current = 120 / 106
    rotor_current = 4.82 - field_current
    back_emf = 120 - rotor_current * 5.9
    close(field_current, 1.13)
    close(rotor_current, 3.69)
    close(back_emf * rotor_current, 362)
    vd45 = 120 / (5.85e28 * E * .0118 * .00023)
    eh45 = vd45 * .95
    vh45 = eh45 * .0118
    close(vd45, 4.73e-3)
    close(eh45, 4.50e-3)
    close(vh45, 53.1e-6)
    # The transverse width z1 cancels between the Hall voltage and current
    # relations: n = I B / (e V_H y1).  The printed source's 131 μV matters.
    n46 = 78.0 * 2.29 / (E * 131e-6 * .00023)
    close(n46, 3.70e28)

    # 27.47–27.54: Gyro motion and mass-spectrometer data.
    omega47 = 7.50 * 4.0
    t47 = .0200
    close((30 / omega47) * math.sin(omega47 * t47), .565)
    close(1 + (30 / omega47) * (math.cos(omega47 * t47) - 1), .825)
    close(.5 * ((30.0**2 + (7.5 * 60 * .02)**2))**.5, .5 * 31.3)
    # The exact 27.48 force is calculated as a vector, not from component magnitudes.
    f48 = 7.26e-8 * np.cross([-1.68e4, -3.11e4, 5.85e4], [.650, 0, 0])
    np.testing.assert_allclose(f48, [0, 2.76e-3, 1.47e-3], rtol=.01, atol=1e-12)
    v49 = math.sqrt(KE * E**2 / (3.34e-27 * 1.0e-15))
    close(v49, 8.30e6)
    close(3.34e-27 * v49 / (E * 1.25), .139)
    close(2 / (1.04e-6 * .200**2), 4.81e7)
    close((1.60e-19 * .85 * .4)**2 / (2 * 1.67e-27), 8.86e-13)
    close(1.88e4 / .682, 2.76e4)
    close(2 * ((14 - 12) / 12) * .5, 1/6)

    # 27.55–27.60: Incline, parallel branch network, Hall/rail-gun, and wire force.
    close(1 / math.tan(math.radians(30)), 1.732)
    r_parallel56 = 1 / (1 / 10 + 1 / 10)
    i_total56 = 120 / (25 + r_parallel56)
    i_bar56 = i_total56 / 2
    f_bar56 = i_bar56 * .850 * 1.60
    m_bar56 = 2.60 / G
    a_lift56 = (f_bar56 - 2.60) / m_bar56
    close(i_total56, 4.0)
    close(i_bar56, 2.0)
    close(f_bar56, 2.72)
    close(a_lift56, .452)
    close(2.0e3 * .50 * .80, 800)
    close(25 * (11.2e3)**2 / (2 * 2.0e3 * .50 * .80), 1.96e6)
    np.testing.assert_allclose(7.40 * .250 * np.cross([0, 0, 1], [-.242, -.985, -.336]),
                               [1.82, -.448, 0], rtol=.01, atol=1e-12)


def main() -> None:
    coverage()
    particle_and_field_checks()
    conductor_and_device_checks()
    print("Source/translation exercise IDs 27.1–27.60: complete.")
    print("Selected independent vector, flux, circuit, Hall, and orbit checks passed.")
    print("P27.56 parallel-branch check: Ibar=2.00 A, FB=2.72 N, lift-case a=0.452 m/s².")
    print("Other findings and scope are recorded in ch27-basic-exercises-cross-review.md.")


if __name__ == "__main__":
    main()
