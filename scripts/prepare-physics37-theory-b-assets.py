"""Extract Chapter 37 Theory B figures (Sections 37.5-37.9, Figures 37.15-37.25)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-37"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "hinh-37-15": (1252, (35, 95, 195, 278)),
    "hinh-37-16": (1254, (330, 403, 565, 495)),
    "hinh-37-17": (1255, (105, 638, 425, 745)),
    "hinh-37-18": (1256, (36, 256, 192, 362)),
    "hinh-37-19": (1256, (320, 454, 562, 628)),
    "hinh-37-20": (1257, (452, 490, 615, 668)),
    "hinh-37-21": (1260, (35, 385, 195, 592)),
    "hinh-37-22": (1262, (85, 450, 245, 582)),
    "hinh-37-23": (1263, (455, 225, 612, 742)),
    "hinh-37-24": (1264, (258, 62, 525, 222)),
    "hinh-37-25": (1264, (36, 244, 192, 422)),
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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 37 Theory B in {OUT}.")

if __name__ == "__main__":
    main()
