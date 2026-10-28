"""Independent numerical checks for the chapter 19 Cheatsheet additions.

No file writes. This verifies named relations, not every course calculation.
"""
import json
import math


def close(actual, expected):
    assert math.isclose(actual, expected, rel_tol=2e-10, abs_tol=1e-8), (actual, expected)


R = 8.314462618
records = []
for gamma in (1.4, 5 / 3):
    cv = R / (gamma - 1)
    cp = gamma * cv
    close(cp - cv, R)
    n, p1, v1 = 2.0, 300000.0, 0.02
    t1 = p1 * v1 / (n * R)
    for ratio in (0.5, 1.0, 2.0, 4.0):
        v2 = ratio * v1
        p2 = p1 * ratio ** (-gamma)
        t2 = p2 * v2 / (n * R)
        work_pv = (p1 * v1 - p2 * v2) / (gamma - 1)
        work_t = n * cv * (t1 - t2)
        # Independent Simpson quadrature of the actual pressure curve.
        steps = 2000
        step = (v2 - v1) / steps

        def pressure(volume):
            return p1 * (v1 / volume) ** gamma

        integral = step / 3 * (
            pressure(v1) + pressure(v2)
            + 4 * sum(pressure(v1 + i * step) for i in range(1, steps, 2))
            + 2 * sum(pressure(v1 + i * step) for i in range(2, steps, 2))
        )
        close(integral, work_pv)
        close(work_pv, work_t)
        close(n * cv * (t2 - t1), -work_pv)
        close(t1 * v1 ** (gamma - 1), t2 * v2 ** (gamma - 1))
        assert (work_pv > 0) == (ratio > 1)
        records.append({"gamma": gamma, "V2_over_V1": ratio, "work_J": work_pv})
    for delta_t in (-80.0, 0.0, 120.0):
        du = n * cv * delta_t
        q_at_constant_v = n * cv * delta_t
        q_at_constant_p = n * cp * delta_t
        work_at_constant_p = n * R * delta_t
        close(du, q_at_constant_v)
        close(du, q_at_constant_p - work_at_constant_p)

# Isothermal compression and expansion, including the pressure-ratio form.
for ratio in (0.5, 1.0, 2.0, 4.0):
    t, n, v1 = 300.0, 2.0, 0.01
    v2 = ratio * v1
    p1 = n * R * t / v1
    p2 = n * R * t / v2
    work = n * R * t * math.log(v2 / v1)
    close(work, n * R * t * math.log(p1 / p2))
    close(work - work, 0.0)  # Q = W gives Delta U = 0.

print(json.dumps({"status": "passed", "adiabatic_states": records,
                  "scope": "Named chapter19 relations, sign conventions, heat capacities and independent pressure integration only."},
                 ensure_ascii=False, indent=2))
