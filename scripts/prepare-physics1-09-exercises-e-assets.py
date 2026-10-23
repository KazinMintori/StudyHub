"""Trích xuất hình ảnh nguyên tác từ PDF cho nhóm bài tập Chapter 09 (9.49-9.95).

Tất cả các hình ảnh được crop trực tiếp với độ phân giải cao (scale=3) từ tệp
raw_materials/physics/source/young-freedman-15.pdf nhằm bảo toàn 100% chi tiết
nguyên gốc, không cắt phạm nhãn, không vẽ lại.
"""
from pathlib import Path
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT_DIR = ROOT / "docs/vat-ly-1/bai-giang/img/young-09"

SCALE = 3
ALPHA = False

# CROPS dict: basename -> (PDF 1-based page, (x0, y0, x1, y1))
CROPS = {
    'e-fig-e9-49': (317, (250, 279, 338, 398)),
    'e-fig-p9-61': (317, (350, 544, 570, 656)),
    'e-fig-p9-64': (318, (190, 129.5, 295, 282)),
    'e-fig-p9-77': (318, (310, 642, 520, 742)),
    'e-fig-p9-78': (319, (75, 108, 285, 252)),
    'e-fig-p9-79': (319, (255, 258, 336, 428)),
    'e-fig-p9-82': (319, (225, 591.5, 336, 668)),
    'e-fig-p9-83': (319, (505, 60, 615, 218)),
    'e-fig-p9-86': (319, (505, 361.0, 615, 532)),
    'e-fig-p9-87': (320, (32, 160, 255, 292)),
    'e-fig-p9-89': (320, (310, 62, 525, 192)),
    'e-fig-p9-90': (320, (310, 264, 500, 408)),
    'e-fig-9-17': (306, (310, 332, 570, 532)),
    'e-table-9-2-cd': (305, (305, 83, 615, 235)),
}


def prepare_assets():
    """Trích xuất và lưu tất cả các hình ảnh theo CROPS."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(PDF_PATH))
    results = {}
    for name, (pno, bbox) in CROPS.items():
        page = doc[pno - 1]
        rect = fitz.Rect(bbox)
        pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(SCALE, SCALE), alpha=ALPHA)
        out_file = OUT_DIR / f"{name}.png"
        pix.save(str(out_file))
        img = Image.open(out_file)
        results[name] = {
            "page": pno,
            "bbox": bbox,
            "size": img.size,
            "path": str(out_file),
        }
        print(f"Saved {name}.png ({img.size[0]}x{img.size[1]}) from page {pno}")
    return results


if __name__ == "__main__":
    prepare_assets()
