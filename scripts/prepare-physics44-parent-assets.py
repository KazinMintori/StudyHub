from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUTPUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-44'
SPECS=[
 ('mo-dau-tinh-van-tarantula.png',1503,(0,0,438,246)),
 ('tom-tat-tao-cap.png',1539,(487,89,572,161)),
 ('tom-tat-cyclotron.png',1539,(485,199,600,259)),
 ('tom-tat-quark.png',1539,(484,405,610,452)),
 ('tom-tat-thong-nhat.png',1539,(379,465,607,567)),
 ('tom-tat-hubble.png',1539,(485,579,633,646)),
 ('tom-tat-lich-su-vu-tru.png',1539,(487,671,577,723)),
 ('lich-su-vu-tru-trang-1.png',1534,(0,50,648,783)),
 ('lich-su-vu-tru-trang-2.png',1535,(0,55,648,783)),
]
def main():
 OUTPUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(SOURCE) as pdf:
  for name,page,rect in SPECS:
   pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(3,3),clip=pymupdf.Rect(rect),alpha=False).save(OUTPUT/name)
 print(f'Saved {len(SPECS)} unaltered PDF source crops for chapter44 opening, summary and full history diagram.')
if __name__=='__main__':main()
