"""Crop source figures for Chapter 11 sections 11.4, 11.5 and the chapter summary.

All rectangles are in PDF points on the 1-based PDF pages of young-freedman-15.pdf.
Output images are stored as flat PNGs in docs/vat-ly-1/bai-giang/img/young-11/
with exclusive prefix 'b-'.
"""

from pathlib import Path
import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-11"
SCALE = 2.5

# Dict mapping basename -> (PDF1based, (x0, y0, x1, y1))
CROPS = {
    "b-hinh-11-12.png": (365, (452, 366, 615, 742)),
    "b-hinh-11-13.png": (365, (175, 635, 340, 742)),
    "b-hinh-11-14.png": (366, (32, 215, 202, 415)),
    "b-ung-dung-11-gan-chan.png": (366, (32, 545, 202, 742)),
    "b-hinh-11-15.png": (367, (455, 400, 615, 565)),
    "b-hinh-11-16.png": (367, (80, 625, 435, 742)),
    "b-ung-dung-11-ca-can-cau.png": (368, (32, 540, 196, 735)),
    "b-hinh-11-17.png": (369, (452, 114, 615, 341)),
    "b-hinh-11-18.png": (370, (32, 123, 202, 368)),
    "b-hinh-11-19.png": (371, (452, 295, 618, 465)),
    "b-hinh-11-20.png": (371, (452, 611, 618, 742)),
    "b-tom-tat-11-can-bang.png": (373, (485, 70, 615, 225)),
    "b-tom-tat-11-keo-nen.png": (373, (485, 290, 615, 395)),
    "b-tom-tat-11-the-tich.png": (373, (485, 400, 615, 515)),
    "b-tom-tat-11-truot.png": (373, (485, 525, 615, 615)),
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    print(f"Opening {PDF}...")
    for name, (p1, box) in CROPS.items():
        page = doc[p1 - 1]
        rect = pymupdf.Rect(box)
        if not page.rect.contains(rect):
            raise ValueError(f"Crop {name} outside PDF page {p1}: {rect} vs {page.rect}")
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(SCALE, SCALE),
            clip=rect,
            alpha=False,
        )
        target = OUT / name
        pix.save(str(target))
        with Image.open(target) as img:
            w, h = img.size
        print(f"Saved {name:30s} -> {w}x{h} px from page {p1}")
    print(f"Successfully generated {len(CROPS)} assets in {OUT}")


if __name__ == "__main__":
    main()
