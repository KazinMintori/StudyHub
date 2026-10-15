"""Crop chapter 38 sections 38.1-38.2 figures (Figures 38.1-38.9) without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-38"

CROPS = {
    "hinh-38-01": (1274, (34, 75, 196, 245)),
    "hinh-38-02": (1274, (34, 390, 196, 716)),
    "hinh-38-03": (1275, (75, 58, 442, 336)),
    "hinh-38-04": (1275, (454, 522, 615, 665)),
    "hinh-38-05": (1276, (34, 615, 196, 725)),
    "hinh-38-06": (1277, (454, 268, 615, 475)),
    "hinh-38-07": (1279, (454, 585, 615, 746)),
    "hinh-38-08": (1280, (34, 342, 196, 520)),
    "hinh-38-09": (1281, (454, 530, 615, 712)),
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
    print(f"Successfully prepared {len(CROPS)} images for chapter 38 theory A.")

if __name__ == "__main__":
    main()
