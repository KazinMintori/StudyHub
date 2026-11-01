"""Crop Chapter 30 theory A figures and application images from the source PDF.

Run from the StudyHub repository root with Python and PyMuPDF installed.
The crop rectangles are page coordinates in points, with a margin added by the
script so labels, arrowheads, and artwork near each illustration remain intact.
"""
from pathlib import Path
import fitz

LOCAL_SOURCE = Path("raw_materials/physics/source/young-freedman-15.pdf")
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUTPUT = Path("docs/vat-ly-2/bai-giang/img/young-30")
OUTPUT.mkdir(parents=True, exist_ok=True)

# Keys are output stems. Values are (one-based PDF page number, x0, y0, x1, y1)
# in the 648 x 783 point page coordinate system. Boxes include the full artwork
# while excluding adjacent prose where practical.
CROPS = {
    "mo-dau-30": (1008, 210, 0, 648, 245),
    "hinh-30-01": (1009, 473, 105, 592, 284),
    "hinh-30-02": (1009, 456, 477, 612, 715),
    "hinh-30-03": (1010, 345, 624, 535, 735),
    "hinh-30-04": (1012, 38, 264, 190, 370),
    "ung-dung-30a-chong-set": (1012, 0, 598, 193, 741),
    "hinh-30-05": (1013, 456, 224, 612, 360),
    "hinh-30-06": (1013, 454, 468, 612, 748),
    "hinh-30-07": (1014, 36, 122, 192, 235),
    "hinh-30-08": (1014, 365, 637, 513, 746),
    "hinh-30-09": (1016, 38, 517, 185, 627),
    "ung-dung-30a-nhat-hoa": (1017, 456, 258, 648, 425),
    "hinh-30-10": (1017, 456, 634, 612, 745),
}

MARGIN = 2
SCALE = 2.5

def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found at {LOCAL_SOURCE} or {MAIN_SOURCE}")
    doc = fitz.open(SOURCE)
    for stem, (page_number, x0, y0, x1, y1) in CROPS.items():
        page = doc[page_number - 1]
        rect = fitz.Rect(x0, y0, x1, y1) + (-MARGIN, -MARGIN, MARGIN, MARGIN)
        rect &= page.rect
        pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=rect, alpha=False)
        target_path = OUTPUT / f"{stem}.png"
        pix.save(target_path)
        print(f"{stem}: PDF p.{page_number}, crop={tuple(round(v, 1) for v in rect)}, size={pix.width}x{pix.height}")
    print(f"Wrote {len(CROPS)} crops to {OUTPUT}")

if __name__ == "__main__":
    main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-30/hinh-30-06.png', 'pdfPage': 1013, 'bounds': [452, 469, 621, 750], 'scale': 2.5, 'masks': []}]
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
