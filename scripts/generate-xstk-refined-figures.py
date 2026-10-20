"""Reproduce and verify all 51 replacement scientific figures.

Usage: python scripts/generate-xstk-refined-figures.py [--check]
Only co-dien-refined is written. Original generators/assets are never imported.
"""
from pathlib import Path
import sys
import json
from xstk_refined_probability import verify_probability_math, generate_all_probability_figures
from xstk_refined_statistics import verify_statistics_math, generate_all_statistics_figures

def main():
    verify_probability_math();verify_statistics_math()
    if "--check" in sys.argv:return
    root=Path(__file__).resolve().parents[1]
    out=root/"docs/xac-suat-thong-ke/bai-giang/img/co-dien-refined"
    generate_all_probability_figures(out);generate_all_statistics_figures(out)
    expected=set(json.loads((root/"scripts/xstk-refined-figures.json").read_text(encoding="utf-8")))
    actual={p.name for p in out.glob("*.svg")}
    assert actual==expected and len(actual)==51,(actual-expected,expected-actual)
    print(f"PASS: Exactly 51 original basenames reproduced in {out}")

if __name__=="__main__":main()
