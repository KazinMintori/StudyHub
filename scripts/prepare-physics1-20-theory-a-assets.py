"""Crop Chapter 20 Theory A figures (Opening photo, Figures 20.1-20.10, and applications) without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-20"

CROPS = {
    "a-mo-dau-20": (662, (210, 0, 648, 245)),
    "a-hinh-20-01": (663, (85, 58, 435, 215)),
    "a-hinh-20-02": (664, (36, 402, 192, 642)),
    "a-hinh-20-03": (665, (465, 205, 605, 380)),
    "a-ung-dung-01": (665, (455, 596, 648, 742)),
    "a-hinh-20-04": (666, (36, 600, 225, 737)),
    "a-hinh-20-05": (667, (76, 525, 612, 745)),
    "a-hinh-20-06": (668, (36, 94, 195, 290)),
    "a-hinh-20-07": (668, (36, 550, 195, 745)),
    "a-hinh-20-08": (669, (470, 415, 595, 565)),
    "a-hinh-20-09": (670, (78, 84, 612, 335)),
    "a-hinh-20-10": (670, (235, 550, 545, 735)),
}

SCALE = 3.0

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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 20 Theory A in {OUT}.")

if __name__ == "__main__":
    main()
