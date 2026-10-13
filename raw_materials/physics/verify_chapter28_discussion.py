"""Independent checks for vector, symmetry, and scaling claims in Q28.1–Q28.20."""

from itertools import product

import numpy as np


MU0 = 4 * np.pi * 1e-7


def close(a, b, rtol=1e-8, atol=1e-14):
    assert np.allclose(a, b, rtol=rtol, atol=atol), (a, b)


def wire_field(current, wire_xy, point_xy):
    displacement = np.asarray(point_xy, dtype=float)-np.asarray(wire_xy, dtype=float)
    return MU0*current/(2*np.pi*np.dot(displacement,displacement))*np.array([-displacement[1],displacement[0]])


def field_loop(radius, current, point, samples=20000):
    """Numerical Biot–Savart field of a CCW circular loop in the xy-plane."""
    theta = np.arange(samples) * (2 * np.pi / samples)
    dtheta = 2 * np.pi / samples
    source = np.column_stack((radius * np.cos(theta), radius * np.sin(theta),
                              np.zeros(samples)))
    dl = np.column_stack((-radius * np.sin(theta), radius * np.cos(theta),
                          np.zeros(samples))) * dtheta
    r = np.asarray(point, dtype=float) - source
    dB = np.cross(dl, r) / np.linalg.norm(r, axis=1)[:, None]**3
    return MU0 * current / (4 * np.pi) * dB.sum(axis=0)


def main():
    # Q1: a hypothetical radial monopole field has nonzero flux through a closed sphere.
    g, radius = 2.0, 3.0
    n_theta, n_phi = 240, 480
    theta = (np.arange(n_theta)+0.5)*np.pi/n_theta
    phi = (np.arange(n_phi)+0.5)*2*np.pi/n_phi
    tt, pp = np.meshgrid(theta, phi, indexing="ij")
    darea = radius**2*np.sin(tt)*(np.pi/n_theta)*(2*np.pi/n_phi)
    monopole_flux = np.sum((g/radius**2)*darea)
    close(monopole_flux, 4*np.pi*g, rtol=2e-5)

    # Q2: a directed stream has a nonzero magnetic field and reversing it reverses B.
    q_stream, v_stream = 2e-9, 3e5
    r_stream = np.array([0.0, 0.04, 0.0])
    b_stream = 1e-7*q_stream*np.cross([v_stream,0,0], r_stream)/np.linalg.norm(r_stream)**3
    b_reverse = 1e-7*q_stream*np.cross([-v_stream,0,0], r_stream)/np.linalg.norm(r_stream)**3
    assert b_stream[2] > 0 and np.allclose(b_reverse, -b_stream)

    # Q3/Q10: Biot–Savart for a finite centered wire approaches Ampere's
    # infinite-wire field as both ends recede compared with the observation distance.
    radius_obs, half_length, current = 0.02, 2.0, 3.0
    dz = 2*half_length/20000
    z = np.linspace(-half_length+dz/2, half_length-dz/2, 20000)
    dl = np.tile([0.0, 0.0, dz], (len(z),1))
    rvec = np.column_stack((np.full_like(z,radius_obs), np.zeros_like(z), -z))
    b_finite = 1e-7*current*np.sum(np.cross(dl,rvec)/np.linalg.norm(rvec,axis=1)[:,None]**3,axis=0)
    b_ampere = MU0*current/(2*np.pi*radius_obs)
    close(np.linalg.norm(b_finite)/b_ampere, half_length/np.hypot(half_length,radius_obs), rtol=1e-7)
    assert np.linalg.norm(b_finite)/b_ampere > 0.9999

    # Q4: magnetic force does no work on a point charge.
    v = np.array([1.2, -0.7, 2.3])
    B = np.array([-0.4, 1.5, 0.8])
    assert abs(np.dot(v, np.cross(v, B))) < 1e-12

    # Q6: same-direction currents attract all pairs; no binary directions repel all three.
    assignments = list(product((1, -1), repeat=3))
    assert any(a == b == c for a, b, c in assignments)
    assert not any(a != b and b != c and a != c for a, b, c in assignments)

    # Q7: including a symmetric conductor's self-field cannot create a net
    # translational force on the whole conductor (internal forces cancel).
    n_loop, loop_r, dtheta = 160, 0.2, 2*np.pi/160
    theta = np.arange(n_loop)*dtheta
    sources = np.column_stack((loop_r*np.cos(theta),loop_r*np.sin(theta),np.zeros(n_loop)))
    elements = np.column_stack((-loop_r*np.sin(theta),loop_r*np.cos(theta),np.zeros(n_loop)))*dtheta
    self_forces = []
    for i in range(n_loop):
        displacement = sources[i]-sources
        distance = np.linalg.norm(displacement,axis=1)
        valid = np.arange(n_loop) != i
        bself = 1e-7*np.sum(np.cross(elements[valid],displacement[valid])/
                            distance[valid,None]**3,axis=0)
        self_forces.append(np.cross(elements[i],bself))
    self_forces = np.asarray(self_forces)
    assert np.linalg.norm(self_forces.sum(axis=0)) < 1e-10*np.linalg.norm(self_forces,axis=1).sum()
    assert np.linalg.norm(self_forces,axis=1).mean() > 0

    # Q5/Q9: a nearby return wire cancels most far field; parallel nearby
    # segments with equal current attract, consistent with a spring contracting.
    sep, far = 1e-3, 0.10
    b_pair = wire_field(1.0,[0,-sep/2],[far,0]) + wire_field(-1.0,[0,sep/2],[far,0])
    b_single = wire_field(1.0,[0,-sep/2],[far,0])
    assert np.linalg.norm(b_pair) < 0.02*np.linalg.norm(b_single)
    force_on_upper = -MU0*2.0*3.0/(2*np.pi*sep**2)*np.array([0.0,sep])
    assert force_on_upper[1] < 0

    # Q8: same-direction concentric loops give outward force on inner loop,
    # inward force on outer loop. Evaluate Bz numerically from Biot–Savart.
    r_inner, r_outer = 0.4, 1.0
    bz_inside = field_loop(r_outer, 1.0, [r_inner, 0, 0])[2]
    bz_outside = field_loop(r_inner, 1.0, [r_outer, 0, 0])[2]
    assert bz_inside > 0 and bz_outside < 0
    dl_at_x = np.array([0.0, 1.0, 0.0])
    assert np.cross(dl_at_x, [0, 0, bz_inside])[0] > 0
    assert np.cross(dl_at_x, [0, 0, bz_outside])[0] < 0

    # Q12: for opposite currents, cancellation would require equal inverted
    # displacement vectors, which is impossible for distinct wire locations.
    # For same currents, the midpoint is an explicit cancellation point.
    a = 0.5
    r_top = np.array([0.0, -a])
    r_bottom = np.array([0.0, a])
    inv = lambda r: r / np.dot(r, r)
    opposite_midpoint = inv(r_top) - inv(r_bottom)
    same_midpoint = inv(r_top) + inv(r_bottom)
    assert np.linalg.norm(opposite_midpoint) > 0
    close(same_midpoint, np.zeros(2))

    # Q11: an ideal toroidal field is tangent to closed azimuthal paths.
    angles = np.linspace(0, 2*np.pi, 721)
    tangent = np.column_stack((-np.sin(angles), np.cos(angles)))
    assert np.allclose(tangent[0], tangent[-1])
    assert np.allclose(np.linalg.norm(tangent,axis=1), 1.0)

    # Q13: polarity b+ drives current through L leftward, parallel to the
    # lower-wire current. The corresponding force is attractive.
    current_lower = np.array([-1.0, 0.0, 0.0])
    current_L_if_b_positive = np.array([-1.0, 0.0, 0.0])
    assert np.dot(current_lower, current_L_if_b_positive) > 0
    current_L_if_a_positive = np.array([1.0, 0.0, 0.0])
    assert np.dot(current_lower, current_L_if_a_positive) < 0

    # Q14: doubling loop radius halves its center field, but changes the
    # off-axis field by a geometry-dependent ratio.
    a0, x = 0.2, 0.5
    ratio_center = (1 / (2*a0)) / (1 / a0)
    ratio_axis = 4 * ((a0*a0 + x*x) / (4*a0*a0 + x*x))**1.5
    close(ratio_center, 0.5)
    assert not np.isclose(ratio_axis, ratio_center)

    # Q15: divide the dimensions of joule by tesla.
    # J/T = (N m)/(N/(A m)) = A m^2.
    joule = {"N": 1, "m": 1}
    tesla = {"N": 1, "A": -1, "m": -1}
    quotient = {unit: joule.get(unit, 0)-tesla.get(unit, 0)
                for unit in set(joule) | set(tesla)}
    assert quotient == {"N": 0, "m": 2, "A": 1}

    # Q16/Q17/Q19: Curie response falls with temperature; susceptibility
    # sign determines attraction/repulsion toward a field-strength gradient.
    temperature = np.array([100.0, 200.0, 400.0])
    chi_para = 2.0/temperature
    assert np.all(np.diff(chi_para) < 0)
    chi_oxygen, chi_nitrogen = 1e-3, -1e-5
    grad_b2 = np.array([1.0, 0.0, 0.0])
    force_o2 = chi_oxygen*grad_b2
    force_n2 = chi_nitrogen*grad_b2
    assert force_o2[0] > 0 and force_n2[0] < 0
    chi_dia = -1e-5*np.ones_like(temperature)
    assert np.all(np.diff(chi_dia) == 0)

    # Q18: paired moments cancel; an unpaired moment leaves a permanent moment.
    paired = np.array([0.0,0.0,1.0])+np.array([0.0,0.0,-1.0])
    unpaired = paired+np.array([0.0,0.0,1.0])
    close(paired, [0,0,0])
    close(unpaired, [0,0,1])

    # Q20: the rotor compensates the reversed microscopic angular momentum.
    delta_l_micro = np.array([0.0,0.0,-2.0])
    delta_l_rotor = -delta_l_micro
    close(delta_l_micro+delta_l_rotor, [0,0,0])

    print("Chapter 28 Discussion Questions: independent checks passed.")


if __name__ == "__main__":
    main()
