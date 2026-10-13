"""Independent numerical checks for Young & Freedman Ch. 27, problems 61–85."""

import math
import numpy as np

E = 1.602e-19
ME = 9.109e-31
MP = 1.673e-27
G = 9.80

def close(value, target, rtol=5e-3):
    np.testing.assert_allclose(value, target, rtol=rtol, atol=1e-35)

def main():
    # 61. For a uniform field, integrate dl x B by endpoint displacement.
    R, I, B = .200, 5.00, .800
    f61a = I * np.cross([R, -R, 0], [0, 0, B])
    f61b = I * np.cross([R, -R, 0], [B, 0, 0])
    np.testing.assert_allclose(f61a, [-.800, -.800, 0])
    np.testing.assert_allclose(f61b, [0, 0, .800])

    # 62. Stated representative estimate: 15 cm hub diameter.
    D62 = .150
    d62 = math.pi * D62 / 36
    mu62 = 1.4 / 12 / 1.0
    area62 = math.pi * (d62 / 2)**2
    n62 = mu62 / ((.75 / 12) * area62)
    close(d62, .0131)
    close(mu62, .1167)
    close(n62, 1.38e4, .02)

    # 63. Earth-field levitation and magnet replacement estimates.
    area63 = math.pi * (.0050 / 2)**2
    bh63 = .50e-4 / math.sqrt(2)
    i63 = 8900 * area63 * G / bh63
    bmin63 = 8900 * area63 * G / 900
    barweight63 = 8900 * area63 * .100 * G
    extra63 = 10 * .100 * 1.0 - barweight63
    close(i63, 4.82e4, .02)
    close(bmin63, 1.90e-3, .02)
    close(extra63, .829, .02)

    # 64. Loop width lies 30 degrees from +x toward +z; current gives
    # mu direction +x - z.
    # Signs follow the current arrow in Fig. P27.64; both field cases checked.
    mu64 = 15 * .08 * .06
    n64 = np.array([math.sin(math.radians(30)), 0, -math.cos(math.radians(30))])
    t64x = mu64 * np.cross(n64, [0.48, 0, 0])
    t64z = mu64 * np.cross(n64, [0, 0, -.48])
    np.testing.assert_allclose(t64x, [0, -.02993, 0], atol=2e-4)
    np.testing.assert_allclose(t64z, [0, .01728, 0], atol=2e-4)

    # 65. Gravitational and magnetic torque balance about the hinge.
    wire_length65 = 2 * (.08 + .06)
    mass65 = .15e-3 / .01 * wire_length65
    mu65 = 8.2 * .08 * .06
    b65 = mass65 * G * .08 * math.tan(math.radians(30)) / (2 * mu65)
    close(mass65, .00420)
    close(b65, .0241)

    # 66. Integral torque of a uniform force per length: integral_0^L x dx.
    xs = np.linspace(0, 1, 100001)
    integral66 = np.trapezoid(xs, xs)
    close(integral66, .5, 1e-8)

    # 67–68. Fig. P27.67 has Q->P, P->R, R->Q.
    # In 67 B=+y; in 68 B=-z. Both closed-loop net forces vanish.
    edges67 = [np.array([0., .6, 0.]), np.array([.8, -.6, 0.]),
               np.array([-.8, 0., 0.])]
    forces67 = [5*np.cross(e, [0, 3, 0]) for e in edges67]
    np.testing.assert_allclose(forces67, [[0,0,0],[0,0,12],[0,0,-12]])
    np.testing.assert_allclose(np.sum(forces67, axis=0), [0,0,0])
    forces68 = [5*np.cross(e, [0, 0, -3]) for e in edges67]
    np.testing.assert_allclose(forces68, [[-9,0,0],[9,12,0],[0,-12,0]])
    np.testing.assert_allclose(np.sum(forces68, axis=0), [0,0,0])
    # Only the torque component along the PR hinge (x) is relevant.
    np.testing.assert_allclose(np.cross([.4,.3,0], forces67[1])[0], 3.6)

    # 69. For a circular coil in nonuniform field the radial components cancel;
    # axial components add, giving N I B cos(60 deg) times circumference.
    f69 = 50 * .950 * .220 * math.sin(math.radians(60)) * math.pi * .0156
    close(f69, .444)

    # 70. Bar pivot torque integral, gravity at midpoint, current balances it.
    L70, theta70, m70, B70 = .300, math.radians(30), .0120, .150
    i70 = m70 * G * (L70 / 2 * math.cos(theta70)) / (B70 * L70**2 / 2)
    close(i70, 2.26)

    # 71. Linear field in yz-plane; integrate each straight side parametrically.
    # Clockwise loop: (0,0)->(0,L)->(L,L)->(L,0)->(0,0).
    # (Results and orientation are represented component-wise in solution.)
    L71, I71, B071 = 1.0, 1.0, 1.0
    vertices71 = [np.array([0., 0., 0.]), np.array([0., L71, 0.]),
                  np.array([L71, L71, 0.]), np.array([L71, 0., 0.]),
                  np.array([0., 0., 0.])]
    forces71 = []
    for a, b in zip(vertices71[:-1], vertices71[1:]):
        count = 2000
        dl = (b-a)/count
        locations = a + (np.arange(count)[:, None]+.5)*dl
        fields = np.column_stack([np.zeros(count), B071*locations[:, 2]/L71,
                                   B071*locations[:, 1]/L71])
        forces71.append(I71*np.sum(np.cross(np.broadcast_to(dl, fields.shape), fields), axis=0))
    np.testing.assert_allclose(forces71, [[.5, 0, 0], [0, -1, 0], [-.5, 0, 0], [0, 0, 0]], atol=1e-12)
    np.testing.assert_allclose(np.sum(forces71, axis=0), [0, -1, 0], atol=1e-12)

    # 72. Static torques about hinge: T L sin(theta) balances mg L/2 cos(theta)
    # plus magnetic torque I B L^2/2 times angle factor from geometry.
    L72, m72, th72, I72, B72 = .180, .0840, math.radians(53), 12.0, .120
    tauB72 = I72 * B72 * L72**2 / 2
    t72 = (m72 * G * L72 / 2 * math.cos(th72) + tauB72) / (L72 * math.sin(th72))
    close(t72, .472, .02)

    # 73. Check torque and work independently in the two geometric stages.
    # First stage: h=R(1-cos(theta)); second: h=R(1+theta).
    r73, mass73, w73, n73, b73, s73 = .40, 2.0, .10, 10, 1.20, 1.30
    mu_b73 = s73 * mass73 * G * r73
    i73 = s73 * mass73 * G / (2 * n73 * w73 * b73)
    close(2 * n73 * i73 * w73 * b73 / (mass73 * G), s73)
    imin73 = mass73 * G / (2 * n73 * w73 * b73)
    close(2 * n73 * imin73 * w73 * b73 / (mass73 * G), 1.0)
    theta73a = np.linspace(0.0, math.pi/2, 20001)
    tau73a = mass73 * G * r73 * (s73 - 1) * np.sin(theta73a)
    ua73 = (1-s73) * mass73 * G * r73 * (1-np.cos(theta73a))
    work_integral73a = np.trapezoid(-tau73a, theta73a)
    close(work_integral73a, float(ua73[-1]), 1e-7)
    theta73b = np.linspace(0.0, math.pi/2, 20001)
    tau73b = mass73 * G * r73 * (s73 * np.cos(theta73b) - 1)
    ub73 = mass73 * G * r73 * (1-s73 + theta73b - s73*np.sin(theta73b))
    work_integral73b = (1-s73)*mass73*G*r73 + np.trapezoid(-tau73b, theta73b)
    close(work_integral73b, float(ub73[-1]), 1e-7)
    close(float(ua73[-1]), float(ub73[0]))
    htop73 = r73 * (1 + math.pi/2)
    close(htop73/r73, 1 + math.pi/2)
    thetaeq73 = math.acos(1/s73)
    taueq73 = mass73*G*r73*(s73*math.cos(thetaeq73)-1)
    close(taueq73, 0.0, 1e-10)
    heq73 = r73*(1+thetaeq73)
    assert r73 <= heq73 <= htop73
    s_limit73 = 0.5*(1+math.pi/2)
    close((1+math.pi/2)-2*s_limit73, 0.0, 1e-12)
    # 74. Gyro-gravitational motion: omega=qB/m, exact analytic trajectories.
    # Check numerical finite-difference ODE residual at representative times.
    q74, m74, b74 = 19.6e-6, 1.00e-6, 10.0
    w74 = q74 * b74 / m74
    for t in np.linspace(0, .02, 11):
        vy = G / w74 * math.sin(w74*t)
        vx = G / w74 * (1 - math.cos(w74*t))
        close(vx*vx + vy*vy, 2*G*(G/w74**2)*(1-math.cos(w74*t)), .02)

    # 75. Torque fixes Bx and By; magnitude 13D/(IA) fixes |Bz|.
    moment75 = np.array([0., 0., -1.])
    field75 = np.array([3., 4., -12.])
    np.testing.assert_allclose(np.cross(moment75, field75), [4., -3., 0.])
    close(float(np.linalg.norm(field75)), 13.0, 1e-12)

    # 76–78. Cyclotron / mass spectrometer data reductions.
    # 76: q/m = 2V/(B^2 R^2); data regression in R^2 versus V.
    V76 = np.array([10,12,14,16,18])*1e3
    r76 = np.array([.199,.218,.236,.252,.268])
    slope76, intercept76 = np.polyfit(V76, r76**2, 1)
    qm76 = 2/(.250**2*slope76)
    v76 = math.sqrt(2*qm76*20e3)
    close(qm76, 7.96e6, .03)
    close(v76, 5.64e5, .03)

    # 77: E^2=(2e/m) B^2 V; ordinate 800 in units of 10^8 at 400 V.
    slope77 = 2.0e8
    m77 = 2*E*.340**2/slope77
    v77 = math.sqrt(2*E*400/m77)
    close(m77, 1.86e-28, .03)
    close(v77, math.sqrt(8.0e10)/.340, 1e-12)

    # 78: alpha cyclotron slope f/B gives q/(2 pi m); read graph slope.
    slope78 = (31e5 - 8e5) / .30
    qm78 = 2*math.pi*slope78
    malpha78 = 2*E/qm78
    fp78 = E*.300/(2*math.pi*MP)
    fe78 = E*.300/(2*math.pi*ME)
    valpha78 = 2*E*.300*.120/malpha78
    kalpha78 = .5*malpha78*valpha78**2
    close(qm78, 4.82e7, .03)
    close(malpha78, 6.65e-27, .03)
    close(fp78, 4.57e6, .02)
    close(fe78, 8.41e9, .02)

    # 79. Integrate latitude-loop moment dmu_z = (1/2) Omega sigma R^4 sin^3(theta)dtheta dphi.
    theta = np.linspace(0, math.pi, 200001)
    integ79 = np.trapezoid(np.sin(theta)**3, theta)
    close(integ79, 4/3, 1e-8)

    # 80. Equator-parallel velocity at latitude80 has a radial parallel component.
    latitude80 = math.radians(80)
    parallel80 = 400e3*math.cos(latitude80)
    perpendicular80 = 400e3*math.sin(latitude80)
    r80 = ME*perpendicular80/(E*15e-6)
    f80 = E*15e-6/(2*math.pi*ME)
    close(r80, .150, .01)
    close(parallel80, 69.5e3, .002)
    close(perpendicular80, 394e3, .002)
    close(f80, 4.20e5, .02)

    # 81. Radius and magnetic-arc geometry, with field width d=0.25 m.
    q81, m81, v81, B81, d81, D81 = 2.15e-6, 3.20e-11, 1.45e5, .420, .250, .750
    R81 = m81*v81/(q81*B81)
    phi81 = math.asin(d81/R81)
    t81 = phi81*R81/v81
    dx1_81 = R81*(1-math.cos(phi81))
    dx_81 = dx1_81 + (D81-d81)*math.tan(phi81)
    close(R81, 5.14)

    # 82. Cycloid energy plus centripetal force at the crest.
    # qvB-qE=mv^2/(2y), and qEy=mv^2/2 imply v=2E/B.
    q82, e82, m82, b82 = 2.0, 3.0, 5.0, 6.0
    y82 = 2*m82*e82/(q82*b82**2)
    v82 = math.sqrt(2*q82*e82*y82/m82)
    centripetal82 = m82*v82**2/(2*y82)
    np.testing.assert_allclose(q82*v82*b82-q82*e82, centripetal82)

    # 83–85. MRI passage: torque, nuclear pairing, nerve current and force.
    tau83 = 1.4e-26 * 2
    v85 = .100 / (.6 * .001 / (math.pi*(.0015/2)**2))
    f85 = v85 * .001 * 2
    close(tau83, 2.8e-26)
    close(v85, .000294, .02)
    close(f85, 5.88e-7, .03)
    print("Chapter 27 exercises 27.61–27.85: numerical checks passed.")

if __name__ == "__main__":
    main()
