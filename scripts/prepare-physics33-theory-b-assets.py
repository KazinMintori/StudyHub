"""Extract chapter 33 theory B figures (sections 33.5-33.7, applications, summary)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-33"

# PDF 1-based page numbers and point bounding boxes (x0, y0, x1, y1)
CROPS = {
    "hinh-33-20": (1110, (95, 645, 575, 743)),
    "hinh-33-21": (1111, (95, 60, 425, 223)),
    "hinh-33-22": (1111, (450, 510, 615, 745)),
    "hinh-33-23": (1112, (220, 60, 560, 222)),
    "hinh-33-24": (1112, (220, 565, 560, 750)),
    "hinh-33-25": (1113, (280, 63.5, 437, 168)),
    "hinh-33-26": (1114, (140, 85, 575, 250)),
    "hinh-33-27": (1114, (35, 530, 195, 750)),
    "hinh-33-28": (1115, (125, 233, 288, 439)),
    "hinh-33-29": (1116, (120, 545, 575, 765)),
    "ung-dung-33-phan-cuc-phim-3d": (1116, (0, 246, 193, 389)),
    "ung-dung-33-man-hinh-tinh-the-long": (1117, (453, 244, 615, 540)),
    "hinh-33-30": (1117, (175, 115, 340, 310)),
    "hinh-33-31": (1118, (130, 85, 575, 255)),
    "ung-dung-33-thi-giac-ong": (1118, (0, 419, 193, 576)),
    "hinh-33-32": (1118, (35, 637, 193, 742)),
    "hinh-33-33": (1119, (455, 115, 615, 290)),
    "hinh-33-34": (1119, (452, 404, 615, 665)),
    "hinh-33-35": (1120, (35, 115, 192, 580)),
    "hinh-33-36": (1121, (75, 75, 612, 215)),
    "tom-tat-33-01": (1121, (478, 433, 597, 537)),
    "tom-tat-33-02": (1121, (478, 598, 607, 677)),
    "tom-tat-33-03": (1121, (478, 693, 610, 747)),
    "tom-tat-33-04": (1122, (436, 60, 567, 144)),
    "tom-tat-33-05": (1122, (436, 166, 537, 240)),
    "tom-tat-33-06": (1122, (436, 242, 527, 298)),
}

SCALE = 3.0

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
    print(f"Successfully prepared 26 images for chapter 33 theory B in {OUT}.")

if __name__ == "__main__":
    main()
