"""Unmodified source figures, application panels and summary diagrams for chapter39."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'hinh-39-30':(1323,(455,136,618,285)),
 'hinh-39-31':(1323,(455.96,466.47,648,670.17)),
 'hinh-39-32':(1324,(34,105,196,287)),
 'hinh-39-33':(1325,(175,536,390,738)),
 'hinh-39-34':(1328,(72,544,577,746)),
 'hinh-39-35':(1329,(473,180,610,289)),
 'ung-dung-doi-mat':(1325,(454,205,612,606)),
 'ung-dung-mau-sao':(1326,(34,285,194,738)),
 'ung-dung-dam-may-khi':(1306,(0,208.737,192,457.856)),
 'ung-dung-huynh-quang-ca':(1313,(456.522,155.14,648,296.5)),
 'tom-tat-song-electron':(1331,(488,88,616,185)),
 'tom-tat-hat-nhan':(1331,(493,202,592,245)),
 'tom-tat-muc-nang-luong':(1331,(492,260,605,326)),
 'tom-tat-bohr':(1331,(488,350,616,445)),
 'tom-tat-laser':(1331,(494,499,600,544)),
 'tom-tat-vat-den':(1331,(488,568,611,671)),
 'tom-tat-bat-dinh':(1331,(493,681,592,752)),
 'hinh-e39-25':(1335,(219,139,337,232)),
 'hinh-e39-27':(1335,(219,449,338,587)),
}
SCALE=3
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-39'
def main():
 OUT.mkdir(parents=True,exist_ok=True);rows=[]
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for stem,(page,clip) in CROPS.items():
   pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(clip),alpha=False)
   p=OUT/(stem+'.png');pix.save(p)
   with Image.open(p) as im:assert im.size==(pix.width,pix.height) and im.convert('RGB').tobytes()==pix.samples
   rows.append(dict(stem=stem,pdfPage=page,clip=clip,scale=SCALE,pixelMatch=True,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 q=ROOT/'qa/physics/chapter39';q.mkdir(parents=True,exist_ok=True)
 (q/'parent-image-ledger.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
 print('Extracted',len(rows),'unchanged source figures/application panels/summary diagrams.')
if __name__=='__main__':main()
