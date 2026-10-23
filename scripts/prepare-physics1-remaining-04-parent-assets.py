"""Exact PDF crops for the parent-authored chapter4 opening and section4.1."""
from pathlib import Path
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
SCALE=2.5
CROPS={
 'parent-mo-dau':(120,(208,0,648,247)),
 'parent-hinh-4-01':(121,(452,63,617,193)),
 'parent-hinh-4-02':(121,(452,219,617,630)),
 'parent-hinh-4-03':(122,(207,62,615,210)),
 'parent-hinh-4-04':(122,(32,61,195,194)),
 'parent-hinh-4-05':(122,(32,247,195,442)),
 'parent-hinh-4-06':(122,(32,543,195,744)),
 'parent-hinh-4-07':(123,(76,392,337,542)),
 'parent-hinh-4-08':(124,(32,62,195,555)),
 'parent-hinh-4-09':(125,(125,62,440,214)),
 'parent-ung-dung-xe-truot':(125,(455,318,648,468)),
 'parent-hinh-4-10':(126,(74,460,614,748)),
 'parent-hinh-4-11':(127,(450,61,615,295)),
 'parent-hinh-4-12':(128,(207,61,616,339)),
 'parent-hinh-4-13':(128,(33,272,195,465)),
 'parent-hinh-4-14':(128,(33,487,195,746)),
 'parent-hinh-4-15':(129,(453,62,615,405)),
 'parent-hinh-4-16':(130,(0,150,204,325)),
 'parent-hinh-4-17':(131,(76,425,337,570)),
 'parent-hinh-4-18':(131,(352,627,612,748)),
 'parent-hinh-4-19':(132,(34,521,196,631)),
 'parent-hinh-4-20':(133,(454,553,615,748)),
 'parent-hinh-4-21':(134,(311,87,572,196)),
 'parent-hinh-4-22':(134,(34,259,196,548)),
 'parent-hinh-4-23':(134,(34,556,196,744)),
 'parent-hinh-4-24':(135,(450,565,615,746)),
 'parent-ung-dung-va-cham':(136,(0,184,193,331)),
 'parent-hinh-4-25':(137,(76,61,614,263)),
 'parent-hinh-4-26':(137,(76,587,614,737)),
 'parent-hinh-4-27':(138,(311,244,574,419)),
 'parent-hinh-4-28':(139,(455,449,614,687)),
 'parent-hinh-4-29':(140,(59,61,575,433)),
 'parent-tom-tat-hop-luc':(141,(485,87,613,149)),
 'parent-tom-tat-can-bang':(141,(485,175,613,235)),
 'parent-tom-tat-dinh-luat-hai':(141,(485,299,613,358)),
 'parent-tom-tat-trong-luong':(141,(485,409,613,459)),
 'parent-tom-tat-dinh-luat-ba':(141,(485,503,613,578)),
}
def main():
 out=ROOT/'docs/vat-ly-1/bai-giang/img/young-04';out.mkdir(parents=True,exist_ok=True)
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for name,(page,rect) in CROPS.items():pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(rect),alpha=False).save(out/(name+'.png'))
 print('Saved',len(CROPS),'exact original-PDF crops')
if __name__=='__main__':main()
