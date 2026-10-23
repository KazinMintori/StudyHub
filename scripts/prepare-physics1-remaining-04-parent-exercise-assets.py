"""Reproducible original PDF figure crops for the later Newton problems."""
from pathlib import Path
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
SCALE=2.5
CROPS={
 'parent-ex-hinh-e4-26':(145,(495,75,614,147)),
 'parent-ex-hinh-p4-35':(146,(35,62,270,174)),
 'parent-ex-hinh-p4-37':(146,(35,336,267,399)),
 'parent-ex-hinh-p4-38':(146,(35,485,267,537)),
 'parent-ex-hinh-p4-45':(146,(521,240,614,338)),
 'parent-ex-hinh-p4-46':(146,(311,400,505,558)),
 'parent-ex-hinh-p4-60':(148,(311,62,614,240)),
}
with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 out=ROOT/'docs/vat-ly-1/bai-giang/img/young-04';out.mkdir(parents=True,exist_ok=True)
 for name,(page,rect) in CROPS.items():
  pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(rect),alpha=False).save(out/(name+'.png'))
print('Saved',len(CROPS),'exact original figures')
