"""Render complete diagrams for the end-of-chapter inductance problems."""
from pathlib import Path
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-30'
CROPS={
 'hinh-q30-10':(1031,(223,541,337,587)),
 'hinh-e30-09':(1032,(216,245,293,279)),
 'hinh-p30-50':(1034,(175,514,296,584)),
 'hinh-p30-51':(1034,(325,214,527,306)),
 'hinh-p30-52':(1034,(461,329,575,398)),
 'hinh-p30-57':(1035,(226,208,338,281)),
 'hinh-p30-58':(1035,(222,305,343,416)),
 'hinh-p30-60':(1035,(117,689,287,748)),
 'hinh-p30-61':(1035,(505,78,619,163)),
 'hinh-p30-63':(1035,(522,322,619,398)),
 'hinh-p30-65':(1035,(423,626,598,712)),
 'hinh-p30-66':(1036,(110,162,220,236)),
 'hinh-p30-67':(1036,(107,485,272,570)),
 'hinh-p30-68':(1036,(349,77,522,164)),
 'hinh-p30-69':(1036,(353,370,536,457)),
 'hinh-p30-70':(1036,(457,485,572,553)),
 'hinh-p30-71':(1037,(234,77,338,177)),
}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for name,(page,rect) in CROPS.items():
   pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(rect),alpha=False).save(OUT/f'{name}.png')
 print('Rendered seventeen end-of-chapter diagrams with their labels and arrows.')
if __name__=='__main__':main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-30/hinh-p30-50.png', 'pdfPage': 1034, 'bounds': [175, 514, 304, 584], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-30/hinh-p30-51.png', 'pdfPage': 1034, 'bounds': [325, 214, 527, 313], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-30/hinh-p30-52.png', 'pdfPage': 1034, 'bounds': [449, 329, 575, 398], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-30/hinh-p30-58.png', 'pdfPage': 1035, 'bounds': [215, 305, 343, 416], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-30/hinh-p30-60.png', 'pdfPage': 1035, 'bounds': [117, 683, 287, 748], 'scale': 3.0, 'masks': [[117, 683, 134, 691]]}, {'file': 'docs/vat-ly-2/bai-giang/img/young-30/hinh-p30-67.png', 'pdfPage': 1036, 'bounds': [107, 485, 272, 576], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-30/hinh-p30-69.png', 'pdfPage': 1036, 'bounds': [345, 370, 536, 457], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-30/hinh-p30-70.png', 'pdfPage': 1036, 'bounds': [457, 478, 572, 553], 'scale': 3.0, 'masks': []}]
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
