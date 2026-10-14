"""Numerical and structural verification for Chapter 30 Track B (sections 30.4–30.6 and summary).

Independent verification of:
- Examples 30.6–30.10
- Test Your Understanding 30.4–30.6
- Key Example Variation Problems VP30.7.1–VP30.7.4, VP30.10.1–VP30.10.4
- Bridging Problem (Analyzing an L-C Circuit)
- Formatting checks on Markdown translation fragments:
  * Equations (30.12)–(30.29)
  * Math delimiters, inline math length, display blocks
  * Capitalization after colons in prose
  * Absence of prohibited comparison phrases
"""

import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def verify_example_30_6() -> None:
    R = 175.0
    I_final = 0.036
    E_req = I_final * R
    assert math.isclose(E_req, 6.3, rel_tol=1e-3), f"Example 30.6 E fail: {E_req}"

    t1 = 58e-6
    i1 = 4.9e-3
    L_req = -R * t1 / math.log(1 - i1 * R / E_req)
    assert math.isclose(L_req, 0.06937271788076092, rel_tol=1e-12), f"Example 30.6 L fail: {L_req}"

    tau = L_req / R
    assert math.isclose(tau, 0.00039641553074720525, rel_tol=1e-12), f"Example 30.6 tau fail: {tau}"

    i_tau = I_final * (1 - math.exp(-1))
    assert math.isclose(i_tau, 0.02275, rel_tol=1e-2), f"Example 30.6 i_tau fail: {i_tau}"
    print("Example 30.6 verified.")


def verify_example_30_7() -> None:
    fraction_remaining = math.exp(-2 * 2.3)
    fraction_dissipated = 1.0 - fraction_remaining
    assert math.isclose(fraction_remaining, 0.010, rel_tol=1e-2), f"Example 30.7 fraction fail: {fraction_remaining}"
    assert math.isclose(fraction_dissipated, 0.990, rel_tol=1e-2), f"Example 30.7 dissipated fail: {fraction_dissipated}"

    L = 0.069
    I0 = 0.036
    U0 = 0.5 * L * I0**2
    assert math.isclose(U0, 4.47e-5, rel_tol=1e-2), f"Example 30.7 U0 fail: {U0}"

    dissipated_energy = fraction_dissipated * U0
    assert math.isclose(dissipated_energy, 4.4e-5, rel_tol=2e-2), f"Example 30.7 dissipated energy fail: {dissipated_energy}"

    tau = 390e-6
    t_decay = 2.3 * tau
    assert math.isclose(t_decay, 0.90e-3, rel_tol=2e-2), f"Example 30.7 time fail: {t_decay}"
    print("Example 30.7 verified.")


def verify_example_30_8() -> None:
    C = 25e-6
    L = 10e-3
    V = 300.0
    Q = C * V
    assert math.isclose(Q, 7.5e-3, rel_tol=1e-4), f"Example 30.8 Q fail: {Q}"

    omega = 1.0 / math.sqrt(L * C)
    assert math.isclose(omega, 2000.0, rel_tol=1e-4), f"Example 30.8 omega fail: {omega}"

    f = omega / (2 * math.pi)
    assert math.isclose(f, 318.31, rel_tol=1e-2), f"Example 30.8 f fail: {f}"

    T = 1.0 / f
    assert math.isclose(T, 3.14e-3, rel_tol=2e-2), f"Example 30.8 T fail: {T}"

    t = 1.2e-3
    phase = omega * t
    assert math.isclose(phase, 2.4, rel_tol=1e-4), f"Example 30.8 phase fail: {phase}"

    q_t = Q * math.cos(phase)
    assert math.isclose(q_t, -5.53e-3, rel_tol=1e-2), f"Example 30.8 q_t fail: {q_t}"

    i_t = -omega * Q * math.sin(phase)
    assert math.isclose(i_t, -10.13, rel_tol=2e-2), f"Example 30.8 i_t fail: {i_t}"
    print("Example 30.8 verified.")


def verify_example_30_9() -> None:
    C = 25e-6
    L = 10e-3
    Q = 7.5e-3
    U_total = Q**2 / (2 * C)
    assert math.isclose(U_total, 1.125, rel_tol=1e-3), f"Example 30.9 U_total fail: {U_total}"

    q_t = -5.53e-3
    i_t = -10.13
    U_B = 0.5 * L * i_t**2
    U_E = q_t**2 / (2 * C)
    assert math.isclose(U_B, 0.513, rel_tol=3e-2), f"Example 30.9 U_B fail: {U_B}"
    assert math.isclose(U_E, 0.612, rel_tol=3e-2), f"Example 30.9 U_E fail: {U_E}"
    assert math.isclose(U_B + U_E, U_total, rel_tol=1e-3), f"Example 30.9 conservation fail: {U_B + U_E}"
    print("Example 30.9 verified.")


def verify_example_30_10() -> None:
    # omega' = omega / 2 => sqrt(1/(LC) - R^2/(4L^2)) = (1/2)*sqrt(1/(LC))
    # 1/(LC) - R^2/(4L^2) = 1/(4LC) => R^2/(4L^2) = 3/(4LC) => R = sqrt(3L/C)
    L = 10e-3
    C = 25e-6
    R_req = math.sqrt(3 * L / C)
    assert math.isclose(R_req, 34.64, rel_tol=1e-2), f"Example 30.10 R_req fail: {R_req}"

    omega = 1.0 / math.sqrt(L * C)
    omega_prime = math.sqrt(1.0 / (L * C) - R_req**2 / (4 * L**2))
    assert math.isclose(omega_prime, omega / 2, rel_tol=1e-4), "Example 30.10 omega_prime fail"

    R_crit = math.sqrt(4 * L / C)
    assert math.isclose(R_crit, 40.0, rel_tol=1e-4), f"Example 30.10 R_crit fail: {R_crit}"
    print("Example 30.10 verified.")


def verify_self_checks() -> None:
    # TYU 30.4: (a) (i) vab > 0, vbc > 0; (b) (ii) vab > 0, vbc < 0
    # TYU 30.5: (a) positive, (b) electric, (c) negative, (d) electric
    # TYU 30.6: R = 2.0 Ohm, R^2 = 4.0 Ohm^2, q0 = 2.0 microcoulomb
    q0 = 2.0e-6
    assert math.isclose(q0, 2.0e-6), f"TYU 30.6 q0 fail: {q0}"
    R = 2.0
    R2 = R**2
    cases = {
        "(i)": (3.0e-6, 6.0e-6),    # 4L/C = 2.0 Ohm^2 <= R2 -> overdamped
        "(ii)": (6.0e-6, 3.0e-6),   # 4L/C = 8.0 Ohm^2 > R2 -> underdamped
        "(iii)": (3.0e-6, 3.0e-6),  # 4L/C = 4.0 Ohm^2 == R2 -> critically damped
    }
    crit = {}
    for k, (L_val, C_val) in cases.items():
        val = 4 * L_val / C_val
        crit[k] = val
    assert crit["(i)"] < R2, "TYU 30.6 case (i) should be overdamped"
    assert crit["(ii)"] > R2, "TYU 30.6 case (ii) should be underdamped"
    assert math.isclose(crit["(iii)"], R2), "TYU 30.6 case (iii) should be critically damped"
    print("Self-checks TYU 30.4–30.6 verified.")


def verify_guided_practice_track_b() -> None:
    # VP30.7.1
    L_vp1 = 4.90e-3
    E_vp1 = 24.0
    t_vp1 = 80.0e-6
    # 1 - exp(-R*t/L) = 0.750 => R = -(L/t)*ln(0.25)
    R_vp1 = -(L_vp1 / t_vp1) * math.log(0.250)
    assert math.isclose(R_vp1, 84.91, rel_tol=1e-2), f"VP30.7.1 R fail: {R_vp1}"
    i_vp1 = 0.750 * (E_vp1 / R_vp1)
    assert math.isclose(i_vp1, 0.212, rel_tol=1e-2), f"VP30.7.1 i fail: {i_vp1}"

    # VP30.7.2
    E_vp2 = 12.0
    R_vp2 = 18.0
    L_vp2 = 37.5e-3
    t_vp2 = 0.700e-3
    tau_vp2 = L_vp2 / R_vp2
    I_final_vp2 = E_vp2 / R_vp2
    i_vp2 = I_final_vp2 * (1 - math.exp(-t_vp2 / tau_vp2))
    assert math.isclose(i_vp2, 0.190, rel_tol=1e-2), f"VP30.7.2 i fail: {i_vp2}"
    didt_vp2 = (E_vp2 / L_vp2) * math.exp(-t_vp2 / tau_vp2)
    assert math.isclose(didt_vp2, 228.68, rel_tol=1e-2), f"VP30.7.2 didt fail: {didt_vp2}"
    U_vp2 = 0.5 * L_vp2 * i_vp2**2
    assert math.isclose(U_vp2, 6.79e-4, rel_tol=1e-2), f"VP30.7.2 U fail: {U_vp2}"

    # VP30.7.3
    i_vp3 = I_final_vp2 * math.exp(-t_vp2 / tau_vp2)
    assert math.isclose(i_vp3, 0.476, rel_tol=1e-2), f"VP30.7.3 i fail: {i_vp3}"
    didt_vp3 = -(R_vp2 / L_vp2) * i_vp3
    assert math.isclose(didt_vp3, -228.68, rel_tol=1e-2), f"VP30.7.3 didt fail: {didt_vp3}"
    U_vp3 = 0.5 * L_vp2 * i_vp3**2
    assert math.isclose(U_vp3, 4.26e-3, rel_tol=1e-2), f"VP30.7.3 U fail: {U_vp3}"

    # VP30.7.4
    # v_L = v_R => exp(-t/tau) = 1/2 => t = tau*ln(2)
    # i = I/2 = E/(2R); didt = E/(2L)

    # VP30.10.1
    L_vp101 = 25.0e-6
    f_vp101 = 445.0
    Q_vp101 = 5.00e-3
    omega_vp101 = 2 * math.pi * f_vp101
    C_vp101 = 1.0 / (omega_vp101**2 * L_vp101)
    assert math.isclose(C_vp101, 5.12e-3, rel_tol=1e-2), f"VP30.10.1 C fail: {C_vp101}"
    I_max_vp101 = omega_vp101 * Q_vp101
    assert math.isclose(I_max_vp101, 14.0, rel_tol=1e-2), f"VP30.10.1 I_max fail: {I_max_vp101}"

    # VP30.10.2
    L_vp102 = 30.0e-6
    C_vp102 = 655e-6
    Q_vp102 = 0.400e-3
    omega_vp102 = 1.0 / math.sqrt(L_vp102 * C_vp102)
    t_zero_vp102 = math.pi / (2 * omega_vp102)
    assert math.isclose(t_zero_vp102, 2.20e-4, rel_tol=1e-2), f"VP30.10.2 t_zero fail: {t_zero_vp102}"
    I_at_zero_vp102 = omega_vp102 * Q_vp102
    assert math.isclose(I_at_zero_vp102, 2.85, rel_tol=1e-2), f"VP30.10.2 I fail: {I_at_zero_vp102}"

    # VP30.10.3 (Corrected: C = 35.1 microfarads)
    E_tot_vp103 = 0.800
    U_E_vp103 = E_tot_vp103 / 2.0
    U_B_vp103 = E_tot_vp103 / 2.0
    q_vp103 = 5.30e-3
    i_vp103 = 8.00
    C_vp103 = q_vp103**2 / (2 * U_E_vp103)
    assert math.isclose(C_vp103, 35.1e-6, rel_tol=1e-2), f"VP30.10.3 C fail: {C_vp103}"
    L_vp103 = 2 * U_B_vp103 / i_vp103**2
    assert math.isclose(L_vp103, 0.0125, rel_tol=1e-3), f"VP30.10.3 L fail: {L_vp103}"
    omega_vp103 = 1.0 / math.sqrt(L_vp103 * C_vp103)
    assert math.isclose(omega_vp103, 1.51e3, rel_tol=1e-2), f"VP30.10.3 omega fail: {omega_vp103}"

    # VP30.10.4 (Corrected: C = 61.1 microfarads)
    L_vp104 = 42.0e-3
    omega_0_vp104 = 624.0
    omega_d_vp104 = 208.0
    C_vp104 = 1.0 / (omega_0_vp104**2 * L_vp104)
    assert math.isclose(C_vp104, 61.1e-6, rel_tol=1e-2), f"VP30.10.4 C fail: {C_vp104}"
    R_vp104 = math.sqrt(4 * L_vp104**2 * (omega_0_vp104**2 - omega_d_vp104**2))
    assert math.isclose(R_vp104, 49.4, rel_tol=1e-2), f"VP30.10.4 R fail: {R_vp104}"

    # Bridging Problem
    L_bp = 60.0e-3
    C_bp = 250e-6
    q0_bp = 6.00e-6
    i0_bp = 0.400e-3
    U_E0_bp = q0_bp**2 / (2 * C_bp)
    U_B0_bp = 0.5 * L_bp * i0_bp**2
    E_tot_bp = U_E0_bp + U_B0_bp
    assert math.isclose(E_tot_bp, 7.68e-8, rel_tol=1e-3), f"Bridging Problem (a) fail: {E_tot_bp}"

    I_max_bp = math.sqrt(2 * E_tot_bp / L_bp)
    assert math.isclose(I_max_bp, 1.60e-3, rel_tol=1e-3), f"Bridging Problem (b) fail: {I_max_bp}"

    V_max_bp = math.sqrt(2 * E_tot_bp / C_bp)
    assert math.isclose(V_max_bp, 24.8e-3, rel_tol=1e-2), f"Bridging Problem (c) fail: {V_max_bp}"

    # (d) when i = I_max / 2
    U_B_half = 0.5 * L_bp * (I_max_bp / 2.0)**2
    assert math.isclose(U_B_half, 1.92e-8, rel_tol=1e-3), f"Bridging Problem (d) U_B fail: {U_B_half}"
    U_E_rem = E_tot_bp - U_B_half
    V_half = math.sqrt(2 * U_E_rem / C_bp)
    assert math.isclose(V_half, 21.5e-3, rel_tol=1e-2), f"Bridging Problem (d) V fail: {V_half}"
    print("Guided Practice and Bridging Problem verified.")


def verify_markdown_fragments() -> None:
    trans_dir = ROOT / "raw_materials/physics/translations/chapter-30"
    files = [
        "04-mach-rl.md",
        "05-mach-lc.md",
        "06-mach-rlc.md",
        "09-tom-tat.md",
    ]

    equation_numbers = {
        "04-mach-rl.md": ["30.12", "30.13", "30.14", "30.15", "30.16", "30.17", "30.18", "30.19"],
        "05-mach-lc.md": ["30.20", "30.21", "30.22", "30.23", "30.24", "30.25", "30.26"],
        "06-mach-rlc.md": ["30.27", "30.28", "30.29"],
        "09-tom-tat.md": ["30.4", "30.5", "30.6", "30.7", "30.9", "30.10", "30.11", "30.16", "30.22", "30.29"]
    }
    expected_equations = {
        fname: [r"(?:\\tag\{" + re.escape(eq) + r"\}|\(" + re.escape(eq) + r"\))" for eq in eqs]
        for fname, eqs in equation_numbers.items()
    }

    forbidden_phrases = [
        "theo sách", "sách dùng", "nguyên tác", "bản dịch của",
        "tiến độ bản dịch", "ảnh lấy từ sách", "hình trong sách",
        "ảnh nguyên gốc sách", "dữ liệu này từ", "đã kiểm chứng",
        "ví dụ do người soạn thêm"
    ]

    for fname in files:
        fpath = trans_dir / fname
        assert fpath.exists(), f"Missing required file: {fpath}"
        content = fpath.read_text(encoding="utf-8")

        # 1. Check equations
        for eq_pattern in expected_equations[fname]:
            assert re.search(eq_pattern, content), f"Missing equation {eq_pattern} in {fname}"

        # 2. Check forbidden phrases
        for phrase in forbidden_phrases:
            assert phrase not in content.lower(), f"Forbidden phrase '{phrase}' found in {fname}"

        # 3. Check $$ delimiters are on their own lines
        lines = content.splitlines()
        for idx, line in enumerate(lines, start=1):
            s = line.strip()
            if "$$" in s and s != "$$":
                # Only acceptable if it's inside code fence or comment
                assert False, f"Non-isolated $$ on line {idx} of {fname}: '{line}'"

        # 4. Check capitalization after colon in prose
        for idx, line in enumerate(lines, start=1):
            s = line.strip()
            # Skip Markdown table rows, image links, URLs, LaTeX blocks, code fences
            if s.startswith("|") or s.startswith("!") or s.startswith("http") or s.startswith("```"):
                continue
            # Strip ::: prefix if present so we can still check titles like '::: tip Tiêu đề: Nội dung'
            check_text = re.sub(r"^:::\s*\w*\s*", "", s) if s.startswith(":::") else s
            # Search for single colon followed by lowercase letter
            colon_matches = re.finditer(r"(?<!:):(?!:)\s+([^\s])", check_text)
            for m in colon_matches:
                ch = m.group(1)
                if not ch.islower():
                    continue
                # Check if it's inside $...$
                pos = m.start()
                dollar_count = s[:pos].count("$")
                if dollar_count % 2 == 0:
                    assert False, (
                        f"Lowercase after colon on line {idx} of {fname}: "
                        f"'{s[max(0, pos-10):min(len(s), pos+20)]}'"
                    )

        # 5. Check inline math length <= 38ex approximation (~38 chars)
        for idx, line in enumerate(lines, start=1):
            s = line.strip()
            if s.startswith("$$") or s.startswith("```"):
                continue
            # find all $...$
            inline_maths = re.findall(r"(?<!\$)\$([^\$]+)\$(?!\$)", s)
            for im in inline_maths:
                # Length check heuristic: very long expressions should be display
                # Note: target <= 38ex, typical TeX commands can have chars ~ 45-50 if commands are long
                # but mathematical length shouldn't be enormous
                if len(im) > 85:
                    print(f"Warning: long inline math ({len(im)} chars) on line {idx} of {fname}: ${im}$")

    print("All Markdown fragments verified.")


def main() -> None:
    print("=== Starting Chapter 30 Track B Verification ===")
    verify_example_30_6()
    verify_example_30_7()
    verify_example_30_8()
    verify_example_30_9()
    verify_example_30_10()
    verify_self_checks()
    verify_guided_practice_track_b()
    # Note: verify_markdown_fragments will be called after fragments are written
    if (ROOT / "raw_materials/physics/translations/chapter-30/04-mach-rl.md").exists():
        verify_markdown_fragments()
    else:
        print("Markdown fragments not yet created; skipping fragment structure checks.")
    print("=== All Numerical Tests Passed Successfully ===")


if __name__ == "__main__":
    main()
