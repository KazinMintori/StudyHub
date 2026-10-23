"""Reproducible original-PDF figure regions for exercises11.49–95."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-11'
SCALE=3
CROPS={
 'e-p11-49':(380,(212,310,295,470)),
 'e-p11-50':(380,(179,508,300,605)),
 'e-p11-51':(380,(70,708,260,748)),
 'e-p11-53':(380,(450,170,575,296)),
 'e-p11-54':(380,(453,365,580,436)),
 'e-p11-55':(380,(443,466,578,542)),
 'e-p11-56':(381,(77,117,325,265)),
 'e-p11-58':(381,(209,385,337,508)),
 'e-p11-63':(381,(493,333,615,500)),
 'e-p11-64':(381,(500,550,615,730)),
 'e-p11-66':(382,(178,203,296,330)),
 'e-p11-67':(382,(34,545,263,646)),
 'e-p11-69':(382,(450,82,575,130)),
 'e-p11-70':(382,(457,202,578,294)),
 'e-p11-71':(382,(461,377,575,530)),
 'e-p11-74':(383,(223,140,338,211)),
 'e-p11-75':(383,(223,249,338,346)),
 'e-p11-76':(383,(78,513,322,580)),
 'e-p11-77':(383,(254,611,330,695)),
 'e-p11-78':(383,(500,80,613,196)),
 'e-p11-79':(383,(488,235,612,322)),
 'e-p11-80':(383,(495,420,613,525)),
 'e-p11-81':(383,(497,585,615,690)),
 'e-p11-83':(384,(173,145,290,217)),
 'e-p11-84':(384,(188,268,300,385)),
 'e-p11-86':(384,(132,543,298,635)),
 'e-p11-89':(385,(78,62,296,165)),
 'e-p11-90':(385,(225,208,337,285)),
 'e-mcat-11-92':(385,(504,76,615,210)),
}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,box) in CROPS.items():
   pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE),clip=pymupdf.Rect(box),alpha=False).save(OUT/(stem+'.png'))
 print('Saved',len(CROPS),'source crops. Pixel equality and visual edges require separate review.')
if __name__=='__main__':main()
