"""Trích xuất hình ảnh cho nhóm bài tập Chapter 10 nhóm E (10.76–10.97)."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'e-p10-79': (354, (365, 361, 520, 455)),
    'e-p10-85': (355, (220, 307, 335, 412)),
    'e-p10-89': (355, (488, 78, 615, 178)),
    'e-p10-90': (355, (350, 499, 565, 615)),
    'e-e10-42': (351, (223, 581, 335, 681)),
    'e-mcat-turntable': (356, (455, 62, 565, 212)),
}
SCALE = 3
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-10'

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
