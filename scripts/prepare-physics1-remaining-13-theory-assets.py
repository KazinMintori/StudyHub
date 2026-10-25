"""Extract complete chapter13 source figures, with all original panels and labels."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-13'
SCALE=2.5
CROPS={'r-theory-13-01': (416, (31, 95, 199, 225)), 'r-theory-13-02': (416, (31, 500, 199, 735)), 'r-theory-13-03': (417, (451, 95, 618, 306)), 'r-theory-13-04': (417, (77, 440, 502, 616)), 'r-theory-13-05': (418, (338, 426, 541, 553)), 'r-theory-13-06': (419, (455, 145, 614, 304)), 'r-theory-13-07': (420, (35, 469, 194, 648)), 'r-theory-13-08': (420, (228, 527, 570, 744)), 'r-theory-13-09': (421, (445, 96, 616, 381)), 'r-theory-13-10': (422, (32, 203, 198, 342)), 'r-theory-13-11': (422, (32, 565, 198, 744)), 'r-theory-13-12': (423, (77, 564, 341, 730)), 'r-theory-13-13': (424, (0, 513, 194, 659)), 'r-theory-13-14': (425, (77, 60, 441, 270)), 'r-theory-13-15': (425, (454, 355, 616, 539)), 'r-theory-13-16': (425, (454, 598, 648, 743)), 'r-theory-13-17': (426, (35, 528, 194, 643)), 'r-theory-13-18': (428, (32, 116, 199, 278)), 'r-theory-13-19': (428, (32, 437, 199, 746)), 'r-theory-13-20': (429, (452, 116, 618, 285)), 'r-theory-13-21': (430, (54, 480, 552, 653)), 'r-theory-13-22': (431, (454, 88, 618, 266)), 'r-theory-13-23': (432, (31, 116, 200, 503)), 'r-theory-13-24': (433, (453, 151, 603, 295)), 'r-theory-13-25': (433, (110, 511, 294, 651)), 'r-theory-13-26': (434, (226, 472, 553, 741)), 'r-theory-13-27': (437, (88, 105, 420, 324)), 'r-theory-13-28': (438, (34, 221, 196, 441)), 'r-theory-13-29': (438, (35, 570, 194, 729)), 'r-theory-opener-saturn': (415, (0, 0, 438, 245)), 'r-theory-application-moon-walk': (420, (35, 205, 194, 365)), 'r-theory-application-interplanetary': (429, (77, 376, 280, 492)), 'r-theory-summary-newton': (439, (490, 457, 609, 531)), 'r-theory-summary-weight': (439, (484, 590, 606, 712)), 'r-theory-summary-orbit': (440, (442, 57, 575, 190)), 'r-theory-summary-black-hole': (440, (438, 199, 566, 296))}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(PDF)as document:
  for key,(page,rectangle)in CROPS.items():
   document[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(rectangle),alpha=False).save(str(OUT/(key+'.png')))
 print('Saved',len(CROPS),'complete original chapter13 theory figures.')
if __name__=='__main__':main()
