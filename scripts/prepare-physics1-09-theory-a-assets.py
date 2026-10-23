"""Prepare PNG assets for Physics 1 Chapter 9 Theory A (Sections 9.1, 9.2, 9.3).

Exposes CROPS and SCALE as required by StudyHub AGY specification.
"""
from pathlib import Path
import pymupdf

SCALE = 2.0

# CROPS maps basename (without extension) -> (PDF1based, (x0, y0, x1, y1))
CROPS = {
    'a-mo-dau': (292, (210.0, 0.0, 648.0, 245.5)),
    'a-hinh-9-01': (293, (455.0, 95.0, 615.0, 235.0)),
    'a-hinh-9-02': (293, (458.0, 278.0, 605.0, 515.0)),
    'a-hinh-9-03': (293, (95.0, 615.0, 425.0, 742.0)),
    'a-hinh-9-04': (294, (34.0, 252.0, 196.0, 450.0)),
    'a-hinh-9-05': (295, (95.0, 585.0, 425.0, 742.0)),
    'a-hinh-9-06': (296, (35.0, 138.0, 196.0, 280.0)),
    'a-hinh-9-07': (297, (454.0, 95.0, 615.0, 215.0)),
    'a-tyu-9-01': (297, (315.0, 188.0, 442.0, 255.0)),
    'a-ung-dung-vi-khuan': (297, (455.0, 502.0, 648.0, 650.0)),
    'a-hinh-9-08': (299, (138.0, 74.0, 275.0, 210.0)),
    'a-hinh-9-09': (300, (30.0, 82.0, 198.0, 302.0)),
    'a-hinh-9-10': (300, (30.0, 490.0, 198.0, 708.0)),
    'a-hinh-9-11': (301, (458.0, 151.0, 612.0, 328.0)),
    'a-hinh-9-12': (301, (170.0, 622.0, 520.0, 735.0)),
    'a-hinh-9-13': (302, (68.0, 383.0, 548.0, 520.0)),
}

def main():
    root = Path(__file__).resolve().parents[1]
    pdf_path = root / 'raw_materials/physics/source/young-freedman-15.pdf'
    out_dir = root / 'docs/vat-ly-1/bai-giang/img/young-09'
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(pdf_path)
    mat = pymupdf.Matrix(SCALE, SCALE)

    print(f"Generating {len(CROPS)} images with SCALE={SCALE}, alpha=False...")
    for name, (p1, (x0, y0, x1, y1)) in CROPS.items():
        page = doc[p1 - 1]
        clip_rect = pymupdf.Rect(x0, y0, x1, y1)
        pix = page.get_pixmap(matrix=mat, clip=clip_rect, alpha=False)
        out_path = out_dir / f"{name}.png"
        pix.save(str(out_path))
        print(f"  Saved {out_path.name} ({pix.width}x{pix.height}) from PDF page {p1}")

if __name__ == '__main__':
    main()
