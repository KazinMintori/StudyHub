"""Extract Chapter 35 Theory B figures (Sections 35.4-35.5, Figures 35.11-35.19)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-35"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "hinh-35-11": (1190, (35, 114, 195, 428)),
    "hinh-35-12": (1190, (35, 545, 195, 685)),
    "hinh-35-13": (1191, (75, 84, 565, 292)),
    "hinh-35-14": (1191, (455, 490, 612, 750)),
    "hinh-35-15": (1192, (330, 392, 550, 495)),
    "hinh-35-16": (1193, (78, 585, 570, 750)),
    "hinh-35-17": (1194, (35, 95, 195, 290)),
    "hinh-35-18": (1194, (35, 368, 195, 525)),
    "hinh-35-19": (1195, (78, 558, 570, 750)),
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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 35 Theory B in {OUT}.")

if __name__ == "__main__":
    main()
