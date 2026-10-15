"""Extract unchanged chapter36 parent-owned source regions."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
root=Path(__file__).resolve().parents[1]
CROPS={
 'mo-dau-36':(1205,(0,0,439,246)),
 'ung-dung-36-adn':(1219,(455,505,648,657)),
 'ung-dung-36-vla':(1223,(455,387,648,530)),
 'ung-dung-36-dai-bang':(1225,(398,63.5,613,208)),
 'tong-ket-36-fresnel-fraunhofer':(1228,(444,90,574,156)),
 'tong-ket-36-mot-khe':(1228,(444,174,574,256)),
 'tong-ket-36-cach-tu':(1228,(444,276,574,335)),
 'tong-ket-36-bragg':(1228,(443,352,533,427)),
 'tong-ket-36-airy':(1228,(435,444,574,527)),
}
SCALE=3
out=root/'docs/vat-ly-2/bai-giang/img/young-36';out.mkdir(parents=True,exist_ok=True)
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,box) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(box),alpha=False)
  dest=out/(stem+'.png');pix.save(dest)
  with Image.open(dest) as im:assert im.convert('RGB').tobytes()==pix.samples
  rows.append(dict(path=dest.relative_to(root).as_posix(),pdfPage=page,box=box,pixelMatch=True,sha256=hashlib.sha256(dest.read_bytes()).hexdigest()))
q=root/'qa/physics/chapter36';q.mkdir(parents=True,exist_ok=True)
(q/'parent-image-source-ledger.json').write_text(json.dumps(dict(status='pixel-match-visual-review-pending',images=rows),indent=2),encoding='utf-8')
print('Extracted',len(rows),'unchanged parent image regions.')
