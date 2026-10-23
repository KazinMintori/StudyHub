"""Prepare PNG assets for Physics 1 Chapter 7 Theory.

Exposes CROPS and SCALE as required by StudyHub AGY specification.
Generates crops for all theoretical figures, photos, examples, and summary diagrams.
"""
from pathlib import Path
import pymupdf

SCALE = 2.0

# CROPS maps basename (without extension) -> (PDF1based, (x0, y0, x1, y1))
CROPS = {
    'r-theory-mo-dau': (221, (0.0, 0.0, 440.0, 246.0)),
    'r-theory-hinh-7-01': (222, (35.0, 126.0, 195.0, 265.0)),
    'r-theory-hinh-7-02': (222, (35.0, 390.0, 195.0, 745.0)),
    'r-theory-hinh-7-03': (223, (78.0, 640.0, 440.0, 747.0)),
    'r-theory-hinh-7-04': (224, (35.0, 502.0, 280.0, 660.0)),
    'r-theory-hinh-7-05': (225, (455.0, 169.0, 648.0, 365.0)),
    'r-theory-hinh-7-06': (226, (35.0, 84.0, 300.0, 320.0)),
    'r-theory-hinh-7-07': (227, (455.0, 93.0, 616.0, 345.0)),
    'r-theory-hinh-7-08': (227, (350.0, 400.0, 612.0, 560.0)),
    'r-theory-hinh-7-09': (228, (35.0, 85.0, 572.0, 238.0)),
    'r-theory-hinh-7-10': (228, (312.0, 574.0, 572.0, 742.0)),
    'r-theory-hinh-7-11': (229, (78.0, 488.0, 335.0, 742.0)),
    'r-theory-tyu-7-01': (230, (250.0, 108.0, 530.0, 185.0)),
    'r-theory-hinh-7-12': (230, (36.0, 424.0, 193.0, 639.0)),
    'r-theory-hinh-7-13': (231, (455.0, 108.0, 616.0, 458.0)),
    'r-theory-hinh-7-14': (231, (455.0, 636.0, 616.0, 745.0)),
    'r-theory-hinh-7-15': (232, (36.0, 502.0, 194.0, 742.0)),
    'r-theory-hinh-7-16': (233, (78.0, 385.0, 335.0, 510.0)),
    'r-theory-hinh-7-17': (234, (36.0, 540.0, 290.0, 742.0)),
    'r-theory-hinh-7-18': (235, (455.0, 605.0, 615.0, 742.0)),
    'r-theory-hinh-7-19': (236, (378.0, 571.0, 506.0, 675.0)),
    'r-theory-hinh-7-20': (237, (78.0, 562.0, 326.0, 742.0)),
    'r-theory-hinh-7-21': (238, (0.0, 473.0, 193.0, 604.0)),
    'r-theory-hinh-7-22': (240, (75.0, 74.0, 575.0, 195.0)),
    'r-theory-hinh-7-23': (242, (35.0, 276.0, 194.0, 509.0)),
    'r-theory-hinh-7-24': (243, (75.0, 85.0, 440.0, 398.0)),
    'r-theory-ung-dung-7-01': (243, (455.0, 492.0, 612.0, 598.0)),
    'r-theory-tom-tat-01': (244, (449.0, 98.0, 573.0, 186.0)),
    'r-theory-tom-tat-02': (244, (449.0, 224.0, 574.0, 288.0)),
    'r-theory-tom-tat-03': (244, (448.0, 323.0, 574.0, 405.0)),
    'r-theory-tom-tat-04': (244, (448.0, 440.0, 584.0, 510.0)),
    'r-theory-tom-tat-05': (244, (449.0, 582.0, 574.0, 653.0)),
    'r-theory-ung-dung-chim-boi-ca': (223, (455.0, 191.0, 613.0, 395.0)),
    'r-theory-ung-dung-bao-ghe-pa': (232, (0.0, 180.0, 193.0, 354.0)),
    'r-theory-ung-dung-lop-xe': (238, (0.0, 207.0, 193.0, 353.0)),
    'r-theory-ung-dung-dia-hinh': (241, (450.0, 257.0, 648.0, 403.0)),
    'r-theory-tyu-7-02': (235, (119.0, 320.0, 441.0, 362.0)),
}


def main():
    root = Path(__file__).resolve().parents[1]
    pdf_path = root / 'raw_materials/physics/source/young-freedman-15.pdf'
    out_dir = root / 'docs/vat-ly-1/bai-giang/img/young-07'
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
