"""Reproducible exact PDF crops for chapter7 end exercises, including all panels."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-07'
SCALE=2.5
CROPS={'r-exercises-fig-7-25': (246, (185, 105, 290, 220)), 'r-exercises-fig-e7-09': (248, (180, 327, 295, 395)), 'r-exercises-fig-e7-36': (249, (490, 308, 615, 395)), 'r-exercises-fig-p7-37': (249, (485, 450, 615, 560)), 'r-exercises-fig-p7-39': (250, (34, 155, 265, 240)), 'r-exercises-fig-p7-40': (250, (34, 365, 275, 450)), 'r-exercises-fig-p7-41': (250, (34, 545, 275, 655)), 'r-exercises-fig-p7-43': (250, (455, 75, 580, 120)), 'r-exercises-fig-p7-45': (250, (455, 230, 575, 305)), 'r-exercises-fig-p7-46': (250, (450, 395, 575, 470)), 'r-exercises-fig-p7-50': (251, (215, 75, 340, 195)), 'r-exercises-fig-p7-51': (251, (225, 230, 340, 360)), 'r-exercises-fig-p7-55': (251, (215, 605, 340, 735)), 'r-exercises-fig-p7-57': (251, (350, 318, 570, 400)), 'r-exercises-fig-p7-58': (251, (350, 528, 605, 615)), 'r-exercises-fig-p7-60': (252, (34, 118, 280, 220)), 'r-exercises-fig-p7-69': (252, (310, 298, 565, 410)), 'r-exercises-fig-p7-76': (253, (215, 274, 335, 355)), 'r-exercises-fig-p7-79': (253, (366, 528, 586, 696)), 'r-exercises-fig-p7-82': (254, (310, 238, 520, 345)), 'r-exercises-fig-p7-84': (254, (310, 455, 560, 525)), 'r-exercises-fig-dna-apparatus': (254, (40, 482, 290, 555)), 'r-exercises-bridge-force-diagrams': (246, (65, 416, 268, 539))}

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(SOURCE)as doc:
  for name,(page,box)in CROPS.items():
   doc[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(box),alpha=False).save(str(OUT/(name+'.png')))
 print('Saved',len(CROPS),'exact original exercise crops.')
if __name__=='__main__':main()
