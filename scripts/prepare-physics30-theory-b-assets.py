"""Crop the original figures for Chapter 30 sections 30.4–30.6 and the summary.

Coordinates use PDF points on the printed page. Captions outside the figure
art are excluded; English text embedded in the illustrations is retained and
translated in docs/.vitepress/physics30-theory-b-image-annotations.mjs.
"""

from pathlib import Path

import pymupdf
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
PDF = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
if not PDF.exists():
    PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-30"
SCALE = 2.5

# name: (printed page, (left, top, right, bottom))
FIGURES = {
    "hinh-30-11": (999, (445, 92, 615, 265)),
    "hinh-30-12": (999, (455, 535, 615, 755)),
    "hinh-30-13": (1001, (455, 497, 615, 675)),
    "hinh-30-14": (1003, (75, 95, 615, 415)),
    "hinh-30-15": (1004, (75, 150, 160, 275)),
    "bang-30-01": (1005, (450, 305, 610, 620)),
    "hinh-30-16": (1007, (445, 120, 615, 470)),
    "hinh-30-17": (1007, (450, 524, 615, 745)),
    "tom-tat-30-01-ho-cam": (1009, (490, 90, 610, 180)),
    "tom-tat-30-02-tu-cam": (1009, (485, 210, 610, 287)),
    "tom-tat-30-03-nang-luong-tu-truong": (1009, (490, 300, 610, 385)),
    "tom-tat-30-04-mach-rl": (1009, (485, 400, 605, 475)),
    "tom-tat-30-05-mach-lc": (1009, (490, 480, 610, 560)),
    "tom-tat-30-06-mach-rlc": (1009, (490, 570, 610, 650)),
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    for name, (printed_page, box) in FIGURES.items():
        # PyMuPDF page indices are zero-based; the PDF index is printed page + 19.
        page = doc[printed_page + 19]
        rect = pymupdf.Rect(box)
        if not page.rect.contains(rect):
            raise ValueError(f"Crop outside printed page {printed_page}: {name} {rect}")
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(SCALE, SCALE),
            clip=rect,
            alpha=False,
        )
        output = OUT / f"{name}.png"
        pix.save(output)
        with Image.open(output) as opened:
            image = opened.convert("RGB")
            difference = ImageChops.difference(image, Image.new("RGB", image.size, "white"))
            bounds = difference.getbbox()
            if bounds:
                padding = round(5 * SCALE)
                left, top, right, bottom = bounds
                bounds = (
                    max(0, left - padding),
                    max(0, top - padding),
                    min(image.width, right + padding),
                    min(image.height, bottom + padding),
                )
                image.crop(bounds).save(output, optimize=True)
    print(f"Prepared {len(FIGURES)} Chapter 30 figures at {SCALE:g}x in {OUT}")


if __name__ == "__main__":
    main()
