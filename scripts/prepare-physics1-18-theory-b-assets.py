"""Prepare and crop source figures for Physics 1, Chapter 18, Theory B.

Covers Sections 18.4, 18.5, 18.6 and Chapter 18 Summary continuation.
All rectangles are in PDF points (1-based page numbers).
Outputs flat PNG files to docs/vat-ly-1/bai-giang/img/young-18/b-*.png.
"""

from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT_DIR = ROOT / "docs/vat-ly-1/bai-giang/img/young-18"

SCALE = 2.5

# Dict mapping basename -> (PDF 1-based page, (x0, y0, x1, y1))
CROPS = {
    "b-hinh-18-17": (614, (45.0, 460.0, 180.0, 742.0)),
    "b-hinh-18-18": (615, (455.0, 275.0, 615.0, 748.0)),
    "b-hinh-18-19": (616, (255.0, 58.0, 525.0, 242.0)),
    "b-hinh-18-20": (616, (48.0, 505.0, 180.0, 635.0)),
    "b-hinh-18-21": (617, (455.0, 124.0, 615.0, 305.0)),
    "b-hinh-18-22": (617, (75.0, 595.0, 435.0, 742.0)),
    "b-hinh-18-23": (618, (36.0, 192.0, 195.0, 452.0)),
    "b-ung-dung-18-01": (619, (456.0, 452.0, 618.0, 595.0)),
    "b-hinh-18-24": (620, (210.0, 83.0, 575.0, 258.0)),
    "b-hinh-18-25": (620, (36.0, 352.0, 192.0, 472.0)),
    "b-hinh-18-26": (621, (90.0, 480.0, 430.0, 740.0)),
    "b-hinh-18-27": (622, (210.0, 58.0, 570.0, 295.0)),
    "b-tom-tat-18-01": (622, (450.0, 570.0, 550.0, 645.0)),
    "b-tom-tat-18-02": (622, (450.0, 665.0, 530.0, 735.0)),
    "b-tom-tat-18-03": (623, (495.0, 46.5, 615.0, 180.0)),
    "b-tom-tat-18-04": (623, (495.0, 190.0, 618.0, 278.0)),
    "b-tom-tat-18-05": (623, (495.0, 280.0, 615.0, 355.0)),
    "b-tom-tat-18-06": (623, (495.0, 358.0, 615.0, 455.0)),
}


def generate_crops(pdf_path=PDF_PATH, out_dir=OUT_DIR, scale=SCALE, crops=CROPS):
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    mat = fitz.Matrix(scale, scale)

    created = []
    for name, (p_num, bbox) in crops.items():
        page = doc[p_num - 1]
        rect = fitz.Rect(bbox)
        pix = page.get_pixmap(clip=rect, matrix=mat, alpha=False)
        out_path = out_dir / f"{name}.png"
        pix.save(str(out_path))
        created.append((name, out_path, pix.width, pix.height))
        print(f"Saved {name}.png ({pix.width}x{pix.height}) from page {p_num}")

    doc.close()
    return created


if __name__ == "__main__":
    generate_crops()
