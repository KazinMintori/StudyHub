from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-03'
CROPS={'r-numbered-late-p3-47': (116, [100.0, 248.0, 230.0, 335.0], 2.5), 'r-numbered-late-p3-54': (116, [310.0, 146.0, 555.0, 292.0], 2.5), 'r-numbered-late-p3-57': (116, [310.0, 460.0, 550.0, 595.0], 2.5), 'r-numbered-late-p3-58': (116, [310.0, 665.0, 550.0, 745.0], 2.5), 'r-numbered-late-p3-60': (117, [75.0, 288.0, 305.0, 370.0], 2.5), 'r-numbered-late-p3-61': (117, [75.0, 470.0, 295.0, 635.0], 2.5), 'r-numbered-late-p3-63': (117, [350.0, 165.0, 560.0, 315.0], 2.5), 'r-numbered-late-p3-65': (117, [350.0, 538.0, 595.0, 655.0], 2.5), 'r-numbered-late-p3-76': (118, [310.0, 225.0, 555.0, 335.0], 2.5)}
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 for name,(page,rect,scale)in CROPS.items():
  pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(scale,scale),clip=pymupdf.Rect(rect),alpha=False).save(OUT/(name+'.png'))
print('Reproduced',len(CROPS),'unchanged original figures.')
