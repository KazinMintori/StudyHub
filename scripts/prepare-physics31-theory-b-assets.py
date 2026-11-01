"""Extract chapter31 figures7–24, application photos and seven summary diagrams."""
from pathlib import Path
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-31'
# PDF1-based page and point coordinates. Retain all labels and panel headings.
CROPS={
 'hinh-31-07':(1042,(34,104,197,471)),
 'hinh-31-08':(1042,(116,592,619,743)),
 'hinh-31-09':(1045,(450,84,617,472)),
 'hinh-31-10':(1045,(350,528,617,613)),
 'hinh-31-11':(1046,(37,175,181,295)),
 'hinh-31-12':(1046,(33,381,196,742)),
 'hinh-31-13':(1047,(451,108,615,550)),
 'hinh-31-14':(1048,(44,199,184,397)),
 'ung-dung-31-do-thanh-phan-co-the':(1048,(35,552,193,742)),
 'hinh-31-15':(1050,(360,372,520,510)),
 'hinh-31-16':(1051,(74,559,612,735)),
 'hinh-31-17':(1052,(33,631,205,742)),
 'hinh-31-18':(1054,(34,232,183,614)),
 'hinh-31-19':(1055,(455,114,611,239)),
 'hinh-31-20':(1055,(118,594,309,741)),
 'ky-hieu-may-bien-ap':(1056,(374,547,402,584)),
 'hinh-31-21':(1056,(414,600,572,750)),
 'ung-dung-31-dien-ap-cao':(1056,(0,457,192,602)),
 'hinh-31-22':(1057,(455,374,613,482)),
 'hinh-31-23':(1057,(455,599,613,746)),
 'hinh-31-24':(1058,(121,606,542,739)),
 'ung-dung-31-truyen-tai-mot-chieu':(1058,(0,224,193,384)),
 'tom-tat-31-01-gian-do-pha':(1060,(448,96,515,166)),
 'tom-tat-31-02-pha-dien-ap':(1060,(448,231,515,293)),
 'tom-tat-31-03-dien-khang':(1060,(445,306,574,370)),
 'tom-tat-31-04-mach-rlc':(1060,(448,405,538,475)),
 'tom-tat-31-05-cong-suat':(1060,(447,488,530,560)),
 'tom-tat-31-06-cong-huong':(1060,(447,573,563,645)),
 'tom-tat-31-07-may-bien-ap':(1060,(449,662,565,736)),
}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,box) in CROPS.items():
   rect=fitz.Rect(box)
   assert pdf[page-1].rect.contains(rect),(stem,rect)
   pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=rect,alpha=False).save(OUT/f'{stem}.png')
 print(f'Prepared {len(CROPS)} section31.2–31.6 and summary images for visual review.')
if __name__=='__main__':main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-31-12.png', 'pdfPage': 1046, 'bounds': [33, 381, 196, 750], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-31-16.png', 'pdfPage': 1051, 'bounds': [74, 559, 612, 742], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-31-18.png', 'pdfPage': 1054, 'bounds': [34, 232, 198, 626], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-31-19.png', 'pdfPage': 1055, 'bounds': [455, 114, 611, 246], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-31-20.png', 'pdfPage': 1055, 'bounds': [106, 594, 309, 741], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-31-21.png', 'pdfPage': 1056, 'bounds': [414, 600, 590, 750], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-31-24.png', 'pdfPage': 1058, 'bounds': [121, 606, 560, 744], 'scale': 3.0, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-31/tom-tat-31-04-mach-rlc.png', 'pdfPage': 1060, 'bounds': [448, 405, 538, 484], 'scale': 3.0, 'masks': []}]
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
