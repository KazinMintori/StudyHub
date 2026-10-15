"""Nine unchanged source exercise figure regions for chapter35."""
from pathlib import Path
import json
import pymupdf as fitz
from PIL import Image
root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-35';out.mkdir(parents=True,exist_ok=True)
CROPS={
 'hinh-e35-03':(1199,(515,400,615,514)),
 'hinh-e35-29':(1201,(99,303,312,390)),
 'hinh-p35-41':(1202,(185,245,295,325)),
 'hinh-p35-42':(1202,(193,377,295,465)),
 'hinh-p35-48':(1202,(310,514,550,673)),
 'hinh-p35-50':(1203,(77,200,325,336)),
 'hinh-p35-53':(1203,(353,62,555,140)),
 'hinh-p35-54':(1203,(353,431,565,575)),
 'hinh-p35-56':(1204,(35,162,285,294)),
}
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,box) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(box),alpha=False);p=out/(stem+'.png');pix.save(p)
  assert Image.open(p).convert('RGB').tobytes()==pix.samples
  rows.append({'path':p.relative_to(root).as_posix(),'pdfPage':page,'box':box,'scale':3,'pixelMatch':True})
q=root/'qa/physics/chapter35';(q/'exercise-image-source-ledger.json').write_text(json.dumps({'status':'partial-inventory-pixel-match-visual-review-pending','expectedExerciseFigures':9,'images':rows},indent=2),encoding='utf-8')
print('Extracted',len(rows),'of nine original exercise figures.')
