"""Crop Chapter 28 end-of-chapter figures from Young–Freedman 15e.

Coordinates are PDF points on printed pages. The zero-based PDF page index is
the printed page number plus 19. Crops are rendered at 2.5x and trimmed to a
small white border so labels, arrows, and graph axes remain legible.
"""

from pathlib import Path

import pymupdf
from PIL import Image, ImageChops, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-28"
SCALE = 2.5

# stem: (printed page, (left, top, right, bottom))
FIGURES = {
    "hinh-bridge28-30": (944, (360, 295, 520, 415)),
    "hinh-q28-13": (945, (255, 350, 335, 395)),
    "hinh-e28-3": (945, (542, 245, 612, 325)),
    "hinh-e28-4": (945, (420, 370, 550, 425)),
    "hinh-e28-6": (945, (510, 505, 620, 590)),
    "hinh-e28-8": (946, (220, 73, 310, 155)),
    "hinh-e28-9": (946, (180, 198, 290, 260)),
    "hinh-e28-12": (946, (45, 460, 165, 540)),
    "hinh-e28-13": (946, (160, 442, 285, 530)),
    "hinh-e28-19": (946, (460, 350, 570, 440)),
    "hinh-e28-21": (946, (480, 580, 575, 615)),
    "hinh-e28-23": (947, (100, 130, 310, 190)),
    "hinh-e28-24": (947, (215, 220, 345, 300)),
    "hinh-e28-25": (947, (115, 365, 270, 495)),
    "hinh-e28-27": (947, (215, 610, 330, 685)),
    "hinh-e28-28": (947, (490, 75, 630, 148)),
    "hinh-e28-29": (947, (480, 165, 610, 230)),
    "hinh-e28-32": (947, (495, 425, 610, 480)),
    "hinh-e28-33": (947, (495, 500, 612, 575)),
    "hinh-e28-38": (948, (185, 140, 300, 240)),
    "hinh-e28-39": (948, (185, 315, 300, 390)),
    "hinh-p28-49": (948, (460, 300, 595, 410)),
    # Include both wires at y=+a and y=-a; the lower wire's into-page symbol
    # sits below the x-axis and was clipped by the previous y=485 boundary.
    "hinh-p28-58": (949, (225, 405, 330, 515)),
    "hinh-p28-59": (949, (75, 650, 310, 770)),
    "hinh-p28-60": (949, (400, 125, 545, 220)),
    # Retain the lower conductor as well as the two hanging cords.
    "hinh-p28-61": (949, (420, 300, 560, 400)),
    "hinh-p28-62": (949, (520, 415, 612, 485)),
    "hinh-p28-64": (950, (180, 75, 310, 225)),
    "hinh-p28-66": (950, (195, 340, 295, 385)),
    "hinh-p28-68": (950, (180, 595, 280, 675)),
    "hinh-p28-69": (950, (395, 110, 500, 170)),
    # Include the full right ends of both infinite-sheet rows with a clear margin.
    "hinh-p28-70": (950, (465, 190, 580, 270)),
    "hinh-p28-71": (950, (450, 345, 590, 455)),
    "hinh-p28-72": (951, (75, 75, 285, 175)),
    "hinh-p28-74": (951, (265, 380, 335, 430)),
    "hinh-p28-76": (951, (490, 90, 630, 220)),
    "hinh-p28-77": (951, (490, 365, 630, 510)),
    "hinh-p28-79": (952, (180, 75, 300, 175)),
}

# Remove the caption that shares the top edge with the E28.13 diagram.
MASKS = {
    "hinh-e28-3": [(542, 245, 560, 275)],
    "hinh-e28-13": [(160, 442, 225, 460)],
    "hinh-e28-25": [(115, 365, 180, 372)],
    "hinh-e28-6": [(510, 515, 530, 540)],
    "hinh-e28-33": [(495, 500, 510, 520)],
    "hinh-p28-49": [(460, 400, 595, 410)],
}


def trim_white(path: Path) -> None:
    image = Image.open(path).convert("RGB")
    bounds = ImageChops.difference(image, Image.new("RGB", image.size, "white")).getbbox()
    if bounds:
        left, top, right, bottom = bounds
        pad = 5
        image.crop((max(0, left - pad), max(0, top - pad),
                    min(image.width, right + pad), min(image.height, bottom + pad))) \
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
                draw.rectangle((round((left - rect.x0) * SCALE), round((top - rect.y0) * SCALE),
                                round((right - rect.x0) * SCALE), round((bottom - rect.y0) * SCALE)),
                               fill="white")
            image.save(out, optimize=True)
        trim_white(out)
    print(f"Prepared {len(FIGURES)} Chapter 28 exercise figures at {SCALE:g}x in {OUT}")


if __name__ == "__main__":
    main()
