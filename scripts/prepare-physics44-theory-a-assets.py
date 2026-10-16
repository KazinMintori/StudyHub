"""Crop Chapter 44 Theory A figures (Figures 44.1-44.9, Applications A1-A2) without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-44"

CROPS = {
    "hinh-44-01": (1505, (454, 104, 614, 346)),
    "hinh-44-02": (1505, (105, 626, 412, 742)),
    "hinh-44-03": (1506, (34, 144, 195, 424)),
    "ung-dung-a-1": (1506, (0, 665, 192, 747)),
    "hinh-44-04": (1507, (454, 84, 614, 325)),
    "hinh-44-05": (1507, (454, 455, 614, 575)),
    "ung-dung-a-2": (1508, (0, 346, 192, 488)),
    "hinh-44-06": (1508, (80, 590, 575, 742)),
    "hinh-44-07": (1510, (34, 265, 195, 582)),
    "hinh-44-08": (1512, (0, 169, 192, 329)),
    "hinh-44-09": (1513, (454, 264, 614, 498)),
}

SCALE = 2.5

def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found at {LOCAL_SOURCE} or {MAIN_SOURCE}")
    OUT.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(SOURCE) as pdf:
        for stem, (page_num, box) in CROPS.items():
            page = pdf[page_num - 1]
            rect = pymupdf.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=rect, alpha=False)
            target = OUT / f"{stem}.png"
            pix.save(target)
            print(f"Saved {stem}: p.{page_num}, box={box}, size={pix.width}x{pix.height}")
    print(f"Successfully prepared {len(CROPS)} images for Chapter 44 Theory A in {OUT}.")

if __name__ == "__main__":
    main()
