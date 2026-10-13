"""Independent numerical and direction checks for Chapter 28.1–28.4."""

from math import isclose, pi, sin, sqrt


MU0 = 4 * pi * 1e-7
EPSILON0 = 8.854e-12


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def close(actual, expected, *, rel=1e-8, abs_tol=1e-14):
    assert isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol), (actual, expected)


def check_moving_protons():
    close(MU0, 1.25663706e-6, rel=1e-8)
    c = 1 / sqrt(EPSILON0 * 1.25663706e-6)
    close(c, 2.998e8, rel=2e-4)
    speed = 0.01 * c
    charge = 1.602e-19
    separation = 0.05
    rhat = (0.0, 1.0, 0.0)
    lower_v = (speed, 0.0, 0.0)
    upper_v_opposite = (-speed, 0.0, 0.0)
    b_lower = tuple(MU0 * charge / (4 * pi * separation**2) * x for x in cross(lower_v, rhat))
    f_opposite = tuple(charge * x for x in cross(upper_v_opposite, b_lower))
    fe = charge**2 / (4 * pi * EPSILON0 * separation**2)
    fb = sqrt(sum(x * x for x in f_opposite))
    assert f_opposite[1] > 0
    close(fb / fe, (speed / c) ** 2, rel=1e-8)

    upper_v_same = lower_v
    f_same = tuple(charge * x for x in cross(upper_v_same, b_lower))
    assert f_same[1] < 0  # Magnetic attraction; electric repulsion remains dominant.
    assert (speed / c) ** 2 < 1


def check_current_element_example():
    current, length, distance = 125.0, 1.0e-2, 1.2
    prefactor = MU0 / (4 * pi) * current * length / distance**2
    b_p1 = prefactor * sin(pi / 2)
    b_p2 = prefactor * sin(pi / 6)
    close(b_p1, 8.680555555555556e-8, rel=1e-10)
    close(b_p2, 4.340277777777778e-8, rel=1e-10)
    d_ell = (-length, 0.0, 0.0)
    rhat_p1 = (0.0, 1.0, 0.0)
    rhat_p2 = (-sqrt(3) / 2, 0.5, 0.0)
    assert cross(d_ell, rhat_p1)[2] < 0
    assert cross(d_ell, rhat_p2)[2] < 0

    # The four self-check points have equal radius L, so rank by sin(phi).
    ranked_factors = [1.0, 0.0, 1.0, sin(pi / 4)]
    assert ranked_factors[0] == ranked_factors[2] > ranked_factors[3] > ranked_factors[1]


def check_finite_wire_integral():
    x, a = 0.3, 1.2
    n = 200_000
    step = 2 * a / n
    total = 0.0
    for index in range(n + 1):
        y = -a + index * step
        value = x / (x * x + y * y) ** 1.5
        weight = 1 if index in (0, n) else (4 if index % 2 else 2)
        total += weight * value
    numerical = total * step / 3
    closed_form = 2 * a / (x * sqrt(x * x + a * a))
    close(numerical, closed_form, rel=1e-10)

    long_wire = 1e8 * x
    finite_wire_b = MU0 * 2.0 / (4 * pi) * 2 * long_wire / (x * sqrt(x * x + long_wire**2))
    infinite_wire_b = MU0 * 2.0 / (2 * pi * x)
    close(finite_wire_b / infinite_wire_b, 1.0, rel=1e-8)

    wire_current, target_b = 1.0, 0.5e-4
    distance = MU0 * wire_current / (2 * pi * target_b)
    close(distance, 4.0e-3, rel=1e-12)


def check_two_wire_superposition():
    # Wires 1 and 2 lie at x=-d and x=+d, with +z and -z currents.
    # On the x-axis, their signed y components add by superposition.
    d, current = 0.02, 3.0

    def by_at(x):
        return MU0 * current / (2 * pi * (x + d)) - MU0 * current / (2 * pi * (x - d))

    close(by_at(-3 * d), -MU0 * current / (8 * pi * d), rel=1e-12)
    close(by_at(0), MU0 * current / (pi * d), rel=1e-12)
    close(by_at(2 * d), -MU0 * current / (3 * pi * d), rel=1e-12)
    x = 1000 * d
    close(by_at(x), -MU0 * current * d / (pi * (x * x - d * d)), rel=1e-12)
    far_approx = -MU0 * current * d / (pi * x**2)
    close(by_at(x) / far_approx, 1 / (1 - (d / x) ** 2), rel=1e-12)


def check_parallel_wire_force():
    distance, current = 4.5e-3, 15_000.0
    force_per_length = MU0 * current**2 / (2 * pi * distance)
    close(force_per_length, 1.0e4, rel=1e-12)

    b_from_lower = cross((1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    same_direction_force = cross((1.0, 0.0, 0.0), b_from_lower)
    opposite_direction_force = cross((-1.0, 0.0, 0.0), b_from_lower)
    assert same_direction_force[1] < 0  # Upper wire is pulled toward lower wire.
    assert opposite_direction_force[1] > 0  # Reversing its current reverses the force.


def check_carrier_signs():
    conventional_current_direction = (1.0, 0.0, 0.0)
    positive_q_v = (1.0, 0.0, 0.0)
    negative_q_v = (-1.0, 0.0, 0.0)
    positive_charge_product = tuple(1.0 * value for value in positive_q_v)
    negative_charge_product = tuple(-1.0 * value for value in negative_q_v)
    assert positive_charge_product == conventional_current_direction
    assert negative_charge_product == conventional_current_direction


def check_compass_and_wire_direction():
    # A southward current below a compass produces a westward magnetic field.
    field_direction = cross((0.0, -1.0, 0.0), (0.0, 0.0, 1.0))
    assert field_direction == (-1.0, 0.0, 0.0)
    earth_field = (0.0, 1.0, 0.0)
    net_field = tuple(a + b for a, b in zip(earth_field, field_direction))
    assert net_field[0] < 0 and net_field[1] > 0  # Northwest, counterclockwise from north.


def check_m0_force_definition():
    force_per_length = (4 * pi * 1e-7) * 1.0 * 1.0 / (2 * pi * 1.0)
    close(force_per_length, 2e-7, rel=1e-12)


def main():
    check_moving_protons()
    check_current_element_example()
    check_finite_wire_integral()
    check_two_wire_superposition()
    check_parallel_wire_force()
    check_carrier_signs()
    check_compass_and_wire_direction()
    check_m0_force_definition()
    print("Chapter 28.1–28.4: numerical, vector-direction, limiting-case, and source-condition checks passed.")


if __name__ == "__main__":
    main()
