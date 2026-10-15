"""Crop chapter 33 opening and sections 33.1-33.4 figures without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-33"

CROPS = {
    "mo-dau-33": (1097, (0, 0, 439, 246)),
    "hinh-33-01": (1098, (36, 185, 193, 291)),
    "hinh-33-02": (1098, (36, 489, 193, 635)),
    "hinh-33-03": (1099, (456, 134, 612, 335)),
    "hinh-33-04": (1099, (456, 386, 612, 665)),
    "hinh-33-05": (1100, (115, 114, 572, 368)),
    "hinh-33-06": (1100, (36, 548, 192, 742)),
    "hinh-33-07": (1101, (455, 84, 613, 325)),
    "hinh-33-08": (1101, (455, 478, 613, 745)),
    "hinh-33-09": (1102, (180, 105, 572, 240)),
    "hinh-33-10": (1102, (220, 595, 565, 742)),
    "ung-dung-33-do-trong-suot-au-trung": (1102, (36, 452, 192, 565)),
    "hinh-33-11": (1104, (75, 222, 265, 320)),
    "hinh-33-12": (1105, (350, 55, 610, 230)),
    "hinh-33-13": (1105, (75, 575, 435, 745)),
    "hinh-33-14": (1106, (265, 540, 520, 770)),
    "hinh-33-15": (1107, (455, 95, 612, 242)),
    "hinh-33-16": (1107, (455, 290, 612, 520)),
    "hinh-33-17": (1108, (36, 300, 192, 505)),
    "hinh-33-18": (1108, (245, 605, 535, 742)),
    "hinh-33-19": (1109, (75, 248, 545, 745)),
}

SCALE = 2.5

def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found at {LOCAL_SOURCE} or {MAIN_SOURCE}")
    OUT.mkdir(parents=True, exist_ok=True)
    with fitz.open(SOURCE) as pdf:
        for stem, (page_num, box) in CROPS.items():
            page = pdf[page_num - 1]
            rect = fitz.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=rect, alpha=False)
            target = OUT / f"{stem}.png"
            pix.save(target)
            print(f"Saved {stem}: p.{page_num}, box={box}, size={pix.width}x{pix.height}")
    print(f"Successfully prepared {len(CROPS)} images for chapter 33 theory A.")

if __name__ == "__main__":
    main()
