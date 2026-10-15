"""Original unnumbered self-check diagram and separate original photo panel.

No redraw, compositing, recoloring or source-pixel modification.
"""
from pathlib import Path
import hashlib,json
import pymupdf as fitz
from PIL import Image

root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-33'
out.mkdir(parents=True,exist_ok=True)
regions={
 'tu-kiem-33-02.png':(1105,(456,263,614,360)),
 'hinh-33-25b.png':(1113,(455,63.5,612.5,220)),
}
ledger=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for name,(number,bounds) in regions.items():
  p=pdf[number-1]
  pix=p.get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(bounds),alpha=False)
  path=out/name
  pix.save(path)
  with Image.open(path) as img:
   assert img.convert('RGB').tobytes()==pix.samples
  ledger.append({'path':path.relative_to(root).as_posix(),'pdfPage':number,'rect':bounds,'scale':3,
   'pixelMatch':True,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
qa=root/'qa/physics/chapter33'
(qa/'extra-image-source-ledger.json').write_text(json.dumps({'status':'passed','sourceCrops':ledger},indent=2),encoding='utf-8')
print('Verified two original source rectangles.')
