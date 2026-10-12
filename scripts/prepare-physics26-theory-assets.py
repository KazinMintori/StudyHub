"""Crop Chapter 26 theory figures from the local Young & Freedman source PDF.

Coordinates are PDF points on the one-based printed pages listed below.  The
script intentionally writes only the shared ``young-26`` image directory.
"""
from pathlib import Path

import pymupdf
from PIL import Image, ImageChops, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-26"

# name: (printed page, (left, top, right, bottom))
FIGURES = {
    "mo-chuong": (844, (208, 0, 648, 245)),
    # Include the (a) panel marker and the resistor labels along the top edge.
    "hinh-26-01": (845, (438, 82, 625, 500)),
    "hinh-26-02": (846, (0, 238, 200, 394)),
    "hinh-26-03": (847, (75, 530, 615, 775)),
    "hinh-26-04": (848, (310, 320, 610, 520)),
    "hinh-26-05": (849, (360, 98, 607, 248)),
    "hinh-26-06": (849, (445, 487, 620, 750)),
    "hinh-26-07": (850, (220, 80, 580, 180)),
    "hinh-26-08": (850, (220, 665, 580, 755)),
    "hinh-26-09": (851, (150, 355, 520, 435)),
    "hinh-26-10": (851, (140, 615, 550, 750)),
    "hinh-26-11": (852, (45, 644, 285, 738)),
    "hinh-26-12": (853, (80, 607, 335, 740)),
    "hinh-26-13": (854, (30, 395, 200, 480)),
    "hinh-26-14": (854, (28, 564, 202, 750)),
    "hinh-26-15": (855, (445, 105, 620, 230)),
    "ung-dung-dien-co": (855, (456, 627, 612, 741)),
    "hinh-26-16": (856, (60, 315, 175, 490)),
    "hinh-26-17": (857, (490, 455, 575, 565)),
    "hinh-26-18": (857, (140, 600, 312, 750)),
    "hinh-26-19": (858, (25, 150, 165, 292)),
    # Keep both circuit panels and the complete blue explanation at the right.
    "hinh-26-20": (859, (92, 54, 430, 195)),
    # Two graphs and their in-figure annotations; stop before the BIO text below.
    "hinh-26-21": (860, (28, 145, 195, 440)),
    "ung-dung-may-tao-nhip-tim": (860, (36, 601, 192, 741)),
    "hinh-26-22": (861, (452, 155, 616, 413)),
    "hinh-26-23": (861, (452, 497, 616, 742)),
    "hinh-26-24": (863, (65, 600, 430, 745)),
    "hinh-26-25": (864, (25, 365, 205, 625)),
    "hinh-26-26": (865, (85, 75, 430, 285)),
    # The summary diagrams extend to the right of the earlier narrow crops.
    "tom-tat-noi-tiep-song-song": (867, (488, 92, 615, 195)),
    "tom-tat-kirchhoff": (867, (488, 212, 615, 304)),
    "tom-tat-dung-cu-do": (867, (490, 321, 615, 413)),
    "tom-tat-mach-rc": (867, (489, 454, 615, 578)),
    "tom-tat-phan-phoi-dien": (867, (490, 643, 576, 733)),
    "hinh-q26-04": (869, (280, 292, 340, 350)),
    "hinh-q26-05": (869, (250, 375, 345, 410)),
    "hinh-q26-06": (869, (155, 575, 255, 615)),
    "hinh-q26-07": (869, (255, 638, 335, 755)),
    "hinh-q26-08": (869, (412, 155, 558, 212)),
    "hinh-q26-09": (869, (410, 250, 558, 315)),
    "hinh-q26-10": (869, (432, 360, 535, 425)),
    "hinh-q26-12": (869, (435, 495, 540, 575)),
    "hinh-q26-14": (869, (430, 645, 548, 725)),
    "hinh-q26-16": (870, (210, 72, 290, 160)),
    "hinh-q26-18": (870, (85, 260, 290, 378)),
}

MASKS = {
    # Figure 26.4's title sits above the two circuit drawings.
    "hinh-26-04": [(310, 320, 610, 332), (310, 510, 610, 520)],
    # The paragraph below Q26.14 begins just after the lower circuit wire.
    "hinh-q26-14": [(430, 712, 548, 725)],
    # The page continuation marker is outside the final panel of Figure 26.3.
    "hinh-26-03": [(585, 742, 615, 755)],
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    for name, (printed_page, box) in FIGURES.items():
        page = doc[printed_page + 19]
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(2, 2),
            clip=pymupdf.Rect(box),
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
                            round((left - box[0]) * 2),
                            round((top - box[1]) * 2),
                            round((right - box[0]) * 2),
                            round((bottom - box[1]) * 2),
                        ),
                        fill="white",
                    )
                image.save(out_path, optimize=True)
        with Image.open(out_path) as image:
            image = image.convert("RGB")
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
    print(f"Prepared {len(FIGURES)} Chapter 26 figure crops in {OUT}")


if __name__ == "__main__":
    main()
