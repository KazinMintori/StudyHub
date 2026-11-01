"""Extract chapter 32 theory B figures (sections 32.4-32.5, bridging, summary)."""
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-32'

# PDF 1-based page numbers and point bounding boxes (x0, y0, x1, y1)
CROPS = {
    'hinh-32-17': (1082, (34, 250, 195, 450)),
    'hinh-32-18': (1082, (0, 597, 192, 740)),
    'hinh-32-19': (1084, (80, 518, 255, 618)),
    'hinh-32-20': (1085, (456, 356, 612, 564)),
    'hinh-32-21': (1085, (400, 620, 565, 730)),
    'hinh-32-22': (1086, (36, 545, 194, 745)),
    'hinh-32-23': (1088, (36, 158, 192, 251)),
    'ung-dung-32-song-trong-chat-lieu': (1083, (456, 209, 612, 408)),
    'tom-tat-32-01': (1089, (495, 205, 609, 326)),
    'tom-tat-32-02': (1089, (495, 375, 596, 455)),
    'tom-tat-32-03': (1089, (490, 537, 585, 645)),
    'tom-tat-32-04': (1089, (495, 675, 598, 745)),
}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pdf_path = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
    with fitz.open(pdf_path) as pdf:
        for stem, (page, box) in CROPS.items():
            rect = fitz.Rect(box)
            assert pdf[page - 1].rect.contains(rect), f'{stem}: {rect} not contained in page {page}'
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
            pix.save(OUT / f'{stem}.png')
    print(f'Prepared {len(CROPS)} chapter 32 theory B images in {OUT}.')

if __name__ == '__main__':
    main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-32/hinh-32-22.png', 'pdfPage': 1086, 'bounds': [34, 545, 200, 680], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-32/tom-tat-32-01.png', 'pdfPage': 1089, 'bounds': [495, 205, 619, 326], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-32/tom-tat-32-04.png', 'pdfPage': 1089, 'bounds': [495, 675, 598, 755], 'scale': 3.0, 'masks': []}]
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
