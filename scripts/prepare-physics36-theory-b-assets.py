"""Extract Chapter 36 Theory B figures (Sections 36.5-36.8, Figures 36.16-36.30)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-36"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "hinh-36-16": (1217, (455, 95, 612, 275)),
    "hinh-36-17": (1217, (455, 363, 612, 518)),
    "hinh-36-18": (1218, (35, 390, 195, 750)),
    "hinh-36-19": (1219, (75, 55, 445, 320)),
    "hinh-36-20": (1220, (110, 570, 570, 750)),
    "hinh-36-21": (1221, (455, 115, 620, 305)),
    "hinh-36-22": (1221, (75, 610, 585, 755)),
    "hinh-36-23": (1222, (210, 55, 570, 195)),
    "hinh-36-24": (1222, (35, 300, 195, 488)),
    "hinh-36-25": (1223, (130, 580, 390, 745)),
    "hinh-36-26": (1224, (35, 88, 195, 222)),
    "hinh-36-27": (1224, (35, 415, 195, 745)),
    "hinh-36-28": (1226, (80, 95, 575, 315)),
    "hinh-36-29": (1227, (26, 114, 512, 308)),
    "hinh-36-30": (1227, (455, 340, 613, 748)),
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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 36 Theory B in {OUT}.")

if __name__ == "__main__":
    main()
