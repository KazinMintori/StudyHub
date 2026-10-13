"""Reproduce complete chapter 29 exercise illustrations with unclipped labels."""
from pathlib import Path
import pymupdf
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-29'
# Printed page and PDF-point rectangle. Caption text is written in Vietnamese
# in the exercise statement, so only the diagram itself is extracted.
FIGURES={
 'hinh-e29-7':(980,(180,604,300,745)),
 'hinh-e29-8':(980,(474,76,575,143)),
 'hinh-e29-12':(980,(486,406,573,450)),
 'hinh-e29-14':(980,(487,550,574,633)),
 'hinh-e29-15':(980,(470,664,574,744)),
 'hinh-e29-16':(981,(125,147,306,269)),
 'hinh-e29-17':(981,(241,296,335,389)),
 'hinh-e29-18':(981,(164,430,242,496)),
 'hinh-e29-19':(981,(137,577,288,653)),
 'hinh-e29-20':(981,(423,60,542,153)),
 'hinh-e29-21':(981,(506,173,614,245)),
 'hinh-e29-22':(981,(522,271,615,360)),
 'hinh-e29-24':(981,(372,549,583,608)),
 'hinh-e29-25':(981,(519,642,614,698)),
 'hinh-e29-26':(982,(184,75,299,161)),
 'hinh-e29-27':(982,(34,321,298,395)),
 'hinh-e29-28':(982,(190,419,297,477)),
 'hinh-e29-29':(982,(175,551,299,611)),
 'hinh-e29-31':(982,(313,155,574,216)),
 'hinh-e29-32':(982,(313,398,574,455)),
 'hinh-e29-33':(982,(313,570,574,636)),
 'hinh-p29-44':(983,(354,381,585,433)),
 'hinh-p29-45':(983,(495,470,614,550)),
 'hinh-p29-48':(984,(181,154,297,233)),
 'hinh-p29-49':(984,(177,260,298,373)),
 'hinh-p29-51':(984,(165,569,298,650)),
 'hinh-p29-53':(984,(445,78,574,158)),
 'hinh-p29-54':(984,(450,187,575,279)),
 'hinh-p29-55':(984,(334,423,575,539)),
 'hinh-p29-56':(984,(475,570,575,657)),
 'hinh-p29-59':(985,(215,243,335,315)),
 'hinh-p29-60':(985,(84,541,285,618)),
 'hinh-p29-61':(985,(240,640,335,738)),
 'hinh-p29-62':(985,(506,79,615,158)),
 'hinh-p29-64':(985,(353,466,616,557)),
 'hinh-p29-65':(985,(502,585,615,648)),
 'hinh-p29-66':(986,(109,256,216,323)),
 'hinh-p29-67':(986,(170,490,298,624)),
 'hinh-p29-68':(986,(482,75,580,208)),
 'hinh-p29-69':(986,(340,452,585,553)),
 'hinh-p29-73':(987,(354,195,620,270)),
 'hinh-p29-74':(987,(354,344,620,506)),
 'mcat29-tms':(987,(85,319,340,430)),
}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 pdf=pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')
 for name,(printed,box) in FIGURES.items():
  pdf[printed+19].get_pixmap(matrix=pymupdf.Matrix(2.5,2.5),clip=pymupdf.Rect(box),alpha=False).save(OUT/f'{name}.png')
  path=OUT/f'{name}.png';image=Image.open(path).convert('RGB')
  bounds=ImageChops.difference(image,Image.new('RGB',image.size,'white')).getbbox()
  if bounds:
   left,top,right,bottom=bounds
   image.crop((max(0,left-12),max(0,top-12),min(image.width,right+12),min(image.height,bottom+12))).save(path,optimize=True)
 print('Prepared',len(FIGURES),'chapter 29 end-of-chapter images.')
if __name__=='__main__':main()
