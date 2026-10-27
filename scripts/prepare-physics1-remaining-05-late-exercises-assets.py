"""Reproduce29unchanged original source frames for chapter5late exercises."""
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-1/bai-giang/img/young-05'
CROPS={'r-numbered-late-p5-60': (184, [312, 60, 572, 185], 2.5), 'r-numbered-late-p5-61': (184, [312, 245, 572, 395], 2.5), 'r-numbered-late-p5-62': (184, [480, 395, 582, 535], 2.5), 'r-numbered-late-p5-64': (184, [470, 625, 625, 750], 2.5), 'r-numbered-late-p5-73': (185, [506, 60, 618, 150], 2.5), 'r-numbered-late-p5-74': (185, [350, 235, 572, 360], 2.5), 'r-numbered-late-p5-75': (185, [558, 358, 620, 500], 2.5), 'r-numbered-late-p5-76': (185, [350, 595, 572, 740], 2.5), 'r-numbered-late-p5-78': (186, [36, 285, 296, 423], 2.5), 'r-numbered-late-p5-79': (186, [36, 480, 296, 551], 2.5), 'r-numbered-late-e5-34': (182, [312, 60, 572, 155], 2.5), 'r-numbered-late-p5-85': (186, [485, 185, 625, 360], 2.5), 'r-numbered-late-p5-87': (186, [450, 465, 625, 585], 2.5), 'r-numbered-late-p5-89': (187, [75, 60, 296, 195], 2.5), 'r-numbered-late-p5-90': (187, [75, 270, 296, 377], 2.5), 'r-numbered-late-p5-91': (187, [75, 415, 296, 555], 2.5), 'r-numbered-late-p5-92': (187, [204, 560, 330, 662], 2.5), 'r-numbered-late-p5-95': (187, [485, 235, 625, 344], 2.5), 'r-numbered-late-p5-96': (187, [350, 440, 572, 565], 2.5), 'r-numbered-late-p5-97': (187, [485, 570, 625, 730], 2.5), 'r-numbered-late-p5-103': (188, [36, 565, 296, 735], 2.5), 'r-numbered-late-p5-104': (188, [448, 55, 575, 225], 2.5), 'r-numbered-late-p5-107': (188, [445, 370, 575, 550], 2.5), 'r-numbered-late-p5-109': (189, [75, 215, 308, 397], 2.5), 'r-numbered-late-p5-112': (189, [350, 560, 614, 636], 2.5), 'r-numbered-late-p5-114': (190, [170, 55, 296, 240], 2.5), 'r-numbered-late-p5-115': (190, [36, 330, 260, 470], 2.5), 'r-numbered-late-table5-110': (189, [75, 485, 338, 521], 2.5), 'r-numbered-late-table5-111': (189, [352, 60, 616, 205], 2.5)}
def main():
 with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for name,(page,rect,scale) in CROPS.items():
   pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(scale,scale),clip=pymupdf.Rect(rect),alpha=False).save(OUT/(name+'.png'))
 print('Reproduced',len(CROPS),'unchanged source frames.')
if __name__=='__main__':main()
