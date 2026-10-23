"""Extract Chapter 09 Theory B figures (Sections 9.4-9.6 and Summary)."""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-09"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "b-ung-dung-01": (303, (456, 375, 613, 481)),
    "b-ung-dung-02": (303, (456, 485, 613, 592)),
    "b-hinh-9-14": (303, (120, 624, 415, 752)),
    "b-hinh-9-15": (304, (42, 235, 285, 368)),
    "b-bang-9-02": (305, (78, 60, 612, 376)),
    "b-hinh-9-16": (305, (350, 642, 580, 730)),
    "b-hinh-9-17": (306, (330, 350, 555, 528)),
    "b-hinh-9-18": (307, (455, 175, 613, 290)),
    "b-hinh-9-19": (307, (456, 514, 616, 676)),
    "b-hinh-9-20": (308, (36, 115, 198, 330)),
    "b-hinh-9-21": (308, (362, 442, 520, 534)),
    "b-hinh-9-22": (309, (455, 278, 613, 420)),
    "b-hinh-9-23": (309, (120, 580, 295, 746)),
    "b-hinh-9-24": (310, (60, 485, 268, 646)),
    "b-tom-tat-9-01": (311, (495, 95, 575, 188)),
    "b-tom-tat-9-02": (311, (495, 260, 610, 345)),
    "b-tom-tat-9-03": (311, (495, 370, 595, 455)),
    "b-tom-tat-9-04": (311, (495, 505, 615, 570)),
}

SCALE = 3.0

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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 09 Theory B in {OUT}.")

if __name__ == "__main__":
    main()
