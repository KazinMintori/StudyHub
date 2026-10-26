from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-01'
CROPS={'r-late-p1-56': (50, [105.0, 555.8, 221.4, 663.0], 2.5), 'r-late-p1-60': (50, [331.8, 305.0, 533.8, 405.4], 2.5), 'r-late-p1-61': (50, [308.6, 467.8, 535.0, 582.2], 2.5), 'r-late-p1-62': (50, [456.6, 603.6, 572.6, 743.2], 2.5), 'r-late-p1-91': (52, [340.6, 631.6, 540.6, 714.4], 2.5), 'r-late-p1-94': (53, [407.0, 148.6, 558.6, 251.0], 2.5)}
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 for name,(page,rect,scale)in CROPS.items():
  pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(scale,scale),clip=pymupdf.Rect(rect),alpha=False).save(OUT/(name+'.png'))
print('Reproduced',len(CROPS),'unchanged source figures.')
