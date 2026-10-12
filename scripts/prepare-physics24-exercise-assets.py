from pathlib import Path
import pymupdf
root=Path(__file__).resolve().parents[1]
doc=pymupdf.open(root/'raw_materials/physics/source/young-freedman-15.pdf')
out=root/'docs/vat-ly-2/bai-giang/img/young-24';out.mkdir(parents=True,exist_ok=True)
figures={
 'hinh-e24-14':(806,(174,291,293,378)),
 'hinh-e24-16':(806,(105,519,222,664)),
 'hinh-e24-17':(806,(381,78,493,177)),
 'hinh-e24-20':(806,(453,271,567,367)),
 'hinh-e24-21':(806,(450,392,567,490)),
 'hinh-e24-28':(807,(211,301,333,330)),
 'hinh-e24-29':(807,(210,375,333,445))
}
for name,(page,clip) in figures.items():doc[page+19].get_pixmap(matrix=pymupdf.Matrix(2,2),clip=pymupdf.Rect(clip)).save(out/(name+'.png'))
print('Prepared',len(figures),'chapter24 exercise figures.')
