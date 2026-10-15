"""Extract the application photographs and summary diagrams without pixel edits."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'ung-dung-tu-ngoai':(1279,(456,441.137,612,545.056)),
 'ung-dung-x-quang':(1282,(0,258.069,192.034,400.148)),
 'ung-dung-bat-buom':(1289,(456,360.112,612,541.791)),
 'tom-tat-quang-dien':(1292,(453,340,568,447)),
 'tom-tat-compton':(1292,(451,469,581,557)),
 'tom-tat-bat-dinh':(1292,(451,638,558,740)),
}
SCALE=3
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-38'
def main():
 OUT.mkdir(parents=True,exist_ok=True);rows=[]
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,clip) in CROPS.items():
   pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(clip),alpha=False)
   p=OUT/(stem+'.png');pix.save(p)
   with Image.open(p) as im:assert im.size==(pix.width,pix.height) and im.convert('RGB').tobytes()==pix.samples
   rows.append(dict(stem=stem,pdfPage=page,clip=clip,scale=SCALE,pixelMatch=True,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 q=ROOT/'qa/physics/chapter38';q.mkdir(parents=True,exist_ok=True)
 (q/'parent-image-ledger.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
 print('Extracted six unchanged application and summary images.')
if __name__=='__main__':main()
