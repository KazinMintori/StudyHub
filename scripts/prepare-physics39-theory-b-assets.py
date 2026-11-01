"""Extract Chapter 39 Theory B figures (Sections 39.3-39.4, Figures 39.15-39.29)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-39"

# 1-based PDF page numbers and bounding boxes (x0, y0, x1, y1) in PDF points
CROPS = {
    "hinh-39-15": (1310, (35, 168, 193, 326)),
    "hinh-39-16": (1310, (35, 385, 193, 460)),
    "hinh-39-17": (1311, (455, 88, 608, 163)),
    "hinh-39-18": (1311, (76, 523, 516, 738)),
    "hinh-39-19": (1312, (102, 115, 572, 362)),
    "hinh-39-20": (1312, (80, 555, 240, 718)),
    "hinh-39-21": (1314, (35, 93, 195, 256)),
    "hinh-39-22": (1314, (225, 638, 532, 748)),
    "hinh-39-23": (1315, (455, 86, 612, 232)),
    "hinh-39-24": (1316, (140, 483, 572, 745)),
    "hinh-39-25": (1317, (76, 631, 570, 742)),
    "hinh-39-26": (1318, (34, 595, 196, 709)),
    "hinh-39-27": (1319, (128, 545, 390, 748)),
    "hinh-39-28": (1320, (35, 402, 195, 684)),
    "hinh-39-29": (1322, (34, 95, 554, 245)),
    "hinh-39-29d": (1322, (34, 267, 195, 401)),
}

SCALE = 3.0

def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found at {LOCAL_SOURCE} or {MAIN_SOURCE}")
    OUT.mkdir(parents=True, exist_ok=True)
    with fitz.open(SOURCE) as pdf:
        for stem, (page_num, box) in CROPS.items():
            page = pdf[page_num - 1]
            rect = fitz.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=rect, alpha=False)
            target = OUT / f"{stem}.png"
            pix.save(target)
            print(f"Saved {stem}: p.{page_num}, box={box}, size={pix.width}x{pix.height}")
    print(f"Successfully prepared {len(CROPS)} images for Chapter 39 Theory B in {OUT}.")

if __name__ == "__main__":
    main()

# Final original PDF frames verified on 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-39/hinh-39-20.png', 'pdfPage': 1312, 'bounds': [80, 555, 240, 735], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-39/hinh-39-22.png', 'pdfPage': 1314, 'bounds': [219, 638, 560, 748], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-39/hinh-39-23.png', 'pdfPage': 1315, 'bounds': [455, 86, 612, 241], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-39/hinh-39-28.png', 'pdfPage': 1320, 'bounds': [35, 402, 195, 687], 'scale': 3.0, 'masks': []}]
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
