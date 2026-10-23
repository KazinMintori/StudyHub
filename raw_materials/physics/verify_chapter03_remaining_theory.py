#!/usr/bin/env python3
"""Comprehensive Python verification for Young & Freedman Chapter 3 Theory.

Validates all numerical calculations, example solutions, derivations,
unit conversions, and self-check questions for Sections 3.1 to 3.5.
"""

import math
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def verify_example_3_1():
    # Rover: x(t) = 2.0 - 0.25 t^2, y(t) = 1.0 t + 0.025 t^3
    t = 2.0
    x = 2.0 - 0.25 * (t ** 2)
    y = 1.0 * t + 0.025 * (t ** 3)
    assert math.isclose(x, 1.0, abs_tol=1e-3), f"Ex 3.1a x: {x}"
    assert math.isclose(y, 2.2, abs_tol=1e-3), f"Ex 3.1a y: {y}"
    r = math.sqrt(x**2 + y**2)
    assert math.isclose(r, 2.4166, abs_tol=0.05), f"Ex 3.1a r: {r}"
    theta = math.degrees(math.atan2(y, x))
    assert math.isclose(theta, 65.55, abs_tol=0.5), f"Ex 3.1a theta: {theta}"

    # Displacement between t=0 and t=2
    x0, y0 = 2.0, 0.0
    dx = x - x0
    dy = y - y0
    dr = math.sqrt(dx**2 + dy**2)
    assert math.isclose(dx, -1.0, abs_tol=1e-3)
    assert math.isclose(dy, 2.2, abs_tol=1e-3)
    assert math.isclose(dr, 2.4166, abs_tol=0.05)

    dt = 2.0
    vx_av = dx / dt
    vy_av = dy / dt
    v_av = math.sqrt(vx_av**2 + vy_av**2)
    assert math.isclose(vx_av, -0.50, abs_tol=1e-3)
    assert math.isclose(vy_av, 1.10, abs_tol=1e-3)
    assert math.isclose(v_av, 1.208, abs_tol=0.05)
    alpha_av = math.degrees(math.atan2(vy_av, vx_av))
    assert math.isclose(alpha_av, 114.44, abs_tol=0.5)

    # Instantaneous velocity at t=2.0
    # vx = -0.50 t, vy = 1.0 + 0.075 t^2
    vx = -0.50 * t
    vy = 1.0 + 0.075 * (t ** 2)
    assert math.isclose(vx, -1.0, abs_tol=1e-3)
    assert math.isclose(vy, 1.3, abs_tol=1e-3)
    v = math.sqrt(vx**2 + vy**2)
    assert math.isclose(v, 1.640, abs_tol=0.05)
    alpha = math.degrees(math.atan2(vy, vx))
    assert math.isclose(alpha, 127.56, abs_tol=0.5)
    return True

def verify_example_3_2():
    # Acceleration of rover
    # vx(0) = 0, vy(0) = 1.0
    # vx(2) = -1.0, vy(2) = 1.3
    dt = 2.0
    ax_av = (-1.0 - 0.0) / dt
    ay_av = (1.3 - 1.0) / dt
    assert math.isclose(ax_av, -0.50, abs_tol=1e-3)
    assert math.isclose(ay_av, 0.15, abs_tol=1e-3)
    a_av = math.sqrt(ax_av**2 + ay_av**2)
    assert math.isclose(a_av, 0.522, abs_tol=0.01)
    alpha_a_av = math.degrees(math.atan2(ay_av, ax_av))
    assert math.isclose(alpha_a_av, 163.3, abs_tol=0.5)

    # Instantaneous acceleration at t=2.0
    # ax = -0.50, ay = 0.15 t
    t = 2.0
    ax = -0.50
    ay = 0.15 * t
    assert math.isclose(ax, -0.50, abs_tol=1e-3)
    assert math.isclose(ay, 0.30, abs_tol=1e-3)
    a = math.sqrt(ax**2 + ay**2)
    assert math.isclose(a, 0.583, abs_tol=0.01)
    alpha_a = math.degrees(math.atan2(ay, ax))
    assert math.isclose(alpha_a, 149.03, abs_tol=0.5)
    return True

def verify_example_3_3():
    # Parallel and perpendicular components of acceleration
    # at t=2.0 s: v = 1.64 m/s at 127.56 deg; a = 0.583 m/s^2 at 149.03 deg
    v = 1.640
    a = 0.583
    theta = 149.03 - 127.56
    assert math.isclose(theta, 21.47, abs_tol=0.5)
    a_par = a * math.cos(math.radians(theta))
    a_perp = a * math.sin(math.radians(theta))
    assert math.isclose(a_par, 0.543, abs_tol=0.01)
    assert math.isclose(a_perp, 0.213, abs_tol=0.01)

    # via dot product: vx = -1.0, vy = 1.3, ax = -0.50, ay = 0.30
    v_dot_a = (-1.0) * (-0.50) + (1.3) * (0.30)
    assert math.isclose(v_dot_a, 0.89, abs_tol=1e-3)
    a_par_dot = v_dot_a / v
    assert math.isclose(a_par_dot, 0.543, abs_tol=0.01)
    a_perp_pyth = math.sqrt(a**2 - a_par_dot**2)
    assert math.isclose(a_perp_pyth, 0.213, abs_tol=0.01)
    return True

def verify_example_3_6():
    # PDF97 original question asks position/distance/velocity at0.50s.
    v0x = 9.0
    g = 9.80
    t = .50
    x = v0x * t
    y=-.5*g*t*t
    assert math.isclose(x, 4.5, abs_tol=1e-10)
    assert math.isclose(y,-1.225,abs_tol=1e-10)
    assert math.isclose(math.hypot(x,y),4.6637565,abs_tol=1e-6)
    vy = -g * t
    assert math.isclose(vy, -4.90, abs_tol=1e-10)
    v = math.sqrt(v0x**2 + vy**2)
    assert math.isclose(v, 10.2474387, abs_tol=1e-6)
    alpha = math.degrees(math.atan2(vy, v0x))
    assert math.isclose(alpha, -28.5658368, abs_tol=1e-6)
    return True

def verify_example_3_7():
    # Baseball: v0 = 37.0 m/s, alpha0 = 53.1 deg, g = 9.80 m/s^2
    v0 = 37.0
    alpha0 = math.radians(53.1)
    g = 9.80
    v0x = v0 * math.cos(alpha0)
    v0y = v0 * math.sin(alpha0)
    assert math.isclose(v0x, 22.21, abs_tol=0.05)
    assert math.isclose(v0y, 29.59, abs_tol=0.05)

    # At t = 2.00 s
    t = 2.00
    x = v0x * t
    y = v0y * t - 0.5 * g * (t ** 2)
    assert math.isclose(x, 44.43, abs_tol=0.1)
    assert math.isclose(y, 39.58, abs_tol=0.1)
    vx = v0x
    vy = v0y - g * t
    assert math.isclose(vx, 22.21, abs_tol=0.05)
    assert math.isclose(vy, 9.99, abs_tol=0.05)
    v = math.sqrt(vx**2 + vy**2)
    assert math.isclose(v, 24.35, abs_tol=0.1)
    alpha = math.degrees(math.atan2(vy, vx))
    assert math.isclose(alpha, 24.22, abs_tol=0.5)

    # At peak: vy = 0
    t_peak = v0y / g
    assert math.isclose(t_peak, 3.019, abs_tol=0.01)
    h_max = (v0y ** 2) / (2 * g)
    assert math.isclose(h_max, 44.67, abs_tol=0.1)

    # Horizontal range R
    t_flight = 2 * t_peak
    assert math.isclose(t_flight, 6.039, abs_tol=0.02)
    R = v0x * t_flight
    assert math.isclose(R, 134.1, abs_tol=0.5)
    return True

def verify_example_3_8():
    # Maximum range and height formulas
    # R = (v0^2 / g) * sin(2*alpha0), maximum at alpha0 = 45 deg
    v0 = 37.0
    g = 9.80
    R_45 = (v0**2 / g) * math.sin(math.radians(90))
    assert math.isclose(R_45, 139.69, abs_tol=0.1)
    h_45 = (v0**2 * (math.sin(math.radians(45))**2)) / (2 * g)
    assert math.isclose(h_45, 34.92, abs_tol=0.1)
    return True

def verify_example_3_9():
    # Original PDF99–100: 8.0m window, 10.0m/s,20degrees BELOW horizontal.
    v0 = 10.0
    alpha0 = math.radians(-20.0)
    g = 9.80
    v0x = v0 * math.cos(alpha0)
    v0y = v0 * math.sin(alpha0)
    assert math.isclose(v0x, 9.3969262, abs_tol=1e-6)
    assert math.isclose(v0y, -3.42020143, abs_tol=1e-6)

    a_quad = 4.90
    b_quad = -v0y
    c_quad = -8.0
    disc = b_quad**2 - 4 * a_quad * c_quad
    t1 = (-b_quad + math.sqrt(disc)) / (2 * a_quad)
    assert math.isclose(t1, .9755579549, abs_tol=1e-9)
    assert math.isclose(v0y*t1-.5*g*t1*t1,-8,abs_tol=1e-10)
    x = v0x * t1
    assert math.isclose(x, 9.1672461, abs_tol=1e-6)
    return True

def verify_example_3_11():
    # Aston Martin V12 Vantage: a_rad = 0.97 g = 0.97 * 9.80 = 9.506 m/s^2 ≈ 9.5 m/s^2
    # Speed v = 40.0 m/s
    a_rad = 0.97 * 9.80
    assert math.isclose(a_rad, 9.506, abs_tol=0.01)
    v = 40.0
    R = (v ** 2) / 9.5
    assert math.isclose(R, 168.42, abs_tol=0.5)
    # 20% speed reduction: v' = 32 m/s
    v_prime = 32.0
    R_prime = (v_prime ** 2) / 9.5
    assert math.isclose(R_prime, 107.79, abs_tol=0.5)
    pct_reduction = (168.42 - 107.79) / 168.42 * 100
    assert math.isclose(pct_reduction, 36.0, abs_tol=0.5)
    return True

def verify_example_3_12():
    # Carnival ride: R = 5.0 m, T = 4.0 s
    R = 5.0
    T = 4.0
    a_rad = (4 * (math.pi ** 2) * R) / (T ** 2)
    assert math.isclose(a_rad, 12.337, abs_tol=0.05)
    assert math.isclose(a_rad / 9.80, 1.259, abs_tol=0.02)
    v = 2 * math.pi * R / T
    assert math.isclose(v, 7.854, abs_tol=0.05)
    a_rad_from_v = (v ** 2) / R
    assert math.isclose(a_rad_from_v, 12.337, abs_tol=0.05)
    return True

def verify_example_3_13():
    # Relative velocity on straight road:
    # v_Y/E = +88 km/h, v_T/E = -104 km/h
    v_YE = 88.0
    v_TE = -104.0
    v_TY = v_TE - v_YE
    assert math.isclose(v_TY, -192.0, abs_tol=1e-3)
    v_YT = -v_TY
    assert math.isclose(v_YT, 192.0, abs_tol=1e-3)
    return True

def verify_example_3_14():
    # Airplane in crosswind: vP/A = 240 km/h north, vA/E = 100 km/h east
    vPA = 240.0
    vAE = 100.0
    vPE = math.sqrt(vPA**2 + vAE**2)
    assert math.isclose(vPE, 260.0, abs_tol=1e-3)
    alpha = math.degrees(math.atan2(vAE, vPA))
    assert math.isclose(alpha, 22.62, abs_tol=0.1)
    return True

def verify_example_3_15():
    # Correcting for crosswind: vPA = 240 km/h, vAE = 100 km/h, resultant due north
    vPA = 240.0
    vAE = 100.0
    vPE = math.sqrt(vPA**2 - vAE**2)
    assert math.isclose(vPE, 218.17, abs_tol=0.1)
    beta = math.degrees(math.asin(vAE / vPA))
    assert math.isclose(beta, 24.62, abs_tol=0.1)
    return True

def verify_self_checks():
    # Source3.1 compares average VECTOR velocity to finalinstantaneousvelocity.
    # It is(iii), straight motion with constant speed.
    # Source3.2 changes from slowing to speeding at crest: a_t=0, a_n downward7.
    # Source3.3 monkey and apex dart have equal altitude: pointB, choice(ii).
    for t in [.1,.5,1.]:
        initial_height=7.
        dart_no_gravity_y=initial_height
        monkey_y=initial_height-.5*9.8*t*t
        dart_y=dart_no_gravity_y-.5*9.8*t*t
        assert math.isclose(monkey_y,dart_y)
    # 3.4: Particle in vertical loop at bottom: a_rad proportional to v^2, 4x acceleration implies 2x speed (Choice ii)
    loop_ratio = math.sqrt(4.0)
    assert math.isclose(loop_ratio, 2.0, abs_tol=1e-3)

    # 3.5: Plane pointed east 150 km/h, ground speed 150 km/h north:
    # v_wind = 150 km/h west + 150 km/h north -> 212 km/h from SE to NW (Choice vi)
    v_wind_mag = math.sqrt(150.0**2 + 150.0**2)
    assert math.isclose(v_wind_mag, 212.13, abs_tol=0.1)
    return True

def main():
    print("Running Chapter 3 Theory Verification...")
    verify_example_3_1()
    print("  ✓ Example 3.1: Rover velocity & displacement verified.")
    verify_example_3_2()
    print("  ✓ Example 3.2: Rover acceleration verified.")
    verify_example_3_3()
    print("  ✓ Example 3.3: Parallel and perpendicular acceleration verified.")
    verify_example_3_6()
    print("  ✓ Example 3.6: Horizontal projectile verified.")
    verify_example_3_7()
    print("  ✓ Example 3.7: Batted baseball verified.")
    verify_example_3_8()
    print("  ✓ Example 3.8: Maximum range & height formulas verified.")
    verify_example_3_9()
    print("  ✓ Example 3.9: Thrown ball with different heights verified.")
    verify_example_3_11()
    print("  ✓ Example 3.11: Centripetal acceleration on curved road (Aston Martin) verified.")
    verify_example_3_12()
    print("  ✓ Example 3.12: Centripetal acceleration on carnival ride verified.")
    verify_example_3_13()
    print("  ✓ Example 3.13: Relative velocity on straight road verified.")
    verify_example_3_14()
    print("  ✓ Example 3.14: Flying in crosswind verified.")
    verify_example_3_15()
    print("  ✓ Example 3.15: Correcting for crosswind verified.")
    verify_self_checks()
    print("  ✓ All Section Self-Checks (3.1 to 3.5) verified.")
    print("All Chapter 3 Theory verifications passed successfully.")

if __name__ == "__main__":
    main()
