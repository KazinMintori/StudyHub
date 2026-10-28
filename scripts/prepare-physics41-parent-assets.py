"""Unchanged source illustrations for the chapter opening and summary."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'mo-dau-liti-heli':(1380,(205,0,648,246)),
 'tom-tat-hop-ba-chieu':(1419,(492,160,620,263)),
 'tom-tat-momen-quy-dao':(1419,(492,280,615,389)),
 'tom-tat-zeeman':(1419,(492,475,616,574)),
 'tom-tat-spin':(1419,(492,588,620,700)),
 'tom-tat-che-chan':(1420,(446,70,545,183)),
 'tom-tat-moseley':(1420,(449,198,568,278)),
 'tom-tat-roi-luong-tu':(1420,(450,281,615,330)),
}
SCALE=3
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-41'
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    qa=ROOT/'qa/physics/chapter41';qa.mkdir(parents=True,exist_ok=True)
    rows=[]
    with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
        for stem,(page,clip) in CROPS.items():
            pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(clip),alpha=False)
            destination=OUT/(stem+'.png');pix.save(destination)
            with Image.open(destination) as image:
                assert image.convert('RGB').tobytes()==pix.samples,stem
            rows.append(dict(stem=stem,pdfPage=page,clip=clip,scale=SCALE,pixelMatch=True,
                             sha256=hashlib.sha256(destination.read_bytes()).hexdigest()))
    (qa/'parent-image-ledger.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    print('Extracted8unchangedsourceillustrations; allRGBpixelsmatch.')
if __name__=='__main__':main()
