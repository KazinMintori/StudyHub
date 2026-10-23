"""Crop source figures for Chapter 10 sections 10.5–10.7 and the full summary.

All rectangles are in PDF points on the 1-based PDF pages (PDF pages 336–345).
Output images preserve all source artwork, embedded labels, and panels.
"""

from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-10"
SCALE = 2.5

# basename -> (PDF1based, (x0, y0, x1, y1))
CROPS = {
    "b-hinh-10-23": (336, (30, 503, 205, 680)),
    "b-hinh-10-24": (337, (454, 102, 648, 290)),
    "b-hinh-10-25": (337, (454, 361, 615, 535)),
    "b-hinh-10-26": (337, (454, 595, 615, 750)),
    "b-hinh-10-27": (338, (30, 115, 205, 280)),
    "b-hinh-10-28": (339, (455, 204, 615, 740)),
    "b-hinh-10-29": (340, (30, 250, 296, 445)),
    "b-hinh-10-30": (340, (310, 502, 575, 748)),
    "b-hinh-10-31": (341, (75, 398, 342, 582)),
    "b-hinh-10-32": (342, (30, 104, 205, 295)),
    "b-hinh-10-33": (342, (30, 387, 205, 695)),
    "b-hinh-10-34": (342, (210, 585, 575, 740)),
    "b-hinh-10-35": (343, (230, 630, 365, 745)),
    "b-hinh-10-36": (344, (30, 226, 296, 440)),
    "b-tom-tat-10-01": (345, (475, 85, 605, 171)),
    "b-tom-tat-10-02": (345, (475, 173, 605, 250)),
    "b-tom-tat-10-03": (345, (475, 252, 605, 397)),
    "b-tom-tat-10-04": (345, (475, 400, 605, 511)),
    "b-tom-tat-10-05": (345, (475, 514, 605, 637)),
    "b-tom-tat-10-06": (345, (475, 643, 605, 735)),
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    for name, (p1, box) in CROPS.items():
        page = doc[p1 - 1]
        rect = pymupdf.Rect(box)
        if not page.rect.contains(rect):
            raise ValueError(f"Crop outside PDF page {p1}: {name} {rect}")
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(SCALE, SCALE),
            clip=rect,
            alpha=False,
        )
        output = OUT / f"{name}.png"
        pix.save(output)
        print(f"Generated {output.name}")


if __name__ == "__main__":
    main()
