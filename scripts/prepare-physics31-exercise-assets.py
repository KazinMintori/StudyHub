"""Extract exercise artwork directly from the supplied PDF, without redrawing."""
from pathlib import Path
import hashlib,json
import pymupdf as fitz
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-31'
CROPS={
 'hinh-bridge31-01':(1047,(450,105,590,220)),
 'hinh-p31-40':(1064,(310,150,560,310)),
 'hinh-p31-44':(1064,(500,499,590,577)),
 'hinh-p31-47':(1065,(220,150,335,230)),
 'hinh-p31-48':(1065,(75,400,335,485)),
 'hinh-p31-53':(1065,(510,255,625,360)),
 'hinh-p31-62':(1066,(310,58,575,165)),
 'hinh-p31-63':(1066,(310,265,575,380)),
 'hinh-p31-65':(1066,(460,560,570,645)),
 'hinh-p31-66':(1067,(235,75,340,160)),
}
def main():
 OUT.mkdir(parents=True,exist_ok=True);records=[]
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,rect) in CROPS.items():
   pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(rect),alpha=False)
   path=OUT/(stem+'.png');pix.save(path)
   with Image.open(path) as image:
    assert image.size==(pix.width,pix.height)
    assert image.convert('RGB').tobytes()==pix.samples,'Artwork pixels changed: '+stem
   records.append({'file':stem+'.png','type':'unchanged-source-artwork','pdfPage':page,
                   'printedPage':page-20,'clipPoints':rect,'scale':3,
                   'pixelEqualityToPdfRendering':True,
                   'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
 p=ROOT/'qa/physics/chapter31/exercise-image-source-ledger.json'
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 print('Extracted ten unchanged source diagrams and verified pixel equality.')
if __name__=='__main__':main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-31/hinh-p31-47.png', 'pdfPage': 1065, 'bounds': [220, 150, 345, 230], 'scale': 3.0, 'masks': []}]
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
