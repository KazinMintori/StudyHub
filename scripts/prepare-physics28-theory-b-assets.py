"""Crop source figures for Chapter 28 sections 28.5–28.8 and the full summary.

All rectangles are in PDF points on the printed pages.  The output is kept to
the complete figure art and its embedded labels; surrounding prose and printed
figure captions are excluded where they sit outside the artwork.
"""

from pathlib import Path

import pymupdf
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-28"
SCALE = 2.5

# name: (printed page, (left, top, right, bottom))
FIGURES = {
    "hinh-28-11": (927, (452, 585, 615, 780)),
    "hinh-28-12": (928, (28, 144, 205, 275)),
    "hinh-28-13": (928, (28, 375, 205, 495)),
    "hinh-28-14": (928, (28, 620, 205, 755)),
    "hinh-28-15": (929, (282, 350, 422, 490)),
    "ung-dung-mri-28": (929, (455, 245, 615, 390)),
    "hinh-28-16": (931, (452, 125, 615, 690)),
    "hinh-28-17": (932, (275, 55, 615, 200)),
    "hinh-28-18": (932, (28, 168, 205, 555)),
    "hinh-28-19": (932, (28, 650, 205, 745)),
    "hinh-28-20": (934, (68, 610, 300, 700)),
    "hinh-28-21": (934, (308, 515, 575, 640)),
    "hinh-28-22": (935, (74, 335, 338, 480)),
    "hinh-28-23": (935, (73, 588, 285, 700)),
    "hinh-28-24": (935, (348, 505, 612, 652)),
    "hinh-28-25": (936, (308, 120, 612, 270)),
    "ung-dung-cap-dong-truc": (936, (0, 500, 205, 680)),
    "hinh-28-26": (937, (452, 310, 615, 455)),
    "bang-28-01": (939, (452, 106, 615, 310)),
    "hinh-28-27": (940, (30, 125, 205, 410)),
    "hinh-28-28": (940, (30, 472, 205, 560)),
    "hinh-28-29": (940, (30, 615, 615, 779)),
    "ung-dung-nano-sat-ung-thu": (941, (454, 220, 615, 424)),
    "tom-tat-28-01-dien-tich-chuyen-dong": (942, (445, 92, 540, 152)),
    "tom-tat-28-02-biot-savart": (942, (445, 218, 540, 282)),
    "tom-tat-28-03-day-thang": (942, (445, 325, 540, 391)),
    "tom-tat-28-04-luc-giua-day": (942, (445, 421, 540, 510)),
    "tom-tat-28-05-vong-dong": (942, (452, 530, 615, 612)),
    "tom-tat-28-06-ampere": (942, (450, 650, 515, 690)),
    "tom-tat-28-bang-phan-bo-dong": (943, (75, 62, 615, 299)),
    "tom-tat-28-tu-tinh": (943, (492, 307, 545, 393)),
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    for name, (printed_page, box) in FIGURES.items():
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
        # Trim only blank paper inside the crop while retaining the complete figure.
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
    print(f"Prepared {len(FIGURES)} Chapter 28 theory crops at {SCALE:g}x in {OUT}")


if __name__ == "__main__":
    main()
