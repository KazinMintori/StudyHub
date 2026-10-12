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
 'hinh-e24-29':(807,(210,375,333,445)),
 'hinh-p24-48':(808,(470,185,571,252)),
 'hinh-p24-51':(808,(363,575,512,650)),
 'hinh-p24-53':(809,(226,90,338,161)),
 'hinh-p24-56':(809,(226,449,338,531)),
 'hinh-p24-59':(809,(510,79,614,141)),
 'hinh-p24-60':(809,(522,176,614,226)),
 'hinh-p24-64':(809,(494,617,614,669)),
 'hinh-p24-66':(810,(188,220,294,333)),
 'hinh-p24-69':(810,(344,243,527,369)),
 'hinh-p24-70':(810,(358,560,523,713)),
 'hinh-p24-72':(811,(238,173,337,293)),
 'tom-tat-tu-phang':(802,(450,469,572,549)),
 'tom-tat-noi-tiep':(802,(450,638,527,696)),
 'tom-tat-song-song':(802,(450,703,527,744)),
 'tom-tat-nang-luong':(803,(492,65,612,124)),
 'tom-tat-dien-moi':(803,(491,161,568,265))
}
for name,(page,clip) in figures.items():doc[page+19].get_pixmap(matrix=pymupdf.Matrix(2,2),clip=pymupdf.Rect(clip)).save(out/(name+'.png'))
print('Prepared',len(figures),'chapter24 exercise figures.')
