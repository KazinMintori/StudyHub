from pathlib import Path
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
CROPS={
'e-hinh-p20-34.png':(694,(179,464,294,556)),
'e-hinh-p20-36.png':(694,(378,115,498,225)),
'e-hinh-p20-37.png':(694,(438,252,571,348)),
'e-hinh-p20-39.png':(694,(457,558,553,662)),
'e-hinh-p20-42.png':(695,(135,368,277,460)),
'e-hinh-p20-49.png':(695,(412,565,546,660)),
'e-hinh-p20-55.png':(696,(470,196,563,291)),
'e-hinh-p20-56.png':(696,(472,482,571,577)),
'e-do-thi-doc-hieu20-59.png':(697,(429,61,538,213))
}
SCALE=3
def main():
 pdf=fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')
 out=ROOT/'docs/vat-ly-1/bai-giang/img/young-20';out.mkdir(parents=True,exist_ok=True)
 for name,(n,box) in CROPS.items():
  pdf[n-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(*box),alpha=False).save(out/name)
 print('Extracted9 exact RGB source crops')
if __name__=='__main__':main()
