"""Extract all26 E/P figures and the original bridge without changing artwork."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
root=Path(__file__).resolve().parents[1]
out=root/'docs/vat-ly-2/bai-giang/img/young-33';out.mkdir(parents=True,exist_ok=True)
CROPS={
 'hinh-bridge33-01':(1123,(424,101,544,165)),
 'hinh-e33-01':(1124,(178,257,296,374)),
 'hinh-e33-08':(1124,(176,669,300,727)),
 'hinh-e33-11':(1124,(454,179,615,326)),
 'hinh-e33-15':(1124,(453,500,615,601)),
 'hinh-e33-21':(1125,(224,242,341,316)),
 'hinh-e33-23':(1125,(210,417,342,492)),
 'hinh-e33-29':(1125,(352,236,615,334)),
 'hinh-e33-30':(1125,(352,428,615,524)),
 'hinh-p33-36':(1126,(171,155,310,352)),
 'hinh-p33-39':(1126,(227,631,300,753)),
 'hinh-p33-40':(1126,(445,61,577,148)),
 'hinh-p33-42':(1126,(451,225,578,309)),
 'hinh-p33-44':(1126,(418,370,577,562)),
 'hinh-p33-45':(1126,(458,594,577,755)),
 'hinh-p33-46':(1127,(221,61,338,118)),
 'hinh-p33-49':(1127,(260,424.8,339,553)),
 'hinh-p33-50':(1127,(77,561,267,640)),
 'hinh-p33-51':(1127,(353,181,617,280)),
 'hinh-p33-52':(1127,(353,444,617,554)),
 'hinh-p33-53':(1127,(353,645,544,734)),
 'hinh-p33-54':(1128,(147,60,294,170)),
 'hinh-p33-56':(1128,(163,488,296,645)),
 'hinh-p33-57':(1128,(311,159,531,280)),
 'hinh-p33-58':(1128,(448,291,617,403)),
 'hinh-p33-59':(1128,(409,622,618,745)),
 'hinh-p33-60':(1129,(184,164,339,360)),
}
rows=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,crop) in CROPS.items():
  pix=pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(crop),alpha=False)
  file=out/(stem+'.png');pix.save(file)
  with Image.open(file) as img:assert img.convert('RGB').tobytes()==pix.samples
  rows.append({'file':file.relative_to(root).as_posix(),'pdfPage':page,'clipPoints':crop,'scale':3,'decodedPixelsMatch':True,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
q=root/'qa/physics/chapter33'
(q/'exercise-image-source-ledger.json').write_text(json.dumps({'status':'passed','images':rows},indent=2),encoding='utf-8')
print('Extracted27 original bridge/E/P diagrams with unchanged PDF-region pixels.')
