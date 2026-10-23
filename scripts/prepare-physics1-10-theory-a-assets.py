"""Reproducible original-PDF crops for chapter10 sections10.1–10.4."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-10'
SCALE=2.5
CROPS={
 'a-mo-dau':(322,(215,0,648,248)),
 'a-hinh-10-01':(323,(451,92,615,265)),
 'a-hinh-10-02':(323,(450,307,615,541)),
 'a-hinh-10-03':(323,(451,602,615,752)),
 'a-hinh-10-04':(324,(33,123,195,400)),
 'a-hinh-10-05':(324,(34,604,578,750)),
 'a-hinh-10-06':(325,(450,486,615,635)),
 'a-hinh-10-07':(326,(34,128,195,234)),
 'a-hinh-10-08':(326,(33,329,195,485)),
 'a-hinh-10-09':(327,(78,391,615,530)),
 'a-hinh-10-10':(328,(34,106,300,325)),
 'a-hinh-10-11':(328,(33,510,195,751)),
 'a-hinh-10-12':(329,(450,182,615,360)),
 'a-hat-phong':(329,(452,575,648,743)),
 'a-hinh-10-13':(330,(210,85,575,244)),
 'a-hinh-10-14':(330,(0,424,194,569)),
 'a-hinh-10-15':(331,(78,79,338,238)),
 'a-hinh-10-16':(331,(78,510,338,590)),
 'a-hinh-10-17':(332,(0,206,194,351)),
 'a-hinh-10-18':(332,(310,438,576,615)),
 'a-hinh-10-19':(333,(78,270,338,407)),
 'a-hinh-10-20':(333,(78,582,442,750)),
 'a-hinh-10-21':(334,(34,465,195,710)),
 'a-hinh-10-22':(335,(451,215,615,414)),
 'a-co-lan':(334,(34,193,195,336)),
 'a-tu-kiem-10-01':(325,(451,205,615,319)),
 'a-tu-kiem-10-02':(328,(33,345,200,451)),
}
def main():
 OUT.mkdir(exist_ok=True)
 with pymupdf.open(PDF) as pdf:
  for name,(page,box) in CROPS.items():
   pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(box),alpha=False).save(OUT/(name+'.png'))
 print('Saved',len(CROPS),'original source crops.')
if __name__=='__main__':main()
