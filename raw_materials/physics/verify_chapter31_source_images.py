"""Read-only comparison of all48 extracted source images against PDF pixels."""
from pathlib import Path
import ast,json,hashlib
import pymupdf as fitz
from PIL import Image
ROOT=Path(__file__).resolve().parents[2]
files=['prepare-physics31-theory-a-assets.py','prepare-physics31-theory-b-assets.py','prepare-physics31-exercise-assets.py']
crops={}
for name in files:
 tree=ast.parse((ROOT/'scripts'/name).read_text(encoding='utf-8-sig'))
 value=next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CROPS' for t in n.targets))
 data=ast.literal_eval(value)
 assert not set(crops).intersection(data)
 crops.update(data)
assert len(crops)==48
records=[]
source=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
with fitz.open(source) as pdf:
 for stem,(page,rect) in crops.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(rect),alpha=False)
  path=ROOT/'docs/vat-ly-2/bai-giang/img/young-31'/(stem+'.png')
  with Image.open(path) as im:
   assert im.size==(pix.width,pix.height),stem
   assert im.convert('RGB').tobytes()==pix.samples,stem
  records.append({'file':path.relative_to(ROOT).as_posix(),'pdfPage':page,'clipPoints':rect,
                  'scale':3,'unchangedSourcePixels':True,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
out=ROOT/'qa/physics/chapter31/source-image-integrity.json'
out.write_text(json.dumps({'status':'passed','images':48,'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                          'records':records},indent=2)+'\n',encoding='utf8')
print('All48 source images exactly match the selected PDF rendering pixels.')
