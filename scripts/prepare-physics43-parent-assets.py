from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUTPUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-43'
SPECS=[
 ('mo-dau-voi-ma-mut.png',1462,(210,0,648,244)),
 ('tom-tat-nang-luong-lien-ket.png',1495,(463,203,575,287)),
 ('tom-tat-phan-ra-alpha.png',1495,(458,338,582,416)),
 ('tom-tat-xa-hinh.png',1495,(467,446,546,528)),
 ('tom-tat-nhiet-hach.png',1495,(462,545,620,592)),
]
def main():
 OUTPUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(SOURCE) as pdf:
  for name,page,rect in SPECS:
   pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(3,3),clip=pymupdf.Rect(rect),alpha=False).save(OUTPUT/name)
 print('Saved five unaltered PDF source crops for chapter43 opening and summary.')
if __name__=='__main__':main()
