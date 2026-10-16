"""Crop chapter 42 sections 42.1-42.4 figures (Figures 42.1-42.19 and applications).

Run from StudyHub root with Python and PyMuPDF installed:
    python -X utf8 scripts/prepare-physics42-theory-a-assets.py

Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-42"

CROPS = {
    "hinh-42-01": (1429, (455, 145, 615, 290)),
    "hinh-42-02": (1429, (455, 510, 615, 755)),
    "hinh-42-03": (1430, (36, 155, 192, 300)),
    "ung-dung-a-1": (1430, (0, 550, 192, 700)),
    "ung-dung-a-2": (1428, (209, 0, 648, 244)),
    "hinh-42-04": (1431, (455, 360, 615, 450)),
    "hinh-42-05": (1431, (470, 600, 605, 750)),
    "hinh-42-06": (1433, (455, 95, 615, 220)),
    "hinh-42-07": (1433, (470, 282, 605, 400)),
    "hinh-42-08": (1433, (455, 494, 615, 755)),
    "hinh-42-09": (1434, (76, 76, 572, 140)),
    "hinh-42-10": (1435, (455, 114, 615, 425)),
    "ung-dung-a-3": (1435, (450, 585, 648, 740)),
    "hinh-42-11": (1436, (160, 75, 575, 222)),
    "hinh-42-12": (1436, (34, 444, 192, 540)),
    "hinh-42-13": (1436, (34, 585, 192, 755)),
    "hinh-42-14": (1437, (455, 138, 615, 345)),
    "hinh-42-15": (1438, (34, 134, 192, 285)),
    "hinh-42-16": (1438, (34, 365, 192, 515)),
    "hinh-42-17": (1438, (35, 620, 192, 742)),
    "hinh-42-18": (1439, (450, 125, 615, 295)),
    "hinh-42-19": (1439, (75, 564, 480, 745)),
    "ung-dung-a-4": (1451, (440, 330, 648, 480)),
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
    print(f"Successfully prepared {len(CROPS)} images for chapter 42 theory A.")

if __name__ == "__main__":
    main()
