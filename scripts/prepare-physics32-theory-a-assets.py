"""Crop chapter 32 opening and sections 32.1-32.3 figures without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-32"

CROPS = {
    "mo-dau-32": (1068, (209, 0, 648, 246)),
    "hinh-32-01": (1069, (456, 530, 612, 742)),
    "hinh-32-02": (1070, (36, 185, 196, 455)),
    "hinh-32-03": (1070, (70, 605, 570, 725)),
    "hinh-32-04": (1071, (75, 566, 475, 722)),
    "hinh-32-05": (1072, (36, 568, 190, 718)),
    "hinh-32-06": (1073, (456, 83, 613, 253)),
    "hinh-32-07": (1073, (456, 367, 613, 685)),
    "hinh-32-08": (1074, (36, 217, 195, 539)),
    "hinh-32-09": (1075, (456, 93, 613, 283)),
    "hinh-32-10": (1076, (36, 93, 191, 351)),
    "hinh-32-11": (1076, (36, 478, 191, 749)),
    "hinh-32-12": (1077, (456, 528, 613, 748)),
    "hinh-32-13": (1078, (36, 253, 195, 430)),
    "hinh-32-14": (1079, (456, 123, 612, 260)),
    "hinh-32-15": (1079, (395, 555, 575, 715)),
    "hinh-32-16": (1080, (0, 606, 192, 742)),
    "ung-dung-32-thi-giac-tu-ngoai": (1072, (36, 225, 193, 345)),
    "ung-dung-32-song-phang-tu-vu-tru": (1078, (0, 600, 193, 742)),
}

SCALE = 2.5

def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found at {LOCAL_SOURCE} or {MAIN_SOURCE}")
    OUT.mkdir(parents=True, exist_ok=True)
    with fitz.open(SOURCE) as pdf:
        for stem, (page_num, box) in CROPS.items():
            page = pdf[page_num - 1]
            rect = fitz.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=rect, alpha=False)
            target = OUT / f"{stem}.png"
            pix.save(target)
            print(f"Saved {stem}: p.{page_num}, box={box}, size={pix.width}x{pix.height}")
    print(f"Successfully prepared {len(CROPS)} images for chapter 32 theory A.")

if __name__ == "__main__":
    main()
