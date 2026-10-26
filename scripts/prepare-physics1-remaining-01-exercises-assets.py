"""Reproduce original reviewed chapter1 exercise image crops without altering them."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-01'
CROPS={'r-exercises-e1-21': (48, (310.0, 260.0, 535.0, 405.0)), 'r-exercises-e1-22': (48, (440.0, 400.0, 615.0, 570.0)), 'r-exercises-e1-33': (49, (75.0, 455.0, 300.0, 580.0)), 'r-exercises-e1-37': (49, (495.0, 60.0, 615.0, 180.0)), 'r-exercises-bridge-fig-1-34': (46, (305, 398, 545, 542)), 'r-exercises-guided-media-qr': (46, (260, 37, 573, 76)), 'r-exercises-q1-21-figure-1-7': (28, (35, 117, 195, 325))}
SCALE=2.5
def main():
 with pymupdf.open(PDF)as pdf:
  for name,(page,rect)in CROPS.items():
   pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rect),alpha=False).save(OUT/(name+'.png'))
 print('Reproduced',len(CROPS),'unchanged original exercise images.')
if __name__=='__main__':main()
