"""Crop chapter 32 opening and sections 32.1-32.3 figures without cutting labels.

Run from StudyHub root with Python and PyMuPDF installed.
Crops maintain artwork, coordinate axes, and internal diagram annotations.
"""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
MAIN_SOURCE = Path("C:/Users/Ai/Documents/StudyHub/raw_materials/physics/source/young-freedman-15.pdf")
SOURCE = LOCAL_SOURCE if LOCAL_SOURCE.is_file() else MAIN_SOURCE

OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-32"

CROPS = {
    "mo-dau-32": (1068, (209, 0, 648, 246)),
    "hinh-32-01": (1069, (456, 530, 612, 742)),
    "hinh-32-02": (1070, (36, 185, 196, 455)),
    "hinh-32-03": (1070, (70, 605, 570, 725)),
    "hinh-32-04": (1071, (75, 566, 475, 722)),
    "hinh-32-05": (1072, (36, 568, 190, 718)),
    "hinh-32-06": (1073, (456, 83, 613, 253)),
    "hinh-32-07": (1073, (456, 367, 613, 685)),
    "hinh-32-08": (1074, (36, 217, 195, 539)),
    "hinh-32-09": (1075, (456, 93, 613, 283)),
    "hinh-32-10": (1076, (36, 93, 191, 351)),
    "hinh-32-11": (1076, (36, 478, 191, 749)),
    "hinh-32-12": (1077, (456, 528, 613, 748)),
    "hinh-32-13": (1078, (36, 253, 195, 430)),
    "hinh-32-14": (1079, (456, 123, 612, 260)),
    "hinh-32-15": (1079, (395, 555, 575, 715)),
    "hinh-32-16": (1080, (0, 606, 192, 742)),
    "ung-dung-32-thi-giac-tu-ngoai": (1072, (36, 225, 193, 345)),
    "ung-dung-32-song-phang-tu-vu-tru": (1078, (0, 600, 193, 742)),
}

SCALE = 2.5

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
    print(f"Successfully prepared {len(CROPS)} images for chapter 32 theory A.")

if __name__ == "__main__":
    main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-32/hinh-32-04.png', 'pdfPage': 1071, 'bounds': [75, 566, 490, 722], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-32/hinh-32-08.png', 'pdfPage': 1074, 'bounds': [36, 217, 195, 546], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-32/hinh-32-14.png', 'pdfPage': 1079, 'bounds': [456, 123, 631, 260], 'scale': 2.5, 'masks': []}]
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
