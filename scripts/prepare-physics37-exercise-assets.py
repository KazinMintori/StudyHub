"""Extract source figures accompanying the chapter37 end questions."""
from pathlib import Path
import json
import pymupdf as fitz
from PIL import Image
root=Path(__file__).resolve().parents[1]
CROPS={
 'hinh-q37-3':(1266,(455,596,575,665)),
 'hinh-e37-18':(1268,(35,574,275,617)),
 'hinh-p37-41':(1269,(130,557,275,642)),
 'hinh-p37-55':(1270,(184,387,301,514)),
 'hinh-p37-67':(1271,(526,79,615,161)),
 'hinh-p37-68':(1271,(496,401,614,500)),
}
SCALE=3
out=root/'docs/vat-ly-2/bai-giang/img/young-37';out.mkdir(parents=True,exist_ok=True)
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,box) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(box),alpha=False)
  p=out/(stem+'.png');pix.save(p)
  with Image.open(p) as im:assert im.convert('RGB').tobytes()==pix.samples
  rows.append(dict(stem=stem,pdfPage=page,box=box,pixelMatch=True))
(root/'qa/physics/chapter37/exercise-image-ledger.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print('Extracted',len(rows),'unchanged exercise figure regions.')
