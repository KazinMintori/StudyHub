"""Independent numerical checks for Chapter 27 sections 27.4–27.5."""

import math

import numpy as np


def main() -> None:
    electron_mass = 9.11e-31  # kg
    elementary_charge = 1.60e-19  # C

    # Example 27.3: magnetron electron cyclotron field.
    frequency = 2450e6  # Hz
    angular_speed = 2 * math.pi * frequency
    magnetron_field = electron_mass * angular_speed / elementary_charge
    np.testing.assert_allclose(magnetron_field, 0.0877, rtol=1e-3)

    # Example 27.4: proton helix in B = +x.
    proton_charge = 1.60e-19  # C
    proton_mass = 1.67e-27  # kg
    field = np.array([0.500, 0.0, 0.0])  # T
    velocity = np.array([1.50e5, 0.0, 2.00e5])  # m/s
    force = proton_charge * np.cross(velocity, field)
    acceleration = force / proton_mass
    np.testing.assert_allclose(force, [0.0, 1.60e-14, 0.0], rtol=1e-14, atol=1e-29)
    np.testing.assert_allclose(acceleration, [0.0, 9.58e12, 0.0], rtol=1e-3, atol=1e-5)

    radius = proton_mass * 2.00e5 / (proton_charge * 0.500)
    proton_omega = proton_charge * 0.500 / proton_mass
    period = 2 * math.pi / proton_omega
    pitch = 1.50e5 * period
    np.testing.assert_allclose(radius, 4.18e-3, rtol=2e-3)
    np.testing.assert_allclose(proton_omega, 4.79e7, rtol=1e-3)
    np.testing.assert_allclose(period, 1.31e-7, rtol=2e-3)
    np.testing.assert_allclose(pitch, 1.97e-2, rtol=2e-3)

    # Example 27.5: Thomson e/m demonstration.
    e_over_m = 1.76e11  # C/kg
    accelerating_voltage = 150.0  # V
    electric_field = 6.0e6  # N/C
    electron_speed = math.sqrt(2 * e_over_m * accelerating_voltage)
    selector_field = electric_field / electron_speed
    radicand = 2 * e_over_m * accelerating_voltage
    np.testing.assert_allclose(radicand, 5.28e13, rtol=1e-14)
    np.testing.assert_allclose(electron_speed, 7.27e6, rtol=1e-3)
    np.testing.assert_allclose(round(selector_field, 2), 0.83, rtol=0.0, atol=0.0)
    reconstructed_e_over_m = electric_field**2 / (
        2 * accelerating_voltage * selector_field**2
    )
    np.testing.assert_allclose(reconstructed_e_over_m, e_over_m, rtol=1e-14)

    # Example 27.6: He+ semicircle in a mass spectrometer.
    helium_charge = elementary_charge
    helium_mass = 6.65e-27  # kg
    helium_speed = 1.00e5  # m/s
    radius = 10.16e-2 / 2  # The stated detector distance is the semicircle diameter.
    numerator = helium_mass * helium_speed
    denominator = helium_charge * radius
    helium_field = numerator / denominator
    np.testing.assert_allclose(radius, 5.08e-2, rtol=1e-14)
    np.testing.assert_allclose(numerator, 6.65e-22, rtol=1e-14)
    np.testing.assert_allclose(denominator, 8.128e-21, rtol=1e-14)
    np.testing.assert_allclose(helium_field, 0.0818, rtol=1e-3)

    # The same crossed-field selector passes He+ and He2+ at the same speed.
    for charge in (elementary_charge, 2 * elementary_charge):
        net_force = charge * 1.0 - charge * helium_speed * (1.0 / helium_speed)
        np.testing.assert_allclose(net_force, 0.0, atol=1e-34)

    print("Chapter 27 sections 27.4–27.5: numerical and direction checks passed.")


if __name__ == "__main__":
    main()
