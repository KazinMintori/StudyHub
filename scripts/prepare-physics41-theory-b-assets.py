#!/usr/bin/env python3
"""
Crop and extract image assets for Young & Freedman 15th ed. Chapter 41 Theory B.
Covers Figures 41.13 through 41.27 and Applications B-1 through B-3.
"""

from pathlib import Path
import fitz  # PyMuPDF

PDF_PATH = Path("raw_materials/physics/source/young-freedman-15.pdf")
OUTPUT_DIR = Path("docs/vat-ly-2/bai-giang/img/young-41")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Format: (name, 0-indexed page in PDF, (left, top, right, bottom) in points)
FIGURES = [
    ("hinh-41-13.png", 1396, (115, 104, 405, 314)),
    ("hinh-41-14.png", 1397, (34, 116, 180, 228)),
    ("hinh-41-15.png", 1397, (234, 95, 534, 255)),
    ("hinh-41-16.png", 1398, (75, 95, 505, 270)),
    ("hinh-41-17.png", 1398, (90, 555, 425, 745)),
    ("ung-dung-b-1.png", 1400, (454, 315, 614, 472)),
    ("hinh-41-18.png", 1401, (320, 104, 560, 226)),
    ("hinh-41-19.png", 1404, (75, 58, 442, 238)),
    ("hinh-41-20.png", 1406, (456, 225, 648, 408)),
    ("hinh-41-21.png", 1407, (34, 275, 188, 468)),
    ("hinh-41-22.png", 1407, (0, 590, 192, 738)),
    ("ung-dung-b-2.png", 1408, (455, 558, 648, 738)),
    ("hinh-41-23.png", 1411, (34, 268, 190, 415)),
    ("hinh-41-24.png", 1411, (260, 550, 520, 735)),
    ("ung-dung-b-3.png", 1412, (455, 188, 648, 335)),
    ("hinh-41-25.png", 1413, (228, 60, 550, 158)),
    ("hinh-41-26.png", 1414, (458, 165, 600, 258)),
    ("hinh-41-27.png", 1416, (105, 485, 415, 745)),
]

def main():
    print(f"Opening PDF: {PDF_PATH}")
    doc = fitz.open(str(PDF_PATH))
    scale = 3.0  # 300% DPI for crisp, high-fidelity web display
    mat = fitz.Matrix(scale, scale)

    for name, page_idx, (x0, y0, x1, y1) in FIGURES:
        page = doc[page_idx]
        clip_rect = fitz.Rect(x0, y0, x1, y1)
        pix = page.get_pixmap(matrix=mat, clip=clip_rect)

        out_path = OUTPUT_DIR / name
        pix.save(str(out_path))
        print(f"Saved {name} ({pix.width}x{pix.height} px) -> {out_path}")

if __name__ == "__main__":
    main()
