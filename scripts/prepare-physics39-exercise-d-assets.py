"""Trích xuất hình ảnh cho nhóm bài tập Chapter 39 nhóm D."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'hinh-39-36': (1332, (377.136, 502.549, 504.864, 630.277)),
    'hinh-p39-84': (1339, (118, 602, 290, 722)),
}
SCALE = 3
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-39'

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    with fitz.open(ROOT / 'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=False)
            p = OUT / (stem + '.png')
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
