"""Verifier for Chapter 17 Theory B (Sections 17.5, 17.6, 17.7, Summary 17)."""
import json
import math
from pathlib import Path
import numpy as np

def close(a, b, rtol=1e-4, atol=1e-6):
    assert np.allclose(a, b, rtol=rtol, atol=atol), f"Mismatch: {a} vs {b}"

results = {}

# --- Section 17.5: Units and Mechanical Equivalent of Heat ---
cal_to_J = 4.186
kcal_to_J = 4186.0
btu_to_J = 1055.0
close(1.0 * cal_to_J, 4.186)
close(1000.0 * cal_to_J, 4186.0)
results["mechanical_equivalent"] = {
    "1_cal_J": cal_to_J,
    "1_kcal_J": kcal_to_J,
    "1_btu_J": btu_to_J,
}

# --- Example 17.5: Feed a cold, starve a fever ---
m_man = 80.0
c_water = 4190.0
delta_T_fever = 2.0  # 39.0 - 37.0
Q_water_model = m_man * c_water * delta_T_fever
Q_water_kcal = Q_water_model / kcal_to_J
close(Q_water_model, 6.704e5, rtol=1e-2)
close(Q_water_kcal, 160.15, rtol=1e-2)

c_body = 3480.0
Q_body_model = m_man * c_body * delta_T_fever
Q_body_kcal = Q_body_model / kcal_to_J
close(Q_body_model, 5.568e5, rtol=1e-2)
close(Q_body_kcal, 133.0, rtol=1e-2)

results["example17.5"] = {
    "Q_water_J": Q_water_model,
    "Q_water_kcal": Q_water_kcal,
    "Q_body_J": Q_body_model,
    "Q_body_kcal": Q_body_kcal,
}

# --- Example 17.6: Overheating electronics ---
m_si = 23e-6  # 23 mg
rate_dQ_dt = 7.4e-3  # 7.4 mW
c_si = 705.0
dT_dt_s = rate_dQ_dt / (m_si * c_si)
dT_dt_min = dT_dt_s * 60.0
close(dT_dt_s, 0.456368, rtol=1e-2)
close(dT_dt_min, 27.38, rtol=1e-2)

results["example17.6"] = {
    "dT_dt_K_per_s": dT_dt_s,
    "dT_dt_K_per_min": dT_dt_min,
}

# --- Section 17.5 Molar Heat Capacity for water ---
M_water = 0.0180  # kg/mol
C_water = M_water * c_water
close(C_water, 75.42, rtol=1e-2)
results["molar_heat_capacity_water"] = {
    "C_water_J_mol_K": C_water,
}

# --- Test Your Understanding 17.5 ---
# Heat to raise 1 K:
# (i) 1 kg mercury: c = 138 J/(kg*K) -> 138 J
# (ii) 1 kg ethanol: c = 2428 J/(kg*K) -> 2428 J
# (iii) 1 mole mercury: C = 27.7 J/(mol*K) -> 27.7 J
# (iv) 1 mole ethanol: C = 111.9 J/(mol*K) -> 111.9 J
Q_tyu5 = {
    "i_mercury_1kg": 1.0 * 138.0 * 1.0,
    "ii_ethanol_1kg": 1.0 * 2428.0 * 1.0,
    "iii_mercury_1mol": 1.0 * 27.7 * 1.0,
    "iv_ethanol_1mol": 1.0 * 111.9 * 1.0,
}
assert Q_tyu5["ii_ethanol_1kg"] > Q_tyu5["i_mercury_1kg"] > Q_tyu5["iv_ethanol_1mol"] > Q_tyu5["iii_mercury_1mol"]
results["test_understanding_17.5"] = {
    "quantities_J": Q_tyu5,
    "ranking": ["ii", "i", "iv", "iii"],
}

# --- Section 17.6 Phase Transitions ---
L_f_water = 3.34e5
L_v_water = 2.256e6
Q_warm_1kg_0_100 = 1.0 * c_water * 100.0
close(Q_warm_1kg_0_100, 4.19e5)
close(L_v_water / Q_warm_1kg_0_100, 2256000.0 / 419000.0, rtol=1e-3)
results["phase_transition_comparison"] = {
    "Q_warm_100C_J": Q_warm_1kg_0_100,
    "L_v_water_J_per_kg": L_v_water,
    "ratio_Lv_to_Qwarm": L_v_water / Q_warm_1kg_0_100,
}

# --- Example 17.7: Coffee in aluminum cup ---
m_coffee = 0.300
T0_coffee = 70.0
m_cup = 0.120
c_cup = 910.0
T0_cup = 20.0
T_eq_17_7 = (m_coffee * c_water * T0_coffee + m_cup * c_cup * T0_cup) / (m_coffee * c_water + m_cup * c_cup)
close(T_eq_17_7, 66.0035, rtol=1e-2)
Q_coffee_lost = m_coffee * c_water * (T_eq_17_7 - T0_coffee)
Q_cup_gained = m_cup * c_cup * (T_eq_17_7 - T0_cup)
close(abs(Q_coffee_lost), 5023.6, rtol=1e-2)
close(Q_cup_gained, 5023.6, rtol=1e-2)
results["example17.7"] = {
    "T_final_C": T_eq_17_7,
    "Q_coffee_J": Q_coffee_lost,
    "Q_cup_J": Q_cup_gained,
}

# --- Example 17.8: Omni-Cola and ice ---
m_cola = 0.25
T0_cola = 25.0
T0_ice = -20.0
c_ice = 2100.0
m_ice = (m_cola * c_water * (T0_cola - 0.0)) / (c_ice * (0.0 - T0_ice) + L_f_water)
close(m_ice, 0.0696476, rtol=1e-2)
results["example17.8"] = {
    "m_ice_kg": m_ice,
    "m_ice_g": m_ice * 1000.0,
}

# --- Example 17.9: What's cooking? ---
m_pot = 2.0
c_cu = 390.0
T0_pot = 150.0
m_w9 = 0.10
T0_w9 = 25.0
# Case 1 contradiction
T_case1 = (m_w9 * c_water * T0_w9 + m_pot * c_cu * T0_pot) / (m_w9 * c_water + m_pot * c_cu)
assert T_case1 > 100.0
close(T_case1, 106.318, rtol=1e-2)
# Case 2 fraction x vaporized at 100 C
x_vap = (-m_pot * c_cu * (100.0 - T0_pot) - m_w9 * c_water * (100.0 - T0_w9)) / (m_w9 * L_v_water)
close(x_vap, 0.033577, rtol=1e-2)
m_steam = x_vap * m_w9
close(m_steam, 0.003358, rtol=1e-2)
# Threshold for all water to vaporize (Case 3)
m_w_threshold = (-m_pot * c_cu * (100.0 - T0_pot)) / (c_water * (100.0 - T0_w9) + L_v_water)
close(m_w_threshold, 0.0151736, rtol=1e-2)
results["example17.9"] = {
    "T_case1_contradiction_C": T_case1,
    "fraction_steam": x_vap,
    "m_steam_g": m_steam * 1000.0,
    "threshold_all_vaporize_g": m_w_threshold * 1000.0,
}

# --- Example 17.10: Camp stove combustion ---
m_w10 = 1.00
delta_T_w10 = 80.0  # 100 - 20
m_boiled = 0.25
Q1_warm = m_w10 * c_water * delta_T_w10
Q2_boil = m_boiled * L_v_water
Q_total_10 = Q1_warm + Q2_boil
close(Q1_warm, 3.352e5, rtol=1e-2)
close(Q2_boil, 5.64e5, rtol=1e-2)
close(Q_total_10, 8.992e5, rtol=1e-2)
efficiency = 0.30
Q_combustion_needed = Q_total_10 / efficiency
close(Q_combustion_needed, 2.99733e6, rtol=1e-2)
L_c_gasoline = 46000.0  # J/g
m_gas_g = Q_combustion_needed / L_c_gasoline
close(m_gas_g, 65.159, rtol=1e-2)
# Additional gasoline to boil remaining 0.75 kg
m_remaining = 0.75
Q_boil_rem = m_remaining * L_v_water
m_gas_rem_g = (Q_boil_rem / efficiency) / L_c_gasoline
close(m_gas_rem_g, 122.608, rtol=1e-2)
results["example17.10"] = {
    "Q1_warm_J": Q1_warm,
    "Q2_boil_J": Q2_boil,
    "Q_total_J": Q_total_10,
    "m_gasoline_g": m_gas_g,
    "m_gasoline_additional_g": m_gas_rem_g,
}

# --- Test Your Understanding 17.6 ---
# Fraction of heat added at t/2
# Q_melt = 3.34e5 * m, Q_warm = 4.19e5 * m, Q_boil = 22.56e5 * m
Q_tot_unit = 3.34e5 + 4.19e5 + 2.256e6
Q_half = Q_tot_unit / 2.0
assert Q_half > (3.34e5 + 4.19e5)  # Reached 100 C
assert Q_half < Q_tot_unit          # Still boiling
results["test_understanding_17.6"] = {
    "Q_half_vs_warm": Q_half - (3.34e5 + 4.19e5),
    "fraction_boiled_at_t_over_2": (Q_half - (3.34e5 + 4.19e5)) / 2.256e6,
    "correct_option": "iv",
}

# --- Section 17.7: Conduction ---
# Bio Application: Fox fur vs Whale blubber
k_fur = 0.04
k_blubber = 0.24
L_fur = 0.01  # 1 cm
L_blubber = L_fur * (k_blubber / k_fur)
close(L_blubber, 0.06)
results["bio_application_fur_blubber"] = {
    "k_fur": k_fur,
    "k_blubber": k_blubber,
    "L_blubber_cm": L_blubber * 100.0,
}

# Example 17.11: Styrofoam cooler
A_cooler = 0.80
L_cooler = 0.020
k_styrofoam = 0.027
delta_T_cooler = 30.0
H_cooler = k_styrofoam * A_cooler * delta_T_cooler / L_cooler
close(H_cooler, 32.4)
t_cooler = 3.0 * 3600.0
Q_cooler = H_cooler * t_cooler
m_ice_melted_11 = Q_cooler / L_f_water
close(m_ice_melted_11, 1.04766, rtol=1e-2)
results["example17.11"] = {
    "H_W": H_cooler,
    "m_ice_melted_kg": m_ice_melted_11,
}

# Example 17.12: Two bars in series
L_steel = 0.100
k_steel = 50.2
L_copper = 0.200
k_copper = 385.0
side_bar = 0.0200
A_bar = side_bar ** 2
T_H_12 = 100.0
T_C_12 = 0.0
T_junction = (k_steel / L_steel * T_H_12 + k_copper / L_copper * T_C_12) / (k_steel / L_steel + k_copper / L_copper)
close(T_junction, 20.684, rtol=1e-2)
H_series_steel = k_steel * A_bar * (T_H_12 - T_junction) / L_steel
H_series_cu = k_copper * A_bar * (T_junction - T_C_12) / L_copper
close(H_series_steel, 15.926, rtol=1e-2)
close(H_series_cu, 15.926, rtol=1e-2)
results["example17.12"] = {
    "T_junction_C": T_junction,
    "H_W": H_series_steel,
}

# Example 17.13: Two bars in parallel
H_par_steel = k_steel * A_bar * (100.0 - 0.0) / L_steel
H_par_cu = k_copper * A_bar * (100.0 - 0.0) / L_copper
H_par_total = H_par_steel + H_par_cu
close(H_par_steel, 20.08, rtol=1e-2)
close(H_par_cu, 77.0, rtol=1e-2)
close(H_par_total, 97.08, rtol=1e-2)
results["example17.13"] = {
    "H_steel_W": H_par_steel,
    "H_copper_W": H_par_cu,
    "H_total_W": H_par_total,
}

# Example 17.14: Radiation from square plate
sigma = 5.67037442e-8
sigma_text = 5.67e-8
A_plate = 2.0 * (0.10 ** 2)
T_plate_K = 1073.0  # 800 C
e_plate = 0.60
H_plate = A_plate * e_plate * sigma_text * (T_plate_K ** 4)
close(H_plate, 899.70, rtol=1e-2)
results["example17.14"] = {
    "H_radiation_W": H_plate,
}

# Example 17.15: Radiation from human body
A_body = 1.20
T_body_K = 303.0  # 30 C
T_surr_K = 293.0  # 20 C
e_body = 1.0
H_emit_body = A_body * e_body * sigma_text * (T_body_K ** 4)
H_net_body = A_body * e_body * sigma_text * (T_body_K ** 4 - T_surr_K ** 4)
close(H_emit_body, 574.07, rtol=1e-2)
close(H_net_body, 72.31, rtol=1e-2)
results["example17.15"] = {
    "H_emit_W": H_emit_body,
    "H_net_W": H_net_body,
}

# Test Your Understanding 17.7:
k_concrete = 0.8
assert k_copper > k_steel > k_concrete
results["test_understanding_17.7"] = {
    "k_values": {"copper": k_copper, "steel": k_steel, "concrete": k_concrete},
    "coldest_to_touch": "ii_copper",
}

# --- Verify image files and fresh PDF RGB pixel comparison ---
import pymupdf
from PIL import Image

source_pdf = Path("raw_materials/physics/source/young-freedman-15.pdf")
if not source_pdf.is_file():
    source_pdf = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")

crops_spec = {
    "b-hinh-17-15": (572, (33.0, 103.0, 192.0, 448.0)),
    "b-hinh-17-16": (572, (34.0, 558.0, 194.0, 683.0)),
    "b-hinh-17-17": (573, (465.0, 213.0, 602.0, 330.0)),
    "b-hinh-17-18": (574, (32.0, 373.0, 194.0, 521.0)),
    "b-hinh-17-19": (576, (33.0, 154.0, 194.0, 292.0)),
    "b-hinh-17-20": (577, (76.0, 95.0, 485.0, 280.0)),
    "b-hinh-17-21": (577, (453.0, 428.0, 617.0, 579.0)),
    "b-hinh-17-22": (578, (33.0, 156.0, 194.0, 353.0)),
    "b-hinh-17-23": (578, (33.0, 522.0, 194.0, 631.0)),
    "b-hinh-17-24": (581, (455.0, 85.0, 610.0, 340.0)),
    "b-ung-dung-17-01": (582, (27.0, 193.0, 195.0, 369.0)),
    "b-hinh-17-25": (583, (85.0, 220.0, 332.0, 353.0)),
    "b-hinh-17-26": (583, (75.0, 638.0, 341.0, 731.0)),
    "b-hinh-17-27": (584, (74.0, 197.0, 214.0, 327.0)),
    "b-hinh-17-28": (584, (33.0, 455.0, 194.0, 662.0)),
    "b-hinh-17-29": (585, (453.0, 225.0, 614.0, 348.0)),
    "b-hinh-17-30": (587, (75.0, 538.0, 588.0, 732.0)),
    "b-tom-tat-01": (588, (447.0, 87.0, 577.0, 207.0)),
    "b-tom-tat-02": (588, (447.0, 242.0, 577.0, 307.0)),
    "b-tom-tat-03": (588, (447.0, 377.0, 577.0, 487.0)),
    "b-tom-tat-04": (588, (447.0, 562.0, 577.0, 652.0)),
}

img_dir = Path("docs/vat-ly-1/bai-giang/img/young-17")
expected_stems = list(crops_spec.keys())
missing_imgs = [stem for stem in expected_stems if not (img_dir / f"{stem}.png").is_file()]
assert not missing_imgs, f"Missing image files: {missing_imgs}"

rgb_verified_count = 0
if source_pdf.is_file():
    with pymupdf.open(source_pdf) as doc:
        for name, (p, box) in crops_spec.items():
            page = doc[p - 1]
            rect = pymupdf.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=pymupdf.Matrix(3.0, 3.0), clip=rect, alpha=False)
            img_disk = Image.open(img_dir / f"{name}.png").convert("RGB")
            arr_disk = np.array(img_disk)
            arr_fresh = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, 3))
            assert arr_disk.shape == arr_fresh.shape, f"Shape mismatch in {name}"
            diff = int(np.max(np.abs(arr_disk.astype(int) - arr_fresh.astype(int))))
            assert diff == 0, f"Pixel difference in {name}: max diff={diff}"
            rgb_verified_count += 1

results["image_assets"] = {
    "count": len(expected_stems),
    "all_present": True,
    "rgb_verified_against_pdf_crops": rgb_verified_count,
}

# --- Verify 4 Owned Markdown Files Exist ---
md_files = [
    Path("raw_materials/physics/translations/chapter-17/05-nhiet-luong.md"),
    Path("raw_materials/physics/translations/chapter-17/06-nhiet-luong-ke-va-chuyen-pha.md"),
    Path("raw_materials/physics/translations/chapter-17/07-cac-co-che-truyen-nhiet.md"),
    Path("raw_materials/physics/translations/chapter-17/17-tom-tat.md"),
]
missing_mds = [str(p) for p in md_files if not p.is_file()]
assert not missing_mds, f"Missing markdown files: {missing_mds}"
results["owned_markdown_files"] = {
    "count": len(md_files),
    "all_present": True,
}

print(json.dumps({"status": "passed", "results": results}, indent=2, ensure_ascii=False))
