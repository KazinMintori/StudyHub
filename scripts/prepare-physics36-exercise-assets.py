"""Unchanged original exercise images, including all dots, labels and the moving membranes."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
root=Path(__file__).resolve().parents[1];out=root/'docs/vat-ly-2/bai-giang/img/young-36';out.mkdir(parents=True,exist_ok=True)
CROPS={
 'hinh-p36-58':(1233,(364,552,602,690)),
 'hinh-p36-61':(1234,(45,580,286,625)),
 'hinh-p36-65':(1235,(216,94,338,229)),
}
SCALE=3;rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,box) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(box),alpha=False);p=out/(stem+'.png');pix.save(p)
  with Image.open(p) as im:assert im.convert('RGB').tobytes()==pix.samples
  rows.append(dict(path=p.relative_to(root).as_posix(),pdfPage=page,box=box,scale=SCALE,pixelMatch=True,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
q=root/'qa/physics/chapter36';q.mkdir(parents=True,exist_ok=True)
(q/'exercise-image-source-ledger.json').write_text(json.dumps(dict(status='pixel-match-visual-review-pending',images=rows),indent=2),encoding='utf-8')
print('Extracted all three unchanged original exercise images.')
