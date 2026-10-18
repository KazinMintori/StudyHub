"""Exercise the functions actually published, beyond their displayed examples."""
from contextlib import contextmanager, redirect_stdout, redirect_stderr
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
import importlib.util
import os
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("lab_code", ROOT / "scripts/complete-data-lab-code.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


@contextmanager
def method(file, identifier, way):
    text = (ROOT / "raw_materials/xu-ly-du-lieu/labs" / file).read_text(encoding="utf-8")
    matched = next(m for m in module.extract_methods(text) if m.exercise == identifier and m.way == way)
    previous = Path.cwd()
    with TemporaryDirectory(prefix="studyhub-edge-") as folder:
        try:
            os.chdir(folder)
            namespace = {"__name__": "__lesson__"}
            with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                exec(compile(text[matched.start:matched.end], identifier, "exec"), namespace)
            yield namespace
            if "plt" in namespace:
                namespace["plt"].close("all")
        finally:
            os.chdir(previous)


def main():
    for way in [1, 2]:
        with method("lab-08.md", "data-lab-08-01", way) as ns:
            dates = pd.DataFrame({"vao": ["02/13/2026", "29/02/2024", "31/06/2026", None], "ra": ["15/02/2026", "02/03/2024", "05/07/2026", "01/01/2026"]}, index=[8, 2, 7, 4])
            actual = ns["calculate_stay_nights"](dates)
            pd.testing.assert_series_equal(actual, pd.Series([np.nan, 2.0, np.nan, np.nan], index=dates.index), check_names=False)
        with method("lab-05-groupby.md", "data-lab-05-04", way) as ns:
            frame = pd.DataFrame({"id": [1, 2], "phan_khuc": pd.Categorical(["trung", "trung"], categories=["re", "trung", "cao"]), "price": [30.0, 60.0], "number_of_reviews_ltm": [2, 4]})
            actual = ns["segment_stats"](frame)
            assert actual.index.tolist() == ["trung"]
            assert actual.loc["trung"].tolist() == [2, 45, 3]
        with method("lab-11.md", "data-lab-11-01", way) as ns:
            frame = pd.DataFrame({"id": [1, 2, 3], "comments": ["a<br/>b", None, "long enough"]})
            name = "choose_sample" if way == 1 else "choose_sample_robust"
            actual = ns[name](frame, do_dai_min=3, n=2, seed=4).sort_values("id")
            assert actual.id.tolist() == [1, 3]
            assert actual.comments.tolist() == ["a b", "long enough"]
            assert frame.comments.iloc[0] == "a<br/>b"
        with method("lab-03.md", "data-lab-03-08", way) as ns:
            if way == 2:
                prices = np.array([0., 10., 10., 50.])
                before = prices.copy()
                result = ns["price_statistics"](prices, threshold=10, sample_size=4, seed=9)
                assert result["share"] == 0.75
                assert result["mean"] == result["sample_mean"] == 17.5
                assert len(set(result["indices"])) == 4
                np.testing.assert_array_equal(prices, before)

    with method("lab-07.md", "data-lab-07-10", 1) as first, method("lab-07.md", "data-lab-07-10", 2) as second:
        pd.testing.assert_series_equal(first["tan_suat_da_loc"], second["top_da_loc"])
    with method("lab-07.md", "data-lab-07-14", 1) as first, method("lab-07.md", "data-lab-07-14", 2) as second:
        pd.testing.assert_frame_equal(first["bang_tin_hieu"], second["df_tin_hieu"])
    with method("lab-06.md", "data-lab-06-11", 1) as first, method("lab-06.md", "data-lab-06-11", 2) as second:
        pd.testing.assert_frame_equal(first["ket_qua_thang_7"]["gop"], second["thang_bay"]["gop"])
        assert first["ket_qua_thang_7"]["so_ngay_thieu"] == second["thang_bay"]["so_thieu"] == 1
        assert np.isclose(first["ket_qua_thang_7"]["he_so_tuong_quan"], second["thang_bay"]["he_so"])
    with method("lab-13.md", "data-lab-13-04", 1) as first, method("lab-13.md", "data-lab-13-04", 2) as second:
        events = pd.DataFrame({"date": pd.to_datetime(["2019-01-01", "2021-06-30", "2021-12-31"])})
        expected = pd.Series([1, 0, 2], index=pd.date_range("2019-12-31", "2021-12-31", freq="YE", name="date"))
        pd.testing.assert_series_equal(first["yearly_counts_resample"](events, "2019", "2021"), expected)
        pd.testing.assert_series_equal(second["yearly_counts_reindex"](events, "2019", "2021"), expected)
    for way in [1, 2]:
        with method("lab-14.md", "data-lab-14-05", way) as ns:
            frame = pd.DataFrame({"calculated_host_listings_count": [1, 1, 8], "number_of_reviews_ltm": [2.0, np.nan, 7.0]})
            actual = ns["reviews_by_host_type"](frame)
            assert actual.to_dict() == {False: 2.0, True: 7.0}
            assert ns["reviews_by_host_type"](frame, nguong=10).index.tolist() == [False]
        with method("lab-14.md", "data-lab-14-07", way) as ns:
            report = ns["audit_host_performance"](ns["DEMO_DS"])
            assert report["so_cho_o"].tolist() == [7, 5]
            assert np.isclose(report["ty_le_xuat_sac"].iloc[0], 5/6, atol=0.0005)
            frame = pd.DataFrame({"id": [None, 2], "calculated_host_listings_count": [1, 1], "number_of_reviews_ltm": [2.0, np.nan], "review_scores_rating": [np.nan, np.nan]})
            actual = ns["audit_host_performance"](frame, nguong=9)
            assert actual["so_cho_o"].tolist() == [2]
            assert "9" in actual.index[0]
            assert pd.isna(actual["ty_le_xuat_sac"].iloc[0])
    print("Published-code edge cases passed: Strict dates/leap year, absent categories, missing/HTML text, sampling, stopwords, both keyword signals and independent weather analysis.")


if __name__ == "__main__":
    os.environ["MPLBACKEND"] = "Agg"
    main()
