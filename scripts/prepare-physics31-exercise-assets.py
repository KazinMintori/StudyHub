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
