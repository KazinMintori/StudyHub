"""Exact PDF crops for chapter6 end figures and referenced diagrams."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-06'
SCALE=2.5
CROPS={'r-exercises-fig-6-29': (212, (72, 338, 254, 435)), 'r-exercises-fig-q6-8': (212, (317, 637, 564, 689)), 'r-exercises-fig-e6-7': (213, (492, 493, 614, 572)), 'r-exercises-fig-e6-33': (215, (289, 259, 326, 362)), 'r-exercises-fig-e6-34': (215, (218, 393, 332, 489)), 'r-exercises-fig-e6-41': (215, (494, 254, 608, 329)), 'r-exercises-fig-p6-71': (217, (225, 573, 337, 674)), 'r-exercises-fig-p6-74': (217, (357, 344, 606, 496)), 'r-exercises-fig-p6-79': (218, (173, 254, 286, 304)), 'r-exercises-fig-p6-81': (218, (178, 440, 292, 523)), 'r-exercises-fig-p6-90': (219, (92, 78, 317, 222)), 'r-exercises-fig-p6-92': (219, (115, 640, 300, 742)), 'r-exercises-fig-p6-94': (219, (385, 555, 581, 714)), 'r-exercises-ref-fig-5-5': (154, (140, 77, 471, 248)), 'r-exercises-ref-fig-5-32': (171, (90, 319, 327, 477))}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(PDF)as doc:
  for key,(page,rect)in CROPS.items():
   doc[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rect),alpha=False).save(str(OUT/(key+'.png')))
 print('Saved',len(CROPS),'exact original crops; fullFig6.22is reused from existingtheory.')
if __name__=='__main__':main()
