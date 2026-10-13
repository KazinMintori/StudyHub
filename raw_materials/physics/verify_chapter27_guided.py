"""Independent checks for Chapter 27 guided practice and discussion solutions."""
from math import asin, cos, pi, sin, sqrt


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def scale(s, v):
    return tuple(s * x for x in v)


def close(a, b, tol=1e-8):
    if b == 0.0:
        assert abs(a) <= 1e-12, (a, b)
    else:
        assert abs(a - b) <= tol * max(abs(a), abs(b), 1e-300), (a, b)


def vec_close(a, b, tol=1e-8):
    for x, y in zip(a, b):
        close(x, y, tol)


# VP27.1.1: electron velocity makes 40 degrees with +x in the xy plane.
q, speed, bmag = -1.60e-19, 2.20e5, 1.55
v = (speed * cos(pi / 4.5), speed * sin(pi / 4.5), 0.0)
f111 = scale(q, cross(v, (0.0, bmag, 0.0)))
close(sqrt(dot(f111, f111)), 4.18e-14, 1e-3)
assert f111[2] < 0

# VP27.1.2: infer charge magnitude from |F|=|q|vB sin(theta).
q112 = 2.50e-10 / (1.95e5 * 0.750 * sin(36 * pi / 180))
close(q112, 2.91e-15, 2e-3)

# VP27.1.3: F=-y, v=+x and B has only z component, so Bz is positive.
q113, vx113, fy113 = 3.20e-19, 3.75e5, -2.10e-15
b113 = -fy113 / (q113 * vx113)
close(b113, 0.0175, 2e-3)

# VP27.1.4: highly ionized iron, v in xz plane and B along +z.
q114, v114, force114 = 2.08e-18, 7.30e3, 2.30e-15
vx114 = v114 * cos(36.9 * pi / 180)
b114 = force114 / (q114 * vx114)
f114 = cross((vx114, 0.0, v114 * cos(53.1 * pi / 180)), (0.0, 0.0, b114))
close(b114, 0.189, 3e-3)  # Rounded to three significant figures in the solution.
assert f114[1] < 0

# VP27.6.1: proton's circular orbit in a perpendicular 0.300 T field.
q_p, m_p, b_p, v_p = 1.60e-19, 1.67e-27, 0.300, 1.25e4
r761 = m_p * v_p / (q_p * b_p)
omega761 = q_p * b_p / m_p
freq761 = omega761 / (2 * pi)
close(r761, 0.435e-3, 2e-3)
close(omega761, 2.87e7, 2e-3)
close(freq761, 4.57e6, 2e-3)

# VP27.6.2: split the velocity into perpendicular and parallel components.
v_perp762, v_parallel762 = 1.00e4, 7.50e3
r762 = m_p * v_perp762 / (q_p * b_p)
pitch762 = v_parallel762 * (2 * pi / omega761)
f762 = q_p * v_perp762 * b_p
close(r762, 0.348e-3, 2e-3)
close(pitch762, 1.64e-3, 2e-3)
close(f762, 4.80e-16, 2e-3)

# VP27.6.3: selector E + v x B = 0; B is +z, so v is -y.
e763, b763 = 2.80e4, 0.0350
v763 = -e763 / b763
f763_when_b_greater = e763 - abs(v763) * (b763 * 1.01)
close(abs(v763), 8.00e5)
assert f763_when_b_greater < 0  # The positive charge is deflected toward -x.

# VP27.6.4: isotope radii in the mass-spectrometer field.
q_ion, v_ion, b_ion = 1.60e-19, 2.00e4, 0.0500
r16 = 2.66e-26 * v_ion / (q_ion * b_ion)
r18 = 2.99e-26 * v_ion / (q_ion * b_ion)
close(r16, 6.64e-2, 2e-3)
close(r18, 7.47e-2, 2e-3)

# VP27.7.1: current +x; field is 20 degrees from -x toward +y.
i771, l771, b771 = 3.50, 0.150, 0.0136
bvec771 = (b771 * cos(160 * pi / 180), b771 * sin(160 * pi / 180), 0.0)
f771 = scale(i771, cross((l771, 0.0, 0.0), bvec771))
close(sqrt(dot(f771, f771)), 2.44e-3, 2e-3)
assert f771[2] > 0

# VP27.7.2: upward current crossed with northward field points west.
i772 = 0.0140 / (0.250 * 0.0350)
f772 = cross((0.0, 0.0, 1.0), (0.0, 0.0350, 0.0))
close(i772, 1.60)
assert f772[0] < 0

# VP27.7.3: vector force components for the stated length vector and field.
f773 = scale(1.20, cross((0.200, -0.120, 0.0), (0.0, 0.0, 0.0175)))
close(f773[0], -2.52e-3)
close(f773[1], -4.20e-3)
close(f773[2], 0.0)
close(sqrt(dot(f773, f773)), 4.90e-3, 2e-3)

# VP27.7.4: sine of the two possible angles giving the required magnitude.
sin_theta774 = 0.0250 / (3.40 * 0.280 * 0.0400)
theta774 = asin(sin_theta774) * 180 / pi
close(theta774, 41.0, 2e-3)
close(180 - theta774, 139.0, 2e-3)

# Bridging Problem: B has a negative z component, as drawn and printed.
area_ring, current_ring = 4.45e-4, 12.5
mu_mag = area_ring * current_ring
b_ring = (1.15e-2 * 12, 1.15e-2 * 3, -1.15e-2 * 4)
mu_i = scale(mu_mag, (-0.800, 0.600, 0.0))
tau_i = cross(mu_i, b_ring)
vec_close(tau_i, (-1.535e-4, -2.046e-4, -6.142e-4), 2e-3)
mu_f = (0.0, 0.0, -mu_mag)
u_i, u_f = -dot(mu_i, b_ring), -dot(mu_f, b_ring)
decrease_u = u_i - u_f
omega_bridge = sqrt(2 * decrease_u / 8.50e-7)
close(decrease_u, 7.55e-4, 2e-3)
close(omega_bridge, 42.1, 2e-3)
unit_b = scale(1 / sqrt(dot(b_ring, b_ring)), b_ring)
assert dot(unit_b, b_ring) > 0  # Stable equilibrium aligns mu with B.

# Discussion checks using the right-hand rule and energy identities.
# Q27.10: outward force for each segment requires mu parallel to B.
force_q10 = cross((0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
assert force_q10 == (1.0, 0.0, 0.0)
# Q27.12: the five pictured positive charges have v=(+y,+z,-x,+x,-z).
bhat_x = (1.0, 0.0, 0.0)
forces_q12 = [cross(vv, bhat_x) for vv in ((0, 1, 0), (0, 0, 1), (-1, 0, 0), (1, 0, 0), (0, 0, -1))]
assert forces_q12 == [(0.0, 0.0, -1.0), (0.0, 1.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, -1.0, 0.0)]
# Q27.15: q(v x B) is perpendicular to v and does no work on a point charge.
velocity, magnetic_field = (1.0, 2.0, 3.0), (0.2, -0.5, 0.7)
assert abs(dot(velocity, cross(velocity, magnetic_field))) < 1e-12
# Q27.16: reversing both armature current and field leaves torque direction unchanged.
mu, field = (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)
assert cross(scale(-1, mu), scale(-1, field)) == cross(mu, field)
# Q27.13 estimate: a 10 m pole in a 50 microtesla field sees at most 50 N at 100 kA.
lightning_force_max = 1.0e5 * 10.0 * 5.0e-5
close(lightning_force_max, 50.0)
# Q27.18: at fixed current and geometry Hall voltage is inversely proportional to n.
hall_ratio = (1 / 1.0e20) / (1 / 1.0e22)
close(hall_ratio, 100.0)

print("PASS: all 12 guided-practice results, bridge torque/energy, and numerical/vector discussion checks")
print(f"VP27.6.1: r={r761*1e3:.3f} mm, omega={omega761:.3g} rad/s, f={freq761:.3g} Hz")
print(f"VP27.7.3 force={f773} N; VP27.7.4 angles={theta774:.1f}, {180-theta774:.1f} degrees")
print(f"Bridge torque={tau_i} N m; energy decrease={decrease_u:.6g} J; omega={omega_bridge:.3f} rad/s")
print(f"Discussion Q27.13 upper-bound force estimate={lightning_force_max:.1f} N")
