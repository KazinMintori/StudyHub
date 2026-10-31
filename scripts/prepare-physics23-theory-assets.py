from pathlib import Path
import pymupdf
from PIL import Image,ImageDraw

root=Path(__file__).resolve().parents[1]
doc=pymupdf.open(root/'raw_materials/physics/source/young-freedman-15.pdf')
out=root/'docs/vat-ly-2/bai-giang/img/young-23';out.mkdir(parents=True,exist_ok=True)
figures={
 'mo-chuong':(747,(0,0,438,245)),
 'hinh-23-1':(748,(35,219,195,366)),
 'hinh-23-2':(748,(35,433,195,590)),
 'hinh-23-3':(749,(77,84,403,276)),
 'hinh-23-4':(749,(455,102,623,467)),
 'hinh-23-5':(749,(455,570,615,744)),
 'hinh-23-6':(750,(35,109,195,291)),
 'hinh-23-7':(750,(35,462,195,745)),
 'hinh-23-8':(752,(35,115,195,240)),
 'hinh-23-9':(752,(35,363,192,520)),
 'hinh-23-10':(753,(405,319,565,359)),
 'hinh-23-11':(754,(35,547,195,678)),
 'hinh-23-12':(756,(35,281,195,550)),
 'hinh-23-13':(758,(370,106,540,260)),
 'hinh-23-14':(759,(395,111,575,254)),
 'hinh-23-15':(759,(400,450,566,510)),
 'hinh-23-16':(761,(183,290,495,426)),
 'hinh-23-17':(762,(35,109,192,243)),
 'hinh-23-18':(762,(365,341,515,455)),
 'hinh-23-19':(763,(354,109,615,239)),
 'hinh-23-20':(763,(427,495,535,589)),
 'hinh-23-21':(764,(380,102,510,263)),
 'hinh-23-22':(765,(149,64,368,221)),
 'hinh-23-23':(765,(77,564,575,744)),
 'hinh-23-24':(766,(35,109,195,313)),
 'hinh-23-25':(766,(35,409,195,540)),
 'hinh-23-26':(766,(35,630,195,748)),
 'ung-dung-dien-tam-do':(755,(455,185,615,291)),
 'ung-dung-xa-tri':(757,(455,207,648,348)),
 'ung-dung-mang-te-bao':(768,(35,207,192,317))
}
for name,(p,clip) in figures.items():
 doc[p+19].get_pixmap(matrix=pymupdf.Matrix(2,2),clip=pymupdf.Rect(clip)).save(out/(name+'.png'))
qa=root/'qa/physics/chapter23';qa.mkdir(parents=True,exist_ok=True)
files=sorted(out.glob('*.png'))
for n in range((len(files)+19)//20):
 sheet=Image.new('RGB',(1400,1100),'white');d=ImageDraw.Draw(sheet)
 for i,p in enumerate(files[n*20:(n+1)*20]):
  x=i%5*280;y=i//5*275;im=Image.open(p).convert('RGB');im.thumbnail((268,238));sheet.paste(im,(x+(280-im.width)//2,y+22));d.text((x+5,y+3),p.stem,fill='black')
 sheet.save(qa/f'asset-contact-{n}.jpg')
print('Prepared',len(figures),'chapter23 theory figures for visual review.')
