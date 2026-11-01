"""Crop chapter31 opening and section31.1 figures without cutting labels."""
from pathlib import Path
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-31'
CROPS={
 'mo-dau-31':(1038,(210,0,648,245)),
 'ky-hieu-nguon-xoay-chieu':(1039,(230,101,287,126)),
 'hinh-31-01':(1039,(455,87,613,226)),
 'hinh-31-02':(1039,(452,373,615,529)),
 'hinh-31-03':(1040,(39,95,192,451)),
 'hinh-31-04':(1040,(35,499,193,724)),
 'hinh-31-05':(1041,(456,87,612,192)),
 'hinh-31-06':(1041,(436,306,561,454)),
 'tu-kiem-31-01':(1041,(484,605,582,698)),
}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,box) in CROPS.items():
   pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(box),alpha=False).save(OUT/f'{stem}.png')
 print('Prepared nine opening and section31.1 assets for source review.')
if __name__=='__main__':main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-31-02.png', 'pdfPage': 1039, 'bounds': [452, 373, 622, 529], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-31-04.png', 'pdfPage': 1040, 'bounds': [35, 499, 193, 733], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-31-06.png', 'pdfPage': 1041, 'bounds': [394, 306, 561, 454], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-31/tu-kiem-31-01.png', 'pdfPage': 1041, 'bounds': [484, 605, 590, 698], 'scale': 3.0, 'masks': []}]
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
