from pathlib import Path
import pymupdf
from PIL import Image,ImageDraw

root=Path(__file__).resolve().parents[1]
doc=pymupdf.open(root/'raw_materials/physics/source/young-freedman-15.pdf')
out=root/'docs/vat-ly-2/bai-giang/img/young-22';out.mkdir(parents=True,exist_ok=True)
figures={
 'mo-chuong':(718,(210,0,648,245)),
 'hinh-22-1':(719,(455,88,615,393)),
 'hinh-22-2':(719,(77,586,575,744)),
 'hinh-22-3':(720,(209,100,575,245)),
 'hinh-22-4':(720,(35,246,195,744)),
 'hinh-22-5':(721,(455,455,615,674)),
 'hinh-22-6':(722,(35,225,195,744)),
 'hinh-22-7':(723,(77,660,270,740)),
 'hinh-22-8':(724,(354,143,615,237)),
 'hinh-22-9':(724,(354,509,615,601)),
 'hinh-22-10':(725,(210,589,310,744)),
 'hinh-22-11':(726,(35,144,195,317)),
 'hinh-22-12':(726,(210,560,570,744)),
 'hinh-22-13':(727,(455,230,615,386)),
 'hinh-22-14':(728,(35,120,195,385)),
 'hinh-22-15':(728,(77,596,298,738)),
 'hinh-22-16':(729,(455,90,615,208)),
 'hinh-22-17':(729,(455,374,615,494)),
 'hinh-22-18':(730,(340,297,615,486)),
 'hinh-22-19':(731,(77,322,335,436)),
 'hinh-22-20':(731,(405,507,565,626)),
 'hinh-22-21':(732,(77,350,615,553)),
 'hinh-22-22':(733,(354,102,615,268)),
 'hinh-22-23':(734,(77,388,570,505)),
 'hinh-22-24':(734,(370,614,510,734)),
 'hinh-22-25':(735,(77,117,615,277)),
 'hinh-22-26':(735,(455,477,615,744)),
 'hinh-22-27':(736,(210,130,615,275)),
 'hinh-22-28':(736,(35,269,195,373)),
 'hinh-22-29':(740,(35,78,280,191)),
 'ung-dung-ca-nham':(723,(455,281,648,450)),
 'ung-dung-neuron':(734,(35,246,192,355)),
 'ung-dung-set':(736,(0,600,192,744)),
 'hinh-e22-2':(741,(136,613,280,670)),
 'hinh-e22-6':(741,(413,285,553,384)),
 'hinh-e22-8':(741,(422,551,615,639)),
 'hinh-e22-28':(742,(390,645,489,741)),
 'hinh-p22-31':(743,(250,216,337,314)),
 'hinh-p22-33':(743,(155,505,260,625)),
 'hinh-p22-42':(743,(553,629,615,674)),
 'hinh-p22-43':(744,(223,80,297,153)),
 'hinh-p22-53':(744,(507,610,574,684)),
 'hinh-p22-54':(745,(255,80,337,159)),
 'hinh-p22-56':(745,(170,501,283,614)),
 'hinh-p22-57':(745,(212,634,337,744)),
 'tom-tat-dien-thong':(738,(450,92,570,193)),
 'tom-tat-gauss':(738,(450,217,570,346))
}
for name,(p,clip) in figures.items():
 doc[p+19].get_pixmap(matrix=pymupdf.Matrix(2,2),clip=pymupdf.Rect(clip)).save(out/(name+'.png'))
qa=root/'qa/physics/chapter22';qa.mkdir(parents=True,exist_ok=True)
files=sorted(out.glob('*.png'))
for n in range((len(files)+19)//20):
 sheet=Image.new('RGB',(1400,1100),'white');d=ImageDraw.Draw(sheet)
 for i,p in enumerate(files[n*20:(n+1)*20]):
  x=i%5*280;y=i//5*275
  im=Image.open(p).convert('RGB');im.thumbnail((268,238));sheet.paste(im,(x+(280-im.width)//2,y+22));d.text((x+5,y+3),p.stem,fill='black')
 sheet.save(qa/f'asset-contact-{n}.jpg')
print('Prepared',len(figures),'chapter22 assets for visual review.')
