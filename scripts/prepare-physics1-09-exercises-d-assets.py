"""Trích xuất hình ảnh cho nhóm bài tập Chapter 09 nhóm D."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'd-hinh-e9-18': (315, (238, 580, 340, 745)),
    'd-hinh-e9-30': (316, (170, 130, 295, 225)),
    'd-hinh-e9-35': (316, (188, 604, 300, 738)),
    'd-hinh-e9-47': (317, (218, 62, 335, 213)),
}
SCALE = 3
alpha = False
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-09'

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    pdf_path = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
    with fitz.open(pdf_path) as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=alpha)
            p = OUT / f'{stem}.png'
            pix.save(p)
            with Image.open(p) as im:
                assert im.size == (pix.width, pix.height) and im.convert('RGB').tobytes() == pix.samples
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            rows.append(dict(stem=stem, pdfPage=page, clip=clip, scale=SCALE, pixelMatch=True, sha256=sha, size=(pix.width, pix.height)))
    print(f'Extracted {len(rows)} figures successfully:')
    for r in rows:
        print(r)

if __name__ == '__main__':
    main()
