"""Independent numerical/vector checks for the Chapter 28 exercises 1–30."""
import math
import numpy as np

MU0 = 4 * math.pi * 1e-7
K = 8.9875517923e9
E = 1.602176634e-19
C = 299_792_458.0
def close(a, b, rtol=2e-3, atol=1e-30):
    assert math.isclose(float(a), float(b), rel_tol=rtol, abs_tol=atol), (a, b)

# 1 and 5: cross products verify both magnitudes and signed directions.
def moving_charge_field(q, v, r):
    return 1e-7 * q * np.cross(v, r) / np.linalg.norm(r) ** 3
v1 = np.array([0.0, 8.00e6, 0.0])
q1 = 6e-6
assert np.allclose(moving_charge_field(q1, v1, [.5, 0, 0]), [0, 0, -1.92e-5])
assert np.allclose(moving_charge_field(q1, v1, [0, -.5, 0]), [0, 0, 0])
assert np.allclose(moving_charge_field(q1, v1, [0, 0, .5]), [1.92e-5, 0, 0])
close(np.linalg.norm(moving_charge_field(q1, v1, [0, -.5, .5])), 6.7882251e-6)
v5 = np.array([6.8e5, 0, 0])
q5 = -4.8e-6
assert np.allclose(moving_charge_field(q5, v5, [.5, 0, 0]), 0)
assert np.allclose(moving_charge_field(q5, v5, [0, .5, 0]), [0, 0, -1.3056e-6])
assert np.allclose(moving_charge_field(q5, v5, [.5, .5, 0]), [0, 0, -4.61599307e-7])
assert np.allclose(moving_charge_field(q5, v5, [0, 0, .5]), [0, 1.3056e-6, 0])

# 2–4: atomic scale, electron sign, geometric angle and vector superposition.
close(K * E / (5.3e-11)**2, 5.126253285e11)
close(1e-7 * E * 2.2e6 / (5.3e-11)**2, 12.5481972)
close(1e-7 * E * .1 * C / (2e-6)**2 * math.sin(math.radians(30)), 6.004006e-8)
for angle in (60, -60):
    rvec = 2e-6*np.array([math.cos(math.radians(angle)), math.sin(math.radians(angle)), 0.0])
    Bvec = moving_charge_field(-E, [0, .1*C, 0], rvec)
    close(np.linalg.norm(Bvec), 6.004006e-8)
    assert Bvec[2] > 0
close(1e-7 * E * .1 * C / (2e-6)**2, 1.2008012e-7)
close(1e-7 * 3 * E * 2.5e5 * math.sin(math.radians(140)) / (8.65e-9)**2, 1.0323024e-4)

# 6: P lies d from each source, but the two charges are 2d apart.
d = .120
B_P = 1e-7 * (8e-6 * 4.5e6 + 3e-6 * 9e6) / d**2
close(B_P, 4.375e-4)
F_E6 = K * 8e-6 * 3e-6 / (2*d)**2
F_B6 = 8e-6 * 4.5e6 * (1e-7 * 3e-6 * 9e6 / (2*d)**2)
close(F_E6, 3.74481325)
close(F_B6, 1.6875e-3)
close(F_E6 / F_B6, 2.219e3)

# 7–13: point/elementary current fields and hand-rule checks.
close(1e-7 * E * 3.3e3 / (6.6e-6)**2, 1.21377e-12)
v28 = 735e3
Be = 1e-7 * (-E) * np.cross([-v28, 0, 0], [0, -5e-9, 0]) / (5e-9)**3
Bp = 1e-7 * E * np.cross([0, -v28, 0], [-4e-9, 0, 0]) / (4e-9)**3
assert Be[2] < 0 and Bp[2] < 0
close(Be[2], -4.7103993e-4)
close(Bp[2], -7.3600e-4)
close((Be+Bp)[2], -1.20703993e-3)
close(1e-7 * E * 735e3 * 5e-9 / (41e-18)**1.5, 2.242807e-4)
close(K * E**2 / (41e-18), 5.6270184e-12)
Fmag8 = E*v28*2.242807e-4
assert np.cross([0.0, -v28, 0.0], [0.0, 0.0, -2.242807e-4])[0] > 0
close(Fmag8, 2.6411294e-17)
close(1e-7 * 10 * 1.1e-3 / .05**2, 4.4e-7)
rB9 = math.hypot(.14, .05)
close(1e-7 * 10 * 1.1e-3 * .05 / rB9**3, 1.674073e-8)
close(np.linalg.norm(1e-7 * 5.4 * np.cross([0, .5e-3, 0], [0, -.73, .39]) / math.hypot(.73, .39)**3), 1.857e-10)
close(1e-7 * 4 * .5e-3 / 2**2, 5e-11)
close(1e-7 * 4 * .5e-3 / 8, 2.5e-11)
close(1e-7 * 36 * 1.5e-3 * (.05/.08) / .08**2, 5.2734375e-7)
close(2 * 1e-7 * 28 * 2e-3 * math.sin(math.pi/4) / (.03/math.sqrt(2))**2, 1.7599102e-5)
P13 = np.array([.015,.015,0.])
source13 = [np.array([0.,0.,0.]),np.array([.03,.03,0.])]
elements13 = [np.array([0.,.002,0.]),np.array([.002,0.,0.])]
B13 = sum(1e-7*28*np.cross(dl,P13-point)/np.linalg.norm(P13-point)**3 for dl,point in zip(elements13,source13))
assert B13[2]<0
close(B13[2],-1.7599102e-5)

# 14–22: force components, units, field superposition, and finite geometry.
B14 = MU0 * 60 / (2*math.pi*.08)
close(-3e-6*9e3/(8e-3*B14), -2.25e4)
close(3e-6*(-5e3)/(8e-3*B14), -1.25e4)
close(MU0*20e3/(2*math.pi*5), 8e-4)
I16 = 8.2e18 * E
close(I16, 1.31378484)
close(MU0 * I16 /(2*math.pi*.04), 6.5689242e-6)
assert np.array_equal(np.cross([-1, 0, 0], [0, 0, 1]), [0, 1, 0])
close(2*math.pi*.05*(10e-10)/MU0, 2.5e-4)
close(MU0/(2*math.pi)*(1 + 1/3), 2.66666667e-7)
close(math.hypot(1.5e-6, MU0*8/(2*math.pi)), 2.19317122e-6)
close((MU0*150/(2*math.pi*8))/(.5e-4)*100, 7.5)
close(MU0*4/(2*math.pi)*(1/.3 + 1/.2), 6.66666667e-6)
close(2*MU0*4/(2*math.pi)*.2/(.05**2+.2**2), 7.52941176e-6)
a, b = .042/2, .095/2
coef22 = MU0/math.pi * math.hypot(a,b)/(a*b)
close(5.5e-5/coef22, 2.64091852)

# 23–30: symmetry, forces, finite wire, and inverse force relation.
side_half = .2/2
wire_field_23 = MU0*100/(2*math.pi*math.sqrt(2)*side_half)
close(4*wire_field_23/math.sqrt(2), 4e-4)
corners = [(-side_half, side_half), (side_half, side_half),
           (-side_half, -side_half), (side_half, -side_half)]
def square_center_field(signs):
    total = np.zeros(2)
    for (x, y), sign in zip(corners, signs):
        total += MU0*100*sign/(2*math.pi*(2*side_half**2))*np.array([y, -x])
    return total
assert np.allclose(square_center_field([-1,-1,-1,-1]), [0,0], atol=1e-15)
assert np.allclose(square_center_field([-1,+1,+1,-1]), [0,0], atol=1e-15)
assert np.allclose(square_center_field([-1,-1,+1,+1]), [-4e-4,0], atol=1e-15)
# Equal distances make the signed current sum the field-cancellation condition.
close(20 - 8 - 10 - 2, 0)
close(MU0*10/(2*math.pi*.08), 25e-6)
close(MU0*12/(2*math.pi*.15), 16e-6)
close(math.hypot(25e-6+16e-6, 0), 41e-6)
close(math.hypot(25e-6-16e-6, 0), 9e-6)
sin_theta = .1 / math.hypot(.1,.05)
Bfinite = MU0*8/(2*math.pi*.05)*sin_theta
Binf = MU0*8/(2*math.pi*.05)
close(Bfinite, 2.8621670e-5)
close((Binf/Bfinite-1)*100, 11.8033989)
# 27: force/length balances weight/length; the algebraic relation is dimensional.
assert math.isclose((MU0/(2*math.pi)) * 1**2 / (1 * 9.8),
                    MU0/(2*math.pi*9.8), rel_tol=1e-12)
close(MU0*5*2/(2*math.pi*.4)*1.2, 6e-6)
close(4*MU0*5*2/(2*math.pi*.4)*1.2, 24e-6)
close(4e-5*2*math.pi*.025/(MU0*.6), 8.33333333)
# 28: opposite middle current repels each outer wire at d; the other outer
# wire attracts it at 2d. Check the signed force and its N/m dimensions.
I_test, d_test = 5.0, .10
f_near = MU0*I_test**2/(2*math.pi*d_test)
f_far = MU0*I_test**2/(2*math.pi*(2*d_test))
close(f_near-f_far, MU0*I_test**2/(4*math.pi*d_test))
close(f_near, 5e-5)
close(f_near-f_far, 2.5e-5)
def wire_force_per_length(I_source, I_target, displacement):
    # Currents are signed along x; displacement points from source wire to target.
    return -MU0*I_source*I_target/(2*math.pi*np.linalg.norm(displacement)**2) * np.array(displacement)
outer_top = wire_force_per_length(-I_test, I_test, [0, d_test, 0])
outer_bottom = wire_force_per_length(I_test, I_test, [0, 2*d_test, 0])
middle_top = wire_force_per_length(I_test, -I_test, [0, -d_test, 0])
middle_bottom = wire_force_per_length(I_test, -I_test, [0, d_test, 0])
assert outer_top[1] > 0 and math.isclose(outer_top[1]+outer_bottom[1], f_near-f_far)
assert math.isclose(middle_top[1]+middle_bottom[1], 0.0, abs_tol=1e-15)
outer_bottom_wire = wire_force_per_length(-I_test, I_test, [0, -d_test, 0]) + wire_force_per_length(I_test, I_test, [0, -2*d_test, 0])
assert outer_bottom_wire[1] < 0
print("Chapter 28 exercises 28.1–28.30: independent numerical and vector checks passed.")
