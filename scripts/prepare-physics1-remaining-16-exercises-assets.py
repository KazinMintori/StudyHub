"""Extract unchanged original chapter16 end-material figures with reviewed frames."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-16'
SCALE=2.5
CROPS={'r-exercises-e16-7': (555, (500, 94.5, 616, 198)), 'r-exercises-e16-32': (556, (310, 456, 566, 525)), 'r-exercises-e16-33': (556, (310, 643, 553, 742)), 'r-exercises-e16-37': (557, (233, 283, 340, 353)), 'r-exercises-e16-43': (557, (350, 107, 612, 166)), 'r-exercises-p16-58': (558, (174, 570, 296, 627)), 'r-exercises-p16-61': (558, (455, 108, 594, 215)), 'r-exercises-p16-75': (559, (380, 692, 554, 748)), 'r-exercises-figure-16-39': (553, (352, 569, 614, 644)), 'r-exercises-figure-q16-25': (555, (223, 60, 339, 179))}
def main():
 OUT.mkdir(exist_ok=True)
 with pymupdf.open(PDF)as doc:
  for name,(page,rect)in CROPS.items():
   doc[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rect),alpha=False).save(str(OUT/(name+'.png')))
 print('Saved',len(CROPS),'unchanged source figures with accepted frames.')
if __name__=='__main__':main()
