#!/usr/bin/env python3
"""
Crop and extract image assets for Young & Freedman 15th ed. Chapter 43 Theory B.
Covers Figures 43.9 through 43.18 and Applications B-1 and B-2.
Source PDF: raw_materials/physics/source/young-freedman-15.pdf
"""

from pathlib import Path
import fitz  # PyMuPDF

PDF_PATH = Path("raw_materials/physics/source/young-freedman-15.pdf")
OUTPUT_DIR = Path("docs/vat-ly-2/bai-giang/img/young-43")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Format: (filename, 0-indexed page in PDF, (x0, y0, x1, y1) in points)
FIGURES = [
    ("hinh-43-09.png", 1483, (34, 528, 185, 744)),
    ("hinh-43-10.png", 1484, (455, 515, 613, 677)),
    ("ung-dung-b-1.png", 1484, (455, 208, 648, 364)),
    ("hinh-43-11.png", 1487, (35, 280, 205, 478)),
    ("hinh-43-12.png", 1488, (75, 75, 570, 195)),
    ("hinh-43-13.png", 1488, (465, 654, 600, 744)),
    ("ung-dung-b-2.png", 1489, (36, 584, 192, 742)),
    ("hinh-43-14.png", 1489, (208, 75, 570, 466)),
    ("hinh-43-15.png", 1490, (138, 60, 380, 240)),
    ("hinh-43-16.png", 1492, (78, 75, 470, 215)),
    ("hinh-43-17.png", 1492, (455, 320, 613, 495)),
    ("hinh-43-18.png", 1493, (0, 352, 192, 569)),
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
