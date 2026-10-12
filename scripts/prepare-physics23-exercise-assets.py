from pathlib import Path
import pymupdf
root=Path(__file__).resolve().parents[1]
doc=pymupdf.open(root/'raw_materials/physics/source/young-freedman-15.pdf')
out=root/'docs/vat-ly-2/bai-giang/img/young-23'
figures={
 'hinh-23-27':(772,(35,271,296,338)),
 'hinh-q23-9':(772,(468,440,570,535)),
 'hinh-e23-5':(773,(495,169,615,226)),
 'hinh-e23-19':(774,(180,369,298,438)),
 'hinh-p23-57':(776,(452,177,565,294)),
 'hinh-p23-59':(776,(382,540,498,642)),
 'hinh-p23-62':(777,(77,452,316,570)),
 'hinh-p23-63':(777,(212,640,338,700)),
 'hinh-p23-65':(777,(534,258,615,422)),
 'hinh-p23-71':(778,(178,80,295,129)),
 'hinh-p23-72':(778,(193,191,296,264)),
 'hinh-p23-78':(778,(354,604,564,713)),
 'hinh-p23-80':(779,(222,623,338,726)),
 'hinh-p23-81':(779,(404,359,563,515)),
 'tom-tat-the-nang':(770,(451,93,615,211)),
 'tom-tat-dien-the':(770,(451,236,615,350)),
 'tom-tat-dang-the':(770,(451,432,592,531))
}
for name,(p,clip) in figures.items():doc[p+19].get_pixmap(matrix=pymupdf.Matrix(2,2),clip=pymupdf.Rect(clip)).save(out/(name+'.png'))
print('Prepared',len(figures),'exercise figures for chapter23.')
