"""Extract original chapter14theory figures, without repainting or translated overlays."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-14'
SCALE=2.5
CROPS={'r-theory-14-01': (450, (286, 74, 480, 148)), 'r-theory-14-02': (450, (32, 124, 201, 469)), 'r-theory-14-03': (451, (451, 574, 619, 746)), 'r-theory-14-04': (452, (31, 198, 201, 413)), 'r-theory-14-05': (452, (111, 563, 574, 746)), 'r-theory-14-06': (453, (452, 344, 620, 683)), 'r-theory-14-07': (454, (32, 289, 198, 501)), 'r-theory-14-08': (454, (308, 590, 577, 741)), 'r-theory-14-09': (455, (452, 441, 618, 552)), 'r-theory-14-10': (455, (76, 636, 618, 747)), 'r-theory-14-11': (456, (274, 86, 503, 210)), 'r-theory-14-12': (456, (31, 464, 197, 750)), 'r-theory-14-13': (457, (452, 96, 619, 440)), 'r-theory-14-14': (459, (77, 587, 557, 749)), 'r-theory-14-15': (460, (238, 61, 618, 233)), 'r-theory-14-16': (461, (351, 101, 618, 313)), 'r-theory-14-17': (462, (212, 76, 577, 270)), 'r-theory-14-18': (462, (32, 634, 201, 735)), 'r-theory-14-19': (463, (451, 392, 618, 512)), 'r-theory-14-20': (464, (77, 76, 618, 236)), 'r-theory-14-21': (466, (32, 86, 201, 450)), 'r-theory-14-22': (466, (32, 530, 201, 662)), 'r-theory-14-23': (467, (452, 521, 630, 752)), 'r-theory-14-24': (469, (351, 112, 618, 279)), 'r-theory-14-25': (469, (453, 595, 648, 744)), 'r-theory-14-26': (470, (31, 486, 201, 660)), 'r-theory-14-27': (471, (452, 104, 618, 368)), 'r-theory-14-28': (472, (207, 530, 579, 745)), 'r-theory-opener-dogs': (449, (0, 0, 438, 245)), 'r-theory-application-hummingbird': (450, (0, 594, 194, 741)), 'r-theory-application-ladybug': (472, (0, 197, 194, 342)), 'r-theory-application-dog-panting': (473, (453, 185, 648, 323)), 'r-theory-summary-periodic': (473, (477, 454, 619, 551)), 'r-theory-summary-shm': (473, (480, 578, 607, 641)), 'r-theory-summary-energy': (474, (445, 72, 562, 137)), 'r-theory-summary-angular': (474, (443, 159, 522, 224)), 'r-theory-summary-simple-pendulum': (474, (443, 245, 538, 342)), 'r-theory-summary-physical-pendulum': (474, (442, 360, 525, 438)), 'r-theory-summary-damped': (474, (444, 459, 564, 576)), 'r-theory-summary-forced': (474, (442, 590, 564, 680))}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(PDF)as document:
  for key,(page,rectangle)in CROPS.items():
   document[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rectangle),alpha=False).save(str(OUT/(key+'.png')))
 print('Saved',len(CROPS),'complete originalchapter14theoryfigures.')
if __name__=='__main__':main()
