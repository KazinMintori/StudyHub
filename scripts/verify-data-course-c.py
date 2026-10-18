"""Verify all Python fences and test outputs for Group C lessons in Data Processing.

Group C lessons:
- Chapter 11: docs/xu-ly-du-lieu/bai-giang/bai-08-du-lieu-thoi-gian.md
- Chapter 12: docs/xu-ly-du-lieu/bai-giang/bai-12-mo-hinh-hoa.md
- Chapter 13: docs/xu-ly-du-lieu/bai-giang/bai-14-ke-chuyen-bang-du-lieu.md
- Appendix A: docs/xu-ly-du-lieu/bai-giang/phu-luc-a-numpy-nang-cao.md
"""
import json
import math
import os
from pathlib import Path
import sys
import tempfile
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
COURSE_DIR = ROOT / "docs/xu-ly-du-lieu/bai-giang"

GROUP_C_FILES = {
    "ch11": COURSE_DIR / "bai-08-du-lieu-thoi-gian.md",
    "ch12": COURSE_DIR / "bai-12-mo-hinh-hoa.md",
    "ch13": COURSE_DIR / "bai-14-ke-chuyen-bang-du-lieu.md",
    "appA": COURSE_DIR / "phu-luc-a-numpy-nang-cao.md",
}

def extract_python_blocks(md_path):
    lines = md_path.read_text(encoding="utf-8").splitlines()
    blocks = []
    curr = []
    in_block = False
    for line in lines:
        stripped = line.strip()
        if not in_block:
            if stripped.startswith("```python"):
                in_block = True
                curr = []
        else:
            if stripped.startswith("```"):
                in_block = False
                blocks.append("\n".join(curr))
            else:
                curr.append(line)
    return blocks

def verify_chapter11(ns):
    # Timezone conversion: localize vs convert
    assert str(ns["t_ha_noi"].tz) == "Asia/Ho_Chi_Minh"
    assert str(ns["t_utc"].tz) == "UTC"
    assert ns["t_ha_noi"].hour == 8 and ns["t_utc"].hour == 1

    # Resample OHLC and downsampling
    assert ns["bang_ohlc"].shape == (2, 4)
    assert list(ns["bang_ohlc"].columns) == ["open", "high", "low", "close"]
    assert len(ns["thang_gd"]) == 3

    # Interpolation and smoothing
    assert ns["up_interp"].iloc[1] == 15.0
    assert math.isclose(ns["ewm_tb"].iloc[-1], 14.903226, abs_tol=1e-4)

    # Period and offsets
    assert str(ns["p_nam"].freqstr) in ("A-DEC", "Y-DEC", "Y", "A")
    assert ns["p_quy"].freqstr == "Q-NOV"
    assert len(ns["p_idx"]) == 4

    # Exercises
    # Exercise 1 (IAI 08): booking exposure
    assert ns["so_dem"].tolist() == [3, 2]
    # Exercise 2 (IAI 08): missing months and shift
    assert ns["tb_moi_ngay"] == 1.0
    # Exercise 3 (IAI 08): spike detection with rolling
    assert len(ns["thang_tang_manh"]) == 2
    assert ns["thang_tang_manh"].iloc[0] == 150

def verify_chapter12(ns):
    # pandas to model
    assert ns["X_so"].shape == (8, 2)
    assert "quan_DongDa" in ns["df_dummies"].columns

    # Patsy formulas
    assert ns["X1"].shape[1] == 3
    assert ns["X2"].shape[1] == 2

    # statsmodels OLS & time series
    assert math.isclose(ns["mo_hinh"].params["dien_tich"], 0.0501, abs_tol=1e-3)
    assert math.isclose(ns["mo_hinh_ar"].params[1], 0.6761, abs_tol=1e-3)

    # sklearn Pipeline & leakage
    assert math.isclose(ns["sai_so_mse"], 0.01875, abs_tol=1e-3)

    # Exercises
    assert ns["X_kh"].shape[1] == 5
    assert ns["mo_hinh_nha"].rsquared > 0.99
    assert ns["diem_ro_ri"] > 0.95
    assert ns["diem_danh_gia"] > 0.95

def verify_chapter13(ns):
    # Case study 1: Timezone logs
    assert ns["tz_sach"].value_counts().index[0] == "Asia/Ho_Chi_Minh"
    assert ns["bang_he_dieu_hanh"].shape == (4, 2)

    # Case study 2: Movie ratings & disagreement
    assert ns["bang_diem"].loc["Phim Hanh Dong A", "F"] == 4.5
    assert ns["bang_diem"].loc["Phim Hanh Dong A", "chenh_lech"] == 3.0
    assert ns["do_phan_tan"].loc["Phim Hanh Dong A"] > 1.8

    # Case study 3: Baby names diversity and ending letters
    assert "n" in ns["bang_chu_cai"].index
    assert "y" in ns["bang_chu_cai"].index

    # Case study 4: Nested nutrition JSON flattening
    assert ns["bang_tong_hop"].shape == (6, 5)
    assert ns["top_protein"].iloc[0]["ten"] == "Trung ga"

    # Case study 5: Grouped donations
    assert "(0, 100]" in [str(c) for c in ns["dong_tien_nhom"].columns]

    # Simpson's Paradox audit
    assert math.isclose(ns["tang_dt"], 10.0)
    assert math.isclose(ns["tang_sach"], 10.0)
    assert ns["tang_gop"] < 0  # Paradox: each subgroup increased by +10%, but overall collapsed by -67.6%

def verify_appendix_a(ns):
    # Internal layout & contiguity
    assert ns["arr_c"].flags.c_contiguous
    assert ns["arr_f"].flags.f_contiguous
    assert ns["arr_c"].strides == (8000, 8)
    assert ns["arr_f"].strides == (8, 8000)

    # Shares memory vs copy
    assert np.shares_memory(ns["goc"], ns["doi_hinh"])
    assert np.shares_memory(ns["goc"], ns["view_phang"])
    assert not np.shares_memory(ns["goc"], ns["sao_phang"])

    # Broadcasting & ufunc methods
    assert ns["bang_cong"].shape == (3, 2)
    assert ns["u_day"].tolist() == [1, 2, 3, 4, 5]
    assert np.add.accumulate(ns["u_day"]).tolist() == [1, 3, 6, 10, 15]
    assert ns["uf_rieng"]([1, 2], [10, 20]).tolist() == [12, 24]

    # Structured arrays
    assert len(ns["kho_hang"]) == 2
    assert ns["kho_hang_rec"].ten.tolist() == ["Ban phim", "Chuot quang"]

    # Sorting algorithms
    assert ns["ten"][ns["chi_muc_sap_xep"]][0] == "An"
    assert ns["phan_hoach"][:3].tolist() == [5, 12, 18]
    assert ns["vi_tri_chen"].tolist() == [0, 2, 4, 5]

    # Numba JIT & memmap
    assert math.isclose(ns["ket_qua"], float(ns["du_lieu_lon"].sum()), rel_tol=1e-5)
    assert ns["phep_nhan_cong_numba"](1.0, 5.0) == 7.5

    # Exercises
    assert np.shares_memory(ns["A"], ns["B"])
    assert ns["hang"].tolist() == [0, 1, 2, 3]
    assert ns["t_numba"] < ns["t_vec"]

VERIFIERS = {
    "ch11": verify_chapter11,
    "ch12": verify_chapter12,
    "ch13": verify_chapter13,
    "appA": verify_appendix_a,
}

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    results = []
    original_cwd = Path.cwd()

    with tempfile.TemporaryDirectory(prefix="studyhub-verify-c-") as temp_dir:
        try:
            os.chdir(temp_dir)
            for key, file_path in GROUP_C_FILES.items():
                if not file_path.exists():
                    raise FileNotFoundError(f"Missing required file: {file_path}")

                blocks = extract_python_blocks(file_path)
                ns = {
                    "__name__": "__verify_c__",
                    "__file__": str(file_path),
                }

                stdout_buf = StringIO()
                stderr_buf = StringIO()

                with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
                    for idx, code in enumerate(blocks, start=1):
                        try:
                            compiled = compile(code, f"{file_path.name}:block-{idx}", "exec")
                            exec(compiled, ns)
                        except Exception as e:
                            print(f"Error in {file_path.name} block {idx}:\n{code}", file=sys.stderr)
                            raise e

                    # Run lesson-specific assertions
                    verifier = VERIFIERS.get(key)
                    if verifier:
                        verifier(ns)

                plt.close("all")
                results.append({
                    "unit": key,
                    "filename": file_path.name,
                    "blocks_count": len(blocks),
                    "status": "passed",
                })
        finally:
            os.chdir(original_cwd)

    summary = {
        "status": "success",
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
        "verified_units": results,
        "total_python_blocks": sum(r["blocks_count"] for r in results),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
