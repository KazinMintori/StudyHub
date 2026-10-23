"""Trích xuất hình ảnh cho nhóm bài tập Chapter 19 (19.1 - 19.33)."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'd-hinh-e19-4': (655, (350, 220, 560, 340)),
    'd-hinh-19-7a': (637, (450, 220, 615, 380)),
    'd-hinh-e19-11': (656, (30, 130, 230, 255)),
    'd-hinh-e19-13': (656, (30, 385, 235, 525)),
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
