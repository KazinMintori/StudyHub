"""Independent numerical and direction checks for Exercises 27.31–27.60."""

import math

import numpy as np


E = 1.60e-19
MP = 1.67e-27
ME = 9.11e-31
G = 9.80


def close(actual, expected, rtol=4e-3):
    np.testing.assert_allclose(actual, expected, rtol=rtol, atol=1e-28)


def main() -> None:
    # 27.31–27.34: Magnetic forces and the magnetic balance.
    i31 = 0.750 * G / (0.500 * 0.450)
    v31 = i31 * 25.0
    i31_short = v31 / 2.0
    a31 = (i31_short * 0.500 * 0.450 - 0.750 * G) / 0.750
    close(i31, 32.7)
    close(v31, 8.17e2)
    close(a31, 112.7)

    f32 = 10.8 * (2 * 0.0250) * 0.550
    close(f32, 0.297)

    # Fig. E27.33: current a→b and B into the page give an upward force.
    i33 = 175.0 / 5.00
    f33 = i33 * 0.600 * 1.50
    close(i33, 35.0)
    close(f33 / G, 3.21)
    np.testing.assert_allclose(np.cross([1.0, 0.0, 0.0], [0.0, 0.0, -1.0]),
                               [0.0, 1.0, 0.0])

    f34 = 2.60 * 0.0100 * 0.588
    f34c = 2.60 * np.cross([0.0, 0.0, -0.0100],
                          [-0.588 * math.cos(math.radians(30)),
                           -0.588 * math.sin(math.radians(30)), 0.0])
    close(f34, 1.53e-2)
    np.testing.assert_allclose(f34c, [-7.64e-3, 1.32e-2, 0.0], rtol=4e-3)

    # 27.35–27.42: Dipole moments, torques, and rotational motion.
    turns35 = 0.194 / (8.80 * 4.0e-4)
    torque35 = 0.194 * 45.0
    close(turns35, 55.1)
    close(torque35, 8.73)

    area36 = 0.050 * 0.080
    moment36 = 6.2 * area36
    perimeter36 = 2 * (0.050 + 0.080)
    max_area36 = perimeter36**2 / (4 * math.pi)
    max_torque36 = 6.2 * 0.19 * max_area36
    close(moment36, 2.48e-2)
    close(max_torque36, 6.34e-3)

    # Fig. E27.37: clockwise loop, 20 cm hinge, 35 cm width, B = +x.
    field37 = np.array([1.20, 0.0, 0.0])
    length37 = 5.00 * np.array([0.0, 0.200, 0.0])
    f37_ab = np.cross(length37, field37)
    f37_cd = 5.00 * np.cross([0.0, -0.200, 0.0], field37)
    torque37 = np.cross([0.350, 0.0, 0.0], f37_cd)
    np.testing.assert_allclose(f37_ab, [0.0, 0.0, -1.20], rtol=1e-14)
    np.testing.assert_allclose(f37_cd, [0.0, 0.0, 1.20], rtol=1e-14)
    np.testing.assert_allclose(torque37, [0.0, -0.420, 0.0], rtol=1e-14)

    moment38 = 1.95 * 0.220 * 0.350
    torque38 = moment38 * 1.50 * math.sin(math.radians(30.0))
    close(moment38, 0.150)
    close(torque38, 0.113)

    mass39 = 0.212
    wire_density39 = mass39 / (2 * (1.00 + 0.500))
    inertia39 = (2 * wire_density39 * 1.00 * 0.250**2
                 + 2 * wire_density39 * 0.500**3 / 12)
    torque39 = 2.00 * (1.00 * 0.500) * 3.00
    alpha39 = torque39 / inertia39
    close(inertia39, 1.03e-2)
    close(alpha39, 291.0)

    mu40 = np.array([0.0, 0.0, 1.0])
    field40 = np.array([0.0, 0.0, 1.0])
    torque40 = np.cross(mu40, field40)
    np.testing.assert_allclose(torque40, [0.0, 0.0, 0.0])
    # Diagram currents give μA = −z (unstable) and μB = +z (stable).
    assert float(np.dot([-0.0, 0.0, -1.0], field40)) < 0
    assert float(np.dot([0.0, 0.0, 1.0], field40)) > 0

    tau41_a = np.cross([0.0, 0.0, 1.0], [0.0, 1.0, 0.0])
    tau41_b = np.cross([0.0, 1.0, 0.0], [0.0, 1.0, 0.0])
    tau41_c = np.cross([0.0, 0.0, -1.0], [0.0, 1.0, 0.0])
    tau41_d = np.cross([0.0, -1.0, 0.0], [0.0, 1.0, 0.0])
    np.testing.assert_allclose(tau41_a, [-1.0, 0.0, 0.0])
    np.testing.assert_allclose(tau41_b, [0.0, 0.0, 0.0])
    np.testing.assert_allclose(tau41_c, [1.0, 0.0, 0.0])
    np.testing.assert_allclose(tau41_d, [0.0, 0.0, 0.0])

    delta_u42 = -2 * 1.45 * 0.835
    close(delta_u42, -2.42)

    # 27.43–27.46: DC motors and the Hall effect.
    if43 = 120.0 / 106.0
    ir43 = 4.82 - if43
    emf43 = 120.0 - ir43 * 5.9
    p_mech43 = emf43 * ir43
    close(if43, 1.13)
    close(ir43, 3.69)
    close(emf43, 98.2)
    close(p_mech43, 362.0)

    i44 = (120.0 - 105.0) / 3.2
    p_in44 = 120.0 * i44
    p_mech44 = 105.0 * i44
    close(i44, 4.69)
    close(p_in44, 563.0)
    close(p_mech44, 492.0)

    density45 = 5.85e28
    z_width45, y_thickness45 = 11.8e-3, 0.23e-3
    vd45 = 120.0 / (density45 * E * z_width45 * y_thickness45)
    ehall45 = vd45 * 0.95
    vhall45 = ehall45 * z_width45
    close(vd45, 4.73e-3)
    close(ehall45, 4.50e-3)
    close(vhall45, 5.31e-5)
    # Electron drift is −x, B is +y, so magnetic force on electrons is +z.
    np.testing.assert_allclose(-E * np.cross([-vd45, 0.0, 0.0], [0.0, 0.95, 0.0]),
                               [0.0, 0.0, E * vd45 * 0.95], rtol=1e-14)

    density46 = 78.0 * 2.29 / (E * y_thickness45 * 131e-6)
    close(density46, 3.70e28)
    drift46 = 131e-6 / (2.29 * z_width45)
    close(density46 * E * drift46 * z_width45 * y_thickness45, 78.0, rtol=1e-12)

    # 27.47–27.54: Coupled fields, isotope data, and mass spectrometry.
    q47, m47, b47, e47, t47 = 3.75e-4, 5.00e-5, 4.00, 60.0, 0.0200
    omega47 = q47 * b47 / m47
    x47 = 30.0 / omega47 * math.sin(omega47 * t47)
    y47 = 1.00 + 30.0 / omega47 * (math.cos(omega47 * t47) - 1)
    z47 = 0.5 * q47 * e47 / m47 * t47**2
    vz47 = q47 * e47 / m47 * t47
    speed47 = math.sqrt(30.0**2 + vz47**2)
    close(x47, 0.565)
    close(y47, 0.825)
    close(z47, 0.0900)
    close(speed47, 31.3)

    force48 = 7.26e-8 * np.cross([-1.68e4, -3.11e4, 5.85e4], [0.650, 0.0, 0.0])
    np.testing.assert_allclose(force48, [0.0, 2.76e-3, 1.47e-3], rtol=4e-3)

    k_coulomb, r49, q49, m49 = 8.99e9, 1.0e-15, E, 3.34e-27
    v49 = math.sqrt(k_coulomb * q49**2 / (r49 * m49))
    b49 = m49 * v49 / (q49 * 1.25)
    close(v49, 8.30e6)
    close(b49, 0.139)

    r50, v50 = 5.3e-11, 2.2e6
    period50 = 2 * math.pi * r50 / v50
    current50 = E / period50
    moment50 = current50 * math.pi * r50**2
    close(period50, 1.51e-16)
    close(current50, 1.06e-3)
    close(moment50, 9.33e-24)

    q_over_m51 = 2 / (1.04e-6 * 0.200**2)
    close(q_over_m51, 4.81e7)

    q52, mp52, r52, b52 = 1.60e-19, 1.67e-27, 0.400, 0.85
    vmax52 = q52 * b52 * r52 / mp52
    kmax52 = 0.5 * mp52 * vmax52**2
    period52 = 2 * math.pi * mp52 / (q52 * b52)
    bdouble52 = b52 * math.sqrt(2)
    alpha_energy52 = 0.5 * 6.64e-27 * (3.20e-19 * b52 * r52 / 6.64e-27) ** 2
    close(kmax52 / E, 5.54e6)
    close(kmax52, 8.86e-13)
    close(period52, 7.70e-8)
    close(bdouble52, 1.20)
    close(alpha_energy52 / E, 5.57e6)

    v53 = 1.88e4 / 0.682
    radii53 = [A * 1.66e-27 * v53 / (E * 0.682) for A in (82, 84, 86)]
    separation53 = [2 * (radii53[i + 1] - radii53[i]) for i in (0, 1)]
    close(v53, 2.76e4)
    close(separation53[0], 1.68e-3)
    close(separation53[1], 1.68e-3)

    m12c54, radius54, field54 = 12 * 1.66e-27, 0.500, 0.150
    voltage54 = E * field54**2 * radius54**2 / (2 * m12c54)
    radius14c54 = radius54 * 14 / 12
    separation54 = 2 * (radius14c54 - radius54)
    close(voltage54, 2.26e4)
    close(separation54, 0.1667)

    # 27.55: The magnetic-force component along the incline balances gravity.
    angle55 = math.radians(30.0)
    mass55, length55, field55 = 1.20, 0.400, 0.80
    current55 = mass55 * G * math.tan(angle55) / (length55 * field55)
    force_along55 = current55 * length55 * field55 * math.cos(angle55)
    gravity_along55 = mass55 * G * math.sin(angle55)
    close(force_along55, gravity_along55, rtol=1e-14)

    current_total56 = 120.0 / (25.0 + 1.0 / (1.0 / 10.0 + 1.0 / 10.0))
    current56 = current_total56 / 2.0
    force56 = current56 * 0.850 * 1.60
    mass56 = 2.60 / G
    acceleration56 = (force56 - 2.60) / mass56
    close(current_total56, 4.00)
    close(current56, 2.00)
    close(force56, 2.72)
    close(acceleration56, .4523)

    b57 = 1.99e-26 * 8.50e3 / (E * 0.125)
    radius13_57 = 0.125 * 2.16e-26 / 1.99e-26
    separation57 = 2 * (radius13_57 - 0.125)
    close(b57, 8.44e-3)
    close(separation57, 2.14e-2)

    # A rotating positive charge is a current loop: μ = qωR²/2.
    q58, omega58, radius58 = E, 6.0, 0.025
    current58 = q58 * omega58 / (2 * math.pi)
    moment58 = current58 * math.pi * radius58**2
    close(moment58, q58 * omega58 * radius58**2 / 2, rtol=1e-14)

    force59 = 2.0e3 * 0.500 * 0.80
    distance59 = 25.0 * (11.2e3) ** 2 / (2 * force59)
    close(force59, 800.0)
    close(distance59, 1.96e6)

    force60 = 7.40 * 0.250 * np.cross([0.0, 0.0, 1.0], [-0.242, -0.985, -0.336])
    np.testing.assert_allclose(force60, [1.82, -0.448, 0.0], rtol=3e-3)
    close(float(np.linalg.norm(force60)), 1.88)

    print("Chapter 27 Exercises 27.31–27.60: numerical/vector checks passed.")


if __name__ == "__main__":
    main()
