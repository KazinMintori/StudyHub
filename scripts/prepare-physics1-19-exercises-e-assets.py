"""Trích xuất hình ảnh cho nhóm bài tập Chapter 19 (19.34 - 19.66)."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'e-hinh-p19-35': (657, (500, 75, 615, 185)),
    'e-hinh-p19-37': (657, (487, 328, 614, 443)),
    'e-hinh-p19-38': (657, (490, 450, 615, 560)),
    'e-hinh-p19-39': (657, (500, 604, 606, 715)),
    'e-hinh-p19-40': (658, (180, 60, 295, 156)),
    'e-hinh-p19-41': (658, (168, 183, 290, 283)),
    'e-hinh-p19-42': (658, (180, 335, 295, 456)),
    'e-hinh-p19-43': (658, (167, 458, 290, 580)),
    'e-hinh-p19-44': (658, (310, 60, 532, 202)),
    'e-hinh-p19-50': (659, (230, 391, 342, 589)),
    'e-hinh-p19-59': (659, (488, 534.6, 614, 650)),
}
SCALE = 3
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-19'

def inspect_edges(img_path):
    """Kiểm tra 4 biên của ảnh xem có bị cắt chữ hoặc dính pixel viền không."""
    with Image.open(img_path) as im:
        arr = np.array(im.convert('RGB'))
    non_white = np.any(arr < 245, axis=2)
    top_active = bool(np.any(non_white[:3, :]))
    bot_active = bool(np.any(non_white[-3:, :]))
    left_active = bool(np.any(non_white[:, :3]))
    right_active = bool(np.any(non_white[:, -3:]))
    return {
        'top_active': top_active,
        'bot_active': bot_active,
        'left_active': left_active,
        'right_active': right_active,
    }

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pdf_path = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
    rows = []
    with fitz.open(pdf_path) as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=False)
            p = OUT / (stem + '.png')
            pix.save(p)
            with Image.open(p) as im:
                assert im.size == (pix.width, pix.height), f'Kích thước không khớp cho {stem}'
                assert im.convert('RGB').tobytes() == pix.samples, f'Byte RGB không khớp cho {stem}'
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            edges = inspect_edges(p)
            assert not any(edges.values()), f'Viền ảnh {stem} bị chạm nội dung: {edges}'
            rows.append({
                'stem': stem,
                'pdfPage': page,
                'clip': clip,
                'scale': SCALE,
                'pixelMatch': True,
                'edgesClean': True,
                'sha256': sha,
                'size': (pix.width, pix.height),
            })
    print(f'Trích xuất thành công {len(rows)} hình ảnh từ PDF:')
    for r in rows:
        print(r)

if __name__ == '__main__':
    main()
