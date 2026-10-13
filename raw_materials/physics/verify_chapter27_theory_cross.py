"""Independent cross-checks for Chapter 27 theory, Sections 27.0–27.9."""
from pathlib import Path
import math
import re

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "raw_materials/physics/translations/chapter-27"

E = 1.60e-19
ME = 9.11e-31
MP = 1.67e-27
G = 9.80


def close(actual: float, expected: float, rtol: float = 5e-3) -> None:
    np.testing.assert_allclose(actual, expected, rtol=rtol, atol=1e-30)


def verify_coverage() -> None:
    names = ["00-mo-dau.md", *[f"{i:02d}-" for i in range(1, 10)]]
    files = [CHAPTER / names[0]]
    for prefix in names[1:]:
        found = list(CHAPTER.glob(prefix + "*.md"))
        assert len(found) == 1, (prefix, found)
        files.extend(found)
    files.append(CHAPTER / "10-tom-tat.md")
    text = "\n".join(path.read_text(encoding="utf-8-sig") for path in files)

    tags = {int(n) for n in re.findall(r"\\tag\{27\.(\d+)\}", text)}
    assert tags == set(range(1, 31)), f"Equation tags missing/extra: {sorted(tags)}"
    examples = {int(n) for n in re.findall(r"Ví dụ 27\.(\d+)", text)}
    assert examples == set(range(1, 13)), f"Examples missing/extra: {sorted(examples)}"
    figures = {int(n) for n in re.findall(r"hinh-27-(\d+)\.png", text)}
    assert figures == set(range(1, 42)), f"Figure references missing/extra: {sorted(figures)}"


def verify_example_values() -> None:
    # 27.1: Proton force and the right-handed direction.
    force1 = E * 3.0e5 * 2.0 * math.sin(math.radians(30))
    close(force1, 4.8e-14)
    np.testing.assert_allclose(np.cross([math.sin(math.pi/6), 0, math.cos(math.pi/6)], [0, 0, 1]),
                               [0, -0.5, 0], atol=1e-14)

    # 27.2: Signed flux fixes the choice of area normal.
    field2 = 0.90e-3 / (3.0e-4 * math.cos(math.radians(60)))
    close(field2, 6.0)

    # 27.3: Magnetron cyclotron frequency.
    omega3 = 2 * math.pi * 2450e6
    b3 = ME * omega3 / E
    close(b3, 0.0877)

    # 27.4: Helical proton motion, including the force direction.
    v4 = np.array([1.50e5, 0.0, 2.00e5])
    b4 = np.array([0.500, 0.0, 0.0])
    f4 = E * np.cross(v4, b4)
    np.testing.assert_allclose(f4, [0.0, 1.60e-14, 0.0], rtol=1e-12)
    radius4 = MP * 2.00e5 / (E * 0.500)
    omega4 = E * 0.500 / MP
    period4 = 2 * math.pi / omega4
    pitch4 = 1.50e5 * period4
    close(radius4, 4.18e-3)
    close(omega4, 4.79e7)
    close(period4, 1.31e-7)
    close(pitch4, 0.0197)

    # 27.5: Thomson's selector, accelerating voltage, and nonrelativistic speed.
    speed5 = math.sqrt(2 * (1.76e11) * 150.0)
    b5 = 6.0e6 / speed5
    close(speed5, 7.27e6)
    close(speed5 / 299792458.0, 0.0243)
    close(b5, 0.83, rtol=1e-2)

    # 27.6: He+ mass-spectrometer radius is half the measured diameter.
    b6 = (6.65e-27 * 1.00e5) / (1.60e-19 * 0.0508)
    close(b6, 0.0818)

    # 27.7: Straight wire force, including the cross-product direction.
    force7 = 50.0 * np.cross([1.00, 0.0, 0.0],
                            [1.20 / math.sqrt(2), 1.20 / math.sqrt(2), 0.0])
    np.testing.assert_allclose(force7, [0.0, 0.0, 42.4], rtol=5e-3)
    close(50.0 * 1.00 * 1.20, 60.0)

    # 27.8: Curved-conductor integral equals the corresponding endpoint result.
    current8, radius8, field8, length8 = 2.0, 0.15, 0.8, 0.4
    arc8 = 2 * current8 * radius8 * field8
    straight8 = current8 * length8 * field8
    total8 = current8 * field8 * (2 * radius8 + length8)
    close(total8, arc8 + straight8, rtol=1e-14)
    close(arc8, 0.48)

    # 27.9–27.10: Dipole moment, torque, and change in potential energy.
    mu9 = 30 * 5.00 * math.pi * 0.0500**2
    torque9 = mu9 * 1.20
    delta_u10 = -mu9 * 1.20
    close(mu9, 1.18)
    close(torque9, 1.41)
    close(delta_u10, -1.41)

    # 27.11: Series motor power balance and stalled-rotor limit.
    emf11 = 120.0 - 4.00 * 2.00
    pin11 = 120.0 * 4.00
    heat11 = 4.00**2 * 2.00
    mech11 = emf11 * 4.00
    stall_i11 = 120.0 / 2.00
    stall_heat11 = stall_i11**2 * 2.00
    close(emf11, 112.0)
    close(pin11, 480.0)
    close(heat11, 32.0)
    close(mech11, 448.0)
    close(mech11 / pin11, 0.933)
    close(stall_i11, 60.0)
    close(stall_heat11, 7200.0)

    # 27.12: Hall polarity, Hall field, and the one-carrier density estimate.
    j12 = 75.0 / (2.0e-3 * 1.50e-2)
    e_hall12 = 0.81e-6 / 1.50e-2
    density12 = -j12 * 0.40 / (-E * e_hall12)
    close(j12, 2.5e6)
    close(e_hall12, 5.4e-5)
    close(density12, 1.16e29)
    # Electrons drift −x; B is +y; magnetic force on electrons is +z.
    electron_velocity = np.array([-1.0, 0.0, 0.0])
    b_direction = np.array([0.0, 1.0, 0.0])
    np.testing.assert_allclose(-np.cross(electron_velocity, b_direction),
                               [0.0, 0.0, 1.0])


def main() -> None:
    verify_coverage()
    verify_example_values()
    print("Chapter 27 theory cross-check: equations 27.1–27.30, Examples 27.1–27.12, Figures 27.1–27.41, numeric and vector checks passed.")


if __name__ == "__main__":
    main()
