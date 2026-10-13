"""Independent selected physics checks for Chapter 27 Problems 27.61–27.85.

The checks are derived from the exercise statements and source figures. They do not
import or reuse the existing chapter verifier.
"""
from pathlib import Path
import math
import re

import numpy as np

ROOT = Path(__file__).resolve().parent
E_CHARGE = 1.60e-19
M_E = 9.11e-31
M_P = 1.67e-27
G = 9.80


def close(value, expected, rtol=5e-3):
    np.testing.assert_allclose(value, expected, rtol=rtol, atol=1e-12)


def verify_prompt_coverage():
    p15 = (ROOT / "translations/chapter-27/15-bai-tong-hop-61-80.md").read_text(encoding="utf-8-sig")
    p16 = (ROOT / "translations/chapter-27/16-bai-nang-cao-mcat.md").read_text(encoding="utf-8-sig")
    ids15 = [int(x) for x in re.findall(r"::: exercise (?:Bài )?27\.(\d+)", p15)]
    ids16 = [int(x) for x in re.findall(r"::: exercise (?:Bài )?27\.(\d+)", p16)]
    assert ids15 == list(range(61, 81)), ids15
    assert ids16 == list(range(81, 86)), ids16


def verify_61_to_70():
    # 27.61: Uniform-field force on a curved wire depends on endpoint displacement.
    current, radius, field = 5.00, .200, .800
    displacement = np.array([radius, -radius, 0.0])
    force_z = current * np.cross(displacement, [0.0, 0.0, field])
    force_x = current * np.cross(displacement, [field, 0.0, 0.0])
    np.testing.assert_allclose(force_z, [-.800, -.800, 0.0], rtol=1e-12)
    np.testing.assert_allclose(force_x, [0.0, 0.0, .800], rtol=1e-12)

    # 27.63: Earth-field lift estimate and added mass with a 1 T magnet.
    diameter, density, g = .0050, 8900.0, G
    area = math.pi * (diameter / 2) ** 2
    b_horizontal = .50e-4 * math.cos(math.radians(45))
    current63 = density * area * g / b_horizontal
    b_min63 = density * area * g / 900.0
    extra_mass63 = (10.0 * .100 * 1.0 - density * area * .100 * g) / g
    close(current63, 4.84e4, rtol=.02)
    close(b_min63, 1.90e-3, rtol=.02)
    close(extra_mass63, .0846, rtol=.02)

    # 27.64: Loop normal from the actual current arrow in Fig. P27.64.
    mu64 = 15.0 * .0800 * .0600
    normal64 = np.array([math.sin(math.radians(30)), 0.0, -math.cos(math.radians(30))])
    torque64_x = mu64 * np.cross(normal64, [1.0, 0.0, 0.0]) * .48
    torque64_minus_z = mu64 * np.cross(normal64, [0.0, 0.0, -1.0]) * .48
    np.testing.assert_allclose(torque64_x, [0.0, -.0299, 0.0], rtol=.01)
    np.testing.assert_allclose(torque64_minus_z, [0.0, .0173, 0.0], rtol=.01)

    # 27.65: Separate gravity and magnetic hinge torques before solving B.
    mass65 = (.15e-3 / .0100) * 2 * (.060 + .080)
    mu65 = 8.2 * .060 * .080
    tau_g65 = mass65 * g * (.080 / 2) * math.sin(math.radians(30))
    b65 = tau_g65 / (mu65 * math.cos(math.radians(30)))
    close(mass65, 4.20e-3)
    close(b65, .0241)

    # 27.66: Distributed force gives the same torque as force at the midpoint.
    length66, current66, field66 = 1.0, 1.0, 1.0
    tau_integral66 = current66 * field66 * length66**2 / 2
    tau_midpoint66 = (current66 * field66 * length66) * length66 / 2
    close(tau_integral66, tau_midpoint66, rtol=1e-14)

    # 27.67–68: Actual vertices and current directions in Fig. P27.67.
    p, q, r = np.array([0.0, 0.0, 0.0]), np.array([0.0, .600, 0.0]), np.array([.800, 0.0, 0.0])
    edges = [q-p, r-q, p-r]
    current67 = 5.00
    forces67 = [current67 * np.cross(edge, [0.0, 3.00, 0.0]) for edge in edges]
    np.testing.assert_allclose(forces67, [[0, 0, 0], [0, 0, 12], [0, 0, -12]], atol=1e-12)
    torque_x67 = .300 * 12.0
    close(torque_x67, 3.60)
    forces68 = [current67 * np.cross(edge, [0.0, 0.0, -3.00]) for edge in edges]
    np.testing.assert_allclose(np.sum(forces68, axis=0), [0, 0, 0], atol=1e-12)
    # B is parallel to mu in problem 27.68, so net torque is zero.
    np.testing.assert_allclose(np.cross([0, 0, -1], [0, 0, -3]), [0, 0, 0])

    # 27.69: Radial field component adds along the coil axis; normal component cancels.
    force69 = 50 * .950 * .220 * math.sin(math.radians(60)) * math.pi * .0156
    close(force69, .444)

    # 27.70: Magnetic torque balances gravity about the pivot.
    current70 = (.0120 * g * math.cos(math.radians(30))) / (.150 * .300)
    close(current70, 2.26)


def verify_71_to_85():
    # 27.71: On the xy loop, z=0. The source field then has By=0 and Bz=B0*y/L.
    # Clockwise currents: left +y, right −y, top +x, bottom −x.
    left71 = np.array([.5, 0.0, 0.0])
    right71 = np.array([-.5, 0.0, 0.0])
    top71 = np.array([0.0, -1.0, 0.0])
    bottom71 = np.zeros(3)
    total71 = left71 + right71 + top71 + bottom71
    np.testing.assert_allclose(left71, [.5, 0, 0], atol=1e-14)
    np.testing.assert_allclose(right71, [-.5, 0, 0], atol=1e-14)
    np.testing.assert_allclose(top71, [0, -1, 0], atol=1e-14)
    np.testing.assert_allclose(total71, [0, -1, 0], atol=1e-14)

    # 27.72: Signed moments from the hinge and source figure.
    m72, length72, angle72, current72, field72 = .0840, .180, math.radians(53), 12.0, .120
    tau_g72 = m72 * G * length72 / 2 * math.cos(angle72)
    tau_b72 = current72 * field72 * length72**2 / 2
    tension72 = (tau_g72 + tau_b72) / (length72 * math.sin(angle72))
    close(tau_g72, .0445)
    close(tau_b72, .0233)
    close(tension72, .472)

    # 27.73: Check piecewise torque/energy formulas against each other and endpoints.
    # Source definitions: mu=2NIWR, s=mu B/(MgR), h_top=R(1+pi/2).
    s, radius73 = 1.30, .20
    htop73 = radius73 * (1 + math.pi / 2)
    theta73 = .40
    h73 = radius73 * (1 + theta73)
    tau2 = lambda th: s * math.cos(th) - 1
    u2 = lambda th: 1 + th - s * (math.sin(th) + 1)
    close(htop73, radius73 * (1 + math.pi / 2), rtol=1e-14)
    # dU/dtheta = -tau_net/(MgR) in the post-contact branch.
    numeric_derivative = (u2(theta73 + 1e-6) - u2(theta73 - 1e-6)) / 2e-6
    close(numeric_derivative, -tau2(theta73), rtol=1e-7)
    u1_at_r = 1 - s
    u2_at_r = u2(0)
    close(u1_at_r, u2_at_r, rtol=1e-14)

    # 27.74: Signed omega changes rotation sense; vertical maximum is sign-invariant.
    omega74 = 19.6e-6 * 10.0 / 1.00e-6
    ymax74 = 2 * G / omega74**2
    close(omega74, 196.0)
    close(ymax74, .510e-3)

    # 27.75: Clockwise loop viewed from +z gives mu=-IA k; solve all components.
    # Given torque D(4 i - 3 j), |B|=13D/(IA), U<0 selects Bz<0.
    vector75 = np.array([3.0, 4.0, -12.0])
    np.testing.assert_allclose(np.linalg.norm(vector75), 13.0, atol=1e-14)
    tau75 = np.cross([0.0, 0.0, -1.0], vector75)
    np.testing.assert_allclose(tau75, [4.0, -3.0, 0.0], atol=1e-14)

    # 27.76: Fit the converted SI data; source graph is R² versus V.
    v76 = np.array([10, 12, 14, 16, 18], dtype=float) * 1e3
    r76 = np.array([19.9, 21.8, 23.6, 25.2, 26.8], dtype=float) * 1e-2
    slope76, intercept76 = np.polyfit(v76, r76**2, 1)
    ratio76 = 2 / (.250**2 * slope76)
    speed76 = math.sqrt(2 * ratio76 * 20e3)
    close(slope76, 4.02e-6, rtol=.01)
    close(ratio76, 7.96e6, rtol=.01)
    close(speed76, 5.64e5, rtol=.01)
    close(.212 / math.sqrt(2), .150, rtol=.01)

    # 27.77: The graph ordinate is in units of 10^8; at 400 V it is 800.
    slope77 = 800 * 1e8 / 400.0
    mass77 = 2 * E_CHARGE * .340**2 / slope77
    plate_v77 = 2.00e5 * .00600
    speed77 = math.sqrt(2 * E_CHARGE * 400 / mass77)
    close(slope77, 2.0e8, rtol=1e-14)
    close(mass77, 1.85e-28, rtol=.01)
    close(plate_v77, 1.20e3, rtol=1e-14)
    close(speed77, 8.32e5, rtol=.01)

    # 27.78: Alpha cyclotron data and the three species frequencies.
    slope78 = 7.67e6
    q_over_m78 = 2 * math.pi * slope78
    m_alpha78 = 2 * E_CHARGE / q_over_m78
    fp78 = E_CHARGE * .300 / (2 * math.pi * M_P)
    fe78 = E_CHARGE * .300 / (2 * math.pi * M_E)
    fa78 = slope78 * .300
    speed_alpha78 = q_over_m78 * .300 * .120
    ke_alpha78 = .5 * m_alpha78 * speed_alpha78**2
    close(m_alpha78, 6.65e-27, rtol=.01)
    close(fp78, 4.57e6, rtol=.01)
    close(fe78, 8.41e9, rtol=.01)
    close(fa78, 2.30e6, rtol=.01)
    close(speed_alpha78, 1.73e6, rtol=.01)
    close(ke_alpha78, 1.00e-14, rtol=.02)

    # 27.79: Uniformly charged spherical shell has mu=Q omega R²/3 along +z.
    # Source field includes both x and y components.
    alpha79 = .70
    b79 = np.array([math.sin(alpha79), math.cos(alpha79), 0.0])
    tau79 = np.cross([0.0, 0.0, 1.0], b79)
    np.testing.assert_allclose(tau79, [-math.cos(alpha79), math.sin(alpha79), 0.0], atol=1e-14)

    # 27.80: Use an equatorial-plane / radial / east triad at latitude 80° N.
    # v points toward the axis in the equatorial plane; B points toward Earth's center.
    lat80 = math.radians(80.0)
    rhat80 = np.array([math.cos(lat80), 0.0, math.sin(lat80)])
    b_hat80 = -rhat80
    v_hat80 = np.array([-1.0, 0.0, 0.0])
    np.testing.assert_allclose(np.dot(v_hat80, b_hat80), math.cos(lat80), atol=1e-14)
    speed80_initial = 4.00e5
    v_parallel80 = speed80_initial * math.cos(lat80)
    v_perp80 = speed80_initial * math.sin(lat80)
    radius80 = M_E * v_perp80 / (E_CHARGE * 15.0e-6)
    freq80 = E_CHARGE * 15.0e-6 / (2 * math.pi * M_E)
    energy_gain80 = E_CHARGE * .0200 * 100e3
    initial_ke80 = .5 * M_E * (4.00e5)**2
    speed80 = math.sqrt((speed80_initial)**2 + 2 * energy_gain80 / M_E)
    close(v_parallel80, 6.946e4, rtol=.01)
    close(v_perp80, 3.939e5, rtol=.01)
    close(radius80, .1495, rtol=.01)
    close(freq80, 4.20e5, rtol=.01)
    close(speed80, 2.65e7, rtol=.01)
    close((initial_ke80 + energy_gain80) / initial_ke80, 4.39e3, rtol=.01)
    # For q < 0 the gyration angular-velocity vector points along B.
    # Since B points away from a space observer looking toward Earth, that is clockwise.
    gyro_omega_hat80 = -np.sign(-1.0) * b_hat80
    np.testing.assert_allclose(gyro_omega_hat80, b_hat80, atol=1e-14)
    assert np.dot(gyro_omega_hat80, b_hat80) > 0

    # 27.81: Small deflection through the magnet and tangent drift to the wall.
    q81, m81, v81, b81 = 2.15e-6, 3.20e-11, 1.45e5, .420
    r81 = m81 * v81 / (q81 * b81)
    phi81 = math.asin(.250 / r81)
    t81 = r81 * phi81 / v81
    dx1_81 = r81 * (1 - math.cos(phi81))
    dx_81 = dx1_81 + (.750 - .250) * math.tan(phi81)
    close(r81, 5.14, rtol=.01)
    close(t81, 1.72e-6, rtol=.01)
    close(dx1_81, 6.08e-3, rtol=.01)
    close(dx_81, 3.05e-2, rtol=.01)

    # 27.82: Energy at a cycloid crest and Newton's normal-force relation.
    q82, mass82, electric82, magnetic82 = 1.0, 2.0, 3.0, 4.0
    height82 = 2 * mass82 * electric82 / (q82 * magnetic82**2)
    speed82 = math.sqrt(2 * q82 * electric82 * height82 / mass82)
    radius82 = 2 * height82
    centripetal82 = mass82 * speed82**2 / radius82
    magnetic82_force = q82 * (2 * electric82 / magnetic82) * magnetic82
    electric82_force = q82 * electric82
    close(centripetal82, electric82_force, rtol=1e-14)
    close(magnetic82_force - electric82_force, centripetal82, rtol=1e-14)
    close(speed82, 2 * electric82 / magnetic82, rtol=1e-14)

    # 27.83–85: MRI spin torque, isotope criterion, and nerve-current force.
    torque83 = 1.4e-26 * 2.0
    assert torque83 == 2.8e-26
    assert (15 % 2, 16 % 2) == (1, 0)  # 31P has an unpaired proton.
    area85 = math.pi * (.0015 / 2) ** 2
    resistance85 = .6 * .001 / area85
    current85 = .100 / resistance85
    force85 = current85 * .001 * 2.0
    close(resistance85, 340.0, rtol=.01)
    close(force85, 5.9e-7, rtol=.02)


def main():
    verify_prompt_coverage()
    verify_61_to_70()
    verify_71_to_85()
    print("Selected independent checks for Problems 27.61–27.85 passed.")


if __name__ == "__main__":
    main()
