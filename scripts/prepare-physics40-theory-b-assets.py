"""Extract Chapter 40 Theory B figures (Sections 40.2-40.3, Figures 40.8-40.17)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-40"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "hinh-40-08": (1351, (452, 362, 612, 508)),
    "hinh-40-09": (1351, (452, 552, 612, 680)),
    "hinh-40-10": (1352, (36, 95, 195, 295)),
    "hinh-40-11": (1353, (78, 565, 435, 745)),
    "hinh-40-12": (1354, (36, 480, 195, 752)),
    "hinh-40-13": (1356, (36, 312, 195, 448)),
    "hinh-40-14": (1357, (452, 358, 612, 465)),
    "hinh-40-15": (1358, (210, 124, 570, 280)),
    "hinh-40-16": (1358, (36, 587, 195, 750)),
    "hinh-40-17": (1359, (150, 194, 367, 336)),
}

SCALE = 3.0

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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 40 Theory B in {OUT}.")

if __name__ == "__main__":
    main()
