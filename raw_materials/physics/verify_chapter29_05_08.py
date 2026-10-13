"""Recalculate the numerical example and key unit conversions in sections 29.5–29.8."""

from math import isclose, pi


mu0 = 4 * pi * 1e-7
n = 500.0  # turns per meter
area = 4.0e-4  # m^2, converted from 4.0 cm^2
d_current_dt = 100.0  # A/s
radius = 2.0e-2  # m, converted from 2.0 cm

emf = -mu0 * n * area * d_current_dt
electric_field = abs(emf) / (2 * pi * radius)

assert isclose(area, 4.0 * (1e-2) ** 2)
assert isclose(radius, 2.0e-2)
assert isclose(emf, -2.5132741228718345e-5, rel_tol=1e-12)
assert isclose(abs(emf), 25.132741228718345e-6, rel_tol=1e-12)
assert isclose(electric_field, 2.0e-4, rel_tol=1e-12)

print(f"emf = {emf:.8g} V ({emf * 1e6:.5g} µV)")
print(f"|E| = {electric_field:.8g} V/m")
print("Unit conversions: 4.0 cm^2 = 4.0e-4 m^2; 2.0 cm = 2.0e-2 m")
