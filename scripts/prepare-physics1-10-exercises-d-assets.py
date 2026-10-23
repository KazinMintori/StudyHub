"""Trích xuất hình ảnh gốc từ PDF cho nhóm bài tập Chapter 10 (nhóm D: 10.1 - 10.75)."""
from pathlib import Path
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-10"

# Tọa độ vùng cắt hình ảnh gốc từ PDF (trang 1-based, (x0, y0, x1, y1))
CROPS = {
    'd-hinh-e10-01': (348, (320, 355, 570, 480)),
    'd-hinh-e10-02': (348, (355, 530, 520, 600)),
    'd-hinh-e10-03': (348, (475, 609, 570, 745)),
    'd-hinh-e10-04': (349, (150, 150, 265, 245)),
    'd-hinh-e10-07': (349, (215, 415, 335, 485)),
    'd-hinh-e10-16': (349, (510, 435, 615, 515)),
    'd-hinh-e10-22': (350, (191, 329, 296, 429)),
    'd-hinh-e10-29': (350, (465, 206, 568, 335)),
    'd-hinh-e10-37': (351, (225, 204, 335, 292)),
    'd-hinh-e10-42': (351, (223, 581, 335, 681)),
    'd-hinh-e10-45': (351, (490, 229, 620, 329)),
    'd-hinh-p10-58': (352, (345, 285, 530, 430)),
    'd-hinh-p10-61': (352, (445, 615, 568, 665)),
    'd-hinh-p10-63': (353, (260, 138, 335, 294)),
    'd-hinh-p10-64': (353, (215, 315, 335, 395)),
    'd-hinh-p10-66': (353, (235, 622, 338, 705)),
    'd-hinh-p10-69': (353, (510, 188, 610, 302)),
    'd-hinh-p10-72': (353, (420, 628, 544, 710)),
    'd-hinh-p10-73': (354, (40, 174, 282, 252)),
    'd-hinh-p10-74': (354, (180, 280, 295, 345)),
    'd-hinh-p10-75': (354, (115, 510, 230, 585)),
}

SCALE = 3

def prepare_assets():
    """Trích xuất ảnh PNG chất lượng cao từ tài liệu nguồn PDF."""
    OUT.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    mat = fitz.Matrix(SCALE, SCALE)

    for basename, (page_1based, box) in CROPS.items():
        page = doc[page_1based - 1]
        rect = fitz.Rect(box)
        pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
        out_path = OUT / f"{basename}.png"
        pix.save(str(out_path))
        print(f"Đã xuất: {out_path.name} ({pix.width}x{pix.height})")

if __name__ == "__main__":
    prepare_assets()
