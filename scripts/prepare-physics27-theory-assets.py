"""Crop Chapter 27 theory figures from the supplied Young & Freedman PDF.

Crop coordinates are PDF points on the printed pages. The PDF page index is
the printed page plus 19. Every output is rendered at 2.5x to keep labels
legible in the lecture page.
"""

from pathlib import Path

import pymupdf
from PIL import Image, ImageChops, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-27"
SCALE = 2.5

# name: (printed page, (left, top, right, bottom))
FIGURES = {
    "mo-chuong": (878, (205, 0, 648, 250)),
    "hinh-27-01": (879, (465, 112, 640, 270)),
    "hinh-27-02": (879, (465, 323, 640, 650)),
    "hinh-27-03": (879, (72, 480, 420, 780)),
    "hinh-27-04": (880, (30, 105, 185, 207)),
    "hinh-27-05": (880, (30, 252, 205, 500)),
    "hinh-27-06": (881, (450, 132, 640, 465)),
    "hinh-27-07": (881, (72, 575, 640, 780)),
    "hinh-27-08": (882, (30, 95, 205, 235)),
    "hinh-27-09": (882, (205, 560, 620, 780)),
    "hinh-27-10": (883, (405, 610, 615, 715)),
    "tu-kiem-tra-27-06": (896, (30, 632, 205, 745)),
    "hinh-27-11": (884, (30, 430, 190, 625)),
    "hinh-27-12": (884, (230, 645, 590, 783)),
    "hinh-27-13": (885, (60, 95, 470, 330)),
    "hinh-27-14": (885, (80, 605, 440, 745)),
    "hinh-27-15": (886, (25, 112, 180, 265)),
    "hinh-27-16": (887, (90, 450, 320, 540)),
    "tu-kiem-tra-27-02": (884, (30, 225, 205, 360)),
    "hinh-27-17": (888, (30, 120, 210, 495)),
    "hinh-27-18": (888, (30, 600, 190, 780)),
    "hinh-27-19": (889, (75, 95, 420, 235)),
    "hinh-27-20": (889, (75, 285, 420, 450)),
    "hinh-27-21": (889, (450, 590, 635, 755)),
    "hinh-27-22": (891, (450, 390, 640, 660)),
    "hinh-27-23": (892, (205, 85, 600, 245)),
    "hinh-27-24": (892, (30, 525, 195, 782)),
    "hinh-27-25": (893, (480, 610, 640, 780)),
    "hinh-27-26": (894, (30, 145, 210, 335)),
    "hinh-27-27": (894, (30, 380, 180, 780)),
    "hinh-27-28": (895, (75, 100, 620, 265)),
    "hinh-27-29": (895, (345, 490, 630, 585)),
    "hinh-27-30": (896, (30, 488, 300, 610)),
    "hinh-27-31": (897, (70, 515, 640, 780)),
    "hinh-27-32": (898, (30, 630, 180, 780)),
    "ung-dung-mri": (898, (0, 248, 192, 395)),
    "hinh-27-33": (899, (450, 365, 640, 475)),
    "hinh-27-34": (899, (450, 565, 640, 750)),
    "hinh-27-35": (900, (135, 215, 275, 310)),
    "hinh-27-36": (900, (30, 555, 205, 780)),
    "hinh-27-37": (901, (450, 138, 640, 430)),
    "hinh-27-38": (901, (450, 595, 640, 780)),
    "hinh-27-39": (902, (85, 535, 640, 760)),
    "hinh-27-40": (903, (440, 200, 648, 325)),
    "hinh-27-41": (904, (30, 325, 205, 700)),
    "ung-dung-tom-hum": (880, (38, 640, 190, 765)),
    "ung-dung-tu-truong-co-the": (882, (0, 380, 192, 535)),
    "ung-dung-may-cheo-thuyen": (905, (450, 220, 648, 365)),
    "tu-kiem-tra-27-09": (905, (450, 650, 570, 760)),
    "tom-tat-luc-tu": (906, (450, 90, 570, 155)),
    "tom-tat-tu-thong": (906, (447, 183, 540, 250)),
    "tom-tat-chuyen-dong": (906, (435, 303, 560, 390)),
    "tom-tat-luc-len-day": (906, (448, 430, 515, 500)),
    "tom-tat-vong-day": (906, (440, 525, 565, 620)),
    "tom-tat-dong-co": (906, (448, 615, 560, 725)),
    "tom-tat-hall": (907, (480, 75, 610, 150)),
}

ROTATE = {"tu-kiem-tra-27-09": 180}

MASKS = {
    # This panel description is printed between the orbital sketch and photo.
    "hinh-27-17": [(30, 310, 210, 343)],
    # These panel titles sit outside the two velocity-selector diagrams.
    "hinh-27-22": [(450, 390, 640, 405), (450, 585, 640, 601)],
    # Remove the separate figure caption while retaining the diagram's labels.
    "hinh-27-29": [(345, 490, 630, 500)],
    # This line belongs to the preceding paragraph, above the Figure 27.32 art.
    "hinh-27-32": [(30, 630, 180, 653)],
    "hinh-27-26": [(30, 145, 210, 160)],
    # The (c) panel heading is outside the magnetic-field diagrams.
    "hinh-27-13": [(60, 220, 470, 238)],
    # The horizontal summary separator is outside the motor diagram.
    "tom-tat-dong-co": [(448, 615, 560, 642)],
    # Mask the Figure 27.16 panel headings while retaining the arrow tips.
    "hinh-27-16": [(90, 450, 320, 462), (220, 460, 320, 472)],
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
        pix.save(out_path)
        if name in MASKS:
            with Image.open(out_path) as image:
                image = image.convert("RGB")
                draw = ImageDraw.Draw(image)
                for left, top, right, bottom in MASKS[name]:
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
        if name in ROTATE:
            with Image.open(out_path) as image:
                image.rotate(ROTATE[name], expand=True).save(out_path)
        with Image.open(out_path) as image:
            image = image.convert("RGB")
            difference = ImageChops.difference(image, Image.new("RGB", image.size, "white"))
            bounds = difference.getbbox()
            if bounds:
                left, top, right, bottom = bounds
                padding = round(5 * SCALE)
                bounds = (
                    max(0, left - padding),
                    max(0, top - padding),
                    min(image.width, right + padding),
                    min(image.height, bottom + padding),
                )
                image.crop(bounds).save(out_path, optimize=True)
    print(f"Prepared {len(FIGURES)} Chapter 27 theory crops at {SCALE:g}x in {OUT}")


if __name__ == "__main__":
    main()
