"""Verification script for Physics 1 Chapter 8 Remaining Theory.

Recalculates all numerical examples, conversions, given-data substitutions,
self-checks, and key kinematic/dynamic relations from original inputs with
explicit assert statements.
"""
import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

def verify_all():
    print("Starting numerical verification of Chapter 8 Theory...")

    # 1. Chapter Opener: Hailstones
    m1_hail = 0.20  # kg
    v1_hail = 15.0  # m/s
    p1_hail = m1_hail * v1_hail
    K1_hail = 0.5 * m1_hail * v1_hail**2

    m2_hail = 0.10  # kg
    v2_hail = 30.0  # m/s
    p2_hail = m2_hail * v2_hail
    K2_hail = 0.5 * m2_hail * v2_hail**2

    assert math.isclose(p1_hail, 3.0, rel_tol=1e-5), f"Opener p1 failed: {p1_hail}"
    assert math.isclose(p2_hail, 3.0, rel_tol=1e-5), f"Opener p2 failed: {p2_hail}"
    assert math.isclose(K1_hail, 22.5, rel_tol=1e-5), f"Opener K1 failed: {K1_hail}"
    assert math.isclose(K2_hail, 45.0, rel_tol=1e-5), f"Opener K2 failed: {K2_hail}"
    assert math.isclose(K2_hail / K1_hail, 2.0, rel_tol=1e-5), "Opener K ratio failed"
    print("  ✓ Chapter Opener Hailstones passed")

    # Original conceptual Example8.1: Two iceboats, m and2m, sameF ands.
    # Independent sample parameters test the symbolic ratios, not new source data.
    for m,F,s in [(2.3,4.7,8.1),(13.0,25.0,60.0)]:
        t1=math.sqrt(2*s*m/F)
        t2=math.sqrt(2*s*2*m/F)
        p1,p2=F*t1,F*t2
        assert math.isclose(t2/t1,math.sqrt(2),rel_tol=1e-12)
        assert math.isclose(p2/p1,math.sqrt(2),rel_tol=1e-12)
        assert math.isclose(p1*p1/(2*m),F*s,rel_tol=1e-12)
        assert math.isclose(p2*p2/(4*m),F*s,rel_tol=1e-12)
    print("  ✓ Example 8.1 passed")

    # 3. Example 8.2: A Ball Hits a Wall
    m_ball = 0.40  # kg
    v1x_ball = -30.0  # m/s
    v2x_ball = 20.0   # m/s
    dt_ball = 0.010   # s
    p1x_ball = m_ball * v1x_ball  # -12.0 kg*m/s
    p2x_ball = m_ball * v2x_ball  # +8.0 kg*m/s
    Jx_ball = p2x_ball - p1x_ball  # 20.0 N*s
    Fav_x_ball = Jx_ball / dt_ball  # 2000.0 N
    assert math.isclose(p1x_ball, -12.0, rel_tol=1e-5)
    assert math.isclose(p2x_ball, 8.0, rel_tol=1e-5)
    assert math.isclose(Jx_ball, 20.0, rel_tol=1e-5)
    assert math.isclose(Fav_x_ball, 2000.0, rel_tol=1e-5)
    print("  ✓ Example 8.2 passed")


    m_soccer = 0.40
    v1_soccer = 20.0
    v1x_soccer = -v1_soccer
    v1y_soccer = 0.0
    v2x_soccer = 30.0*math.cos(math.pi/4)
    v2y_soccer = 30.0*math.sin(math.pi/4)
    p1x_soccer = m_soccer * v1x_soccer
    p1y_soccer = m_soccer * v1y_soccer
    p2x_soccer = m_soccer * v2x_soccer
    p2y_soccer = m_soccer * v2y_soccer
    Jx_soccer = p2x_soccer - p1x_soccer
    Jy_soccer = p2y_soccer - p1y_soccer
    dt_soccer = 0.010
    Fav_x_soccer = Jx_soccer / dt_soccer
    Fav_y_soccer = Jy_soccer / dt_soccer
    Fav_mag = math.sqrt(Fav_x_soccer**2 + Fav_y_soccer**2)
    Fav_ang = math.degrees(math.atan2(Fav_y_soccer, Fav_x_soccer))
    assert math.isclose(Jx_soccer, 16.4852813742, rel_tol=1e-9)
    assert math.isclose(Jy_soccer, 8.4852813742, rel_tol=1e-9)
    assert math.isclose(Fav_mag, 1854.1, rel_tol=1e-3)
    assert math.isclose(Fav_ang, 27.23, rel_tol=1e-3)
    print("  ✓ Example 8.3 passed")

    # 5. Example 8.4: Recoil of a Rifle
    m_rifle = 3.00       # kg
    m_bullet = 0.00500   # kg (5.00 g)
    v_bullet_2x = 300.0  # m/s
    v_rifle_2x = -(m_bullet / m_rifle) * v_bullet_2x  # -0.500 m/s
    K_bullet = 0.5 * m_bullet * (v_bullet_2x**2)      # 225.0 J
    K_rifle = 0.5 * m_rifle * (v_rifle_2x**2)          # 0.375 J
    assert math.isclose(v_rifle_2x, -0.500, rel_tol=1e-5)
    assert math.isclose(K_bullet, 225.0, rel_tol=1e-5)
    assert math.isclose(K_rifle, 0.375, rel_tol=1e-5)
    assert math.isclose(K_bullet / K_rifle, 600.0, rel_tol=1e-5)
    assert math.isclose(m_rifle / m_bullet, 600.0, rel_tol=1e-5)
    print("  ✓ Example 8.4 passed")


    mA_5 = 0.50
    vA1x_5 = 2.0
    mB_5 = 0.30
    vB1x_5 = -2.0
    vB2x_5 = 2.0
    P1x_5 = mA_5 * vA1x_5 + mB_5 * vB1x_5
    vA2x_5 = (P1x_5-mB_5*vB2x_5)/mA_5
    delta_vA_5 = vA2x_5 - vA1x_5
    delta_vB_5 = vB2x_5 - vB1x_5
    assert math.isclose(P1x_5, 0.40, rel_tol=1e-5)
    assert math.isclose(vA2x_5, -0.40, rel_tol=1e-5)
    assert math.isclose(vB2x_5, 2.0, rel_tol=1e-5)
    assert math.isclose(delta_vA_5 / delta_vB_5, -0.60, rel_tol=1e-5)
    print("  ✓ Example 8.5 passed")

    # 7. Example 8.6: Collision in a Horizontal Plane (Robots)
    mA_6 = 20.0   # kg
    vA1x_6 = 2.0  # m/s
    vA1y_6 = 0.0
    mB_6 = 12.0   # kg
    vB1x_6 = 0.0
    vB1y_6 = 0.0
    vA2_6 = 1.0   # m/s
    alpha_6 = math.radians(30.0)
    vA2x_6 = vA2_6 * math.cos(alpha_6)  # 0.8660 m/s
    vA2y_6 = vA2_6 * math.sin(alpha_6)  # 0.5000 m/s
    # Momentum conservation:
    # mA*vA1x = mA*vA2x + mB*vB2x
    vB2x_6 = (mA_6 * vA1x_6 - mA_6 * vA2x_6) / mB_6  # (40.0 - 17.3205) / 12 = 1.890 m/s
    vB2y_6 = (0.0 - mA_6 * vA2y_6) / mB_6            # -10.0 / 12 = -0.8333 m/s
    vB2_mag_6 = math.sqrt(vB2x_6**2 + vB2y_6**2)     # 2.0656 m/s
    beta_6 = math.degrees(math.atan2(abs(vB2y_6), vB2x_6))  # 23.79 deg
    assert math.isclose(vB2x_6, 1.890, rel_tol=1e-3)
    assert math.isclose(vB2y_6, -0.8333, rel_tol=1e-3)
    assert math.isclose(vB2_mag_6, 2.066, rel_tol=1e-3)
    assert math.isclose(beta_6, 23.79, rel_tol=1e-2)
    print("  ✓ Example 8.6 passed")

    # 8. Example 8.7: Completely Inelastic Collision
    v2x_7 = P1x_5 / (mA_5 + mB_5)  # 0.40 / 0.80 = 0.50 m/s
    K1_7 = 0.5 * mA_5 * (vA1x_5**2) + 0.5 * mB_5 * (vB1x_5**2)  # 1.0 + 0.60 = 1.6 J
    K2_7 = 0.5 * (mA_5 + mB_5) * (v2x_7**2)  # 0.5 * 0.80 * 0.25 = 0.10 J
    delta_K_7 = K2_7 - K1_7  # -1.5 J
    assert math.isclose(v2x_7, 0.50, rel_tol=1e-5)
    assert math.isclose(K1_7, 1.60, rel_tol=1e-5)
    assert math.isclose(K2_7, 0.10, rel_tol=1e-5)
    assert math.isclose(delta_K_7, -1.50, rel_tol=1e-5)
    print("  ✓ Example 8.7 passed")

    # 9. Example 8.8: Ballistic Pendulum
    mB_8 = 0.00500  # kg
    mW_8 = 2.00     # kg
    g = 9.80        # m/s^2
    y_8 = 0.0300    # m (3.00 cm)
    V_8 = math.sqrt(2 * g * y_8)  # sqrt(2 * 9.80 * 0.03) = 0.76681 m/s
    v1_8 = ((mB_8 + mW_8) / mB_8) * V_8  # (2.005 / 0.005) * 0.76681 = 307.49 m/s
    K1_8 = 0.5 * mB_8 * (v1_8**2)  # 236.37 J
    K2_8 = 0.5 * (mB_8 + mW_8) * (V_8**2)  # 0.5895 J
    assert math.isclose(V_8, 0.7668, rel_tol=1e-3)
    assert math.isclose(v1_8, 307.5, rel_tol=1e-3)
    assert math.isclose(K1_8, 236.4, rel_tol=1e-3)
    assert math.isclose(K2_8, 0.5895, rel_tol=1e-3)
    assert math.isclose(K2_8 / K1_8, mB_8 / (mB_8 + mW_8), rel_tol=1e-5)
    print("  ✓ Example 8.8 passed")

    # 10. Example 8.9: Automobile Collision in 2D
    mA_9 = 1000.0  # kg (traveling north at 15 m/s)
    vA1y_9 = 15.0  # m/s
    mB_9 = 2000.0  # kg (traveling east at 10 m/s)
    vB1x_9 = 10.0  # m/s
    Px_9 = mB_9 * vB1x_9  # 20000 kg*m/s
    Py_9 = mA_9 * vA1y_9  # 15000 kg*m/s
    M_9 = mA_9 + mB_9     # 3000 kg
    V2x_9 = Px_9 / M_9    # 6.6667 m/s
    V2y_9 = Py_9 / M_9    # 5.0000 m/s
    V2_9 = math.sqrt(V2x_9**2 + V2y_9**2)  # 8.3333 m/s
    theta_9 = math.degrees(math.atan2(V2y_9, V2x_9))  # 36.87 deg
    K1_9 = 0.5 * mA_9 * (vA1y_9**2) + 0.5 * mB_9 * (vB1x_9**2)  # 112500 + 100000 = 212500 J
    K2_9 = 0.5 * M_9 * (V2_9**2)  # 104167 J
    delta_K_9 = K2_9 - K1_9  # -108333 J
    assert math.isclose(V2_9, 8.333, rel_tol=1e-3)
    assert math.isclose(theta_9, 36.87, rel_tol=1e-3)
    assert math.isclose(K1_9, 212500.0, rel_tol=1e-5)
    assert math.isclose(K2_9, 104167.0, rel_tol=1e-3)
    assert math.isclose(delta_K_9, -108333.0, rel_tol=1e-3)
    print("  ✓ Example 8.9 passed")

    # 11. Example 8.10: Elastic Straight-Line Collision
    # mA = 0.50 kg, vA1 = 2.0 m/s, mB = 0.30 kg, vB1 = -2.0 m/s
    # Elastic formulas:
    # vA2x = ((mA - mB)/(mA + mB))*vA1x + (2*mB/(mA + mB))*vB1x
    # vB2x = (2*mA/(mA + mB))*vA1x + ((mB - mA)/(mA + mB))*vB1x
    vA2x_10 = ((0.50 - 0.30)/0.80)*2.0 + (2*0.30/0.80)*(-2.0)  # (0.20/0.80)*2 + (0.60/0.80)*(-2) = 0.50 - 1.50 = -1.0 m/s
    vB2x_10 = (2*0.50/0.80)*2.0 + ((0.30 - 0.50)/0.80)*(-2.0)  # (1.00/0.80)*2 + (-0.20/0.80)*(-2) = 2.50 + 0.50 = +3.0 m/s
    assert math.isclose(vA2x_10, -1.0, rel_tol=1e-5)
    assert math.isclose(vB2x_10, 3.0, rel_tol=1e-5)
    # Relative velocities:
    assert math.isclose(vB2x_10 - vA2x_10, -(vB1x_5 - vA1x_5), rel_tol=1e-5)
    # Kinetic energies:
    K1_10 = 0.5 * 0.50 * (2.0**2) + 0.5 * 0.30 * ((-2.0)**2)  # 1.60 J
    K2_10 = 0.5 * 0.50 * ((-1.0)**2) + 0.5 * 0.30 * (3.0**2)   # 0.25 + 1.35 = 1.60 J
    assert math.isclose(K1_10, K2_10, rel_tol=1e-5)
    print("  ✓ Example 8.10 passed")

    # 12. Example 8.11: Moderating Fission Neutrons
    mn_11 = 1.0  # u
    mC_11 = 12.0 # u
    # Target initially at rest:
    frac_v_11 = (mn_11 - mC_11) / (mn_11 + mC_11)  # -11/13 = -0.84615
    frac_K_11 = frac_v_11**2  # 121 / 169 = 0.71598
    transferred_11 = 1.0 - frac_K_11  # 0.2840
    assert math.isclose(frac_v_11, -11.0 / 13.0, rel_tol=1e-5)
    assert math.isclose(frac_K_11, 121.0 / 169.0, rel_tol=1e-5)
    assert math.isclose(transferred_11, 48.0 / 169.0, rel_tol=1e-5)
    print("  ✓ Example 8.11 passed")

    # 13. Test Your Understanding 8.4: Water moderator
    mw_tyu = 18.0  # u
    frac_v_tyu = (1.0 - 18.0) / (1.0 + 18.0)  # -17 / 19 = -0.8947
    frac_K_tyu = frac_v_tyu**2  # 289 / 361 = 0.80055
    assert math.isclose(abs(frac_v_tyu), 17.0 / 19.0, rel_tol=1e-5)
    assert math.isclose(frac_K_tyu, 0.80055, rel_tol=1e-4)
    print("  ✓ TYU 8.4 passed")

    # 14. Example 8.12: 2D Elastic Collision of Pucks
    mA_12 = 0.500  # kg
    mB_12 = 0.300  # kg
    vA1_12 = 4.00  # m/s
    vA2_12 = 2.00  # m/s
    # Elastic collision kinetic energy:
    vB2_sq_12 = (mA_12 * (vA1_12**2) - mA_12 * (vA2_12**2)) / mB_12
    vB2_12 = math.sqrt(vB2_sq_12)  # sqrt((0.500*16 - 0.500*4)/0.300) = sqrt(6/0.300) = sqrt(20) = 4.4721 m/s
    assert math.isclose(vB2_12, 4.4721, rel_tol=1e-3)
    # Angles alpha and beta from text:
    alpha_12 = math.radians(36.9)
    beta_12 = math.radians(26.6)
    # Check x-momentum:
    Px_after = mA_12 * vA2_12 * math.cos(alpha_12) + mB_12 * vB2_12 * math.cos(beta_12)
    Px_before = mA_12 * vA1_12  # 2.00 kg*m/s
    assert math.isclose(Px_after, Px_before, rel_tol=1e-2)
    # Check y-momentum:
    Py_A_after = mA_12 * vA2_12 * math.sin(alpha_12)  # 0.500 * 2.00 * sin(36.9) = 0.600 kg*m/s
    Py_B_after = -mB_12 * vB2_12 * math.sin(beta_12) # -0.300 * 4.472 * sin(26.6) = -0.600 kg*m/s
    assert math.isclose(Py_A_after + Py_B_after, 0.0, abs_tol=1e-2)
    print("  ✓ Example 8.12 passed")

    # 15. Example 8.13: Center of Mass of Water Molecule
    mO_13 = 16.0  # u
    mH_13 = 1.0   # u
    d_13 = 9.57e-11  # m
    theta_half = math.radians(105.0 / 2.0)  # 52.5 deg
    M_water = mO_13 + 2 * mH_13  # 18.0 u
    x_cm_13 = (2 * mH_13 * d_13 * math.cos(theta_half)) / M_water
    assert math.isclose(x_cm_13, 6.47e-12, rel_tol=1e-2)
    print("  ✓ Example 8.13 passed")

    # 16. Example 8.14: Tug-of-War on the Ice
    mJ_14 = 90.0  # kg (James)
    mR_14 = 60.0  # kg (Ramon)
    L_14 = 20.0   # m apart, mug midway
    # Origin at mug: James at -10.0 m, Ramon at +10.0 m
    x_cm_14 = (mJ_14 * (-10.0) + mR_14 * (10.0)) / (mJ_14 + mR_14)  # -300 / 150 = -2.00 m
    # James moves 6.0 m toward mug: new position xJ2 = -4.0 m
    # Center of mass remains at -2.00 m:
    xR2_14 = ((mJ_14 + mR_14) * x_cm_14 - mJ_14 * (-4.0)) / mR_14  # (150 * (-2) - 90 * (-4)) / 60 = (-300 + 360)/60 = +1.0 m
    disp_Ramon = 10.0 - xR2_14  # 9.0 m toward mug
    assert math.isclose(x_cm_14, -2.00, rel_tol=1e-5)
    assert math.isclose(disp_Ramon, 9.00, rel_tol=1e-5)
    print("  ✓ Example 8.14 passed")

    # 17. Example 8.15: Acceleration of a Rocket
    vex_15 = 2400.0  # m/s
    # dm/dt = -m0 / 120 s
    a_initial_15 = vex_15 / 120.0  # 20.0 m/s^2
    assert math.isclose(a_initial_15, 20.0, rel_tol=1e-5)
    print("  ✓ Example 8.15 passed")

    # 18. Example 8.16: Speed of a Rocket
    m0_m_ratio = 4.0  # m = m0 / 4
    v_rocket_16 = vex_15 * math.log(m0_m_ratio)  # 2400 * ln(4) = 3327.1 m/s
    assert math.isclose(v_rocket_16, 3327.1, rel_tol=1e-3)
    # Speed of last exhaust relative to launch pad:
    v_last_exhaust = v_rocket_16 - vex_15  # 3327.1 - 2400 = 927.1 m/s forward
    assert math.isclose(v_last_exhaust, 927.1, rel_tol=1e-3)
    print("  ✓ Example 8.16 passed")

    # Original in-theory catching application: Same impulse,5xwork/distance.
    catch_masses=[0.50,0.10]
    catch_speeds=[4.0,20.0]
    catch_p=[m*v for m,v in zip(catch_masses,catch_speeds)]
    catch_k=[0.5*m*v*v for m,v in zip(catch_masses,catch_speeds)]
    assert catch_p==[2.0,2.0]
    assert catch_k==[4.0,20.0]
    assert catch_k[1]/catch_k[0]==5.0
    # Original self-check8.1: Five specified impulses, independent of duration
    # when the initial and final momentum are already fixed.
    impulses=[1000*(0-25),1000*(0-25),2000*10,-2000*10,1000*(-25-25)]
    assert impulses == [-25000,-25000,20000,-20000,-50000]
    assert abs(impulses[4])>abs(impulses[0])==abs(impulses[1])>abs(impulses[2])==abs(impulses[3])
    # Equal-mass spring toy: Representative tests of the symbolic conclusion.
    for va,vb in [(-3.0,-4.0),(-0.7,-2.1)]:
        vcx,vcy=-va,-vb
        assert va+vcx==0 and vb+vcy==0
        assert vcx>0 and vcy>0
        assert math.hypot(vcx,vcy)>max(abs(va),abs(vb))
    # Rebound heights imply the corresponding kinetic-energy ratios.
    h=2.1
    incident=math.sqrt(2*g*h)
    assert math.isclose(0.5*incident**2,g*h)
    assert math.isclose((math.sqrt(2*g*h/2)/incident)**2,0.5)
    # After one fragment lands, a positive normal force changes the external
    # force on the two-fragment system, hence changes CM acceleration.
    M_frag,N_ground=2.0,3.0
    assert -g+N_ground/M_frag != -g
    # Constant thrust with decreasing mass, and converse constant acceleration.
    initial_mass,final_mass=120.0,30.0
    thrust=initial_mass*20.0
    assert thrust/final_mass > thrust/initial_mass
    assert final_mass*20.0 < initial_mass*20.0
    # Source8.9 force scale uses rounded original estimates10kN and110kJ.
    assert 10000*0.5 == 5000
    assert (1.1e5/0.20)/5000 == 110
    # Additional source evaluation in8.11 and8.16.
    assert math.isclose((-11/13)*2.6e7,-2.2e7)
    assert math.isclose((2/13)*2.6e7,4.0e6)
    assert math.isclose(0.72**2,0.5184,rel_tol=1e-12)
    assert math.isclose((11/13)**4,14641/28561,rel_tol=1e-12)
    t_exhaust_at_rest=120*(1-math.exp(-1))
    assert math.isclose(t_exhaust_at_rest,75.85446705942692,rel_tol=1e-12)
    m_fraction=1-t_exhaust_at_rest/120
    assert math.isclose(vex_15*math.log(1/m_fraction)-vex_15,0.0,abs_tol=1e-10)
    # Solve the original two-dimensional elastic collision without inserting
    # rounded angles into the conservation laws as assumptions.
    pa1=mA_12*vA1_12;pa2=mA_12*vA2_12;pb2=mB_12*vB2_12
    alpha_exact=math.acos((pa1*pa1+pa2*pa2-pb2*pb2)/(2*pa1*pa2))
    beta_exact=math.asin(pa2*math.sin(alpha_exact)/pb2)
    assert math.isclose(pa2*math.cos(alpha_exact)+pb2*math.cos(beta_exact),pa1,rel_tol=1e-12)
    assert math.isclose(pa2*math.sin(alpha_exact)-pb2*math.sin(beta_exact),0.0,abs_tol=1e-12)
    assert math.isclose(math.degrees(alpha_exact),36.86989764584402,rel_tol=1e-12)
    assert math.isclose(math.degrees(beta_exact),26.56505117707799,rel_tol=1e-12)
    va_final=(vA2_12*math.cos(alpha_exact),vA2_12*math.sin(alpha_exact))
    vb_final=(vB2_12*math.cos(beta_exact),-vB2_12*math.sin(beta_exact))
    assert math.isclose(math.hypot(vb_final[0]-va_final[0],vb_final[1]-va_final[1]),vA1_12,rel_tol=1e-12)
    for va,vb,boost in [(2.0,-3.0,4.1),(-1.2,5.4,-7.0)]:
        assert math.isclose((vb-boost)-(va-boost),vb-va,rel_tol=1e-12)
    assert math.isclose(0.4*9.8,3.92,rel_tol=1e-12)
    assert math.isclose((2400*1000)/120000,(2400*0.5)/60,rel_tol=1e-12)
    print("\nOriginal16 examples, opener,6 self-checks, conversions and sampled symbolic residuals passed. Source coverage and browser layout require separate review.")
    return True

if __name__ == '__main__':
    verify_all()
