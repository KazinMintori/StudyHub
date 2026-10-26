from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-03'
CROPS={'r-numbered-early-e3-10': (113, [352, 63, 546, 158], 2.5), 'r-numbered-early-e3-19': (114, [35, 285, 290, 444], 2.5), 'r-numbered-early-e3-29': (114, [311, 634, 506, 739], 2.5), 'r-numbered-early-e3-31': (115, [226, 63, 337, 190], 2.5), 'r-numbered-early-e3-36': (115, [76, 653, 317, 743], 2.5), 'r-numbered-early-e3-38': (115, [352, 165, 594, 258], 2.5)}
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 for name,(page,rect,scale)in CROPS.items():
  pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(scale,scale),clip=pymupdf.Rect(rect),alpha=False).save(OUT/(name+'.png'))
print('Reproduced',len(CROPS),'unchanged original figures.')
