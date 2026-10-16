#!/usr/bin/env python3
"""
Crop and extract image assets for Young & Freedman 15th ed. Chapter 44 Theory B.
Covers Figures 44.10 through 44.24 and Application B-1.
"""

from pathlib import Path
import pymupdf

PDF_PATH = Path("raw_materials/physics/source/young-freedman-15.pdf")
OUTPUT_DIR = Path("docs/vat-ly-2/bai-giang/img/young-44")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Format: (name, 0-indexed page in PDF, (left, top, right, bottom) in points)
FIGURES = [
    ("hinh-44-10.png", 1518, (450, 315, 615, 510)),
    ("hinh-44-11.png", 1519, (215, 485, 565, 608)),
    ("hinh-44-12.png", 1519, (215, 620, 565, 745)),
    ("hinh-44-13.png", 1520, (455, 465, 615, 735)),
    ("hinh-44-14.png", 1522, (455, 295, 615, 585)),
    ("hinh-44-15.png", 1523, (35, 168, 193, 399)),
    ("hinh-44-16.png", 1524, (455, 216, 615, 502)),
    ("hinh-44-17.png", 1525, (35, 115, 195, 240)),
    ("hinh-44-18.png", 1526, (450, 345, 615, 730)),
    ("hinh-44-19.png", 1528, (460, 145, 610, 280)),
    ("hinh-44-20.png", 1529, (35, 360, 195, 505)),
    ("hinh-44-21.png", 1529, (35, 600, 195, 750)),
    ("ung-dung-b-1.png", 1530, (455, 220, 648, 376)),
    ("hinh-44-22.png", 1532, (75, 510, 440, 735)),
    ("hinh-44-23.png", 1536, (455, 168, 615, 405)),
    ("hinh-44-24.png", 1536, (150, 632, 366, 743)),
]

def main():
    print(f"Opening PDF: {PDF_PATH}")
    doc = pymupdf.open(str(PDF_PATH))
    scale = 3.0  # 300% DPI for crisp, high-fidelity web display
    mat = pymupdf.Matrix(scale, scale)

    for name, page_idx, (x0, y0, x1, y1) in FIGURES:
        page = doc[page_idx]
        clip_rect = pymupdf.Rect(x0, y0, x1, y1)
        pix = page.get_pixmap(matrix=mat, clip=clip_rect)

        out_path = OUTPUT_DIR / name
        pix.save(str(out_path))
        print(f"Saved {name} ({pix.width}x{pix.height} px) -> {out_path}")

if __name__ == "__main__":
    main()
