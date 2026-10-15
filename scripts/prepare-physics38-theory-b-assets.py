"""Extract Chapter 38 Theory B figures (Sections 38.3-38.4, Figures 38.10-38.19)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-38"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "hinh-38-10": (1282, (36, 484, 195, 725)),
    "hinh-38-11": (1282, (235, 638, 545, 742)),
    "hinh-38-12": (1283, (455, 342, 608, 520)),
    "hinh-38-13": (1283, (454, 576, 616, 745)),
    "hinh-38-14": (1284, (36, 432, 195, 725)),
    "hinh-38-15": (1286, (36, 222, 195, 340)),
    "hinh-38-16": (1286, (36, 428, 195, 665)),
    "hinh-38-17": (1287, (85, 60, 430, 230)),
    "hinh-38-18": (1288, (35, 547, 195, 723)),
    "hinh-38-19": (1290, (258, 58, 528, 178)),
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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 38 Theory B in {OUT}.")

if __name__ == "__main__":
    main()
