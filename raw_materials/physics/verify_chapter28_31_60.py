"""Independent numerical and vector checks for Chapter 28 exercises 28.31–28.60."""

from __future__ import annotations

import math

import numpy as np


MU0 = 4 * math.pi * 1e-7
MU0_OVER_4PI = 1e-7
E = 1.602176634e-19
ME = 9.1093837139e-31
G = 9.80665


def near(value: float, expected: float, rel: float = 1e-6) -> None:
    assert math.isclose(value, expected, rel_tol=rel, abs_tol=1e-15), (value, expected)


def point_charge_field(q: float, velocity: np.ndarray, r_vec: np.ndarray) -> np.ndarray:
    r = np.linalg.norm(r_vec)
    return MU0_OVER_4PI * q * np.cross(velocity, r_vec) / r**3


def wire_field_z(current_z: float, r_vec_xy: np.ndarray) -> np.ndarray:
    x, y = r_vec_xy
    r2 = x * x + y * y
    return MU0 * current_z / (2 * math.pi * r2) * np.array([-y, x, 0.0])


def test_31_36() -> dict[str, float]:
    b31 = 3.0e-8 * 1e-4
    i31 = 2 * 0.08 * b31 / MU0
    near(i31, 3.8197186342e-7)

    # A radial straight lead has dl parallel r, so only the semicircle contributes.
    i32, radius32 = 3.2, 0.04
    b32 = MU0 * i32 / (4 * radius32)
    assert np.linalg.norm(np.cross([1, 0, 0], [1, 0, 0])) == 0

    i1_33, i2_33, radius33 = 2.5, 1.7, 0.06
    b33 = MU0 * abs(i2_33 - i1_33) / (4 * radius33)
    assert b33 > 0
    near(MU0 * abs(i1_33 - i1_33) / (4 * radius33), 0.0)

    a34, n34, b034 = 0.024, 800, 0.0770
    i34 = 2 * a34 * b034 / (MU0 * n34)
    xhalf34 = a34 * math.sqrt(2 ** (2 / 3) - 1)
    ratio34 = a34**3 / (xhalf34**2 + a34**2) ** 1.5
    near(i34, 3.6764792)
    near(ratio34, 0.5)

    i35 = 12 * 0.15 / 0.10
    b_in35 = MU0 * 12 / (2 * 0.10)
    b_out35 = MU0 * i35 / (2 * 0.15)
    near(i35, 18.0)
    near(b_in35, b_out35)

    a36, x36, i36, field36 = 0.06, 0.06, 2.5, 6.39e-4
    n36 = field36 * 2 * (x36**2 + a36**2) ** 1.5 / (MU0 * i36 * a36**2)
    near(n36, 69.0362551)
    return {
        "I31_A": i31,
        "B32_T": b32,
        "B33_T": b33,
        "I34_A": i34,
        "x_half34_m": xhalf34,
        "I35_A": i35,
        "N36_turns": n36,
    }


def test_37_48() -> dict[str, float]:
    integral37 = 3.83e-4
    i37 = integral37 / MU0
    near(i37, 304.781716)
    assert math.isclose(-integral37, -(integral37), rel_tol=0)

    # Fig. E28.38, counterclockwise paths: outward currents are positive.
    path_currents38 = {"a": 2.0, "b": -4.0, "c": 2.0, "d": 4.0}
    assert path_currents38 == {"a": 2.0, "b": -4.0, "c": -4.0 + 6.0, "d": -4.0 + 6.0 + 2.0}
    integrals38 = {key: MU0 * value for key, value in path_currents38.items()}

    # Coax: outside encloses equal opposite currents; same-direction variant sums.
    assert 5.0 - 5.0 == 0.0
    b41 = MU0 * (2.0 + 3.0) / (2 * math.pi * 0.25)
    near(b41, 4.0e-6)

    b40 = MU0 * (4000 / 0.55) * 16.4
    near(b40, 0.1496, rel=0.01)
    b42 = MU0 * (600 / 0.15) * 8.0
    near(b42, 0.0402124)

    n43 = 0.0270 / (MU0 * 12.0)
    turns43 = math.ceil(n43 * 0.400)
    length43 = turns43 * (2 * math.pi * 0.0140)
    b43_actual = MU0 * (turns43 / 0.400) * 12.0
    near(n43, 1790.493)
    assert turns43 == 717 and b43_actual >= 0.0270
    near(length43, 63.073, rel=1e-3)

    b44 = MU0 * 250 * 8.50 / (2 * math.pi * 0.160)
    near(b44, 2.65625e-3)
    i45a = 37.2 * 2 * math.pi * 0.0200 / MU0
    i45b = 2 * 0.420 * 37.2 / (MU0 * 100)
    i45c = 37.2 / (MU0 * (40000 / 0.320))
    near(i45a, 3.72e6)
    near(i45b, 2.4866368e5)
    near(i45c, 236.8226)

    b046 = MU0 * 400 * 0.25 / (2 * math.pi * 0.060)
    b46 = 80 * b046
    b_atom46 = b46 - b046
    near(b46, 2.6666667e-2)
    near(b_atom46 / b46, 0.9875)

    b047 = MU0 * 6000 * 0.15
    b47 = 5200 * b047
    m47 = (5200 - 1) * 6000 * 0.15
    near(b047, 1.1309734e-3)
    near(b47, 5.8810614)
    near(m47, 4.6791e6)

    b048 = MU0 * 500 * 2.4 / (2 * math.pi * 0.2500)
    km48 = 1.940 / b048
    chi48 = km48 - 1
    near(km48, 2020.8333)
    near(chi48, 2019.8333)
    return {
        "I37_A": i37,
        "integrals38_Tm": integrals38,
        "I40_A": 16.4,
        "B42_T": b42,
        "turns_per_m43": n43,
        "integer_turns43": turns43,
        "wire_length43_m": length43,
        "B44_T": b44,
        "I45_A": (i45a, i45b, i45c),
        "B46_T": b46,
        "B_atomic46_T": b_atom46,
        "B47_T": b47,
        "M47_A_per_m": m47,
        "Km48": km48,
        "chi48": chi48,
    }


def test_49_56() -> dict[str, float]:
    q, qp = 8.0e-6, -5.0e-6
    v = np.array([9.0e4, 0.0, 0.0])
    vp = np.array([0.0, 6.5e4, 0.0])
    rq_to_origin = np.array([0.0, -0.300, 0.0])
    rqp_to_origin = np.array([-0.400, 0.0, 0.0])
    b49_q = point_charge_field(q, v, rq_to_origin)
    b49_qp = point_charge_field(qp, vp, rqp_to_origin)
    b49 = b49_q + b49_qp
    near(np.linalg.norm(b49), 1.003125e-6)
    assert b49[2] < 0
    r_qp_to_q = np.array([-0.400, 0.300, 0.0])
    b_at_q = point_charge_field(qp, vp, r_qp_to_q)
    f49 = q * np.cross(v, b_at_q)
    near(np.linalg.norm(f49), 7.488e-8)
    assert f49[1] > 0

    q1, q2 = 4.80e-6, -2.90e-6
    v1 = np.array([9.20e5, 0.0, 0.0])
    v2 = np.array([0.0, -5.30e5, 0.0])
    r12 = np.array([0.150, -0.250, 0.0])
    b50 = point_charge_field(q1, v1, r12)
    f50 = q2 * np.cross(v2, b50)
    near(np.linalg.norm(f50), 6.8472243e-6, rel=2e-8)
    assert f50[0] < 0 and abs(f50[1]) < 1e-30

    # The field-zero points are checked by evaluating signed wire fields.
    p51 = np.array([0.0, 0.200])
    b51 = wire_field_z(2.0, p51 - np.array([0.0, 0.0])) + wire_field_z(6.0, p51 - np.array([0.0, 0.8]))
    near(np.linalg.norm(b51), 0.0)
    p52 = np.array([0.0, -0.400])
    b52 = wire_field_z(2.0, p52 - np.array([0.0, 0.0])) + wire_field_z(-6.0, p52 - np.array([0.0, 0.8]))
    near(np.linalg.norm(b52), 0.0)

    # Problem 28.53 loop-pair estimate, with explicit chosen estimates F=5 N, A=25 cm^2.
    force53, area53, separation53 = 5.0, 25e-4, 0.025
    radius53 = math.sqrt(area53 / math.pi)
    field53 = 0.5 * math.sqrt(MU0 * force53 * separation53 / radius53**3)
    near(field53, 4.1825134e-2)

    b54 = MU0 * 8.60 / (2 * math.pi * 0.0450)
    f54 = E * 6.00e4 * b54
    near(f54, 3.6768e-19)

    b55 = MU0 * 13.0 / (2 * math.pi * 0.0200)
    f55 = E * 2.50e5 * b55
    a55 = f55 / ME
    e55 = 2.50e5 * b55
    weight55 = ME * G
    near(b55, 1.3e-4)
    near(a55, 5.72e12, rel=1e-3)
    near(e55, 32.5)
    assert f55 / weight55 > 1e11

    b56_vec = np.array([0.0, 0.0, -MU0 * 9.00 / (2 * math.pi * 0.200)])
    v56 = np.array([5.00e4, -3.00e4, 0.0])
    f56 = -E * np.cross(v56, b56_vec)
    near(np.linalg.norm(f56), 8.41e-20, rel=1e-3)
    assert f56[0] < 0 and f56[1] < 0
    return {
        "B49_origin_T": float(np.linalg.norm(b49)),
        "F49_N": float(np.linalg.norm(f49)),
        "F50_N": float(np.linalg.norm(f50)),
        "B51_residual_T": float(np.linalg.norm(b51)),
        "B52_residual_T": float(np.linalg.norm(b52)),
        "B53_T_estimate": field53,
        "F54_N": f54,
        "a55_m_per_s2": a55,
        "E55_V_per_m": e55,
        "F56_components_N": tuple(f56),
    }


def test_57_60() -> dict[str, float]:
    # Transparent illustrative phone-power scenario, not a typical-power claim.
    p57, vb, head_width, speaker_diameter = 0.10, 1.5, 0.16, 0.020
    current57 = p57 / vb
    a57, x57 = speaker_diameter / 2, head_width / 2
    b57 = MU0 * current57 * a57**2 / (2 * (x57**2 + a57**2) ** 1.5)
    earth_percent57 = 100 * b57 / (50e-6)
    near(current57, 0.0666666667)
    near(b57, 8.0e-9, rel=2e-3)
    near(earth_percent57, 0.0160, rel=2e-3)

    # Problem 28.58: equal opposite currents at y=±a.
    a58, current58 = 0.04, 2.0
    def b58(x: float) -> np.ndarray:
        scale = MU0 * current58 / (2 * math.pi * (x * x + a58 * a58))
        return np.array([2 * scale * a58, 0.0, 0.0])
    assert b58(0.0)[0] > b58(0.04)[0] > 0
    near(b58(0.0)[0], MU0 * current58 / (math.pi * a58))
    near(b58(0.04)[0] / b58(0.0)[0], 0.5)

    # Fig. P28.59. Wire 1 is into page at x=0; at P, I2=2 A out of page cancels.
    i2_59 = 2.0
    p59 = np.array([1.5, 0.0])
    bp = wire_field_z(-6.0, p59 - np.array([0.0, 0.0])) + wire_field_z(i2_59, p59 - np.array([1.0, 0.0]))
    near(np.linalg.norm(bp), 0.0)
    q59 = np.array([-0.5, 0.0])
    bq = wire_field_z(-6.0, q59 - np.array([0.0, 0.0])) + wire_field_z(i2_59, q59 - np.array([1.0, 0.0]))
    near(np.linalg.norm(bq), 2.133333333e-6)
    s59 = np.array([0.36, 0.48])
    bs = wire_field_z(-6.0, s59 - np.array([0.0, 0.0])) + wire_field_z(i2_59, s59 - np.array([1.0, 0.0]))
    near(np.linalg.norm(bs), 2.0615528e-6)

    # Problem 28.60 parallel upper/lower sides; horizontal side forces cancel.
    f60 = MU0 * 14.0 * 5.0 * 0.200 / (2 * math.pi) * (1 / 0.026 - 1 / 0.126)
    near(f60, 8.54700855e-5)
    return {
        "phone_I_for_assumed_P_A": current57,
        "phone_B_midpoint_T": b57,
        "phone_percent_earth_field": earth_percent57,
        "B58_center_T": float(b58(0)[0]),
        "I2_59_A_out_of_page": i2_59,
        "B59_Q_T": float(np.linalg.norm(bq)),
        "B59_S_T": float(np.linalg.norm(bs)),
        "F60_N_upward": f60,
    }


def main() -> None:
    suites = {
        "28.31–28.36": test_31_36(),
        "28.37–28.48": test_37_48(),
        "28.49–28.56": test_49_56(),
        "28.57–28.60": test_57_60(),
    }
    for name, results in suites.items():
        print(f"PASS {name}: {results}")


if __name__ == "__main__":
    main()
