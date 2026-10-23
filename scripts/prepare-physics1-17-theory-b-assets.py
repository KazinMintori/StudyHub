"""Extract Chapter 17 Theory B figures (Sections 17.5, 17.6, 17.7 and Summary 17)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-17"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "b-hinh-17-15": (572, (33.0, 103.0, 192.0, 448.0)),
    "b-hinh-17-16": (572, (34.0, 558.0, 194.0, 683.0)),
    "b-hinh-17-17": (573, (465.0, 213.0, 602.0, 330.0)),
    "b-hinh-17-18": (574, (32.0, 373.0, 194.0, 521.0)),
    "b-hinh-17-19": (576, (33.0, 154.0, 194.0, 292.0)),
    "b-hinh-17-20": (577, (76.0, 95.0, 485.0, 280.0)),
    "b-hinh-17-21": (577, (453.0, 428.0, 617.0, 579.0)),
    "b-hinh-17-22": (578, (33.0, 156.0, 194.0, 353.0)),
    "b-hinh-17-23": (578, (33.0, 522.0, 194.0, 631.0)),
    "b-hinh-17-24": (581, (455.0, 85.0, 610.0, 340.0)),
    "b-ung-dung-17-01": (582, (27.0, 193.0, 195.0, 369.0)),
    "b-hinh-17-25": (583, (85.0, 220.0, 332.0, 353.0)),
    "b-hinh-17-26": (583, (75.0, 638.0, 341.0, 731.0)),
    "b-hinh-17-27": (584, (74.0, 197.0, 268.0, 327.0)),
    "b-hinh-17-28": (584, (33.0, 455.0, 194.0, 662.0)),
    "b-hinh-17-29": (585, (453.0, 225.0, 614.0, 348.0)),
    "b-hinh-17-30": (587, (75.0, 542.0, 588.0, 748.0)),
    "b-tom-tat-01": (588, (447.0, 87.0, 577.0, 207.0)),
    "b-tom-tat-02": (588, (447.0, 242.0, 577.0, 307.0)),
    "b-tom-tat-03": (588, (447.0, 377.0, 577.0, 487.0)),
    "b-tom-tat-04": (588, (447.0, 562.0, 577.0, 652.0)),
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
    print(f"Successfully prepared {len(CROPS)} images for Chapter 17 Theory B in {OUT}.")

if __name__ == "__main__":
    main()
