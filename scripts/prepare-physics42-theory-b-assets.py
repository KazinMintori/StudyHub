"""Extract Chapter 42 Theory B figures (Sections 42.5-42.8, Figures 42.20-42.36 and Bio Application)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-42"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "hinh-42-20": (1441, (455, 195, 613, 325)),
    "hinh-42-21": (1441, (455, 446, 613, 555)),
    "hinh-42-22": (1442, (35, 238, 193, 375)),
    "hinh-42-23": (1442, (35, 612, 193, 748)),
    "hinh-42-24": (1446, (35, 292, 285, 410)),
    "hinh-42-25": (1446, (35, 606, 195, 746)),
    "hinh-42-26": (1447, (455, 295, 615, 635)),
    "hinh-42-27": (1448, (35, 93, 195, 435)),
    "hinh-42-28": (1448, (35, 528, 195, 642)),
    "hinh-42-29": (1449, (455, 103, 614, 370)),
    "hinh-42-30": (1449, (78, 595, 435, 750)),
    "hinh-42-31": (1450, (260, 600, 525, 770)),
    "hinh-42-32": (1451, (455, 143, 613, 320)),
    "hinh-42-33": (1451, (455, 563, 613, 745)),
    "hinh-42-34": (1452, (175, 73, 333, 265)),
    "hinh-42-35": (1452, (355, 103, 575, 265)),
    "hinh-42-36": (1452, (35, 528, 192, 620)),
    "ung-dung-b-1": (1451, (440, 332, 648, 478)),
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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 42 Theory B in {OUT}.")

if __name__ == "__main__":
    main()
