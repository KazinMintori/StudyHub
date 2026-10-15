"""Extract Chapter 34 Theory B figures (Sections 34.5-34.8, Figures 34.40-34.54)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-34"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "hinh-34-40": (1155, (75, 590, 445, 745)),
    "hinh-34-41": (1156, (35, 118, 572, 230)),
    "hinh-34-42": (1157, (455, 364, 608, 590)),
    "hinh-34-43": (1157, (75, 635, 565, 745)),
    "hinh-34-44": (1158, (120, 552, 570, 745)),
    "hinh-34-45": (1159, (455, 428, 612, 745)),
    "hinh-34-46": (1160, (245, 58, 575, 238)),
    "hinh-34-47": (1160, (85, 272, 575, 465)),
    "hinh-34-48": (1160, (215, 598, 570, 740)),
    "hinh-34-49": (1161, (350, 304, 615, 395)),
    "hinh-34-50": (1161, (310, 652, 608, 738)),
    "hinh-34-51": (1162, (125, 610, 572, 755)),
    "hinh-34-52": (1164, (78, 105, 572, 385)),
    "hinh-34-53": (1165, (75, 478, 565, 728)),
    "hinh-34-54": (1167, (78, 85, 572, 325)),
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
    print(f"Successfully prepared 15 images for Chapter 34 Theory B in {OUT}.")

if __name__ == "__main__":
    main()
