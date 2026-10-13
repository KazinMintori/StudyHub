"""Reproduce chapter 29 opening, summary illustrations and bridge diagram."""
from pathlib import Path
import pymupdf
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-29'
FIGURES={
    'mo-dau-29':(953,(0,0,430,246)),
    'tom-tat-faraday':(977,(488,91,615,178)),
    'tom-tat-lenz':(977,(488,192,578,257)),
    'tom-tat-chuyen-dong':(977,(484,276,592,337)),
    'tom-tat-dien-truong':(977,(487,385,590,442)),
    'hinh-bridge29-28':(978,(340,621,563,734)),
}
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    pdf=pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')
    for name,(printed,box) in FIGURES.items():
        page=pdf[printed+19]
        pix=page.get_pixmap(matrix=pymupdf.Matrix(2.5,2.5),clip=pymupdf.Rect(box),alpha=False)
        file=OUT/f'{name}.png';pix.save(file)
        if name!='mo-dau-29':
            image=Image.open(file).convert('RGB')
            bounds=ImageChops.difference(image,Image.new('RGB',image.size,'white')).getbbox()
            if bounds:
                x0,y0,x1,y1=bounds
                image.crop((max(0,x0-12),max(0,y0-12),min(image.width,x1+12),min(image.height,y1+12))).save(file,optimize=True)
    print(f'Prepared {len(FIGURES)} opening, summary and bridge assets.')
if __name__=='__main__':main()
