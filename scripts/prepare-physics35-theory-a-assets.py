"""Crop chapter 35 sections 35.1-35.3 figures (Figures 35.1-35.10) without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-35"

CROPS = {
    "hinh-35-01": (1180, (36, 435, 195, 595)),
    "hinh-35-02": (1181, (75, 95, 575, 255)),
    "hinh-35-03": (1182, (36, 135, 195, 370)),
    "hinh-35-04": (1183, (455, 125, 620, 335)),
    "hinh-35-05": (1183, (75, 455, 435, 748)),
    "hinh-35-06": (1184, (36, 340, 195, 635)),
    "hinh-35-07": (1185, (78, 225, 340, 360)),
    "hinh-35-08": (1185, (78, 600, 340, 735)),
    "hinh-35-09": (1186, (36, 585, 195, 750)),
    "hinh-35-10": (1189, (78, 75, 545, 205)),
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
    print(f"Successfully prepared {len(CROPS)} images for chapter 35 theory A.")

if __name__ == "__main__":
    main()
