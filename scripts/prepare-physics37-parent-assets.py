"""Extract unchanged opening, application and summary regions for chapter37."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image

root=Path(__file__).resolve().parents[1]
CROPS={
 'mo-dau-37':(1237,(0,0,444,252)),
 'ung-dung-37-sinh-doi':(1247,(455,249,613,364)),
 'ung-dung-37-chay-tiep-suc':(1253,(455,255,615,444)),
 'ung-dung-37-nang-luong-hat-nhan':(1261,(455,170,648,323)),
 'tong-ket-37-bat-bien':(1264,(444,510,569,557)),
 'tong-ket-37-thoi-gian':(1264,(444,567,566,642)),
 'tong-ket-37-chieu-dai':(1264,(444,654,567,726)),
 'tong-ket-37-lorentz':(1265,(490,60,614,145)),
 'tong-ket-37-doppler':(1265,(490,206,614,255)),
 'tong-ket-37-nang-luong':(1265,(488,285,614,405)),
}
SCALE=3
out=root/'docs/vat-ly-2/bai-giang/img/young-37';out.mkdir(parents=True,exist_ok=True)
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,box) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(box),alpha=False)
  dest=out/(stem+'.png');pix.save(dest)
  with Image.open(dest) as im:assert im.convert('RGB').tobytes()==pix.samples
  rows.append(dict(path=dest.relative_to(root).as_posix(),pdfPage=page,box=box,pixelMatch=True,sha256=hashlib.sha256(dest.read_bytes()).hexdigest()))
q=root/'qa/physics/chapter37';q.mkdir(parents=True,exist_ok=True)
(q/'parent-image-source-ledger.json').write_text(json.dumps(dict(status='pixel-match-visual-review-pending',images=rows),indent=2)+'\n',encoding='utf-8')
print('Extracted',len(rows),'unchanged parent image regions.')
