"""Exact original source crops for exercises17.61–119."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-17'
SCALE=3
CROPS={
 'e-p17-79':(595,(225,159,342,231)),
 'e-p17-91':(595,(498,656,615,737)),
 'e-p17-109':(597,(214,448,335,582)),
 'e-p17-113':(597,(488,382,615,484)),
 'e-p17-115':(598,(180,225,296,310)),
 'e-p17-117':(598,(312,204,525,292)),
}
def main():
 OUT.mkdir(exist_ok=True)
 with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,box) in CROPS.items():
   pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(box),alpha=False).save(OUT/(stem+'.png'))
 print('Saved6 original source figures.')
if __name__=='__main__':main()
