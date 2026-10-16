"""Extract unchanged source images for the chapter42 parent fragments."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'mo-dau-sao-kim':(1428,(205,0,648,246)),
 'tom-tat-fermi-dirac':(1454,(449,65,558,137)),
 'tom-tat-ban-dan':(1454,(449,176,557,264)),
 'tom-tat-diot':(1454,(450,285,574,337)),
}
SCALE=3
def main():
    out=ROOT/'docs/vat-ly-2/bai-giang/img/young-42';out.mkdir(parents=True,exist_ok=True)
    qa=ROOT/'qa/physics/chapter42';qa.mkdir(exist_ok=True)
    rows=[]
    with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
        for stem,(page,clip) in CROPS.items():
            pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(clip),alpha=False)
            file=out/(stem+'.png');pix.save(file)
            with Image.open(file) as image:
                assert image.convert('RGB').tobytes()==pix.samples and image.size==(pix.width,pix.height)
            rows.append(dict(stem=stem,pdfPage=page,clip=clip,scale=SCALE,pixelMatch=True,sha256=hashlib.sha256(file.read_bytes()).hexdigest()))
    (qa/'parent-image-ledger.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    print('Extracted4unchangedsourcecrops;pixelmatchtrue.Visualboundariesrequireinspection.')
if __name__=='__main__':main()
