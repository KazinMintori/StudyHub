"""Independent numerical and cross-product checks for Sections 27.6–27.7."""
from math import cos, pi, sin, sqrt


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def close(actual, expected, tol=1e-9):
    assert abs(actual - expected) <= tol * max(1.0, abs(expected)), (actual, expected)


def close_vec(actual, expected, tol=1e-9):
    for a, e in zip(actual, expected):
        close(a, e, tol)


# Section 27.6, Example 27.7: eastward current and northeast field.
i, length, bmag = 50.0, 1.00, 1.20
phi = pi / 4
lvec = (length, 0.0, 0.0)
bvec = (bmag * cos(phi), bmag * sin(phi), 0.0)
force = scale(i, cross(lvec, bvec))
close(sqrt(dot(force, force)), 42.4264068712)
close_vec(force, (0.0, 0.0, 42.4264068712))

# Rotating the conductor southeast makes it perpendicular to B and retains upward force.
l_se = (length * cos(phi), -length * sin(phi), 0.0)
force_max = scale(i, cross(l_se, bvec))
close(sqrt(dot(force_max, force_max)), 60.0)
close_vec(force_max, (0.0, 0.0, 60.0))
close_vec(scale(-1, force), cross(scale(-i, lvec), bvec))
close_vec(scale(-1, force), scale(i, cross(lvec, scale(-1, bvec))))

# Section 27.6, Example 27.8: integrate force over the semicircle.
# With B out of the page, the arc integral has cancelling x-components and +y net force.
f_arc_x = i * bmag * (sin(pi) - sin(0.0))
f_arc_y = i * bmag * (-cos(pi) + cos(0.0))
close(f_arc_x, 0.0)
close(f_arc_y, 2 * i * bmag)
l_straight = 0.40
f_total_y = f_arc_y + i * l_straight * bmag
close(f_total_y, i * bmag * (2 * 1.0 + l_straight))

# Section 27.7: rectangular loop has zero net force and torque magnitude I A B sin(phi).
current, a, b, bmag = 2.5, 0.30, 0.20, 1.4
for angle in (0.0, pi / 6, pi / 2, pi):
    normal = (sin(angle), 0.0, cos(angle))
    side_a = (0.0, 1.0, 0.0)
    side_b = cross(normal, side_a)
    r_a = scale(a / 2, side_a)
    r_b = scale(b / 2, side_b)
    wire_edges = ((a, side_a), (b, side_b), (a, scale(-1, side_a)), (b, scale(-1, side_b)))
    edge_centers = (scale(-1, r_b), r_a, r_b, scale(-1, r_a))
    total_force = (0.0, 0.0, 0.0)
    total_torque = (0.0, 0.0, 0.0)
    for edge_index, (edge_length, edge_direction) in enumerate(wire_edges):
        edge_force = scale(current * edge_length, cross(edge_direction, (0.0, 0.0, bmag)))
        total_force = add(total_force, edge_force)
        total_torque = add(total_torque, cross(edge_centers[edge_index], edge_force))
    mu = scale(current * a * b, normal)
    expected_torque = cross(mu, (0.0, 0.0, bmag))
    close_vec(total_force, (0.0, 0.0, 0.0))
    close_vec(total_torque, expected_torque)
    close(sqrt(dot(total_torque, total_torque)), current * a * b * bmag * abs(sin(angle)))

# Section 27.7, Example 27.9: 30-turn circular coil.
turns, current, radius, bmag = 30, 5.00, 0.0500, 1.20
area = pi * radius**2
mu = turns * current * area
torque = mu * bmag
close(mu, 1.1780972450961724)
close(torque, 1.4137166941154069)
close(-mu * bmag * (cos(0.0) - cos(pi / 2)), -1.4137166941154069)

# A dipole lowers its potential energy by moving toward alignment; a field gradient
# attracts a parallel moment and repels an antiparallel one in the 1-D magnet model.
close(-mu * bmag * cos(0.0), -mu * bmag)
close(-mu * bmag * cos(pi), mu * bmag)
dbdx = 0.10  # field magnitude increases toward the magnet
close(mu * dbdx, 0.11780972450961725)  # parallel: toward stronger field
close(-mu * dbdx, -0.11780972450961725)  # antiparallel: toward weaker field

print("PASS: Sections 27.6–27.7 magnitudes, vector directions, torque, energy, and field-gradient checks")
print(f"27.6 straight-wire example: F={sqrt(dot(force, force)):.3f} N up; maximum={sqrt(dot(force_max, force_max)):.3f} N up")
print(f"27.6 curved-wire example: F_arc=({f_arc_x:.3g}, {f_arc_y:.3f}) N; total y force={f_total_y:.3f} N")
print(f"27.7 circular coil: mu={mu:.3f} A m^2; torque={torque:.3f} N m; aligned-state energy change={-torque:.3f} J")
