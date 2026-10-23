#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trích xuất hình ảnh gốc cho bài tập Chương 20 Nhóm D (Young & Freedman 15th ed).
Trích xuất chính xác các panel và nhãn từ PDF gốc, không làm mờ/cắt chữ/sửa pixel gốc.
"""
from pathlib import Path
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "raw_materials" / "physics" / "source" / "young-freedman-15.pdf"
OUT = ROOT / "docs" / "vat-ly-1" / "bai-giang" / "img" / "young-20"

# CROPS: basename -> (PDF1based, (x0, y0, x1, y1))
CROPS = {
    "d-hinh-e20-05": (692, (310, 565, 502, 675)),
}
SCALE = 3


def crop_assets():
    """Trích xuất hình ảnh trực tiếp từ PDF gốc với độ sắc nét cao và không có alpha channel."""
    OUT.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    dpi = 72 * SCALE

    for basename, (page_1based, box) in CROPS.items():
        page = doc[page_1based - 1]
        rect = fitz.Rect(*box)
        # alpha=False để xuất định dạng RGB nguyên bản không kênh trong suốt
        pix = page.get_pixmap(clip=rect, dpi=dpi, alpha=False)
        out_file = OUT / f"{basename}.png"
        pix.save(str(out_file))
        print(f"Đã lưu {out_file.name}: kích thước {pix.width}x{pix.height} px")

        # Kiểm tra biên mép ảnh bằng Pillow để đảm bảo không cắt vào nét vẽ hoặc chữ
        img = Image.open(out_file)
        assert img.mode == "RGB", f"Ảnh {out_file} phải là RGB (alpha=False)"
        w, h = img.size
        top_row = [img.getpixel((x, 0)) for x in range(w)]
        bottom_row = [img.getpixel((x, h - 1)) for x in range(w)]
        left_col = [img.getpixel((0, y)) for y in range(h)]
        right_col = [img.getpixel((w - 1, y)) for y in range(h)]

        assert all(p[0] > 240 and p[1] > 240 and p[2] > 240 for p in top_row), f"Cạnh trên của {basename} bị cắt"
        assert all(p[0] > 240 and p[1] > 240 and p[2] > 240 for p in bottom_row), f"Cạnh dưới của {basename} bị cắt"
        assert all(p[0] > 240 and p[1] > 240 and p[2] > 240 for p in left_col), f"Cạnh trái của {basename} bị cắt"
        assert all(p[0] > 240 and p[1] > 240 and p[2] > 240 for p in right_col), f"Cạnh phải của {basename} bị cắt"
        print(f"Kiểm tra 4 cạnh ảnh {basename}: Hoàn toàn sạch viền trắng, bảo toàn toàn bộ nhãn.")


if __name__ == "__main__":
    crop_assets()
