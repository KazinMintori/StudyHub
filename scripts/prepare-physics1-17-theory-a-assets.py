"""Crop Chapter 17 Theory A figures from Young & Freedman (15th ed.) pages 561-571.

Generates high-resolution PNG image assets for Sections 17.1-17.4 and Chapter opening.
Preserves original labels, panels, coordinate axes, and diagrams without cutting.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-17"

SCALE = 2.5

# Dict format: basename -> (PDF1based_page, (x0, y0, x1, y1))
CROPS = {
    "a-mo-dau-17.png": (561, (0, 0, 439, 246)),
    "a-hinh-17-01.png": (562, (34, 85, 195, 405)),
    "a-hinh-17-02.png": (562, (250, 600, 535, 745)),
    "a-hinh-17-03.png": (563, (454, 425, 614, 746)),
    "a-hinh-17-04.png": (564, (0, 128, 194, 278)),
    "a-hinh-17-05.png": (565, (75, 58, 442, 280)),
    "a-ung-dung-17-01.png": (565, (454, 368, 614, 595)),
    "a-hinh-17-06.png": (565, (454, 642, 618, 746)),
    "a-hinh-17-07.png": (566, (34, 552, 196, 665)),
    "a-hinh-17-08.png": (567, (454, 218, 614, 395)),
    "a-hinh-17-09.png": (567, (75, 560, 442, 750)),
    "a-hinh-17-10.png": (568, (34, 106, 195, 282)),
    "a-hinh-17-11.png": (568, (0, 380, 194, 542)),
    "a-hinh-17-12.png": (570, (34, 350, 195, 530)),
    "a-hinh-17-13.png": (570, (34, 634, 194, 743)),
    "a-hinh-17-14.png": (571, (76, 565, 265, 642)),
}


def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found at {LOCAL_SOURCE} or {MAIN_SOURCE}")
    OUT.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(SOURCE) as pdf:
        for basename, (page_num, box) in CROPS.items():
            page = pdf[page_num - 1]
            rect = pymupdf.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=rect, alpha=False)
            target = OUT / (basename if basename.endswith(".png") else f"{basename}.png")
            pix.save(str(target))
            print(f"Saved {target.name}: page {page_num}, box={box}, size={pix.width}x{pix.height}")
    print(f"Successfully generated {len(CROPS)} images in {OUT}")


if __name__ == "__main__":
    main()
