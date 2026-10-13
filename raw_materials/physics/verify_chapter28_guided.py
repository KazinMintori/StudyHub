"""Independent numerical and direction checks for Chapter 28 Guided Practice."""

import numpy as np


MU0 = 4.0 * np.pi * 1.0e-7
E = 1.602e-19


def close(actual, expected, rtol=2e-3, atol=0.0):
    assert np.allclose(actual, expected, rtol=rtol, atol=atol), (actual, expected)


def wire_field(current, wire_xy, point_xy):
    """Field in the xy-plane from an infinite wire along +z; vector result."""
    r = np.asarray(point_xy, dtype=float) - np.asarray(wire_xy, dtype=float)
    return MU0 * current / (2.0 * np.pi * np.dot(r, r)) * np.array([-r[1], r[0]])


def main():
    # VP28.2.1: moving-charge field, including the collinear zero and cross-product signs.
    q, v = E, 2.00e5
    points = [np.array([0.0, 1e-3, 0.0]), np.array([0.0, 0.0, 2e-3]),
              np.array([1e-3, 0.0, 0.0]), np.array([1e-3, 1e-3, 0.0])]
    field = []
    for r in points:
        field.append(1e-7 * q * np.cross([v, 0, 0], r) / np.linalg.norm(r)**3)
    close(field[0], [0, 0, 3.204e-15])
    close(field[1], [0, -8.010e-16, 0])
    close(field[2], [0, 0, 0])
    close(field[3], [0, 0, 1.133e-15])

    # VP28.2.2: the signed cross products point toward one another.
    distance, speed = 2.00e-3, 4.20e5
    qp, qe = E, -E
    vp, ve = np.array([0.0, speed, 0.0]), np.array([0.0, -speed, 0.0])
    r_p_to_e, r_e_to_p = np.array([distance, 0.0, 0.0]), np.array([-distance, 0.0, 0.0])
    B_at_e = 1e-7 * qp * np.cross(vp, r_p_to_e) / distance**3
    B_at_p = 1e-7 * qe * np.cross(ve, r_e_to_p) / distance**3
    F_on_e = qe * np.cross(ve, B_at_e)
    F_on_p = qp * np.cross(vp, B_at_p)
    fmag = 1e-7 * E**2 * speed**2 / distance**2
    close(B_at_e, [0.0, 0.0, -1e-7*E*speed/distance**2])
    close(B_at_p, [0.0, 0.0, +1e-7*E*speed/distance**2])
    close(F_on_e, [-fmag, 0.0, 0.0])
    close(F_on_p, [fmag, 0.0, 0.0])
    close(np.linalg.norm(F_on_e), 1.131e-28)
    assert F_on_e[0] < 0 < F_on_p[0]

    # VP28.2.3 and VP28.2.4: Biot–Savart direction and force on negative charge.
    close(np.array([3.0, 4.0, 0.0]) / 5.0, [0.6, 0.8, 0.0])
    b_segment = 1e-7 * 6.0 * np.cross([0, 2e-3, 0], [0.6, 0.8, 0]) / 25.0
    close(b_segment, [0, 0, -2.88e-11])
    b_short = 1e-7 * 4.0 * 8e-3 / 1.25**2
    force_short = (-E) * np.cross([-3e5, 0, 0], [0, b_short, 0])
    close([b_short], [2.048e-9])
    close(force_short, [0, 0, 9.835e-23])

    # VP28.5.1 and 28.5.2: current and superposed fields from parallel wires.
    current = 3.20e-5 * 2 * np.pi * 0.014 / MU0
    close(current, 2.24)
    a = 0.010
    fields = [wire_field(1.0, [0, a], [0, 0]) + wire_field(4.0, [0, -a], [0, 0]),
              wire_field(1.0, [0, a], [0, 2*a]) + wire_field(4.0, [0, -a], [0, 2*a]),
              wire_field(1.0, [0, a], [0, -2*a]) + wire_field(4.0, [0, -a], [0, -2*a])]
    close(fields[0], [-60e-6, 0])
    close(fields[1], [-46.6666667e-6, 0])
    close(fields[2], [86.6666667e-6, 0])

    # VP28.5.3: midpoint fields oppose for equal direction, add for opposite.
    factor = MU0 / (2 * np.pi * 0.015)
    close(abs(2.0 - 5.0) * factor, 40e-6)
    close((2.0 + 1.0) * factor, 40e-6)

    # VP28.5.4: force per length implies an upward current that attracts wire 1.
    i2 = 95.0 * 2 * np.pi * 0.900 / (MU0 * 1.30e4)
    close(i2, 3.29e4)

    # VP28.10.1: continuous field at the surface of a uniformly conducting cylinder.
    radius, total_current = 0.045, 2.00
    inside = lambda r: MU0 * total_current * r / (2 * np.pi * radius**2)
    outside = lambda r: MU0 * total_current / (2 * np.pi * r)
    close([inside(0.025), inside(radius), outside(0.060)],
          [4.938e-6, 8.889e-6, 6.667e-6])
    close([inside(radius)], [outside(radius)])

    # VP28.10.2: the field is zero in the hollow, continuous at R2, and maximal there.
    r1, r2, j = 0.02, 0.05, 800.0
    b_annulus = lambda r: MU0 * j * (r**2-r1**2) / (2*r)
    b_outer = lambda r: MU0 * j * (r2**2-r1**2) / (2*r)
    assert b_annulus(r1) == 0.0
    close([b_annulus(r2)], [b_outer(r2)])
    assert b_annulus(0.04) < b_annulus(r2) and b_outer(0.06) < b_outer(r2)

    # VP28.10.3 and 28.10.4: long-solenoid and toroid fields.
    close(0.0320 / (MU0 * 8.00e3), 3.1831)
    nturn = 2e-3 * 2*np.pi*0.07 / (MU0*0.840)
    close(nturn, 833.3)
    close([MU0*nturn*0.840/(2*np.pi*0.06), MU0*nturn*0.840/(2*np.pi*0.08)],
          [2.333e-3, 1.750e-3])

    # Bridge problem: direct annular integration agrees with the closed form.
    q_total, rotations, disk_radius = 2e-6, 3.0, 0.10
    sigma = q_total / (np.pi * disk_radius**2)
    r = np.linspace(0, disk_radius, 200_001)
    # dB = (mu0/2r) dI and dI = n sigma (2 pi r dr), so integrand is constant.
    integrand = np.full_like(r, MU0 * np.pi * rotations * sigma)
    numeric = np.trapezoid(integrand, r)
    analytic = MU0 * rotations * q_total / disk_radius
    close(numeric, analytic, rtol=1e-10)
    rim_only = MU0 * rotations * q_total / (2 * disk_radius)
    close(rim_only, analytic / 2, rtol=1e-12)

    print("Chapter 28 Guided Practice and Bridging Problem: independent checks passed.")


if __name__ == "__main__":
    main()
