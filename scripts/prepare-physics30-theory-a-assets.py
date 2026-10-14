"""Crop Chapter 30 theory A figures and application images from the source PDF.

Run from the StudyHub repository root with Python and PyMuPDF installed.
The crop rectangles are page coordinates in points, with a margin added by the
script so labels, arrowheads, and artwork near each illustration remain intact.
"""
from pathlib import Path
import fitz

LOCAL_SOURCE = Path("raw_materials/physics/source/young-freedman-15.pdf")
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUTPUT = Path("docs/vat-ly-2/bai-giang/img/young-30")
OUTPUT.mkdir(parents=True, exist_ok=True)

# Keys are output stems. Values are (one-based PDF page number, x0, y0, x1, y1)
# in the 648 x 783 point page coordinate system. Boxes include the full artwork
# while excluding adjacent prose where practical.
CROPS = {
    "mo-dau-30": (1008, 210, 0, 648, 245),
    "hinh-30-01": (1009, 473, 105, 592, 284),
    "hinh-30-02": (1009, 456, 477, 612, 715),
    "hinh-30-03": (1010, 345, 624, 535, 735),
    "hinh-30-04": (1012, 38, 264, 190, 370),
    "ung-dung-30a-chong-set": (1012, 0, 598, 193, 741),
    "hinh-30-05": (1013, 456, 224, 612, 360),
    "hinh-30-06": (1013, 454, 468, 612, 748),
    "hinh-30-07": (1014, 36, 122, 192, 235),
    "hinh-30-08": (1014, 365, 637, 513, 746),
    "hinh-30-09": (1016, 38, 517, 185, 627),
    "ung-dung-30a-nhat-hoa": (1017, 456, 258, 648, 425),
    "hinh-30-10": (1017, 456, 634, 612, 745),
}

MARGIN = 2
SCALE = 2.5

def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found at {LOCAL_SOURCE} or {MAIN_SOURCE}")
    doc = fitz.open(SOURCE)
    for stem, (page_number, x0, y0, x1, y1) in CROPS.items():
        page = doc[page_number - 1]
        rect = fitz.Rect(x0, y0, x1, y1) + (-MARGIN, -MARGIN, MARGIN, MARGIN)
        rect &= page.rect
        pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=rect, alpha=False)
        target_path = OUTPUT / f"{stem}.png"
        pix.save(target_path)
        print(f"{stem}: PDF p.{page_number}, crop={tuple(round(v, 1) for v in rect)}, size={pix.width}x{pix.height}")
    print(f"Wrote {len(CROPS)} crops to {OUTPUT}")

if __name__ == "__main__":
    main()
