"""Extract chapter31 figures7–24, application photos and seven summary diagrams."""
from pathlib import Path
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-31'
# PDF1-based page and point coordinates. Retain all labels and panel headings.
CROPS={
 'hinh-31-07':(1042,(34,104,197,471)),
 'hinh-31-08':(1042,(116,592,619,743)),
 'hinh-31-09':(1045,(450,84,617,472)),
 'hinh-31-10':(1045,(350,528,617,613)),
 'hinh-31-11':(1046,(37,175,181,295)),
 'hinh-31-12':(1046,(33,381,196,742)),
 'hinh-31-13':(1047,(451,108,615,550)),
 'hinh-31-14':(1048,(44,199,184,397)),
 'ung-dung-31-do-thanh-phan-co-the':(1048,(35,552,193,742)),
 'hinh-31-15':(1050,(360,372,520,510)),
 'hinh-31-16':(1051,(74,559,612,735)),
 'hinh-31-17':(1052,(33,631,205,742)),
 'hinh-31-18':(1054,(34,232,183,614)),
 'hinh-31-19':(1055,(455,114,611,239)),
 'hinh-31-20':(1055,(118,594,309,741)),
 'ky-hieu-may-bien-ap':(1056,(374,547,402,584)),
 'hinh-31-21':(1056,(414,600,572,750)),
 'ung-dung-31-dien-ap-cao':(1056,(0,457,192,602)),
 'hinh-31-22':(1057,(455,374,613,482)),
 'hinh-31-23':(1057,(455,599,613,746)),
 'hinh-31-24':(1058,(121,606,542,739)),
 'ung-dung-31-truyen-tai-mot-chieu':(1058,(0,224,193,384)),
 'tom-tat-31-01-gian-do-pha':(1060,(448,96,515,166)),
 'tom-tat-31-02-pha-dien-ap':(1060,(448,231,515,293)),
 'tom-tat-31-03-dien-khang':(1060,(445,306,574,370)),
 'tom-tat-31-04-mach-rlc':(1060,(448,405,538,475)),
 'tom-tat-31-05-cong-suat':(1060,(447,488,530,560)),
 'tom-tat-31-06-cong-huong':(1060,(447,573,563,645)),
 'tom-tat-31-07-may-bien-ap':(1060,(449,662,565,736)),
}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,box) in CROPS.items():
   rect=fitz.Rect(box)
   assert pdf[page-1].rect.contains(rect),(stem,rect)
   pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=rect,alpha=False).save(OUT/f'{stem}.png')
 print(f'Prepared {len(CROPS)} section31.2–31.6 and summary images for visual review.')
if __name__=='__main__':main()
