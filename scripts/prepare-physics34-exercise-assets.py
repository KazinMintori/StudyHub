"""Exact chapter34 exercise figure regions. Expand only after page inspection."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image

root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-34'
out.mkdir(parents=True,exist_ok=True)
CROPS={
 'hinh-e34-15':(1171,(506,588,615,676)),
 'hinh-e34-63':(1174,(226,278,301,380)),
 'hinh-p34-72':(1174,(310,263,514,362)),
 'hinh-p34-80':(1175,(76,343,310,398)),
 'hinh-p34-81':(1175,(76,444,302,505)),
 'hinh-p34-85':(1175,(537,190,615,360)),
 'hinh-p34-89':(1176,(35,60,245,140)),
 'hinh-p34-99':(1176,(310,391,615,505)),
 'hinh-p34-100':(1176,(310,623,615,746)),
 'hinh-p34-102':(1177,(208,336,330,435)),
 'hinh-p34-104':(1177,(481,249,615,370)),
 'hinh-p34-106':(1177,(499,557,615,665)),
}
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,box) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(box),alpha=False)
  p=out/(stem+'.png');pix.save(p)
  with Image.open(p) as im:assert im.convert('RGB').tobytes()==pix.samples
  rows.append({'path':p.relative_to(root).as_posix(),'pdfPage':page,'box':box,'scale':3,'pixelMatch':True,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
q=root/'qa/physics/chapter34';q.mkdir(parents=True,exist_ok=True)
(q/'exercise-image-source-ledger.json').write_text(json.dumps({'status':'partial-inventory-pixel-checks-passed','expectedExerciseFigures':12,'extractedExerciseFigures':len(rows),'images':rows},indent=2),encoding='utf-8')
print('Verified',len(rows),'original exercise regions; full inventory requires12.')
