"""Trích xuất hình ảnh gốc từ PDF Young & Freedman 15th ed cho Chapter 19 bài tập nhóm C.

Các hình ảnh cần trích xuất:
- c-fig-19-22: Hình 19.22 (trang 654) cho Bài tập cầu nối (Bridging Problem).
- c-fig-q19-23: Hình Q19.23 (trang 655) cho câu hỏi thảo luận Q19.23.
- c-fig-q19-24: Hình Q19.24 (trang 655) cho câu hỏi thảo luận Q19.24.
"""

from pathlib import Path
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT_DIR = ROOT / "docs/vat-ly-1/bai-giang/img/young-19"
SCALE = 3
alpha = False

# CROPS dict basename -> (PDF 1-based page, (x0, y0, x1, y1))
CROPS = {
    "c-fig-19-22": (654, (308, 58, 566, 173)),
    "c-fig-q19-23": (655, (74, 230, 265, 346)),
    "c-fig-q19-24": (655, (74, 425, 265, 555)),
}


def crop_images():
    """Trích xuất ảnh gốc từ PDF ở độ phân giải cao và lưu định dạng RGB PNG (alpha=False)."""
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Không tìm thấy file PDF nguồn: {PDF_PATH}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF_PATH)

    for basename, (page_1based, rect_coords) in CROPS.items():
        page = doc[page_1based - 1]
        rect = fitz.Rect(rect_coords)
        pix = page.get_pixmap(clip=rect, dpi=72 * SCALE, alpha=alpha)
        target = OUT_DIR / f"{basename}.png"
        pix.save(target)

        # Kiểm tra lại bằng Pillow để đảm bảo kênh màu RGB và alpha=False
        with Image.open(target) as img:
            if img.mode != "RGB":
                img = img.convert("RGB")
                img.save(target)
            w, h = img.size

        print(f"Đã xuất: {target.relative_to(ROOT)} ({w}x{h}, RGB, alpha={alpha})")


def verify_image_edges():
    """Kiểm tra các đường viền ảnh để đảm bảo không bị cắt phạm văn bản hay nhãn đồ thị."""
    for basename in CROPS:
        target = OUT_DIR / f"{basename}.png"
        if not target.exists():
            raise FileNotFoundError(f"Thiếu file ảnh: {target}")
        with Image.open(target) as img:
            w, h = img.size
            assert w > 100 and h > 100, f"Ảnh {basename} có kích thước bất thường ({w}x{h})"
            # Kiểm tra 4 góc không bị đen hoặc lỗi biên
            pixels = img.load()
            corners = [pixels[0, 0], pixels[w - 1, 0], pixels[0, h - 1], pixels[w - 1, h - 1]]
            for c in corners:
                assert min(c) > 200, f"Góc ảnh {basename} không sáng (nền trắng): {c}"
        print(f"Kiểm tra biên ảnh {basename}.png: HỢP LỆ")


if __name__ == "__main__":
    crop_images()
    verify_image_edges()
