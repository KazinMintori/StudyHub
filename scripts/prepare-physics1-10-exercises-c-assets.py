"""Trích xuất hình ảnh gốc từ PDF Young & Freedman 15th Edition cho Chapter 10 Nhóm C."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'c-hinh-10-11': (328, (35, 464, 195, 750)),
    'c-hinh-10-32': (342, (35, 60, 195, 256)),
    'c-hinh-10-37': (346, (310, 642, 538, 728)),
}
SCALE = 3
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-10'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    pdf_path = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
    with fitz.open(pdf_path) as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=False)
            p = OUT / f'{stem}.png'
            pix.save(p)
            with Image.open(p) as im:
                assert im.size == (pix.width, pix.height), f'Size mismatch for {stem}'
                assert im.convert('RGB').tobytes() == pix.samples, f'Pixel mismatch for {stem}'
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

    print(f'Prepared {len(rows)} assets successfully:')
    for r in rows:
        print(r)


if __name__ == '__main__':
    main()
