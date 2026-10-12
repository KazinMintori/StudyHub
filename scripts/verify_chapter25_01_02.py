"""Independent arithmetic checks for Young & Freedman Chapter 25, Sections 25.1–25.2."""

from math import pi, isclose


def close(actual, expected, *, rel=5e-3):
    assert isclose(actual, expected, rel_tol=rel, abs_tol=0.0), (actual, expected)


# Example 25.1: 18-gauge copper wire carrying 1.67 A.
current = 1.67  # A
diameter = 1.02e-3  # m
electron_density = 8.5e28  # m^-3
elementary_charge = 1.60e-19  # C
area = pi * diameter**2 / 4
current_density = current / area
drift_speed = current_density / (electron_density * elementary_charge)
travel_time_one_metre = 1.0 / drift_speed

close(area, 8.17e-7)
close(current_density, 2.04e6)
close(drift_speed, 1.5e-4)
close(drift_speed * 1e3, 0.15)
close(travel_time_one_metre, 6.7e3, rel=0.01)

# Doubling the diameter quadruples area, so J and drift speed fall by four.
wide_area = pi * (2 * diameter) ** 2 / 4
wide_current_density = current / wide_area
wide_drift_speed = wide_current_density / (electron_density * elementary_charge)
close(wide_area / area, 4.0, rel=1e-12)
close(wide_drift_speed / drift_speed, 0.25, rel=1e-12)
close(wide_drift_speed * 1e3, 0.0375)

# Sign check: conventional current density points with E for either carrier sign.
positive_carrier_current = (+1.0) * (+2.0)
electron_current = (-1.0) * (-2.0)
assert positive_carrier_current > 0
assert electron_current > 0

# Table 25.1: reciprocal of copper resistivity gives representative conductivity.
copper_resistivity = 1.72e-8  # ohm m
copper_conductivity = 1.0 / copper_resistivity
close(copper_conductivity, 5.81e7)

print(f"A={area:.4g} m^2")
print(f"J={current_density:.4g} A/m^2")
print(f"v_d={drift_speed:.4g} m/s = {drift_speed * 1e3:.3g} mm/s")
print(f"time for 1 m={travel_time_one_metre:.4g} s")
print(f"double-diameter v_d={wide_drift_speed * 1e3:.4g} mm/s")
print(f"copper conductivity={copper_conductivity:.4g} S/m")
print("All Chapter 25.1–25.2 numerical and sign checks passed.")
