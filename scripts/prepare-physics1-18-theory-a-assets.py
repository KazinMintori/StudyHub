"""Crop Chapter 18 sections 18.1-18.3 figures without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-18"

CROPS = {
    "a-mo-dau-18": (599, (0, 0, 438, 246)),
    "a-hinh-18-01": (600, (35, 485, 198, 768)),
    "a-hinh-18-02": (601, (455, 155, 615, 310)),
    "a-ung-dung-18-01": (601, (458, 545, 620, 742)),
    "a-hinh-18-03": (603, (80, 95, 325, 242)),
    "a-hinh-18-04": (604, (355, 84, 525, 238)),
    "a-hinh-18-05": (604, (35, 345, 197, 588)),
    "a-hinh-18-06": (605, (455, 124, 615, 255)),
    "a-hinh-18-07": (605, (455, 370, 615, 525)),
    "a-hinh-18-08": (606, (35, 95, 195, 385)),
    "a-hinh-18-09": (606, (35, 558, 272, 742)),
    "a-hinh-18-10": (606, (362, 582, 520, 735)),
    "a-hinh-18-11": (608, (35, 550, 185, 742)),
    "a-hinh-18-12": (609, (455, 138, 610, 308)),
    "a-hinh-18-13": (610, (35, 108, 193, 435)),
    "a-hinh-18-14": (611, (455, 330, 615, 458)),
    "a-hinh-18-15": (612, (35, 642, 195, 742)),
    "a-hinh-18-16": (613, (455, 438, 615, 584)),
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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 18 Theory A.")

if __name__ == "__main__":
    main()
