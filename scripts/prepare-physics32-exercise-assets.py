"""Extract unchanged end-of-chapter artwork from the original PDF."""
from pathlib import Path
import hashlib,json
import pymupdf as fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-32'
CROPS={
 'hinh-bridge32-01':(1090,(310,585,576,744)),
 'hinh-p32-37':(1093,(495,416,615,480)),
 'hinh-p32-42':(1094,(190,125,302,270)),
 'hinh-p32-47':(1094,(310,394,573,501)),
 'hinh-p32-48':(1094,(452,503,617,570)),
 'hinh-p32-50':(1095,(77,464,299,587)),
}
OUT.mkdir(parents=True,exist_ok=True);rows=[]
with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,box) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(box),alpha=False)
  p=OUT/(stem+'.png');pix.save(p)
  with Image.open(p) as im:
   assert im.size==(pix.width,pix.height) and im.convert('RGB').tobytes()==pix.samples
  rows.append({'file':stem+'.png','pdfPage':page,'clipPoints':box,'scale':3,'unchangedSourcePixels':True,
               'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
q=ROOT/'qa/physics/chapter32';q.mkdir(parents=True,exist_ok=True)
(q/'exercise-image-source-ledger.json').write_text(json.dumps({'status':'passed','images':rows},indent=2),encoding='utf8')
sheet=Image.new('RGB',(1200,1260),'#ddd');draw=ImageDraw.Draw(sheet)
for index,stem in enumerate(CROPS):
 with Image.open(OUT/(stem+'.png')) as im:
  im.thumbnail((550,370));x=(index%2)*600;y=(index//2)*420
  sheet.paste(im,(x+10,y+25));draw.text((x+10,y+5),stem,fill='black')
sheet.save(q/'exercise-crops-review.png')
print('Extracted six source diagrams with verified unchanged pixels.')
