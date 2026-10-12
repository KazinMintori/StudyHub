from pathlib import Path
import pymupdf
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
doc=pymupdf.open(root/'raw_materials/physics/source/young-freedman-15.pdf')
out=root/'docs/vat-ly-2/bai-giang/img/young-24';out.mkdir(parents=True,exist_ok=True)
figures={
 'mo-chuong':(781,(0,0,437,245)),
 'hinh-24-1':(782,(35,120,195,290)),
 'ky-hieu-tu':(782,(345,211,435,238)),
 'hinh-24-2':(783,(455,107,615,346)),
 'hinh-24-3':(783,(455,564,648,706)),
 'hinh-24-4':(784,(35,109,193,224)),
 'hinh-24-5':(785,(95,312,303,440)),
 'hinh-24-6':(785,(405,529,565,646)),
 'hinh-24-7':(786,(35,257,193,374)),
 'hinh-24-8':(786,(35,466,195,744)),
 'hinh-24-9':(787,(455,504,615,744)),
 'hinh-24-10':(789,(77,464,615,573)),
 'hinh-24-11':(791,(455,198,615,336)),
 'hinh-24-12':(792,(312,132,562,195)),
 'hinh-24-13':(793,(455,610,615,744)),
 'hinh-24-14':(794,(35,125,195,467)),
 'hinh-24-15':(795,(455,236,615,443)),
 'hinh-24-16':(798,(312,100,563,211)),
 'hinh-24-17':(799,(455,150,615,403)),
 'hinh-24-18':(799,(455,445,615,745)),
 'hinh-24-19':(799,(188,548,378,740)),
 'hinh-24-20':(800,(230,97,544,307)),
 'hinh-24-21':(800,(35,560,195,730)),
 'hinh-24-22':(801,(455,163,615,413)),
 'ung-dung-man-hinh':(787,(455,268,612,373)),
 'ung-dung-do-tuong':(795,(455,624,612,729)),
 'ung-dung-mang-te-bao':(798,(35,561,192,729)),
 'ung-dung-dien-thoai':(800,(0,187,192,306))
}
for name,(page,clip) in figures.items():
 doc[page+19].get_pixmap(matrix=pymupdf.Matrix(2,2),clip=pymupdf.Rect(clip)).save(out/(name+'.png'))
qa=root/'qa/physics/chapter24'
files=sorted(out.glob('*.png'))
for start in range(0,len(files),16):
 sheet=Image.new('RGB',(1120,1080),'white');d=ImageDraw.Draw(sheet)
 for i,f in enumerate(files[start:start+16]):
  im=Image.open(f).convert('RGB');im.thumbnail((264,235));x=i%4*280;y=i//4*270
  sheet.paste(im,(x+(280-im.width)//2,y+25));d.text((x+5,y+4),f.stem,fill='black')
 sheet.save(qa/f'asset-contact-{start//16}.jpg')
print('Prepared',len(figures),'chapter24 theory figures; inspect every crop before integration.')
