"""Prepare PNG assets for Physics 1 Chapter 8 Theory.

Exposes CROPS and SCALE as required by StudyHub AGY specification.
"""
from pathlib import Path
import pymupdf

SCALE = 2.0

# CROPS maps basename (without extension) -> (PDF1based, (x0, y0, x1, y1))
CROPS = {
    'r-theory-mo-dau': (255, (0.0, 0.0, 440.0, 245.5)),
    'r-theory-hinh-8-01': (256, (34.0, 267.0, 198.0, 387.0)),
    'r-theory-hinh-8-02': (256, (0.0, 594.0, 194.0, 746.0)),
    'r-theory-hinh-8-03': (257, (454.0, 417.0, 640.0, 746.0)),
    'r-theory-hinh-8-04': (258, (34.0, 106.0, 196.0, 341.0)),
    'r-theory-hinh-8-05': (258, (34.0, 493.0, 196.0, 658.0)),
    'r-theory-hinh-8-06': (259, (76.0, 670.0, 342.0, 744.0)),
    'r-theory-hinh-8-07': (259, (352.0, 505.0, 512.0, 744.0)),
    'r-theory-hinh-8-08': (260, (34.0, 391.0, 298.0, 586.0)),
    'r-theory-hinh-8-09': (261, (454.0, 255.0, 618.0, 434.0)),
    'r-theory-hinh-8-10': (261, (454.0, 498.0, 618.0, 753.0)),
    'r-theory-hinh-8-11': (262, (34.0, 326.0, 201.0, 564.0)),
    'r-theory-hinh-8-12': (263, (76.0, 278.0, 342.0, 399.0)),
    'r-theory-hinh-8-13': (263, (352.0, 472.0, 616.0, 647.0)),
    'r-theory-hinh-8-14': (264, (34.0, 480.0, 298.0, 700.0)),
    'r-theory-hinh-8-15': (265, (454.0, 332.0, 618.0, 594.0)),
    'r-theory-hinh-8-16': (265, (76.0, 658.0, 515.0, 746.0)),
    'r-theory-hinh-8-17': (266, (0.0, 233.0, 205.0, 406.0)),
    'r-theory-hinh-8-18': (266, (310.0, 611.0, 575.0, 735.0)),
    'r-theory-hinh-8-19': (267, (76.0, 512.0, 342.0, 740.0)),
    'r-theory-hinh-8-20': (268, (310.0, 104.0, 575.0, 275.0)),
    'r-theory-hinh-8-21': (268, (137.0, 676.0, 575.0, 744.0)),
    'r-theory-hinh-8-22': (269, (455.0, 408.0, 648.0, 625.0)),
    'r-theory-hinh-8-23': (270, (34.0, 84.0, 201.0, 365.0)),
    'r-theory-hinh-8-24': (270, (34.0, 418.0, 201.0, 550.0)),
    'r-theory-hinh-8-25': (271, (352.0, 175.0, 616.0, 285.0)),
    'r-theory-hinh-8-26': (271, (352.0, 556.0, 616.0, 688.0)),
    'r-theory-hinh-8-27': (272, (310.0, 227.0, 575.0, 399.0)),
    'r-theory-hinh-8-28': (273, (76.0, 602.0, 342.0, 731.0)),
    'r-theory-hinh-8-29': (274, (34.0, 84.0, 201.0, 302.0)),
    'r-theory-hinh-8-30': (274, (34.0, 373.0, 196.0, 608.0)),
    'r-theory-hinh-8-31': (275, (76.0, 75.0, 342.0, 150.0)),
    'r-theory-hinh-8-32': (276, (207.0, 60.0, 576.0, 189.0)),
    'r-theory-hinh-8-33': (277, (95.0, 60.0, 405.0, 212.0)),
    'r-theory-hinh-8-34': (278, (34.0, 134.0, 196.0, 431.0)),
    'r-theory-tom-tat-1': (280, (447.0, 92.0, 574.0, 171.0)),
    'r-theory-tom-tat-2': (280, (449.0, 188.0, 585.0, 277.0)),
    'r-theory-ung-dung-go-kien': (257, (454.0, 216.0, 615.0, 377.0)),
    'r-theory-ung-dung-ngoai-hanh-tinh': (276, (34.0, 419.0, 198.0, 480.0)),
    'r-theory-ung-dung-muc': (277, (456.0, 610.0, 623.0, 744.0)),
    'r-theory-tom-tat-3': (280, (447.0, 308.0, 573.0, 407.0)),
    'r-theory-tom-tat-4': (280, (447.0, 423.0, 512.0, 477.0)),
    'r-theory-tom-tat-5': (280, (449.0, 500.0, 576.0, 565.0)),
    'r-theory-tom-tat-6': (280, (448.0, 626.0, 560.0, 687.0)),
}

def main():
    root = Path(__file__).resolve().parents[1]
    pdf_path = root / 'raw_materials/physics/source/young-freedman-15.pdf'
    out_dir = root / 'docs/vat-ly-1/bai-giang/img/young-08'
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(str(pdf_path))
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
