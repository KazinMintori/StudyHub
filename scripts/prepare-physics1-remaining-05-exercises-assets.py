"""Reproduce the unchanged source figures for chapter5 guided material."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-05'
CROPS={'r-exercises-guided-media-qr': (177, (302, 201, 615, 245), 2.5), 'r-exercises-bridge-fig-5-39': (178, (35, 290, 256, 446), 2.5), 'r-exercises-fig-q5-25': (179, (76, 622, 330, 690), 2.5), 'r-exercises-fig-q5-26': (179, (352, 60, 605, 128), 2.5), 'r-exercises-ref-figure-5-5': (154, (138, 76, 470, 247), 2.5), 'r-exercises-ref-figure-5-21': (165, (78, 152, 338, 295), 2.5), 'r-exercises-ref-figure-5-32': (171, (78, 318, 338, 480), 2.5), 'r-exercises-ref-figure-5-34': (172, (142, 583, 464, 734), 2.5), 'r-exercises-ref-figure-5-35': (173, (490, 140, 612, 295), 2.5)}
def main():
 with pymupdf.open(PDF)as pdf:
  for name,(page,rect,scale)in CROPS.items():
   pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(scale,scale),clip=pymupdf.Rect(rect),alpha=False).save(OUT/(name+'.png'))
 print('Reproduced',len(CROPS),'unchanged source figures.')
if __name__=='__main__':main()
