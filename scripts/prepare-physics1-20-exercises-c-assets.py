"""Trích xuất hình ảnh gốc từ PDF cho nhóm bài tập Chapter 20 nhóm C.

Bao gồm:
- c-hinh-20-23: Hình 20.23 trong Bài tập cầu nối (trang PDF 691).
- c-hinh-20-06: Hình 20.6 Chu trình Otto cho câu Q20.10 (trang PDF 668).
- c-hinh-20-09: Hình 20.9 Chu trình làm lạnh cơ học cho câu Q20.11 (trang PDF 670).
- c-hinh-20-13: Hình 20.13 Chu trình Carnot cho VP20.4.2 và câu Q20.10 (trang PDF 674).
"""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'c-hinh-20-23': (691, (350, 238, 608, 380)),
    'c-hinh-20-06': (668, (33, 94, 195, 290)),
    'c-hinh-20-09': (670, (78, 84, 612, 335)),
    'c-hinh-20-13': (674, (170, 84, 615, 350)),
}
SCALE = 3
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-20'


def crop_images():
    """Trích xuất ảnh gốc từ PDF với độ phân giải cao và lưu đúng vị trí."""
    doc = fitz.open(ROOT / 'raw_materials/physics/source/young-freedman-15.pdf')
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
