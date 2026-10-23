"""Original-PDF figure and supplementary requested plot for exercises17.1–60."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
SCALE=3
CROPS={'d-hinh-e17-60':(593,(354,654,604,734))}
def main():
 out=ROOT/'docs/vat-ly-1/bai-giang/img/young-17';out.mkdir(exist_ok=True)
 with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for name,(p,box) in CROPS.items():
   pdf[p-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(box),alpha=False).save(out/(name+'.png'))
 print('Saved source figure E17.60.')
if __name__=='__main__':main()
