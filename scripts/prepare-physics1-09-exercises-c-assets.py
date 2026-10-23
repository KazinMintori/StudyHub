"""Trích xuất hình ảnh gốc từ PDF cho nhóm bài tập Chapter 09 nhóm C."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

CROPS = {
    'c-hinh-9-25': (312, (308, 610, 528, 715)),
    'c-hinh-q9-2': (313, (75, 495, 275, 622)),
    'c-hinh-q9-4': (313, (348, 363, 608, 508)),
    'c-hinh-q9-18': (314, (194, 428, 298, 578)),
}
SCALE = 3
alpha = False
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-09'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pdf_path = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
    rows = []
    with fitz.open(pdf_path) as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=alpha)
            p = OUT / (stem + '.png')
            pix.save(p)
            with Image.open(p) as im:
                assert im.size == (pix.width, pix.height) and im.convert('RGB').tobytes() == pix.samples
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            rows.append(dict(stem=stem, pdfPage=page, clip=clip, scale=SCALE, pixelMatch=True, sha256=sha, size=(pix.width, pix.height)))

    print(f'Prepared {len(rows)} assets successfully:')
    for r in rows:
        print(r)


if __name__ == '__main__':
    main()
