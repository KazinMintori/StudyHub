from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
root=Path(__file__).resolve().parents[1]
CROPS={
 'hinh-p38-38':(1297,(125,240,290,420)),
 'hinh-p38-39':(1297,(108,590,310,730)),
 'hinh-p38-44':(1298,(35,190,291,300)),
}
SCALE=3
out=root/'docs/vat-ly-2/bai-giang/img/young-38';out.mkdir(parents=True,exist_ok=True)
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,clip) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(clip),alpha=False);p=out/(stem+'.png');pix.save(p)
  with Image.open(p) as im:assert im.convert('RGB').tobytes()==pix.samples
  rows.append(dict(stem=stem,pdfPage=page,clip=clip,scale=SCALE,pixelMatch=True,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(root/'qa/physics/chapter38/exercise-image-ledger.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print('Extracted',len(rows),'unchanged exercise figure regions.')
