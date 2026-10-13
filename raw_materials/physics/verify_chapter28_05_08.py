"""Independent numerical checks for Chapter 28 sections 28.5–28.8."""

from __future__ import annotations

import math

import numpy as np


MU0 = 4 * math.pi * 1e-7
E_CHARGE = 1.602176634e-19
ELECTRON_MASS = 9.1093837139e-31
PLANCK = 6.62607015e-34
BOLTZMANN = 1.380649e-23
EV_J = E_CHARGE


def close(actual: float, expected: float, *, rel: float = 1e-9) -> None:
    assert math.isclose(actual, expected, rel_tol=rel, abs_tol=1e-15), (actual, expected)


def test_loop_geometry_and_example_28_6() -> dict[str, float]:
    n, current, radius, x = 100, 5.0, 0.60, 0.80
    field = MU0 * n * current * radius**2 / (2 * (x**2 + radius**2) ** 1.5)
    center = MU0 * n * current / (2 * radius)
    moment = n * current * math.pi * radius**2
    close(field, 1.1309733552923255e-4)
    close(moment, 5.654866776461628e2)
    x_eighth = math.sqrt(3) * radius
    field_eighth = MU0 * n * current * radius**2 / (
        2 * (x_eighth**2 + radius**2) ** 1.5
    )
    close(field_eighth / center, 1 / 8)

    # Independent vector check: opposite loop elements cancel transverse
    # components while preserving their axial components.
    x_axial, a = 0.8, radius
    def differential(phi: float) -> np.ndarray:
        dl = np.array([0.0, -a * math.sin(phi), a * math.cos(phi)])
        r_vec = np.array([x_axial, -a * math.cos(phi), -a * math.sin(phi)])
        return np.cross(dl, r_vec) / np.linalg.norm(r_vec) ** 3

    first = differential(0.37)
    opposite = differential(0.37 + math.pi)
    assert first[0] > 0 and opposite[0] > 0
    close(first[1] + opposite[1], 0.0)
    close(first[2] + opposite[2], 0.0)
    return {"B_at_0.8m_T": field, "B_center_T": center, "moment_A_m2": moment}


def test_ampere_path_independence() -> dict[str, float]:
    # Numerically integrate the field of an infinitely long z-directed wire
    # around centered and offset ellipses. The first encloses the wire, the
    # second does not.
    theta = np.linspace(0, 2 * math.pi, 200_001)
    def integral(cx: float, ax: float, by: float) -> float:
        px = cx + ax * np.cos(theta)
        py = by * np.sin(theta)
        dpx = -ax * np.sin(theta)
        dpy = by * np.cos(theta)
        rho2 = px**2 + py**2
        bx = -MU0 / (2 * math.pi) * py / rho2
        by_field = MU0 / (2 * math.pi) * px / rho2
        integrand = bx * dpx + by_field * dpy
        return float(np.trapezoid(integrand, theta))

    enclosed = integral(0.0, 0.7, 0.4)
    not_enclosed = integral(1.2, 0.4, 0.3)
    close(enclosed, MU0, rel=1e-8)
    close(not_enclosed, 0.0, rel=1e-8)
    return {"ellipse_enclosing_wire_Wb_per_A": enclosed, "ellipse_not_enclosing_wire": not_enclosed}


def test_ampere_applications() -> dict[str, float]:
    current, radius, r = 4.0, 0.02, 0.01
    inside = MU0 * current * r / (2 * math.pi * radius**2)
    outside = MU0 * current / (2 * math.pi * radius)
    at_surface_inside = MU0 * current * radius / (2 * math.pi * radius**2)
    at_surface_outside = MU0 * current / (2 * math.pi * radius)
    close(at_surface_inside, at_surface_outside)
    assert inside > 0 and outside > 0 and inside < at_surface_inside

    # A path around an ideal coax encloses equal and opposite currents.
    net_enclosed = current - current
    assert net_enclosed == 0
    external_coax_field = MU0 * net_enclosed / (2 * math.pi * 0.05)
    assert external_coax_field == 0

    turns_per_m, solenoid_current, length = 850.0, 1.3, 0.4
    b_solenoid = MU0 * turns_per_m * solenoid_current
    loop_integral = b_solenoid * length
    enclosed_solenoid_current = turns_per_m * length * solenoid_current
    close(loop_integral, MU0 * enclosed_solenoid_current)

    turns, toroid_current, path_r = 500, 1.3, 0.08
    b_toroid = MU0 * turns * toroid_current / (2 * math.pi * path_r)
    close(b_toroid, MU0 * (turns * toroid_current) / (2 * math.pi * path_r))
    return {
        "cylinder_inside_T": inside,
        "cylinder_outside_at_R_T": outside,
        "solenoid_midpoint_T": b_solenoid,
        "toroid_core_field_T": b_toroid,
    }


def test_magnetic_materials() -> dict[str, float]:
    bohr_magneton = E_CHARGE * PLANCK / (4 * math.pi * ELECTRON_MASS)
    close(bohr_magneton, 9.2740100783e-24, rel=2e-6)

    max_interaction = bohr_magneton * 1.5
    mean_thermal = 1.5 * BOLTZMANN * 300.0
    ratio = max_interaction / mean_thermal
    close(max_interaction, 1.3911015117e-23, rel=2e-6)
    close(mean_thermal, 6.2129205e-21, rel=1e-9)
    close(ratio, 0.0022389, rel=2e-4)
    return {
        "Bohr_magneton_J_per_T": bohr_magneton,
        "NO_interaction_energy_J": max_interaction,
        "mean_thermal_energy_J": mean_thermal,
        "energy_ratio": ratio,
    }


def test_example_28_12() -> dict[str, float]:
    magnetization = 8e5
    side = 2e-2
    distance = 0.10
    moment = magnetization * side**3
    field = MU0 * moment / (2 * math.pi * distance**3)
    close(moment, 6.4)
    close(field, 1.28e-3)
    # Approximation check: the largest dimension is small versus observation distance.
    close(side / distance, 0.2)
    return {"magnet_moment_A_m2": moment, "axis_field_T": field}


def main() -> None:
    checks = {
        "loop and Example 28.6": test_loop_geometry_and_example_28_6(),
        "Ampere path-independence": test_ampere_path_independence(),
        "Ampere applications": test_ampere_applications(),
        "magnetic-material constants": test_magnetic_materials(),
        "Example 28.12": test_example_28_12(),
    }
    for name, values in checks.items():
        print(f"PASS {name}: {values}")


if __name__ == "__main__":
    main()
