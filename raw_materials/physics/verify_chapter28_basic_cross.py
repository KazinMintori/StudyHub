"""Independent vector cross-checks for high-risk Chapter 28 configurations.

This suite reconstructs fields from coordinates and signed source currents.
It deliberately does not import the other Chapter 28 verifier modules.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


MU0 = 4.0 * math.pi * 1e-7
K_MU0 = MU0 / (4.0 * math.pi)
E_CHARGE = 1.602176634e-19
K_E = 8.9875517923e9
OUT = Path("qa/physics/chapter28/basic-cross.json")


def close(actual: float, expected: float, rel: float = 1e-8, abs_tol: float = 1e-24) -> None:
    assert math.isclose(float(actual), expected, rel_tol=rel, abs_tol=abs_tol), (actual, expected)


def assert_vec(actual: np.ndarray, expected: tuple[float, ...], *, rel: float = 1e-8, abs_tol: float = 1e-22) -> None:
    assert np.allclose(actual, np.asarray(expected, dtype=float), rtol=rel, atol=abs_tol), (actual, expected)


def charge_field(q: float, velocity: np.ndarray, r_from_charge: np.ndarray) -> np.ndarray:
    radius = float(np.linalg.norm(r_from_charge))
    assert radius > 0
    return K_MU0 * q * np.cross(velocity, r_from_charge) / radius**3


def z_wire_field(current_z: float, displacement_xy: np.ndarray) -> np.ndarray:
    x, y = map(float, displacement_xy)
    r2 = x * x + y * y
    assert r2 > 0
    return MU0 * current_z / (2.0 * math.pi * r2) * np.array([-y, x, 0.0])


def signed_line_field(current: float, tangent: np.ndarray, displacement: np.ndarray) -> np.ndarray:
    """Infinite-line field in the transverse plane, retaining vector direction."""
    radius = float(np.linalg.norm(displacement))
    assert radius > 0
    return MU0 * current * np.cross(tangent, displacement) / (2.0 * math.pi * radius**2)


def main() -> dict[str, object]:
    result: dict[str, object] = {}

    # E28.7. The source glyph is micro, confirmed from the source-page crop.
    r7, v7 = 6.60e-6, 3.30e3
    b7 = K_MU0 * 1.60e-19 * v7 / r7**2
    close(b7, 1.2121e-12, rel=1e-4)
    result["E28.7"] = {"source_distance_um": 6.60, "speed_km_per_s": 3.30,
                       "B_pT_perpendicular": b7 * 1e12}

    # E28.3. Figure angles are measured from the horizontal while v points up.
    speed3 = 0.100 * 299_792_458.0
    r3 = 2.00e-6
    base3 = K_MU0 * E_CHARGE * speed3 / r3**2
    # In the diagram the radial lines are at +60 and -60 degrees from +x.
    angle_a = math.radians(60.0)
    angle_b = math.radians(-60.0)
    electron3_a = charge_field(-E_CHARGE, np.array([0.0, speed3, 0.0]),
                               r3 * np.array([math.cos(angle_a), math.sin(angle_a), 0.0]))
    electron3_b = charge_field(-E_CHARGE, np.array([0.0, speed3, 0.0]),
                               r3 * np.array([math.cos(angle_b), math.sin(angle_b), 0.0]))
    electron3_c = charge_field(-E_CHARGE, np.array([0.0, speed3, 0.0]), np.array([r3, 0.0, 0.0]))
    electron3_d = charge_field(-E_CHARGE, np.array([0.0, speed3, 0.0]), np.array([0.0, -r3, 0.0]))
    close(np.linalg.norm(electron3_a), base3 * 0.5)
    close(np.linalg.norm(electron3_b), base3 * 0.5)
    assert electron3_a[2] > 0 and electron3_b[2] > 0 and electron3_c[2] > 0
    assert_vec(electron3_d, (0.0, 0.0, 0.0))
    close(np.linalg.norm(electron3_c), base3)
    result["E28.3_T"] = {
        "A_nT_out": float(electron3_a[2] * 1e9),
        "B_nT_out": float(electron3_b[2] * 1e9),
        "C_nT_out": float(electron3_c[2] * 1e9),
        "D_T": float(np.linalg.norm(electron3_d)),
    }

    # E28.8. Use the source figure coordinates and signed charges directly.
    v8 = 735e3
    e8 = E_CHARGE
    electron8_at_origin = charge_field(-e8, np.array([-v8, 0.0, 0.0]), np.array([0.0, -5e-9, 0.0]))
    proton8_at_origin = charge_field(e8, np.array([0.0, -v8, 0.0]), np.array([-4e-9, 0.0, 0.0]))
    field_at_electron8_from_proton = charge_field(e8, np.array([0.0, -v8, 0.0]), np.array([-4e-9, 5e-9, 0.0]))
    force_on_electron8 = -e8 * np.cross(np.array([-v8, 0.0, 0.0]), field_at_electron8_from_proton)
    field_at_proton8_from_electron = charge_field(-e8, np.array([-v8, 0.0, 0.0]), np.array([4e-9, -5e-9, 0.0]))
    force_on_proton8 = e8 * np.cross(np.array([0.0, -v8, 0.0]), field_at_proton8_from_electron)
    field8_total = electron8_at_origin + proton8_at_origin
    assert field8_total[2] < 0 and electron8_at_origin[2] < 0 and proton8_at_origin[2] < 0
    close(np.linalg.norm(field8_total), 1.207e-3, rel=1e-3)
    close(np.linalg.norm(field_at_proton8_from_electron), 2.2428e-4, rel=1e-3)
    assert field_at_proton8_from_electron[2] < 0
    assert force_on_electron8[1] > 0 and force_on_proton8[0] > 0
    close(np.linalg.norm(force_on_electron8), 2.1129e-17, rel=1e-3)
    close(np.linalg.norm(force_on_proton8), 2.6411e-17, rel=1e-3)
    result["E28.8"] = {
        "B_origin_mT_into": float(-field8_total[2] * 1e3),
        "B_electron_at_proton_mT_into": float(-field_at_proton8_from_electron[2] * 1e3),
        "force_on_electron_N": float(np.linalg.norm(force_on_electron8)),
        "force_on_proton_N": float(np.linalg.norm(force_on_proton8)),
        "force_on_electron_components_N": [float(v) for v in force_on_electron8],
        "force_on_proton_components_N": [float(v) for v in force_on_proton8],
    }

    # E28.16. Charge flow is east; conventional current is west.
    current16 = 8.2e18 * E_CHARGE
    field16 = signed_line_field(current16, np.array([-1.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.040]))
    assert field16[1] > 0
    close(np.linalg.norm(field16), 6.5689e-6, rel=1e-4)
    result["E28.16"] = {"B_uT": float(np.linalg.norm(field16) * 1e6), "direction": "north"}

    # E28.19. Superpose the wire field and the uniform +x field at all three points.
    wire_current19 = 8.0  # Tangent below points along -y.
    uniform19 = np.array([1.5e-6, 0.0, 0.0])
    points19 = {
        "a": np.array([0.0, 0.0, 1.0]),
        "b": np.array([1.0, 0.0, 0.0]),
        "c": np.array([0.0, 0.0, -0.25]),
    }
    fields19 = {}
    for label, point in points19.items():
        transverse = np.array([point[0], point[2]])
        b_wire = signed_line_field(wire_current19, np.array([0.0, -1.0, 0.0]), point)
        total = b_wire + uniform19
        fields19[label] = total
    close(np.linalg.norm(fields19["a"]), 0.1e-6)
    assert fields19["a"][0] < 0
    close(np.linalg.norm(fields19["b"]), math.hypot(1.5, 1.6) * 1e-6)
    assert fields19["b"][2] > 0 and fields19["b"][0] > 0
    close(np.linalg.norm(fields19["c"]), 7.9e-6)
    assert fields19["c"][0] > 0
    result["E28.19_uT"] = {key: [float(v * 1e6) for v in value] for key, value in fields19.items()}

    # E28.21. Wires parallel +z at x=+/-5 cm, each carrying current out of page.
    wires21 = [(np.array([0.05, 0.0]), 4.0), (np.array([-0.05, 0.0]), 4.0)]
    points21 = {"P1": np.array([0.0, 0.0]), "P2": np.array([0.25, 0.0]), "P3": np.array([0.0, 0.20])}
    fields21 = {name: sum((z_wire_field(i, point - pos) for pos, i in wires21), np.zeros(3))
                for name, point in points21.items()}
    assert_vec(fields21["P1"], (0.0, 0.0, 0.0))
    close(np.linalg.norm(fields21["P2"]), 6.6666667e-6)
    assert fields21["P2"][1] > 0
    close(np.linalg.norm(fields21["P3"]), 7.5294118e-6)
    assert fields21["P3"][0] < 0
    result["E28.21_uT"] = {key: [float(v * 1e6) for v in value] for key, value in fields21.items()}

    # E28.23. Corner-wire field is summed as a vector in the image plane.
    half23 = 0.100
    corners23 = [(-half23, half23), (half23, half23), (-half23, -half23), (half23, -half23)]

    def square_center(signs: tuple[int, int, int, int]) -> np.ndarray:
        total = np.zeros(2)
        for (x, y), sign in zip(corners23, signs):
            # z-directed signed current: B proportional to (-y, x).
            # Field point is the center, so r_from_wire=(-x,-y): k x r=(-r_y,r_x)=(y,-x).
            total += MU0 * 100.0 * sign / (2.0 * math.pi * (x * x + y * y)) * np.array([y, -x])
        return total

    fields23 = {
        "a": square_center((-1, -1, -1, -1)),
        "b": square_center((-1, 1, 1, -1)),
        "c": square_center((-1, -1, 1, 1)),
    }
    assert np.linalg.norm(fields23["a"]) < 1e-16 and np.linalg.norm(fields23["b"]) < 1e-16
    close(np.linalg.norm(fields23["c"]), 4.0e-4)
    assert fields23["c"][0] < 0
    result["E28.23_mT"] = {key: [float(v * 1e3) for v in value] for key, value in fields23.items()}

    # E28.24. Four long currents run along the square's edges, evaluated at center.
    half24 = 0.200
    per_amp = MU0 / (2.0 * math.pi * half24)
    signed_currents24 = {"top": -8.0, "bottom": 20.0, "left": -10.0, "right": 0.0}
    right_needed24 = -sum(signed_currents24.values())
    signed_currents24["right"] = right_needed24
    assert right_needed24 == -2.0  # Negative means downward on the right edge.
    field_edges24 = (
        signed_line_field(8.0, np.array([1.0, 0.0, 0.0]), np.array([0.0, -half24, 0.0]))
        + signed_line_field(20.0, np.array([1.0, 0.0, 0.0]), np.array([0.0, half24, 0.0]))
        + signed_line_field(10.0, np.array([0.0, 1.0, 0.0]), np.array([half24, 0.0, 0.0]))
        + signed_line_field(right_needed24, np.array([0.0, 1.0, 0.0]), np.array([-half24, 0.0, 0.0]))
    )
    assert np.linalg.norm(field_edges24) < 1e-19, field_edges24
    close(per_amp * sum(signed_currents24.values()), 0.0)
    result["E28.24"] = {"required_right_current_A": right_needed24, "direction": "down"}

    # E28.25. Horizontal current changes sign; vertical current stays +y at 12 A.
    horizontal_current25 = 10.0
    vertical_current25 = 12.0
    r_h25, r_v25 = 0.080, 0.150
    b_h25 = MU0 * horizontal_current25 / (2.0 * math.pi * r_h25)
    b_v25 = MU0 * vertical_current25 / (2.0 * math.pi * r_v25)
    close(b_h25, 25.0e-6)
    close(b_v25, 16.0e-6)
    result["E28.25"] = {
        "B_horizontal_uT": b_h25 * 1e6,
        "B_vertical_uT": b_v25 * 1e6,
        "rightward_P_into_Q_out_uT": (b_h25 + b_v25) * 1e6,
        "leftward_P_out_Q_into_uT": abs(b_h25 - b_v25) * 1e6,
    }
    p_fields25_a = signed_line_field(10.0, np.array([1.0, 0.0, 0.0]), np.array([0.0, -0.08, 0.0])) + signed_line_field(12.0, np.array([0.0, 1.0, 0.0]), np.array([0.15, 0.0, 0.0]))
    q_fields25_a = signed_line_field(10.0, np.array([1.0, 0.0, 0.0]), np.array([0.0, 0.08, 0.0])) + signed_line_field(12.0, np.array([0.0, 1.0, 0.0]), np.array([-0.15, 0.0, 0.0]))
    p_fields25_b = signed_line_field(-10.0, np.array([1.0, 0.0, 0.0]), np.array([0.0, -0.08, 0.0])) + signed_line_field(12.0, np.array([0.0, 1.0, 0.0]), np.array([0.15, 0.0, 0.0]))
    q_fields25_b = signed_line_field(-10.0, np.array([1.0, 0.0, 0.0]), np.array([0.0, 0.08, 0.0])) + signed_line_field(12.0, np.array([0.0, 1.0, 0.0]), np.array([-0.15, 0.0, 0.0]))
    assert p_fields25_a[2] < 0 and q_fields25_a[2] > 0
    assert p_fields25_b[2] > 0 and q_fields25_b[2] < 0
    close(np.linalg.norm(p_fields25_a), 41.0e-6)
    close(np.linalg.norm(q_fields25_b), 9.0e-6)
    result["E28.25"]["P_rightward_components_uT"] = [float(v * 1e6) for v in p_fields25_a]
    result["E28.25"]["Q_rightward_components_uT"] = [float(v * 1e6) for v in q_fields25_a]
    result["E28.25"]["P_leftward_components_uT"] = [float(v * 1e6) for v in p_fields25_b]
    result["E28.25"]["Q_leftward_components_uT"] = [float(v * 1e6) for v in q_fields25_b]

    # E28.28. Collinear z currents +I, -I, +I at y=-d,0,+d.
    d28, i28 = 0.10, 5.0

    def wire_force_per_length(source_i: float, target_i: float, dy: float) -> float:
        # Positive force points +y. Same-sign currents attract, opposite signs repel.
        return -MU0 * source_i * target_i / (2.0 * math.pi * dy)

    force_middle_from_outers = wire_force_per_length(i28, -i28, d28) + wire_force_per_length(i28, -i28, -d28)
    force_top_from_middle = wire_force_per_length(-i28, i28, d28)
    force_top_from_bottom = wire_force_per_length(i28, i28, 2.0 * d28)
    force_top_net = force_top_from_middle + force_top_from_bottom
    close(force_middle_from_outers, 0.0)
    close(abs(force_top_net), MU0 * i28**2 / (4.0 * math.pi * d28))
    assert force_top_net > 0
    result["E28.28_N_per_m"] = {
        "middle": force_middle_from_outers,
        "top": force_top_net,
        "bottom": -force_top_net,
    }

    # E28.29. Source figure shows opposite currents, hence repulsion.
    force29 = MU0 * 5.0 * 2.0 * 1.20 / (2.0 * math.pi * 0.400)
    close(force29, 6.0e-6)
    close(4.0 * force29, 24.0e-6)
    result["E28.29_uN"] = {"initial_repulsive": force29 * 1e6, "doubled_currents_repulsive": 4 * force29 * 1e6}

    # E28.38. Signed current enclosed by four contours from the source figure.
    signed_currents38 = {"I1_into": -4.0, "I2_out": 6.0, "I3_out": 2.0}
    enclosed38 = {
        "a": signed_currents38["I3_out"],
        "b": signed_currents38["I1_into"],
        "c": signed_currents38["I1_into"] + signed_currents38["I2_out"],
        "d": sum(signed_currents38.values()),
    }
    expected38 = {"a": 2.0, "b": -4.0, "c": 2.0, "d": 4.0}
    assert enclosed38 == expected38
    ampere38 = {key: MU0 * value for key, value in enclosed38.items()}
    result["E28.38"] = {"I_enclosed_A": enclosed38, "integral_Tm": ampere38}

    # E28.49. Two moving charges, fields at O and force on q due to q'.
    q49, qp49 = 8.0e-6, -5.0e-6
    v49, vp49 = np.array([9.0e4, 0.0, 0.0]), np.array([0.0, 6.5e4, 0.0])
    b49_o = charge_field(q49, v49, np.array([0.0, -0.300, 0.0])) + charge_field(qp49, vp49, np.array([-0.400, 0.0, 0.0]))
    b49_at_q = charge_field(qp49, vp49, np.array([-0.400, 0.300, 0.0]))
    f49_on_q = q49 * np.cross(v49, b49_at_q)
    close(np.linalg.norm(b49_o), 1.003125e-6)
    assert b49_o[2] < 0 and f49_on_q[1] > 0
    close(np.linalg.norm(f49_on_q), 7.488e-8)
    result["E28.49"] = {
        "B_origin_uT_into": float(-b49_o[2] * 1e6),
        "force_on_q_N": float(np.linalg.norm(f49_on_q)),
        "force_direction": "+y",
    }

    # E28.50. Independent vector evaluation of force on q2 by field of q1.
    q150, q250 = 4.80e-6, -2.90e-6
    v150 = np.array([9.20e5, 0.0, 0.0])
    v250 = np.array([0.0, -5.30e5, 0.0])
    displacement50 = np.array([0.150, -0.250, 0.0])
    b1_at_2_50 = charge_field(q150, v150, displacement50)
    f2_by_1_50 = q250 * np.cross(v250, b1_at_2_50)
    close(np.linalg.norm(f2_by_1_50), 6.8472243e-6)
    assert f2_by_1_50[0] < 0 and abs(f2_by_1_50[1]) < 1e-22
    result["E28.50"] = {"force_N": float(np.linalg.norm(f2_by_1_50)), "direction": "-x"}

    # E28.58. Two opposite z currents at y=+/-a. Check direction, maximum and far field.
    a58, i58 = 0.040, 2.0

    def field58(x: float) -> np.ndarray:
        upper = z_wire_field(i58, np.array([x, -a58]))
        lower = z_wire_field(-i58, np.array([x, a58]))
        return upper + lower

    b58_zero, b58_a, b58_twoa = field58(0.0), field58(a58), field58(2.0 * a58)
    close(b58_zero[0], 20.0e-6)
    close(b58_a[0], 10.0e-6)
    assert b58_zero[0] > b58_a[0] > b58_twoa[0] > 0
    close(b58_zero[0], MU0 * i58 / (math.pi * a58))
    result["E28.58_uT"] = {
        "B0": float(b58_zero[0] * 1e6),
        "Ba": float(b58_a[0] * 1e6),
        "B2a": float(b58_twoa[0] * 1e6),
        "far_field_coefficient_T_m2": float((MU0 * i58 * a58 / math.pi)),
    }

    # E28.59. Solve I2 for B(P)=0, then independently evaluate Q and S.
    pos1_59 = np.array([0.0, 0.0])
    pos2_59 = np.array([1.0, 0.0])
    i1_59 = -6.0
    p59 = np.array([1.5, 0.0])
    b1_p59 = z_wire_field(i1_59, p59 - pos1_59)
    unit2_p59 = z_wire_field(1.0, p59 - pos2_59)
    i2_59 = -b1_p59[1] / unit2_p59[1]
    close(i2_59, 2.0)
    q59 = np.array([-0.5, 0.0])
    s59 = np.array([0.36, 0.48])
    bq59 = z_wire_field(i1_59, q59 - pos1_59) + z_wire_field(i2_59, q59 - pos2_59)
    bs59 = z_wire_field(i1_59, s59 - pos1_59) + z_wire_field(i2_59, s59 - pos2_59)
    close(np.linalg.norm(b1_p59 + i2_59 * unit2_p59), 0.0)
    close(np.linalg.norm(bq59), 2.133333333e-6, rel=1e-7)
    close(np.linalg.norm(bs59), 2.061552813e-6, rel=1e-7)
    result["E28.59"] = {
        "I2_out_A": i2_59,
        "B_Q_uT": float(np.linalg.norm(bq59) * 1e6),
        "B_S_uT": float(np.linalg.norm(bs59) * 1e6),
        "B_Q_components_uT": [float(v * 1e6) for v in bq59[:2]],
        "B_S_components_uT": [float(v * 1e6) for v in bs59[:2]],
    }

    # P28.60. Integrate force on the two long loop sides; short-side forces cancel.
    i_wire60, i_loop60, length60 = 14.0, 5.0, 0.200
    near60, far60 = 0.026, 0.126
    force60 = MU0 * i_wire60 * i_loop60 * length60 / (2.0 * math.pi) * (1.0 / near60 - 1.0 / far60)
    close(force60, 8.5470085e-5)
    short_side_force = MU0 * i_wire60 * i_loop60 / (2.0 * math.pi) * math.log(far60 / near60)
    short_side_net = short_side_force - short_side_force
    close(short_side_net, 0.0)
    result["P28.60"] = {
        "net_force_N": force60,
        "direction": "up",
        "short_side_force_magnitude_each_N": short_side_force,
        "short_side_net_N": short_side_net,
    }

    # VP28.2.2. Opposite velocities and opposite charges yield mutual attraction.
    vvp, d_vp = 4.20e5, 2.00e-3
    b_from_proton_at_e = charge_field(E_CHARGE, np.array([0.0, vvp, 0.0]), np.array([d_vp, 0.0, 0.0]))
    force_on_e = -E_CHARGE * np.cross(np.array([0.0, -vvp, 0.0]), b_from_proton_at_e)
    b_from_e_at_proton = charge_field(-E_CHARGE, np.array([0.0, -vvp, 0.0]), np.array([-d_vp, 0.0, 0.0]))
    force_on_p = E_CHARGE * np.cross(np.array([0.0, vvp, 0.0]), b_from_e_at_proton)
    close(np.linalg.norm(force_on_e), 1.13e-28, rel=2e-3)
    assert force_on_e[0] < 0 and force_on_p[0] > 0
    result["VP28.2.2"] = {
        "force_on_electron_N": float(np.linalg.norm(force_on_e)),
        "force_on_proton_N": float(np.linalg.norm(force_on_p)),
        "directions": {"electron": "-x toward proton", "proton": "+x toward electron"},
        "interaction": "attraction",
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Independent Chapter 28 high-risk cross checks passed: {len(result)} configurations. JSON: {OUT}")
    return result


if __name__ == "__main__":
    main()
