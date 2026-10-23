#!/usr/bin/env python3
"""Asset preparation script for Physics 1 Chapter 6 Theory.
Extracts high-resolution, unmasked original crops from Young & Freedman 15th ed. PDF.
"""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parent.parent
SOURCE_PDF = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
DEST_DIR = ROOT / "docs" / "vat-ly-1" / "bai-giang" / "img" / "young-06"

SCALE = 2.5

# Table of crops: (pdf_page_1_based, (x0, y0, x1, y1))
CROPS = {
    # Opening
    "r-theory-mo-dau": (191, (0.0, 0.0, 439.0, 246.0)),

    # Section 6.1
    "r-theory-06-01": (192, (35.0, 96.0, 193.0, 214.0)),
    "r-theory-06-02": (192, (35.0, 335.0, 195.0, 452.0)),
    "r-theory-06-03": (192, (90.0, 666.0, 572.0, 745.0)),
    "r-theory-app-running": (193, (450.0, 196.0, 648.0, 365.0)),
    "r-theory-06-04": (194, (74.0, 80.0, 570.0, 274.0)),
    "r-theory-06-05": (194, (35.0, 330.0, 195.0, 432.0)),
    "r-theory-06-06": (194, (100.0, 610.0, 570.0, 741.0)),
    "r-theory-06-07": (195, (76.0, 578.0, 344.0, 725.0)),

    # Section 6.2
    "r-theory-06-08": (196, (68.0, 551.0, 568.0, 752.0)),
    "r-theory-06-09": (197, (455.0, 89.0, 611.0, 144.0)),
    "r-theory-06-10": (197, (454.0, 327.0, 614.0, 548.0)),
    "r-theory-06-11": (198, (55.0, 678.0, 276.0, 737.0)),
    "r-theory-06-12": (199, (150.0, 544.0, 563.0, 738.0)),
    "r-theory-06-13": (200, (35.0, 87.0, 195.0, 268.0)),
    "r-theory-06-14": (200, (80.0, 516.0, 250.0, 624.0)),

    # Section 6.3
    "r-theory-06-15": (201, (469.0, 106.0, 595.0, 272.0)),
    "r-theory-06-16": (201, (454.0, 427.0, 616.0, 747.0)),
    "r-theory-06-17": (202, (44.0, 213.0, 195.0, 365.0)),
    "r-theory-06-18": (202, (44.0, 437.0, 185.0, 503.0)),
    "r-theory-06-19": (202, (35.0, 566.0, 195.0, 719.0)),
    "r-theory-06-20": (203, (455.0, 96.0, 614.0, 321.0)),
    "r-theory-06-21": (203, (89.0, 528.0, 315.0, 650.0)),
    "r-theory-app-tendons": (204, (35.0, 245.0, 194.0, 528.0)),
    "r-theory-06-22": (204, (315.0, 599.0, 565.0, 716.0)),
    "r-theory-06-23": (205, (454.0, 503.0, 614.0, 745.0)),
    "r-theory-06-24": (206, (45.0, 582.0, 285.0, 741.0)),

    # Section 6.4
    "r-theory-app-muscle": (207, (450.0, 634.0, 615.0, 742.0)),
    "r-theory-06-25": (208, (44.0, 96.0, 193.0, 331.0)),
    "r-theory-06-26": (208, (35.0, 369.0, 195.0, 492.0)),
    "r-theory-06-27": (208, (317.0, 576.0, 565.0, 668.0)),
    "r-theory-06-28": (209, (82.0, 333.0, 329.0, 493.0)),

    # Summary (PDF 210)
    "r-theory-summary-01": (210, (446.0, 88.0, 563.0, 135.0)),
    "r-theory-summary-02": (210, (447.0, 193.0, 598.0, 294.0)),
    "r-theory-summary-03": (210, (447.0, 318.0, 615.0, 400.0)),
    "r-theory-summary-04": (210, (447.0, 428.0, 573.0, 508.0)),
    "r-theory-summary-05": (210, (445.0, 552.0, 603.0, 636.0)),
}

def generate_crops():
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    assert SOURCE_PDF.is_file(), f"Source PDF not found at {SOURCE_PDF}"
    with fitz.open(SOURCE_PDF) as doc:
        for stem, (pno, rect) in CROPS.items():
            page = doc[pno - 1]
            clip = fitz.Rect(rect)
            pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=clip, alpha=False)
            out_path = DEST_DIR / f"{stem}.png"
            pix.save(str(out_path))
            print(f"Saved {out_path.name}: {pix.width}x{pix.height} px")

if __name__ == "__main__":
    generate_crops()
