"""Unmodified source rectangles for the opening and section34.1."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image

root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-34'
out.mkdir(parents=True,exist_ok=True)
CROPS={
 'mo-dau-34':(1130,(210,0,648,246)),
 'hinh-34-01':(1131,(485,115,577,195)),
 'hinh-34-02':(1131,(455,290,615,436)),
 'hinh-34-03':(1131,(455,550,615,712)),
 'hinh-34-04':(1132,(35,117,195,248)),
 'hinh-34-05':(1132,(35,303,195,539)),
 'hinh-34-06':(1132,(35,596,195,715)),
 'hinh-34-07':(1133,(455,143,615,301)),
 'hinh-34-08':(1133,(456,379,612,487)),
 'hinh-34-09':(1133,(455,572,615,734)),
}
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,box) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(box),alpha=False)
  p=out/(stem+'.png');pix.save(p)
  with Image.open(p) as im:assert im.convert('RGB').tobytes()==pix.samples
  rows.append({'path':p.relative_to(root).as_posix(),'pdfPage':page,'box':box,'scale':3,'pixelMatch':True,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
q=root/'qa/physics/chapter34';q.mkdir(parents=True,exist_ok=True)
(q/'opening-image-source-ledger.json').write_text(json.dumps({'status':'pixel-match-visual-review-pending','images':rows},indent=2),encoding='utf-8')
print('Extracted ten original source regions. Visual review still required.')
