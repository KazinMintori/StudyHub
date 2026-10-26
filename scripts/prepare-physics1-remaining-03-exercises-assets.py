"""Reproduce unchanged original figures for the reviewed chapter3 guided material."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-03'
CROPS={'r-exercises-figure-3-11': (92, (34, 262, 197, 490)), 'r-exercises-figure-3-37': (111, (352, 615, 552, 688)), 'r-exercises-figure-q3-16': (112, (310, 503, 557, 584)), 'r-exercises-chapter3-media-qr': (111, (302, 57, 615, 101))}
SCALE=2.5
def main():
 with pymupdf.open(PDF)as pdf:
  for name,(page,rect)in CROPS.items():
   pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rect),alpha=False).save(OUT/(name+'.png'))
 print('Reproduced',len(CROPS),'unchanged original guided-material figures.')
if __name__=='__main__':main()
