"""Crop chapter 34 sections 34.2-34.4 figures (Figures 34.10-34.39) without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-34"

CROPS = {
    "hinh-34-10": (1134, (36, 135, 194, 445)),
    "hinh-34-11": (1134, (36, 538, 192, 715)),
    "hinh-34-12": (1135, (455, 165, 623, 670)),
    "hinh-34-13": (1136, (36, 85, 192, 455)),
    "hinh-34-14": (1136, (260, 588, 520, 730)),
    "hinh-34-15": (1137, (355, 554, 605, 650)),
    "hinh-34-16": (1138, (125, 598, 575, 736)),
    "hinh-34-17": (1139, (90, 75, 430, 250)),
    "hinh-34-18": (1139, (155, 582, 560, 740)),
    "hinh-34-19": (1140, (85, 545, 568, 738)),
    "hinh-34-20": (1142, (115, 203, 565, 520)),
    "hinh-34-21": (1143, (115, 97, 400, 222)),
    "hinh-34-22": (1144, (250, 60, 532, 185)),
    "hinh-34-23": (1144, (0, 590, 194, 744)),
    "hinh-34-24": (1145, (350, 218, 638, 300)),
    "hinh-34-25": (1145, (270, 640, 640, 730)),
    "hinh-34-26": (1146, (72, 295, 260, 485)),
    "hinh-34-27": (1146, (310, 235, 570, 400)),
    "hinh-34-28": (1147, (455, 228, 615, 535)),
    "hinh-34-29": (1147, (125, 600, 365, 710)),
    "hinh-34-30": (1148, (208, 580, 572, 750)),
    "hinh-34-31": (1149, (456, 106, 612, 370)),
    "hinh-34-32": (1149, (455, 431, 605, 652)),
    "hinh-34-33": (1150, (208, 94, 552, 208)),
    "hinh-34-34": (1150, (0, 278, 194, 420)),
    "hinh-34-35": (1150, (226, 600, 546, 746)),
    "hinh-34-36": (1151, (77, 597, 572, 744)),
    "hinh-34-37": (1152, (124, 468, 572, 737)),
    "hinh-34-38": (1154, (310, 88, 572, 205)),
    "hinh-34-39": (1154, (55, 564, 280, 731)),
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
    print(f"Successfully prepared {len(CROPS)} images for chapter 34 theory A.")

if __name__ == "__main__":
    main()
