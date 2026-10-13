"""Independent numerical checks for Chapter 27 sections 27.1–27.2."""

import math

import numpy as np


def main() -> None:
    charge = 1.6e-19  # C
    speed = 3.0e5  # m/s
    field = 2.0  # T
    angle = math.radians(30.0)

    magnitude = abs(charge) * speed * field * math.sin(angle)
    np.testing.assert_allclose(magnitude, 4.8e-14, rtol=1e-14)

    # The proton velocity lies in xz, while B points along +z.
    velocity = np.array([speed * math.sin(angle), 0.0, speed * math.cos(angle)])
    np.testing.assert_allclose(velocity, [1.5e5, 0.0, 2.598076211e5], rtol=1e-9)
    magnetic_field = np.array([0.0, 0.0, field])
    proton_force = charge * np.cross(velocity, magnetic_field)
    np.testing.assert_allclose(proton_force, [0.0, -4.8e-14, 0.0], rtol=1e-14, atol=1e-29)

    electron_force = -charge * np.cross(velocity, magnetic_field)
    np.testing.assert_allclose(electron_force, [0.0, 4.8e-14, 0.0], rtol=1e-14, atol=1e-29)

    # Parallel and antiparallel motion have no perpendicular velocity component.
    for direction in (1.0, -1.0):
        force = charge * np.cross([0.0, 0.0, direction * speed], magnetic_field)
        np.testing.assert_allclose(force, [0.0, 0.0, 0.0], atol=0.0)

    one_gauss_in_tesla = 1.0 * 1e-4
    np.testing.assert_allclose(one_gauss_in_tesla, 1e-4, rtol=0.0, atol=0.0)
    print("Chapter 27 sections 27.1–27.2: numerical and direction checks passed.")


if __name__ == "__main__":
    main()
