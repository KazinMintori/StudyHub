"""Extract original chapter15 exercise images without changing their content."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-15'
SCALE=2.5
CROPS={'r-exercises-e15-11': (514, (452, 198, 612, 286)), 'r-exercises-e15-28': (515, (484, 332, 615, 414)), 'r-exercises-e15-29': (515, (484, 431, 615, 506)), 'r-exercises-e15-30': (515, (350, 604, 615, 700)), 'r-exercises-e15-32': (516, (32, 136, 272, 254)), 'r-exercises-e15-43': (516, (456, 383, 583, 514)), 'r-exercises-p15-52': (517, (232, 629, 340, 765)), 'r-exercises-p15-53': (517, (489, 139, 613, 226)), 'r-exercises-p15-62': (518, (35, 317, 288, 409)), 'r-exercises-p15-75': (519, (100, 530, 310, 646)), 'r-exercises-p15-77': (519, (506, 254, 614, 407)), 'r-exercises-p15-79': (519, (499, 559, 615, 677)), 'r-exercises-p15-80': (520, (333, 78, 554, 179))}
def main():
 OUT.mkdir(exist_ok=True)
 with pymupdf.open(PDF)as doc:
  for name,(page,rectangle)in CROPS.items():
   doc[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rectangle),alpha=False).save(str(OUT/(name+'.png')))
 print('Saved',len(CROPS),'unchanged original exercise figures.')
if __name__=='__main__':main()
