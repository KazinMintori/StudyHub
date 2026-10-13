"""Crop the source exercise figures used by Chapter 27's raw exercise files.

Coordinates are PDF points on printed pages. The book PDF page index equals
the printed page plus 19. Crops render at 2.5x and are trimmed to 5 px of
white space after any caption/prose masks are applied.
"""

from pathlib import Path

import pymupdf
from PIL import Image, ImageChops, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-27"
SCALE = 2.5

# asset stem: (printed page, (left, top, right, bottom))
# Rectangles exclude prose and figure captions, but retain diagram labels,
# arrows, units, graph ticks, and complete circuit/cube boundaries.
FIGURES = {
    "hinh-q27-12": (908, (443, 607, 645, 780)),
    "hinh-e27-13": (909, (495, 343, 640, 430)),
    "hinh-e27-14": (909, (495, 488, 620, 558)),
    "hinh-e27-19": (910, (225, 170, 305, 250)),
    "hinh-e27-22": (910, (205, 407, 300, 485)),
    "hinh-e27-25": (910, (165, 669, 310, 760)),
    "hinh-e27-29": (910, (445, 360, 640, 465)),
    "hinh-e27-31": (910, (455, 565, 640, 638)),
    "hinh-e27-33": (911, (225, 75, 340, 165)),
    "hinh-e27-37": (911, (35, 645, 285, 775)),
    "hinh-e27-38": (911, (500, 76, 635, 150)),
    "hinh-e27-39": (911, (420, 310, 625, 400)),
    "hinh-e27-40": (911, (540, 435, 615, 490)),
    "hinh-e27-41": (911, (495, 558, 615, 608)),
    "hinh-e27-43": (912, (105, 165, 220, 242)),
    "hinh-e27-45": (912, (75, 430, 240, 500)),
    "hinh-p27-55": (913, (235, 78, 390, 150)),
    "hinh-p27-56": (913, (78, 292, 290, 356)),
    "hinh-p27-59": (913, (375, 77, 615, 158)),
    "hinh-p27-63": (913, (420, 630, 620, 760)),
    "hinh-p27-64": (914, (35, 178, 225, 330)),
    "hinh-p27-65": (914, (25, 440, 220, 590)),
    "hinh-p27-66": (914, (235, 615, 290, 690)),
    "hinh-p27-67": (914, (365, 230, 530, 320)),
    "hinh-p27-69": (914, (375, 500, 495, 595)),
    "hinh-p27-70": (914, (500, 615, 575, 720)),
    "hinh-p27-71": (915, (235, 75, 340, 170)),
    "hinh-p27-72": (915, (270, 255, 340, 330)),
    "hinh-p27-73": (915, (220, 385, 345, 525)),
    "hinh-p27-77": (915, (490, 604, 635, 685)),
    "hinh-p27-78": (916, (85, 220, 230, 390)),
    "hinh-p27-81": (916, (300, 270, 635, 466)),
    "hinh-p27-82": (916, (325, 630, 590, 773)),
    "mcat-spin": (917, (360, 60, 600, 195)),
}

# Caption fragments that share a crop edge, removed without altering the art.
MASKS = {}


def trim_white(path: Path) -> None:
    image = Image.open(path).convert("RGB")
    bounds = ImageChops.difference(image, Image.new("RGB", image.size, "white")).getbbox()
    if bounds:
        left, top, right, bottom = bounds
        pad = 5
        image.crop((max(0, left-pad), max(0, top-pad),
                    min(image.width, right+pad), min(image.height, bottom+pad))) \
             .save(path, optimize=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    for stem, (printed_page, coordinates) in FIGURES.items():
        page = doc[printed_page + 19]
        rect = pymupdf.Rect(coordinates)
        if not page.rect.contains(rect):
            raise ValueError(f"Crop outside printed page {printed_page}: {stem} {rect}")
        pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=rect, alpha=False)
        out = OUT / f"{stem}.png"
        pix.save(out)
        if stem in MASKS:
            image = Image.open(out).convert("RGB")
            draw = ImageDraw.Draw(image)
            for left, top, right, bottom in MASKS[stem]:
                draw.rectangle((round((left-rect.x0)*SCALE), round((top-rect.y0)*SCALE),
                                round((right-rect.x0)*SCALE), round((bottom-rect.y0)*SCALE)),
                               fill="white")
            image.save(out, optimize=True)
        trim_white(out)
    print(f"Prepared {len(FIGURES)} Chapter 27 exercise figures at {SCALE:g}x in {OUT}")


if __name__ == "__main__":
    main()
