"""Recompute numerical results used in the chapter 29 theory drafts."""
import math
import numpy as np

# Example 29.1: changing B through one loop, then Ohm's law.
area_291 = 120e-4
rate_b_291 = 0.020
resistance_291 = 5.0
emf_291 = area_291 * rate_b_291
current_291 = emf_291 / resistance_291
assert math.isclose(emf_291, 2.4e-4, rel_tol=1e-12)
assert math.isclose(current_291, 4.8e-5, rel_tol=1e-12)

# Example 29.2: field angle is 30 degrees from the area vector.
turns_292 = 500
radius_292 = 0.0400
rate_b_292 = 0.200
angle_292 = math.radians(30.0)
emf_292 = turns_292 * rate_b_292 * math.pi * radius_292**2 * math.cos(angle_292)
assert math.isclose(emf_292, 0.4353, rel_tol=1e-3)

# Example 29.4: mean absolute emf of a commutated rotating coil.
mean_emf_294 = 112.0
turns_294 = 500
field_294 = 0.200
side_294 = 0.100
omega_294 = math.pi * mean_emf_294 / (2 * turns_294 * field_294 * side_294**2)
assert math.isclose(omega_294, 175.9, rel_tol=1e-3)

# Example 29.6: slidewire power balance, in symbolic and numeric form.
field_296, length_296, speed_296, resistance_296 = 0.60, 0.10, 2.5, 0.030
emf_296 = field_296 * length_296 * speed_296
current_296 = emf_296 / resistance_296
force_296 = current_296 * length_296 * field_296
p_diss_296 = current_296**2 * resistance_296
p_mech_296 = force_296 * speed_296
assert math.isclose(emf_296, 0.15, rel_tol=1e-12)
assert math.isclose(current_296, 5.0, rel_tol=1e-12)
assert math.isclose(force_296, 0.30, rel_tol=1e-12)
assert math.isclose(p_diss_296, p_mech_296, rel_tol=1e-12)

# Example 29.9: same slidewire results, with B=0.60 T, L=0.10 m, v=2.5 m/s, R=0.030 ohm.
assert math.isclose(emf_296, 0.15, rel_tol=1e-12)
assert math.isclose(current_296, 5.0, rel_tol=1e-12)
assert math.isclose(force_296, 0.30, rel_tol=1e-12)

# Example 29.10: integrate the radial motional-emf element omega*B*r dr.
# Integral from 0 to R is (1/2)*omega*B*R^2. Verify with an antiderivative.
R = 0.37
omega, B = 12.3, 0.80
integral = 0.5 * omega * B * R**2
r_mid=(np.arange(100000)+0.5)*R/100000
quadrature=float(np.sum(omega*B*r_mid)*(R/100000))
assert math.isclose(integral, quadrature, rel_tol=1e-12)

# Differentiate the rotating-coil flux numerically at a nonstationary phase.
time=.071;delta=1e-7
flux=lambda t:.017*.20*math.cos(12.3*t)
derivative=(flux(time+delta)-flux(time-delta))/(2*delta)
emf_exact=12.3*.20*.017*math.sin(12.3*time)
assert math.isclose(-derivative,emf_exact,rel_tol=1e-8)

# Average the rectified sine by numerical quadrature rather than substituting
# its closed-form mean into the same expression twice.
phase=(np.arange(100000)+.5)*math.pi/100000
rectified_mean=float(np.mean(np.sin(phase)))
assert math.isclose(rectified_mean,2/math.pi,rel_tol=1e-10)

print(f"29.1 emf={emf_291:.8g} V, current={current_291:.8g} A")
print(f"29.2 emf={emf_292:.6f} V")
print(f"29.4 angular_speed={omega_294:.6f} rad/s")
print(f"29.6 emf={emf_296:.6f} V, current={current_296:.6f} A, force={force_296:.6f} N, powers={p_diss_296:.6f} W")
print(f"29.9 emf={emf_296:.6f} V, current={current_296:.6f} A, force={force_296:.6f} N")
print(f"29.10 flux integral={integral:.8g} V")

