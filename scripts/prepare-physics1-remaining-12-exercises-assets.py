"""Extract complete original chapter12 end-exercise figures without changing pixels."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-12'
SCALE=2.5
CROPS={'r-exercises-fig-12-32': (406, (336, 601, 546, 716.1)), 'r-exercises-fig-q12-30': (408, (178, 232, 295, 355)), 'r-exercises-fig-e12-15': (408, (497, 473, 572, 612)), 'r-exercises-fig-e12-19': (409, (217, 135, 334, 300)), 'r-exercises-fig-e12-33': (409, (508, 258, 615, 350)), 'r-exercises-fig-p12-57': (410, (458, 497, 573, 565)), 'r-exercises-fig-p12-62': (411, (227, 311, 329, 423)), 'r-exercises-fig-p12-63': (411, (218, 477, 333, 585)), 'r-exercises-fig-p12-67': (411, (501, 223, 614, 274.5)), 'r-exercises-fig-p12-72': (411, (507, 585, 614, 723)), 'r-exercises-fig-p12-77': (412, (164, 421, 295, 506)), 'r-exercises-fig-p12-81': (412, (361, 162, 522, 282)), 'r-exercises-fig-p12-83': (412, (353, 522, 514, 630)), 'r-exercises-fig-p12-86': (413, (130, 323, 281, 447)), 'r-exercises-fig-p12-88': (413, (424, 224, 538, 317)), 'r-exercises-mcat-elephant': (413, (423, 500, 540, 610))}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(PDF)as document:
  for key,(page,rectangle)in CROPS.items():
   document[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rectangle),alpha=False).save(str(OUT/(key+'.png')))
 print('Saved',len(CROPS),'complete original exercise figures.')
if __name__=='__main__':main()
