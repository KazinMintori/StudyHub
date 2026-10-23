"""Trích xuất hình ảnh tham chiếu cho nhóm bài tập Chapter 17 nhóm C."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'c-thanh-ghep-dan-nhiet': (583, (76, 622, 326, 718)),
}
SCALE = 3
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-17'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    with fitz.open(ROOT / 'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=False)
            p = OUT / (stem + '.png')
            pix.save(p)
            with Image.open(p) as im:
                assert im.size == (pix.width, pix.height), f"Kích thước ảnh không khớp cho {stem}"
                assert im.convert('RGB').tobytes() == pix.samples, f"Dữ liệu pixel không khớp cho {stem}"
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            rows.append({
                'stem': stem,
                'pdfPage': page,
                'clip': clip,
                'scale': SCALE,
                'pixelMatch': True,
                'sha256': sha,
                'size': (pix.width, pix.height)
            })

    print(f'Đã trích xuất thành công {len(rows)} tài nguyên hình ảnh:')
    for r in rows:
        print(r)


if __name__ == '__main__':
    main()
