"""Crop chapter31 opening and section31.1 figures without cutting labels."""
from pathlib import Path
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-31'
CROPS={
 'mo-dau-31':(1038,(210,0,648,245)),
 'ky-hieu-nguon-xoay-chieu':(1039,(230,101,287,126)),
 'hinh-31-01':(1039,(455,87,613,226)),
 'hinh-31-02':(1039,(452,373,615,529)),
 'hinh-31-03':(1040,(39,95,192,451)),
 'hinh-31-04':(1040,(35,499,193,724)),
 'hinh-31-05':(1041,(456,87,612,192)),
 'hinh-31-06':(1041,(436,306,561,454)),
 'tu-kiem-31-01':(1041,(484,605,582,698)),
}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,box) in CROPS.items():
   pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(box),alpha=False).save(OUT/f'{stem}.png')
 print('Prepared nine opening and section31.1 assets for source review.')
if __name__=='__main__':main()
