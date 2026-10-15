"""Exact unchanged rectangles for applications, quiz and summary artwork."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-34';out.mkdir(parents=True,exist_ok=True)
CROPS={
 'hinh-34-41-d':(1156,(35,240,195,512)),
 'ung-dung-34-chao-thu':(1137,(455,214,615,497)),
 'tu-kiem-34-4-de':(1155,(455,60,615,180)),
 'tu-kiem-34-4-dap-an':(1155,(150,105,370,250)),
 'ung-dung-34-tac-ke':(1162,(0,328,192,471)),
 'tong-ket-34-phan-xa-phang':(1168,(440,88,555,149)),
 'tong-ket-34-phong-dai':(1168,(440,164,555,231)),
 'tong-ket-34-tieu-diem':(1168,(440,246,555,346)),
 'tong-ket-34-tia-chinh':(1168,(440,365,565,427)),
 'tong-ket-34-thau-kinh':(1168,(440,548,565,602)),
 'tong-ket-34-may-anh':(1169,(460,60,590,149)),
 'tong-ket-34-mat':(1169,(463,160,575,230)),
 'tong-ket-34-kinh-lup':(1169,(463,242,580,320)),
 'tong-ket-34-kinh-hien-vi':(1169,(463,334,585,403)),
}
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,box) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(box),alpha=False)
  p=out/(stem+'.png');pix.save(p)
  with Image.open(p) as im:assert im.convert('RGB').tobytes()==pix.samples
  rows.append({'path':p.relative_to(root).as_posix(),'pdfPage':page,'box':box,'scale':3,'pixelMatch':True,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
q=root/'qa/physics/chapter34';q.mkdir(parents=True,exist_ok=True)
(q/'supplement-image-source-ledger.json').write_text(json.dumps({'status':'pixel-match-visual-review-pending','images':rows},indent=2),encoding='utf-8')
sheet=Image.new('RGB',(1500,2000),'#eee');draw=ImageDraw.Draw(sheet)
for i,row in enumerate(rows):
 p=root/row['path'];im=Image.open(p).convert('RGB');im.thumbnail((480,360));x=(i%3)*500;y=(i//3)*400
 sheet.paste(im,(x+(500-im.width)//2,y+30));draw.text((x+5,y+5),p.stem,fill='black')
sheet.save(q/'supplement-contact.png')
print('Extracted14unchanged supplementary source regions; inspect visual boundaries.')
