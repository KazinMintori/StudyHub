"""Reproduce the seven unchanged source frames accompanying chapter8 guided work and discussion."""
from pathlib import Path
import json
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'raw_materials/physics/translations/chapter-08/parent-guided-discussion-image-assets.json').read_text(encoding='utf8'))
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for row in rows:
  pdf[row['source_pdf_page_1based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['clip_pdf_points']),alpha=False).save(ROOT/row['publicFile'])
print('Reproduced seven original source frames, unchanged.')
