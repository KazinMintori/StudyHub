"""Extract original chapter14 exercise figures without altering source content."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-14'
SCALE=3
CROPS={'r-exercises-e14-4': (477, (76, 140, 276, 240)), 'r-exercises-e14-7': (477, (76, 405, 294, 503)), 'r-exercises-e14-19': (477, (348, 492, 548, 590)), 'r-exercises-e14-40': (479, (76, 110, 276, 216)), 'r-exercises-e14-48': (479, (76, 644, 310, 737)), 'r-exercises-e14-53': (479, (388, 449, 583, 580)), 'r-exercises-e14-58': (480, (173, 188, 296, 273)), 'r-exercises-p14-66': (480, (361, 227, 524, 287)), 'r-exercises-p14-73': (481, (167, 364, 256, 459)), 'r-exercises-p14-85': (482, (188, 370, 298, 488)), 'r-exercises-p14-87': (482, (183, 592, 295, 719)), 'r-exercises-p14-88': (482, (457, 76, 572, 176)), 'r-exercises-p14-89': (482, (452, 209, 578, 276)), 'r-exercises-p14-92': (483, (228, 91, 334, 279)), 'r-exercises-mcat14-94-96': (483, (491, 295, 610, 349)), 'r-exercises-figure-14-29': (475, (351, 522, 615, 604))}
SCALES={'r-exercises-figure-14-29': 2.5}
def main():
 OUT.mkdir(exist_ok=True)
 with pymupdf.open(PDF)as document:
  for name,(page,rect)in CROPS.items():
   scale=SCALES.get(name,SCALE)
   document[page-1].get_pixmap(matrix=pymupdf.Matrix(scale,scale),clip=pymupdf.Rect(rect),alpha=False).save(str(OUT/(name+'.png')))
 print('Saved',len(CROPS),'unchanged original exercise images.')
if __name__=='__main__':main()
