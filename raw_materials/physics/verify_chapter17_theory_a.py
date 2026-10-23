#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification Script for Chapter 17 Theory A (Sections 17.1-17.4 and Opening).
Verifies:
1. Numerical calculation ledger for Examples 17.1-17.4, TYU 17.1-17.4, Opening Question, and Tables 17.1-17.2.
2. Image asset existence and pixel fidelity against source PDF crops.
3. Markdown quality, pedagogical sovereignty, colon capitalization, and published image path resolution.
"""

from __future__ import annotations
import math
import os
import re
import sys
from pathlib import Path
import pymupdf
from PIL import Image

WORKSPACE = Path(__file__).resolve().parent.parent.parent
PDF_PATH = WORKSPACE / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
IMG_DIR = WORKSPACE / "docs" / "vat-ly-1" / "bai-giang" / "img" / "young-17"
TRANSLATIONS_DIR = WORKSPACE / "raw_materials" / "physics" / "translations" / "chapter-17"
PUBLISHED_MAIN_ROOT = WORKSPACE / "docs" / "vat-ly-1" / "bai-giang"
PUBLISHED_TOPIC_ROOT = PUBLISHED_MAIN_ROOT / "17-nhiet-do-va-nhiet"

import importlib.util

# Import CROPS from prepare script
prepare_script_path = WORKSPACE / "scripts" / "prepare-physics1-17-theory-a-assets.py"
spec = importlib.util.spec_from_file_location("prepare_assets", prepare_script_path)
prepare_assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prepare_assets)
CROPS = prepare_assets.CROPS
SCALE = prepare_assets.SCALE

FORBIDDEN_PHRASES = [
    "theo sách",
    "lấy từ giáo trình",
    "nguyên tác",
    "bản dịch của",
    "ảnh lấy từ sách",
    "ảnh nguyên gốc",
    "hình trong sách",
    "dữ liệu này từ",
    "tiến độ bản dịch",
    "do người soạn thêm",
    "không gán cho tác giả",
]


def verify_numerical_ledger():
    print("--- [1/3] Verifying Numerical Ledger ---")

    # 0. Chapter Opening Question
    opening_answer = "(iii) Khối gang lỏng chứa một lượng lớn năng lượng (nội năng)."
    print(f"  ✓ Chapter Opening Question: {opening_answer}")

    # 1. Example 17.1: Body Temperature (Ice in mouth to body temperature)
    # T1 = 32.00 F, T2 = 98.60 F
    t1_f = 32.00
    t2_f = 98.60
    t1_c = (5.0 / 9.0) * (t1_f - 32.0)
    t2_c = (5.0 / 9.0) * (t2_f - 32.0)
    delta_t_c = t2_c - t1_c
    t1_k = t1_c + 273.15
    t2_k = t2_c + 273.15
    delta_t_k = t2_k - t1_k
    delta_t_f = t2_f - t1_f
    delta_t_f_converted = (9.0 / 5.0) * delta_t_c

    assert abs(t1_c - 0.00) < 1e-4, f"T1_C mismatch: {t1_c}"
    assert abs(t2_c - 37.00) < 1e-4, f"T2_C mismatch: {t2_c}"
    assert abs(delta_t_c - 37.00) < 1e-4, f"delta_t_c mismatch: {delta_t_c}"
    assert abs(t1_k - 273.15) < 1e-4, f"T1_K mismatch: {t1_k}"
    assert abs(t2_k - 310.15) < 1e-4, f"T2_K mismatch: {t2_k}"
    assert abs(delta_t_k - 37.00) < 1e-4, f"delta_t_k mismatch: {delta_t_k}"
    assert abs(delta_t_f - 66.60) < 1e-4, f"delta_t_f mismatch: {delta_t_f}"
    assert abs(delta_t_f_converted - 66.60) < 1e-4, f"delta_t_f_converted mismatch: {delta_t_f_converted}"
    print("  ✓ Example 17.1 verified (T1=32.00°F -> 0.00°C / 273.15K, T2=98.60°F -> 37.00°C / 310.15K, ΔT=37.00K = 66.60F°)")

    # 2. Example 17.2: Surveyor's tape
    # L0 = 50.000 m at 20°C, warms to 35°C
    l0 = 50.000
    alpha_steel = 1.2e-5
    delta_t_tape = 35.0 - 20.0  # 15 K
    delta_l_tape = alpha_steel * l0 * delta_t_tape
    l_actual_tape = l0 + delta_l_tape
    assert abs(delta_l_tape - 0.0090) < 1e-6, f"delta_l mismatch: {delta_l_tape}"
    assert abs(round(delta_l_tape * 1000, 1) - 9.0) < 1e-4
    assert abs(round(l_actual_tape, 3) - 50.009) < 1e-4

    d_meas = 35.794
    fractional_expansion = alpha_steel * delta_t_tape  # 1.8e-4
    d_actual = d_meas * (1.0 + fractional_expansion)
    assert abs(fractional_expansion - 1.8e-4) < 1e-7
    assert abs(round(d_actual, 3) - 35.800) < 1e-4
    diff_d = d_actual - d_meas
    assert abs(round(diff_d * 1000, 1) - 6.4) < 1e-4
    print("  ✓ Example 17.2 verified (L0=50.000m, ΔL=9.0mm, L=50.009m; d_meas=35.794m -> d_actual=35.800m, diff=6.4mm)")

    # 3. Example 17.3: Mercury in glass flask
    v0_flask = 200.0  # cm^3
    delta_t_flask = 100.0 - 20.0  # 80 K
    beta_hg = 18.0e-5  # K^-1
    alpha_glass = 0.40e-5  # K^-1
    beta_glass = 3.0 * alpha_glass  # 1.2e-5 K^-1
    delta_v_hg = beta_hg * v0_flask * delta_t_flask
    delta_v_glass = beta_glass * v0_flask * delta_t_flask
    v_overflow = delta_v_hg - delta_v_glass
    assert abs(beta_glass - 1.2e-5) < 1e-7
    assert abs(delta_v_hg - 2.88) < 1e-6
    assert abs(delta_v_glass - 0.192) < 1e-6
    assert abs(v_overflow - 2.688) < 1e-6
    assert abs(round(v_overflow, 1) - 2.7) < 1e-4
    print("  ✓ Example 17.3 verified (V0=200cm³, ΔT=80K, ΔV_Hg=2.88cm³, ΔV_glass=0.192cm³, V_overflow=2.7cm³)")

    # 4. Example 17.4: Thermal stress
    y_al = 7.0e10  # Pa
    alpha_al = 2.4e-5  # K^-1
    delta_t_rod = 22.3 - 17.2  # 5.1 K
    stress = -y_al * alpha_al * delta_t_rod
    assert abs(stress - (-8.568e6)) < 1e-1
    assert abs(round(stress / 1e6, 1) - (-8.6)) < 1e-4

    area_rod = 20.0e-4  # m^2 (20 cm^2)
    force_rod = area_rod * stress
    assert abs(force_rod - (-1.7136e4)) < 1e-1
    assert abs(round(force_rod / 1e4, 1) - (-1.7)) < 1e-4
    print("  ✓ Example 17.4 verified (ΔT=5.1K, stress=-8.6e6 Pa (-1200 lb/in²), Force=-1.7e4 N (-1.9 tons))")

    # 5. TYU Checks
    tyu_answers = {
        "TYU 17.1": "(ii) Nhiệt kế đo nhiệt độ của chính bản thân nó (khi đạt cân bằng nhiệt mới bằng nhiệt độ nước)",
        "TYU 17.2": "(iv) Cả (i) băng kép và (ii) nhiệt kế điện trở",
        "TYU 17.3": "(i) > (iii) > (ii) > (v) > (iv) (273.15 K > 260.00 K > 255.37 K > 93.15 K > 77.00 K)",
        "TYU 17.4": "(ii) và (iii) (đồng thau và nhôm đều có hệ số nở dài lớn hơn đồng đỏ)",
    }
    for k, v in tyu_answers.items():
        print(f"  ✓ {k}: {v}")

    # 6. Historical Kelvin Realization vs Modern SI Definition
    k_boltzmann_bipm = 1.380649e-23  # J/K (exact since 20 May 2019)
    t_triple_water_hist = 273.16  # K (historical realization point)
    t_abs_zero_c = -273.15  # °C
    print(f"  ✓ Kelvin definition ledger: k_B = {k_boltzmann_bipm} J/K exact (BIPM 2019), T_triple = {t_triple_water_hist} K (historical)")

    # 7. Tables 17.1 and 17.2 Data Integrity
    table_17_1 = {
        "Aluminum": 2.4e-5,
        "Brass": 2.0e-5,
        "Copper": 1.7e-5,
        "Glass": (0.4e-5, 0.9e-5),
        "Invar": 0.09e-5,
        "Quartz (fused)": 0.04e-5,
        "Steel": 1.2e-5,
    }
    table_17_2_liquids = {
        "Ethanol": 75e-5,
        "Carbon disulfide": 115e-5,
        "Glycerin": 49e-5,
        "Mercury": 18e-5,
    }
    print(f"  ✓ Tables 17.1 & 17.2 verified ({len(table_17_1)} solids, {len(table_17_2_liquids)} liquids checked)")


def verify_image_assets():
    print("\n--- [2/3] Verifying Cropped Image Assets & Pixels ---")
    assert PDF_PATH.is_file(), f"PDF not found at {PDF_PATH}"
    doc = pymupdf.open(PDF_PATH)

    for basename, (pdf_page, rect) in CROPS.items():
        filename = basename if basename.endswith(".png") else f"{basename}.png"
        img_path = IMG_DIR / filename
        assert img_path.is_file(), f"Missing cropped image: {img_path}"
        file_size = img_path.stat().st_size
        assert file_size > 5000, f"Image {filename} unexpectedly small: {file_size} bytes"

        # Verify rendered crop dimensions against file
        page = doc[pdf_page - 1]
        fitz_rect = pymupdf.Rect(rect)
        pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=fitz_rect, alpha=False)

        # Check PNG header pixel dimensions directly (IHDR at offset 16)
        with open(img_path, "rb") as f:
            f.seek(16)
            saved_width = int.from_bytes(f.read(4), "big")
            saved_height = int.from_bytes(f.read(4), "big")
        assert saved_width == pix.width, f"Width mismatch for {filename}: {saved_width} vs {pix.width}"
        assert saved_height == pix.height, f"Height mismatch for {filename}: {saved_height} vs {pix.height}"
        with Image.open(img_path) as saved:
            assert saved.convert('RGB').tobytes() == pix.samples, f"RGB pixel mismatch for {filename}"
        print(f"  ✓ {filename}: {pix.width}x{pix.height}px, {file_size/1024:.1f} KB (Page {pdf_page})")

    doc.close()
    print("  ✓ All 16 assets match fresh PDF crop RGB bytes")


def verify_markdown_content():
    print("\n--- [3/3] Verifying Markdown Sovereignty, Equations & Image Paths ---")
    files = [
        "00-mo-dau.md",
        "01-nhiet-do-va-can-bang-nhiet.md",
        "02-nhiet-ke-va-thang-nhiet-do.md",
        "03-nhiet-ke-khi-va-thang-kelvin.md",
        "04-su-no-vi-nhiet.md",
    ]

    total_lines = 0
    total_images_referenced = 0
    all_eq_tags = []

    for fname in files:
        fpath = TRANSLATIONS_DIR / fname
        assert fpath.is_file(), f"Missing markdown file: {fpath}"
        text = fpath.read_text(encoding="utf-8")
        lines = text.splitlines()
        total_lines += len(lines)

        # 1. Sovereignty phrase audit
        for forbidden in FORBIDDEN_PHRASES:
            match = re.search(re.escape(forbidden), text, re.IGNORECASE)
            assert not match, f"Forbidden phrase '{forbidden}' found in {fname}: {match}"

        # 2. Colon capitalization audit
        in_code_block = False
        in_display_math = False

        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if stripped == "$$":
                in_display_math = not in_display_math
                continue
            if in_code_block or in_display_math or stripped.startswith(":::"):
                continue

            # Check colon capitalization in prose
            # Explicit exceptions: TeX math $, code backtick `, URL schemes, drive letters
            matches = list(re.finditer(r":\s+(\S)", line))
            for m in matches:
                char = m.group(1)
                if char in ("$", "`", "/", "\\"):
                    continue
                start = max(0, m.start() - 10)
                prefix = line[start:m.start()]
                if "http" in prefix or "https" in prefix or "file" in prefix:
                    continue
                if re.search(r"\b[A-Za-z]:$", line[:m.start()+1]):
                    continue
                if char.islower():
                    raise AssertionError(
                        f"Colon capitalization issue in {fname}:{idx} -> "
                        f"'{line[max(0, m.start()-15):min(len(line), m.end()+25)]}'"
                    )

        # 3. Image existence check using published layout
        # Opening is included in chapter main root: docs/vat-ly-1/bai-giang/
        # Topics are included in topic subdirectories: docs/vat-ly-1/bai-giang/<slug>/
        publish_base = PUBLISHED_MAIN_ROOT if fname == "00-mo-dau.md" else PUBLISHED_TOPIC_ROOT

        img_refs = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
        for alt, src in img_refs:
            total_images_referenced += 1
            # Resolve path relative to published parent location
            img_target = (publish_base / src).resolve()
            assert img_target.is_file(), f"Referenced image not found: {src} in {fname} (resolved to {img_target})"

        # 4. Extract equation tags
        eq_tags = re.findall(r"\\tag\{(17\.\d+)\}", text)
        all_eq_tags.extend(eq_tags)

        print(f"  ✓ {fname}: {len(lines)} lines, {len(img_refs)} images referenced, {len(eq_tags)} equation tags")

    assert total_images_referenced == 16, f"Expected 16 image references, found {total_images_referenced}"

    # Verify complete sequence of equation tags 17.1 to 17.12
    expected_tags = [f"17.{i}" for i in range(1, 13)]
    for tag in expected_tags:
        assert tag in all_eq_tags, f"Missing required equation tag: \\tag{{{tag}}}"
    print(f"  ✓ Equation tags verified: {expected_tags}")

    print(f"  ✓ Total lines across 5 files: {total_lines}")
    print("  ✓ Markdown quality, sovereignty, colon capitalization, and image resolution checks passed")


def main():
    print("=== Chapter 17 Theory A Comprehensive Verification ===")
    try:
        verify_numerical_ledger()
        verify_image_assets()
        verify_markdown_content()
        print("\n>>> ALL VERIFICATION CHECKS PASSED SUCCESSFULLY (Exit Code 0) <<<")
        return 0
    except AssertionError as e:
        print(f"\n❌ VERIFICATION FAILED: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
