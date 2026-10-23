"""Crop source figures for Chapter 19 sections 19.5-19.8 and chapter summary.

Exposes CROPS and SCALE as required.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-19"

SCALE = 2.5

# Mapping basename -> (PDF1based, (x0, y0, x1, y1))
CROPS = {
    "b-hinh-19-14.png": (644, (33, 193, 194, 339)),
    "b-hinh-19-15.png": (644, (33, 465, 194, 612)),
    "b-hinh-19-16.png": (645, (452, 134, 614, 292)),
    "b-hinh-19-17.png": (645, (455, 355, 614, 445)),
    "b-hinh-19-18.png": (646, (34, 95, 195, 355)),
    "b-hinh-19-19.png": (646, (40, 459, 195, 618)),
    "b-hinh-19-20.png": (649, (452, 218, 614, 380)),
    "b-ung-dung-01.png": (650, (35, 215, 193, 415)),
    "b-hinh-19-21.png": (651, (395, 108, 580, 245)),
    "b-tom-tat-19-01.png": (652, (452, 88, 552, 201)),
    "b-tom-tat-19-02.png": (652, (452, 244, 567, 329)),
    "b-tom-tat-19-03.png": (652, (452, 382, 550, 467)),
    "b-tom-tat-19-04.png": (652, (454, 478, 608, 565)),
    "b-tom-tat-19-05.png": (652, (454, 575, 608, 665)),
}

# Also support stem lookups
for _stem, _val in list(CROPS.items()):
    if _stem.endswith(".png"):
        CROPS[_stem[:-4]] = _val


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    saved_count = 0
    for name, (p1based, rect_coords) in list(CROPS.items()):
        if not name.endswith(".png"):
            continue
        page = doc[p1based - 1]
        rect = pymupdf.Rect(rect_coords)
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(SCALE, SCALE),
            clip=rect,
            alpha=False,
        )
        out_path = OUT / name
        pix.save(str(out_path))
        saved_count += 1
    print(f"Successfully generated {saved_count} figure crops in {OUT}")


if __name__ == "__main__":
    main()
