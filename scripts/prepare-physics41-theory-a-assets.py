"""Crop Chapter 41 Theory A figures (Figures 41.1-41.12) without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-41"

CROPS = {
    "hinh-41-01": (1382, (34, 545, 195, 672)),
    "hinh-41-02": (1384, (34, 300, 195, 755)),
    "hinh-41-03": (1385, (400, 205, 560, 350)),
    "hinh-41-04": (1386, (245, 530, 528, 748)),
    "hinh-41-05": (1388, (34, 160, 195, 345)),
    "hinh-41-06": (1390, (34, 215, 195, 528)),
    "hinh-41-07": (1391, (454, 165, 614, 370)),
    "hinh-41-08": (1393, (454, 224, 614, 515)),
    "hinh-41-09": (1393, (100, 545, 425, 715)),
    "hinh-41-10": (1394, (215, 104, 575, 305)),
    "hinh-41-11": (1395, (454, 280, 614, 545)),
    "hinh-41-12": (1395, (454, 600, 614, 755)),
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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 41 Theory A in {OUT}.")

if __name__ == "__main__":
    main()
