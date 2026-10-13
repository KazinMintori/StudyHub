"""Independent numerical/vector checks for Chapter 27 Exercises 27.1–27.30."""

import math

import numpy as np


E_CHARGE = 1.602176634e-19
M_E = 9.1093837015e-31
M_P = 1.67262192369e-27
G = 9.80


def check_close(actual: float, expected: float, rtol: float = 2e-3) -> None:
    np.testing.assert_allclose(actual, expected, rtol=rtol, atol=1e-30)


def main() -> None:
    # 27.1–27.8: Magnetic force on a charge.
    q1 = -1.24e-8
    v1 = np.array([4.19e4, -3.85e4, 0.0])
    f1a = q1 * np.cross(v1, [1.40, 0.0, 0.0])
    f1b = q1 * np.cross(v1, [0.0, 0.0, 1.40])
    np.testing.assert_allclose(f1a, [0.0, 0.0, -6.68e-4], rtol=2e-3)
    np.testing.assert_allclose(f1b, [6.68e-4, 7.27e-4, 0.0], rtol=2e-3)

    q2 = -2.50e-8
    m2 = 0.195e-3
    v2 = 4.00e4
    b2 = m2 * G / (abs(q2) * v2)
    check_close(b2, 1.91)
    # Coordinates: east = +x, north = +y, up = +z. Eastward B gives upward force.
    np.testing.assert_allclose(q2 * np.cross([0.0, v2, 0.0], [b2, 0.0, 0.0]),
                               [0.0, 0.0, m2 * G], rtol=1e-14)

    q3 = 8.50e-3
    f3 = q3 * 4.75e3 * 1.25
    check_close(f3, 50.5)
    np.testing.assert_allclose(q3 * np.cross([0.0, 4.75e3, 0.0], [0.0, 0.0, 1.25]),
                               [f3, 0.0, 0.0], rtol=1e-14)

    f4 = 1.22e-8 * 3.00e4 * 1.63
    a4 = f4 / 1.81e-3
    check_close(f4, 5.97e-4)
    check_close(a4, 0.330)

    v5 = 5.50e-18 / (E_CHARGE * 0.200)
    check_close(v5, 171.6)
    # Negative electron: force -y implies velocity -x for B = +z.
    np.testing.assert_allclose(-E_CHARGE * np.cross([-v5, 0.0, 0.0], [0.0, 0.0, 0.200]),
                               [0.0, -5.50e-18, 0.0], rtol=1e-14)

    a6max = E_CHARGE * 1.40e6 * 7.40e-2 / M_E
    check_close(a6max, 1.82e16)
    theta6 = math.asin(0.25)
    check_close(math.degrees(theta6), 14.48)
    check_close(math.degrees(math.pi - theta6), 165.52)

    bx7 = 8.50e-16 / (E_CHARGE * 4.75e3)
    bz7 = -2.25e-16 / (E_CHARGE * 1.50e3)
    f7 = -E_CHARGE * np.cross([0.0, -3.20e3, 0.0], [bx7, 0.0, bz7])
    check_close(bx7, 1.117)
    check_close(bz7, -0.936)
    field7 = np.array([bx7, 0.0, bz7])
    np.testing.assert_allclose(E_CHARGE * np.cross([1.50e3, 0.0, 0.0], field7),
                               [0.0, 2.25e-16, 0.0], rtol=1e-12, atol=1e-30)
    np.testing.assert_allclose(-E_CHARGE * np.cross([0.0, 0.0, -4.75e3], field7),
                               [0.0, 8.50e-16, 0.0], rtol=1e-12, atol=1e-30)
    check_close(float(np.linalg.norm(field7)), 1.46)
    np.testing.assert_allclose(f7, [-4.80e-16, 0.0, -5.73e-16], rtol=2e-3)

    q8 = -5.60e-9
    b8 = np.array([0.0, 0.0, -1.25])
    f8 = np.array([-3.40e-7, 7.40e-7, 0.0])
    vx8 = -f8[1] / (q8 * -1.25)
    vy8 = f8[0] / (q8 * -1.25)
    v8 = np.array([vx8, vy8, 0.0])
    np.testing.assert_allclose(q8 * np.cross(v8, b8), f8, rtol=1e-14)
    check_close(float(np.dot(v8, f8)), 0.0, rtol=1e-12)

    # 27.9–27.13: Magnetic flux.
    area9 = math.pi * 0.065**2
    flux9a = 0.230 * area9
    flux9b = flux9a * math.cos(math.radians(53.1))
    check_close(flux9a, 3.05e-3)
    check_close(flux9b, 1.83e-3)

    flux10 = 0.500 * 0.034**2
    check_close(flux10, 5.78e-4)

    flux11 = 1.75 * math.pi * (0.025 / 2) ** 2 * math.cos(math.radians(25.0))
    check_close(flux11, 7.79e-4)

    b12 = 3.10e-4 / (0.0280 * 0.0320 * math.sin(math.radians(30.0)))
    check_close(b12, 0.692)

    # E27.13: The volume is a triangular prism with a 30-40-50 cm
    # right-triangle cross-section, extruded 30 cm along y. B is +z.
    flux13_abcd = 0.0
    flux13_befc = -0.128 * 0.30 * 0.30
    flux13_aefd = 0.128 * 0.30 * 0.30
    check_close(flux13_abcd, 0.0)
    check_close(flux13_befc, -1.152e-2)
    check_close(flux13_aefd, 1.152e-2)
    check_close(flux13_befc + flux13_aefd, 0.0)

    # 27.14–27.22: Motion in a magnetic field.
    v14 = 1.41e6
    r14 = 0.100 / 2
    b14e = M_E * v14 / (E_CHARGE * r14)
    t14 = math.pi * r14 / v14
    check_close(b14e, 1.60e-4, rtol=3e-3)
    check_close(t14, 1.11e-7, rtol=4e-3)
    b15p = M_P * v14 / (E_CHARGE * r14)
    t15 = math.pi * r14 / v14
    check_close(b15p, 0.294)
    check_close(t15, t14, rtol=1e-14)

    q16 = 2 * E_CHARGE
    m16 = 6.64e-27
    v16 = 35.6e3
    b16 = 1.80
    r16 = m16 * v16 / (q16 * b16)
    a16 = q16 * v16 * b16 / m16
    check_close(2 * r16, 8.19e-4)
    check_close(a16, 3.09e12)

    q17 = -4.00e8 * E_CHARGE
    v17 = math.sqrt(2 * G * 125.0)
    f17 = q17 * np.cross([0.0, 0.0, -v17], [-0.250, 0.0, 0.0])
    check_close(v17, 49.5)
    check_close(float(np.linalg.norm(f17)), 7.93e-10)
    assert f17[1] < 0  # South, for east=x, north=y, up=z.

    e18 = 5.0e6 * E_CHARGE
    m18 = M_P  # H− mass is approximated by the proton mass.
    v18 = math.sqrt(2 * e18 / m18)
    r18 = m18 * v18 / (E_CHARGE * 1.9)
    check_close(v18, 3.10e7)
    check_close(r18, 0.170)

    m19 = 12 * M_P
    q19 = 3 * E_CHARGE
    r19 = 0.950 / 2
    b19 = 0.250
    v19 = q19 * b19 * r19 / m19
    fmag19 = q19 * v19 * b19
    weight19 = m19 * G
    check_close(v19, 2.84e6)
    assert fmag19 / weight19 > 1e12

    m20, q20, r20, b20 = 3.34e-27, 1.60e-19, 6.96e-3, 2.50
    v20 = q20 * b20 * r20 / m20
    half_period20 = math.pi * m20 / (q20 * b20)
    voltage20 = m20 * v20**2 / (2 * q20)
    check_close(v20, 8.34e5)
    check_close(half_period20, 2.62e-8)
    check_close(voltage20, 7.25e3)

    v21 = math.sqrt(2 * E_CHARGE * 2.00e3 / M_E)
    b21 = M_E * v21 / (E_CHARGE * 0.180)
    check_close(v21, 2.65e7)
    check_close(b21, 8.38e-4)

    arc22 = 1.18e-2
    r22 = 2 * arc22 / math.pi  # The path turns through 90 degrees.
    b22 = M_P * 1.20e3 / (E_CHARGE * r22)
    check_close(r22, 7.51e-3)
    check_close(b22, 1.67e-3)

    # 27.23–27.28: Crossed fields and mass analysis.
    e23 = 5.85e3 * 1.35
    np.testing.assert_allclose(e23, 7.90e3, rtol=1e-3)
    # Chosen axes: v=+y, B=−z, E=+x. Both charge signs pass undeflected.
    for q23 in (0.640e-9, -0.320e-9):
        f23 = q23 * (np.array([e23, 0.0, 0.0])
                     + np.cross([0.0, 5.85e3, 0.0], [0.0, 0.0, -1.35]))
        np.testing.assert_allclose(f23, [0.0, 0.0, 0.0], atol=1e-25)

    v24 = 1.56e4 / 4.62e-3
    r24 = M_E * v24 / (E_CHARGE * 4.62e-3)
    period24 = 2 * math.pi * M_E / (E_CHARGE * 4.62e-3)
    check_close(v24, 3.38e6)
    check_close(r24, 4.16e-3)
    check_close(period24, 7.73e-9)

    e25 = 150.0 / 8.20e-3
    v25 = math.sqrt(2 * 2 * E_CHARGE * 1.75e3 / 6.64e-27)
    b25 = e25 / v25
    check_close(e25, 1.83e4)
    check_close(v25, 4.11e5)
    check_close(b25, 4.45e-2)

    e26 = 0.510 * 1.82e6
    voltage26 = e26 * 5.20e-3
    check_close(e26, 9.28e5)
    check_close(voltage26, 4.83e3)

    v27 = 155.0 / 0.0315
    m27 = E_CHARGE * 0.0175 * 0.175 / v27
    check_close(v27, 4.92e3)
    check_close(m27, 9.97e-26)

    r12c = 0.125
    r14n = r12c * 2.32e-26 / 1.99e-26
    r15n = r12c * 2.49e-26 / 1.99e-26
    separation28 = 2 * (r15n - r14n)
    check_close(separation28, 2.14e-2, rtol=3e-3)

    # 27.29–27.30: Force on current-carrying wires.
    f29 = 4.50 * np.cross([0.60, 0.30, 0.0], [0.0, 0.0, 0.240])
    np.testing.assert_allclose(f29, [0.324, -0.648, 0.0], rtol=1e-14)
    check_close(float(np.linalg.norm(f29)), 0.725)

    f30 = 1.5 * 2.5 * (0.55e-4)
    check_close(f30, 2.06e-4)

    print("Chapter 27 Exercises 27.1–27.30: numerical and direction checks passed.")


if __name__ == "__main__":
    main()
