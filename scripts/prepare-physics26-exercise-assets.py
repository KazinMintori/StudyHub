"""Crop exercise figures cited by raw Chapter 26 exercise files.

Coordinates are PDF points on the printed pages. Source page numbers are mapped
to zero-based PDF indices with the book's +19 offset. Crops render at 2.5x.
Only hinh-e26-*.png and hinh-p26-*.png in the Chapter 26 lecture image folder
are written by this script.
"""

from pathlib import Path

import pymupdf
from PIL import Image, ImageChops, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-26"
SCALE = 2.5

# filename: (printed page, (left, top, right, bottom))
# Figure rectangles contain the complete circuit, graph, or multi-panel art
# while excluding the adjacent exercise prose and the separate figure caption.
FIGURES = {
    "hinh-e26-01": (870, (205, 530, 310, 562)),
    "hinh-e26-02": (870, (175, 586, 300, 640)),
    "hinh-e26-05": (870, (490, 82, 570, 128)),
    "hinh-e26-06": (870, (450, 166, 610, 236)),
    "hinh-e26-07": (870, (385, 264, 490, 342)),
    "hinh-e26-11": (870, (380, 642, 510, 712)),
    "hinh-e26-13": (871, (70, 122, 255, 181)),
    "hinh-e26-14": (871, (70, 254, 255, 314)),
    "hinh-e26-15": (871, (255, 344, 335, 397)),
    "hinh-e26-16": (871, (70, 530, 270, 613)),
    "hinh-e26-17": (871, (115, 692, 230, 760)),
    "hinh-e26-18": (871, (510, 76, 625, 151)),
    "hinh-e26-19": (871, (510, 188, 625, 254)),
    "hinh-e26-20": (871, (510, 276, 625, 345)),
    "hinh-e26-22": (871, (360, 551, 610, 605)),
    "hinh-e26-23": (871, (360, 662, 610, 733)),
    "hinh-e26-24": (872, (35, 103, 290, 158)),
    "hinh-e26-25": (872, (80, 214, 245, 284)),
    "hinh-e26-26": (872, (115, 324, 245, 405)),
    "hinh-e26-29": (872, (35, 570, 280, 620)),
    "hinh-e26-30": (872, (100, 675, 230, 750)),
    "hinh-e26-31": (872, (455, 78, 625, 151)),
    "hinh-e26-32": (872, (335, 225, 520, 325)),
    "hinh-e26-34": (872, (515, 430, 620, 485)),
    "hinh-e26-41": (873, (75, 370, 270, 435)),
    "hinh-e26-45": (873, (80, 670, 260, 757)),
    "hinh-e26-47": (873, (345, 186, 625, 300)),
    "hinh-e26-49": (873, (510, 360, 630, 454)),
    "hinh-p26-54": (874, (175, 225, 300, 300)),
    "hinh-p26-56": (874, (235, 365, 290, 395)),
    "hinh-p26-57": (874, (35, 455, 280, 520)),
    "hinh-p26-58": (874, (155, 551, 300, 640)),
    "hinh-p26-59": (874, (185, 676, 300, 760)),
    "hinh-p26-60": (874, (470, 79, 625, 132)),
    "hinh-p26-62": (874, (445, 245, 575, 300)),
    "hinh-p26-63": (874, (375, 387, 555, 515)),
    "hinh-p26-64": (874, (440, 530, 570, 595)),
    "hinh-p26-66": (875, (70, 122, 270, 230)),
    "hinh-p26-67": (875, (245, 246, 350, 330)),
    "hinh-p26-69": (875, (194, 456, 350, 552)),
    "hinh-p26-70": (875, (210, 677, 335, 765)),
    "hinh-p26-71": (875, (488, 78, 625, 150)),
    "hinh-p26-73": (875, (520, 321, 625, 350)),
    "hinh-p26-74": (875, (507, 408, 642, 502)),
    "hinh-p26-75": (875, (505, 583, 625, 655)),
    "hinh-p26-78": (876, (50, 235, 275, 328)),
    "hinh-p26-81": (876, (305, 147, 520, 225)),
    "hinh-p26-82": (876, (305, 378, 520, 455)),
    "hinh-p26-83": (876, (340, 554, 515, 615)),
    "hinh-p26-84": (876, (305, 690, 615, 755)),
}

# Small source-caption masks are applied only where a figure caption shares a
# horizontal band with the drawing. Coordinates remain in PDF points.
MASKS = {
    "hinh-e26-29": [(35, 560, 106, 578)],
    "hinh-e26-32": [(335, 225, 367, 237)],
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
        out_path = OUT / f"{name}.png"
        if name in MASKS:
            image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            draw = ImageDraw.Draw(image)
            for mask in MASKS[name]:
                left, top, right, bottom = mask
                draw.rectangle(
                    (
                        round((left - rect.x0) * SCALE),
                        round((top - rect.y0) * SCALE),
                        round((right - rect.x0) * SCALE),
                        round((bottom - rect.y0) * SCALE),
                    ),
                    fill="white",
                )
            image.save(out_path, optimize=True)
        else:
            pix.save(out_path)
        image = Image.open(out_path).convert("RGB")
        difference = ImageChops.difference(image, Image.new("RGB", image.size, "white"))
        bounds = difference.getbbox()
        if bounds:
            padding = 5
            left, top, right, bottom = bounds
            bounds = (
                max(0, left - padding),
                max(0, top - padding),
                min(image.width, right + padding),
                min(image.height, bottom + padding),
            )
            image.crop(bounds).save(out_path, optimize=True)
    print(f"Prepared {len(FIGURES)} Chapter 26 exercise crops at {SCALE:g}x in {OUT}")


if __name__ == "__main__":
    main()
