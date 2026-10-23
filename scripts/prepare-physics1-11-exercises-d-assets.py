"""Trích xuất hình ảnh cho nhóm bài tập Chapter 11 (11.1 - 11.48).

Chương 11: Cân bằng và Tính đàn hồi (Equilibrium and Elasticity).
Tất cả các hình trích xuất từ canonical PDF: raw_materials/physics/source/young-freedman-15.pdf.
"""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# CROPS dict: basename -> (PDF1based, (x0, y0, x1, y1))
CROPS = {
    'd-hinh-11-9b': (363, (75, 550, 600, 725)),
    'd-hinh-e11-02': (376, (165, 604, 295, 685)),
    'd-hinh-e11-07': (376, (310, 370, 550, 480)),
    'd-hinh-e11-10': (376, (460, 616, 575, 750)),
    'd-hinh-e11-13': (377, (75, 276, 285, 352)),
    'd-hinh-e11-14': (377, (75, 473, 326, 555)),
    'd-hinh-e11-15': (377, (76, 618, 325, 751)),
    'd-hinh-e11-16': (377, (499, 60, 614, 200)),
    'd-hinh-e11-17': (377, (493, 198, 612, 328)),
    'd-hinh-e11-18': (377, (495, 333, 613, 509)),
    'd-hinh-e11-19': (377, (490, 565, 614, 700)),
    'd-hinh-e11-20': (378, (168, 60, 290, 196)),
    'd-hinh-e11-21': (378, (32, 345, 279, 501)),
    'd-hinh-e11-22': (378, (34, 644, 245, 766)),
    'd-hinh-e11-23': (378, (308, 158, 524, 249)),
    'd-hinh-e11-24': (378, (308, 376, 501, 580)),
    'd-hinh-e11-38': (379, (213, 654, 330, 753)),
    'd-hinh-p11-45': (379, (506, 372, 620, 545)),
    'd-hinh-p11-47': (379, (350, 678, 615, 758)),
    'd-hinh-p11-48': (380, (34, 183, 281, 284)),
}

SCALE = 3
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-11'


def check_border_edges(img_arr):
    """Xác minh 4 mép ảnh không bị cắt xén (mép biên là nền trắng 255)."""
    t = int(np.sum(img_arr[:2, :, :] < 250))
    b = int(np.sum(img_arr[-2:, :, :] < 250))
    l = int(np.sum(img_arr[:, :2, :] < 250))
    r = int(np.sum(img_arr[:, -2:, :] < 250))
    return t, b, l, r


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pdf_path = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
    rows = []

    with fitz.open(pdf_path) as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(
                matrix=fitz.Matrix(SCALE, SCALE),
                clip=fitz.Rect(clip),
                alpha=False,
            )
            out_png = OUT / f'{stem}.png'
            pix.save(out_png)

            with Image.open(out_png) as im:
                im_rgb = im.convert('RGB')
                assert im.size == (pix.width, pix.height), f'Size mismatch for {stem}'
                assert im_rgb.tobytes() == pix.samples, f'Byte samples mismatch for {stem}'
                arr = np.array(im_rgb)
                edges = check_border_edges(arr)
                assert edges == (0, 0, 0, 0), f'Border clip detected in {stem}: {edges}'

            sha = hashlib.sha256(out_png.read_bytes()).hexdigest()
            rows.append({
                'stem': stem,
                'pdfPage': page,
                'clip': clip,
                'scale': SCALE,
                'pixelMatch': True,
                'edges': edges,
                'sha256': sha,
                'size': (pix.width, pix.height),
            })

    print(f'Extracted and verified {len(rows)} figures successfully:')
    for r in rows:
        print(f"  {r['stem']}: P{r['pdfPage']} {r['size']} edges={r['edges']} sha256={r['sha256'][:12]}...")


if __name__ == '__main__':
    main()
