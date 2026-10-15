"""Crop chapter 37 sections 37.1-37.4 figures (Figures 37.1-37.14) without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-37"

CROPS = {
    "hinh-37-01": (1238, (34, 105, 195, 255)),
    "hinh-37-02": (1238, (90, 580, 575, 750)),
    "hinh-37-03": (1239, (455, 435, 615, 578)),
    "hinh-37-04": (1240, (35, 530, 195, 743)),
    "hinh-37-05": (1241, (75, 60, 440, 495)),
    "hinh-37-06": (1242, (140, 575, 572, 742)),
    "hinh-37-07": (1244, (35, 155, 195, 292)),
    "hinh-37-08": (1244, (35, 360, 195, 490)),
    "hinh-37-09": (1244, (35, 554, 195, 740)),
    "hinh-37-10": (1247, (75, 520, 445, 755)),
    "hinh-37-11": (1248, (35, 360, 195, 605)),
    "hinh-37-12": (1249, (75, 60, 440, 195)),
    "hinh-37-13": (1250, (320, 103, 565, 256)),
    "hinh-37-14": (1251, (465, 125, 605, 560)),
}

SCALE = 2.5

def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found at {LOCAL_SOURCE} or {MAIN_SOURCE}")
    OUT.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(SOURCE) as pdf:
        for stem, (page_num, box) in CROPS.items():
            page = pdf[page_num - 1]
            rect = pymupdf.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=rect, alpha=False)
            target = OUT / f"{stem}.png"
            pix.save(target)
            print(f"Saved {stem}: p.{page_num}, box={box}, size={pix.width}x{pix.height}")
    print(f"Successfully prepared {len(CROPS)} images for chapter 37 theory A.")

if __name__ == "__main__":
    main()
