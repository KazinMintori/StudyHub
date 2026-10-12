"""Independent numerical checks for translated Physics II exercises 26.61–88."""
from math import exp, log, pi, sqrt


def solve_2(a, b, c, d, e, f):
    det = a * d - b * c
    return ((e * d - b * f) / det, (a * f - e * c) / det)


def close(actual, expected, rel=2e-3):
    assert abs(actual - expected) <= rel * max(abs(expected), 1e-30), (actual, expected)


def run():
    # P26.61: illustrative wire estimate using the stated design current density.
    area61 = 1.0 / 5.0  # mm^2 at 5 A/mm^2
    diameter61 = sqrt(4 * area61 / pi)
    resistance_per_m61 = 1.72e-8 / (area61 * 1e-6)
    length61 = 1.0 / (2 * resistance_per_m61)
    close(diameter61, 0.505, 2e-3)
    close(resistance_per_m61, 0.0860, 1e-3)
    close(length61, 5.814, 1e-3)

    # P26.62: nodal solution for the two internal junctions, not a series-parallel guess.
    vl, vr = solve_2(2.5, -1.0, -1.0, 2.5, 14.0, 7.0)
    currents = {
        "R1": (14.0 - vl) / 1.0,
        "R4": vl / 2.0,
        "R2": (14.0 - vr) / 2.0,
        "R5": vr / 1.0,
        "R3": vl - vr,
    }
    close(vl, 8.0)
    close(vr, 6.0)
    assert all(i > 0 for i in currents.values())
    close(sum(i * i * r for i, r in zip(currents.values(), (1, 2, 2, 1, 1))), 140.0)
    close(sum(currents.values()), 22.0)  # Branch currents count the bridge leg twice.
    close((vl - vr) / 1.0, 2.0)
    close(14.0 / (currents["R1"] + currents["R2"]), 1.4)

    # P26.63: reduced multi-loop network and independent branch/power checks.
    req_upper = 1.0 / (1 / 30.0 + 1 / 60.0 + 1 / 60.0 + 1 / 30.0)
    close(req_upper, 10.0)
    i_total = 2.0
    v_upper = i_total * req_upper
    v_bottom = -5.0 - v_upper - 2.0 * 5.0 - 10.0
    i_20 = v_bottom / 20.0
    i_15 = i_total - i_20
    emf = v_bottom - 15.0 * i_15
    close(v_upper, 20.0)
    close(v_bottom, -45.0)
    close(i_20, -2.25)
    close(i_15, 4.25)
    close(emf, -108.75)
    i_10 = v_upper / 30.0
    close(60.0 / (i_10 * i_10 * 10.0), 13.5)
    p63 = (i_total**2 * 5.0 + i_total**2 * 5.0
           + i_20**2 * 20.0 + i_15**2 * 15.0
           + i_10**2 * (10.0 + 20.0) + (v_upper/60.0)**2 * 60.0 * 2
           + (v_upper/30.0)**2 * 30.0)
    source63 = 5.0 * i_total + 108.75 * i_15 - 10.0 * i_total
    close(p63, source63)

    # P26.66: full branch reduction and hottest-resistor power limit.
    r_mid = 1.0 / (1 / 25.0 + 1 / 15.0 + 1 / (10.0 + 1.0 / (1 / 20.0 + 1 / 20.0)))
    r_total = 25.0 + 30.0 + r_mid + 40.0 + 25.0
    e_max = sqrt(2.0 / 40.0) * r_total
    close(r_mid, 6.3829787234)
    close(e_max, 28.25, 1e-2)
    close((sqrt(2.0 / 40.0) / 2.0) ** 2 * 50.0, 0.625)

    # P26.64 and P26.68: bounded maximum and same-voltage power ratio.
    r1_64, r2_64, r3_64, e64 = 6.0, 24.0, 12.0, 24.0
    rpar64 = 1 / (1 / r1_64 + 1 / r2_64)
    v1_64 = e64 * rpar64 / (r3_64 + rpar64)
    close(v1_64**2 / r1_64, 7.84, 1e-3)
    close(45.0 * 9.0, 405.0)

    # P26.67: open and closed switch nodal checks, current direction, source power balance.
    va, vb = 12.0, 24.0
    close(va - vb, -12.0)
    va, vb = solve_2(1 / 6 + 1 / 3 + 1 / 3, -1 / 3,
                     -1 / 3, 1 / 3 + 1 / 6 + 1 / 3,
                     36 / 6, 36 / 3)
    close(va, 15.4285714)
    close(vb, 20.5714286)
    close((vb - va) / 3.0, 12 / 7)
    isource = (36.0 - va) / 6 + (36.0 - vb) / 3
    close(isource, 60 / 7)
    p_resistors = ((36.0 - va) ** 2 / 6 + va * va / 3
                   + (36.0 - vb) ** 2 / 3 + vb * vb / 6
                   + (vb - va) ** 2 / 3)
    close(36.0 * isource, p_resistors)

    # P26.69 dielectric leakage, using source units (30.0 micrometres).
    eps0 = 8.8541878128e-12
    tau = 8.70 * eps0 * 3.10e12
    cap69 = 8.70 * eps0 * 1.00e-4 / 30.0e-6
    q69 = cap69 * 5.00
    t_half = tau * log(2.0)
    i_half = q69 / (2.0 * tau)
    close(tau, 239.0, 1e-2)
    close(cap69, 2.567e-10, 1e-3)
    close(q69, 1.2835e-9, 1e-3)
    close(t_half, 165.522, 1e-3)
    close(i_half, 2.685e-12, 1e-2)

    # P26.70 initial short / final open limits.
    i70 = 42.0 / (8.0 + 1 / (1 / 6.0 + 1 / 3.0))
    vparallel70 = (42.0 - 8.0 * i70)
    close(i70, 4.2)
    close(vparallel70 / 6.0, 1.4)
    close(vparallel70 / 3.0, 2.8)
    close(4e-6 * 42.0 * 6.0 / (8.0 + 6.0), 72e-6)

    # P26.71: charge continuity at dielectric insertion, RC transient, battery and heat energy.
    c71 = eps0 * (0.02**2) / 0.003
    q71 = c71 * 10.0
    v_after = 10.0 / 12.0
    i_after = (10.0 - v_after) / 10.0
    u_after = 0.5 * 12 * c71 * v_after**2
    u_final = 0.5 * 12 * c71 * 10.0**2
    battery_energy = 10.0 * (12 * c71 * 10.0 - q71)
    heat = 0.5 * 12 * c71 * (10.0 - v_after) ** 2
    close(i_after, 11 / 12)
    close(battery_energy, (u_final - u_after) + heat)
    close(q71, 1.18e-11, 1e-2)

    # P26.72 resistor power limits the current and determines capacitor energy.
    i72 = sqrt(300.0 / 5.0)
    vc72 = 50.0 - 5.0 * i72
    close(0.5 * 6e-6 * vc72**2, 3.81e-4, 1e-3)

    # P26.73 loaded divider and ideal-meter limit.
    for rv, expected in ((50e3, 114.286), (5e6, 263.158), (float("inf"), 266.667)):
        load = 200e3 if rv == float("inf") else 1 / (1 / 200e3 + 1 / rv)
        close(400 * load / (100e3 + load), expected, 1e-3)

    # P26.74 Wheatstone bridge result.
    close(850.0 * 33.48 / 15.0, 1897.2, 1e-4)

    # P26.75 charge conservation at the joined capacitor node.
    vb75 = (6.0 * 18.0 - 54.0) / 9.0
    close(vb75, 6.0)
    close(6.0 * (18.0 - vb75), 72.0)
    close(3.0 * vb75, 18.0)

    # P26.76–77 energy and RC identities.
    u76 = (6.90e-6) ** 2 / (2 * 4.62e-6)
    p76_0 = (6.90e-6 / 4.62e-6) ** 2 / 850.0
    close(u76, 5.15e-6, 1e-3)
    close(p76_0, 2.6242e-3, 1e-3)
    r77 = 110.0 / 6.5e-5
    c77 = 5.2 / r77
    close(r77, 1.6923077e6, 1e-6)
    close(c77, 3.073e-6, 1e-3)

    # P26.79 least-squares fit q(i), units confirmed as microcoulombs.
    imA = [56.0, 48.0, 40.0, 32.0, 24.0]
    qmicro = [10.1, 19.8, 30.2, 40.0, 49.9]
    xbar, ybar = sum(imA) / len(imA), sum(qmicro) / len(qmicro)
    slope = sum((x-xbar)*(y-ybar) for x, y in zip(imA, qmicro)) / sum((x-xbar)**2 for x in imA)
    intercept = ybar - slope*xbar
    resistance = -slope * 1e-3 / 5e-6
    emf79 = intercept * 1e-6 / 5e-6
    t79 = -resistance * 5e-6 * log(1 - 10.0 / emf79)
    close(resistance, 249.2, 3e-3)
    close(emf79, 16.0, 2e-3)
    close(t79, 1.226e-3, 3e-3)

    # P26.80 inventory inversion.
    rsum, rprod = 48.0**2 / 48.0, 9.0 * 48.0
    disc = sqrt(rsum**2 - 4 * rprod)
    r1, r2 = (rsum + disc) / 2, (rsum - disc) / 2
    close(r1, 36.0)
    close(r2, 12.0)

    # P26.82 charge/discharge thresholds and period.
    rc82 = 10e3 * 10e-6
    period82 = rc82 * (4 * log(2) + 0.8 * log(3.5))
    close(1 / period82, 2.65, 2e-3)

    # P26.81 gain and the bias point implied by Vout=7.5 V.
    gain81 = -1000.0 / 100.0
    vin_bias81 = 0.60 + (15.0 - 7.5) / 10.0
    close(gain81, -10.0)
    close(vin_bias81, 1.35)
    close(15.0 - 10.0 * (15.0 - 0.60), -129.0)

    # P26.84 symmetry reduction of the cube network.
    close(1 / 3.0 + 1 / 6.0 + 1 / 3.0, 5 / 6)

    # P26.78 graph read-off, with points digitized approximately from the printed plot.
    tms78 = [0.5, 1.0, 1.5, 2.0, 3.0]
    ln_i78 = [-2.4, -2.7, -3.0, -3.35, -4.0]
    xb, yb = sum(tms78) / len(tms78), sum(ln_i78) / len(ln_i78)
    slope78 = sum((x-xb)*(y-yb) for x,y in zip(tms78,ln_i78)) / sum((x-xb)**2 for x in tms78)
    intercept78 = yb - slope78*xb
    tau78 = -1 / slope78 * 1e-3
    i078 = exp(intercept78)
    c78 = tau78 / 196.0
    q078 = tau78 * i078
    close(c78, 8.0e-6, 0.08)
    close(q078, 2.0e-4, 0.08)

    # Infinite ladder, attenuation and bridge calculations.
    r1, r2 = 6.4e3, 8.0e8
    rt = r1 + sqrt(r1**2 + 2 * r1 * r2)
    beta = 2 * r1 * (rt + r2) / (rt * r2)
    close(rt, 3.2064e6, 2e-4)
    close(beta, 0.00401, 2e-3)
    segments_per_2mm = 2.0e-3 / 1.0e-6
    remaining_unmyelinated = (1 + beta) ** -segments_per_2mm
    reduction_unmyelinated = 1 - remaining_unmyelinated
    close(segments_per_2mm, 2000)
    close(remaining_unmyelinated, 3.4e-4, 2e-2)
    close(reduction_unmyelinated, 0.99966, 2e-4)
    r2_myelin = 3.3e12
    rt_myelin = r1 + sqrt(r1**2 + 2 * r1 * r2_myelin)
    beta_myelin = 2 * r1 * (rt_myelin + r2_myelin) / (rt_myelin * r2_myelin)
    remaining_myelinated = (1 + beta_myelin) ** -segments_per_2mm
    reduction_myelinated = 1 - remaining_myelinated
    close(rt_myelin, 2.055e8, 2e-3)
    close(beta_myelin, 6.23e-5, 2e-3)
    close(remaining_myelinated, 0.883, 2e-3)
    close(reduction_myelinated, 0.117, 2e-2)

    # MCAT passage: channel resistivity, density and membrane time constant.
    rho86 = 1e11 * pi * (0.3e-9) ** 2 / 12e-9
    density87 = 5e-3 / (50e-3 / 1e11) / 1e8  # channels per square micrometre
    tau88 = 1e-6 / (5e-3 / 50e-3)
    close(rho86, 2.356, 1e-3)
    close(density87, 100.0)
    close(tau88, 10e-6)

    print("PASS: independent circuit, energy, RC, regression, and MCAT calculations")
    print(f"P26.62 nodes: Va={vl:.3f} V, Vb={vr:.3f} V, Req={1.4:.3f} ohm")
    print(f"P26.63 emf={emf:.3f} V, P26.66 limit={e_max:.3f} V")
    print(f"P26.69 tau={tau:.3f} s, Q0={q69:.4e} C")
    print(f"P26.79 fit: slope={slope:.4f} microC/mA, R={resistance:.2f} ohm, E={emf79:.3f} V")
    print(f"P26.85 Δx=1 μm, n={segments_per_2mm:.0f}: unmyelinated remaining={remaining_unmyelinated:.5g}, loss={reduction_unmyelinated:.5%}")
    print(f"P26.85 myelinated remaining={remaining_myelinated:.5g}, loss={reduction_myelinated:.5%}")


if __name__ == "__main__":
    run()
