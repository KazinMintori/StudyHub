#!/usr/bin/env python3
"""
Crop and extract image assets for Young & Freedman 15th ed. Chapter 44 Theory B.
Covers Figures 44.10 through 44.24 and Application B-1.
"""

from pathlib import Path
import pymupdf

PDF_PATH = Path("raw_materials/physics/source/young-freedman-15.pdf")
OUTPUT_DIR = Path("docs/vat-ly-2/bai-giang/img/young-44")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Format: (name, 0-indexed page in PDF, (left, top, right, bottom) in points)
FIGURES = [
    ("hinh-44-10.png", 1518, (450, 315, 615, 510)),
    ("hinh-44-11.png", 1519, (215, 485, 565, 608)),
    ("hinh-44-12.png", 1519, (215, 620, 565, 745)),
    ("hinh-44-13.png", 1520, (455, 465, 615, 735)),
    ("hinh-44-14.png", 1522, (455, 295, 615, 585)),
    ("hinh-44-15.png", 1523, (35, 168, 193, 399)),
    ("hinh-44-16.png", 1524, (455, 216, 615, 502)),
    ("hinh-44-17.png", 1525, (35, 115, 195, 240)),
    ("hinh-44-18.png", 1526, (450, 345, 615, 730)),
    ("hinh-44-19.png", 1528, (460, 145, 610, 280)),
    ("hinh-44-20.png", 1529, (35, 360, 195, 505)),
    ("hinh-44-21.png", 1529, (35, 600, 195, 750)),
    ("ung-dung-b-1.png", 1530, (455, 220, 648, 376)),
    ("hinh-44-22.png", 1532, (75, 510, 440, 735)),
    ("hinh-44-23.png", 1536, (455, 168, 615, 405)),
    ("hinh-44-24.png", 1536, (150, 632, 366, 743)),
]

def main():
    print(f"Opening PDF: {PDF_PATH}")
    doc = pymupdf.open(str(PDF_PATH))
    scale = 3.0  # 300% DPI for crisp, high-fidelity web display
    mat = pymupdf.Matrix(scale, scale)

    for name, page_idx, (x0, y0, x1, y1) in FIGURES:
        page = doc[page_idx]
        clip_rect = pymupdf.Rect(x0, y0, x1, y1)
        pix = page.get_pixmap(matrix=mat, clip=clip_rect)

        out_path = OUTPUT_DIR / name
        pix.save(str(out_path))
        print(f"Saved {name} ({pix.width}x{pix.height} px) -> {out_path}")

if __name__ == "__main__":
    main()

# Final original PDF frames verified on 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-44/hinh-44-18.png', 'pdfPage': 1527, 'bounds': [450, 345, 615, 742], 'scale': 3.0, 'masks': []}]
if __name__ == "__main__":
    from pathlib import Path as _StudyHubPath
    import pymupdf as _studyhub_pdf
    from PIL import Image as _StudyHubImage, ImageDraw as _StudyHubImageDraw
    _studyhub_root = _StudyHubPath(__file__).resolve().parents[1]
    with _studyhub_pdf.open(_studyhub_root / 'raw_materials/physics/source/young-freedman-15.pdf') as _studyhub_document:
        for _studyhub_spec in _studyhub_final_frame_specs:
            _studyhub_box = _studyhub_spec['bounds']
            _studyhub_scale = _studyhub_spec['scale']
            _studyhub_pix = _studyhub_document[_studyhub_spec['pdfPage'] - 1].get_pixmap(matrix=_studyhub_pdf.Matrix(_studyhub_scale, _studyhub_scale), clip=_studyhub_pdf.Rect(_studyhub_box), alpha=False)
            _studyhub_image = _StudyHubImage.frombytes('RGB', (_studyhub_pix.width, _studyhub_pix.height), _studyhub_pix.samples)
            for _studyhub_mask in _studyhub_spec['masks']:
                _StudyHubImageDraw.Draw(_studyhub_image).rectangle([(_studyhub_mask[0] - _studyhub_box[0]) * _studyhub_scale, (_studyhub_mask[1] - _studyhub_box[1]) * _studyhub_scale, (_studyhub_mask[2] - _studyhub_box[0]) * _studyhub_scale, (_studyhub_mask[3] - _studyhub_box[1]) * _studyhub_scale], fill='white')
            _studyhub_destination = _studyhub_root / _studyhub_spec['file']
            _studyhub_destination.parent.mkdir(parents=True, exist_ok=True)
            _studyhub_image.save(_studyhub_destination)
