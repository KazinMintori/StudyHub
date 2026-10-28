"""Verify two original chapter10 crops without modifying public files."""
from pathlib import Path
import ast,hashlib
import pymupdf
from PIL import Image
ROOT=Path(__file__).resolve().parents[2]
tree=ast.parse((ROOT/'scripts/prepare-physics1-10-theory-a-assets.py').read_text('utf8'))
values={}
for node in tree.body:
 if isinstance(node,ast.Assign):
  for target in node.targets:
   if isinstance(target,ast.Name)and target.id in['CROPS','SCALE']:values[target.id]=ast.literal_eval(node.value)
pdf=pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')
expected={'a-hinh-10-10':(328,(34,96,300,325)),'a-hinh-10-18':(332,(310,427,576,615))}
for name,want in expected.items():
 page,box=values['CROPS'][name];assert(page,box)==want
 pix=pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(values['SCALE'],values['SCALE']),clip=pymupdf.Rect(box),alpha=False)
 p=ROOT/'docs/vat-ly-1/bai-giang/img/young-10'/(name+'.png')
 im=Image.open(p).convert('RGB')
 assert im.size==(pix.width,pix.height)and im.tobytes()==pix.samples,name
 print('PASS exact originalPDF raster',name,hashlib.sha256(p.read_bytes()).hexdigest())
print('Scope: Two original rasters only. Complete framing visually reviewed separately; no wholecourse proof.')
