"""Extract unchanged original chapter13 exercise figures with complete frames."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-13'
SCALE=2.5
CROPS={'r-exercises-fig-e13-5': (442, (178, 676, 294, 742)), 'r-exercises-fig-e13-6': (442, (330, 105, 553, 185)), 'r-exercises-fig-e13-38': (444, (63, 199, 266, 237)), 'r-exercises-fig-e13-39': (444, (180, 267, 303, 338)), 'r-exercises-fig-p13-45': (444, (455, 305, 596, 395)), 'r-exercises-fig-p13-58': (445, (365, 123, 614, 187)), 'r-exercises-fig-p13-79': (447, (490, 173, 615, 303)), 'r-exercises-fig-p13-81': (447, (500, 600, 618, 698))}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(PDF)as document:
  for key,(page,rectangle)in CROPS.items():
   document[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rectangle),alpha=False).save(str(OUT/(key+'.png')))
 print('Saved',len(CROPS),'original chapter13 exercise figures.')
if __name__=='__main__':main()
