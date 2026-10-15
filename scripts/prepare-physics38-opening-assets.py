from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
root=Path(__file__).resolve().parents[1]
CROPS={'mo-dau-38':(1273,(0,0,444,252))}
SCALE=3
out=root/'docs/vat-ly-2/bai-giang/img/young-38';out.mkdir(parents=True,exist_ok=True)
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 rows=[]
 for stem,(page,clip) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(clip),alpha=False);p=out/(stem+'.png');pix.save(p)
  with Image.open(p) as im:assert im.convert('RGB').tobytes()==pix.samples
  rows.append(dict(path=p.relative_to(root).as_posix(),pdfPage=page,clip=clip,scale=SCALE,pixelMatch=True,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
q=root/'qa/physics/chapter38';q.mkdir(parents=True,exist_ok=True)
(q/'opening-image-ledger.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print('Extracted unchanged chapter38 opening image.')
