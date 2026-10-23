"""Trích xuất hình ảnh chuẩn xác từ PDF nguồn cho nhóm bài tập Chapter 11 nhóm C."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]

# CROPS định nghĩa ánh xạ: basename -> (PDF 1-based page, (x0, y0, x1, y1))
CROPS = {
    'c-fig-11-11': (365, (448, 95, 615, 223)),
    'c-fig-11-21': (374, (380, 615, 500, 702)),
    'c-fig-q11-19': (376, (95, 175, 230, 305)),
}

SCALE = 3
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-11'


def crop_images():
    """Trích xuất ảnh gốc từ PDF với độ phân giải cao và lưu đúng vị trí."""
    pdf_path = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
    doc = fitz.open(pdf_path)
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (page_1based, rect_coords) in CROPS.items():
        page = doc[page_1based - 1]
        rect = fitz.Rect(rect_coords)
        pix = page.get_pixmap(clip=rect, dpi=72 * SCALE, alpha=False)
        target = OUT / f"{name}.png"
        pix.save(target)
        print(f"Đã xuất ảnh: {target.relative_to(ROOT)} ({pix.width}x{pix.height})")


if __name__ == '__main__':
    crop_images()
