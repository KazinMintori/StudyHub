"""Unchanged chapter35 opening, application and summary source regions."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-35';out.mkdir(parents=True,exist_ok=True)
CROPS={
 'mo-dau-35':(1179,(0,0,439,246)),
 'ung-dung-35-thinh-giac':(1182,(0,580,192,741)),
 'ung-dung-35-canh-buom':(1195,(456,239,648,404)),
 'ung-dung-35-oct':(1196,(35,274,192,377)),
 'tong-ket-35-nguon-ket-hop':(1197,(494,92,582,171)),
 'tong-ket-35-hai-nguon':(1197,(494,193,590,256)),
 'tong-ket-35-gian-do-pha':(1197,(494,350,582,443)),
 'tong-ket-35-mang-mong':(1197,(494,461,590,531)),
 'tong-ket-35-michelson':(1197,(494,631,615,729)),
}
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,box) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(box),alpha=False)
  path=out/(stem+'.png');pix.save(path)
  with Image.open(path) as im:assert im.convert('RGB').tobytes()==pix.samples
  rows.append({'path':path.relative_to(root).as_posix(),'pdfPage':page,'box':box,'scale':3,'pixelMatch':True,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
q=root/'qa/physics/chapter35';q.mkdir(parents=True,exist_ok=True)
(q/'parent-image-source-ledger.json').write_text(json.dumps({'status':'pixel-match-visual-review-pending','images':rows},indent=2),encoding='utf-8')
sheet=Image.new('RGB',(1500,1200),'#eee');draw=ImageDraw.Draw(sheet)
for i,row in enumerate(rows):
 p=root/row['path'];im=Image.open(p).convert('RGB');im.thumbnail((480,360));x=(i%3)*500;y=(i//3)*400
 sheet.paste(im,(x+(500-im.width)//2,y+30));draw.text((x+5,y+5),p.stem,fill='black')
sheet.save(q/'parent-contact.png')
print('Extracted nine unchanged source regions. Review all crop edges.')
