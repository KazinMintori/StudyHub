"""Run every Python fence in the course, then independently check key results.

Requires numpy, pandas, matplotlib and seaborn. Uses synthetic data only; no API
calls or credentials. Generated example files live in a temporary directory.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json
import math
import os
import re
import tempfile
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "docs/xu-ly-du-lieu/bai-giang"

def verify(number, ns):
    if number == 1:
        assert (ns["tong"], ns["so_mat_hang"], ns["trung_binh"], ns["so_thieu"]) == (120, 3, 40, 1)
        valid = [x for x in [None, None] if x is not None]
        assert not valid
    elif number == 2:
        f = ns["doc_gia"]
        assert [f(x) for x in [" 18.5 ", "N/A", "-2", "NaN", None]] == [18.5, None, None, None, None]
        assert f("0") == 0 and f("inf") is None
        try:
            f(18)
        except TypeError:
            pass
        else:
            raise AssertionError("Incorrect input type must fail")
        a = [{"gia": 24}]; b = a.copy(); b[0]["gia"] = 99
        assert a[0]["gia"] == 99
        assert ns["gia_trung_binh"]([]) is None
    elif number == 3:
        a = ns["A"]
        assert a.shape == (2, 3) and a.sum() == 210
        np.testing.assert_array_equal(ns["B"], [[11, 22, 33], [41, 52, 63]])
        assert np.isclose(ns["v"].var(), 8 / 3) and ns["v"].var(ddof=1) == 4
        try:
            np.empty((4, 3)) + np.empty((4,))
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid broadcasting must fail")
    elif number == 4:
        df = ns["df"]
        assert (len(df), df.gia.count(), df.nhom.nunique()) == (4, 3, 2)
        assert df.doanh_thu.sum(min_count=1) == 170
        s = pd.Series([None, None], dtype="float64")
        assert s.sum() == 0 and pd.isna(s.sum(min_count=1))
    elif number == 5:
        df = ns["df"]
        assert ns["s"].loc[2] == 10 and ns["s"].iloc[2] == 30
        np.testing.assert_allclose(df.gia - df.gia_tb_nhom, [-10, 10, 0])
        left = pd.DataFrame({"k": ["A"] * 3}); right = pd.DataFrame({"k": ["A"] * 2})
        assert len(left.merge(right, on="k")) == 6
        try:
            left.merge(right, on="k", validate="many_to_one")
        except pd.errors.MergeError:
            pass
        else:
            raise AssertionError("Duplicate lookup keys must fail validation")
    elif number == 6:
        assert ns["tb"] == 50 and ns["chon"].doanh_thu.sum() == 100
        assert sum([10, 20, 30, 40]) / 4 == 25
        assert (10 + sum([20, 30, 40]) / 3) / 2 == 20
    elif number == 7:
        assert ns["clean"].dropna().tolist() == ["hà nội"] * 3
        assert ns["dung"].tolist() == [True, True, False, False]
        assert ns["loi_doc"].tolist() == [False, False, True, False]
        assert float("1.200,50".replace(",", "")) == 1.2005
    elif number == 8:
        assert ns["utc"][0].isoformat() == "2026-02-01T00:00:00+00:00"
        np.testing.assert_allclose(ns["daily"], [40, np.nan, 20], equal_nan=True)
        np.testing.assert_allclose(ns["moving"], [np.nan, 15, 25], equal_nan=True)
    elif number == 10:
        assert (len(ns["raw"]), int(ns["dup"].sum()), len(ns["clean"]), len(ns["rejected"])) == (5, 1, 1, 3)
        assert (ns["q1"], ns["q3"], ns["iqr"], ns["lo"], ns["hi"]) == (12, 16, 4, 6, 22)
        bins = pd.cut(pd.Series([15, 50]), bins=[0, 15, 50], right=False)
        assert bins.iloc[0].left == 15 and pd.isna(bins.iloc[1])
    elif number == 11:
        assert math.isclose(ns["accuracy"], 2 / 3)
        assert (ns["precision"], ns["recall"]) == (.5, 1)
        f = ns["validate_result"]
        for value in ['[]', '{"id":"R1","nhan":"sai","bang_chung":"Giao nhanh"}', '{"id":"R1","nhan":"tich_cuc","bang_chung":"khong co"}']:
            try:
                f(value, "R1", ns["text"])
            except ValueError:
                pass
            else:
                raise AssertionError("Invalid extraction must fail")
        assert 3 / (3 + 1) == .75 and 3 / (3 + 2) == .6
    elif number == 12:
        assert ns["freq"].tolist() == [0, 4, 4, 2]
        assert ns["counts"].sum() == 25 and 8 / 25 == .32
        assert np.histogram([10, 20, 40], bins=[0, 10, 20, 30, 40])[0].tolist() == [0, 1, 1, 1]
    elif number == 13:
        a = ns["data"].loc[lambda d: d.nhom == "A", "gia"]
        assert a.median() == 14 and a.quantile(.25) == 12 and a.quantile(.75) == 16
        assert np.isclose(2 / 98 * 100, 2.0408163265306123)
    elif number == 14:
        assert ns["overall"].loc["Truoc", "gia_tb"] == 4.8
        assert ns["overall"].loc["Sau", "gia_tb"] == 6.2
        assert np.isclose(ns["rate_change"], -.2) and ns["count_growth"] == .6

def main():
    rows = []
    original_cwd = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="studyhub-data-examples-") as temp:
        try:
            os.chdir(temp)
            for path in sorted(COURSE.glob("bai-*.md")):
                content = path.read_text(encoding="utf-8")
                blocks = re.findall(r"^```python\s*\n(.*?)^```\s*$", content, re.M | re.S)
                ns = {"__name__": "__studyhub_example__"}
                with redirect_stdout(StringIO()):
                    for i, code in enumerate(blocks, 1):
                        exec(compile(code, f"{path.name}:block-{i}", "exec"), ns)
                    verify(int(path.name.split("-")[1]), ns)
                plt.close("all")
                rows.append({"lesson": path.stem, "python_blocks": len(blocks), "status": "passed"})
        finally:
            os.chdir(original_cwd)
    assert len(rows) == 13
    print(json.dumps({"numpy": np.__version__, "pandas": pd.__version__, "lessons": rows, "total_blocks": sum(r["python_blocks"] for r in rows)}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
