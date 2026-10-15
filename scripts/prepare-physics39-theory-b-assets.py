"""Extract Chapter 39 Theory B figures (Sections 39.3-39.4, Figures 39.15-39.29)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-39"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "hinh-39-15": (1310, (35, 168, 193, 326)),
    "hinh-39-16": (1310, (35, 385, 193, 460)),
    "hinh-39-17": (1311, (455, 88, 608, 163)),
    "hinh-39-18": (1311, (76, 523, 516, 738)),
    "hinh-39-19": (1312, (102, 115, 572, 362)),
    "hinh-39-20": (1312, (80, 555, 240, 718)),
    "hinh-39-21": (1314, (35, 93, 195, 256)),
    "hinh-39-22": (1314, (225, 638, 532, 748)),
    "hinh-39-23": (1315, (455, 86, 612, 232)),
    "hinh-39-24": (1316, (140, 483, 572, 745)),
    "hinh-39-25": (1317, (76, 638, 432, 742)),
    "hinh-39-26": (1318, (34, 595, 196, 709)),
    "hinh-39-27": (1319, (128, 545, 390, 748)),
    "hinh-39-28": (1320, (35, 402, 195, 684)),
    "hinh-39-29": (1322, (34, 95, 554, 245)),
    "hinh-39-29d": (1322, (34, 267, 195, 401)),
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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 39 Theory B in {OUT}.")

if __name__ == "__main__":
    main()
