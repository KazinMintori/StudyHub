#!/usr/bin/env python3
"""Asset generation script for Physics 1 Chapter 11 Theory A (Sections 11.1 - 11.3).
Extracts high-resolution, unmasked original crops from Young & Freedman 15th ed. PDF.
"""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parent.parent
SOURCE_PDF = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
DEST_DIR = ROOT / "docs" / "vat-ly-1" / "bai-giang" / "img" / "young-11"

SCALE = 3.0

CROPS = {
    "a-mo-dau": (357, (0.0, 0.0, 438.5, 245.5)),
    "a-hinh-11-01": (358, (35.0, 105.0, 195.0, 508.0)),
    "a-hinh-11-02": (359, (455.0, 323.0, 612.0, 547.0)),
    "a-hinh-11-03": (360, (35.0, 128.0, 193.0, 238.5)),
    "a-hinh-11-04": (360, (35.0, 328.0, 184.0, 533.0)),
    "a-hinh-11-05": (360, (235.0, 610.0, 541.0, 742.0)),
    "a-hinh-11-06": (361, (134.0, 308.0, 281.0, 405.0)),
    "a-hinh-11-07": (361, (455.0, 451.0, 620.0, 489.0)),
    "a-hinh-11-08": (362, (46.0, 505.0, 283.0, 724.0)),
    "a-hinh-11-09": (363, (97.0, 579.0, 591.0, 723.0)),
    "a-hinh-11-10": (364, (35.0, 510.0, 485.0, 712.0)),
    "a-hinh-11-11": (365, (452.0, 97.0, 611.0, 221.0)),
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
