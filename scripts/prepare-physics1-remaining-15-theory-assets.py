"""Extract every original chapter15 figure, retaining the sign-contrast graphic unchanged."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-15'
SCALE=2.5
CROPS={'r-theory-mo-dau': (484, (210, 0, 648, 246)), 'r-theory-15-01': (485, (76, 96, 575, 323)), 'r-theory-app-snake': (485, (456, 599, 648, 741)), 'r-theory-15-02': (486, (272, 63, 508, 221)), 'r-theory-15-03': (486, (257, 601, 551, 741)), 'r-theory-15-04': (487, (455, 92, 616, 566)), 'r-theory-15-05': (487, (168, 613, 349, 730)), 'r-theory-15-06': (488, (207, 76, 573, 185)), 'r-theory-15-07': (488, (33, 198, 195, 532)), 'r-theory-15-08': (489, (455, 371, 615, 748)), 'r-theory-15-09': (490, (35, 478, 195, 755)), 'r-theory-15-10': (494, (136, 98, 575, 256)), 'r-theory-15-11': (495, (78, 80, 424, 229)), 'r-theory-15-12': (496, (0, 141.0, 192.1, 283.2)), 'r-theory-15-13': (496, (35, 400, 195, 576)), 'r-theory-app-peristalsis': (497, (462, 195, 608, 379)), 'r-theory-15-14': (497, (392, 527, 583, 724)), 'r-theory-app-duck': (498, (0, 435.6, 192.1, 552.2)), 'r-theory-15-15': (498, (35, 639, 195, 744)), 'r-theory-15-16': (499, (455, 324, 615, 439)), 'r-theory-15-17': (500, (35, 360, 195, 535)), 'r-theory-15-18': (501, (455, 96, 616, 376)), 'r-theory-15-19': (501, (455, 464, 616, 745)), 'r-theory-15-20': (502, (35, 105, 195, 379)), 'r-theory-15-21': (502, (35, 444, 158, 674)), 'r-theory-15-22': (502, (454, 597, 576, 645)), 'r-theory-selfcheck-15-6-answer': (502, (262, 651, 342, 753)), 'r-theory-15-23': (503, (77, 492, 575, 740)), 'r-theory-15-24': (504, (221, 59, 571, 472)), 'r-theory-15-25': (507, (456, 284, 648, 430)), 'r-theory-15-26': (507, (456, 514, 615, 744)), 'r-theory-15-27': (508, (309, 64, 470, 247)), 'r-theory-15-28': (508, (35, 377, 195, 557)), 'r-theory-15-29': (509, (115, 290, 397, 459)), 'r-theory-summary-01': (511, (500, 88, 615, 172)), 'r-theory-summary-02': (511, (500, 250, 590, 399)), 'r-theory-summary-03': (511, (500, 410, 615, 493)), 'r-theory-summary-04': (511, (500, 515, 555, 568)), 'r-theory-summary-05': (511, (500, 573, 616, 720))}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(PDF)as document:
  for key,(page,rectangle)in CROPS.items():
   document[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rectangle),alpha=False).save(str(OUT/(key+'.png')))
 print('Saved',len(CROPS),'unaltered original chapter15 theory figures.')
if __name__=='__main__':main()
