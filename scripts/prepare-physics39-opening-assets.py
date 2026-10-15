from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={'mo-dau-39':(1299,(0,0,444,252))}
SCALE=3
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-39'
def main():
 OUT.mkdir(parents=True,exist_ok=True);rows=[]
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,clip) in CROPS.items():
   pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(clip),alpha=False);p=OUT/(stem+'.png');pix.save(p)
   with Image.open(p) as im:assert im.size==(pix.width,pix.height) and im.convert('RGB').tobytes()==pix.samples
   rows.append(dict(stem=stem,pdfPage=page,clip=clip,scale=SCALE,pixelMatch=True,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 q=ROOT/'qa/physics/chapter39';q.mkdir(parents=True,exist_ok=True);(q/'opening-image-ledger.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
 print('Extracted unchanged chapter39 opening image.')
if __name__=='__main__':main()
