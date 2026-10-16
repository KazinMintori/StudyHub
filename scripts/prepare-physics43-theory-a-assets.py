"""Crop Chapter 43 Theory A figures (Figures 43.1-43.8 and applications) without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-43"

CROPS = {
    "hinh-43-01": (1467, (75, 75, 575, 428)),
    "hinh-43-02": (1469, (355, 84, 615, 273)),
    "hinh-43-03": (1472, (34, 94, 195, 415)),
    "hinh-43-04": (1473, (110, 55, 435, 475)),
    "hinh-43-05": (1474, (95, 87, 575, 245)),
    "hinh-43-06": (1477, (455, 560, 612, 740)),
    "hinh-43-07": (1478, (250, 55, 525, 495)),
    "hinh-43-08": (1479, (468, 614, 605, 755)),
    "ung-dung-a-1": (1464, (0, 339, 192, 501)),
    "ung-dung-a-2": (1468, (0, 258, 192, 397)),
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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 43 Theory A in {OUT}.")

if __name__ == "__main__":
    main()
