"""Exact, unchanged PDF crops for the parent-owned chapter 40 sections."""
from pathlib import Path
import json, hashlib
import pymupdf as fitz
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'mo-dau-cham-luong-tu':(1341,(0,0,439,242)),
 'ung-dung-polyacetylene':(1353,(456,253,615,486)),
 'hinh-40-18':(1360,(46,429,180,525)),
 'hinh-40-19':(1360,(52,668,175,744)),
 'hinh-40-20':(1361,(126,86,395,207)),
 'hinh-40-21':(1362,(232,59,551,208)),
 'hinh-40-22':(1362,(35,541,193,733)),
 'ung-dung-enzyme':(1362,(0,328,195,466)),
 'hinh-40-23':(1363,(469,347,606,459)),
 'hinh-40-24':(1364,(36,209,195,334)),
 'hinh-40-25':(1364,(38,629,184,737)),
 'cong-thuc-40-46':(1364,(210,531,570,602)),
 'hinh-40-28':(1366,(35,487,194,598)),
 'hinh-40-29':(1367,(456,267,614,419)),
 'hinh-40-30':(1369,(454,181,618,391)),
 'tom-tat-ham-song':(1370,(445,482,603,600)),
 'tom-tat-hat-trong-hop':(1371,(496,84,595,151)),
 'tom-tat-chuan-hoa':(1371,(505,198,595,265)),
 'tom-tat-gieng-huu-han':(1371,(494,289,620,377)),
 'tom-tat-xuyen-ham':(1371,(493,392,609,453)),
 'tom-tat-dao-dong':(1371,(501,463,600,545)),
}
for n,(left,right) in enumerate([(80,195),(201,323),(323,450),(448,573)]):
 CROPS[f'hinh-40-26-n{n}']=(1366,(left,106,right,219))
 CROPS[f'hinh-40-27-n{n}']=(1366,(left,284,right,354))
SCALE=3
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-40'

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 qa=ROOT/'qa/physics/chapter40';qa.mkdir(parents=True,exist_ok=True)
 rows=[];thumbs=[]
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,clip) in CROPS.items():
   pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(clip),alpha=False)
   destination=OUT/(stem+'.png');pix.save(destination)
   with Image.open(destination) as image:
    assert image.convert('RGB').tobytes()==pix.samples
    thumb=image.convert('RGB');thumb.thumbnail((290,210))
   panel=Image.new('RGB',(310,240),'white');panel.paste(thumb,(8,25))
   ImageDraw.Draw(panel).text((8,7),stem,fill='black');thumbs.append(panel)
   rows.append(dict(stem=stem,pdfPage=page,clip=clip,scale=SCALE,pixelMatch=True,sha256=hashlib.sha256(destination.read_bytes()).hexdigest()))
 contact=Image.new('RGB',(310*4,240*((len(thumbs)+3)//4)),(225,225,225))
 for i,panel in enumerate(thumbs):contact.paste(panel,((i%4)*310,(i//4)*240))
 contact.save(qa/'parent-crops-contact.png')
 (qa/'parent-image-ledger.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
 print(f'Extracted {len(rows)} unchanged source crops; every PNG matches fresh PDF pixels.')
if __name__=='__main__':main()
