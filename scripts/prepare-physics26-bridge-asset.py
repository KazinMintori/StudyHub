from pathlib import Path
import pymupdf
from PIL import Image,ImageChops
root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-26'
out.mkdir(parents=True,exist_ok=True)
doc=pymupdf.open(root/'raw_materials/physics/source/young-freedman-15.pdf')
doc[868+19].get_pixmap(matrix=pymupdf.Matrix(3,3),clip=pymupdf.Rect(492,552,589,657)).save(out/'hinh-26-27.png')
image=Image.open(out/'hinh-26-27.png').convert('RGB')
bounds=ImageChops.difference(image,Image.new('RGB',image.size,'white')).getbbox()
assert bounds
left,top,right,bottom=bounds
image.crop((max(0,left-5),max(0,top-5),min(image.width,right+5),min(image.height,bottom+5))).save(out/'hinh-26-27.png',optimize=True)
print('Prepared figure26.27; crop requires visual review.')
