"""Recheck the exact original PDF rasters for eight reviewed figure repairs."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image
ROOT=Path(__file__).resolve().parents[2]
report=json.loads((ROOT/'raw_materials/physics/reviews/confirmed-original-frame-restoration-20261028.json').read_text('utf8'))
with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as doc:
 for row in report['figures']:
  asset=ROOT/row['asset'];assert hashlib.sha256(asset.read_bytes()).hexdigest()==row['sha256'],asset
  scale=row['scale'];pix=doc[row['sourcePDFPage']-1].get_pixmap(matrix=fitz.Matrix(scale,scale),clip=fitz.Rect(row['completeBox']))
  actual=Image.open(asset).convert('RGB');expected=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
  assert actual.size==expected.size and actual.tobytes()==expected.tobytes(),asset
assert len(report['figures'])==8 and report['actualCaseCount']==30
print('PASS eight complete original figure crops. Scope is only the recorded repairs, not all-course fidelity.')
