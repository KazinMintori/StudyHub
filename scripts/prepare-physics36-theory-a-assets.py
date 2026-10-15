"""Crop chapter 36 sections 36.1-36.4 figures (Figures 36.1-36.15) without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-36"

CROPS = {
    "hinh-36-01": (1206, (36, 85, 195, 258)),
    "hinh-36-02": (1206, (210, 560, 575, 735)),
    "hinh-36-03": (1207, (75, 588, 575, 745)),
    "hinh-36-04": (1208, (38, 74, 575, 226)),
    "hinh-36-05": (1208, (210, 545, 575, 742)),
    "hinh-36-06": (1209, (455, 420, 580, 565)),
    "hinh-36-07": (1210, (36, 74, 275, 198)),
    "hinh-36-08": (1210, (36, 275, 195, 742)),
    "hinh-36-09": (1211, (455, 460, 615, 745)),
    "hinh-36-10": (1212, (105, 630, 575, 748)),
    "hinh-36-11": (1213, (450, 125, 610, 235)),
    "hinh-36-12": (1214, (36, 335, 195, 740)),
    "hinh-36-13": (1215, (455, 260, 615, 455)),
    "hinh-36-14": (1215, (75, 626, 445, 735)),
    "hinh-36-15": (1216, (36, 135, 195, 565)),
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
    print(f"Successfully prepared {len(CROPS)} images for chapter 36 theory A.")

if __name__ == "__main__":
    main()
