from pathlib import Path
import pymupdf
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parents[1]
doc=pymupdf.open(root/'raw_materials/physics/source/young-freedman-15.pdf')
out=root/'docs/vat-ly-2/bai-giang/img/young-25';out.mkdir(parents=True,exist_ok=True)
figures={
 'mo-chuong':(812,(220,0,648,245)),
 'hinh-25-01':(813,(456,315,612,580)),
 'hinh-25-02':(814,(35,112,195,410)),
 'hinh-25-03':(814,(35,519,195,750)),
 'hinh-25-04':(815,(455,590,648,741)),
 'hinh-25-05':(817,(455,465,615,642)),
 'hinh-25-06':(818,(35,136,195,425)),
 'anh-mang-myelin':(818,(0,593,192,741)),
 'hinh-25-07':(819,(456,356,612,476)),
 'hinh-25-08':(820,(0,246,192,388)),
 'hinh-25-09':(820,(35,470,195,537)),
 'hinh-25-10':(821,(95,85,420,240)),
 'hinh-25-11':(822,(35,238,195,502)),
 'hinh-25-12':(822,(0,585,192,741)),
 'hinh-25-13':(823,(456,244,612,430)),
 'hinh-25-14':(823,(456,534,615,750)),
 'hinh-25-15':(824,(35,544,195,703)),
 'anh-ca-duoi-dien':(824,(10,247,192,349)),
 'hinh-25-16':(825,(85,561,274,633)),
 'hinh-25-17':(826,(36,76,230,180)),
 'hinh-25-18':(826,(312,347,567,441)),
 'hinh-25-19':(826,(312,642,568,760)),
 'hinh-25-20':(827,(456,270,612,455)),
 'hinh-25-21':(828,(72,120,175,178)),
 'hinh-25-22':(829,(455,168,615,530)),
 'hinh-25-23':(829,(455,590,615,750)),
 'hinh-25-24':(830,(312,520,572,640)),
 'hinh-25-25':(831,(82,622,282,756)),
 'hinh-25-26':(832,(35,317,195,555)),
 'hinh-25-27':(832,(35,653,195,743)),
 'hinh-e25-26':(839,(144,360,260,422)),
 'hinh-e25-27':(839,(236,453,329,516)),
 'hinh-e25-28':(839,(160,580,273,655)),
 'hinh-e25-29':(839,(242,683,326,760)),
 'hinh-e25-30':(839,(385,140,542,220)),
 'hinh-p25-59':(841,(280,375,342,449)),
 'hinh-p25-62':(841,(215,646,335,720)),
 'hinh-p25-69':(841,(468,610,615,676)),
 'hinh-p25-70':(842,(175,164,298,206)),
 'hinh-p25-71':(842,(178,274,296,316)),
 'hinh-p25-72':(842,(103,441,276,532)),
 'tom-tat-dong-dien':(835,(495,98,607,160)),
 'tom-tat-dien-tro-suat':(835,(492,214,602,310)),
 'tom-tat-dien-tro':(835,(493,329,602,400)),
 'tom-tat-suat-dien-dong':(835,(494,430,609,505)),
 'tom-tat-cong-suat':(835,(493,527,594,580)),
 'tom-tat-dan-dien':(835,(494,623,578,662)),
 'hinh-q25-12':(837,(80,659,330,749)),
 'hinh-q25-14':(837,(386,263,578,334)),
 'hinh-q25-15':(837,(389,458,575,535)),
 'hinh-q25-16':(837,(386,625,578,710))
 ,'hinh-e25-47':(840,(208,572,297,631))
 ,'hinh-p25-54':(840,(473,631,567,723))
}
for name,(page,clip) in figures.items():
 doc[page+19].get_pixmap(matrix=pymupdf.Matrix(2,2),clip=pymupdf.Rect(clip)).save(out/(name+'.png'))
qa=root/'qa/physics/chapter25';qa.mkdir(parents=True,exist_ok=True)
files=sorted(out.glob('*.png'))
for start in range(0,len(files),16):
 sheet=Image.new('RGB',(1120,1100),'white');d=ImageDraw.Draw(sheet)
 for i,f in enumerate(files[start:start+16]):
  im=Image.open(f).convert('RGB');im.thumbnail((264,235));x=i%4*280;y=i//4*275
  sheet.paste(im,(x+(280-im.width)//2,y+25));d.text((x+5,y+4),f.stem,fill='black')
 sheet.save(qa/f'asset-contact-{start//16}.jpg')
print('Prepared',len(figures),'chapter25 figures; inspect each crop before integration.')
