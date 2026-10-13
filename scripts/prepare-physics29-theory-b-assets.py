"""Crop the original figures for Chapter 29 sections 29.5–29.8.

Coordinates use PDF points on the printed page. Captions outside the figure
art are excluded; English text embedded in the illustrations is retained and
translated in docs/.vitepress/physics29-theory-b-image-annotations.mjs.
"""

from pathlib import Path

import pymupdf
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-29"
SCALE = 2.5

# name: (printed page, (left, top, right, bottom))
FIGURES = {
    "hinh-29-18": (967, (451, 485, 630, 780)),
    "hinh-29-19": (968, (22, 505, 205, 760)),
    "hinh-29-20": (969, (450, 440, 620, 780)),
    "hinh-29-21": (970, (210, 107, 580, 270)),
    "ung-dung-io": (970, (30, 440, 195, 620)),
    "hinh-29-22": (971, (450, 219, 620, 365)),
    "hinh-29-23": (972, (25, 340, 200, 550)),
    "hinh-29-24": (974, (25, 110, 205, 415)),
    "hinh-29-25": (975, (470, 162, 615, 280)),
    "hinh-29-26": (975, (30, 614, 620, 780)),
    "hinh-29-27": (976, (20, 94, 200, 240)),
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
    print(f"Prepared {len(FIGURES)} Chapter 29 figures at {SCALE:g}x in {OUT}")


if __name__ == "__main__":
    main()
