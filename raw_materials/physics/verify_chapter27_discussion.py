"""Independent direction and estimate checks for Discussion Questions Q27.1–Q27.18."""
from math import cos, pi, sin


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def scale(s, v):
    return tuple(s * x for x in v)


def close(a, b, tol=1e-9):
    if b == 0.0:
        assert abs(a) <= 1e-12, (a, b)
    else:
        assert abs(a - b) <= tol * max(abs(a), abs(b), 1e-300), (a, b)


# Q27.1 and Q27.7: v parallel to B produces zero magnetic force.
assert cross((1.0, 2.0, 3.0), scale(4.0, (1.0, 2.0, 3.0))) == (0.0, 0.0, 0.0)

# Q27.3/Q27.6/Q27.15: magnetic force is reversed for q<0 and perpendicular to v.
v, b = (1.0, -2.0, 0.5), (0.2, 0.4, -0.8)
f_positive = cross(v, b)
f_negative = scale(-1.0, f_positive)
assert abs(dot(v, f_positive)) < 1e-12
assert abs(dot(v, f_negative)) < 1e-12
assert f_negative == scale(-1.0, f_positive)

# Q27.5: choose a circular orbit of radius 0.4 side lengths in a centered plane.
side, radius = 1.0, 0.4
assert radius < side / 2

# Q27.8/Q27.10: a counterclockwise loop viewed from +z has mu=+z; with B=+z,
# dℓ x B points radially outward at representative points around the circle.
for theta in (0.0, pi / 2, pi, 3 * pi / 2):
    radial = (cos(theta), sin(theta), 0.0)
    tangent = (-radial[1], radial[0], 0.0)
    force_per_length = cross(tangent, (0.0, 0.0, 1.0))
    close(dot(force_per_length, radial), 1.0)

# Q27.11: with v perpendicular to B, r scales with v and reverses curvature with q.
m, q, B, v0 = 2.0, 1.0, 0.5, 3.0
r = m * v0 / (q * B)
close(m * (2 * v0) / (q * B), 2 * r)
close(m * v0 / (abs(-q) * B), r)

# Q27.12: source figure has B=+x and v at a,b,c,d,e respectively +y,+z,-x,+x,-z.
B = (1.0, 0.0, 0.0)
velocities = ((0, 1, 0), (0, 0, 1), (-1, 0, 0), (1, 0, 0), (0, 0, -1))
forces = [cross(velocity, B) for velocity in velocities]
expected = [(0, 0, -1), (0, 1, 0), (0, 0, 0), (0, 0, 0), (0, -1, 0)]
assert forces == expected

# Q27.13: explicit upper-bound estimate under assumptions stated in the solution.
force_lightning = 1.0e5 * 10.0 * 5.0e-5
close(force_lightning, 50.0)
close(1.0e4 * 10.0 * 5.0e-5, 5.0)

# Q27.16: series-field motor reverses both vectors; PM motor reverses only armature.
mu, Bfield = (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)
torque_initial = cross(mu, Bfield)
torque_series_reversed = cross(scale(-1, mu), scale(-1, Bfield))
torque_pm_reversed = cross(scale(-1, mu), Bfield)
assert torque_series_reversed == torque_initial
assert torque_pm_reversed == scale(-1, torque_initial)

# Q27.17/Q27.18: Hall force vanishes when drift is parallel B; at fixed geometry,
# Hall voltage is proportional to 1/n.
assert cross((0.0, 0.0, 2.0), (0.0, 0.0, 3.0)) == (0.0, 0.0, 0.0)
close((1 / 1.0e20) / (1 / 1.0e22), 100.0)

print("PASS: discussion vector directions, no-work condition, Hall scaling, motor cases, and estimate")
print(f"Q27.13: estimated upper bound={force_lightning:.1f} N for 10 m and 100 kA")
print(f"Q27.12 force directions at a–e: {forces}")
