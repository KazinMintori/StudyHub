"""Crop Chapter 29 figures and application images from the source PDF.

Run from the StudyHub repository root with Python and PyMuPDF installed.
The crop rectangles are page coordinates in points, with a margin added by the
script so labels, arrowheads, and captions near each illustration remain visible.
"""
from pathlib import Path
import fitz

SOURCE = Path("raw_materials/physics/source/young-freedman-15.pdf")
OUTPUT = Path("docs/vat-ly-2/bai-giang/img/young-29")
OUTPUT.mkdir(parents=True, exist_ok=True)

# Keys are output stems. Values are (one-based PDF page number, x0, y0, x1, y1)
# in the 648 x 783 point page coordinate system. Boxes include the full artwork
# while excluding adjacent prose where practical.
CROPS = {
    "mo-chuong-the-doc": (973, 0, 0, 355, 260),
    "ung-dung-kich-thich-tu-xuyen-so": (974, 0, 160, 285, 490),
    "hinh-29-01": (974, 25, 500, 620, 770),
    "hinh-29-02": (975, 434, 67, 600, 265),
    "hinh-29-03": (975, 405, 550, 620, 745),
    "hinh-29-04": (976, 20, 50, 620, 285),
    "hinh-29-05": (976, 380, 440, 620, 700),
    "hinh-29-06": (977, 20, 430, 620, 755),
    "hinh-29-07": (978, 330, 590, 550, 775),
    "hinh-29-08": (979, 55, 570, 620, 770),
    "hinh-29-09": (980, 307, 66, 614, 277),
    "hinh-29-10": (980, 25, 530, 620, 755),
    "hinh-29-11": (981, 342, 77, 602, 312),
    "hinh-29-12": (981, 340, 470, 620, 680),
    "hinh-29-13": (983, 420, 560, 620, 755),
    "hinh-29-14": (984, 28, 74, 616, 265),
    "hinh-29-15": (985, 443, 72, 610, 364),
    "hinh-29-16": (986, 27, 67, 468, 401),
    "hinh-29-17": (987, 65, 70, 318, 402),
}

MARGIN = 9
SCALE = 2.0

def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found: {SOURCE}")
    doc = fitz.open(SOURCE)
    for stem, (page_number, x0, y0, x1, y1) in CROPS.items():
        page = doc[page_number - 1]
        rect = fitz.Rect(x0, y0, x1, y1) + (-MARGIN, -MARGIN, MARGIN, MARGIN)
        rect &= page.rect
        pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=rect, alpha=False)
        pix.save(OUTPUT / f"{stem}.png")
        print(f"{stem}: PDF p.{page_number}, crop={tuple(round(v, 1) for v in rect)}")
    print(f"Wrote {len(CROPS)} crops to {OUTPUT}")

if __name__ == "__main__":
    main()





