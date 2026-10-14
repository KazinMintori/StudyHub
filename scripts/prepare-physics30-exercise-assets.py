"""Render complete diagrams for the end-of-chapter inductance problems."""
from pathlib import Path
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-30'
CROPS={
 'hinh-q30-10':(1031,(223,541,337,587)),
 'hinh-e30-09':(1032,(216,245,293,279)),
 'hinh-p30-50':(1034,(175,514,296,584)),
 'hinh-p30-51':(1034,(325,214,527,306)),
 'hinh-p30-52':(1034,(461,329,575,398)),
 'hinh-p30-57':(1035,(226,208,338,281)),
 'hinh-p30-58':(1035,(222,305,343,416)),
 'hinh-p30-60':(1035,(117,689,287,748)),
 'hinh-p30-61':(1035,(505,78,619,163)),
 'hinh-p30-63':(1035,(522,322,619,398)),
 'hinh-p30-65':(1035,(423,626,598,712)),
 'hinh-p30-66':(1036,(110,162,220,236)),
 'hinh-p30-67':(1036,(107,485,272,570)),
 'hinh-p30-68':(1036,(349,77,522,164)),
 'hinh-p30-69':(1036,(353,370,536,457)),
 'hinh-p30-70':(1036,(457,485,572,553)),
 'hinh-p30-71':(1037,(234,77,338,177)),
}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for name,(page,rect) in CROPS.items():
   pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(rect),alpha=False).save(OUT/f'{name}.png')
 print('Rendered seventeen end-of-chapter diagrams with their labels and arrows.')
if __name__=='__main__':main()
