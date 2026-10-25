"""Extract all original chapter16 theory images with unchanged pixels and labels."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-16'
SCALE=2.5
CROPS={'r-theory-opening': (521, (0, 0, 439, 247)), 'r-theory-16-01': (522, (34, 98, 196, 429)), 'r-theory-16-02': (522, (34, 553, 196, 734)), 'r-theory-16-03': (523, (76, 58, 422, 366)), 'r-theory-16-04': (524, (310, 371, 572, 535)), 'r-theory-16-05': (525, (454, 269, 615, 705)), 'r-theory-app-hearing-loss': (526, (36, 158, 192, 339)), 'r-theory-16-06': (526, (35, 572, 194, 683)), 'r-theory-16-07': (527, (453, 126, 621, 307)), 'r-theory-16-08': (528, (311, 106, 562, 257)), 'r-theory-16-09': (528, (0, 489, 193, 635)), 'r-theory-16-10': (531, (449, 118, 648, 250)), 'r-theory-16-11': (533, (352, 464, 612, 570)), 'r-theory-16-12': (534, (208, 583, 572, 743)), 'r-theory-16-13': (535, (451, 128, 619, 406)), 'r-theory-16-14': (535, (352, 587, 594, 703)), 'r-theory-16-15': (536, (0, 88, 194, 251)), 'r-theory-16-16': (536, (34, 354, 195, 579)), 'r-theory-16-17': (536, (76, 667, 614, 751)), 'r-theory-16-18': (537, (76, 84, 614, 172)), 'r-theory-16-19': (538, (34, 487, 200, 746)), 'r-theory-app-ear-resonance': (539, (455, 197, 648, 343)), 'r-theory-16-20': (539, (454, 421, 648, 593)), 'r-theory-16-21': (540, (34, 524, 200, 743)), 'r-theory-16-22': (541, (76, 58, 423, 279)), 'r-theory-16-23': (541, (77, 632, 322, 746)), 'r-theory-16-24': (542, (35, 108, 194, 247)), 'r-theory-16-25': (542, (257, 564, 527, 745)), 'r-theory-16-26': (543, (454, 598, 648, 743)), 'r-theory-16-27': (544, (208, 565, 573, 743)), 'r-theory-16-28': (545, (76, 59, 423, 267)), 'r-theory-16-29': (546, (0, 118, 193, 241)), 'r-theory-16-30': (546, (312, 541, 571, 614)), 'r-theory-16-31': (547, (352, 100, 613, 166)), 'r-theory-16-32': (547, (352, 343, 613, 411)), 'r-theory-16-33': (547, (352, 576, 613, 642)), 'r-theory-16-34': (548, (310, 108, 571, 309)), 'r-theory-16-35': (549, (454, 125, 614, 234)), 'r-theory-16-36': (549, (76, 570, 575, 744)), 'r-theory-16-37': (550, (0, 228, 194, 346)), 'r-theory-16-38': (551, (77, 106, 333, 274)), 'r-theory-summary-wave': (551, (488, 475, 617, 677)), 'r-theory-summary-intensity': (552, (441, 60, 570, 126)), 'r-theory-summary-standing': (552, (438, 199, 573, 357)), 'r-theory-summary-interference': (552, (441, 385, 575, 449)), 'r-theory-summary-beats': (552, (441, 471, 576, 562)), 'r-theory-summary-doppler': (552, (441, 581, 576, 668)), 'r-theory-summary-shock': (552, (441, 691, 575, 743))}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(PDF)as document:
  for key,(page,rectangle)in CROPS.items():
   document[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rectangle),alpha=False).save(str(OUT/(key+'.png')))
 print('Saved',len(CROPS),'original chapter16 source images.')
if __name__=='__main__':main()
