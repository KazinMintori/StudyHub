"""Crop chapter 39 sections 39.1-39.2 figures (Figures 39.1-39.14) without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-39"

CROPS = {
    "hinh-39-01": (1300, (34, 146, 194, 360)),
    "hinh-39-02": (1300, (235, 572, 555, 746)),
    "hinh-39-03": (1301, (454, 125, 616, 472)),
    "hinh-39-04": (1301, (454, 610, 648, 746)),
    "hinh-39-05": (1304, (34, 358, 196, 615)),
    "hinh-39-06": (1305, (454, 175, 648, 314)),
    "hinh-39-07": (1305, (105, 552, 405, 744)),
    "hinh-39-08": (1306, (268, 105, 512, 242)),
    "hinh-39-09": (1306, (0, 592, 194, 744)),
    "hinh-39-10": (1307, (454, 166, 614, 300)),
    "hinh-39-11": (1307, (78, 526, 420, 746)),
    "hinh-39-12": (1308, (34, 84, 196, 265)),
    "hinh-39-13": (1308, (215, 448, 560, 595)),
    "hinh-39-14": (1309, (454, 365, 615, 660)),
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
    print(f"Successfully prepared {len(CROPS)} images for chapter 39 theory A.")

if __name__ == "__main__":
    main()
