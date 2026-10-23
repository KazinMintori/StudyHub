"""Trích xuất hình ảnh gốc từ PDF cho nhóm bài tập Chapter 18 nhóm C."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-18'

# Danh mục vùng cắt chuẩn xác từ file PDF gốc (young-freedman-15.pdf)
# Định dạng: stem -> (trang PDF tính từ 1, (x0, y0, x1, y1))
CROPS = {
    'c-hinh-18-15-quang-duong-tu-do': (612, (35, 642, 195, 742)),
    'c-hinh-18-19-nhiet-dung-h2': (616, (255, 58, 525, 242)),
    'c-hinh-18-23-phan-bo-maxwell-boltzmann': (618, (36, 192, 195, 452)),
    'c-hinh-18-24-gian-do-pha': (620, (210, 83, 575, 258)),
}
SCALE = 3


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pdf_path = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
    if not pdf_path.exists():
        raise FileNotFoundError(f"Không tìm thấy file PDF nguồn tại: {pdf_path}")

    doc = fitz.open(pdf_path)
    rows = []

    for stem, (page_1based, clip_coords) in CROPS.items():
        page = doc[page_1based - 1]
        rect = fitz.Rect(clip_coords)
        pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(SCALE, SCALE), alpha=False)
        out_file = OUT / f"{stem}.png"
        pix.save(str(out_file))

        # Kiểm tra tính toàn vẹn từng pixel RGB
        with Image.open(out_file) as im:
            assert im.size == (pix.width, pix.height), f"Lỗi kích thước ảnh {stem}"
            assert im.convert('RGB').tobytes() == pix.samples, f"Lỗi sai lệch dữ liệu RGB {stem}"

        sha = hashlib.sha256(out_file.read_bytes()).hexdigest()
        rows.append({
            'stem': stem,
            'pdfPage': page_1based,
            'clip': clip_coords,
            'scale': SCALE,
            'size': (pix.width, pix.height),
            'sha256': sha,
            'pixelMatch': True,
        })
        print(f"Đã xuất và kiểm tra thành công: {out_file.name} ({pix.width}x{pix.height}) - SHA256: {sha[:16]}...")

    doc.close()
    print(f"\nTổng số ảnh đã trích xuất: {len(rows)} ảnh.")
    return rows


if __name__ == '__main__':
    main()
