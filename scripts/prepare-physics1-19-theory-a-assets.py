"""Prepare chapter 19 theory A image assets (sections 19.1 - 19.4).

Crops preserve original PDF pixels, labels, panels and clean artwork boundaries.
Exposes CROPS and SCALE for verification.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-19"

SCALE = 2.5

# Dict format: basename -> (PDF1based_page, (x0, y0, x1, y1))
CROPS = {
    "a-mo-chuong": (633, (0.0, 0.0, 438.2, 245.3)),
    "a-hinh-19-01": (634, (35.0, 115.0, 193.0, 260.0)),
    "a-hinh-19-02": (634, (215.0, 548.0, 395.0, 726.0)),
    "a-hinh-19-03": (634, (409.0, 540.0, 575.0, 741.0)),
    "a-hinh-19-04": (635, (450.0, 143.0, 615.0, 362.0)),
    "a-hinh-19-05": (635, (455.0, 435.0, 610.0, 523.0)),
    "a-hinh-19-06": (636, (190.0, 75.0, 572.0, 238.0)),
    "a-hinh-19-07": (637, (450.0, 256.0, 620.0, 749.0)),
    "a-hinh-19-08": (638, (35.0, 133.0, 195.0, 470.0)),
    "a-hinh-19-09": (639, (452.0, 116.0, 615.0, 417.0)),
    "a-ung-dung-tap-the-duc": (639, (455.0, 582.0, 648.5, 748.0)),
    "a-hinh-19-10": (640, (0.0, 145.0, 193.0, 295.0)),
    "a-hinh-19-11": (640, (215.0, 535.0, 555.0, 745.0)),
    "a-hinh-19-12": (641, (388.0, 618.0, 575.0, 744.0)),
    "a-hinh-19-13": (642, (82.0, 592.0, 245.0, 735.0)),
}


def main() -> None:
    if not PDF.is_file():
        raise FileNotFoundError(f"Source PDF not found at {PDF}")
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    for stem, (pno, box) in CROPS.items():
        page = doc[pno - 1]
        rect = pymupdf.Rect(box) & page.rect
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(SCALE, SCALE),
            clip=rect,
            alpha=False,
        )
        dest = OUT / f"{stem}.png"
        pix.save(str(dest))
        print(f"Saved {dest.name}: page {pno}, box={box}, size={pix.width}x{pix.height}")
    print(f"Successfully generated {len(CROPS)} assets.")


if __name__ == "__main__":
    main()
