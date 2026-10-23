"""Original statement figures inspected against PDF143–145."""
from pathlib import Path
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
SCALE=2.5
CROPS={
 'r-exercises-q4-31':(143,(489,505,614,568)),
 'r-exercises-e4-2':(144,(35,324,221,456)),
 'r-exercises-e4-3':(144,(194,460,296,580)),
 'r-exercises-e4-4':(144,(35,638,221,747)),
 'r-exercises-e4-13':(144,(440,514,570,598)),
 'r-exercises-e4-14':(144,(440,635,570,732)),
 'r-exercises-e4-23':(145,(214,554,338,623)),
}
with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 out=ROOT/'docs/vat-ly-1/bai-giang/img/young-04';out.mkdir(parents=True,exist_ok=True)
 for name,(page,rect) in CROPS.items():
  pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(rect),alpha=False).save(out/(name+'.png'))
print('Saved',len(CROPS),'original early exercise figures')
